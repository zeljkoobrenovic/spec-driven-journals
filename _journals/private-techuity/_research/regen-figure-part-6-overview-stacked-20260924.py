#!/usr/bin/env python3
"""One-off driver: generate the Part V (SUSTAIN) chapter overview.

Part V "SUSTAIN: Keep the Technology You Run Worth Its Cost" was created on
24 September 2026 (posts/part-6-intro). This driver produces its Figure 1 with
the same recipe as the Part IV (SCALE) overview: one stacked column on a 9:16
canvas, one card per row, one group label, explanation lines at exactly the
title size, ochre banner, cropped to content with Pillow (20 px margin).

Round 2 (same day): the AI strategy chapter moved to Part III, so the overview
now has TWO independent cards with NO arrows or connectors between them:
"Critically evaluate cloud costs" and "Build and test resilience" under the
group label "Two separate questions about the technology you already run".
The three-card round-1 render (sha d4ef52921d70) is archived under
_research/discarded-illustration-variants/. Copied from
regen-figure-part-5-overview-stacked-20260924.py. Driven directly through the
illustrator module. Run with python3.11.
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
    "of OWNED: Product & Engineering Leadership Under Investors. It maps two independent "
    "chapters and their shared purpose; it is not a business scene. Tall portrait 9:16 "
    "composition. Match the book's visual language: warm ivory paper, dark navy text, clean "
    "slightly organic ink outlines, pale muted teal cards, soft ochre highlights, restrained "
    "flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width (side margins no wider than one twentieth of the image), one card per "
    "row, two rows in total, read top to bottom. Never place two cards side by side. "
    "The image will be shown on a narrow phone screen, so ALL lettering must be very "
    "large and the cards must fill the column with little empty space. Sizes: each card "
    "title is bold sans-serif with a cap height of about one fourteenth of the image width; "
    "each explanation line under a title is regular sans-serif at EXACTLY THE SAME SIZE as "
    "the title (only not bold), never smaller, so that the explanation lines are as tall "
    "as the title above them; the group label and the bottom banner use the title size. "
    "Reduce the gaps between cards to the minimum, and shrink the top heading to the "
    "group-label size, to make room for the large lettering. Explanations are broken onto "
    "the short lines given below, one line per line break, left-aligned next to the symbol, "
    "so no line is ever squeezed or shrunk to fit.\n\n"
    "Heading at the top: \"SUSTAIN\".\n\n"
    "One group label, above the first card, in the same size as the card titles, wrapped "
    "onto as many lines as needed: \"Two separate questions about the technology you "
    "already run\".\n\n"
    "Card 1 title: \"Critically evaluate cloud costs\"; explanation on two lines: "
    "\"A lower bill is not\" / \"always better\". Small line-drawn cloud with a price tag "
    "hanging from it at the left.\n\n"
    "Card 2 title: \"Build and test resilience\"; explanation on two lines: "
    "\"Backups are not enough:\" / \"prove you can restore\". Small line-drawn shield with "
    "a circular restore arrow on it at the left.\n\n"
    "The two chapters are independent. Draw NO arrows, NO connectors, NO rail, NO bracket "
    "and NO vertical line between or beside the cards; the cards simply sit one under the "
    "other with a small gap. There is no arrow between card 1 and card 2, and none from "
    "card 2 into the banner.\n\n"
    "Below card 2, an ochre banner across the bottom with the exact text on two lines: "
    "\"Keep the technology you run\" / \"worth its cost\"; the banner lettering is bold and "
    "at least as large as the card titles.\n\n"
    "Exactly two cards, one group label, one banner and zero arrows; every title appears "
    "once; reproduce the supplied words with exact spelling and add no other words. "
    "Symbols must contain no digits, letters, currency signs or percent signs. No photographs, "
    "people, 3D, screens, watermarks, chapter numbers or decorative clutter. Keep all text "
    "inside the image. Do not draw a buyout-to-exit timeline."
)

ALT = (
    "Two chapters stacked under the heading SUSTAIN, each a separate application of one method: "
    "Critically evaluate cloud costs, a lower bill is not always better; Build and test resilience, "
    "backups are not enough. A final banner reads Keep the technology you run worth its cost."
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
