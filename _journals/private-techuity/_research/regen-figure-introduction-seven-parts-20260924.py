#!/usr/bin/env python3
"""One-off driver: regenerate Figure 2 of the introduction as a seven-part framework.

On 24 September 2026 the book gained a new Part IV ("SCALE: Change the Team, the
Systems and the Company Deliberately"); the former Parts IV-VI became V-VII. The
displayed Figure 2 (owned-six-part-framework.jpeg, generated 21 September 2026 from
_research/introduction-framework-20260921/prompt.txt) therefore showed one part too
few. This driver reuses that prompt's style and card layout, inserts the new IV
Scale card between III Commit and V Collaborate, and renumbers Lead and Learn to VI
and VII. The alt text in posts/introduction/index.md is the contract for the labels.
Driven directly through the illustrator module, as in
regen-figure-introduction-20260923.py. Aspect ratio 3:2 matches the six-part file
(1448 x 1000).
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/introduction"

STYLE = (
    "Create one finished editorial infographic illustration for Owned, a practical book "
    "for product and engineering leaders. Landscape 3:2, polished, generous margins, "
    "crisp and highly readable. Restrained, elegant editorial illustration for an "
    "illustrated nonfiction leadership book: warm ivory paper background (#faf8f2), dark "
    "navy outlines and text, muted teal and soft ochre accents, clean simple illustrated "
    "symbols with slightly organic ink lines and very subtle paper character, "
    "predominantly flat light fills. No photographs, fake screenshots, heavy texture or "
    "3D effects. All lettering must be large, high-contrast, correctly spelled and legible "
    "at article width and on a narrow phone screen. Use only the exact text requested "
    "below and no other words, letters, numbers or symbols. No figure number, no "
    "headline, no watermark, no logos, no people. Render edge-to-edge on the ivory canvas "
    "with no surrounding page, frame or mockup.\n\n"
)

FIG2 = STYLE + (
    "Show the seven parts of the book as one coherent leadership framework around a "
    "shared purpose. Seven balanced rounded cards of equal size are arranged clockwise "
    "around a central circle, with one clear outer clockwise arrow path I -> II -> III -> "
    "IV -> V -> VI -> VII and a wraparound return arrow from VII back up to I, plus fine "
    "inward connector lines tying each card to the central circle. Keep every arrow and "
    "connector clear of all text. The outer path is a chain of seven separate short "
    "arrows, each from one card to the next: I to II, II to III, III down into the top of "
    "IV, IV down out of its bottom into V, V to VI, VI to VII, and VII up to I. IV must "
    "sit on the path with one arrow entering it and one arrow leaving it; no arrow may "
    "bypass IV.\n\n"
    "Placement: top row from left to right: I at upper left, II at top centre, III at "
    "upper right. IV alone on the right-hand side at middle height, beside the centre. "
    "Bottom row from right to left: V at lower right, VI at bottom centre, VII at lower "
    "left. The left-hand side at middle height stays empty except for the return arrow "
    "from VII up to I.\n\n"
    "Central circle, soft ochre fill, large clear text on three short lines: "
    "'Commitments the company can keep'.\n\n"
    "Each card carries a small ochre circle with its Roman numeral, then a prominent "
    "capitalised action word, then a smaller but readable subtitle, then one modest "
    "symbol below the text:\n"
    "'I' / 'UNDERSTAND' / 'Money & obligations' : an open financial ledger and a few coins.\n"
    "'II' / 'ALIGN' / 'Authority & incentives' : an agreement sheet and a decision fork with a tick.\n"
    "'III' / 'COMMIT' / 'Feasible work' : a few building blocks and a ticked work plan.\n"
    "'IV' / 'SCALE' / 'Team, systems & company boundary' : three building blocks growing "
    "in size from left to right, with a small dashed boundary line drawn around them. Coins carry no currency signs.\n"
    "'V' / 'COLLABORATE' / 'Useful help & capability' : two collaborating hands supporting a small gear.\n"
    "'VI' / 'LEAD' / 'Funding & ownership changes' : a bridge connecting two different landscapes.\n"
    "'VII' / 'LEARN' / 'Evidence from other companies' : an open book with small charts on its pages and a magnifying glass; no words on the pages.\n\n"
    "Constraints: exactly seven cards, each Roman numeral used once and paired with the "
    "correct action word; absolutely accurate spelling of every word. Text is dominant "
    "over the small symbols. Make the VII-to-I return arrow visible and unambiguous. No "
    "extra parts, no statistics, no other words anywhere."
)

TARGETS = [
    {
        "id": "owned-seven-part-framework",
        "status": "pending",
        "asset": "assets/images/introduction/owned-seven-part-framework.jpeg",
        "aspect_ratio": "3:2",
        "prompt": FIG2,
        "alt": "Seven parts form a connected framework around commitments the company can keep: I Understand money and obligations; II Align authority and incentives; III Commit to feasible work; IV Scale the team, the systems and the company deliberately; V Collaborate for useful help and capability; VI Lead through funding and ownership changes; VII Learn from evidence about other companies. A clockwise path connects the parts and returns from learning to understanding.",
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
            placeholder_index=2,
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
