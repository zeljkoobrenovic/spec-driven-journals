#!/usr/bin/env python3
"""One-off driver: regenerate Figure 1 of the introduction (four questions).

In-depth review 23 September 2026, finding INTRO-MAJOR-1: the previous render
illustrated "What is changing" with "New feature" and "Process update", while
the prose uses that question for ownership and business situations (a carve-out
or a turnaround); the Owners panel carried unexplained P and E letters and the
Rights panel a copyright symbol. This version keeps the four cards and the
Commitment notebook from the 13 September prompt archive (key "introduction",
figure 1) and constrains the panel contents. Driven directly through the
illustrator module, as in regen-figure-anatomy-of-a-layoff-20260923.py.

Round 2 (same day, INTRO-MAJOR-1 residual): the first re-render drew the
"Leaving a larger company" arrow from the small building toward the larger
one, the reverse of a separation. The upper scene is now specified with the
large outline on the left, the small building on the right and the arrow
leading away from the larger building. Alt text rewritten to the visible
content (no loan, no locked/unlocked decision).
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
    "Create one finished explanatory illustration for Owned, a practical book for "
    "product and engineering leaders. Landscape 16:9. Editorial ink-and-color diagram "
    "on a warm ivory background (#faf8f2), navy linework, muted teal for resources and "
    "useful progress, warm ochre for conditions and uncertainty. Use concrete objects "
    "and clean flat drawing with very light texture, generous space and a clear reading "
    "order. All labels must be large, high-contrast, correctly spelled and legible at "
    "article width and on a narrow phone screen. Use only the short labels requested "
    "below and no other text, letters, numbers or symbols. Convey meaning through layout "
    "and objects; no dense paragraphs, no figure number, no decorative headline, no "
    "watermark, no logos, no photorealism, no 3D gradients. Do not invent financial "
    "values, dates, research findings or institutional policies.\n\n"
)

FIG1 = STYLE + (
    "A company leader's open notebook sits at the center, labelled exactly 'Commitment' "
    "on its cover band; its pages carry only blank ruled lines. Four question cards "
    "surround it, two on the left and two on the right, and each card sends one "
    "separate arrow into the notebook (teal arrows from the top cards, ochre arrows "
    "from the bottom cards).\n\n"
    "Top left card, headed exactly 'Owners': three different people standing side by "
    "side in business clothes, drawn without any letters, badges, gears, crowns or keys.\n\n"
    "Top right card, headed exactly 'Rights': a signed document with a large round "
    "approval stamp reading exactly 'APPROVED', and beside it a small ballot-style "
    "checkbox with a tick. No copyright symbol, no scales, no shield, no padlock, no "
    "blueprint.\n\n"
    "Bottom left card, headed exactly 'Funding': a money bag, a stack of coins and a "
    "simple rising line chart. No currency signs.\n\n"
    "Bottom right card, headed exactly 'What is changing': two small scenes stacked "
    "vertically, each with one short label. Upper scene labelled exactly 'Leaving a "
    "larger company': on the left, a large office building drawn only in faint outline "
    "with an empty dashed slot in its right-hand side; on the right, a small solid "
    "building standing on its own; one bold arrow starts at the empty slot and points "
    "to the right, away from the large building and toward the small building, so the "
    "small building is clearly moving out of the large one. The arrow must not point "
    "toward the large building. Lower scene labelled exactly 'Fixing a struggling "
    "business': a cracked building being repaired with a wrench and a supporting "
    "beam.\n\n"
    "Draw no other words anywhere."
)

TARGETS = [
    {
        "id": "four-questions-before-a-commitment",
        "status": "pending",
        "asset": "assets/images/introduction/four-questions-before-a-commitment.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG1,
        "alt": "Four cards feed one notebook labelled Commitment: Owners (three people in business clothes), Rights (a signed document stamped APPROVED beside a ticked checkbox), Funding (a money bag, stacked coins and a rising line chart) and What is changing (a small building moving out of a larger building outline, labelled Leaving a larger company, and a cracked building being repaired with a wrench and propped by a beam, labelled Fixing a struggling business).",
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
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
