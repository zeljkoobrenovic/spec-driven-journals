#!/usr/bin/env python3
"""One-off driver: regenerate Figure 1 of 25-acquisition-adds-work-first.

The 13 September prompt archive keys this post under its legacy slug
(14-acquisitions-and-carveouts), so the illustrator module is driven directly
rather than through placeholder discovery in the published index.md.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/25-acquisition-adds-work-first"

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

FIG1 = STYLE + (
    "Three equally sized alternative models for two software businesses, arranged in "
    "three columns of equal weight with no arrow, ladder or ranking between them.\n\n"
    "Left column, headed exactly 'Separate operations': two separate product windows, "
    "each above its own small group of people, joined only by a thin dotted line with a "
    "handshake on it labelled exactly 'Sales agreement'.\n\n"
    "Middle column, headed exactly 'Shared services': two separate product windows side "
    "by side, both resting on one wide horizontal bar labelled exactly 'Shared tools and "
    "data services'.\n\n"
    "Right column, headed exactly 'Combined product': one single wider product window "
    "resting on one bar labelled exactly 'One combined customer record'.\n\n"
    "Beneath each of the three columns place one small ochre card, each bearing exactly "
    "the words 'Which benefit?'. Use no other labels anywhere in the image: no technical "
    "terms, no abbreviations, no risk words, no cloud shapes, no question marks scattered "
    "in the background."
)

TARGETS = [
    {
        "id": "integration-depth-by-benefit",
        "status": "pending",
        "asset": "assets/images/25-acquisition-adds-work-first/integration-depth-by-benefit.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG1,
        "alt": "Three columns: two separate products joined by a sales agreement; two products on shared tools and data services; one combined product on one combined customer record.",
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
