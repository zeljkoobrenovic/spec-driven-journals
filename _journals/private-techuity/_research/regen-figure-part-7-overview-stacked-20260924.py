#!/usr/bin/env python3
"""One-off driver: regenerate the Part VI chapter overview with four cards.

24 September 2026: the LEAD part was renumbered from Part V to Part VI and its
layoff chapter ("Plan layoffs", anatomy-of-a-layoff) moved out to the new Part IV
SCALE. The previous render (742x1341, sha 9e142b419b19..., archived under
_research/discarded-illustration-variants/part-7-intro-chapter-overview-9e142b419b19.jpeg)
still showed five cards. This round keeps the round-2 layout (one stacked column,
two labelled groups, ochre banner, 9:16 canvas cropped with Pillow) and drops
the fifth card: group 2 now holds only "Manage funding delays", followed by a
short dashed teal pointer to a two-line note "Only if a cut is required:" /
"see Plan layoffs (Part IV)". Copied from
regen-figure-part-7-overview-stacked-20260923-r2.py. Driven directly through the
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

POST = ROOT / "_journals/private-techuity/posts/part-7-intro"

PROMPT = (
    "Create ONE finished editorial framework illustration for the introduction to a part "
    "of OWNED: Product & Engineering Leadership Under Investors. It maps four chapters in "
    "two separate groups and their shared purpose; it is not a business scene. Tall "
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
    "as the title above them; the two group labels, the pointer note and the bottom banner "
    "use the title size. Reduce the gaps between cards and the arrows to the minimum, and "
    "shrink the top heading to the group-label size, to make room for the large lettering. "
    "Explanations are broken onto the short lines given below, one line per line break, "
    "left-aligned next to the symbol, so no line is ever squeezed or shrunk to fit.\n\n"
    "Heading at the top: \"LEAD\".\n\n"
    "Group label 1, above the first card, on two lines in the same size as the card titles: "
    "\"Follow a customer setup problem\" / \"Some setups depend on one specialist\".\n"
    "Card 1 title: \"Use diligence\"; explanation on two lines: \"Check the business\" / "
    "\"before the deal is signed\". Small line-drawn magnifying glass over a document at the left.\n"
    "A short solid teal downward arrow links card 1 to card 2.\n"
    "Card 2 title: \"Plan the first hundred days\"; explanation on two lines: "
    "\"Fund the work\" / \"and review the finding\". Small line-drawn calendar with a tick at the left.\n"
    "A short solid teal downward arrow links card 2 to card 3.\n"
    "Card 3 title: \"Manage the handover\"; explanation on two lines: \"Pass on the evidence\" / "
    "\"and unfinished promises\". Small line-drawn folder passed between two hands at the left.\n"
    "Do not draw any vertical line, bracket or rail along the edge of the cards; the arrows "
    "alone connect card 1 to card 2 and card 2 to card 3.\n\n"
    "Below card 3 leave a clear gap with a fine horizontal ochre rule across the column, so the "
    "second group is visibly separate. There must be NO arrow from card 3 into the second group.\n\n"
    "Group label 2, above the fourth card: \"Separate funding-delay scenario\".\n"
    "Card 4 title: \"Manage funding delays\"; explanation on two lines: \"Expected money is late:\" / "
    "\"replan payments and promised work\". Small line-drawn hourglass beside coins at the left.\n"
    "Below card 4 there is NO fifth card. Instead a SHORT DASHED teal downward pointer leads "
    "from card 4 to a small note written in the title size on two lines, with no box around it: "
    "\"Only if a cut is required:\" / \"see Plan layoffs (Part IV)\". The note sits in the gap "
    "under card 4 and does not overlap the card or the banner. This is conditional: a delay "
    "does not always lead to a cut, and the layoff chapter lives in another part of the book.\n\n"
    "A short solid teal downward arrow leads from the note into an ochre banner across the bottom "
    "with the exact text on two lines: \"Account for decisions, evidence\" / \"and promises through change\"; "
    "the banner lettering is bold and at least as large as the card titles. Arrows never cross text.\n\n"
    "Exactly four cards, two group labels (the first on two lines), one dashed pointer with its two-line note and one banner; every "
    "title appears once; reproduce the supplied words with exact spelling and add no other words. "
    "Symbols must contain no digits, letters, currency signs or percent signs. No photographs, "
    "people, 3D, screens, watermarks, chapter numbers or decorative clutter. Keep all text and "
    "arrowheads inside the image. Do not draw a buyout-to-exit timeline."
)

ALT = (
    "Four chapters stacked in one column under the heading LEAD. Group one, Follow a customer setup "
    "problem, where some setups depend on one specialist: Use diligence (check the business before the "
    "deal is signed) leads to Plan the first hundred days (fund the work and review the finding), which "
    "leads to Manage the handover (pass on the evidence and unfinished promises). Group two, Separate "
    "funding-delay scenario: Manage funding delays (expected money is late: replan payments and promised "
    "work), with a dashed pointer labelled Only if a cut is required, see Plan layoffs in Part IV. A final "
    "banner reads Account for decisions, evidence and promises through change."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-7-intro/chapter-overview.jpeg",
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
