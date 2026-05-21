#!/usr/bin/env python3
"""One-off script: backfill stub spec.md for every post in selected journals.

For each post folder under _journals/<journal>/posts/**/index.md that does not
already have a sibling spec.md, write a stub spec using the 7-section template.
Intent comes from the post's `excerpt:` front matter (or `title:`). Decision
log and Sources are deliberately stubbed with TODO markers — they get filled
in during the next real session that touches the post.

Usage:
    python3 _wiring/_backfill_specs.py <journal> [<journal> ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNALS = ROOT / "_journals"


def parse_front_matter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = text[3:end].strip()
    meta = {}
    for line in fm.splitlines():
        line = line.rstrip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        v = value.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        meta[key.strip()] = v
    return meta, text[end + 4:]


SPEC_TEMPLATE = """\
---
status: draft
revised: 2026-05-20
---

# Spec: {title}

> Stub spec backfilled when the spec-driven convention was rolled out
> across the journal. Status `draft` until a session walks the post
> against the spec and either accepts the contract or rewrites it.

## Intent

{intent}

## Audience

- TODO: name the specific reader(s) and what they should walk away with.
  Replace this list during the next session that touches this post.

## Success criteria

- [ ] TODO: write 3-5 checkable items a reviewer can verify against the
      post.

## Non-goals

- TODO: list what this post deliberately does **not** cover, so future
  sessions don't drift into adjacent topics.

## Open questions

- TODO: capture anything still unresolved. If everything in the post is
  settled, leave a single bullet noting that.

## Decision log

- **2026-05-20** — Stub backfilled. Real decision log entries (chosen
  options + rejected alternatives + reasons) are captured during the
  next session that revisits this post. *(automated backfill)*

## Sources

- **Internal**
  - TODO: link sibling records the post depends on via `[[name]]`.
- **External**
  - TODO: name external references the post draws from.

## Changelog

- **2026-05-20** — Stub backfilled as part of journal-wide spec-driven
  rollout. Status `draft`; spec has not yet been reviewed against the
  post. *(automated backfill)*
"""


def intent_from_meta(meta: dict) -> str:
    excerpt = meta.get("excerpt", "").strip()
    title = meta.get("title", "").strip()
    if excerpt:
        parts = excerpt.replace("—", "-").split(". ")
        short = ". ".join(parts[:2]).rstrip(".") + "."
        return short
    if title:
        return (
            f'Capture the contract behind "{title}". '
            "TODO: replace this placeholder during the next session "
            "that touches the post."
        )
    return "TODO: state what this post needs to land."


def write_spec(post_path: Path, overwrite: bool = False) -> bool:
    spec_path = post_path.parent / "spec.md"
    if spec_path.exists() and not overwrite:
        return False
    text = post_path.read_text(encoding="utf-8")
    meta, _ = parse_front_matter(text)
    title = meta.get("title", post_path.parent.name)
    intent = intent_from_meta(meta)
    spec_path.write_text(
        SPEC_TEMPLATE.format(title=title, intent=intent),
        encoding="utf-8",
    )
    return True


def main(args):
    overwrite = "--overwrite" in args
    journals = [a for a in args if not a.startswith("--")]
    written = 0
    skipped = 0
    for j in journals:
        jdir = JOURNALS / j
        if not jdir.is_dir():
            print(f"[skip] {j}: not a directory", file=sys.stderr)
            continue
        for post in sorted(jdir.glob("posts/**/index.md")):
            if write_spec(post, overwrite=overwrite):
                written += 1
                print(f"[wrote] {post.parent.relative_to(JOURNALS)}/spec.md")
            else:
                skipped += 1
    print(f"\ndone: wrote {written}, skipped {skipped}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:])
