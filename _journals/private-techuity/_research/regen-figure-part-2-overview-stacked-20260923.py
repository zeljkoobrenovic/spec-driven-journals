#!/usr/bin/env python3
"""One-off driver: regenerate the Part II chapter overview as a stacked column.

In-depth review 23 September 2026, round 2, finding P2-006: the four-card
4:3 overview accepted in round 1 (driver regen-part-overview-part-2-20260923.py)
is clear at full size, but at a 375-pixel phone width (about 327 CSS pixels
for a 1200-pixel image) its three-column questions and the return-arrow label
fall to roughly 8 pixels. This version keeps the four chapter cards, the
return arrow, the shared-evidence foundation and the purpose banner, but
stacks the cards in one column with large type, as the Part I overview was
regenerated on the same day (regen-figure-part-1-overview-20260923.py).
Driven directly through the illustrator module.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/part-2-intro"

PROMPT = (
    "Create ONE finished editorial framework illustration for the introduction to a part "
    "of OWNED: Product & Engineering Leadership Under Investors. It maps four chapters, "
    "their reading order and their shared purpose; it is not a business scene. Portrait "
    "3:4 composition. Match the book's visual language: warm ivory paper, dark navy text, "
    "clean slightly organic ink outlines, pale muted teal cards, soft ochre highlights, "
    "restrained flat fills, extremely subtle paper texture.\n\n"
    "LAYOUT, STRICT: a single vertical column. Every chapter card spans almost the full "
    "image width, one card per row, four rows in total, read top to bottom. Never place two "
    "cards side by side. The image will be shown on a narrow phone screen, so all lettering "
    "must be very large: each card title is bold and about one twentieth of the image width "
    "in cap height; each question subtitle is about two thirds of the title size; the "
    "return-arrow label is bold and the same size as the subtitles. Keep margins comfortable "
    "but do not waste space; the cards and labels should fill the column. No frame, border "
    "or ruled lines around the composition.\n\n"
    "Heading at the top: \"ALIGN\".\n\n"
    "Card 1 title: \"Clarify authority\"; subtitle: \"Who can decide and deliver?\" "
    "Small line-drawn signed decision sheet symbol at the left of the card.\n"
    "A short teal downward arrow links card 1 to card 2.\n"
    "Card 2 title: \"Compare incentives and stakes\"; subtitle: \"What does each party gain or risk?\" "
    "Small line-drawn balance scale with two different weights at the left of the card.\n"
    "A short teal downward arrow links card 2 to card 3.\n"
    "Card 3 title: \"Assess investor fit\"; subtitle: \"How does the relationship handle pressure?\" "
    "Small line-drawn handshake symbol at the left of the card.\n"
    "A fine curved navy return arrow runs up the right margin from card 3 back to card 1, "
    "with the arrowhead entering card 1. Its label \"Revisit the arrangements\" is written "
    "horizontally in one short line beside the arrow, between card 1 and card 2 at the right "
    "edge, and does not overlap any card or arrow.\n\n"
    "Card 4 sits directly beneath card 3 and is drawn as a foundation slab: the same pale "
    "teal, a slightly heavier base line, and three short fine navy connectors rising from its "
    "top edge into card 3 to show that the chapters above rest on it. Card 4 title: "
    "\"Build shared evidence\"; subtitle: \"Which facts are we using?\" Small line-drawn open "
    "ledger with a source tag at the left of the card.\n\n"
    "A short teal downward arrow leads from card 4 into an ochre banner across the bottom "
    "with the exact text: \"Accountable decisions with competing demands explicit\". Arrows "
    "never cross text.\n\n"
    "Exactly four cards, one return arrow and one banner; every title appears once; reproduce "
    "the supplied labels with exact spelling and add no other words. Symbols must contain no "
    "digits, letters, currency signs or percent signs. No photographs, people, 3D, screens, "
    "watermarks, chapter numbers or decorative clutter. Keep all text and arrowheads inside "
    "the image. Do not imply that shared ownership automatically aligns interests."
)

ALT = (
    "Four chapters stacked in one column under the heading ALIGN. Clarify authority (Who can "
    "decide and deliver?) leads to Compare incentives and stakes (What does each party gain or "
    "risk?), then to Assess investor fit (How does the relationship handle pressure?). A return "
    "arrow labelled Revisit the arrangements runs from the third chapter back to the first. "
    "Beneath them, Build shared evidence (Which facts are we using?) is drawn as a foundation "
    "used by all three. A final banner reads Accountable decisions with competing demands "
    "explicit."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-2-intro/chapter-overview.jpeg",
        "aspect_ratio": "3:4",
        "prompt": PROMPT,
        "alt": ALT,
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
