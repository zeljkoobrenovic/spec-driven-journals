#!/usr/bin/env python3
"""Re-letter the fictional company name on accepted Owned images (3 October 2026).

The shared scenario company was renamed from Larkspur to Rotaline in every text
file. These 24 images (23 comic pages, one summary figure) letter the old name
in the artwork; OCR found them. Each image gets one in-place Gemini edit that
replaces only the name, keeping the artwork, then the comic block's recorded
sha256 is updated in place (no re-render, so comics.md changes by one hash).

Usage from the repository root:

    GEMINI_API_KEY=... python3 _journals/private-techuity/_research/retext-rotaline-20261003.py [--only <substring>]

Replaced images are archived under _research/discarded-comic-variants/.
Edited images are listed in _research/retext-rotaline-20261003.done and skipped
on the next run, so an interrupted run can be resumed; --only re-edits one image.
Inspect every edited image against its page block before accepting it.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
JOURNAL = ROOT / "_journals/private-techuity"
sys.path.insert(0, str(ROOT / ".claude/skills/explainer-comics/scripts"))
import generate_comic_pages as pages  # noqa: E402
import generate_comic_panels as panels  # noqa: E402

TARGETS = [
    "00-understand-expectations/assets/images/00-understand-expectations/summary-at-a-glance.jpeg",
    "01-understand-funding-control/assets/images/01-understand-funding-control/comic-page-02-who-receives-the-money.jpeg",
    "01-understand-funding-control/assets/images/01-understand-funding-control/comic-page-03-four-organizations-four-wallets.jpeg",
    "01-understand-funding-control/assets/images/01-understand-funding-control/comic-page-05-three-payments-three-agreements.jpeg",
    "01-understand-funding-control/assets/images/01-understand-funding-control/comic-page-06-the-one-page-record.jpeg",
    "02-understand-valuation/assets/images/02-understand-valuation/comic-page-07-funding-round-headline.jpeg",
    "03-understand-investor-returns/assets/images/03-understand-investor-returns/comic-page-06-a-smaller-slice.jpeg",
    "04-understand-funding-choices/assets/images/04-understand-funding-choices/comic-page-03-size-the-work-first.jpeg",
    "06-clarify-authority/assets/images/06-clarify-authority/comic-page-02-who-may-approve-what.jpeg",
    "07-compare-incentives-stakes/assets/images/07-compare-incentives-stakes/comic-page-04-a-target-changes-behavior.jpeg",
    "07-compare-incentives-stakes/assets/images/07-compare-incentives-stakes/comic-page-05-one-closure-four-bets.jpeg",
    "08-assess-investor-fit/assets/images/08-assess-investor-fit/comic-page-01-two-offers-same-promises.jpeg",
    "13-clarify-adviser-role/assets/images/13-clarify-adviser-role/comic-page-01-a-specialist-joins-the-meeting.jpeg",
    "18-test-revenue-assumptions/assets/images/18-test-revenue-assumptions/comic-page-03-capacity-is-not-cash.jpeg",
    "19-clarify-ai-strategy/assets/images/19-clarify-ai-strategy/comic-page-05-the-support-pilot.jpeg",
    "23-scale-the-team-down/assets/images/23-scale-the-team-down/comic-page-04-cash-does-not-arrive-monthly.jpeg",
    "23-scale-the-team-down/assets/images/23-scale-the-team-down/comic-page-09-both-sides-of-the-door.jpeg",
    "24-scale-the-team-with-ai/assets/images/24-scale-the-team-with-ai/comic-page-01-the-note-that-says-fewer-people.jpeg",
    "26-plan-acquisitions-separations/assets/images/26-plan-acquisitions-separations/comic-page-04-decide-what-waits.jpeg",
    "26-plan-acquisitions-separations/assets/images/26-plan-acquisitions-separations/comic-page-05-the-independence-bill.jpeg",
    "28-build-test-resilience/assets/images/28-build-test-resilience/comic-page-01-six-in-the-morning.jpeg",
    "31-use-diligence/assets/images/31-use-diligence/comic-page-04-three-options-one-agreed-response.jpeg",
    "38-success-for-whom/assets/images/38-success-for-whom/comic-page-03-thirty-customers-on-the-old-path.jpeg",
    "38-success-for-whom/assets/images/38-success-for-whom/comic-page-04-a-breach-is-not-a-saving.jpeg",
]

PROMPT = (
    "Edit the attached image. Change ONLY the company name: wherever the word \"LARKSPUR\" or \"Larkspur\" is "
    "lettered, replace it with \"ROTALINE\" or \"Rotaline\" in the same case, same lettering style, size and color, "
    "in the same place, keeping any possessive (\"LARKSPUR'S\" becomes \"ROTALINE'S\"). Every other word stays exactly "
    "as it is. Keep every other pixel of the image as it is: the same drawings, people, faces, colors, strips, "
    "borders, speech bubbles, boards, cards, numbers, labels and all other text. Add nothing else."
)
DONE = Path(__file__).with_suffix(".done")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", action="append", default=[], help="Only images whose path contains this text.")
    parser.add_argument("--model", default=panels.DEFAULT_MODEL)
    parser.add_argument("--sleep", type=float, default=2.0)
    args = parser.parse_args()
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("error: GEMINI_API_KEY is not set.", file=sys.stderr)
        return 2
    done = set(DONE.read_text().split()) if DONE.exists() else set()
    for rel in TARGETS:
        if args.only and not any(o in rel for o in args.only):
            continue
        if rel in done and not args.only:
            print(f"skip done: {rel}")
            continue
        image_path = JOURNAL / "posts" / rel
        post_dir = JOURNAL / "posts" / rel.split("/")[0]
        comics = post_dir / "comics.md"
        old = image_path.read_bytes()
        print(f"editing: {rel}", flush=True)
        data, mime = pages.call_image(api_key, args.model, PROMPT, aspect_ratio_of(comics, image_path), old)
        data, _, _ = panels.normalize_image_bytes_for_target(data, mime, image_path)
        pages.archive(image_path, comics, None)
        image_path.write_bytes(data)
        # keep the comic block's recorded hash in step with the new image, without re-rendering comics.md
        old_sha, new_sha = hashlib.sha256(old).hexdigest(), hashlib.sha256(data).hexdigest()
        if comics.exists() and old_sha in (text := comics.read_text(encoding="utf-8")):
            comics.write_text(text.replace(old_sha, new_sha), encoding="utf-8")
        done.add(rel)
        DONE.write_text("\n".join(sorted(done)) + "\n")
        time.sleep(args.sleep)
    print("Done. Inspect every edited image before accepting it.")
    return 0


def aspect_ratio_of(comics: Path, image_path: Path) -> str:
    """The page block's aspect ratio for comic pages; the image's own shape otherwise."""
    if comics.exists():
        try:
            _, _, _, blocks = pages.load(comics)
            for page in blocks:
                if panels.source_image_path(comics, page["asset"]) == image_path:
                    return page.get("aspect_ratio", pages.DEFAULT_ASPECT)
        except ValueError:
            pass
    w, h = panels_size(image_path)
    ratios = {"1:1": 1, "2:3": 2 / 3, "3:2": 1.5, "3:4": 0.75, "4:3": 4 / 3, "9:16": 9 / 16, "16:9": 16 / 9, "4:5": 0.8, "5:4": 1.25}
    return min(ratios, key=lambda k: abs(ratios[k] - w / h))


def panels_size(image_path: Path) -> tuple[int, int]:
    import subprocess
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(image_path)], capture_output=True, text=True).stdout
    vals = [int(line.split()[-1]) for line in out.splitlines() if "pixel" in line]
    return vals[0], vals[1]


if __name__ == "__main__":
    raise SystemExit(main())
