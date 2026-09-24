#!/usr/bin/env python3
"""One-off driver: generate the Part IV (SCALE) chapter overview.

Part IV "SCALE: Change the Team, the Systems and the Company Deliberately" was
created on 24 September 2026 (posts/part-5-intro). This driver produces its
Figure 1 with the same recipe as the Part V (LEAD) round-2 overview: one stacked
column on a 9:16 canvas, one card per row, three labelled groups, explanation
lines at exactly the title size, ochre banner, cropped to content with Pillow
(20 px margin). Four cards: "Scale the team up" and "Scale the team down"
under "Change the team" (joined by one short teal arrow), "Plan for growth"
under "Change the systems", and "Plan acquisitions and separations" under
"Change the company's boundary". No rail, bracket or arrow crosses a group
boundary. Copied from regen-figure-part-7-overview-stacked-20260923-r2.py.
Driven directly through the illustrator module. Run with python3.11.
Revised 24 September 2026 (team chapters retitled): card 1 became "Scale the team up"
/ "Headcount is not capacity" / "Trace the work before hiring", card 2 became "Scale the
team down"; round-1 render 03408a8a7595 archived.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/part-5-intro"

PROMPT = (
    "Create ONE finished editorial framework illustration for the introduction to a part "
    "of OWNED: Product & Engineering Leadership Under Investors. It maps four chapters in "
    "three separate groups and their shared purpose; it is not a business scene. Tall "
    "portrait 9:16 composition. Match the book's visual language: warm ivory paper, dark "
    "navy text, clean slightly organic ink outlines, pale muted teal cards, soft ochre "
    "highlights, restrained flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width (side margins no wider than one twentieth of the image), one card per "
    "row, four rows in total, read top to bottom. Never place two cards side by side. "
    "The image will be shown on a narrow phone screen, so ALL lettering must be very "
    "large and the cards must fill the column with little empty space. Sizes: each card "
    "title is bold sans-serif with a cap height of about one fourteenth of the image width; "
    "each explanation line under a title is regular sans-serif at EXACTLY THE SAME SIZE as "
    "the title (only not bold), never smaller, so that the explanation lines are as tall "
    "as the title above them; the three group labels, and the bottom banner "
    "use the title size. Reduce the gaps between cards and the arrow to the minimum, and "
    "shrink the top heading to the group-label size, to make room for the large lettering. "
    "Explanations are broken onto the short lines given below, one line per line break, "
    "left-aligned next to the symbol, so no line is ever squeezed or shrunk to fit.\n\n"
    "Heading at the top: \"SCALE\".\n\n"
    "Group label 1, above the first card, in the same size as the card titles: "
    "\"Change the team\".\n"
    "Card 1 title: \"Scale the team up\"; explanation on two lines: "
    "\"Headcount is not capacity\" / \"Trace the work before hiring\". Small line-drawn "
    "organisation chart with a magnifying glass over it at the left.\n"
    "A short solid teal downward arrow links card 1 to card 2. This is the ONLY arrow "
    "between cards in the whole image.\n"
    "Card 2 title: \"Scale the team down\"; explanation on two lines: \"Decide what work stops,\" / "
    "\"then who leaves\". Small line-drawn list with one row crossed out at the left; "
    "no people.\n\n"
    "Below card 2 leave a clear gap with a fine horizontal ochre rule across the column, so the "
    "second group is visibly separate. There must be NO arrow from card 2 into the second group.\n\n"
    "Group label 2, above the third card: \"Change the systems\".\n"
    "Card 3 title: \"Plan for growth\"; explanation on two lines: \"Choose which system change\" / "
    "\"and how to fund it\". Small line-drawn stack of blocks with one block being swapped "
    "out at the left.\n\n"
    "Below card 3 leave a clear gap with a second fine horizontal ochre rule across the column, "
    "so the third group is visibly separate. There must be NO arrow from card 3 into the third group.\n\n"
    "Group label 3, above the fourth card: \"Change the company's boundary\".\n"
    "Card 4 title: \"Plan acquisitions and separations\"; explanation on two lines: "
    "\"Account for the extra work\" / \"a new boundary adds\". Small line-drawn dotted "
    "boundary around two buildings at the left.\n\n"
    "Do not draw any vertical line, bracket or rail along the edge of the cards, and no "
    "connector of any kind between the groups; the single teal arrow between card 1 and "
    "card 2 is the only connector between cards.\n\n"
    "A short solid teal downward arrow leads from card 4 into an ochre banner across the bottom "
    "with the exact text on three lines: \"Change size deliberately,\" / \"fund the transition,\" / "
    "\"keep the customer promise\"; "
    "the banner lettering is bold and at least as large as the card titles. Arrows never cross text.\n\n"
    "Exactly four cards, three group labels, two ochre rules, one arrow between cards and one banner; every "
    "title appears once; reproduce the supplied words with exact spelling and add no other words. "
    "Symbols must contain no digits, letters, currency signs or percent signs. No photographs, "
    "people, 3D, screens, watermarks, chapter numbers or decorative clutter. Keep all text and "
    "arrowheads inside the image. Do not draw a buyout-to-exit timeline."
)

ALT = (
    'Four chapters in three groups under the heading SCALE. Group one, change the team: scale the team up only after tracing the work, because headcount is not capacity; then scale the team down by deciding what work stops before deciding who leaves. Group two, change the systems: plan for growth by choosing which system change to make and how to fund it. Group three, change the company’s boundary: plan acquisitions and separations by accounting for the extra work a new boundary adds. A final banner reads change size deliberately, fund the transition, keep the customer promise.'
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-5-intro/chapter-overview.jpeg",
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
