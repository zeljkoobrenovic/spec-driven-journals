#!/usr/bin/env python3
"""One-off driver: regenerate the Part II chapter overview (four chapters).

In-depth review 23 September 2026, finding P2-001: the 22 September render
(prompt archive part-overview-images-20260922.json, part 2) showed only three
chapter cards (authority, incentives, investor fit) although Part II has four
configured chapters. This version keeps the three-card sequence, the return
arrow and the ochre purpose banner from the archived prompt and adds a wide
fourth card, "Build shared evidence", beneath the row as the foundation the
other three rest on. Driven directly through the illustrator module, as in
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

POST = ROOT / "_journals/private-techuity/posts/part-2-intro"

STYLE = (
    "Create ONE finished editorial framework illustration for the introduction to a part of "
    "OWNED: Product & Engineering Leadership Under Investors. It must map the chapters, their "
    "learning connections and their shared purpose, not illustrate a business scene. Landscape "
    "4:3 composition. Match the book's existing visual language: warm ivory paper, dark navy "
    "text and clean slightly organic ink outlines, pale muted teal cards, soft ochre highlights, "
    "restrained flat fills, extremely subtle paper texture. Large, crisp, carefully typeset "
    "labels; short chapter titles visually stronger than subtitles. Generous spacing around "
    "labels and arrows. A small simple line-drawn symbol in each chapter card can help "
    "recognition, but text and connections dominate. The result should remain legible when "
    "placed at book-page width and on a narrow phone screen: card titles bold and large, "
    "subtitles and the return-arrow label at least two thirds of the title size, cards compact "
    "with little empty space inside them. No photographs, people, 3D, "
    "screens, watermarks, chapter numbers, currency signs, extraneous text or decorative "
    "clutter. Keep all text and arrowheads inside the image with comfortable margins. Reproduce "
    "the exact labels supplied, with accurate spelling and no invented claims. Use only the "
    "listed chapter cards; the shared-purpose banner is visually distinct in ochre. This is a "
    "learning framework, not an investment promise.\n\n"
)

LAYOUT = (
    "Heading at the top: \"ALIGN\".\n"
    "Three chapter cards of equal size form a left-to-right sequence across the upper half of "
    "the image. Each has a short title, a one-line question subtitle and a small editorial "
    "symbol. Large clear teal arrows connect card 1 to card 2 to card 3. A fine curved return "
    "arrow runs above the cards from card 3 back to card 1, with the exact short label "
    "\"Revisit the arrangements\". Leave enough whitespace that the return arrow and label do "
    "not touch the heading.\n\n"
    "Left card title: \"Clarify authority\"; subtitle: \"Who can decide and deliver?\" "
    "Symbol: signed decision sheet.\n"
    "Middle card title: \"Compare incentives and stakes\"; subtitle: \"What does each party "
    "gain or risk?\" Symbol: a balance scale with two different weights (no currency signs).\n"
    "Right card title: \"Assess investor fit\"; subtitle: \"How does the relationship handle "
    "pressure?\" Symbol: a handshake being tested.\n\n"
    "Directly beneath the three cards, one wide but short fourth chapter card spans the full "
    "width of the row, in the same pale teal, drawn as a foundation the three cards stand on. "
    "Title: \"Build shared evidence\"; subtitle: \"Which facts are we using?\"; a small "
    "ledger-with-source-tag symbol sits at the left of the card beside the text, so the card "
    "stays short. Three short fine connectors rise from this wide card into each of the three "
    "cards above it, showing that all three use it.\n\n"
    "Below the wide card, one connector leads down into one wide ochre purpose banner with "
    "the exact text: \"Accountable decisions with competing demands explicit\".\n"
    "Exactly four chapter cards and one banner. Do not imply shared ownership automatically "
    "aligns interests. The return arrow means observed behavior can reopen decision and "
    "escalation arrangements."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-2-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + LAYOUT,
        "alt": (
            "Four chapter boxes under the heading ALIGN. Three sit in a row joined by arrows: "
            "Clarify authority (Who can decide and deliver?), Compare incentives and stakes (What "
            "does each party gain or risk?) and Assess investor fit (How does the relationship "
            "handle pressure?). A return arrow above them is labelled Revisit the arrangements. A "
            "wide fourth box beneath the row, Build shared evidence (Which facts are we using?), "
            "supports all three. The boxes lead to a banner reading Accountable decisions with "
            "competing demands explicit."
        ),
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
        data, _source_mime, final_mime = gen.normalize_image_bytes_for_target(data, mime, out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({final_mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
