#!/usr/bin/env python3
"""One-off driver: regenerate the Part VI chapter overview (Figure 1 of part-6-intro)
as a stacked column with self-contained labels.

In-depth review 23 September 2026, finding P6-003: the 22 September 4:3 render
(part-overview-images-20260922.json) used specialist shorthand a newcomer cannot
follow ("Check continuity of money", "Explain the successful exit", "Test the cash
behind earnings", "Evidence -> possible mechanism -> leadership decision"), and its
two-column card grid left the subtitles at roughly 6 CSS pixels on a phone. This
version keeps the same structure (four independent case cards with no arrows
between them, one shared reading method, the closing chapter, one ochre banner)
but stacks the cards one per row, states each case's question in ordinary words,
writes the method line in plain verbs, and asks for explanation lines at title
size, as the Part I and Part II overviews were regenerated earlier the same day.
Driven directly through the illustrator module; the raw render is cropped to its
drawn content with Pillow (run the --crop step with python3.11).
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
    "of OWNED: Product & Engineering Leadership Under Investors. It maps five chapters, "
    "their reading connections and their shared purpose; it is not a business scene. Tall "
    "portrait 9:16 composition. Match the book's visual language: warm ivory paper, dark "
    "navy text, clean slightly organic ink outlines, pale muted teal cards, soft ochre "
    "highlights, restrained flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width (side margins no wider than one twentieth of the image), one card per "
    "row, read top to bottom. Never place two cards side by side. The image will be shown "
    "on a narrow phone screen, so all lettering must be very large: each card title is "
    "bold and about one eighteenth of the image width in cap height, and every explanation "
    "line is set at EXACTLY the same size as the title, in regular weight, wrapped onto "
    "short lines of at most five words so it never shrinks. Fill the column; do not leave "
    "empty paper above or below the drawing. No frame, border or ruled lines around the "
    "composition.\n\n"
    "Heading at the top: \"LEARN\".\n"
    "Small group label under the heading: \"Four independent case chapters\".\n\n"
    "Card 1 title: \"Hilton and Skype\"; explanation: \"Explain the investors' successful sale\". "
    "Small line-drawn open book at the left of the card.\n"
    "Card 2 title: \"Visma\"; explanation: \"Which investors paid, and which received money?\" "
    "Small line-drawn magnifying glass at the left of the card.\n"
    "Card 3 title: \"Toys R Us\"; explanation: \"Why did reported profit leave so little cash?\" "
    "Small line-drawn stack of coins at the left of the card.\n"
    "Card 4 title: \"TeamSystem\"; explanation: \"What commitments pass to each new owner?\" "
    "Small line-drawn chain link at the left of the card.\n"
    "There are NO arrows between these four cards: the histories do not cause one another. "
    "Instead, one fine navy bracket runs down the right margin beside all four cards and "
    "turns inward beneath card 4 into a single downward arrow.\n\n"
    "That arrow points to one unboxed reading-method line in bold navy lettering, the same "
    "size as the card titles, written on three short lines: \"What happened\", "
    "\"What might explain it\", \"What a leader could change\", with a small navy arrow "
    "between the lines.\n\n"
    "A short teal downward arrow leads from the method to card 5, which is slightly taller "
    "and is the only card with a soft ochre edge. Card 5 title: \"Success for whom, and for "
    "how long?\"; explanation: \"Who gained, who paid, what can the company still do?\" "
    "Small line-drawn balance scale at the left of the card.\n\n"
    "A short teal downward arrow leads from card 5 into an ochre banner across the bottom "
    "with the exact text: \"Make judgments the evidence supports\". Arrows never cross text.\n\n"
    "Exactly five cards, one bracket, one method line and one banner; every label appears "
    "once; reproduce the supplied labels with exact spelling and add no other words. Symbols "
    "must contain no digits, letters, currency signs or percent signs, and no corporate "
    "logos. No photographs, people, 3D, screens, watermarks, chapter numbers or decorative "
    "clutter. Keep all text and arrowheads inside the image. This is a learning framework, "
    "not an investment promise."
)

ALT = (
    "Four independent case chapters stacked under the heading LEARN, each with its own "
    "question: Hilton and Skype, explain the investors’ successful sale; Visma, which "
    "investors paid and which received money; Toys R Us, why reported profit left so little "
    "cash; TeamSystem, what commitments pass to each new owner. A bracket gathers the four "
    "into one reading method, what happened, what might explain it, what a leader could "
    "change, which leads to the closing chapter, Success for whom, and for how long, asking "
    "who gained, who paid and what the company can still do. A final banner reads Make "
    "judgments the evidence supports."
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
    ap.add_argument("--out", default=None, help="Write to this path instead of the asset path.")
    ap.add_argument("--crop", default=None, help="Skip generation; crop this raw render to its content.")
    ap.add_argument("--crop-margin", type=int, default=20)
    ap.add_argument("--print-prompts", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-retries", type=int, default=4)
    ap.add_argument("--retry-delay-seconds", type=float, default=5.0)
    ap.add_argument("--model", default=gen.DEFAULT_MODEL)
    args = ap.parse_args()

    if args.crop:
        src = Path(args.crop)
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
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
