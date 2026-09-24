#!/usr/bin/env python3
"""One-off driver: regenerate the Part III chapter overview (Figure 1 of part-4-intro).

Round 2 (finding P3-002, same day): the AI card now names its three questions in verbs
("sell it, use it, or be replaced by it?") and the third band carries a one-line key
saying what artificial intelligence does, so the diagram reads standalone.

In-depth review 23 September 2026, finding P3-002: the 22 September render used
shorthand a newcomer cannot follow ("Fit cash and capacity", "Test the service
unit", "Fund transition work", unexpanded "AI"). This version keeps the layout
recorded in part-overview-images-20260922.json (heading COMMIT, three bands of
2 + 3 + 4 cards, no arrows between the four applications, one ochre banner) and
replaces every second line, and two band labels, with plain words. Driven
through the illustrator module, as in regen-figure-introduction-20260923.py.
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
    "Exactly NINE chapter cards organized into THREE clearly separated horizontal bands, stacked "
    "from top to bottom. This is a compact overview, not a tall poster.\n\n"
    "First band label: \"Choose and justify the work\".\n"
    "Two chapter cards across the band, with an arrow between them:\n"
    "\"Set priorities\" / \"Fit the cash and team time\"\n"
    "\"Test revenue assumptions\" / \"Does the change bring sales?\"\n\n"
    "A centered downward arrow connects the first band to the second.\n"
    "Second band label: \"Assess and change how work is delivered\".\n"
    "Three chapter cards across the band, with arrows left to right:\n"
    "\"Assess capability\" / \"What can the team support?\"\n"
    "\"Trace the work\" / \"Fix roles before hiring\"\n"
    "\"Plan for growth\" / \"Choose and pay for system changes\"\n\n"
    "A centered downward arrow connects the second band to the third.\n"
    "Third band label: \"Apply the same reasoning to four choices\".\n"
    "Four chapter cards in a clearly balanced TWO-BY-TWO grid within this band. "
    "Top-left \"Cloud costs\" / \"Rented computing per customer task\"; "
    "top-right \"Resilience\" / \"Restore service after failure\"; "
    "bottom-left \"AI strategy\" / \"Artificial intelligence: sell it, use it, or be replaced by it?\"; "
    "bottom-right \"Acquisitions and separations\" / \"Buying or splitting off a business\".\n"
    "These four application cards have NO arrows between them: they are different applications "
    "of the shared method, not sequential prerequisites. Use a single branch or bracket to show "
    "that the same reasoning reaches all four.\n\n"
    "Inside the third band, below the four cards, one small single-line key in plain lettering: "
    "\"Artificial intelligence (AI): software that predicts or generates content from data\".\n"
    "An arrow from the third band reaches one gold bottom banner: \"Fund feasible work and review "
    "the evidence\".\n"
    "Only the listed nine chapter cards; no extra or duplicated card. Do not number chapters or "
    "suggest that cloud changes must precede resilience, AI or acquisitions."
)

ALT = (
    "Nine chapters in three moves under the heading COMMIT. First, choose and justify the work: "
    "set priorities to fit cash and team time, then test whether the change brings sales. Second, "
    "assess and change how work is delivered: find what the team can support, fix roles and "
    "decisions before hiring, then choose and pay for system changes. Third, apply the same "
    "reasoning to four separate choices: cloud costs as rented computing per customer task, "
    "resilience as restoring service after failure, artificial intelligence (software that predicts "
    "or generates content from data) as three questions, sell it, use it or be replaced by it, and "
    "buying or splitting off a business. All lead to one outcome: fund feasible work and review "
    "the evidence."
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
