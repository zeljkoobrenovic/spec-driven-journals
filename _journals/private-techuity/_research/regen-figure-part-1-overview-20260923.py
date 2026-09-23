#!/usr/bin/env python3
"""One-off driver: regenerate the Part I chapter overview as a stacked column.

In-depth review 23 September 2026, findings P1-002 and P1-003: the 22 September
two-column overview (archive key part 1 in part-overview-images-20260922.json)
used subtitles a beginner cannot decode in place ("Numbers and assumptions",
"Same performance, different outcomes", "Available cash and dates") and, at a
375-pixel phone width, its lettering fell to roughly 7-8 CSS pixels. This
version keeps the six cards, the three stage labels and the purpose banner, but
stacks the cards in one column with large type and plain-language subtitles.
Driven directly through the illustrator module, as in
regen-figure-introduction-20260923.py.
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
    "their reading order and their shared purpose; it is not a business scene. Portrait "
    "3:4 composition. Match the book's visual language: warm ivory paper, dark navy text, "
    "clean slightly organic ink outlines, pale muted teal cards, soft ochre highlights, "
    "restrained flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width, one card per row, six rows in total, read top to bottom. Never place two "
    "cards side by side. The image will be shown on a narrow phone screen, so all lettering "
    "must be very large: each card title is bold and about one twentieth of the image width "
    "in cap height; each subtitle is about two thirds of the title size; the stage labels "
    "sit between the title and subtitle sizes. Keep margins comfortable but do not waste "
    "space; the cards and labels should fill the column.\n\n"
    "Heading at the top: \"UNDERSTAND\".\n\n"
    "Stage label 1: \"Trace money and control\".\n"
    "Card 1 title: \"Customers, lenders, investors\"; subtitle: \"What each source expects\". "
    "Small line-drawn ledger-and-coins symbol at the left of the card.\n"
    "Card 2 title: \"Funding and control\"; subtitle: \"Who receives money and approves spending\". "
    "Small line-drawn approval-stamp symbol at the left of the card.\n\n"
    "Stage label 2: \"Interpret value and returns\".\n"
    "Card 3 title: \"Valuation\"; subtitle: \"Estimating what a business is worth\". "
    "Small line-drawn magnifying glass over a small building symbol.\n"
    "Card 4 title: \"Investor returns\"; subtitle: \"Gains or losses on invested money\". "
    "Small line-drawn symbol of three branching arrows, one up, one level, one down.\n\n"
    "Stage label 3: \"Confirm funding for the work\".\n"
    "Card 5 title: \"Funding choices\"; subtitle: \"Match the money to the work\". "
    "Small line-drawn two-piece jigsaw symbol.\n"
    "Card 6 title: \"Cash flow\"; subtitle: \"Money coming in and going out\". "
    "Small line-drawn calendar with coins symbol.\n\n"
    "A short teal downward arrow links each card to the next, and a final arrow leads from "
    "card 6 into an ochre banner across the bottom with the exact text: "
    "\"Know what can fund a commitment to do the work\". Arrows never cross text.\n\n"
    "Exactly six cards; every title appears once; reproduce the supplied labels with exact "
    "spelling and add no other words. Symbols must contain no digits, letters, currency "
    "signs or percent signs. No photographs, people, 3D, screens, watermarks, chapter "
    "numbers or decorative clutter. Keep all text and arrowheads inside the image."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-1-intro/chapter-overview.jpeg",
        "aspect_ratio": "3:4",
        "prompt": PROMPT,
        "alt": "Six chapters stacked in three stages. Trace money and control: Customers, lenders, investors (what each source expects) leads to Funding and control (who receives money and approves spending). Interpret value and returns: Valuation (estimating what a business is worth) leads to Investor returns (gains or losses on invested money). Confirm funding for the work: Funding choices (match the money to the work) leads to Cash flow (money coming in and going out). A final banner reads Know what can fund a commitment to do the work.",
    },
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--out", default=None, help="Write to this path instead of the asset path.")
    ap.add_argument("--print-prompts", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-retries", type=int, default=4)
    ap.add_argument("--retry-delay-seconds", type=float, default=5.0)
    ap.add_argument("--model", default=gen.DEFAULT_MODEL)
    args = ap.parse_args()

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
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
