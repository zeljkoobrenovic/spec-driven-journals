# Pipeline: where it stands and what is proposed

Status: schemas approved by the author on 11 November 2026; the pipeline in
section 2 is implemented (validator, draft checker, build rendering, skills).
No existing journal has been converted: section 1 still describes how every
current post was produced, and posts with only a `spec.md` keep working that
way until they are converted.

## 1. The pipeline today

### Where journals, parts and posts are defined

| Level | Defined in | What it holds | Read by |
| --- | --- | --- | --- |
| Journal | `_journals/<j>/config.yaml` | Title, description, logo, `ai_credit`, the list of sections | `build.py` |
| Journal (books only) | `_journals/<j>/PLAN.md` | Positioning, the central idea, the structure table, the teaching discipline, one "chapter contract" per page (folder, permalink, title, the question, what to cover, the terms it owns, the briefs) | Writer and reviewer agents, by instruction. Nine journals have one. |
| Journal (books only) | `_journals/<j>/_research/` | `style-guide.md`, `scenario-ledger.md`, `brief-*.md`, and the role briefs (`WRITER-BRIEF.md`, `REVIEWER-BRIEF.md`, `INTRO-BRIEF.md`, `ILLUSTRATOR-BRIEF.md`) | Writer and reviewer agents |
| Part | `sections:` in `config.yaml` (title, description) and a `part-N-intro` post | A title, a one-sentence description and a page that lists the part's chapters | `build.py`; readers |
| Post | `posts/<slug>/spec.md` | Intent, Audience, Success criteria, Non-goals, Modalities, Open questions, Decision log, Sources, Changelog; `status` and `revised` in front matter | Authoring skills; rendered as the spec page |
| Post | `posts/<slug>/index.md` and modality files | The prose | `build.py` |

750 of the 832 posts have a `spec.md`.

### What each generation step receives

| Step | Done by | Inputs | Output |
| --- | --- | --- | --- |
| Plan a book | An agent session with the author | Source material, research briefs | `PLAN.md`, `config.yaml`, `_research/*` |
| Write a spec | `spec-creator` skill | `INPUT.md` or notes, `config.yaml`, one or two neighbouring specs, `_wiring/spec-template.md` | `spec.md` |
| Write a post | `detailed-article` skill | `spec.md`, one or two neighbouring posts, the house style | `index.md`; walks the Success criteria itself |
| Write a book chapter | A writer agent under `WRITER-BRIEF.md` | Style guide, `PLAN.md` contract, scenario ledger, research briefs, a model chapter | `index.md` **and** `spec.md`, in the same pass |
| Review | A reviewer agent under `REVIEWER-BRIEF.md`; `post-review` skill | Style guide, ledger, `PLAN.md`, the post and its spec | Edits; `REVIEW.md` |
| Sharpen | `sharpen-post` skill | `index.md`, optionally `spec.md` | A shorter `index.md`; `skeleton.py` prints the heading outline and each paragraph's first sentence |
| Build | `_wiring/build.py` | `config.yaml`, `index.md`, modality files, `spec.md` | `docs/<j>/…`; no generation and no checking of prose |

### What this leaves unspecified

1. **No journal-level or part-level argument is written down in a checkable
   form.** `PLAN.md` gives the central idea as prose and each chapter's
   question and coverage list. It does not say which claim each part
   establishes, how the parts add up, or what connects one chapter to the
   next.
2. **Success criteria are content inventories.** The nine criteria in chapter
   4's `spec.md` each say what the chapter contains ("A table shows…", "Three
   mermaid diagrams…"). None says what a reader can do afterwards.
3. **In the book workflow the spec is written with the post**, by the same
   writer in the same pass, and its boxes are ticked by that writer. It
   describes the post; it does not constrain it.
4. **Order of ideas is not specified below the section list**, so nothing can
   detect a paragraph that carries two ideas, an example nobody explains, or a
   transition that claims a relationship the two paragraphs do not have.
5. **Checks are run by the agent that wrote the text**, with the spec in
   view. There is no reader who sees only the prose.

### Where the new specs plug in

| New artifact | Location | Replaces or extends | Consumed by |
| --- | --- | --- | --- |
| Journal spec | `_journals/<j>/journal-spec.json` | The positioning, structure and "question" half of `PLAN.md`; adds theses, roles, flow and transitions. `config.yaml` stays the build's input and is cross-checked against it. | Post-spec authoring; part-intro and introduction writers; the validator |
| Post spec | `_journals/<j>/posts/<slug>/spec.json` | `spec.md` entirely: its Intent, Audience and Success criteria become the outcome fields, and its other six sections are carried as fields | The writer; the check step |
| Check report | `_journals/<j>/posts/<slug>/check-report.json` | The writer's self-check in `detailed-article` step 4 and the alignment layer of `post-review` | The revise step; the author |

Style guides, scenario ledgers and research briefs are untouched: they govern
voice, facts and evidence, which these specs do not.

## 2. The pipeline

```
journal spec ──validate──▶ post spec ──validate──▶ draft ──check──▶ pass ──▶ accepted
     ▲            │            ▲           │          ▲       │
     └── fix ◀────┘            └── fix ◀───┘          │       ├─ fail, fault = draft ──▶ revise (2 rounds) ─┐
                                                      │       │                                              │
                                                      └───────┼──────────────────────────────────────────────┘
                                                              └─ fail, fault = spec, or budget spent ──▶ author
```

### Step 1. Spec

1. The journal spec is written top-down: journal intent and thesis with its
   supporting claims, then every part at `outline` (question, claim, role,
   transition), then one part at a time to `full`.
2. A post spec is created from its journal entry (intent, thesis and role are
   copied, never retyped), then the sections, then the paragraphs, then the
   introduction and conclusion last, because both depend on the body.
3. The author reviews and sets `status: accepted`. No draft is generated from
   a spec in `draft`.

### Step 2. Validate (no prose yet)

Two layers, both of which must pass before the author is asked to accept.

- **Schema**: the file validates against its JSON Schema.
- **Semantic rules**, deterministic:
  - every supporting claim has a supporting child, every arguing child
    supports a claim, no child cites an unknown claim;
  - every child after the first has a `transition_in`;
  - parts and posts appear in `config.yaml` order with matching titles and folders;
  - `opening.carried_by` and `closing.carried_by` name posts of the unit;
  - the post spec's intent outcome, thesis and role equal the journal entry;
  - every roadmap promise points at a section and every section is promised;
  - paragraphs with function `evidence` or `example` have evidence, and every
    evidence item says what it shows;
  - `conclusion.hand_off` names the next post and uses the relationship that
    post declares.
- **Thesis rubric**, one model call per thesis by a judge that sees only the
  thesis object: does the claim answer the question, could a reasonable
  reader dispute it, is it free of vague evaluative words, and are `so_what`
  and `how_why` more than restatements?

The semantic rules were run once, as a throwaway script, against the two
examples in `examples/`; both pass, and eight deliberately broken variants
were each rejected by the schemas.

**When validation fails**, the spec stays in `draft`, the failures are listed
by JSON pointer, and nothing downstream runs. A gap or orphan is fixed in the
parent (add or drop a supporting claim) or the child (change what it
supports), which is an editorial decision and is not made automatically.

### Step 3. Draft

The writer receives the accepted post spec, the journal's style guide, ledger
and briefs, and the previous and next posts' journal entries. It writes
`index.md` paragraph by paragraph in spec order. It may not add, drop, merge
or reorder paragraphs; if it finds it must, it stops and reports why, which
is a spec fault (see step 5).

### Step 4. Check the draft against the spec

Four readers, kept apart so that none marks its own work and none sees more
than its check needs.

| Reader | Sees | Does | Checks |
| --- | --- | --- | --- |
| Script | Spec and draft | Compares headings, paragraph counts per section, length, the hand-off link, cross-link targets | The structural half of `reverse_outline_matches_spec`; length |
| Reverse outliner | The draft only | Writes one short phrase per paragraph; flags any paragraph that needs two | `reverse_outline_matches_spec`, `one_controlling_idea_per_paragraph` |
| Cold reader | The introduction only, or the draft only | Answers each criterion's `probe` | `intro_predicts_content` and every `cold_reader` criterion |
| Judge | Spec, draft, the outline and the cold reader's answers | Aligns outline to spec; scores answers against `expected`; rules on each transition, each evidence item, the introduction and the conclusion, quoting the passage each verdict rests on | All remaining checks |

The output is one `check-report.json` (schema in this folder), stamped with
the hashes of the spec and the draft it judged.

### Step 5. Revise, and what happens when a check fails

Every failed result names a `fault`: the draft, the spec, or unclear.

| Failure | Fault | What happens |
| --- | --- | --- |
| A paragraph's summary does not match its controlling idea | draft | That paragraph is rewritten from its spec entry; its neighbours' transitions are re-checked. |
| Paragraphs are out of order, missing or extra | draft | The section is regenerated from the spec. |
| A paragraph needs two summaries | draft, or spec if the spec's idea was itself double | Split per spec; if the spec is at fault, escalate. |
| A paragraph cannot be tied to a supporting claim | draft | Cut or rewrite. If the paragraph is in the spec, the spec is at fault: escalate. |
| Evidence is left unexplained | draft | Add the explaining sentence from `evidence[].shows`. |
| A transition expresses a different relationship | draft | Rewrite the boundary sentences only. |
| A transition cannot be written because the relationship does not hold | spec | Escalate: the order or the declared relationship is wrong. |
| The cold reader cannot predict the content from the introduction | draft | Rewrite the roadmap paragraph, then the hook and bridge if it fails again. |
| A weak introduction or conclusion pattern is found | draft | Rewrite the named element; the report gives the pattern. |
| The conclusion summarizes, or does not return to the introduction | draft | Rewrite from `conclusion.synthesis` and `conclusion.callback`. |
| A custom cold-reader criterion fails | unclear | Revise the sections that the probe depends on once; if it fails again, escalate. |
| The draft is better than the spec asked for | spec | Escalate; never silently accept. |

Rules that hold across the table:

- **Revision is local.** Only the units named in the report are rewritten,
  then the whole draft is re-checked, since a local fix can break a neighbour.
- **Two rounds.** After two revisions with failures remaining, the verdict is
  `escalate` and the author decides: revise by hand, change the spec, or
  waive the criterion with a reason, recorded in the report.
- **The spec is changed first, and only by the author's decision.** A spec
  fault stops the loop. The spec is edited, re-validated, and the affected
  units are redrafted.
- **Status follows the report.** `accepted` requires a report with verdict
  `pass` whose hashes match the current spec and draft. Any later edit to
  `index.md` (a sharpen pass, a figure, a manual fix) makes the report stale;
  the post is re-checked, and if it fails the spec becomes `drifted`.
- **A failed blocker blocks publication.** How the build shows this (a chip,
  as today for `drifted`, or exclusion) is a build change and is not proposed
  in detail here.

### How it is implemented

| Step | Implemented by |
| --- | --- |
| Journal spec | `journal-spec` skill → `_journals/<j>/journal-spec.json` |
| Post spec | `spec-creator` skill → `posts/<slug>/spec.json` (replaces `spec.md`) |
| Validate | `python3 _wiring/validate_spec.py <journal> [<folder>]`: schema, then the semantic rules. The thesis rubric is a step of the two spec skills. |
| Draft | `detailed-article` skill, section "Writing from `spec.json`" |
| Check | `draft-check` skill starts the readers; `python3 _wiring/check_draft.py` does the deterministic part (`structure`), prepares the reader input (`units`), assembles and validates the report and computes the verdict (`finalize`), and reports staleness (`status`) |
| Revise | `draft-check` skill, two rounds, then escalation |
| Spec page | `build.py` renders `spec.json` through `outcome_specs.post_spec_markdown` |

`_wiring/outcome_specs.py` holds the shared code. Its schema validator covers
only the JSON Schema keywords these schemas use; it was compared with the
`jsonschema` library on 2,108 random mutations of the two examples and agreed
on every one.

How a draft is split into units, which the structural check relies on:
everything before the first `##` is the introduction; each `##` heading
starts a section; the conclusion runs from its heading to the first apparatus
heading (`Sources and Evidence`, `To Probe Further`, `Authoritative
References`, `References`, `Further Reading`) or the end. A unit is a prose
paragraph, or a list together with the paragraph that introduces it. Tables,
figures, captions and callout blockquotes are not units; the spec records
them as a paragraph's evidence.

### Not done

- No existing `spec.md` has been converted and `_wiring/spec-template.md` is
  kept for the posts that still use it.
- The per-journal writer and reviewer briefs (`_research/WRITER-BRIEF.md` and
  others) still describe the old workflow; they change when their journal is
  converted.
- `journal-spec.json` and `check-report.json` are not rendered by the build,
  and a failing or stale check does not yet show on the published page.
- `PLAN.md` chapter contracts are unchanged.

## 3. What the worked example exposed

These are observations made while reconstructing the two example specs from
the published text. They are my reading, not the output of the proposed
checks, which do not exist yet.

1. **The book has no page that closes it.** The last argued page,
   `case-composable-movement`, ends by handing off to the reference pages.
   The nearest thing to a closing is the last paragraph of Part X ("the
   newest kind of actor asking the oldest question in the book"). The
   example's `closing` therefore states what a closing should do and names
   the last case as its carrier; the published page does not do it.
2. **Chapter 4's conclusion does not return to its opening.** The chapter
   opens with a parcel that is Delivered in one system and In picking in
   another, resolves that puzzle in the bounded-contexts section, and never
   mentions it again. "What to Take Away" is three sorted lists; two of its
   eight bullets (the author's synthesis) say something the sections do not.
3. **Chapter 4 states its thesis in a callout, not in the introduction's
   prose.** The first KEY POINTS bullet carries the claim; the lead
   paragraphs define a system of record and give the roadmap.
4. **Two of Part I's four chapter hand-offs use the same move**: "X says…;
   it does not yet say…" (chapters 2 and 3). This is visible only when the
   transitions are listed side by side, which the journal spec does.
5. **The paragraph-level spec is as long as the chapter**: 6,765 words of
   JSON for 6,619 words of prose. Accepted: see section 4.
6. **Part theses for Parts II to XI are derived from the plan**, not from a
   reading of those chapters. They are plausible and unconfirmed.

### One end-to-end run (12 November 2026)

The whole check step was run once on a scratch copy of chapter 4: a reverse
outliner and four cold readers that saw only the prose, then a judge, then
`check_draft.py finalize`. Verdict `escalate` in round 1, with 11 results
passed and 9 failed.

- All three cold-reader criteria passed; 52 of 53 paragraphs matched the
  spec's controlling ideas in order; 47 of 49 transitions expressed the
  declared relationship; no weak introduction or conclusion pattern.
- Four failures were faults of the draft, among them observation 2 above
  (the conclusion does not return to the opening), which the judge found
  independently.
- Three were faults of the example spec and one was unclear: a paragraph
  specified as one idea that holds two, a roadmap that used "writer" before
  it is defined and under-promised the evidence, and "three words" for four
  terms. The example has been corrected; the draft-side findings are listed
  in its `open_questions`.

This is one run with one judge. It shows the step works end to end and that
it finds faults on both sides; it does not establish how reliable any single
ruling is.

## 4. Decisions

### Made (author, 11 November 2026)

1. **Full paragraph level.** Every paragraph is specified with its
   controlling idea, function, evidence and incoming transition. The
   template's rule that a spec should be shorter than its post no longer
   applies.
2. **One spec file, `spec.json`.** It replaces `spec.md`. Non-goals,
   Modalities, Open questions, Decision log, Sources and Changelog are fields
   of the post spec; the journal spec carries the same fields except
   Modalities. Both examples now include them, carried over from the
   published `spec.md`.
3. **Transitions on the child.** Each child carries a `transition_in` from
   its predecessor; there is no list of pairs.
4. **Post-level flow, introduction and conclusion live in the post spec
   only.** The journal spec holds each post's intent, thesis, role and
   incoming transition.

### Still open

5. **The nine extension enum values** listed in `RULES.md`.
6. **House formats.** ADR-shaped records and the book chapters have fixed
   section orders and callouts. The schema records them as ordinary sections
   and the style guide still governs them; a `house_format` field that
   pre-fills sections is possible and not included.
7. **Other modalities.** Checklists, summaries, dialogs and comics derive
   from `index.md`; the post spec lists which ones a post has but does not
   specify their content.
8. **Cost of checking.** Each draft check is roughly four model calls plus
   one per cold-reader probe, repeated per revision round.
