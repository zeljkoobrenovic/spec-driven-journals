#!/usr/bin/env python3
"""One-off driver: regenerate Figure 2 of 26-anatomy-of-a-layoff.

In-depth review 23 September 2026, finding LAY-009: the first render drew the
unchanged onboarding workbench much larger after the reduction and carried no
engineer counts. This version labels every work stream with its count (before:
4/2/5/3/2 = 16; after, from 1 April: onboarding 4, core 8 = 12, excluding Alex)
and keeps the onboarding bench the same size on both sides. The figure has no
entry in the 13 September prompt archive, so the illustrator module is driven
directly, as in regen-figure-17-acquisition-20260922.py.

Round 3 (finding LAY-017): the right-hand heading now carries the base-case
qualification (the retained specialist leaves on 31 March; in the extension
branches a thirteenth engineer is still there on 1 April), and the alt text no
longer calls the left-hand benches equal.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/26-anatomy-of-a-layoff"

STYLE = (
    "Create one finished explanatory illustration for Owned, a practical book for "
    "product and engineering leaders. Landscape 16:9. Editorial ink-and-color diagram "
    "on a warm ivory background (#faf8f2), navy linework, muted teal for resources and "
    "useful progress, warm ochre for conditions and uncertainty. Use concrete objects "
    "and clean flat drawing with very light texture, generous space and a clear reading "
    "order. All labels must be large, high-contrast, correctly spelled and legible at "
    "article width and on a narrow phone screen. Use only the short labels requested "
    "below and no other text. Convey meaning through layout and objects; no dense "
    "paragraphs, no figure number, no decorative headline, no watermark, no logos, no "
    "photorealism, no 3D gradients. Do not invent financial values, dates, research "
    "findings or institutional policies.\n\n"
)

FIG2 = STYLE + (
    "A before-and-after diagram of one engineering team organized by work, in two "
    "halves separated by a thick navy arrow pointing right.\n\n"
    "Left half, headed exactly '1 OCTOBER: 16 ENGINEERS'. Five small workbenches of "
    "EXACTLY the same size stacked in a neat column, each with one label: "
    "'ONBOARDING 4', 'RECOVERY 2', 'CORE 5', 'SECOND COUNTRY 3', 'MOBILE APP 2'.\n\n"
    "Right half, headed exactly '1 APRIL: 12 ENGINEERS', with directly beneath it a "
    "smaller navy subheading, underlined in ochre, reading exactly 'BASE CASE: SPECIALIST LEFT 31 MARCH'. Top: one workbench labelled "
    "'ONBOARDING 4', drawn EXACTLY the same size as the left-hand onboarding bench, with "
    "a small tag 'UNCHANGED'. Middle: one clearly longer workbench labelled 'CORE 8', "
    "with two small teal tags hanging from it reading exactly '+2 FROM RECOVERY' and "
    "'+1 SECOND COUNTRY'. Bottom: one small bench covered with an ochre cloth, with a "
    "tag reading exactly 'MOBILE APP STOPPED'.\n\n"
    "Draw no people and no other labels, numbers or words anywhere."
)

TARGETS = [
    {
        "id": "team-by-work-before-and-after",
        "status": "pending",
        "asset": "assets/images/24-anatomy-of-a-layoff/team-by-work-before-and-after.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG2,
        "alt": "Before and after: five benches (onboarding 4, recovery 2, core 5, second country 3, mobile app 2) become onboarding 4 unchanged, core 8 with two from recovery and one from the second country, and the mobile app stopped.",
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
