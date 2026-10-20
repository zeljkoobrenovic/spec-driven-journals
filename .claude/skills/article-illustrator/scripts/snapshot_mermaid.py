#!/usr/bin/env python3
"""Screenshot every rendered mermaid diagram of built post pages, as layout references.

Usage from the repository root (needs Playwright; run after python3 _wiring/build.py):

    python3.11 snapshot_mermaid.py <journal> <out-dir> [post-folder ...]

Writes <out-dir>/<post-folder>/<k>.png for the k-th mermaid block of each post,
in document order, which is the order mermaid_to_illustrations.py stages them.
The image model redraws from these, so boxes and arrows keep their structure.
"""

import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    journal, out = sys.argv[1], Path(sys.argv[2])
    only = set(sys.argv[3:])
    posts = Path("_journals") / journal / "posts"
    docs = Path("docs") / journal
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2)
        for index in sorted(posts.glob("*/index.md")):
            folder = index.parent.name
            text = index.read_text(encoding="utf-8")
            if (only and folder not in only) or "---begin mermaid---" not in text:
                continue
            permalink = re.search(r"^permalink:\s*\"?([^\"\n]+)", text, re.M).group(1).strip()
            page.goto((docs / f"{permalink}.html").resolve().as_uri())
            page.wait_for_timeout(2500)
            svgs = page.locator(".mermaid svg")
            expected = text.count("---begin mermaid---")
            if svgs.count() != expected:
                print(f"WARN {folder}: {svgs.count()} rendered, {expected} in source")
            (out / folder).mkdir(parents=True, exist_ok=True)
            for k in range(svgs.count()):
                svg = svgs.nth(k)
                svg.scroll_into_view_if_needed()
                svg.screenshot(path=str(out / folder / f"{k + 1}.png"), omit_background=False)
            print(f"{folder}: {svgs.count()} diagram(s)")
        browser.close()


if __name__ == "__main__":
    main()
