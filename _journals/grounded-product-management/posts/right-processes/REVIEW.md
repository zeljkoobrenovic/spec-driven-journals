# Review: The Right Processes

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article is tightly argued in the house shape, the checklist reproduces all seventeen source sections with every number intact, the comic's eight panels track the article's beats faithfully, and every image, icon, cross-link, and source file resolves. The single most important thing to address is a coverage-parity gap: two whole checklist sections — "Craft the Product Strategy" and "Communicate the Outcome, Vision, and Strategy" — have no echo in the article (or in the spec's Intent), so an article-only reader misses the strategy-session machinery (notably "agree on the decision-making process before forcing agreement on the decision"). Everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 3

### Blockers

- None.

### Major

- **[checklist.md · "Craft the Product Strategy" + "Communicate the Outcome, Vision, and Strategy" vs index.md · Statement/Rationale]** The checklist carries two full sections (cross-functional strategy session, decision-process-before-decision, CEO/empowered-leader as final decision-maker; communicating the outcome/vision/strategy as a story) that the article never mentions and the spec's Intent does not list. The spec is internally split: the Success criterion "checklist survives intact" pulls all 17 sections in, while Intent enumerates only ~8 themes. *Either add one clause to the article (Statement or How to Read This) acknowledging the strategy-session and vision-communication steps — e.g. pointing at sibling records like [[product-strategy]] / [[outcomes]] — or note in the spec that the first four checklist sections overlap territory owned by sibling records and are reproduced here only for checklist completeness.*

### Minor

- **[index.md · Statement bullet 3 + Rationale ¶2]** "at least four hours a week, multiple methods, even when there is no immediate project" and "four hours a week, multiple methods, conversations even when no project demands them" are near-verbatim twins. The record shape licenses layered restatement, but not verbatim phrase reuse. *Vary one of the two.*
- **[index.md · highlight, Statement bullet 3, Rationale ¶2, table row 2]** "Research before deciding what to build" appears four times in essentially the same words. Twice is the shape; four is repetition. *Compress or rephrase one occurrence.*
- **[spec.md · Intent]** The Intent is a single ~130-word sentence carrying nine parallel clauses — hard to parse as a contract. *Break into two or three sentences.*
- **[index.md · What This Means in Practice, table row 1, right column]** "Process is bad — no process is just prioritization by loudness" does two jobs in one cell (the negated claim plus its reason) and takes two reads to parse. *Split or simplify, e.g. "Process is bad — the absence of process just means prioritization by loudness."*

### Nits

- **[comics.md · Panel 6]** Image filename is `comic-06-cadence-sized-to-company.jpeg` but the concept (and caption) is cadence sized to the *horizon*. The file exists and renders, so this is cosmetic — but the name will mislead future edits.
- **[spec.md · Changelog, 2026-07-27 entry]** "Comics modality staged … with pending panel blocks; inline illustration placeholders staged" — the panels and figures were subsequently generated, but no entry closes the loop, so the changelog's last word is "pending."
- **[spec.md · Sources]** The internal PDF path is line-wrapped mid-filename across two lines ("…Right / Processes.pdf"); the file exists, but the wrapped path won't copy-paste cleanly.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("machinery in service of outcomes, never as ceremony"; "research before deciding what to build, not after") |
| The loop is explicit | met | index.md · Figure 1 + caption (discovery → validation → prioritization → delivery → learning feeding the roadmap); Statement bullets echo the stages |
| The numbers survive | met | index.md · Statement (4 h/week, one-third/one-quarter, quarterly/yearly, quarterly outcome reviews, top 1–2); checklist.md preserves all, bolded |
| Prioritization derives from strategy | met | index.md · Rationale ¶3 (idea bank, RICE, transparent no) + ¶5 (allocation argued via "backlog does not appear automatically"); checklist.md · "Handle Inbound Product Requests" |
| Process is matched to work | met | index.md · Statement bullet 6 + Rationale ¶5; checklist.md · "Choose the Right Development Process" |
| The checklist survives intact | met | checklist.md — all 17 sections present, numbers preserved (verified against section count; source PDF exists) |
| Credit is explicit | met | index.md · Authoritative References (full Foster & Nerlikar citation) |

Non-goals respected: yes — no Scrum/Kanban tutorial, engineering-side machinery explicitly deferred to [[run-engineering-processes]], the allocation discussion stays on the process side of the [[balanced-roadmap]] boundary, no framework is claimed mandatory (table row 3 says so explicitly).

Drift: none material. The one tension is spec-internal (Intent vs the "checklist survives intact" criterion — see the major finding), not post-vs-spec; `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — the same numbers (4 h/week, one-third/one-quarter, quarterly/yearly, top 1–2), the same frameworks (RICE, innovation sprints/Scrum/Kanban), the same ceremony-vs-outcome frame across all three modalities.
- **Terminology:** Consistent — "idea bank," "outcome pyramid," "innovation/iteration/operation," "ceremony" carry through; the comic's terser "one consistent framework" (no RICE) is appropriate compression, not drift.
- **Voice & tone:** Consistent — first-person declarative in the article, imperative in the checklist, VERA/MILA cast in the comic per journal convention.
- **Coverage parity:** Uneven in one place — checklist sections 3–4 (strategy session; vision/strategy communication) have no article or comic counterpart (see the major finding). All other checklist sections map to Statement bullets or Rationale paragraphs; the comic covers hook → problem → principle → discovery → prioritization → cadence → evidence → closer, matching the article's arc.

## Layer-by-layer notes

### Spec

- Complete template: all eight sections plus Changelog, front-matter `status: accepted` / `revised:` present. Unchecked Success-criteria boxes match journal convention (right-team spec is the same).
- Success criteria are genuinely checkable (specific numbers, named sections, named citation) — a good contract.
- Intent is one very long sentence (minor finding); Decision log usefully records the framing choice ("process serves the outcome" as the load-bearing idea).

### index.md

- House shape fully observed: status highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References; headings in Title Case; all three figures captioned and resolving; all four `[[cross-links]]` resolve (two in-journal, two cross-journal).
- Argument quality is high — each Rationale paragraph pairs a claim with a mechanism ("a silent no breeds shadow roadmaps," "overpromising is debt collected with interest").
- Repetition is the main weakness: the "research before build" and "four hours" beats recur near-verbatim (minor findings).
- The seven-part Statement is a clean spine; the table of contrasts is effective, with one overloaded cell (minor finding).

### checklist.md

- Serves its modality well: 17 sections of grouped, imperative action bullets with sub-lists where the source enumerates (research methods, journey stages, stakeholder groups); key numbers bolded.
- The one-line italic pointer to the Article tab is a good orientation device.
- Bullets are consistently actionable ("Ask…", "Avoid…", "Track…") — no rationale prose leaking in.

### comics.md

- Eight panels — right count for the form; every referenced image exists under `assets/images/right-processes/`; alt text and captions agree panel by panel.
- Clear arc (hook → problem → principle → mechanisms → closer) with a consistent visual metaphor (calendar/gears) that bookends: wall-to-wall calendar in Panel 1, lean calendar in Panel 8.
- Cast and style block match the journal's VERA/MILA convention.
- One filename/content mismatch on Panel 6 (nit).

## Fixes applied (2026-07-29)

- **Major — checklist strategy-session/vision-communication sections unechoed:** fixed. Added a sentence to index.md "How to Read This" pointing at [[product-strategy]] and [[outcomes]] and noting the two sections are reproduced in the checklist for completeness; added a matching paragraph to the spec's Intent so it agrees with the "checklist survives intact" criterion. checklist.md untouched.
- **Minor — "four hours a week, multiple methods" twin phrasing (Statement bullet 3 vs Rationale ¶2):** fixed. Rationale ¶2 reworded to "the weekly hours are protected, the methods varied, the conversations ongoing whether or not a project demands them"; the numbers stay in the Statement.
- **Minor — "research before deciding what to build" four occurrences:** fixed. Statement bullet 3 reworded to "Customer research informs what gets built, not just how it landed"; the highlight keeps the quotable phrasing per the spec's success criterion.
- **Minor — spec Intent one ~130-word sentence:** fixed. Split into three sentences (plus the new overlap paragraph); content unchanged.
- **Minor — overloaded table cell (row 1, right column):** fixed. Now reads "Process is bad — the absence of process just means prioritization by loudness." per the reviewer's suggestion.
- **Nit — Panel 6 filename `comic-06-cadence-sized-to-company.jpeg`:** skipped. Cosmetic only; renaming would touch comics.md and the asset with no user-visible change, so the file name stays.
- **Nit — changelog's last word is "pending":** fixed. The 2026-07-29 changelog entry closes the loop, noting panels and figures were subsequently generated.
- **Nit — Sources PDF path wrapped mid-filename:** fixed. Path now sits on one line in the spec's Sources section.
- Spec `revised:` bumped to 2026-07-29 with a changelog line. Build not run per work order.
