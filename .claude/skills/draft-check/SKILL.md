---
name: draft-check
description: Check a post's draft (index.md) against its outcome spec (spec.json) with readers who did not write it, write check-report.json, and revise the draft where it fails. Use after writing or changing an article that has a spec.json, or when asked to check, verify or validate a draft against its spec, run the outcome checks, do a reverse outline, see whether a post still matches its spec, or clear a stale or failing check report in _journals/*/posts/*/.
---

# Draft Check (`check-report.json`)

## Goal

Decide, with evidence, whether `index.md` achieves what `spec.json` says it
must, and write the result to `check-report.json` next to the draft. Where the
draft fails, revise it locally and check again, at most twice. Where the spec
is at fault, stop and hand the decision to the author.

The checks and their sources are in `_wiring/outcome-specs/RULES.md`
("Check catalogue"); what happens on each kind of failure is in
`_wiring/outcome-specs/PIPELINE.md` (step 5).

## Contract rules

- **Never edit `spec.json` from this skill.** A draft that is better than its
  spec, or a spec that cannot be satisfied, is reported with
  `"fault": "spec"`; the author decides.
- **Readers are separate agents and see only what their job needs.** The
  session that wrote the draft does not judge it. Start each reader with the
  Agent tool as a fresh agent, not a fork, and give it exactly the inputs
  listed below. Do not paste the spec into the reverse outliner's or the cold
  reader's prompt, and do not tell any reader what result you expect.
- **Every failure quotes the draft.** A failed result with no quoted passage
  and no stated finding is not accepted by the script.
- **Report what happened.** A check that could not be run is reported as not
  run; it is never recorded as passed.

## Workflow

Let `P` be the post folder.

1. **Validate the spec:** `python3 _wiring/validate_spec.py <journal> <folder>`.
   If it fails, stop: the spec must be fixed first.
2. **Structure:** `python3 _wiring/check_draft.py structure P > <scratch>/structure.json`.
   It gives the deterministic results and the alignment of each spec
   paragraph to a draft unit. If sections or unit counts do not match, fix the
   draft now (step 7) and rerun before spending readers on it.
3. **Units:** `python3 _wiring/check_draft.py units P > <scratch>/units.json`:
   the draft as numbered units, with nothing from the spec.
4. **Reverse outliner** (one agent; input: `units.json` only). Ask it to write,
   for every unit, what the unit is about in one short phrase of its own
   words, and to mark any unit that needs two phrases because it holds two
   ideas. It returns `[{draft_locator, summary, two_ideas}]`.
5. **Cold readers** (one agent per probe; input: draft text only).
   - For `intro_predicts_content`: give it the introduction units and callouts
     only and ask what the post will discuss, in what order, with what kind of
     evidence, and in what tone.
   - For each acceptance criterion with `method: cold_reader`: give it the
     whole draft and the criterion's `probe`, nothing else.
   - For `flow_is_followable`: give it the whole draft and ask how easy it
     was to follow, not whether it is good: what principle orders the
     sections; for each section, why it comes where it does; every place it
     lost the thread, had to re-read or met something out of place, with the
     sentence quoted; and whether any reordering would have been easier. Tell
     it not to invent problems and not to leave out real ones.
   Each returns its answer in plain prose.
6. **Judge** (one agent; input: `spec.json`, `structure.json`, the reverse
   outline, the cold readers' answers). It returns one result per check and
   criterion, in the `--results` format of `check_draft.py`:
   - `reverse_outline_matches_spec`: each summary against the controlling idea
     of the spec paragraph it is aligned to; set `matched_spec_paragraph`.
   - `one_controlling_idea_per_paragraph`: every unit the outliner marked.
   - `paragraph_traces_to_thesis`: each unit against the supporting claims.
   - `evidence_is_explained`: each `evidence` item, each table, figure and
     quotation in the draft.
   - `transition_expresses_declared_relationship`: every `transition_in`, read
     at the boundary between the two aligned units.
   - `flow_is_followable`: the flow reader's account against the spec's
     `flow` (post level and per section). Pass when the organising principle
     the reader describes agrees with the declared pattern, no section's
     position is "unclear" to it, and it reports no material lost-thread
     point. Each material point is one failed result with the reader's quote;
     the fault is the draft when the spec's order is fine and the prose
     obscures it, the spec when the reader's difficulty comes from the order
     itself.
   - `known_before_new`: terms against `audience.already_knows` and
     `does_not_know`.
   - `no_weak_introduction_pattern`, `no_weak_conclusion_pattern`: name the
     pattern in `weak_pattern` when one is found.
   - `conclusion_synthesizes_and_answers_so_what`,
     `conclusion_calls_back_to_introduction`.
   - `intro_predicts_content` and each cold-reader criterion: the answer
     against the roadmap or the criterion's `expected`.
   The results file also carries the outline as `reverse_outline`, one entry
   per unit with exactly `draft_locator`, `summary` and
   `matched_spec_paragraph` (null when the unit matches nothing in the spec).
   Each result has `verdict` (`pass` or `fail`), and for a fail: `spec_locus`,
   `draft_locus`, `quote`, `finding` and `fault` (`draft`, `spec` or
   `unclear`). One failing boundary or paragraph is one result; do not merge
   several into one.
7. **Finalize:**
   `python3 _wiring/check_draft.py finalize P --results <scratch>/results.json --round <n>`.
   It writes `check-report.json` and prints `PASS`, `REVISE` or `ESCALATE`.
8. **On `REVISE`:** rewrite only the units named in the failed results, each
   from its own spec entry (controlling idea, function, evidence, transition).
   Do not add, drop, merge or reorder units. Then return to step 2 with
   `--round` increased by one (round 1 is the first check, so two revisions
   end at round 3) and fresh readers; a reader that saw the
   previous round is not reused.
9. **On `ESCALATE`:** stop. The script escalates when a failure is at fault
   in the spec, or when failures remain after two revisions (the check of
   round 3). Report each
   remaining failure with its quote, say whether the draft or the spec looks
   wrong and why, and give the author the three options: revise by hand,
   change the spec (then re-validate and redraft the affected units), or
   waive the criterion. A waiver is recorded as a result with
   `"verdict": "waived"` and `waived_by` giving who and why; only the author
   can grant one.
10. **On `PASS`:** run `python3 _wiring/check_draft.py status P` and report its
    output. Do not change `status` in `spec.json`; say that the spec can be
    set to `accepted`.

## After any later edit

Any change to `index.md` or `spec.json` makes the report stale
(`check_draft.py status` says so). Rerun this skill. If the edited draft no
longer passes and the author wants to keep the edit, the spec is `drifted`
until it is changed to match.

## Report

Verdict and round; counts of passed, failed and waived; each failure with its
locus and quote; what was revised between rounds; anything not run.

## Anti-patterns

- Judging the draft yourself in the session that wrote it.
- Giving the reverse outliner or a cold reader the spec, the expected answer,
  or the criterion's wording beyond its probe.
- Recording a pass for a check no reader ran.
- Regenerating a whole section to fix one boundary.
- Editing the spec so that a failing check passes.
- A third revision round.
