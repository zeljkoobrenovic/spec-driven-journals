---
name: journal-spec
description: Create or refine a journal's journal-spec.json — the outcome spec for a whole journal (journal → parts → posts) with each unit's intent, thesis, role, flow and transitions, authored before any prose. Use when asked to plan a new journal or book, write or update the journal spec, add or specify a part or a post in it, reorder parts or posts, or check that the parts and posts add up to the journal's thesis in _journals/*/.
---

# Journal Spec (`journal-spec.json`)

## Goal

Produce or improve `_journals/<journal>/journal-spec.json`: the contract for
what the journal argues, what each part and post contributes to that argument,
the order they come in, and what links each to the next. Post specs
(`spec.json`) copy their intent, thesis and role from here, so nothing is
drafted for a post until its entry here is `full` and the file validates.

This skill writes **only** `journal-spec.json`. Post specs are written by
`spec-creator`; prose by `detailed-article`.

## Read first

- `_wiring/outcome-specs/journal-spec.schema.json` and `common.schema.json`:
  the fields and their descriptions.
- `_wiring/outcome-specs/RULES.md`: the rule behind each field.
- `_wiring/outcome-specs/examples/commerce-platform-architecture.journal-spec.json`:
  a worked example.
- The journal's `config.yaml`, and `PLAN.md` and `_research/` if they exist.

## Contract rules

- **Outcome, not coverage.** `intent.outcome` says what the reader will know,
  believe or be able to do. Every acceptance criterion is something two
  reviewers would agree had passed or failed against the finished prose. "The
  part covers X" is not a criterion.
- **A thesis is a disputable answer to a stated question.** Fill `question`,
  `claim`, `disputed_by`, `so_what` and `how_why`. If you cannot name who
  would disagree, it is a summary, not a thesis.
- **Children add up to the parent.** The journal thesis lists
  `supporting_claims`; each part's `role.supports` names the ones it argues
  for. The same holds between a part and its posts. A claim no child supports
  is a gap; an arguing child that supports nothing is an orphan. Part intros,
  front matter and reference pages are exempt.
- **The author decides the argument.** The journal thesis, the audience, the
  order of parts and what each part claims are the author's. Use
  `AskUserQuestion` for those when the source material does not settle them;
  choose defaults for the rest and record them in `decision_log`.
- **`config.yaml` stays the build's input.** Part titles and the order of
  parts and posts must equal `config.yaml`. When the two disagree, fix
  whichever is wrong; do not leave them different.

## Workflow

1. **Journal level.** Write `intent` (with `audience`), `thesis` with its
   `supporting_claims`, and `non_goals`. Stop and confirm the thesis with the
   author before going further; everything below depends on it.
2. **Parts at outline.** For every part: `id`, `title`, `detail: "outline"`,
   `thesis` (question and claim), `role`, and `transition_in` on all but the
   first. List each part's posts with `id` (the permalink), `folder`, `title`,
   `kind`, `detail: "outline"` and `question`.
3. **Flow.** Name the pattern that orders the parts and say, in `rationale`,
   what would break for the reader if they were reordered. If you cannot say,
   the order is not yet a decision.
4. **Opening and closing.** Say which post carries each and what it must do.
   A journal with no page that performs its closing has a gap: name the page
   or add one.
5. **One part at a time to `full`.** Add the part's `intent`, full `thesis`
   with `supporting_claims`, `flow`, `opening`, `closing`, and bring every
   post in it to `full`: `intent`, `thesis`, `role`, `transition_in`.
6. **Transitions.** For each child after the first, choose the relationship
   first, then write what it carries over from its predecessor and what it
   introduces. Read the transitions of one part side by side: the same
   relationship or the same move several times in a row is a sign the order
   is a list, not an argument.
7. **Validate:** `python3 _wiring/validate_spec.py <journal>`. Fix every
   error; a gap or an orphan is fixed by changing the parent's claims or the
   child's role, which is an editorial choice — report it rather than patch
   it silently.
8. **Thesis rubric.** For the journal thesis and each new or changed part and
   post thesis, start a fresh agent that is given only that thesis object and
   answers four questions with a reason each: does the claim answer the
   question; could a reasonable reader hold `disputed_by` instead; is the
   claim free of vague evaluative words ("good", "successful", "important",
   "in positive and negative ways"); are `so_what` and `how_why` more than
   restatements of the claim. Revise any thesis that fails and say which did.
9. Set `revised`, add a `changelog` entry, leave `status: draft`. The author
   sets `accepted`.

## Changing an accepted journal spec

- Changing a post's intent, thesis or role here makes its `spec.json`
  disagree with this file. Update the post spec in the same session and say
  that its prose now needs re-checking.
- Reordering parts or posts invalidates the `transition_in` of every unit
  whose predecessor changed. Rewrite those transitions; do not keep text
  written for a different pair.
- Adding a post: add the entry here first, then wire it in `config.yaml`,
  then run `spec-creator`.

## Report

Files written; what is at `outline` and what at `full`; validator result;
theses that failed the rubric and how they changed; decisions you took by
default; questions for the author.

## Anti-patterns

- Writing post specs or prose from this skill.
- Theses that name a topic ("This part is about payments").
- Acceptance criteria that list contents.
- Giving every part `additional_support` as its transition.
- Marking a post `full` with a thesis copied from its title.
- Setting `status: accepted` yourself.
