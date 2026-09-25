#!/usr/bin/env python3
"""One-off driver: regenerate the Part II, V, VI, VII and VIII chapter overviews
as compact landscape 4:3 figures.

24 September 2026: the stacked 9:16 overviews produced on 23-24 September for
Parts II, V, VI, VII and VIII (drivers regen-figure-part-{2,5,6,7,8}-overview-*.py)
rendered at the full content width of the page with lettering far larger than
the surrounding prose, and did not match the compact landscape overviews the
author kept for Parts I, III and IV (regen-part-4-overview-20260924-r4.py
recipe: wide 4:3 canvas, bands of cards, band labels, ochre banner). This driver
re-renders the five overviews in that landscape style, keeping every card title,
explanation, connector and banner of the accepted stacked versions. Before a
render overwrites an asset, the previous file is archived under
_research/discarded-illustration-variants/<slug>-chapter-overview-<sha12>.jpeg.
Driven directly through the illustrator module.

Usage (from the repository root):

    GEMINI_API_KEY=... python3 _journals/private-techuity/_research/regen-part-overviews-landscape-20260924.py [--only part-2-intro] [--out PATH]
"""
import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / ".claude/skills/article-illustrator/scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_illustrations_nanobanana as gen  # noqa: E402

JOURNAL = ROOT / "_journals/private-techuity"
ARCHIVE = JOURNAL / "_research/discarded-illustration-variants"

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
    "investment promise. This is a compact overview, not a tall poster: the drawing fills the "
    "wide canvas from left to right.\n\n"
)

PART_2 = (
    "Heading: \"ALIGN\".\n"
    "Exactly FOUR chapter cards.\n\n"
    "Top row: THREE chapter cards in ONE evenly spaced row across the width, left to right, "
    "with a short teal arrow between the first and second and between the second and third:\n"
    "\"Clarify authority\" / \"Who can decide and deliver?\" (small line-drawn signed decision "
    "sheet symbol)\n"
    "\"Compare incentives and stakes\" / \"What does each party gain or risk?\" (small line-drawn "
    "balance scale with two different weights)\n"
    "\"Assess investor fit\" / \"How does the relationship handle pressure?\" (small line-drawn "
    "handshake symbol)\n"
    "Above the row, one fine curved navy return arrow runs from the top of the third card back "
    "to the top of the first card, its arrowhead entering the first card. Its label \"Revisit "
    "the arrangements\" is written horizontally in one short line above the arrow's middle and "
    "overlaps nothing.\n\n"
    "Below the row: ONE wide foundation card spanning the full width under all three cards, "
    "drawn as a slab in the same pale teal with a slightly heavier base line, and three short "
    "fine navy connectors rising from its top edge into the three cards above to show that "
    "they rest on it:\n"
    "\"Build shared evidence\" / \"Which facts are we using?\" (small line-drawn open ledger with "
    "a source tag)\n\n"
    "A centered short teal arrow leads from the foundation card into one ochre bottom banner: "
    "\"Accountable decisions with competing demands explicit\".\n"
    "Only the listed four chapter cards, one return arrow, one banner; no extra or duplicated "
    "card. Do not number chapters. Do not imply that shared ownership automatically aligns "
    "interests."
)

PART_5 = (
    "Heading: \"SCALE\".\n"
    "Exactly FIVE chapter cards organized into THREE clearly separated horizontal bands, "
    "stacked from top to bottom, each band separated from the next by a thin plain ochre rule "
    "across the width (a plain line with no arrowheads).\n\n"
    "First band label: \"Change the team\".\n"
    "Three chapter cards in ONE evenly spaced row across the band, left to right, with a short "
    "teal arrow between the first and second only, and NO arrow between the second and third:\n"
    "\"Scale the team up\" / \"Headcount is not capacity: trace the work before hiring\" (small "
    "line-drawn organisation chart with a magnifying glass over it)\n"
    "\"Scale the team down\" / \"Decide what work stops, then who leaves\" (small line-drawn list "
    "with one row crossed out; no people)\n"
    "\"Scale the team with AI\" / \"Test a capacity claim with the same evidence\" (small "
    "line-drawn person outline beside a microchip)\n\n"
    "Second band label: \"Change the systems\".\n"
    "ONE single chapter card, centered in the band, with a two-line subtitle:\n"
    "\"Plan for growth\" / \"Choose which system change and how to fund it\" (small line-drawn "
    "stack of blocks with one block being swapped out)\n"
    "No other card in this band; leave the space either side of the single card empty.\n\n"
    "Third band label: \"Change the company's boundary\".\n"
    "ONE single chapter card, centered in the band, with a two-line subtitle:\n"
    "\"Plan acquisitions and separations\" / \"Account for the extra work a new boundary adds\" "
    "(small line-drawn dotted boundary around two buildings)\n"
    "No other card in this band; leave the space either side of the single card empty.\n\n"
    "There are NO arrows between the bands; the single teal arrow between the first two cards "
    "of the first band is the only connector between cards. A centered short teal arrow leads "
    "from the third band into one ochre bottom banner: \"Change size deliberately, fund the "
    "transition, keep the customer promise\".\n"
    "Only the listed five chapter cards, three band labels, two ochre rules, one banner; no "
    "extra or duplicated card. Do not number chapters. Do not draw a buyout-to-exit timeline."
)

PART_6 = (
    "Heading: \"SUSTAIN\".\n"
    "Exactly FOUR chapter cards organized into TWO clearly separated horizontal bands, "
    "stacked from top to bottom, separated by a thin plain ochre rule across the width (a plain "
    "line with no arrowheads).\n\n"
    "First band label: \"The estate on three columns: cost, risk and speed\".\n"
    "ONE single chapter card, centered in the band, with a two-line subtitle:\n"
    "\"Manage technical debt\" / \"Fund the fix by the cost, the risk and the speed it buys\" "
    "(small line-drawn building with scaffolding on one section of it)\n"
    "No other card in this band; leave the space either side of the single card empty.\n\n"
    "Second band label: \"Three applications of the same method\".\n"
    "Three chapter cards in ONE evenly spaced row across the band, left to right, with NO "
    "arrows between them; the three chapters are independent:\n"
    "\"Build and test resilience\" / \"Backups are not enough: prove you can restore\" (small "
    "line-drawn shield with a circular restore arrow on it)\n"
    "\"Critically evaluate cloud costs\" / \"A lower bill is not always better\" (small "
    "line-drawn cloud with a price tag hanging from it)\n"
    "\"Critically evaluate AI costs\" / \"Measure the return per task and per period\" (small "
    "line-drawn gauge dial with a small square microchip beside it)\n\n"
    "Apart from the single thin ochre rule between the bands, draw NO arrows, connectors, "
    "rails or brackets anywhere; the cards simply sit in their bands. Below the second band, "
    "one ochre bottom banner: \"Keep the technology you run worth its cost\".\n"
    "Only the listed four chapter cards, two band labels, one arrowless rule, one banner; no "
    "extra or duplicated card. Do not number chapters. Do not draw a buyout-to-exit timeline."
)

PART_7 = (
    "Heading: \"LEAD\".\n"
    "Exactly THREE chapter cards.\n\n"
    "Under the heading, one band label on a single line: \"Follow a customer setup problem: "
    "some setups depend on one specialist\".\n"
    "Three chapter cards in ONE evenly spaced row across the width, left to right, with a short "
    "solid teal arrow between the first and second and between the second and third:\n"
    "\"Use diligence\" / \"Check the business before the deal is signed\" (small line-drawn "
    "magnifying glass over a document)\n"
    "\"Plan the first hundred days\" / \"Fund the work and review the finding\" (small "
    "line-drawn calendar with a tick)\n"
    "\"Manage the handover\" / \"Pass on the evidence and unfinished promises\" (small "
    "line-drawn folder passed between two hands)\n\n"
    "Do not draw any vertical line, bracket or rail beside the cards; the two arrows alone "
    "connect the cards. A centered short teal arrow leads from the row into one ochre bottom "
    "banner: \"Account for decisions, evidence and promises through change\".\n"
    "Only the listed three chapter cards, one band label, three arrows, one banner; there is no "
    "second group, no separator rule, no dashed pointer and no note. Do not number chapters. Do "
    "not draw a buyout-to-exit timeline."
)

PART_8 = (
    "Heading: \"LEARN\".\n"
    "Exactly FIVE chapter cards.\n\n"
    "Under the heading, one band label: \"Four independent case chapters\".\n"
    "Four chapter cards in ONE evenly spaced row across the width, left to right, with NO "
    "arrows between them (the histories do not cause one another):\n"
    "\"Hilton and Skype\" / \"Explain the investors' successful sale\" (small line-drawn open "
    "book)\n"
    "\"Visma\" / \"Which investors paid, and which received money?\" (small line-drawn "
    "magnifying glass)\n"
    "\"Toys R Us\" / \"Why did profit before borrowing costs and tax generate almost no cash?\" "
    "(small line-drawn stack of coins)\n"
    "\"TeamSystem\" / \"What commitments pass to each new owner?\" (small line-drawn chain "
    "link)\n"
    "Beneath the row, one fine navy bracket spans the full width under all four cards and "
    "turns into a single centered downward arrow.\n\n"
    "That arrow points to one unboxed reading-method line in bold navy lettering, written "
    "horizontally on a single line with a small navy arrow between the phrases: "
    "\"What happened\" -> \"What might explain it\" -> \"What a leader could change\".\n\n"
    "A short teal downward arrow leads from the method line to the fifth card, centered, "
    "wider than the case cards, and the only card with a soft ochre edge:\n"
    "\"Success for whom, and for how long?\" / \"Who gained, who paid, what can the company "
    "still do?\" (small line-drawn balance scale)\n\n"
    "A short teal downward arrow leads from the fifth card into one ochre bottom banner: "
    "\"Make judgments the evidence supports\".\n"
    "Only the listed five chapter cards, one band label, one bracket, one method line, one "
    "banner; no extra or duplicated card. Symbols contain no corporate logos. Do not number "
    "chapters."
)

TARGETS = [
    {
        "slug": "part-2-intro",
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-2-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + PART_2,
        "alt": (
            "Four chapters under the heading ALIGN. In one row, Clarify authority (Who can decide "
            "and deliver?) leads to Compare incentives and stakes (What does each party gain or "
            "risk?), then to Assess investor fit (How does the relationship handle pressure?). A "
            "return arrow labelled Revisit the arrangements runs from the third chapter back to the "
            "first. Beneath them, Build shared evidence (Which facts are we using?) is drawn as a "
            "foundation used by all three. A final banner reads Accountable decisions with competing "
            "demands explicit."
        ),
    },
    {
        "slug": "part-5-intro",
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-5-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + PART_5,
        "alt": (
            "Five chapters in three groups under the heading SCALE. Group one, change the team: "
            "scale the team up only after tracing the work, because headcount is not capacity; scale "
            "the team down by deciding what work stops before deciding who leaves; and scale the team "
            "with AI by testing a capacity claim with the same evidence as headcount. Group two, "
            "change the systems: plan for growth by choosing which system change to make and how to "
            "fund it. Group three, change the company’s boundary: plan acquisitions and separations "
            "by accounting for the extra work a new boundary adds. A final banner reads change size "
            "deliberately, fund the transition, keep the customer promise."
        ),
    },
    {
        "slug": "part-6-intro",
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-6-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + PART_6,
        "alt": (
            "Four chapters under the heading SUSTAIN: Manage technical debt, fund the fix by the "
            "cost, the risk and the speed it buys, framing the part with three columns; then, in one "
            "row, three applications of one method: Build and test resilience, backups are not "
            "enough; Critically evaluate cloud costs, a lower bill is not always better; Critically "
            "evaluate AI costs, measure the return per task and per period. A final banner reads Keep "
            "the technology you run worth its cost."
        ),
    },
    {
        "slug": "part-7-intro",
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-7-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + PART_7,
        "alt": (
            "Three chapters in one row under the heading LEAD, following a customer setup problem "
            "where some setups depend on one specialist: Use diligence (check the business before "
            "the deal is signed) leads to Plan the first hundred days (fund the work and review the "
            "finding), which leads to Manage the handover (pass on the evidence and unfinished "
            "promises). A final banner reads Account for decisions, evidence and promises through "
            "change."
        ),
    },
    {
        "slug": "part-8-intro",
        "id": "chapter-overview",
        "status": "pending",
        "asset": "assets/images/part-8-intro/chapter-overview.jpeg",
        "aspect_ratio": "4:3",
        "prompt": STYLE + PART_8,
        "alt": (
            "Four independent case chapters in one row under the heading LEARN, each with its own "
            "question: Hilton and Skype, explain the investors’ successful sale; Visma, which "
            "investors paid and which received money; Toys R Us, why profit before borrowing costs "
            "and tax generated almost no cash; TeamSystem, what commitments pass to each new owner. "
            "A bracket gathers the four into one reading method, what happened, what might explain "
            "it, what a leader could change, which leads to the closing chapter, Success for whom, "
            "and for how long, asking who gained, who paid and what the company can still do. A "
            "final banner reads Make judgments the evidence supports."
        ),
    },
]


def archive_existing(path: Path, slug: str) -> Path | None:
    if not path.exists():
        return None
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    dest = ARCHIVE / f"{slug}-chapter-overview-{digest}{path.suffix}"
    if not dest.exists():
        shutil.copy2(path, dest)
    return dest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", action="append", default=[], help="Slug substring, e.g. part-5-intro.")
    ap.add_argument("--out", default=None, help="Write to this path instead of the asset path (single target).")
    ap.add_argument("--print-prompts", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-archive", action="store_true", help="Do not copy the previous render to the archive.")
    ap.add_argument("--max-retries", type=int, default=4)
    ap.add_argument("--retry-delay-seconds", type=float, default=5.0)
    ap.add_argument("--model", default=gen.DEFAULT_MODEL)
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key and not args.dry_run:
        print("GEMINI_API_KEY is not set", file=sys.stderr)
        return 2

    for item in TARGETS:
        if args.only and not any(o in item["slug"] for o in args.only):
            continue
        post = JOURNAL / "posts" / item["slug"]
        out = Path(args.out) if args.out else post / item["asset"]
        target = gen.IllustrationTarget(
            post_path=post / "index.md",
            placeholder_index=1,
            start=0,
            end=0,
            item=item,
            image_path=out,
        )
        if args.print_prompts:
            print(f"--- {item['slug']} -> {out}\n{item['prompt']}\n")
        if args.dry_run:
            continue
        data, mime = gen.call_gemini(api_key, args.model, target, args)
        data, _src, mime = gen.normalize_image_bytes_for_target(data, mime, out)
        if not args.no_archive and not args.out:
            archived = archive_existing(out, item["slug"])
            if archived:
                print(f"[archived] {archived}")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f"[wrote] {out} ({mime}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
