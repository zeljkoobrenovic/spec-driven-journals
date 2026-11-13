#!/usr/bin/env python3
"""Generate explainer-comic panels from comic-panel blocks in comics.md.

Usage from the repository root:

    python3 .claude/skills/explainer-comics/scripts/generate_comic_panels.py \
        _journals/<journal>/posts/<slug>/comics.md --dry-run --print-prompts

    GEMINI_API_KEY=... python3 .claude/skills/explainer-comics/scripts/generate_comic_panels.py \
        _journals/<journal>/posts/<slug>/comics.md --replace

The script reads one ``<!-- comic-style ... -->`` JSON comment (cast + visual
style, prepended to every panel prompt for cross-panel consistency) and one
``<!-- comic-panel ... -->`` JSON comment per panel, calls the Gemini image
API, writes each image to the source asset path implied by the placeholder,
and can replace completed placeholders with markdown panel figures.

Standard-library-only, same API pattern as the repo's other generators.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

STYLE_START = "<!-- comic-style"
PANEL_START = "<!-- comic-panel"
END = "-->"
REQUIRED_PANEL = {"id", "status", "asset", "aspect_ratio", "prompt", "alt", "caption"}
REQUIRED_STYLE = {"cast", "style"}

DEFAULT_MODEL = "gemini-3-pro-image-preview"
API_URL_TEMPLATE = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent?key={api_key}"
)
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"
JPEG_MIME_TYPES = {"image/jpeg", "image/jpg"}
PNG_MIME_TYPES = {"image/png"}


@dataclass
class PanelTarget:
    comics_path: Path
    panel_index: int
    start: int
    end: int
    item: dict
    image_path: Path
    full_prompt: str

    @property
    def id(self) -> str:
        return str(self.item["id"])

    @property
    def asset(self) -> str:
        return str(self.item["asset"])

    @property
    def aspect_ratio(self) -> str:
        return str(self.item["aspect_ratio"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "comics",
        type=Path,
        help="Path to a post's comics.md file.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini image model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--api-key-env",
        default="GEMINI_API_KEY",
        choices=("GEMINI_API_KEY", "GOOGLE_API_KEY"),
        help="Environment variable containing the Gemini API key.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help=(
            "Only process panels whose id, asset path, or filename matches "
            "this value. Can be provided multiple times."
        ),
    )
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of images to generate.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned work without API calls or writes.")
    parser.add_argument("--print-prompts", action="store_true", help="Print full prompts during dry runs.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate images even when files exist.")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace placeholders with markdown panel figures after image files exist.",
    )
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds to sleep between API calls.")
    parser.add_argument("--max-retries", type=int, default=4, help="Retries for transient API failures.")
    parser.add_argument(
        "--retry-delay-seconds",
        type=float,
        default=5.0,
        help="Base delay for exponential backoff on transient failures.",
    )
    return parser.parse_args(argv)


def post_slug(comics_path: Path) -> str:
    return comics_path.parent.name


def source_image_path(comics_path: Path, asset: str) -> Path:
    slug = post_slug(comics_path)
    expected_prefix = f"assets/images/{slug}/"
    if not asset.startswith(expected_prefix):
        raise ValueError(f"asset must start with {expected_prefix!r}; got {asset!r}")
    return comics_path.parent / "assets" / "images" / slug / Path(asset).name


def replacement_text(item: dict, panel_number: int) -> str:
    return (
        f"![{item['alt']}]({item['asset']})\n"
        f"**Panel {panel_number}:** *{item['caption']}*"
    )


def _extract_blocks(text: str, start_marker: str) -> list[tuple[int, int, str]]:
    pattern = re.compile(
        re.escape(start_marker) + r"\s*(\{.*?\})\s*" + re.escape(END),
        re.DOTALL,
    )
    return [(m.start(), m.end(), m.group(1)) for m in pattern.finditer(text)]


def load_style(comics_path: Path, text: str) -> dict:
    blocks = _extract_blocks(text, STYLE_START)
    if not blocks:
        raise ValueError(f"{comics_path}: no comic-style block found (required, one per file).")
    if len(blocks) > 1:
        raise ValueError(f"{comics_path}: multiple comic-style blocks; keep exactly one.")
    try:
        style = json.loads(blocks[0][2])
    except json.JSONDecodeError as exc:
        raise ValueError(f"{comics_path}: invalid JSON in comic-style block: {exc}") from exc
    missing = sorted(REQUIRED_STYLE - set(style))
    if missing:
        raise ValueError(f"{comics_path}: comic-style block missing fields: {', '.join(missing)}")
    return style


def build_full_prompt(style: dict, panel_prompt: str) -> str:
    return (
        "Recurring cast (keep these characters visually identical in every "
        f"panel): {style['cast']}\n"
        f"Visual style (consistent across the whole strip): {style['style']}\n\n"
        f"{panel_prompt}"
    )


def load_targets(comics_path: Path) -> list[PanelTarget]:
    text = comics_path.read_text(encoding="utf-8")
    style = load_style(comics_path, text)
    targets: list[PanelTarget] = []
    for index, (start, end, raw_json) in enumerate(_extract_blocks(text, PANEL_START), start=1):
        try:
            item = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{comics_path}: invalid JSON in panel {index}: {exc}") from exc
        missing = sorted(REQUIRED_PANEL - set(item))
        if missing:
            raise ValueError(
                f"{comics_path}: panel {index} missing required fields: " + ", ".join(missing)
            )
        targets.append(
            PanelTarget(
                comics_path=comics_path,
                panel_index=index,
                start=start,
                end=end,
                item=item,
                image_path=source_image_path(comics_path, item["asset"]),
                full_prompt=build_full_prompt(style, str(item["prompt"])),
            )
        )
    return targets


def filter_targets(targets: list[PanelTarget], args: argparse.Namespace) -> list[PanelTarget]:
    only = set(args.only or [])
    if only:
        targets = [
            target
            for target in targets
            if target.id in only
            or target.asset in only
            or Path(target.asset).name in only
        ]
    return targets


def detect_image_mime(image_bytes: bytes) -> str:
    if image_bytes.startswith(PNG_SIGNATURE):
        return "image/png"
    if image_bytes.startswith(JPEG_SIGNATURE):
        return "image/jpeg"
    return ""


def convert_with_pillow(image_bytes: bytes, output_format: str) -> bytes | None:
    try:
        from PIL import Image
        import io
    except ImportError:
        return None

    with Image.open(io.BytesIO(image_bytes)) as image:
        output = io.BytesIO()
        if output_format == "JPEG":
            image = image.convert("RGB")
            image.save(output, format=output_format, quality=92)
        else:
            image.save(output, format=output_format)
        return output.getvalue()


def convert_with_sips(image_bytes: bytes, source_suffix: str, output_format: str) -> bytes | None:
    import shutil
    import subprocess
    import tempfile

    if not shutil.which("sips"):
        return None

    target_suffix = ".jpg" if output_format == "jpeg" else ".png"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        src = tmp_dir / f"input{source_suffix}"
        dst = tmp_dir / f"output{target_suffix}"
        src.write_bytes(image_bytes)
        result = subprocess.run(
            ["sips", "-s", "format", output_format, str(src), "--out", str(dst)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not dst.exists():
            return None
        return dst.read_bytes()


def convert_image(image_bytes: bytes, source_mime_type: str, final_mime_type: str) -> bytes:
    if final_mime_type == "image/png":
        converted = convert_with_pillow(image_bytes, "PNG")
        if converted:
            return converted
        converted = convert_with_sips(image_bytes, ".jpg", "png")
        if converted:
            return converted
    if final_mime_type == "image/jpeg":
        converted = convert_with_pillow(image_bytes, "JPEG")
        if converted:
            return converted
        source_suffix = ".png" if source_mime_type == "image/png" else ".jpg"
        converted = convert_with_sips(image_bytes, source_suffix, "jpeg")
        if converted:
            return converted
    raise RuntimeError(
        f"Could not convert {source_mime_type or 'unknown image data'} "
        f"to {final_mime_type}. Install Pillow or run on macOS with sips."
    )


def normalize_image_bytes_for_target(
    image_bytes: bytes, response_mime_type: str, target_path: Path
) -> tuple[bytes, str, str]:
    detected_mime_type = detect_image_mime(image_bytes)
    source_mime_type = (response_mime_type or detected_mime_type or "unknown").lower()
    suffix = target_path.suffix.lower()

    if suffix in {".jpg", ".jpeg"}:
        if detected_mime_type == "image/jpeg" or source_mime_type in JPEG_MIME_TYPES:
            return image_bytes, source_mime_type, "image/jpeg"
        if detected_mime_type == "image/png" or source_mime_type in PNG_MIME_TYPES:
            return convert_image(image_bytes, "image/png", "image/jpeg"), source_mime_type, "image/jpeg"

    if suffix == ".png":
        if detected_mime_type == "image/png" or source_mime_type in PNG_MIME_TYPES:
            return image_bytes, source_mime_type, "image/png"
        if detected_mime_type == "image/jpeg" or source_mime_type in JPEG_MIME_TYPES:
            return convert_image(image_bytes, "image/jpeg", "image/png"), source_mime_type, "image/png"

    return image_bytes, source_mime_type, detected_mime_type or source_mime_type


def extract_image_bytes(payload: dict) -> tuple[bytes, str]:
    candidates = payload.get("candidates") or []
    for candidate in candidates:
        content = (candidate or {}).get("content") or {}
        for part in content.get("parts") or []:
            inline_data = part.get("inlineData") or part.get("inline_data")
            if isinstance(inline_data, dict) and inline_data.get("data"):
                mime_type = inline_data.get("mimeType") or inline_data.get("mime_type") or ""
                return base64.b64decode(inline_data["data"]), mime_type.lower()
    raise RuntimeError(f"Gemini response did not contain image data: {json.dumps(payload)[:1000]}")


def call_gemini(api_key: str, model: str, target: PanelTarget, args: argparse.Namespace) -> tuple[bytes, str]:
    request_url = API_URL_TEMPLATE.format(
        model=urllib.parse.quote(model, safe=""),
        api_key=urllib.parse.quote(api_key, safe=""),
    )
    body = json.dumps(
        {
            "contents": [{"role": "user", "parts": [{"text": target.full_prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": target.aspect_ratio},
            },
        }
    ).encode("utf-8")

    transient_status_codes = {500, 502, 503, 504}
    max_attempts = max(1, int(args.max_retries) + 1)
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        req = urllib.request.Request(
            request_url,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                payload = json.loads(response.read().decode("utf-8"))
            return extract_image_bytes(payload)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"Gemini API error {exc.code}: {detail}")
            if exc.code not in transient_status_codes or attempt == max_attempts:
                raise last_error from exc
        except urllib.error.URLError as exc:
            last_error = RuntimeError(f"Network error while calling Gemini image API: {exc}")
            if attempt == max_attempts:
                raise last_error from exc

        delay = float(args.retry_delay_seconds) * (2 ** (attempt - 1))
        print(f"Transient Gemini failure on attempt {attempt}/{max_attempts}; retrying in {delay:.1f}s")
        time.sleep(delay)

    if last_error:
        raise last_error
    raise RuntimeError("Gemini request failed without a captured error.")


def replace_placeholders(
    comics_path: Path,
    targets: list[PanelTarget],
    dry_run: bool,
    assume_available: bool = False,
) -> int:
    ready = [t for t in targets if assume_available or t.image_path.exists()]
    replaced = 0
    text = comics_path.read_text(encoding="utf-8")
    for target in sorted(ready, key=lambda item: item.start, reverse=True):
        replacement = replacement_text(target.item, target.panel_index)
        if dry_run:
            print(f"would replace panel {target.id} in {comics_path}")
        else:
            text = text[: target.start] + replacement + text[target.end :]
        replaced += 1
    if not dry_run and replaced:
        comics_path.write_text(text, encoding="utf-8")
    return replaced


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.comics.is_file():
        print(f"error: {args.comics} is not a file.", file=sys.stderr)
        return 2

    targets = filter_targets(load_targets(args.comics), args)
    print(f"Discovered {len(targets)} comic panel(s).")

    to_generate = [
        target
        for target in targets
        if args.overwrite or not target.image_path.exists()
    ]
    if args.limit:
        to_generate = to_generate[: args.limit]

    api_key = os.environ.get(args.api_key_env, "").strip()
    if to_generate and not args.dry_run and not api_key:
        print(f"error: {args.api_key_env} environment variable is not set.", file=sys.stderr)
        return 2

    generated = 0
    skipped = 0
    ready_for_replacement: list[PanelTarget] = []

    for index, target in enumerate(targets, start=1):
        rel_image = target.image_path.as_posix()
        exists = target.image_path.exists()
        should_generate = target in to_generate

        if not should_generate:
            if exists:
                print(f"skip existing: {rel_image}")
                skipped += 1
                ready_for_replacement.append(target)
            continue

        if args.dry_run:
            action = "would overwrite" if exists else "would generate"
            print(f"{action}: {rel_image}")
            print(f"  id: {target.id}")
            print(f"  aspect ratio: {target.aspect_ratio}")
            if args.print_prompts:
                print("  prompt:")
                print(target.full_prompt)
            if args.replace:
                ready_for_replacement.append(target)
            continue

        print(f"generating: {rel_image}")
        image_bytes, response_mime_type = call_gemini(api_key, args.model, target, args)
        image_bytes, source_mime_type, final_mime_type = normalize_image_bytes_for_target(
            image_bytes, response_mime_type, target.image_path
        )
        target.image_path.parent.mkdir(parents=True, exist_ok=True)
        target.image_path.write_bytes(image_bytes)
        if source_mime_type != final_mime_type:
            print(f"  normalized: {source_mime_type} -> {final_mime_type}")
        generated += 1
        ready_for_replacement.append(target)
        if args.sleep and generated < len(to_generate) and index < len(targets):
            time.sleep(args.sleep)

    replaced = 0
    if args.replace:
        replaced = replace_placeholders(
            args.comics,
            ready_for_replacement,
            args.dry_run,
            assume_available=args.dry_run,
        )

    print(
        f"Done. Generated {generated} image(s); skipped {skipped} existing image(s); "
        f"replaced {replaced} placeholder(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
