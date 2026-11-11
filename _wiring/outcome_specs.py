#!/usr/bin/env python3
"""Outcome specs: shared library.

Used by validate_spec.py (spec validation), check_draft.py (draft checks) and
build.py (rendering spec.json as the spec page). Standard library only.

The schemas live in _wiring/outcome-specs/*.schema.json. This module contains
a validator for the subset of JSON Schema 2020-12 those files use, the
semantic rules that JSON Schema cannot express (coverage of theses, order
against config.yaml, agreement between journal spec and post spec), a parser
that turns a draft index.md into numbered units, and a renderer that turns a
spec into markdown.
"""

import hashlib
import json
import re
from pathlib import Path

WIRING = Path(__file__).resolve().parent
ROOT = WIRING.parent
SCHEMA_DIR = WIRING / "outcome-specs"
JOURNALS_DIR = ROOT / "_journals"

JOURNAL_SPEC = "journal-spec.json"
POST_SPEC = "spec.json"
CHECK_REPORT = "check-report.json"

# Post kinds that carry structure rather than argument: exempt from the
# orphan rule and from the requirement to have a thesis.
STRUCTURAL_KINDS = {"part_intro", "front_matter", "reference"}

# Second-level headings that are apparatus, not part of the argument. They
# end the conclusion region and are never matched against spec sections.
APPARATUS_HEADINGS = {
    "sources and evidence", "to probe further", "authoritative references",
    "references", "further reading",
}

# Default severity of each standard check (RULES.md, "Check catalogue").
DEFAULT_SEVERITY = {
    "thesis_passes_tests": "blocker",
    "flow_order_is_sound": "major",
    "children_cover_parent_thesis": "blocker",
    "role_matches_journal_spec": "blocker",
    "intro_predicts_content": "major",
    "reverse_outline_matches_spec": "blocker",
    "one_controlling_idea_per_paragraph": "major",
    "paragraph_traces_to_thesis": "major",
    "evidence_is_explained": "major",
    "transition_expresses_declared_relationship": "major",
    "known_before_new": "major",
    "flow_is_followable": "major",
    "no_weak_introduction_pattern": "major",
    "no_weak_conclusion_pattern": "major",
    "conclusion_synthesizes_and_answers_so_what": "major",
    "conclusion_calls_back_to_introduction": "major",
    "custom": "major",
}
# Checks that need a reader (a model or a person); check_draft.py cannot run them.
DRAFT_READER_CHECKS = [c for c in DEFAULT_SEVERITY
                       if c not in ("thesis_passes_tests", "flow_order_is_sound", "children_cover_parent_thesis",
                                    "role_matches_journal_spec", "custom")]
MAX_REVISION_ROUNDS = 2


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# JSON Schema subset validator
# ---------------------------------------------------------------------------

_SCHEMAS = {}


def _schema(name):
    if name not in _SCHEMAS:
        _SCHEMAS[name] = load_json(SCHEMA_DIR / name)
    return _SCHEMAS[name]


def _resolve(ref, doc):
    """Resolve '#/a/b' or 'file.json#/a/b' to (subschema, document name)."""
    name, _, pointer = ref.partition("#")
    name = name or doc
    node = _schema(name)
    for token in [t for t in pointer.split("/") if t]:
        node = node[token.replace("~1", "/").replace("~0", "~")]
    return node, name


_TYPES = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}


def _validate(inst, schema, doc, path, errors):
    if "$ref" in schema:
        target, target_doc = _resolve(schema["$ref"], doc)
        _validate(inst, target, target_doc, path, errors)
    t = schema.get("type")
    if t is not None:
        names = t if isinstance(t, list) else [t]
        if not any(_TYPES[n](inst) for n in names):
            errors.append(f"{path or '/'}: expected {' or '.join(names)}")
            return
    if "const" in schema and inst != schema["const"]:
        errors.append(f"{path or '/'}: must be {schema['const']!r}")
    if "enum" in schema and inst not in schema["enum"]:
        errors.append(f"{path or '/'}: {inst!r} is not one of {', '.join(map(str, schema['enum']))}")
    if isinstance(inst, str) and "pattern" in schema and not re.search(schema["pattern"], inst):
        errors.append(f"{path or '/'}: {inst!r} does not match {schema['pattern']}")
    if isinstance(inst, (int, float)) and not isinstance(inst, bool) and "minimum" in schema \
            and inst < schema["minimum"]:
        errors.append(f"{path or '/'}: must be at least {schema['minimum']}")
    if isinstance(inst, list):
        if len(inst) < schema.get("minItems", 0):
            errors.append(f"{path or '/'}: needs at least {schema['minItems']} item(s)")
        if schema.get("uniqueItems") and len({json.dumps(i, sort_keys=True) for i in inst}) != len(inst):
            errors.append(f"{path or '/'}: items must be unique")
        if "items" in schema:
            for i, item in enumerate(inst):
                _validate(item, schema["items"], doc, f"{path}/{i}", errors)
    if isinstance(inst, dict):
        for key in schema.get("required", []):
            if key not in inst:
                errors.append(f"{path or '/'}: missing required field '{key}'")
        if len(inst) < schema.get("minProperties", 0):
            errors.append(f"{path or '/'}: needs at least {schema['minProperties']} field(s)")
        props = schema.get("properties", {})
        for key, value in inst.items():
            if key in props:
                _validate(value, props[key], doc, f"{path}/{key}", errors)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path or '/'}: unknown field '{key}'")
    for sub in schema.get("allOf", []):
        _validate(inst, sub, doc, path, errors)
    if "anyOf" in schema:
        attempts = []
        for sub in schema["anyOf"]:
            sub_errors = []
            _validate(inst, sub, doc, path, sub_errors)
            if not sub_errors:
                break
            attempts.append(sub_errors)
        else:
            errors.extend(min(attempts, key=len))
    if "if" in schema:
        probe = []
        _validate(inst, schema["if"], doc, path, probe)
        branch = schema.get("then") if not probe else schema.get("else")
        if branch is not None:
            _validate(inst, branch, doc, path, errors)


def schema_errors(instance, schema_name):
    """Validate against one of the outcome-spec schemas; returns error strings."""
    errors = []
    _validate(instance, _schema(schema_name), schema_name, "", errors)
    return list(dict.fromkeys(errors))


# ---------------------------------------------------------------------------
# Semantic rules
# ---------------------------------------------------------------------------

def _coverage(parent, claims, children, errors):
    """children: (label, supports, exempt). Reports gaps, orphans, unknown ids."""
    ids = [c["id"] for c in claims]
    if len(ids) != len(set(ids)):
        errors.append(f"{parent}: duplicate supporting-claim ids")
    used = set()
    for label, supports, exempt in children:
        unknown = sorted(set(supports) - set(ids))
        if unknown:
            errors.append(f"{label}: supports {', '.join(unknown)}, which {parent} does not declare")
        if not supports and not exempt:
            errors.append(f"{label}: orphan, supports no claim of {parent}")
        used |= set(supports)
    for gap in [i for i in ids if i not in used]:
        errors.append(f"{parent}: gap, no child argues for claim {gap}")


def reading_order(journal):
    """All posts of a journal spec in reading order, as (part, post) pairs."""
    return [(part, post) for part in journal["parts"] for post in part["posts"]]


def _config_sections(journal_dir):
    import build  # lazy: build.py imports this module
    cfg = build.parse_yaml((journal_dir / "config.yaml").read_text(encoding="utf-8"))
    out = []
    for section in cfg.get("sections") or []:
        folders = [re.sub(r"/index\.(md|markdown)$", "", p) for p in (section.get("posts") or [])]
        out.append((section.get("title", ""), folders))
    return out


def journal_semantic_errors(journal, journal_dir=None):
    """Rules for a journal spec that already passes its schema."""
    errors = []
    parts = journal["parts"]
    _coverage("journal thesis", journal["thesis"]["supporting_claims"],
              [(f"part {p['id']}", p["role"]["supports"],
                all(q["kind"] in STRUCTURAL_KINDS for q in p["posts"])) for p in parts], errors)
    ids = [q["id"] for _p, q in reading_order(journal)]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"post id {dup} appears more than once")
    for ref in ("opening", "closing"):
        if journal[ref]["carried_by"] not in ids:
            errors.append(f"journal {ref}.carried_by: {journal[ref]['carried_by']} is not a post of this journal")
    for i, part in enumerate(parts):
        label = f"part {part['id']}"
        if i and "transition_in" not in part:
            errors.append(f"{label}: missing transition_in (required on every part but the first)")
        if part["detail"] != "full":
            continue
        _coverage(f"{label} thesis", part["thesis"]["supporting_claims"],
                  [(f"post {q['id']}", q["role"]["supports"], q["kind"] in STRUCTURAL_KINDS)
                   for q in part["posts"]], errors)
        own = [q["id"] for q in part["posts"]]
        for ref in ("opening", "closing"):
            if part[ref]["carried_by"] not in own:
                errors.append(f"{label} {ref}.carried_by: {part[ref]['carried_by']} is not a post of this part")
        for k, post in enumerate(part["posts"]):
            if k and "transition_in" not in post:
                errors.append(f"post {post['id']}: missing transition_in (required on every post but the first of its part)")
    if journal_dir is not None and (journal_dir / "config.yaml").is_file():
        sections = _config_sections(journal_dir)
        if [t for t, _f in sections] != [p["title"] for p in parts]:
            errors.append("part titles or part order differ from the sections in config.yaml")
        if [f for _t, fs in sections for f in fs] != [q["folder"] for _p, q in reading_order(journal)]:
            errors.append("post folders or post order differ from config.yaml")
    return errors


def _containers(post):
    """The post's paragraph containers in reading order: (label, object)."""
    return ([("introduction", post["introduction"])]
            + [(s["id"], s) for s in post["sections"]]
            + [("conclusion", post["conclusion"])])


def post_semantic_errors(post, journal=None):
    """Rules for a post spec that already passes its schema."""
    errors = []
    _coverage("post thesis", post["thesis"]["supporting_claims"],
              [(f"section {s['id']}", s["advances_thesis"]["supports"], False)
               for s in post["sections"]], errors)
    claim_ids = {c["id"] for c in post["thesis"]["supporting_claims"]}
    section_ids = [s["id"] for s in post["sections"]]
    if len(section_ids) != len(set(section_ids)):
        errors.append("duplicate section ids")
    promised = set()
    for promise in post["introduction"]["roadmap"]["promises"]:
        for sid in promise["kept_in"]:
            if sid not in section_ids:
                errors.append(f"roadmap: promise is kept in unknown section {sid}")
            promised.add(sid)
    for sid in section_ids:
        if sid not in promised:
            errors.append(f"section {sid}: not announced by any roadmap promise")
    seen = []
    for label, container in _containers(post):
        if label != "introduction" and "transition_in" not in container:
            errors.append(f"{label}: missing transition_in")
        for k, para in enumerate(container["paragraphs"]):
            where = f"{label}/{para['id']}"
            seen.append(para["id"])
            if k and "transition_in" not in para:
                errors.append(f"{where}: missing transition_in (required on every paragraph but the first of its section)")
            if para["function"] in ("evidence", "example") and not para.get("evidence"):
                errors.append(f"{where}: function is {para['function']} but no evidence is listed")
            unknown = sorted(set(para.get("advances_thesis", {}).get("supports", [])) - claim_ids)
            if unknown:
                errors.append(f"{where}: supports {', '.join(unknown)}, which the post thesis does not declare")
    for dup in sorted({i for i in seen if seen.count(i) > 1}):
        errors.append(f"paragraph id {dup} appears more than once")

    if journal is None:
        return errors
    order = reading_order(journal)
    index = next((i for i, (_p, q) in enumerate(order) if q["id"] == post["id"]), None)
    if index is None:
        return errors + [f"post {post['id']} is not in the journal spec"]
    part, entry = order[index]
    if journal["id"] != post["journal"]:
        errors.append("journal: differs from the journal spec's id")
    if part["id"] != post["part"]:
        errors.append(f"part: journal spec places this post in {part['id']}")
    if entry["detail"] != "full":
        return errors + ["the journal spec holds this post at outline level; specify it in full there first"]
    for field in ("question", "claim", "disputed_by", "so_what", "how_why"):
        if "thesis" in entry and post["thesis"][field] != entry["thesis"][field]:
            errors.append(f"thesis.{field}: differs from the journal spec")
    if post["role"] != entry["role"]:
        errors.append("role: differs from the journal spec")
    if post["intent"]["outcome"] != entry["intent"]["outcome"]:
        errors.append("intent.outcome: differs from the journal spec")
    own = {c["id"]: c for c in post["intent"]["acceptance_criteria"]}
    for criterion in entry["intent"]["acceptance_criteria"]:
        if own.get(criterion["id"]) != criterion:
            errors.append(f"acceptance criterion {criterion['id']}: missing or changed (the post spec may add criteria, not remove or alter them)")
    hand_off = post["conclusion"].get("hand_off")
    if index + 1 < len(order):
        next_part, next_post = order[index + 1]
        if hand_off is None:
            errors.append(f"conclusion.hand_off: missing; the next post is {next_post['id']}")
        else:
            if hand_off["to"] != next_post["id"]:
                errors.append(f"conclusion.hand_off.to: next post in reading order is {next_post['id']}")
            declared = next_post.get("transition_in") if next_part is part else next_part.get("transition_in")
            if declared and declared["relationship"] != hand_off["relationship"]:
                errors.append(f"conclusion.hand_off.relationship: {next_post['id']} declares {declared['relationship']}")
    return errors


def validate_file(path, journal=None, journal_dir=None):
    """Schema then semantic validation of one spec file. Returns (kind, errors)."""
    try:
        doc = load_json(path)
    except (OSError, ValueError) as exc:
        return None, [f"cannot read: {exc}"]
    kind = doc.get("kind") if isinstance(doc, dict) else None
    if kind == "journal":
        errors = schema_errors(doc, "journal-spec.schema.json")
        return kind, errors or journal_semantic_errors(doc, journal_dir)
    if kind == "post":
        errors = schema_errors(doc, "post-spec.schema.json")
        return kind, errors or post_semantic_errors(doc, journal)
    return kind, ["'kind' must be 'journal' or 'post'"]


def flow_outline(doc):
    """The order of ideas of a spec and the flow it declares, as plain text.

    This is all the flow rubric's reader is given: the claims in order and
    the declared pattern and rationale, with no intent, evidence, transitions
    or record keeping, so the order is judged on its own.
    """
    def flow_lines(flow, indent=""):
        extra = "; ".join(f"{a['pattern']} in {a['applies_to']}" for a in flow.get("additional_patterns", []))
        return [f"{indent}Declared order: {flow['pattern']}" + (f" (also {extra})" if extra else ""),
                f"{indent}Declared reason: {flow['rationale']}"]

    out = []
    if doc.get("kind") == "journal":
        out += [f"JOURNAL: {doc['title']}", f"Claim: {doc['thesis']['claim']}"] + flow_lines(doc["flow"]) + [""]
        for n, part in enumerate(doc["parts"], 1):
            out.append(f"{n}. PART {part['title']}: {part['thesis']['claim']}")
            if part.get("flow"):
                out += flow_lines(part["flow"], "   ")
            for k, post in enumerate(part["posts"], 1):
                claim = post.get("thesis", {}).get("claim") or post["question"]
                out.append(f"   {n}.{k} [{post['kind']}] {post['title']}: {claim}")
            out.append("")
        return "\n".join(out)
    out += [f"POST: {doc['title']}", f"Claim: {doc['thesis']['claim']}"] + flow_lines(doc["flow"]) + [""]
    out.append("0. INTRODUCTION")
    out += [f"   0.{k} {p['controlling_idea']}" for k, p in enumerate(doc["introduction"]["paragraphs"], 1)]
    out.append("")
    for n, section in enumerate(doc["sections"], 1):
        out.append(f"{n}. SECTION {section['heading']}: {section['controlling_idea']}")
        if section.get("flow"):
            out += flow_lines(section["flow"], "   ")
        out += [f"   {n}.{k} {p['controlling_idea']}" for k, p in enumerate(section["paragraphs"], 1)]
        out.append("")
    n = len(doc["sections"]) + 1
    out.append(f"{n}. CONCLUSION")
    out += [f"   {n}.{k} {p['controlling_idea']}" for k, p in enumerate(doc["conclusion"]["paragraphs"], 1)]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Draft parsing
# ---------------------------------------------------------------------------

def _body_lines(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
    out, fence = [], None
    for line in lines:
        s = line.strip()
        if fence:
            if s == fence or (fence == "```" and s.startswith("```")):
                fence = None
            continue
        if s.startswith("```"):
            fence = "```"
            continue
        m = re.match(r"^---begin ([\w-]+)---$", s)
        if m:
            fence = f"---end {m.group(1)}---"
            continue
        out.append(line)
    return out


def _blocks(lines):
    block = []
    for line in lines:
        s = line.strip()
        if not s or s.lower() in ("<br>", "<br/>", "<br />"):
            if block:
                yield block
                block = []
        elif s.startswith("#"):
            if block:
                yield block
                block = []
            yield [line]
        else:
            block.append(line)
    if block:
        yield block


def _classify(block):
    first = block[0].strip()
    if first.startswith("#"):
        return "heading"
    if first.startswith("|"):
        return "table"
    if first.startswith(">"):
        return "quote"
    if re.match(r"^([-*+]|\d+[.)])\s", first):
        return "list"
    if first.startswith("!["):
        return "image"
    if re.match(r"^\*\*Figure\s+\d+", first):
        return "caption"
    if first.startswith("<") and not re.search(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}", re.sub(r"<[^>]+>", "", first)):
        return "html"
    return "para"


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9€$£%'’-]+", text))


def unit_locator(region):
    """Locator of the next unit of a region: its heading and a paragraph number."""
    return f"{region['heading'] or 'Introduction'} ¶{len(region['units']) + 1}"


def parse_draft(text):
    """Split a draft into regions of numbered units.

    A unit is what a spec 'paragraph' describes: a prose paragraph, or a list
    together with the paragraph that introduces it. Tables, figures, captions
    and callout blockquotes are attached to the unit before them as
    'attachments' (the spec records them as that paragraph's evidence).

    Returns {"regions": [{"heading", "level", "units": [...]}], "words": n}.
    The first region has heading None: everything before the first '##'.
    Lower-level headings do not start a region; they are kept as a unit
    attachment so locators stay stable.
    """
    regions = [{"heading": None, "units": [], "callouts": []}]
    words = 0
    counting = True
    for block in _blocks(_body_lines(text)):
        kind = _classify(block)
        raw = "\n".join(block)
        region = regions[-1]
        if kind == "heading":
            level = len(block[0].strip()) - len(block[0].strip().lstrip("#"))
            title = block[0].strip().lstrip("#").strip()
            if level <= 2:
                regions.append({"heading": title, "units": [], "callouts": []})
                counting = title.lower() not in APPARATUS_HEADINGS
            elif region["units"]:
                region["units"][-1]["attachments"].append({"kind": "subheading", "text": title})
            else:
                region["callouts"].append({"kind": "subheading", "text": title})
            continue
        if counting and kind in ("para", "list", "table", "quote"):
            words += word_count(raw)
        if kind == "para":
            region["units"].append({"form": "prose", "text": re.sub(r"\s+", " ", raw).strip(), "attachments": [],
                                    "locator": unit_locator(region)})
        elif kind == "list":
            last = region["units"][-1] if region["units"] else None
            if last and last["form"] == "prose" and not last["attachments"]:
                last["form"] = "list"
                last["text"] += "\n" + raw
            else:
                region["units"].append({"form": "list", "text": raw, "attachments": [], "locator": unit_locator(region)})
        elif kind in ("table", "caption", "image", "quote"):
            item = {"kind": kind, "text": raw if kind != "image" else ""}
            (region["units"][-1]["attachments"] if region["units"] else region["callouts"]).append(item)
    return {"regions": regions, "words": words}


def align_regions(post, draft):
    """Match spec containers to draft regions by heading.

    Returns (pairs, findings). pairs: (label, spec container, [draft units]).
    The introduction is everything before the first '##'. The conclusion
    runs from its heading to the first apparatus heading or the end, so
    headings such as 'Questions to Ask' fall inside it.
    """
    findings = []
    regions = draft["regions"]
    body = [r for r in regions[1:]]
    norm = lambda s: re.sub(r"\s+", " ", (s or "").replace("“", '"').replace("”", '"')).strip().lower()
    conclusion_heading = norm(post["conclusion"].get("heading"))
    cut = next((i for i, r in enumerate(body) if conclusion_heading and norm(r["heading"]) == conclusion_heading), None)
    if cut is None:
        apparatus_at = next((i for i, r in enumerate(body) if norm(r["heading"]) in APPARATUS_HEADINGS), len(body))
        cut = len(post["sections"]) if len(post["sections"]) < apparatus_at else apparatus_at
        if conclusion_heading:
            findings.append(f"conclusion heading '{post['conclusion']['heading']}' not found in the draft")
    section_regions, tail = body[:cut], body[cut:]
    conclusion_units = []
    for r in tail:
        if norm(r["heading"]) in APPARATUS_HEADINGS:
            break
        conclusion_units += r["units"]
    spec_headings = [s["heading"] for s in post["sections"]]
    draft_headings = [r["heading"] for r in section_regions]
    if [norm(h) for h in spec_headings] != [norm(h) for h in draft_headings]:
        missing = [h for h in spec_headings if norm(h) not in map(norm, draft_headings)]
        extra = [h for h in draft_headings if norm(h) not in map(norm, spec_headings)]
        if missing:
            findings.append("sections in the spec but not in the draft: " + "; ".join(missing))
        if extra:
            findings.append("sections in the draft but not in the spec: " + "; ".join(extra))
        if not missing and not extra:
            findings.append("sections are in a different order from the spec")
    by_heading = {norm(r["heading"]): r for r in section_regions}
    pairs = [("introduction", post["introduction"], regions[0]["units"])]
    for section in post["sections"]:
        region = by_heading.get(norm(section["heading"]))
        pairs.append((section["id"], section, region["units"] if region else []))
    pairs.append(("conclusion", post["conclusion"], conclusion_units))
    return pairs, findings


# ---------------------------------------------------------------------------
# Rendering a spec as markdown (for the spec page)
# ---------------------------------------------------------------------------

_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def _cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def _link(ref):
    return f"[[{ref}]]" if _SLUG.match(ref) else ref


def _bullets(items):
    return [f"- {i}" for i in items] + [""]


def _intent_md(intent, out):
    labels = (("know", "Know"), ("believe", "Believe"), ("can_do", "Be able to"))
    out.append("**After reading, the reader should:**")
    out.append("")
    for key, label in labels:
        for item in intent["outcome"].get(key, []):
            out.append(f"- **{label}:** {item}")
    out.append("")
    audience = intent.get("audience")
    if audience:
        out += ["**Audience:** " + audience["who"], "", "**Already knows:**", ""]
        out += _bullets(audience["already_knows"])
        if audience.get("does_not_know"):
            out += ["**Does not yet know:**", ""] + _bullets(audience["does_not_know"])
    out += ["**Acceptance criteria**", "", "| Id | Criterion | Check | Method | Severity |", "| --- | --- | --- | --- | --- |"]
    for c in intent["acceptance_criteria"]:
        statement = c["statement"] + (f" *Probe:* {c['probe']}" if c.get("probe") else "")
        out.append(f"| {c['id']} | {_cell(statement)} | `{c['check']}` | {c['method']} | {c['severity']} |")
    out.append("")


def _thesis_md(thesis, out):
    out += [f"**Question:** {thesis['question']}", "", f"> **Claim:** {thesis['claim']}", ""]
    for key, label in (("disputed_by", "Disputed by"), ("so_what", "So what"), ("how_why", "How and why")):
        if thesis.get(key):
            out += [f"**{label}:** {thesis[key]}", ""]
    if thesis.get("supporting_claims"):
        out += ["**Supporting claims**", ""]
        out += _bullets(f"**{c['id']}** — {c['claim']}" for c in thesis["supporting_claims"])


def _flow_md(flow, out):
    extra = "; ".join(f"`{a['pattern']}` in {a['applies_to']}" for a in flow.get("additional_patterns", []))
    out += [f"**Pattern:** `{flow['pattern']}`" + (f" (also {extra})" if extra else ""), "", flow["rationale"], ""]


def _transition_text(t):
    return f"`{t['relationship']}`: {t['carries_over']} → {t['introduces']}" if t else ""


def _paragraphs_md(paragraphs, out):
    out += ["| Id | Function | Controlling idea | Evidence | Transition in |", "| --- | --- | --- | --- | --- |"]
    for p in paragraphs:
        evidence = "; ".join(f"{e['kind']}: {e['what']}" for e in p.get("evidence", []))
        function = p["function"] + (f" ({p['form']})" if p.get("form", "prose") != "prose" else "")
        out.append(f"| {p['id']} | {function} | {_cell(p['controlling_idea'])} | {_cell(evidence)} | "
                   f"{_cell(_transition_text(p.get('transition_in')))} |")
    out.append("")


def _record_md(spec, out):
    if spec.get("non_goals"):
        out += ["## Non-goals", ""]
        for n in spec["non_goals"]:
            where = ", ".join(_link(r) for r in n.get("covered_in", []))
            out.append(f"- {n['topic']}" + (f" See {where}." if where else ""))
        out.append("")
    if "modalities" in spec:
        out += ["## Modalities", "", ("Article, " + ", ".join(spec["modalities"])) if spec["modalities"] else "Article only.", ""]
    if spec.get("open_questions"):
        out += ["## Open questions", ""] + _bullets(spec["open_questions"])
    if spec.get("decision_log"):
        out += ["## Decision log", ""]
        for d in spec["decision_log"]:
            rejected = " Rejected: " + "; ".join(d["rejected"]) if d.get("rejected") else ""
            out.append(f"- **{d['date']}** — {d['decision']}{rejected}")
        out.append("")
    if spec.get("sources"):
        out += ["## Sources", ""]
        for kind, label in (("internal", "Internal"), ("external", "External")):
            items = [s for s in spec["sources"] if s["kind"] == kind]
            if items:
                out.append(f"- **{label}**")
                out += [f"  - {s['ref']} — {s['contributed']}" for s in items]
        out.append("")
    if spec.get("changelog"):
        out += ["## Changelog", ""] + _bullets(f"**{c['date']}** — {c['change']}" for c in spec["changelog"])


def post_spec_markdown(spec):
    """Render a post spec as markdown for the spec page."""
    out = []
    if spec.get("basis"):
        out += [f"> {spec['basis']}", ""]
    out += ["## Intent", ""]
    _intent_md(spec["intent"], out)
    out += ["## Thesis", ""]
    _thesis_md(spec["thesis"], out)
    role = spec["role"]
    out += ["## Role in the part", "", role["contribution"]
            + (f" Supports {', '.join(role['supports'])} of part `{spec['part']}`." if role["supports"] else ""), ""]
    out += ["## Flow", ""]
    _flow_md(spec["flow"], out)
    intro = spec["introduction"]
    out += ["## Introduction", "",
            f"**Hook** (`{intro['hook']['type']}`): {intro['hook']['content']}", "",
            f"**Bridge:** {intro['bridge']['from_reader_world']} → {intro['bridge']['to_topic']}", "",
            f"**Thesis statement** ({intro['thesis_statement']['placement']}): {intro['thesis_statement']['text']}", "",
            f"**Roadmap** ({intro['roadmap']['placement']}):", ""]
    out += _bullets(f"{p['promise']} *Kept in:* {', '.join(p['kept_in'])}." for p in intro["roadmap"]["promises"])
    _paragraphs_md(intro["paragraphs"], out)
    out += ["## Sections", ""]
    for s in spec["sections"]:
        out += [f"### {s['heading']}", "",
                f"**Controlling idea** (`{s['function']}`, id `{s['id']}`): {s['controlling_idea']}", "",
                f"**Advances the thesis** ({', '.join(s['advances_thesis']['supports'])}): {s['advances_thesis']['how']}", ""]
        if s.get("transition_in"):
            out += [f"**Transition in:** {_transition_text(s['transition_in'])}", ""]
        if s.get("flow"):
            out += [f"**Order of paragraphs** (`{s['flow']['pattern']}`): {s['flow']['rationale']}", ""]
        _paragraphs_md(s["paragraphs"], out)
    c = spec["conclusion"]
    out += ["## Conclusion" + (f": {c['heading']}" if c.get("heading") else ""), "",
            f"**Synthesis:** {c['synthesis']}", "", f"**So what:** {c['so_what']}", "",
            f"**Callback:** {c['callback']['to']} {c['callback']['how']}", "",
            f"**Takeaway** (`{c['takeaway']['type']}`): {c['takeaway']['content']}", ""]
    if c.get("hand_off"):
        h = c["hand_off"]
        out += [f"**Hand-off** to {_link(h['to'])}: `{h['relationship']}`: {h['carries_over']} → {h['introduces']}", ""]
    _paragraphs_md(c["paragraphs"], out)
    _record_md(spec, out)
    return "\n".join(out)
