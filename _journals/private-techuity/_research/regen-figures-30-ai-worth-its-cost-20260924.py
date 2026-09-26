#!/usr/bin/env python3
"""One-off driver: regenerate the three article figures of 30-ai-worth-its-cost.

In-depth review 24 September 2026, round 1 (findings AIC-001, AIC-004, AIC-005):
the bridge is recomputed from unrounded inputs (€1,400 -> +€2,644 usage,
+€3,236 construction, −€1,456 rates -> €5,824); the three-cards figure relabels
customer value as time freed before the fee and cash return as cash
contribution before payroll (about €26,900); the commitment-floor figure carries
the derived 2028 range (€3,300 / €5,200 / €7,600, €2,000 stress) and the resized
floors (B €3,900, C €2,400) and names its unit. The illustrator module is driven
directly, as in regen-figure-anatomy-of-a-layoff-20260923.py; replaced images
are archived under _research/discarded-illustration-variants/.
"""
import argparse
import hashlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

POST = ROOT / "_journals/private-techuity/posts/30-ai-worth-its-cost"
ARCHIVE = ROOT / "_journals/private-techuity/_research/discarded-illustration-variants"

STYLE = (
    "Create one finished explanatory illustration for Owned, a practical book for product and "
    "engineering leaders. Landscape 16:9. Editorial ink-and-color diagram on a warm ivory background "
    "(#faf8f2), navy linework, muted teal and warm ochre accents. Clean flat drawing with very light "
    "texture, generous space and a clear reading order. All labels must be large, high-contrast, "
    "correctly spelled and legible at article width and on a narrow phone screen. Use only the labels "
    "requested below, spelled exactly as written, and no other text. No dense paragraphs, no figure "
    "number, no decorative headline, no watermark, no logos, no photorealism, no 3D gradients. Do not "
    "invent financial values, dates, research findings or institutional policies.\n\n"
)

FIG1 = STYLE + (
    "A single bridge chart (waterfall chart) of five vertical bars standing on one shared horizontal "
    "baseline, drawn to one consistent scale so that every bar length is exactly proportional to the "
    "euro amount written on it. Read left to right.\n\n"
    "Bar 1, navy, a full bar from the baseline, height 14 units, label under it: 'April' and the amount "
    "written just above it: '€1,400'.\n"
    "Bar 2, teal, a floating step that starts at the top of bar 1 and rises 26 units higher (from 14 up "
    "to 40), label under it: 'Usage' and the amount written beside it: '+€2,644'.\n"
    "Bar 3, ochre, a floating step that starts at the top of bar 2 and rises 32 units higher (from 40 up "
    "to 73), label under it: 'Construction' and the amount written beside it: '+€3,236'.\n"
    "Bar 4, a floating step drawn as a navy outline with a light hatched fill, that starts at the top of "
    "bar 3 and drops 15 units (from 73 down to 58), with a small downward arrow, label under it: 'Rates' "
    "and the amount written beside it: '−€1,456'.\n"
    "Bar 5, navy, a full bar from the baseline, height 58 units, label under it: 'August' and the amount "
    "written just above it: '€5,824'.\n\n"
    "Thin dashed connector lines join the top of each step to the start of the next. Bar 3 must reach "
    "clearly higher than bar 5, so the reader sees that the price cut brought the total down from its "
    "peak. Use exactly these ten labels and nothing else: April, €1,400, Usage, +€2,644, Construction, "
    "+€3,236, Rates, −€1,456, August, €5,824. No axis numbers, no legend, no title, no other words."
)

FIG2 = STYLE + (
    "Three separate cards of equal size arranged in one row with clear gaps between them, each card drawn "
    "as a rounded rectangle with a navy outline on the ivory background. In each of the two gaps, between "
    "card 1 and card 2 and between card 2 and card 3, draw one large navy plus sign with a bold navy "
    "diagonal bar struck through it from upper left to lower right, the way a road sign forbids "
    "something, meaning the amounts must not be added together.\n\n"
    "Card 1, teal accent: at the top the heading 'Customer value'; in the middle a simple drawing of a "
    "planner's desk clock beside a small stack of documents; at the bottom the two lines '€540 a month' "
    "and 'planner time freed, before the fee'.\n"
    "Card 2, ochre accent: at the top the heading 'Revenue'; in the middle a simple drawing of a price tag "
    "on a subscription card with a euro coin; at the bottom the two lines '€57,000' and 'April to "
    "September 2027'.\n"
    "Card 3, navy accent: at the top the heading 'Cash contribution'; in the middle a simple drawing of a "
    "coin dropping into a small open cash box; at the bottom the two lines 'about €26,900' and 'after "
    "running cost, before payroll'.\n\n"
    "Use exactly these labels and nothing else: Customer value, €540 a month, planner time freed, before "
    "the fee, Revenue, €57,000, April to September 2027, Cash contribution, about €26,900, after running "
    "cost, before payroll. The price tag carries no digits. No title, no equals sign, no total, no other "
    "words."
)

FIG3 = STYLE + (
    "One vertical scale of monthly model charges, drawn as a tall plain navy axis line on the left of the "
    "image with the baseline at the bottom. The axis carries no tick marks, no numbers and no words of any "
    "kind, not even a zero; every height is shown only by the labelled elements to its right. All heights "
    "are proportional to the euro amounts in the labels, measured from the baseline.\n\n"
    "A wide shaded teal band with soft edges spans most of the width. Its top edge sits near the top of "
    "the image and its bottom edge sits a little below the middle of the image. Write '€7,600 high' just "
    "inside the top edge of the band and '€3,300 low' just inside the bottom edge of the band. Inside the "
    "band, a little below its middle, a thin dashed navy line labelled '€5,200 expected'. Above the band, "
    "the two-line heading 'Demand range 2028' over 'euros a month at list price'.\n\n"
    "Two solid horizontal floor lines cross the whole width, drawn thick like the floor of a room, each "
    "with a small downward bracket at its right end showing it is a floor. An ochre floor sits inside the "
    "band, a little above the band's bottom edge and clearly below the dashed line, labelled 'Option B "
    "floor €3,900'. A navy floor sits below the band, roughly a quarter of the way from the band's bottom "
    "edge down towards the baseline, labelled 'Option C floor €2,400', with a small navy check mark right "
    "after that label.\n\n"
    "Below the navy floor, and still clearly above the baseline, a short dashed ochre line labelled "
    "'€2,000 stress case'.\n\n"
    "Vertical order from top to bottom: €7,600 high, €5,200 expected, Option B floor €3,900, €3,300 low, "
    "Option C floor €2,400, €2,000 stress case, then the empty baseline. Use exactly these eight labels "
    "and nothing else: Demand range 2028, euros a month at list price, €7,600 high, €5,200 expected, "
    "€3,300 low, €2,000 stress case, Option B floor €3,900, Option C floor €2,400. No axis numbers, no "
    "tick labels, no title, no legend, no other words or digits anywhere."
)

TARGETS = [
    {
        "id": "usage-construction-rates-bridge",
        "asset": "assets/images/30-ai-worth-its-cost/usage-construction-rates-bridge.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG1,
        "alt": "A bridge chart from April's €1,400 of model charges to August's €5,824. Usage adds €2,644, construction adds €3,236, and the vendor's rate cut removes €1,456, so the bill peaks above the August total before the price cut brings it down.",
    },
    {
        "id": "three-numbers-never-added",
        "asset": "assets/images/30-ai-worth-its-cost/three-numbers-never-added.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG2,
        "alt": "Three cards separated by crossed-out plus signs. Customer value: €540 a month, planner time freed, before the fee. Revenue: €57,000, April to September 2027. Cash contribution: about €26,900, after running cost, before payroll.",
    },
    {
        "id": "commitment-floor-against-demand-range",
        "asset": "assets/images/30-ai-worth-its-cost/commitment-floor-against-demand-range.jpeg",
        "aspect_ratio": "16:9",
        "prompt": FIG3,
        "alt": "A vertical scale of monthly model charges in euros at list price. A shaded band marks the 2028 demand range from €3,300 low to €7,600 high with €5,200 expected. Option C's committed floor of €2,400 lies below the band; Option B's floor of €3,900 lies inside it. A €2,000 stress case sits below both.",
    },
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--out", default=None, help="Write to this path instead of the asset path (no archive).")
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
        target = gen.IllustrationTarget(post_path=POST / "index.md", placeholder_index=1, start=0, end=0, item=item, image_path=out)
        if args.print_prompts:
            print(f"--- {item['id']} -> {out}\n{item['prompt']}\n")
        if args.dry_run:
            continue
        raw, mime = gen.call_gemini(api_key, args.model, target, args)
        raw, _, _ = gen.normalize_image_bytes_for_target(raw, mime, out)
        assert raw.startswith(b"\xff\xd8\xff"), "not a JPEG after normalization"
        if not args.out and out.exists():
            old = out.read_bytes()
            ARCHIVE.mkdir(exist_ok=True)
            backup = ARCHIVE / f"30-ai-worth-its-cost-{item['id']}-{hashlib.sha256(old).hexdigest()[:12]}.jpeg"
            backup.write_bytes(old)
            print(f"[archived] {backup}")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(raw)
        print(f"[wrote] {out} ({len(raw)} bytes, sha256 {hashlib.sha256(raw).hexdigest()[:12]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
