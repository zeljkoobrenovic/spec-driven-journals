---
name: spec-creator
description: Create or refine a post's spec.json — the outcome spec that drives a spec-driven journal post (intent, thesis, sections and paragraphs with their transitions, introduction, conclusion, acceptance criteria) — from source material (an INPUT.md, raw notes, a described intent) and the journal spec. Use when asked to create, draft, write, improve, or polish a spec, spec.json, or "the contract" for a post in _journals/*/posts/*/, before the article (index.md) is written, or to convert a post's older spec.md to spec.json.
---

# Spec Creator (the `spec.json` contract)

## Goal

Produce or improve `_journals/<journal>/posts/<slug>/spec.json`: the contract
the article is written from and checked against. It says what the reader
should know, believe or be able to do afterwards, the one claim the post
makes, and the order of ideas down to each paragraph, with the transition
into each.

This skill writes **only** the spec. `detailed-article` writes `index.md`
from it; `draft-check` checks the result. A good spec is one a different
agent could draft from without asking the author what they meant, and a
reader who never saw it could be tested against.

`spec.json` replaces the older `spec.md`. Posts that still have only a
`spec.md` keep working as before; convert one only when asked (see
"Converting a `spec.md`").

## Read first

- `_wiring/outcome-specs/post-spec.schema.json` and `common.schema.json`: the
  fields, with a description of each.
- `_wiring/outcome-specs/RULES.md`: the rule behind each field and the checks
  a draft will face.
- `_wiring/outcome-specs/examples/boundaries-and-systems-of-record.post-spec.json`:
  a worked example.

## Contract rules

- **The journal spec comes first.** If `_journals/<journal>/journal-spec.json`
  exists, the post must have a `full` entry there. Copy `intent.outcome`,
  the entry's acceptance criteria, the thesis (`question`, `claim`,
  `disputed_by`, `so_what`, `how_why`) and `role` from it unchanged. If the
  entry is missing or at `outline`, stop and say so: that is the
  `journal-spec` skill's job. If the journal has no journal spec, write those
  fields here and say that agreement with a journal spec was not checked.
- **Outcome, not coverage.** An acceptance criterion states what a reader can
  do or what the text demonstrably does. "A table shows the four options" is
  an inventory; "given two options, the reader says which fits a one-channel
  merchant and why" is a criterion. Give every `cold_reader` criterion a
  `probe` (the exact question) and an `expected` answer.
- **One controlling idea per paragraph.** Write each as a full sentence a
  topic sentence could state. If it needs "and" to join two ideas, it is two
  paragraphs. A table, list or figure that belongs to a paragraph is that
  paragraph's `evidence`; a list that stands as its own unit has
  `"form": "list"`.
- **Evidence says what it shows.** Every `evidence` item has `what` (the
  figure, quotation or case itself) and `shows` (why it supports the
  controlling idea). Do not invent evidence: if the source material has none
  for a claim, leave the paragraph out or record an open question.
- **Choose the relationship before the words.** Each `transition_in` names
  the logical relationship to the previous unit, what is carried over, and
  what is introduced. If no relationship from the list fits, the order is
  wrong.
- **Don't decide what is the author's to decide.** Audience, the claim, and
  what the reader is left with are theirs. Use `AskUserQuestion` for the few
  choices that change what gets written; choose defaults for the rest and
  record them in `decision_log` with the alternatives rejected.

## Workflow

1. **Find the source.** `INPUT.md` or notes in the post folder, or intent
   described in the request. If there is none, stop and ask; do not invent
   content.
2. **Read the context.** The post's entry and its neighbours' entries in
   `journal-spec.json`; `config.yaml`; the journal's style guide and ledger
   if it has them. The neighbours' entries tell you what the reader already
   knows and what this post must not re-teach.
3. **Top of the spec.** `intent` (copied, plus `audience` where this post
   narrows the journal's), `thesis` (copied), `role` (copied), and the post's
   own `supporting_claims`: the three to six claims that together establish
   the thesis.
4. **Sections.** One per supporting claim or step of the argument. For each:
   `heading`, `controlling_idea`, `function`, `advances_thesis`, and
   `transition_in`. Then the post-level `flow`: the pattern and why this
   order serves the reader.
5. **Paragraphs.** For each section, the paragraphs in order: `controlling_idea`,
   `function`, `evidence`, `transition_in` (all but the first). Add the
   section's own `flow` when it has more than two paragraphs.
6. **Introduction and conclusion last**, because both depend on the body.
   - Introduction: a `hook` that is the actual scenario, example or question,
     not a description of one; the `bridge` from the reader's world to the
     topic; where the thesis is stated; a `roadmap` whose promises each name
     the sections that keep them.
   - Conclusion: a `synthesis` that says something no single section says; an
     answer to "so what?"; a `callback` to the hook; a `takeaway`; and the
     `hand_off` to the next post, using the relationship that post declares
     in the journal spec.
7. **Record keeping.** `non_goals` (with `covered_in` where another post owns
   the topic), `modalities` (empty means article only), `open_questions`,
   `decision_log`, `sources`, `changelog`. Set `status: "draft"` and
   `revised` to today.
8. **Validate:** `python3 _wiring/validate_spec.py <journal> <folder>`. Fix
   every error. Typical ones: a section no roadmap promise announces, a
   supporting claim no section argues for, a hand-off that disagrees with the
   next post's `transition_in`.
9. **Thesis rubric**, when the thesis was written here rather than copied:
   as in the `journal-spec` skill, a fresh agent given only the thesis object.
10. **Build** if the post is wired and has an `index.md`:
    `python3 _wiring/build.py`. The spec renders as
    `docs/<journal>/<slug>.spec.html`.

Leave `status: draft`. The author sets `accepted`; no article is drafted
from a spec that is not accepted.

## Improving an existing spec

- Read the whole spec and, if it exists, `check-report.json`: failed results
  with `"fault": "spec"` say where the spec is wrong.
- Change the smallest unit that fixes the problem. Reordering paragraphs or
  sections invalidates the `transition_in` of every unit whose predecessor
  changed; rewrite those.
- Do not change `intent`, the thesis or `role` here when a journal spec
  exists. Change them there first.
- Add a `changelog` entry and update `revised`. If an `index.md` exists, say
  that its check report is now stale and which units need redrafting.

## Converting a `spec.md`

Only when asked, for the post named.

1. Carry over Non-goals, Modalities, Open questions, Decision log, Sources
   and Changelog as the fields of the same names.
2. Do not carry Success criteria over as they are: most are inventories.
   Rewrite each as an outcome, or drop it and say so.
3. If `index.md` exists, reconstruct sections and paragraphs from it in its
   own order (`python3 _wiring/check_draft.py units <post-dir>` lists the
   units), and write `basis` saying the spec was reconstructed. Where the
   contract asks for something the published text does not do, record it
   under `open_questions`; do not describe the text as doing it.
4. Validate, then delete `spec.md` so the post has one contract.

## Report

File written; validator result; which fields were copied from the journal
spec; decisions taken by default; open questions; for a conversion, the
success criteria rewritten or dropped.

## Anti-patterns

- Writing `index.md` or modality files. This skill stops at the spec.
- Inventing source material or evidence the author did not provide.
- Acceptance criteria that list what the post contains.
- A controlling idea that is a topic ("Pricing") rather than a sentence.
- `sequence` as the relationship for every transition.
- A conclusion whose synthesis is a list of the section headings.
- Editing intent, thesis or role away from the journal spec.
- Setting `status: accepted` yourself.
