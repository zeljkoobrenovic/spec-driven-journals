# Review: Writing OKRs

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Solid, publish-ready with one real gap to close: the spec commits to landing
"aspirational vs. committed" as an objective-writing best practice, and it
never appears in `index.md` — only in `checklist.md` (§7). Everything else —
numbers, grammar, checklist items, panel captions — checks out cleanly against
the source workbook pages (24–29) and across all three files. No blockers.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Major
- **[index.md · Statement / Rationale]** The spec's Success Criterion
  "Objectives vs. key results best practices both land" explicitly lists
  "aspirational vs. committed for objectives" as required content. This
  concept — an objective is individually labeled aspirational (70%) or
  committed (100%) at write time — never appears in `index.md`, only in
  `checklist.md` §7. Because the article's own ambition discussion uses a
  *different* "70 percent" (the aggregate 70–80% scoring band), a
  reader of the article alone is likely to conflate the two distinct
  70%-labeled concepts from the source. *Add one clause to the "Objectives
  are outcomes" or "Ambition is calibrated" bullet naming the aspirational/
  committed label explicitly.*

### Minor
- **[comics.md · Panel 7]** The mid-quarter green/yellow/red scoring ritual —
  a named spec Success Criterion ("Iteration discipline survives") — has no
  dedicated panel. Panel 7 jumps from the must-hit dial (Panel 6) straight to
  the "silent edit" cost, only implying scoring happened. *Consider folding a
  green/yellow/red beat into Panel 7's caption or art if a 9th panel isn't
  wanted.*
- **[index.md · Related Records, line 79]** "this record supplies the writing
  grammar and scoring discipline that model runs on" is a slightly tangled
  possessive-less construction ("that model" reads ambiguously as "that
  [mental] model" vs. a typo for "that model [it] runs on"). *Reword for
  clarity, e.g. "...that that model runs on" or "...the model in that record
  runs on."*

### Nits
- **[checklist.md · §7]** "Objective can be long-term, spanning several
  quarters or years" and "Objective charts intent and direction, not a task
  list" are granular workbook bullets with no echo anywhere in `index.md` or
  `comics.md` — fine for a checklist (exhaustive by design) but worth knowing
  these two best-practice lines are checklist-only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The metrics table survives | met | checklist.md §1 (table), §2–4 (full scrutiny checklist) |
| Ambition calibration is explicit | met | index.md Statement/Rationale/table; checklist.md §6; comics.md Panel 6 |
| Objectives vs. key results best practices both land | partial | checklist.md §7–8 fully; index.md covers outcomes/user-problem/nesting but **omits aspirational-vs-committed** |
| Common pitfalls are named | met | index.md Anti-Patterns; checklist.md §9 |
| Iteration discipline survives | met | index.md Rationale + table; checklist.md §10–11; comics.md Panel 7 (compressed) |
| Credit is explicit | met | index.md Authoritative References; checklist.md intro line |

Non-goals respected: yes — no drift into `team-objectives`, `quarterly-business-reviews`, `team-charter`, or performance-management territory. All four non-goal cross-links resolve to real posts.

Drift: none rising to `status: drifted` — the one gap (aspirational/committed) is a coverage omission, not a factual disagreement with the spec. Worth a follow-up edit to `index.md` rather than a spec-status change.

## Cross-modality alignment

- **Facts & framing:** consistent. All four files agree on 3–5 objectives, 1–5 key results, 70–80 percent typical, 20–30 percent must-hit at 95 percent or better, the counterweight-metric example (users vs. revenue, "grow users by giving the product away for free"), and the relative-target example (5,000 → 6,000, 20 percent). All match the source PDF (pp. 24–29) verbatim.
- **Terminology:** consistent — "scrutiny checklist," "must-hit," "counterweight," "write–collaborate–publish," "green/yellow/red" / "on-track/off-track/at-risk" are used identically across index, checklist, and comics.
- **Voice & tone:** consistent first-person declarative in index.md and checklist.md; comics.md appropriately shifts to the VERA/NOA dialogue register without changing any stated fact.
- **Coverage parity:** mostly even. The one gap is aspirational-vs-committed labeling (checklist-only, flagged above as major since the spec requires it in the article). The green/yellow/red scoring beat is present in index.md and checklist.md but only implied, not shown, in comics.md (flagged as minor).

## Layer-by-layer notes

### Spec
- Clean, on-template, all eight sections present plus Changelog. Success criteria are checkable and specific (this is what let the "partial" call above be made precisely).
- No bloat — the spec is shorter than the post, as intended. Open Questions correctly closed out ("None").
- Decision log gives real rationale for scoping the three workbook tools together rather than splitting them — good internal consistency between Intent and structure.
- `status: accepted` alongside post `status: draft:gray` is the journal's documented convention, not a finding (per task framing).

### index.md
- Follows house MADR order exactly: Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References. Headings correctly Title Case.
- Three figures, all captioned, all image files present and load-bearing (grammar shape, counterweight balance, write-collaborate-publish pipeline).
- The "give the product away for free" example recurs in Statement, Rationale, and Anti-Patterns — this is intentional MADR-style reinforcement (preview → explain → name-the-failure), not redundant filler.
- The aspirational/committed omission (major finding above) is the one real content gap against the spec.
- All six `[[cross-links]]` resolve to real posts in the correct journals.

### checklist.md
- Reproduces the workbook's two checklists, the ambition-calibration guidance, and the iterating/scoring guidance faithfully and completely — verified line-by-line against PDF pp. 24–29.
- Sentence-case headings throughout, per journal convention (not a finding).
- Structure mirrors the workbook's own section order (metrics table → scrutinize objectives → SMART → scrutinize metrics → write/collaborate/publish → calibrate ambition → best practices → pitfalls → scoring → change handling), which reads logically as a run-order for an actual OKR-writing session.

### comics.md
- Eight panels, each with alt text + caption, all eight panel image files present.
- Visual metaphor (VERA the skeptical executive, NOA the earnest first-time manager with a clipboard) stays consistent panel to panel; captions match their alt text and images.
- Covers the hook (nine objectives), two anti-patterns (activity-as-outcome, roadmap-in-disguise), the fixed grammar, the scrutiny checklist, the ambition dials, the change-discipline cost, and publishing — a well-chosen eight-beat compression of the record's load-bearing ideas.
- Minor coverage gap: green/yellow/red scoring itself is not visually depicted (see Minor finding above).

## Fixes applied (2026-07-29)

- **[Major, index.md Statement]** Fixed: added the aspirational (~70 percent) vs. committed (100 percent) per-objective label to the "Objectives are outcomes" bullet, with an explicit clause distinguishing it from the aggregate 70–80 percent scoring band discussed in the next bullet, so the two "70"s can no longer be conflated.
- **[Minor, index.md Related Records]** Fixed: reworded "this record supplies the writing grammar and scoring discipline that model runs on" to "...that model of collaboration runs on," removing the ambiguous bare "that model" construction.
- **[Minor, comics.md Panel 7]** Skipped: folding a green/yellow/red scoring beat into Panel 7's caption would contradict what the existing image depicts (the silent-edit/documented-change moment, not a scoring ritual) — per policy, comic text may only be edited when it can't contradict the drawn art, and this one can't be worded around without a new panel or regenerated art, both out of scope here.
- **[Nit, checklist.md §7]** Skipped: the finding is an observation ("worth knowing"), not a requested fix — these two best-practice lines are intentionally checklist-only per the review's own framing.
