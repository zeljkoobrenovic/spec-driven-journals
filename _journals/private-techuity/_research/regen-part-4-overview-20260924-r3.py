#!/usr/bin/env python3
"""One-off driver: regenerate the Part III chapter overview (Figure 1 of part-4-intro).

24 September 2026, round 3: the AI strategy chapter ("Clarify AI strategy" /
sell it, use it, or be replaced by it?) moved back into Part III COMMIT, joining
the first band. Part III now has FIVE chapters in three moves: 3 + 1 + 1. This
driver keeps the layout style, palette, 4:3 ratio, band arrows and ochre banner of
round 2 (regen-part-4-overview-20260924-r2.py), adds the AI card with a small
brain-chip icon as the third card of the first band, and restores the AI key line
under that band, matching the updated alt text and Learning Path bullets in
posts/part-4-intro/index.md. The four-card round-2 render is archived under
discarded-illustration-variants/part-4-intro-chapter-overview-9de571b78f2f.jpeg.
Driven through the illustrator module, as before.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/part-4-intro"

STYLE = (
    "Create ONE finished editorial framework illustration for the introduction to a part of "
    "OWNED: Product & Engineering Leadership Under Investors. It must map the chapters, their "
    "learning connections and their shared purpose, not illustrate a business scene. Landscape "
    "4:3 composition. Match the book's existing visual language: warm ivory paper, dark navy "
    "text and clean slightly organic ink outlines, pale muted teal cards, soft ochre highlights, "
    "restrained flat fills, extremely subtle paper texture. Large, crisp, carefully typeset "
    "labels; short chapter titles visually stronger than subtitles, but subtitles still large "
    "enough to read on a phone screen. Generous spacing around labels and arrows. A small simple "
    "line-drawn symbol in each chapter card can help recognition, but text and connections "
    "dominate; omit a symbol rather than crowd the text. No photographs, people, 3D, screens, "
    "watermarks, chapter numbers, extraneous text or decorative clutter. Keep all text and "
    "arrowheads inside the image with comfortable margins. Reproduce the exact labels supplied, "
    "with accurate spelling and no invented claims. Use only the listed chapter cards; the "
    "shared-purpose banner is visually distinct in ochre. This is a learning framework, not an "
    "investment promise.\n\n"
)

LAYOUT = (
    "Heading: \"COMMIT\".\n"
    "Exactly FIVE chapter cards organized into THREE clearly separated horizontal bands, stacked "
    "from top to bottom. This is a compact overview, not a tall poster.\n\n"
    "First band label: \"Choose and justify the work\".\n"
    "Three chapter cards in ONE evenly spaced row across the band, left to right, with an arrow "
    "between the first and second and between the second and third:\n"
    "\"Set priorities\" / \"Fit the cash and team time\"\n"
    "\"Test revenue assumptions\" / \"Does the change bring sales?\"\n"
    "\"Clarify AI strategy\" / \"Sell it, use it, or be replaced by it?\"\n"
    "The third card carries a small simple line-drawn symbol of a brain outline inside a "
    "microchip, in the same navy ink as the outlines, placed so it does not crowd the text.\n"
    "Inside the first band, below the three cards, one small single-line key in plain lettering: "
    "\"Artificial intelligence (AI): software that predicts or generates content from data\".\n\n"
    "A centered downward arrow connects the first band to the second.\n"
    "Second band label: \"Assess what delivery requires\".\n"
    "ONE single chapter card, centered in the band, with a two-line subtitle:\n"
    "\"Assess capability\" / \"What can the software and team support, and what would a transition cost?\"\n"
    "No other card in this band; leave the space either side of the single card empty.\n\n"
    "A centered downward arrow connects the second band to the third.\n"
    "Third band label: \"Revise when the money is late\".\n"
    "ONE single chapter card, centered in the band, with a two-line subtitle:\n"
    "\"Manage funding delays\" / \"Put cash and commitments on a calendar; choose one fallback in time\"\n"
    "This card carries a small simple line-drawn symbol of a calendar page with a small hourglass "
    "beside it, in the same navy ink as the outlines, placed so it does not crowd the text. "
    "No other card in this band; leave the space either side of the single card empty.\n\n"
    "An arrow from the third band reaches one gold bottom banner: \"Fund feasible work and review "
    "the evidence\".\n"
    "Only the listed five chapter cards; no extra or duplicated card; the AI key line is the only "
    "footnote. Do NOT include any card about cloud costs, resilience, hiring, roles, system changes, "
    "growth, acquisitions or separations. Do not number chapters."
)

ALT = (
    "Five chapters in three moves under the heading COMMIT. First, choose and justify the work: "
    "set priorities to fit cash and team time, test whether the change brings sales, then separate "
    "the three investment questions inside an AI strategy request (artificial intelligence is "
    "software that predicts or generates content from data): sell it, use it, or be replaced by it. "
    "Second, assess what delivery requires: find what the software and the team can support and "
    "what a transition would cost. Third, revise when the money is late: put cash and commitments "
    "on a calendar and choose one fallback in time. All lead to one outcome: fund feasible work "
    "and review the evidence."
)

TARGETS = [
    {
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-4-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + LAYOUT,
        "layout": LAYOUT,
        "alt": ALT,
    },
]


def main() -> int:
    ap = argparse.ArgumentParser()
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
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
