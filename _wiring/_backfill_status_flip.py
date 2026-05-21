#!/usr/bin/env python3
"""One-off script: flip post `status:` and highlight `**Status**:` value to
`draft:gray` / `DRAFT` across selected journals.

Only touches:
  - The first `status:` line in front matter (skips later ones in code blocks).
  - The first `> **Status**:` line in the body (skips code-block examples).

Usage:
    python3 _wiring/_backfill_status_flip.py <journal> [<journal> ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNALS = ROOT / "_journals"


FM_STATUS = re.compile(r"^status:\s*[^\n]+$", re.MULTILINE)
BODY_STATUS = re.compile(r"^> \*\*Status\*\*:\s*[^\n]+$", re.MULTILINE)


def flip(text: str):
    fm_done = False
    body_done = False

    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[:end]
            new_fm, n = FM_STATUS.subn("status: draft:gray", fm, count=1)
            if n:
                text = new_fm + text[end:]
                fm_done = True

    new_body, n = BODY_STATUS.subn("> **Status**: DRAFT", text, count=1)
    if n:
        text = new_body
        body_done = True

    return text, fm_done, body_done


def main(journal_names):
    fm_flipped = 0
    body_flipped = 0
    untouched = 0
    for j in journal_names:
        jdir = JOURNALS / j
        if not jdir.is_dir():
            print(f"[skip] {j}: not a directory", file=sys.stderr)
            continue
        for post in sorted(jdir.glob("posts/**/index.md")):
            old = post.read_text(encoding="utf-8")
            new, fm, body = flip(old)
            if new == old:
                untouched += 1
                continue
            post.write_text(new, encoding="utf-8")
            if fm:
                fm_flipped += 1
            if body:
                body_flipped += 1
            tags = []
            if fm:
                tags.append("fm")
            if body:
                tags.append("body")
            print(f"[flip {','.join(tags):>9}] {post.relative_to(JOURNALS)}")
    print(
        f"\ndone: front-matter={fm_flipped}, body={body_flipped}, "
        f"untouched={untouched}"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:])
