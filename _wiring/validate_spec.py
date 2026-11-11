#!/usr/bin/env python3
"""Validate outcome specs before any prose is drafted from them.

    python3 _wiring/validate_spec.py <journal>              # journal-spec.json and every posts/**/spec.json
    python3 _wiring/validate_spec.py <journal> <folder>     # the journal spec and one post spec
    python3 _wiring/validate_spec.py --file <spec.json> [--journal-spec <journal-spec.json>]

<journal> is a directory name under _journals/. Two layers run for each file:
the JSON Schema in _wiring/outcome-specs/, then the semantic rules (thesis
coverage, transitions, order against config.yaml, agreement between the
journal spec and the post spec). Exit status is 1 if any file has errors.

This does not judge whether a thesis is any good; that is the thesis rubric
in the journal-spec and spec-creator skills.
"""

import sys
from pathlib import Path

import outcome_specs as osp


def report(label, kind, errors):
    if errors:
        print(f"FAIL  {label}" + (f" ({kind} spec)" if kind else ""))
        for e in errors:
            print(f"      {e}")
    else:
        print(f"ok    {label} ({kind} spec)")
    return not errors


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        sys.exit(__doc__)
    if argv[0] == "--file":
        path = Path(argv[1])
        journal = None
        if "--journal-spec" in argv:
            journal = osp.load_json(argv[argv.index("--journal-spec") + 1])
        kind, errors = osp.validate_file(path, journal=journal)
        if kind == "post" and journal is None and not errors:
            print("note  no --journal-spec given: agreement with the journal spec was not checked")
        sys.exit(0 if report(str(path), kind, errors) else 1)

    journal_dir = osp.JOURNALS_DIR / argv[0]
    if not journal_dir.is_dir():
        sys.exit(f"no such journal: {journal_dir}")
    ok = True
    journal = None
    journal_path = journal_dir / osp.JOURNAL_SPEC
    if journal_path.is_file():
        kind, errors = osp.validate_file(journal_path, journal_dir=journal_dir)
        ok &= report(f"{argv[0]}/{osp.JOURNAL_SPEC}", kind, errors)
        if not errors:
            journal = osp.load_json(journal_path)
    else:
        print(f"note  {argv[0]} has no {osp.JOURNAL_SPEC}; post specs are checked on their own")

    posts_dir = journal_dir / "posts"
    if len(argv) > 1:
        post_specs = [posts_dir / argv[1] / osp.POST_SPEC]
        if not post_specs[0].is_file():
            sys.exit(f"no such file: {post_specs[0]}")
    else:
        post_specs = sorted(posts_dir.glob(f"**/{osp.POST_SPEC}"))
    for path in post_specs:
        kind, errors = osp.validate_file(path, journal=journal)
        ok &= report(str(path.relative_to(journal_dir)), kind, errors)

    if len(argv) == 1:
        with_json = {p.parent for p in post_specs}
        legacy = [p for p in posts_dir.glob("**/spec.md") if p.parent not in with_json]
        print(f"\n{len(post_specs)} post spec(s) in {osp.POST_SPEC}; {len(legacy)} post(s) still on spec.md")
        if journal:
            full = [q for _p, q in osp.reading_order(journal) if q["detail"] == "full"]
            missing = [q["folder"] for q in full if not (posts_dir / q["folder"] / osp.POST_SPEC).is_file()]
            print(f"{len(full)} post(s) specified in full in the journal spec; {len(missing)} of them have no {osp.POST_SPEC} yet")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv[1:])
