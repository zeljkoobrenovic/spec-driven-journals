#!/usr/bin/env python3
"""Check a draft (index.md) against its post spec (spec.json).

    python3 _wiring/check_draft.py units <post-dir>
        The draft as numbered units, as JSON, with no information from the
        spec. This is what the reverse outliner and the cold reader are given.

    python3 _wiring/check_draft.py structure <post-dir>
        The deterministic checks (sections, unit counts and forms, length,
        hand-off link) and the positional alignment of spec paragraphs to
        draft units, as JSON. This is what the judge is given.

    python3 _wiring/check_draft.py finalize <post-dir> --results <file.json> [--round N]
        Merge the readers' results with the deterministic ones, compute the
        verdict and write check-report.json next to the draft.

    python3 _wiring/check_draft.py status <post-dir>
        Say whether a current, passing report exists. Exit status 0 only then.

<post-dir> is the post folder (…/posts/<folder>), containing index.md and
spec.json. The script runs no model: the reverse outline, the cold-reader
answers and the judge's rulings come from the draft-check skill and reach
this script through --results. Its format:

    {"reverse_outline": [{"draft_locator", "summary", "matched_spec_paragraph"}],
     "results": [{"criterion", "check", "verdict", "spec_locus", "draft_locus",
                  "quote", "finding", "weak_pattern", "fault", "corroborated_by",
                  "waived_by"}]}

'severity' is filled in from the spec's acceptance criteria and the defaults.
A failed known_before_new or flow_is_followable result is minor (recorded,
not blocking) unless it carries 'corroborated_by': a second, independent
reader who reported the same point.
"""

import datetime
import json
import re
import sys
from pathlib import Path

import outcome_specs as osp


def locate(post_dir):
    post_dir = Path(post_dir).resolve()
    spec, draft = post_dir / osp.POST_SPEC, post_dir / "index.md"
    for f in (spec, draft):
        if not f.is_file():
            sys.exit(f"missing {f}")
    journal_dir = next((p for p in post_dir.parents if (p / "config.yaml").is_file()), None)
    journal = None
    if journal_dir and (journal_dir / osp.JOURNAL_SPEC).is_file():
        journal = osp.load_json(journal_dir / osp.JOURNAL_SPEC)
    return post_dir, spec, draft, journal


def rel(path):
    try:
        return str(Path(path).resolve().relative_to(osp.ROOT))
    except ValueError:
        return str(path)


def cmd_units(post_dir):
    _dir, _spec, draft, _journal = locate(post_dir)
    parsed = osp.parse_draft(draft.read_text(encoding="utf-8"))
    out = []
    for region in parsed["regions"]:
        if (region["heading"] or "").lower() in osp.APPARATUS_HEADINGS:
            continue
        for item in region["callouts"]:
            if item["kind"] == "quote":
                out.append({"draft_locator": f"{region['heading'] or 'Introduction'} callout", "form": "callout",
                            "text": item["text"]})
        for unit in region["units"]:
            out.append({"draft_locator": unit["locator"], "form": unit["form"], "text": unit["text"],
                        "attachments": [a["kind"] + (": " + a["text"] if a["kind"] in ("caption", "subheading") else "")
                                        for a in unit["attachments"]]})
    print(json.dumps(out, indent=2, ensure_ascii=False))


def severity_for(post, criterion, check, result=None):
    """Severity from the spec's acceptance criteria, else the default.

    A failed result of an open-ended check (osp.CORROBORATION_CHECKS) that no
    second reader corroborated is minor, unless the spec names that check in
    an acceptance criterion, in which case the spec's severity stands.
    """
    criteria = post["intent"]["acceptance_criteria"]
    for c in criteria:
        if c["id"] == criterion:
            return c["severity"]
    for c in criteria:
        if c["check"] == check and check != "custom":
            return c["severity"]
    if result and check in osp.CORROBORATION_CHECKS and result.get("verdict") == "fail" \
            and not result.get("corroborated_by"):
        return "minor"
    return osp.DEFAULT_SEVERITY[check]


def structure(post_dir):
    """Deterministic results plus the spec-to-draft alignment."""
    _dir, spec_path, draft_path, journal = locate(post_dir)
    kind, errors = osp.validate_file(spec_path, journal=journal)
    if errors:
        print(f"{spec_path} does not validate; fix the spec first:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(2)
    post = osp.load_json(spec_path)
    text = draft_path.read_text(encoding="utf-8")
    draft = osp.parse_draft(text)
    pairs, heading_findings = osp.align_regions(post, draft)
    results, alignment = [], []

    def fail(check, finding, spec_locus=None, draft_locus=None, criterion=None):
        r = {"criterion": criterion or check, "check": check, "verdict": "fail",
             "severity": severity_for(post, criterion, check), "finding": finding, "fault": "draft"}
        if spec_locus:
            r["spec_locus"] = spec_locus
        if draft_locus:
            r["draft_locus"] = draft_locus
        results.append(r)

    for finding in heading_findings:
        fail("reverse_outline_matches_spec", finding)
    for index, (label, container, units) in enumerate(pairs):
        pointer = ("/introduction" if label == "introduction" else "/conclusion" if label == "conclusion"
                   else f"/sections/{index - 1}")
        heading = None if label == "introduction" else container.get("heading")
        paragraphs = container["paragraphs"]
        if len(units) != len(paragraphs):
            fail("reverse_outline_matches_spec",
                 f"{label}: the spec has {len(paragraphs)} paragraph(s), the draft has {len(units)} unit(s); "
                 "something was added, dropped, merged or split",
                 spec_locus=pointer + "/paragraphs", draft_locus=heading or "Introduction")
        for k, para in enumerate(paragraphs):
            unit = units[k] if k < len(units) else None
            where = unit["locator"] if unit else None
            alignment.append({"spec_paragraph": para["id"], "spec_locus": f"{pointer}/paragraphs/{k}",
                              "container": label, "draft_locator": where,
                              "draft_text": unit["text"] if unit else None,
                              "draft_attachments": [a["kind"] for a in unit["attachments"]] if unit else []})
            if unit and len(units) == len(paragraphs):
                want = "list" if para.get("form") == "list" else "prose"
                if para.get("form", "prose") in ("prose", "list") and unit["form"] != want:
                    fail("reverse_outline_matches_spec",
                         f"{para['id']}: the spec asks for {want}, the draft has {unit['form']}",
                         spec_locus=f"{pointer}/paragraphs/{k}", draft_locus=where)
    limit = post.get("length", {}).get("max_words")
    if limit and draft["words"] > limit:
        results.append({"criterion": "length", "check": "custom", "verdict": "fail", "severity": "major",
                        "finding": f"the draft has {draft['words']} words; the spec allows {limit}", "fault": "draft"})
    hand_off = post["conclusion"].get("hand_off")
    if hand_off:
        tail = " ".join(u["text"] for u in pairs[-1][2][-2:])
        if not re.search(r"\[\[" + re.escape(hand_off["to"]) + r"\]\]|\(" + re.escape(hand_off["to"]) + r"\.html\)", tail):
            fail("transition_expresses_declared_relationship",
                 f"the closing units do not link to the next post, {hand_off['to']}",
                 spec_locus="/conclusion/hand_off", draft_locus="Conclusion")
    if not any(r["check"] == "reverse_outline_matches_spec" for r in results):
        results.append({"criterion": "structure", "check": "reverse_outline_matches_spec", "verdict": "pass",
                        "severity": severity_for(post, None, "reverse_outline_matches_spec"),
                        "finding": "sections, unit counts and unit forms match the spec"})
    return post, spec_path, draft_path, {"words": draft["words"], "results": results, "alignment": alignment}


def cmd_structure(post_dir):
    _post, _spec, _draft, out = structure(post_dir)
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_finalize(post_dir, results_path, round_no):
    post, spec_path, draft_path, det = structure(post_dir)
    supplied = osp.load_json(results_path)
    results = list(det["results"])
    for r in supplied.get("results", []):
        r = dict(r)
        if r.get("check") not in osp.DEFAULT_SEVERITY:
            sys.exit(f"unknown check in results: {r.get('check')!r}")
        r.setdefault("criterion", r["check"])
        r["severity"] = severity_for(post, r["criterion"], r["check"], r)
        if r.get("verdict") == "fail" and r["check"] != "reverse_outline_matches_spec" \
                and osp.DEFAULT_SEVERITY.get(r["check"]) and not r.get("quote") and not r.get("finding"):
            sys.exit(f"failed result for {r['criterion']} has neither a quote nor a finding")
        if r.get("verdict") == "waived" and not r.get("waived_by"):
            sys.exit(f"waived result for {r['criterion']} must say who waived it and why (waived_by)")
        results.append(r)

    have_checks = {r["check"] for r in results}
    have_criteria = {r["criterion"] for r in results}
    missing = [c for c in osp.DRAFT_READER_CHECKS if c not in have_checks]
    missing += [c["id"] for c in post["intent"]["acceptance_criteria"]
                if c["id"] not in have_criteria and c["check"] == "custom"]
    if not any(r.get("check") == "reverse_outline_matches_spec"
               for r in supplied.get("results", [])):
        missing.append("reverse_outline_matches_spec (the reverse outliner's ruling; the script only checks structure)")
    if missing:
        sys.exit("no result supplied for: " + ", ".join(dict.fromkeys(missing)))

    failing = [r for r in results if r["verdict"] == "fail" and r["severity"] in ("blocker", "major")]
    if not failing:
        verdict = "pass"
    elif any(r.get("fault") == "spec" for r in failing) or round_no > osp.MAX_REVISION_ROUNDS:
        verdict = "escalate"
    else:
        verdict = "revise"
    report = {
        "spec": rel(spec_path), "draft": rel(draft_path),
        "spec_sha": osp.sha(spec_path), "draft_sha": osp.sha(draft_path),
        "run_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "round": round_no, "verdict": verdict,
    }
    if supplied.get("reverse_outline"):
        report["reverse_outline"] = supplied["reverse_outline"]
    report["results"] = results
    errors = osp.schema_errors(report, "check-report.schema.json")
    if errors:
        sys.exit("the assembled report does not validate:\n  " + "\n  ".join(errors))
    out = Path(post_dir).resolve() / osp.CHECK_REPORT
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = {v: sum(1 for r in results if r["verdict"] == v) for v in ("pass", "fail", "waived")}
    print(f"{verdict.upper()}  round {round_no}  pass={counts['pass']} fail={counts['fail']} waived={counts['waived']}  -> {rel(out)}")
    for r in failing:
        print(f"  [{r['severity']}] {r['criterion']} ({r.get('fault', 'unclear')}): {r.get('finding', '')}")
    minor = [r for r in results if r["verdict"] == "fail" and r["severity"] == "minor"]
    if minor:
        print(f"  {len(minor)} minor finding(s) recorded, not blocking:")
        for r in minor:
            note = "" if r["check"] not in osp.CORROBORATION_CHECKS else " (one reader only)"
            print(f"    [minor] {r['criterion']}{note}: {r.get('finding', '')}")
    if verdict == "escalate":
        print("  Stop revising: a failure points at the spec, or the revision budget is spent. The author decides.")
    sys.exit(0 if verdict == "pass" else 1)


def cmd_status(post_dir):
    post_dir, spec, draft, _journal = locate(post_dir)
    path = post_dir / osp.CHECK_REPORT
    if not path.is_file():
        print("unchecked: no check-report.json")
        sys.exit(1)
    report = osp.load_json(path)
    stale = [n for n, f in (("spec", spec), ("draft", draft)) if report.get(f"{n}_sha") != osp.sha(f)]
    if stale:
        print(f"stale: the {' and the '.join(stale)} changed after the report of {report.get('run_at')}; check again")
        sys.exit(1)
    print(f"{report['verdict']}: round {report['round']}, {report['run_at']}")
    sys.exit(0 if report["verdict"] == "pass" else 1)


def main(argv):
    if len(argv) < 2 or argv[0] not in ("units", "structure", "finalize", "status"):
        sys.exit(__doc__)
    command, post_dir = argv[0], argv[1]
    if command == "units":
        cmd_units(post_dir)
    elif command == "structure":
        cmd_structure(post_dir)
    elif command == "status":
        cmd_status(post_dir)
    else:
        if "--results" not in argv:
            sys.exit("finalize needs --results <file.json>")
        round_no = int(argv[argv.index("--round") + 1]) if "--round" in argv else 1
        cmd_finalize(post_dir, argv[argv.index("--results") + 1], round_no)


if __name__ == "__main__":
    main(sys.argv[1:])
