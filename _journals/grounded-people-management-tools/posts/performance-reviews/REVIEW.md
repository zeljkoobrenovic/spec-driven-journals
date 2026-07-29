# Review: Performance Reviews

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, tightly-grounded record — the checklist reproduces the workbook's
Performance Review Template (pp. 104–110) field-for-field, the article's five-part
Statement maps cleanly onto it, and all twelve referenced images (3 figures + logo +
8 comic panels) exist on disk. It is publish-ready as is. The single thing worth
addressing: the comic's Panel 7 ("the cost of the edges") introduces a beat — that
writing both edge sentences is effortful, not free — that never appears in `index.md`
or `checklist.md`, so a reader of only the comic walks away with a beat the other
modalities don't carry.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers
*(none)*

### Major
*(none)*

### Minor
- **[comics.md · Panel 7]** "Honesty at the edges is not free — it costs the rewrite
  you would rather skip" is a beat unique to the comic; it doesn't echo anywhere in
  `index.md` (Rationale or Anti-Patterns) or `checklist.md`. Not wrong, just an
  uncovered addition. *Either fold a one-clause version into the Rationale
  why-not-higher/lower paragraph, or leave as an intentional comic-only flourish.*

### Nits
- **[index.md · Rationale, "Impact has to be named work" paragraph]** "the line that
  actually settles the question" is a small hedge-phrase that could be cut without
  losing meaning — minor tightening opportunity, not a real problem.
- **[checklist.md · §1 Header]** The workbook's field is phrased as one question
  ("How long they were here during the review period... note whether the review
  period was less than a half-year and consider any time on leave"); the checklist
  compresses this to one bullet ("Time present during the review period, noting any
  leave and whether the period was less than a half-year") — faithful in substance,
  just flag for a final compare-to-source pass since it's a paraphrase, not a quote.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (line 17) states why-not-higher/lower discipline + one-sentence takeaway in one paragraph |
| Header discipline is explicit | met | index.md Statement bullet 1 + Rationale para 2; checklist.md §1 (name, level, start date, time present net of leave) precede narrative |
| The edge test survives | met | index.md Statement bullet 3 + Rationale para 3 (N/A exemptions stated correctly: "greatly exceeds" / "does not meet"); checklist.md §1 reproduces both N/A conditions verbatim |
| Impact is evidence-shaped | met | index.md Statement bullet 4 + Rationale para 4; checklist.md §2 table (context/difficulty, duration, collaborators, role/expectation, resulting impact + metrics); company-building work explicitly counted in both |
| Strengths and development areas are structured | met | index.md Rationale para 5; checklist.md §3–4 (1–2 each, approximate designation, 1–2 examples; development areas add improvement ideas) |
| Promotion logic survives intact | met | index.md Rationale para 6 + What This Means in Practice table; checklist.md §5 reproduces both no-branch (timing, what to demonstrate) and yes-branch (duration, examples, next-level development area framed as proactive) |

All six criteria are fully met. No partial or unmet items.

Non-goals respected: yes. The post stays inside "one manager's written review and its
calibration defense" — no drift into career-conversation trajectory content,
compensation mechanics, the managing-underperformance process, or the level-ladder/
calibration-process definitions themselves (both correctly deferred to
`[[careers-and-performance]]` / `[[calibrating-your-standards]]` via cross-link).

Intent & Audience: landed. The post serves both the writing manager (defensibility
before calibration) and the person receiving the review (fixed, evidence-based shape),
in first-person declarative voice throughout.

Drift: none. Spec `status: accepted` correctly reflects spec↔post agreement.

## Cross-modality alignment

- **Facts & framing:** consistent across index.md and checklist.md — same six
  header fields, same N/A exemptions, same 2–3 impact dimensions, same promotion
  branch structure. comics.md compresses the same six beats (calibration-room
  stakes, denominator, edges-not-middle, named-work impact, promotion branches,
  the takeaway sentence) faithfully, plus one extra beat (Panel 7, see Minor finding).
- **Terminology:** consistent — "why not higher / why not lower," "designation,"
  "calibration room," "one sentence" (takeaway) are used identically across all
  three files; no renaming or synonym drift.
- **Voice & tone:** consistent first-person-manager register in index.md and
  checklist.md; comics.md appropriately externalizes the same content through the
  VERA/NOA dialogue-free visual metaphor without introducing a different stance.
- **Coverage parity:** even, except comics.md Panel 7 (see above) — every other
  load-bearing beat in index.md's five-part Statement is present in both checklist.md
  and comics.md at appropriate compression.

## Layer-by-layer notes

### Spec
- Follows the template shape exactly: Intent, Audience, Success criteria, Non-goals,
  Modalities, Open questions, Decision log, Sources, Changelog all present and used
  correctly.
- Success criteria are genuinely checkable — each names a specific structural
  element (header fields, N/A exemptions, table columns, branch logic) rather than
  restating Intent as a checkbox.
- Concise: 111 lines against a ~2000-word article — proportionate, no bloat.
- Decision log correctly captures the load-bearing editorial choice (why-not-higher/
  lower + takeaway as the organizing idea, not the header fields).

### index.md
- House record shape followed precisely: Statement → How to Read This → Rationale →
  What This Means in Practice → Anti-Patterns → Related Records → Scope and
  Revisiting → Authoritative References, all in Title Case.
- Three figures (five-part loop, assertion-vs-argument ladders, promotion branch
  flow) are well-placed, each captioned with a numbered caption that adds rather
  than repeats.
- Rationale paragraphs each open with a bolded topic sentence that restates and
  expands its Statement bullet — this is the established house pattern (confirmed
  against `career-conversations/index.md`), not redundancy.
- All five cross-links (`career-conversations`, `compensation-conversations`,
  `managing-underperformance`, `careers-and-performance`,
  `calibrating-your-standards`) resolve to existing posts.
- Grammar and mechanics clean; no typos or malformed markdown found.

### checklist.md
- Reproduces the workbook's Performance Review Template (verified against PDF pp.
  104–110) field-for-field: header block, impact table + checkboxes, strengths,
  development areas, promotion proposal (both branches), and a closing
  pre-conversation gate section not in the source but a reasonable operational
  addition.
- Sentence-case section headings ("## 1. Header," "## 2. Impact," …) match journal
  convention (not a finding, per the review brief).
- Section 6 ("Before the review conversation") is an original addition beyond the
  workbook — a good synthesis gate, consistent with the spec's emphasis on the
  document being calibration-ready.

### comics.md
- 8 panels, each with a one-sentence caption in the house register; alt text and
  captions match their described imagery throughout.
- All 8 panel images plus the 3 article figures and the logo (12 files total)
  exist under `assets/images/performance-reviews/` — no broken image references.
- Visual metaphor (VERA the seasoned executive, NOA the first-time manager) is
  consistent panel to panel and matches the cast declared in the leading HTML
  comment block.
- Panel 7 introduces a beat absent from the other modalities (see Minor finding
  above) — otherwise coverage of the five-part Statement is complete and correctly
  compressed.

## Fixes applied (2026-07-29)

- **[Minor · comics.md Panel 7]** Skipped — fixing requires either regenerating the
  comic panel image (out of scope for a text-only fix) or removing/rewording the
  caption in a way that would understate a beat the image likely still shows;
  left as an intentional comic-only flourish per the reviewer's own alternative.
- **[Nit · index.md Rationale, "Impact has to be named work"]** Fixed — cut "the
  line that actually settles the question," tightening the sentence without
  losing meaning.
- **[Nit · checklist.md §1 Header]** Skipped — compared against the workbook
  source; the checklist's compression ("Time present during the review period,
  noting any leave and whether the period was less than a half-year") is a
  faithful paraphrase of the source question, not a factual drift. No change
  needed.
