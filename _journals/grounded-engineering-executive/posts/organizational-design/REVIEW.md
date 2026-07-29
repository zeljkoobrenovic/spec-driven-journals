# Review: Organizational Design

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready appendix record. The spec is tight and fully checkable, the article carries the "fix the system, not the symptom" framing cleanly, the checklist reproduces all nine sections with the numbers intact, and the eight-panel comic tells the same story in the same voice with every panel image present on disk. The most important thing to address is small: a tangled opening sentence in "How to Read This" and a dense hypergrowth paragraph that packs three distinct ideas into one block.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · How to Read This, first sentence]** "unlike the core records in this journal, grounded in Will Larson's *The Engineering Executive's Primer*, this one is grounded in his earlier…" — the participial phrase "grounded in…Primer" dangles between two commas and momentarily reads as modifying "this journal" or "this one". *Restructure: "the core records in this journal are grounded in X; this one is grounded in Y."*
- **[index.md · Rationale, "Hypergrowth is an entropy problem" paragraph]** Three distinct ideas (hiring/training load, structural scaling per order of magnitude, entropy controls) are compressed into one long paragraph; the entropy list at the end reads as a breathless inventory. *Consider splitting into two paragraphs or trimming the entropy inventory to its top three items.*
- **[checklist.md · "Diagnose Each Team's State", line "- For each team, mark its current state:"]** A plain bullet sits inside an otherwise task-list section, breaking the checkbox pattern (renders as a bulleted line among checkboxes). *Make it a lead-in sentence outside the list, or drop the leading hyphen.*

### Nits
- **[checklist.md · Entropy control]** "Concentrate on hiring and growth rather than spreading it evenly across the board" is ambiguous about what is being concentrated ("it" has no clear referent); the source idea is concentrating hiring into fewer teams at a time.
- **[index.md · front matter excerpt]** The excerpt is four sentences and near-paragraph length for an index card; the last sentence ("…should not need me in it") is the strongest and could carry more of the weight.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (diagnose before prescribing; shift scope, not people) | met | index.md · Principle highlight |
| Four states explicit with matching fixes | met | index.md · Statement + Rationale + Figure 1; checklist.md · Diagnose/Apply sections |
| Numbers survive (6–8, 4–6, ~8, 8–10→4–5, layer per order of magnitude, ~3 interviews/week) | met | index.md · Statement + Rationale; checklist.md · Size/Hypergrowth |
| Consolidation over peanut-buttering argued, not listed | met | index.md · Rationale ("Consolidated investment compounds…") + Figure 3 |
| Succession included, replaceability as endgame | met | index.md · Statement, Practice, Anti-Patterns; checklist.md · Build Succession Plans |
| Checklist survives intact — nine sections, numbers preserved | met | checklist.md (9 H2 sections, all numbers present) |
| Credit explicit (Larson, lethain.com) | met | index.md · Authoritative References |

Non-goals respected: yes — no reorg playbook, no org chart, hiring deferred to [[hiring]], leadership team deferred to [[gelling-your-engineering-leadership-team]], numbers framed as defaults ("shift the burden of proof, nothing more").
Drift: none. Spec `accepted` status is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — the four states, one-fix-per-state, sizing numbers, shift-scope-not-people, consolidate-vs-peanut-butter, and succession all match across article, checklist, and comic.
- **Terminology:** Consistent — "peanut-butter", "gelled/re-gelling", "treading water", "slack" carry through all three files; comic Panel 7's "mitosis" is a fresh metaphor but describes the same grow-to-8–10-split-into-4–5 rule.
- **Voice & tone:** Consistent first-person declarative in article; checklist is imperative as its form requires; comic uses the shared VERA/LEO cast in the journal's usual register.
- **Coverage parity:** Even. The comic compresses hypergrowth/entropy and organizational risk out (reasonable for eight panels); checklist and article both carry them.

## Layer-by-layer notes

### Spec
- All seven success criteria are genuinely checkable against the artifacts; no Intent prose with checkboxes.
- Non-goals correctly fence off the two adjacent records and disclaim the numbers as laws.
- Decision log records the appendix framing and the load-bearing-idea choice; changelog is current. No bloat.

### index.md
- House record shape followed: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References. Headings are Title Case.
- The says/does-not-say table is well constructed; each row pairs a real claim with a real disclaimed overreach.
- Three figures present with numbered captions; all image files exist under assets/.
- Six [[cross-links]] present, all pointing at real sibling records in this journal.
- The bolded topic-sentence pattern in Rationale makes the argument skimmable; only the hypergrowth paragraph overloads it (see Minor).

### checklist.md
- Serves its purpose as an operational working checklist: nine grouped sections, imperative checkable items, numbers preserved exactly (6–8, 4–6, ~8, 8–10→4–5, order-of-magnitude layers, three interviews/week).
- Sub-grouping (Manager load / Team size; per-state fixes; Hiring / Scaling / Entropy) keeps the long list runnable.
- One formatting break (the non-checkbox lead-in bullet, see Minor) and one ambiguous item (see Nits); otherwise clean.

### comics.md
- Eight panels, hook → problem → principle → fix → two rules → mechanism → closer: a sound arc that mirrors the article's Statement order.
- All eight referenced panel images exist under assets/images/organizational-design/.
- Captions are one line each, match their alt text, and stay within the form; cast/style block present and consistent with the journal's VERA/LEO convention.
