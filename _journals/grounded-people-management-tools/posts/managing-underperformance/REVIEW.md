# Review: Managing Underperformance

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, tightly grounded record — the arc (document → PIP → manage out)
is explicit, the checklist reproduces the workbook's four letters, PIP
mechanics, and eight-step managing-out sequence with high fidelity (verified
against `sources/Scaling-People-Workbooks_PDF_23_03_05.pdf`, pp. 113–124), and
the comic's eight panels track the same arc beat for beat. It is publish-ready
as is. The one thing worth a second look before calling it done: the "a PIP
should never be the first feedback" thesis is restated near-verbatim four
times across the excerpt, highlight, Statement, and Rationale — deliberate
emphasis in this house style, but the Rationale repetition in particular adds
little the Statement bullet hasn't already said.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 1

### Blockers
*(none)*

### Major
*(none)*

### Minor
- **[index.md · Statement bullet 3 / Rationale para 2]** The "a PIP is never
  the first feedback" claim is stated almost identically in the Statement
  bullet ("A PIP is an escalation, never an opener") and the opening line of
  the second Rationale paragraph ("The follow-up letters exist so a PIP is
  never the first feedback anyone gets"), on top of the highlight blockquote
  and the excerpt already carrying it. *Consider having Rationale build on
  the claim (why the letters achieve it) rather than restate it.*
- **[checklist.md · item 9 vs. workbook pp. 120–121]** The checklist folds the
  workbook's three distinct labeled fields — "Goal and time frame," "Deliverable,"
  and the separate "Milestones" section (with its own project/deadline list) —
  into two bullets ("goal and time frame" + "deliverable") plus a third
  ("concrete milestones... with hard deadlines"). Faithful in substance but
  collapses what the source keeps as three separately headed fields. *Not
  wrong, just worth knowing if fidelity-to-structure ever matters more than
  fidelity-to-content.*

### Nits
- **[index.md · line 26 vs. checklist.md item 8 title]** "Three or fewer" (index,
  Statement bullet) vs. "up to three" (checklist heading and index's own table
  row, line 61) — same meaning, two phrasings. Minor terminology wobble, not a
  factual conflict.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (line 17), excerpt |
| The arc is explicit (feedback → letters → PIP → managing out, in order) | met | index.md Statement (lines 21–27), Rationale |
| The four letters keep their distinct jobs | met | checklist.md items 1–4; index.md Rationale para 2 |
| The PIP mechanics survive (4–6 weeks, 3–5 role bullets, ≤3 improvement areas, goals/milestones, HR partner, weekly checks, caveats, signatures) | met | checklist.md items 6–12; index.md Rationale paras 3–4 |
| The Managing Out Checklist keeps all eight steps in sequence | met | checklist.md item 13; verified verbatim order against source p.124 |
| Local law caveat is explicit | met | index.md Rationale para 4 ("may need to be adapted... jurisdictions"), Statement bullet 5, checklist.md item 5 and item 13 step 4 |
| The checklist survives intact (all three tools in Checklist tab) | met | checklist.md, all 13 sections |
| Credit is explicit (Scaling People workbooks named) | met | index.md Authoritative References; spec.md Sources |

Non-goals respected: yes — no compensation mechanics, no jurisdiction-specific
legal guidance beyond the caveat, no post-announcement offboarding/severance
detail; [[performance-reviews]] and [[compensation-conversations]] are
referenced, not re-explained.

Drift: none. Spec `status: accepted` against post `draft:gray` is the
journal's normal convention (spec agreement vs. post publication state), not
drift.

## Cross-modality alignment

- **Facts & framing:** consistent. PIP duration (4–6 weeks), improvement-area
  cap (three), the four letters, and the eight managing-out steps match
  identically across index.md, checklist.md, and comics.md, and all match the
  workbook source.
- **Terminology:** consistent, with the one nit above ("three or fewer" vs.
  "up to three" — same meaning, no factual drift).
- **Voice & tone:** consistent first-person declarative voice across index.md
  and checklist.md; comics.md carries the same beats through the VERA/NOA cast
  without contradicting the article's framing.
- **Coverage parity:** even. Every load-bearing beat in index.md (document
  early, four-letter loop, PIP mechanics and caveats, managing-out sequence)
  has a matching checklist section and a matching comic panel (panels 1–3
  cover the problem/anti-pattern, 4–6 the document-then-PIP arc, 7 the
  caveats, 8 the managing-out-together close).

## Layer-by-layer notes

### Spec
- Follows the template shape well; Success criteria are genuinely checkable
  (each cites a specific structural element from the workbook), not vague
  intent restated as bullets.
- Decision log is useful and specific (names the framing choice and why the
  PIP-as-starting-point alternative was rejected).
- Open questions is empty, which is fine for a record this settled — no
  dangling threads.

### index.md
- Follows house record shape correctly: Status/Principle highlight, Statement
  → How to Read This → Rationale → What This Means in Practice → Anti-Patterns
  → Related Records → Scope and Revisiting → Authoritative References.
- Headings are Title Case throughout, consistent with house style.
- Three figures are well-placed (funnel, loop, sequence map) and each caption
  adds an interpretive line rather than just describing the image.
- The "What This Means in Practice" table is a clean contrast table, consistent
  with the journal's convention seen in `performance-reviews`.
- One repeated thesis (see Minor finding above) — otherwise no unsupported
  claims; every mechanical detail (4–6 weeks, ≤3 areas, at-will caveat) is
  traceable to the workbook.

### checklist.md
- All 13 sections map cleanly onto the three source tools (four letters, PIP
  in six sub-sections, managing-out checklist), verified against pp. 113–124
  of the source PDF — wording is close-to-verbatim where the workbook uses
  fixed language (e.g. the at-will/no-guarantee/sustained-performance
  caveats) and appropriately imperative elsewhere.
- Sentence-case headings are the journal's stated convention, not a finding.
- Item 5 ("Before starting a PIP") and item 13 step 4 both carry a
  local-law caveat — this is not duplication but two distinct real
  moments in the source (the PIP template's own jurisdiction note vs. the
  Managing Out Checklist's own regulations step); both are preserved
  correctly and separately.

### comics.md
- Eight panels, one caption sentence each, consistent length and tone; no
  caption exceeds the form.
- All eight referenced image files exist on disk
  (`comic-01-the-surprise-pip.jpeg` through `comic-08-managing-out-together.jpeg`).
- Cast (VERA/NOA) is declared once in the style comment and used consistently;
  visual metaphor (documents, corkboard, calendar, checklist) stays consistent
  panel to panel.
- Panel 1 opens on the "surprise PIP" failure mode before panel 4 states the
  "document first" principle — an effective inversion (problem before
  principle) that mirrors the article's Anti-Patterns-reinforces-Statement
  structure rather than contradicting it.

## Fixes applied (2026-07-29)

- **Nit — "three or fewer" vs. "up to three" (index.md lines 26, 61):** aligned
  both occurrences in index.md to "up to three," matching the checklist
  heading (`checklist.md` item 8) and the workbook's own phrasing.
- **Minor — checklist item 9 collapses three labeled workbook fields
  (checklist.md):** restored "Goal and time frame," "Deliverable," and
  "Milestones" as three distinct labeled bullets (bolded field names) instead
  of two bullets plus an unlabeled third, matching the workbook's own
  structure at pp. 120–121.
- **Minor — near-verbatim "never the first feedback" repetition (index.md
  Rationale para 2 opener):** reworded the opening line to argue *why* the
  four letters achieve that outcome (they make the gap undeniable and the
  support real, in writing, before anything formal starts) rather than
  restate that they exist for that purpose. Left the highlight blockquote,
  excerpt, and Statement bullet 3 untouched — the blockquote → Statement →
  Rationale escalation is the intended house pattern, not a finding to flatten.
- **Skipped — comics "credit" reading:** not applicable per policy; comics
  never carry source credits in this journal.
- **Skipped — sentence-case checklist headings:** journal convention, no
  internal inconsistency found within checklist.md, so no change.
- **Skipped — spec `status: accepted` vs. post `draft:gray`:** journal
  convention (spec agreement vs. post publication state), not drift.
- **Skipped — comic panel content/beats:** out of scope per policy (would
  require regenerating panel images); none of the findings called for this
  regardless.
