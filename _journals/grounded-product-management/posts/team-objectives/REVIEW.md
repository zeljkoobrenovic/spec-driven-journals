# Review: Team Objectives

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is tight and fully satisfied: all seven
success criteria are met, all four cross-links resolve, all eight comic panel
images and all three article figures exist, and the article follows the house
record shape cleanly. The single most important thing to address is a
cross-modality framing tension: the checklist's "Define Strong Key Results"
section addresses the *leader* as the one who sets key results ("Set 2 to 4 key
results per objective", "Let the team help determine the actual KPI targets…
when appropriate"), while the article's load-bearing claim is that key results
are proposed *by the team* ("the proposal direction is up, not down"). The spec
requires the checklist survive intact from the PDF, so the resolution is the
author's call — but the tension should be acknowledged, not left silent.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

- None.

### Major

- **[checklist.md · "Define Strong Key Results" (lines 24–29) ↔ index.md · Statement / Rationale]**
  The checklist frames the reader (the leader) as the one defining key results,
  with team input as optional assistance ("Let the team help determine the
  actual KPI targets and timing when appropriate"), while the article's central
  claim — in the highlight, Statement bullet 2, and Rationale — is that key
  results flow *up*, proposed by the team. Not a hard contradiction (the article
  concedes "I still negotiate"), and the spec's "checklist survives intact"
  criterion protects the PDF wording — but a first-time reader switching tabs
  gets two different directions of proposal. *Suggested direction: one bridging
  clause in the checklist's italic intro line noting the checklist keeps the
  source's leader-addressed voice, or soften the "Set 2 to 4" bullet to
  "Expect the team to propose…".*

### Minor

- **[index.md · Figure 3 (after "Objectives die of neglect" paragraph)]** The
  high-integrity-commitment figure lands one paragraph *after* the commitment
  paragraph it illustrates, splitting the active-management paragraph from the
  section that follows it. *Suggested direction: move Figure 3 up to sit
  directly after the "A commitment that was never investigated…" paragraph.*
- **[comics.md · overall arc]** The accountability-proportional-to-ambition /
  constructive-postmortem beat — Statement part 5 and an explicit element of the
  spec's Intent — has no echo in the comic; the arc ends at active steering
  (Panel 8). Eight-panel economy is a fair defense, but it is the only one of
  the article's five Statement parts with no panel presence. *Suggested
  direction: fold a proportional-accountability nod into Panel 8's caption, or
  accept the omission deliberately.*
- **[checklist.md · Quick Quality Check, line 115]** The intro line "- Before
  finalizing team objectives, ask:" is a stray plain bullet mixed into the task
  list; sibling checklists (e.g. product-vision-and-principles) introduce their
  final check with no such bullet. *Suggested direction: drop the leading
  hyphen so it renders as a plain paragraph.*

### Nits

- **[index.md · "What This Means in Practice" table, row 2]** "results don't
  match" is the record's only contraction; the same clause appears as "do not
  match the business need" in the Rationale (and checklist line 46). Use
  "do not" for consistency.
- **[index.md · Statement bullet 5 / Rationale para 3]** "improve(s) the
  system, not just the team" appears verbatim in both. The
  Statement-summarizes-Rationale pattern is house-normal, but a verbatim repeat
  of a signature phrase within one article is worth a glance.
- **[spec.md · Changelog]** The latest entry still describes the comic as
  "pending panel blocks" and the article as having "inline illustration
  placeholders staged," but panels and figures are now generated. A one-line
  changelog entry recording generation would keep the history accurate.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("problems to solve, not features to ship"; "proposed by the team that has to deliver them") |
| Two-way flow explicit | met | index.md · Statement bullet 2 + Figure 1; comics.md Panels 4–5 |
| The numbers survive | met | index.md · Statement (2–4 KRs, primary + guardrails), Rationale (weekly check-ins), Scope (quarterly refresh); echoed in checklist.md |
| Ambition is a dial, not a mood | met | index.md · Statement bullet 3, Rationale para 3, Figure 2; comics.md Panel 6 |
| High-integrity commitments the exception | met | index.md · Statement bullet 4, Rationale para 4; checklist.md "Handle Commitments Carefully"; comics.md Panel 7 |
| Checklist survives intact | met | checklist.md — 13 sections + Quick Quality Check, all present |
| Credit is explicit | met | index.md · Authoritative References (EMPOWERED + svpg.com) |

Non-goals respected: yes — no tooling/template content; boundaries with
[[outcomes]] and [[empowered-product-strategy]] drawn explicitly in How to Read
This and Related Records; no claim that OKRs are mandatory ("OKRs without
empowerment are theater").

Drift: none. Spec `status: accepted` is correct; spec and post agree.

## Cross-modality alignment

- **Facts & framing:** Consistent, with one tension — the direction of
  key-result proposal between checklist.md and index.md (the major finding
  above). All numbers (2–4 KRs, weekly cadence, quarterly refresh) match across
  modalities.
- **Terminology:** Consistent — "roof shot / moon shot", "high-integrity
  commitment", "keep-the-lights-on", "portfolio risk management" travel intact
  through article, checklist, and comic.
- **Voice & tone:** Consistent for the forms. The checklist keeps the source
  PDF's second-person imperative rather than the article's first person, which
  is the journal's established checklist register; the comic's narrator captions
  match the house comic voice.
- **Coverage parity:** Article and checklist are in full parity. The comic
  covers four of the five Statement parts (problems-not-features, two-way flow,
  ambition dial, commitments) plus active steering; the
  proportional-accountability/postmortem beat is the one omission (minor
  finding above).
- **Stale propagation:** None observed — figures, panels, and text all reflect
  the same generation pass.

## Layer-by-layer notes

### Spec

- Follows the template fully; every Success criterion is concretely checkable
  (quotable phrases, named numbers, a countable "thirteen sections"). No bloat —
  the spec is shorter than the article, as it should be.
- Decision log does real work: the boundary with [[outcomes]] is drawn in the
  spec before the article draws it, which is the pattern working as intended.
- Only blemish is the stale "pending panel blocks" wording in the newest
  changelog entry (nit).

### index.md

- House record shape is exact: status highlight, Statement → How to Read This →
  Rationale → What This Means in Practice → Anti-Patterns → Related Records →
  Scope and Revisiting → Authoritative References. Headings are in Title Case;
  all three figures are captioned and their images exist.
- All four `[[…]]` cross-links resolve (outcomes, empowered-product-strategy in
  this journal; measuring-engineering-organizations, planning cross-journal).
- The Rationale's five bolded topic sentences are strong and each earns its
  paragraph; "a guess with a deadline" and "a roadmap with extra ceremony" are
  the kind of quotable compression the journal aims for.
- Two placement/flow points: Figure 3 lags its paragraph, and the
  keep-the-lights-on beat rides as a single appended sentence on the
  "die of neglect" paragraph — present and countable, but the seam shows.

### checklist.md

- Faithful, well-grouped reproduction: 13 sections plus the Quick Quality
  Check, imperative action bullets throughout, key numbers bolded. Judged as an
  operational working checklist, it runs well — a leader could execute a
  quarter from it.
- The one substantive issue is the key-result-direction framing in "Define
  Strong Key Results" (major finding).
- The Quick Quality Check intro line carries a stray bullet (minor finding).

### comics.md

- All eight referenced panel images exist under
  `assets/images/team-objectives/`; captions match their alt text; the
  mountain-and-route metaphor introduced in Panel 3 is carried through to
  Panel 8, and the wax-seal commitment image in Panel 7 rhymes with the
  article's Figure 3 ("sealed, dated, tracked separately").
- Clean arc: hook → problem → principle → context down → key results up →
  ambition → the exception → closer. Caption lengths fit the form.
- The only parity gap is the missing accountability/postmortem beat (minor
  finding).

## Fixes applied (2026-07-29)

- **Major — checklist key-result direction:** fixed. Bullets verified verbatim
  against `sources/empowered/Checklist_ PM _ Team Objectives.pdf` and left
  intact; added an italic bridging intro line under "Define Strong Key Results"
  noting the section keeps the source's leader-addressed voice while the
  proposal direction is up (per the Article tab).
- **Minor — Figure 3 placement:** fixed. Figure 3 moved up to sit directly
  after the high-integrity-commitment paragraph, before "Objectives die of
  neglect".
- **Minor — comic accountability beat:** fixed. Panel 8 caption extended with
  the postmortem/improve-the-system nod (caption only; alt text still
  describes the unchanged image, no regeneration).
- **Minor — Quick Quality Check stray bullet:** fixed. Leading hyphen dropped
  from the "Before finalizing team objectives, ask:" intro line so it renders
  as a plain paragraph, matching sibling checklists.
- **Nit — "results don't match" contraction:** fixed. Changed to "do not
  match" in the What This Means in Practice table, matching Rationale and
  checklist wording.
- **Nit — verbatim "improve the system, not just the team" repeat:** skipped.
  House-normal Statement-summarizes-Rationale pattern; the signature phrase is
  kept deliberately in both places.
- **Nit — stale spec changelog:** fixed. New 2026-07-29 changelog entry
  records panel/figure generation and the review-fix pass; `revised:` bumped
  to 2026-07-29.
