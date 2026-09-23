#!/usr/bin/env python3
"""One-off driver: regenerate the Part I chapter overview, round 2.

In-depth review 23 September 2026, round 2, findings P1-002 and P1-003: the
round-1 stacked 3:4 overview (sha 67f2bb10...) still rendered its subtitles at
roughly 10-11 CSS pixels inside a 375-pixel phone viewport (327 px content
width), and its first card only said "What each source expects" without saying
what customers, lenders and investors are. This version keeps the six cards,
the three stage labels and the purpose banner, but uses a taller 9:16 canvas,
wraps every explanation onto short lines, asks for explanation lettering nearly
as large as the titles, and lets the first card name what each party expects.
Driven directly through the illustrator module, as in
regen-figure-part-1-overview-20260923.py (round 1). Run with python3.11 (the
content crop needs Pillow).

Outcome: three renders. The second (raw sha 52e1b1f5..., 768x1376) was accepted
after crop_to_content(margin=20) -> 646x1285, sha 2c962e03...; the first and
third are archived under _research/discarded-illustration-variants/ as
part-1-intro-chapter-overview-51856afb6ea8.jpeg and ...-10fbe0ee44f0.jpeg.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/part-1-intro"

PROMPT = (
    "Create ONE finished editorial framework illustration for the introduction to a part "
    "of OWNED: Product & Engineering Leadership Under Investors. It maps six chapters, "
    "their reading order and their shared purpose; it is not a business scene. Tall "
    "portrait 9:16 composition. Match the book's visual language: warm ivory paper, dark "
    "navy text, clean slightly organic ink outlines, pale muted teal cards, soft ochre "
    "highlights, restrained flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width (side margins no wider than one twentieth of the image), one card per "
    "row, six rows in total, read top to bottom. Never place two cards side by side. "
    "The image will be shown on a narrow phone screen, so ALL lettering must be very "
    "large and the cards must fill the column with little empty space. Sizes: each card "
    "title is bold sans-serif with a cap height of about one fourteenth of the image width; "
    "each explanation line under a title is regular sans-serif at EXACTLY THE SAME SIZE as "
    "the title (only not bold), never smaller, so that the explanation lines are as tall "
    "as the title above them; the stage labels and the bottom banner use the title size. "
    "Reduce the gaps between cards and the arrows to the minimum, and shrink the top "
    "heading to the stage-label size, to make room for the large lettering. Explanations "
    "are broken "
    "onto the short lines given below, one line per line break, left-aligned next to the "
    "symbol, so no line is ever squeezed or shrunk to fit.\n\n"
    "Heading at the top: \"UNDERSTAND\".\n\n"
    "Stage label 1: \"Trace money and control\".\n"
    "Card 1 title: \"Customers, lenders, investors\"; explanation on three lines: "
    "\"Customers pay for what they buy\" / \"Lenders must be repaid\" / "
    "\"Investors hope for a gain\". Small line-drawn ledger-and-coins symbol at the left.\n"
    "Card 2 title: \"Funding and control\"; explanation on two lines: "
    "\"Who receives money\" / \"and approves spending\". Small line-drawn approval-stamp "
    "symbol at the left.\n\n"
    "Stage label 2: \"Interpret value and returns\".\n"
    "Card 3 title: \"Valuation\"; explanation on two lines: \"Estimating what\" / "
    "\"a business is worth\". Small line-drawn magnifying glass over a small building.\n"
    "Card 4 title: \"Investor returns\"; explanation on two lines: \"Gains or losses\" / "
    "\"on invested money\". Small line-drawn symbol of three branching arrows, one up, "
    "one level, one down.\n\n"
    "Stage label 3: \"Confirm funding for the work\".\n"
    "Card 5 title: \"Funding choices\"; explanation on two lines: \"Match the money\" / "
    "\"to the work\". Small line-drawn two-piece jigsaw symbol.\n"
    "Card 6 title: \"Cash flow\"; explanation on two lines: \"Money coming in\" / "
    "\"and going out\". Small line-drawn calendar with coins symbol.\n\n"
    "A short teal downward arrow links each card to the next, and a final arrow leads from "
    "card 6 into an ochre banner across the bottom with the exact text on two lines: "
    "\"Know what can fund\" / \"a commitment to do the work\"; the banner lettering is bold "
    "and at least as large as the card titles. Arrows never cross text.\n\n"
    "Exactly six cards; every title appears once; reproduce the supplied words with exact "
    "spelling and add no other words. Symbols must contain no digits, letters, currency "
    "signs or percent signs. No photographs, people, 3D, screens, watermarks, chapter "
    "numbers or decorative clutter. Keep all text and arrowheads inside the image."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-1-intro/chapter-overview.jpeg",
        "aspect_ratio": "9:16",
        "prompt": PROMPT,
        "alt": "Six chapters stacked in three stages. Trace money and control: Customers, lenders, investors (customers pay for what they buy, lenders must be repaid, investors hope for a gain) leads to Funding and control (who receives money and approves spending). Interpret value and returns: Valuation (estimating what a business is worth) leads to Investor returns (gains or losses on invested money). Confirm funding for the work: Funding choices (match the money to the work) leads to Cash flow (money coming in and going out). A final banner reads Know what can fund a commitment to do the work.",
    },
]


def crop_to_content(data: bytes, margin: int) -> bytes:
    """Trim the empty ivory paper around the drawn cards so the lettering scales
    larger at a fixed CSS width. Gemini leaves roughly a tenth of the width empty
    on each side; at 327 CSS pixels that margin alone costs about 2 pixels of
    letter height. Requires Pillow (run with python3.11)."""
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
