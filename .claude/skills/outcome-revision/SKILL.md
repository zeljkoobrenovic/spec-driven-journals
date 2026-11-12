---
name: outcome-revision
description: Revise existing, published posts of a journal through the whole outcome-spec pipeline in one unattended run — journal spec to full detail, each post's spec.md converted to spec.json, the order of ideas improved from the flow rubric, index.md revised to match, and a draft check of up to three rounds. Use when asked to run the outcome-spec revision or "the same pass" on a journal, a part or a list of posts in _journals/*/, to migrate a journal to outcome specs and revise its prose, or to "move to the next post(s)" of such a run.
---

# Outcome Revision (a whole journal, part or list of posts)

## Goal

Take posts that are already published and bring each one to the state the
outcome-spec pipeline asks for: a `spec.json` that says what the reader should
come away with, an `index.md` that matches it unit for unit, and a
`check-report.json` from readers who did not write it.

This skill orchestrates four others and adds nothing to their rules:
`journal-spec`, `spec-creator`, `detailed-article` (for prose edits) and
`draft-check`. Read `CLAUDE.md` ("Outcome specs") and
`_wiring/outcome-specs/PIPELINE.md` first.

## Inputs

- **Journal** and **scope**: the whole journal, one part, or named posts.
  If the scope is "the next post(s)", take the next posts in `config.yaml`
  order that have no `spec.json`, and stop at the end of the current part.
- **Canonical facts**: where the journal keeps them (for example
  `_research/scenario-ledger.md` and `_research/consistency-issues.md`). If
  the journal has none, say so in the report.
- **Rounds**: at most three draft-check rounds per post unless the author
  names another number.

## Contract rules

- **Work without stopping for questions**, except at the one stop below.
  Take your own recommendations, record every decision in the spec's
  `decision_log`, and put anything that is the author's to decide in
  `open_questions`.
- **One stop: theses before prose.** After the journal spec is at full detail
  for the scope and both rubrics have run, show the author the journal thesis,
  the part theses and the post theses, with the rubric verdicts, and wait. A
  thesis that fails the rubric after its chapter has been revised costs the
  whole pass again. Skip the stop only when the author says the theses are
  already approved, or asks for no stops at all.
- **Canonical facts win.** Change no figure, date or name away from the
  journal's ledger and rulings. Check every "correction" against the rulings
  before making it. Change or add no statement about a real company, product,
  price or date.
- **Keep the author's text.** Wording, voice, numbers, links, figures,
  callouts, front matter and permalink stay. Change only what the spec changes
  require. Keep the word limit the old spec set.
- **Write plainly.** A sentence a newcomer cannot parse on first reading is a
  fault; no figurative flourishes.
- **The journal spec is not edited from a post's pass.** Intent, thesis, role
  and acceptance criteria copied from it stay as they are. Criteria added for
  a post are `minor` and listed in `decision_log` for the author to keep or
  drop.
- **Specs stay at `status: draft`.** No commit and no push until the author
  asks. Do not run a further round after the last one.

## Workflow

1. **Branch.** Work on a branch, not on the default branch.
2. **Journal spec** (`journal-spec` skill). Write `journal-spec.json` if the
   journal has none. Bring every part in scope, and every post in it, to
   `detail: "full"`. Validate; run the thesis rubric on each new thesis and
   the flow rubric on each part whose order was written. Keep an example copy
   in sync if the repository holds one.
3. **Stop for the author's review of the theses** (see the contract rule).
4. **One agent per post**, started with the Agent tool as a fresh
   general-purpose agent; posts are independent, so run them side by side.
   Give each agent this brief, with the post's facts filled in:
   - the post folder, id, kind and part; the previous and next page in
     reading order, whose hand-off and `transition_in` it must agree with;
   - what earlier pages established: terms already defined, names fixed,
     vocabulary rulings (the agent may rely on these and must not contradict
     them; anything beyond them needs a gloss on first use);
   - where the canonical facts are;
   - the steps:
     a. **Spec.** Convert `spec.md` to `spec.json` from the published text,
        one paragraph per unit (`check_draft.py units`); carry over the
        record-keeping sections; rewrite inventory criteria as outcomes or
        drop them; validate; make `check_draft.py structure` pass; `git rm`
        the `spec.md` (staged only).
     b. **Rubrics.** Thesis rubric: report a failure, change nothing. Flow
        rubric: take the notes that make the piece easier to follow (forward
        references, a roadmap that announces every section, related sections
        side by side, paragraphs that make the same point merged, a
        conclusion with synthesis, so-what and callback); rewrite every
        `transition_in` a move invalidates; rerun after changing the order;
        record notes not taken in `open_questions`.
     c. **Prose.** Revise `index.md` to match the spec unit for unit, within
        the word limit.
     d. **Draft check** exactly as the `draft-check` skill says, in a scratch
        folder per round. On `REVISE`, fix the named units and run the next
        round with new readers. When a blocking failure is at fault in the
        spec, the agent may change the spec's order, paragraph ideas or
        transitions, log it, re-validate and continue; it never changes
        intent, thesis, role or the journal spec's criteria, and never waives.
     e. **Close.** After the last round, apply the cheap, plainly right fixes
        without another round and record what remains in `open_questions`.
        On `PASS`, make no further edit, so the report stays current.
   - the constraints: touch only that post's `index.md`, `spec.json`,
     `spec.md` and `check-report.json`; no commits, no build, no other files;
   - the reply wanted: spec size; rubric verdicts; changes to order and prose;
     each round's verdict with counts; what still fails and whose fault; every
     figure or name changed or added, with the ledger line that supports it;
     decisions for the author; final word count; whether the validator and
     the structure check pass; whether the report is current or stale.
5. **Check each agent's work when it returns.** Run the validator and the
   structure check yourself. Compare every figure or name the agent says it
   changed against the canonical facts, and revert what the rulings do not
   support. Note anything the agent did against its brief (added criteria,
   a raised word limit, a changed heading).
6. **Build** once all posts in the batch are back: `python3 _wiring/build.py`.
7. **Report** (below). Commit and push only when asked, and only the posts
   that are finished: an agent still running has staged files of its own.

## What to expect

A fresh pair of flow and term readers finds a new set of small points on
every pass, so most posts end in `ESCALATE` after the last round, not `PASS`,
with the fixed-question checks passing and the report stale after the closing
fixes. Say this plainly; do not present it as a pass. If a post's failures
are mostly at fault in the spec or need facts only the author has, stop that
post early and say why.

A full pass costs a few hundred thousand tokens of agent work per post, more
for long catalogue pages. For a large journal, propose a part at a time.

## Report

One table: post, words against limit, rounds run, last verdict, what still
fails. Then the decisions left for the author, grouped as canonical facts,
journal spec, and wording, each in one or two sentences. Then anything you
reverted or that an agent did against its brief, and whether the work is
committed.

## Anti-patterns

- Revising prose before the theses are settled.
- Editing the journal spec, the ledger or another post from a post's pass.
- Accepting an agent's "ledger correction" without reading the ruling.
- A fourth round, or edits after a `PASS`.
- Reporting `ESCALATE` with stale reports as "done and checked".
- Committing a post whose agent is still running.
- Setting `status: accepted`.
