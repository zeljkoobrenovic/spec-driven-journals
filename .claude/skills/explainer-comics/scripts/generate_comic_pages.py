#!/usr/bin/env python3
"""Generate explainer-comic PAGES from comic-page blocks in comics.md.

A comic page is one image made of two or three stacked strips. The dialogue,
short labels and amounts are lettered in the artwork, so the picture explains
the beat by itself and the caption under it stays short.

Usage from the repository root:

    # check the script, rewrite the visible figures/captions/transcripts from the blocks
    python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
        _journals/<journal>/posts/<slug>/comics.md --render --print-prompts

    # generate missing page images (costs money), then render
    GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
        _journals/<journal>/posts/<slug>/comics.md --generate [--only <page-id>] [--overwrite]

    # small corrections on an accepted page, keeping its artwork: one lettered string, or one stray detail
    GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
        _journals/<journal>/posts/<slug>/comics.md --only <page-id> --retext "old words" "new words"
    GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_pages.py \
        _journals/<journal>/posts/<slug>/comics.md --only <page-id> --edit "Remove the dollar sign from the money bag."

comics.md is the single source of truth: one ``<!-- comic-style ... -->`` block,
an optional intro paragraph, then one ``<!-- comic-page ... -->`` block per page.
Everything visible under a page block (image, caption, transcript) is rendered
from the block; edit the block, never the rendered lines.

Standard-library-only. Reuses the image helpers of generate_comic_panels.py,
which remains the generator for legacy single-panel comics.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_comic_panels as panels  # noqa: E402  (shared block parsing and image normalization)

PAGE_START = "<!-- comic-page"
REQUIRED_PAGE = {"id", "title", "asset", "strips", "alt", "caption"}
DEFAULT_ASPECT = "3:4"
POSITIONS = {2: ["top", "bottom"], 3: ["top", "middle", "bottom"]}
MAX_BUBBLE_WORDS = 14
MAX_LABEL_WORDS = 5
MAX_NARRATION_WORDS = 14
MAX_BUBBLES_PER_STRIP = 2


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("comics", type=Path, help="Path to a post's comics.md file.")
    parser.add_argument("--render", action="store_true", help="Rewrite the visible figures, captions and transcripts from the blocks.")
    parser.add_argument("--generate", action="store_true", help="Call the image API for pages without an image (implies --render).")
    parser.add_argument("--retext", nargs=2, metavar=("OLD", "NEW"), help="With one --only page: replace one lettered string on the existing image, keeping the artwork.")
    parser.add_argument("--edit", metavar="INSTRUCTION", help="With one --only page: apply one small correction to the existing image (remove a stray symbol, uncover a label), keeping the rest of the artwork.")
    parser.add_argument("--only", action="append", default=[], help="Only process pages whose id matches. Can be repeated.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate images even when files exist (the old image is archived).")
    parser.add_argument("--print-prompts", action="store_true", help="Print the full prompt of each selected page.")
    parser.add_argument("--archive-dir", type=Path, help="Where replaced images go (default: <journal>/_research/discarded-comic-variants/).")
    parser.add_argument("--model", default=panels.DEFAULT_MODEL)
    parser.add_argument("--api-key-env", default="GEMINI_API_KEY", choices=("GEMINI_API_KEY", "GOOGLE_API_KEY"))
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds to sleep between API calls.")
    return parser.parse_args(argv)


def journal_dir(comics_path: Path) -> Path:
    return comics_path.resolve().parents[2]  # _journals/<journal>/posts/<slug>/comics.md


def load(comics_path: Path) -> tuple[str, dict, str, list[dict]]:
    """Return (style block text, style, intro, pages)."""
    text = comics_path.read_text(encoding="utf-8")
    style = panels.load_style(comics_path, text)
    style_start, style_end, _ = panels._extract_blocks(text, panels.STYLE_START)[0]
    blocks = panels._extract_blocks(text, PAGE_START)
    if not blocks:
        raise ValueError(f"{comics_path}: no comic-page blocks found.")
    if panels._extract_blocks(text, panels.PANEL_START):
        raise ValueError(f"{comics_path}: mixes comic-panel and comic-page blocks; convert the panels or use generate_comic_panels.py.")
    pages = []
    for index, (_, _, raw) in enumerate(blocks, start=1):
        try:
            pages.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{comics_path}: invalid JSON in page {index}: {exc}") from exc
    intro = text[style_end:blocks[0][0]].strip()
    return text[style_start:style_end], style, intro, pages


def check(comics_path: Path, style: dict, pages: list[dict]) -> list[str]:
    problems = []
    seen = set()
    identity = style.get("identity") or {}
    for index, page in enumerate(pages, start=1):
        missing = sorted(REQUIRED_PAGE - set(page))
        if missing:
            problems.append(f"page {index}: missing fields: {', '.join(missing)}")
            continue
        where = page["id"]
        if not re.match(r"^\d\d-[a-z0-9-]+$", where):
            problems.append(f"{where}: id must be NN-kebab-case")
        if where in seen:
            problems.append(f"{where}: duplicate id")
        seen.add(where)
        try:
            panels.source_image_path(comics_path, page["asset"])
        except ValueError as exc:
            problems.append(f"{where}: {exc}")
        if len(page["strips"]) not in POSITIONS:
            problems.append(f"{where}: {len(page['strips'])} strips (use 2 or 3)")
        for name in page.get("cast", []):
            if identity and name not in identity:
                problems.append(f"{where}: cast member {name} has no entry in the style block's identity map")
        for n, strip in enumerate(page["strips"], start=1):
            spot = f"{where} strip {n}"
            if not strip.get("scene"):
                problems.append(f"{spot}: no scene")
            bubbles = strip.get("bubbles", [])
            if len(bubbles) > MAX_BUBBLES_PER_STRIP:
                problems.append(f"{spot}: {len(bubbles)} bubbles (max {MAX_BUBBLES_PER_STRIP})")
            for bubble in bubbles:
                if page.get("cast") and bubble["who"] not in page["cast"]:
                    problems.append(f"{spot}: {bubble['who']} speaks but is not in the page cast")
                if len(bubble["text"].split()) > MAX_BUBBLE_WORDS:
                    problems.append(f"{spot}: bubble over {MAX_BUBBLE_WORDS} words: {bubble['text']}")
            for label in strip.get("labels", []):
                if len(label.split()) > MAX_LABEL_WORDS:
                    problems.append(f"{spot}: label over {MAX_LABEL_WORDS} words: {label}")
            if len(strip.get("narration", "").split()) > MAX_NARRATION_WORDS:
                problems.append(f"{spot}: narration over {MAX_NARRATION_WORDS} words")
    return problems


def expected_text(page: dict) -> list[str]:
    """Every string that must appear in the image, in reading order: the list to verify the artwork against."""
    out = []
    for strip in page["strips"]:
        if strip.get("narration"):
            out.append(strip["narration"])
        out += [bubble["text"] for bubble in strip.get("bubbles", [])]
        out += strip.get("labels", [])
    return out


def build_prompt(style: dict, page: dict) -> str:
    strips = page["strips"]
    count = len(strips)
    identity = style.get("identity") or {}
    cast = page.get("cast", [])
    lines = [
        f"Draw ONE finished comic PAGE, portrait {page.get('aspect_ratio', DEFAULT_ASPECT)}, made of exactly {count} "
        "full-width horizontal strips stacked top to bottom, read from top to bottom. Each strip has a thin dark "
        "border; clean light gutters separate the strips.",
        f"Visual style (consistent across the whole comic): {style['style']}",
        f"Recurring cast (keep these characters visually identical in every strip and page): {style['cast']}",
    ]
    if style.get("reference"):
        lines.append(
            "The attached image is a character-design reference only. Reuse the matching named characters, their "
            "faces, hair, skin tone and clothing colors; do not reproduce the reference-sheet layout."
        )
    if cast:
        lines.append("Characters on this page: " + ", ".join(cast) + ". Do not draw cast members that a strip does not mention.")
    lines += ["Any other people the scenes ask for are unnamed, wear plain grey clothes and do not resemble the cast.", ""]
    for n, strip in enumerate(strips, start=1):
        lines.append(f"STRIP {n} ({POSITIONS[count][n - 1]}). Scene: {strip['scene']}")
        if strip.get("narration"):
            lines.append(f'  Narration box (small pale rectangle in the top-left corner of this strip), exact words: "{strip["narration"]}"')
        for bubble in strip.get("bubbles", []):
            lines.append(f'  Speech bubble, tail pointing to {bubble["who"].upper()}, exact words: "{bubble["text"]}"')
        if strip.get("labels"):
            lines.append("  Printed labels on props, exact text: " + " | ".join(f'"{label}"' for label in strip["labels"]))
            if strip.get("label_notes"):
                lines.append("  Label placement: " + strip["label_notes"])
        lines.append("")
    lines += [
        "LETTERING RULES. All lettering is large, high-contrast, clean sans-serif comic lettering that stays readable "
        "when the page is shown 400 pixels wide. Spell every string exactly as supplied, including currency signs, "
        "minus and plus signs, percent signs and decimal points, and print each string in its own strip, as many times "
        "as it is listed there and no more. Within a strip, place speech bubbles in reading order, left to right, in "
        "clear space above heads, and stand the speakers left to right in that same order so that each tail reaches "
        "its own speaker without crossing; never cover a face or a printed label with a bubble or a hand; keep bubbles "
        "and tails inside the strip. Print NO other text anywhere: no character names, strip numbers, page title, "
        "caption, watermark, and no amounts, dates or percentages other than the supplied ones. Leave other documents "
        "and screens as blank lines.",
        "Where sizes or counts are compared (stacks, boxes, slips), make the differences obvious and in the stated order.",
        "Meaning to convey, not text to print: " + page["caption"],
        "FINAL CHECKS. Character identity in every strip: "
        + (" ".join(identity[name] for name in cast if name in identity) or style["cast"])
        + " Draw a narration box only in a strip that supplies narration words; never invent narration, location "
        "captions or any other wording.",
    ]
    return "\n".join(lines)


def call_image(api_key: str, model: str, prompt: str, aspect_ratio: str, image: bytes | None) -> tuple[bytes, str]:
    parts: list[dict] = [{"text": prompt}]
    if image:
        mime = panels.detect_image_mime(image) or "image/jpeg"
        parts.append({"inline_data": {"mime_type": mime, "data": base64.b64encode(image).decode()}})
    body = json.dumps({
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect_ratio, "imageSize": "2K"}},
    }).encode("utf-8")
    url = "https://generativelanguage.googleapis.com/v1beta/models/" + urllib.parse.quote(model, safe="") + ":generateContent"
    for attempt in range(4):
        request = urllib.request.Request(url, data=body, method="POST",
                                         headers={"Content-Type": "application/json", "x-goog-api-key": api_key})
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                return panels.extract_image_bytes(json.loads(response.read().decode("utf-8")))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise RuntimeError(f"Gemini API error {exc.code}: {detail[:700]}") from None
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                raise RuntimeError(f"Network error while calling Gemini image API: {exc}") from None
        time.sleep(5 * (2 ** attempt))
    raise RuntimeError("Image request exhausted retries.")


def archive(image_path: Path, comics_path: Path, archive_dir: Path | None) -> None:
    """Never destroy an accepted image silently: keep the replaced bytes."""
    if not image_path.exists():
        return
    data = image_path.read_bytes()
    research = journal_dir(comics_path) / "_research"
    target_dir = archive_dir or (research / "discarded-comic-variants" if research.is_dir() else image_path.parent / "discarded")
    target_dir.mkdir(parents=True, exist_ok=True)
    name = f"{panels.post_slug(comics_path)}-{image_path.stem}-{hashlib.sha256(data).hexdigest()[:12]}{image_path.suffix}"
    (target_dir / name).write_bytes(data)


def render(comics_path: Path, style_block: str, intro: str, pages: list[dict]) -> None:
    out = [style_block, ""]
    if intro:
        out += [intro, ""]
    for number, page in enumerate(pages, start=1):
        image_path = panels.source_image_path(comics_path, page["asset"])
        page = dict(page)
        page["status"] = "generated" if image_path.exists() else "pending"
        if image_path.exists():
            generation = dict(page.get("generation") or {})
            generation["sha256"] = hashlib.sha256(image_path.read_bytes()).hexdigest()
            page["generation"] = generation
        else:
            page.pop("generation", None)
        out += [PAGE_START + "\n" + json.dumps(page, ensure_ascii=False, indent=2) + "\n" + panels.END, ""]
        if image_path.exists():
            out += [f"![{page['alt']}]({page['asset']})", ""]
        out += [f"**Page {number}: {page['title']}.** {page['caption']}", ""]
        # The transcript keeps the dialogue readable independently of the image text.
        for n, strip in enumerate(page["strips"], start=1):
            parts = [f"*Narration:* {strip['narration']}"] if strip.get("narration") else []
            parts += [f"**{bubble['who']}:** “{bubble['text']}”" for bubble in strip.get("bubbles", [])]
            out.append(f"- *Strip {n}.* " + " ".join(parts))
        out.append("")
    comics_path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.comics.is_file():
        print(f"error: {args.comics} is not a file.", file=sys.stderr)
        return 2
    try:
        style_block, style, intro, pages = load(args.comics)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    problems = check(args.comics, style, pages)
    for problem in problems:
        print(f"[check] {problem}")
    if problems:
        return 1

    selected = [page for page in pages if not args.only or page["id"] in args.only]
    print(f"Discovered {len(pages)} comic page(s), {sum(len(p['strips']) for p in pages)} strips; selected {len(selected)}.")
    if args.print_prompts:
        for page in selected:
            print(f"===== {page['id']} =====\n{build_prompt(style, page)}\n--- text to verify in the image:")
            for string in expected_text(page):
                print(f"    {string}")
            print()

    needs_api = args.generate or args.retext or args.edit
    api_key = os.environ.get(args.api_key_env, "").strip()
    if needs_api and not api_key:
        print(f"error: {args.api_key_env} environment variable is not set.", file=sys.stderr)
        return 2
    reference = None
    if style.get("reference"):
        reference_path = journal_dir(args.comics) / style["reference"]
        if not reference_path.is_file():
            print(f"error: cast reference {reference_path} not found.", file=sys.stderr)
            return 2
        reference = reference_path.read_bytes()

    if args.retext:
        if len(selected) != 1:
            print("error: --retext needs exactly one --only page.", file=sys.stderr)
            return 2
        page = selected[0]
        image_path = panels.source_image_path(args.comics, page["asset"])
        old, new = args.retext
        if new not in expected_text(page):
            print("error: put the new words into the page block first; --retext makes the image match the block.", file=sys.stderr)
            return 2
        prompt = (
            "Edit the attached comic page. Change ONLY one piece of lettering: replace the exact words "
            f'"{old}" with the exact words "{new}", in the same box, same lettering style and size, resizing that box '
            "only as much as the new words need. Keep every other pixel of the page as it is: the same drawings, "
            "people, faces, colors, strips, borders, speech bubbles, labels and all other text. Add nothing else."
        )
        data, mime = call_image(api_key, args.model, prompt, page.get("aspect_ratio", DEFAULT_ASPECT), image_path.read_bytes())
        data, _, _ = panels.normalize_image_bytes_for_target(data, mime, image_path)
        archive(image_path, args.comics, args.archive_dir)
        image_path.write_bytes(data)
        print(f"retexted: {image_path}")

    if args.edit:
        if len(selected) != 1:
            print("error: --edit needs exactly one --only page.", file=sys.stderr)
            return 2
        page = selected[0]
        image_path = panels.source_image_path(args.comics, page["asset"])
        prompt = (
            f"Edit the attached comic page. Make ONLY this correction: {args.edit} Keep every other pixel of the page "
            "as it is: the same drawings, people, faces, colors, strips, borders, speech bubbles, labels and all "
            "other text. Add no new text."
        )
        data, mime = call_image(api_key, args.model, prompt, page.get("aspect_ratio", DEFAULT_ASPECT), image_path.read_bytes())
        data, _, _ = panels.normalize_image_bytes_for_target(data, mime, image_path)
        archive(image_path, args.comics, args.archive_dir)
        image_path.write_bytes(data)
        print(f"edited: {image_path}")

    generated = 0
    if args.generate:
        for page in selected:
            image_path = panels.source_image_path(args.comics, page["asset"])
            if image_path.exists() and not args.overwrite:
                print(f"skip existing: {image_path}")
                continue
            print(f"generating: {image_path}")
            data, mime = call_image(api_key, args.model, build_prompt(style, page), page.get("aspect_ratio", DEFAULT_ASPECT), reference)
            data, _, _ = panels.normalize_image_bytes_for_target(data, mime, image_path)
            archive(image_path, args.comics, args.archive_dir)
            image_path.parent.mkdir(parents=True, exist_ok=True)
            image_path.write_bytes(data)
            page["generation"] = {"model": args.model, **({"reference": style["reference"]} if style.get("reference") else {})}
            generated += 1
            if args.sleep:
                time.sleep(args.sleep)

    if args.render or args.generate or args.retext or args.edit:
        render(args.comics, style_block, intro, pages)
        print(f"rendered: {args.comics}")
    print(f"Done. Generated {generated} image(s). Inspect every new image against its text-to-verify list before accepting it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
