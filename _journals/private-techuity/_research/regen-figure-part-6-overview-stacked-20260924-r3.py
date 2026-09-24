#!/usr/bin/env python3
"""One-off driver: generate the Part VI (SUSTAIN) chapter overview, round 3.

Part V "SUSTAIN: Keep the Technology You Run Worth Its Cost" was created on
24 September 2026 (posts/part-6-intro). This driver produces its Figure 1 with
the same recipe as the Part IV (SCALE) overview: one stacked column on a 9:16
canvas, one card per row, one group label, explanation lines at exactly the
title size, ochre banner, cropped to content with Pillow (20 px margin).

Round 3 (same day): Part VI SUSTAIN now has FOUR chapters in a new order, so
the overview has FOUR independent cards with NO arrows or connectors between
them, top to bottom: "Build and test resilience", "Critically evaluate cloud
costs", "Critically evaluate AI costs", "Manage technical debt", under the
group label "Four separate questions about the technology you already run".
The two-card round-2 render (sha 770cd55be762) is archived under
_research/discarded-illustration-variants/. Copied from
regen-figure-part-6-overview-stacked-20260924.py; every sizing and legibility
rule is kept (stacked one card per row, 9:16, explanations at title size,
Pillow crop_to_content 20 px, no rail, no arrows). Driven directly through the
illustrator module. Run with python3.11.

Round 3, second pass (same day, edited in place): the chapter order changed
again just after the first r3 render (sha 18bc6938b39d, archived under
_research/discarded-illustration-variants/). "Manage technical debt" now OPENS
the part and frames it, so card 1 is the debt chapter, followed by resilience,
cloud costs and AI costs. The group label above card 1 is now two lines at
title size: "The estate on three columns:" / "cost, risk and speed", and a thin
ochre horizontal rule separates card 1 from cards 2-4. Still no arrows and no
rail; heading, banner and every sizing rule unchanged.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/part-6-intro"

PROMPT = (
    "Create ONE finished editorial framework illustration for the introduction to a part "
    "of OWNED: Product & Engineering Leadership Under Investors. It maps four independent "
    "chapters and their shared purpose; it is not a business scene. Tall portrait 9:16 "
    "composition. Match the book's visual language: warm ivory paper, dark navy text, clean "
    "slightly organic ink outlines, pale muted teal cards, soft ochre highlights, restrained "
    "flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width (side margins no wider than one twentieth of the image), one card per "
    "row, four rows in total, read top to bottom. Never place two cards side by side. "
    "The image will be shown on a narrow phone screen, so ALL lettering must be very "
    "large and the cards must fill the column with little empty space. Sizes: each card "
    "title is bold sans-serif with a cap height of about one sixteenth of the image width; "
    "each explanation line under a title is regular sans-serif at EXACTLY THE SAME SIZE as "
    "the title (only not bold), never smaller, so that the explanation lines are as tall "
    "as the title above them; the group label and the bottom banner use the title size. "
    "Reduce the gaps between cards to the minimum, and shrink the top heading to the "
    "group-label size, to make room for the large lettering. Explanations are broken onto "
    "the short lines given below, one line per line break, left-aligned next to the symbol, "
    "so no line is ever squeezed or shrunk to fit.\n\n"
    "Heading at the top: \"SUSTAIN\".\n\n"
    "One group label, above the first card, in the same size as the card titles, on exactly "
    "two lines: \"The estate on three columns:\" / \"cost, risk and speed\".\n\n"
    "Card 1 title: \"Manage technical debt\"; explanation on two lines: "
    "\"Fund the fix by the cost,\" / \"the risk and the speed it buys\". Small line-drawn "
    "building with scaffolding on one section of it at the left.\n\n"
    "Directly below card 1, a thin horizontal ochre rule across the column, separating "
    "card 1 from the three cards beneath it. The rule is a plain straight line of even "
    "thickness, like a simple horizontal divider or underline, whose two ends simply stop; "
    "it is NOT an arrow and NOT a dimension line: absolutely no arrowhead, triangle, point, "
    "chevron, end cap, tick, serif or vertical bar at either end, no text and no symbols.\n\n"
    "Card 2 title: \"Build and test resilience\"; explanation on two lines: "
    "\"Backups are not enough:\" / \"prove you can restore\". Small line-drawn shield with "
    "a circular restore arrow on it at the left.\n\n"
    "Card 3 title: \"Critically evaluate cloud costs\"; explanation on two lines: "
    "\"A lower bill is not\" / \"always better\". Small line-drawn cloud with a price tag "
    "hanging from it at the left.\n\n"
    "Card 4 title: \"Critically evaluate AI costs\"; explanation on two lines: "
    "\"Measure the return\" / \"per task and per period\". Small line-drawn gauge dial "
    "with a small square microchip beside it at the left.\n\n"
    "The four chapters are independent. Apart from the single thin ochre rule under card 1, "
    "draw NO arrows, NO connectors, NO rail, NO bracket and NO vertical line between or "
    "beside the cards; the cards simply sit one under the other with a small gap. There is "
    "no arrow between any two cards, and none from card 4 into the banner.\n\n"
    "Below card 4, an ochre banner across the bottom with the exact text on two lines: "
    "\"Keep the technology you run\" / \"worth its cost\"; the banner lettering is bold and "
    "at least as large as the card titles.\n\n"
    "Exactly four cards, one two-line group label, one thin arrowless rule, one banner and "
    "zero arrows or arrowheads anywhere; every title appears once; reproduce the supplied words with exact spelling and "
    "add no other words. Symbols must contain no digits, letters, currency signs or percent "
    "signs. No photographs, people, 3D, screens, watermarks, chapter numbers or decorative "
    "clutter. Keep all text inside the image. Do not draw a buyout-to-exit timeline."
)

ALT = (
    "Four chapters stacked under the heading SUSTAIN: Manage technical debt, fund the fix by the "
    "cost, the risk and the speed it buys, framing the part with three columns; then three "
    "applications of one method: Build and test resilience, backups are not enough; Critically "
    "evaluate cloud costs, a lower bill is not always better; Critically evaluate AI costs, measure "
    "the return per task and per period. A final banner reads Keep the technology you run worth its cost."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-6-intro/chapter-overview.jpeg",
        "aspect_ratio": "9:16",
        "prompt": PROMPT,
        "alt": ALT,
    },
]


def crop_to_content(data: bytes, margin: int) -> bytes:
    """Trim the empty ivory paper around the drawn cards so the lettering scales
    larger at a fixed CSS width (same helper as the Part I round-2 driver).
    Requires Pillow (run with python3.11)."""
    import io

    from PIL import Image, ImageChops

    im = Image.open(io.BytesIO(data)).convert("RGB")
    paper = im.getpixel((4, 4))
    diff = ImageChops.difference(im, Image.new("RGB", im.size, paper)).convert("L")
    bbox = diff.point(lambda v: 255 if v > 40 else 0).getbbox()
    if not bbox:
        return data
    left = max(0, bbox[0] - margin)
    top = max(0, bbox[1] - margin)
    right = min(im.width, bbox[2] + margin)
    bottom = min(im.height, bbox[3] + margin)
    cropped = im.crop((left, top, right, bottom))
    buf = io.BytesIO()
    cropped.save(buf, format="JPEG", quality=92, optimize=True)
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--out", default=None, help="Write to this path instead of the asset path.")
    ap.add_argument("--print-prompts", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-retries", type=int, default=4)
    ap.add_argument("--retry-delay-seconds", type=float, default=5.0)
    ap.add_argument("--model", default=gen.DEFAULT_MODEL)
    ap.add_argument("--no-crop", action="store_true", help="Keep Gemini's empty paper margins.")
    ap.add_argument("--crop-margin", type=int, default=20, help="Pixels of paper kept around the content.")
    ap.add_argument("--crop-only", default=None, help="Crop this existing image instead of generating.")
    args = ap.parse_args()

    if args.crop_only:
        src = Path(args.crop_only)
        out = Path(args.out) if args.out else POST / TARGETS[0]["asset"]
        data = crop_to_content(src.read_bytes(), args.crop_margin)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[cropped] {src} -> {out} ({len(data)} bytes)")
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key and not args.dry_run:
        print("GEMINI_API_KEY is not set", file=sys.stderr)
        return 2

    for item in TARGETS:
        if args.only and not any(o in item["id"] for o in args.only):
            continue
        out = Path(args.out) if args.out else POST / item["asset"]
        target = gen.IllustrationTarget(
            post_path=POST / "index.md",
            placeholder_index=1,
            start=0,
            end=0,
            item=item,
            image_path=out,
        )
        if args.print_prompts:
            print(f"--- {item['id']} -> {out}\n{item['prompt']}\n")
        if args.dry_run:
            continue
        data, mime = gen.call_gemini(api_key, args.model, target, args)
        data, _src, mime = gen.normalize_image_bytes_for_target(data, mime, out)
        if not args.no_crop:
            data = crop_to_content(data, args.crop_margin)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
