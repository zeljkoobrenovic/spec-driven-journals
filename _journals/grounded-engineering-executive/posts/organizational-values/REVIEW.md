# Review: Organizational Values

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the cleaner records in the journal. The three-test quality bar (reversible / applicable / honest) is the centerpiece the spec asked for and it carries all four files; the checklist reproduces all eight source sections; the comic's poster-vs-worn-card metaphor is consistent from panel 1 to panel 8 and every image exists. The most important thing to address is minor: the "does not say" column of the practice table packs corrective sub-clauses into several cells, which blunts the table's scannability.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · What This Means in Practice table]** Several right-column cells state the disclaimed misreading and then append a correction after an em dash (e.g. "Never aspire to change — aspiration drives the behavior change; the value records its arrival."), so the cell argues instead of just naming what the principle does not say. Row 1's right cell ("Values are just strategy restated — they are the decision-guiding layer…") has the same double duty. *Trim each cell to the misreading; let the body carry the correction.*
- **[checklist.md · headings]** Sections use H3 (`### 1. Clarify…`) where the sibling checklist in organizational-design uses H2, so the two Checklist tabs render with different heading weight. *Align heading level with the journal's other checklists.*

### Nits
- **[index.md · after Figures 1–3]** Double blank lines after each figure caption (e.g. lines 32–33, 46–47) — inconsistent with single-blank-line spacing elsewhere in the file.
- **[comics.md · Panel 3 alt text]** "holds an excellence card next to a mirror reflecting it blank" is hard to parse as a described image; the caption is clear, but the alt text could name the idea more plainly (mirror shows nothing because the opposite is nonsense).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable ("decision tools, not decoration" in one paragraph) | met | index.md · Principle highlight |
| Rationale argued, not asserted (why the three tests; why behavior precedes documentation) | met | index.md · Rationale, first two paragraphs |
| Checklist survives intact — all eight PDF sections in Checklist tab | met | checklist.md · sections 1–8 match the spec's list exactly |
| Anti-patterns concrete, at least three | met | index.md · Anti-Patterns (six, including the three the spec names) |
| Credit explicit (Primer + lethain.com companion) | met | index.md · Authoritative References |

Non-goals respected: yes — strategy deferred to [[engineering-strategy]], standards to [[calibrating-your-standards]], and no value list is proposed for any specific organization (explicitly disclaimed in How to Read This).
Drift: none. Spec `accepted` status is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — the three tests, behavior-before-documentation sequence, extend-over-invent preference, slow rollout, and the five integration points (hiring, onboarding, promotions, 1:1s, decisions) match across article, checklist, and comic.
- **Terminology:** Consistent — "reversible / applicable / honest", "used, not framed", "buy-in rather than announcing", "applause" (article Rationale and comic Panel 3 both use it) carry through.
- **Voice & tone:** Consistent first-person declarative article; imperative-interrogative checklist as the form requires; comic in the journal's shared VERA/LEO register.
- **Coverage parity:** Even. The comic drops scope (extend vs invent) and maintenance — a reasonable compression for eight panels; both are present in article and checklist. No modality introduces a beat the others lack.

## Layer-by-layer notes

### Spec
- Five success criteria, all checkable; the checklist criterion helpfully enumerates the eight expected sections, making the check mechanical.
- Decision log captures the load-bearing choice (quality tests over rollout as centerpiece) with its rejected alternative — a model decision-log entry.
- Non-goals cleanly fence the two adjacent records. No bloat; changelog current.

### index.md
- House shape complete: highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References; Title Case headings throughout.
- The Rationale's "each test kills a distinct failure mode" paragraph is the strongest passage — it argues rather than asserts, satisfying the spec's toughest criterion.
- Three figures, captioned and numbered; files exist. Five [[cross-links]], all resolving to sibling records, each with a stated relationship.
- "A value used weekly needs no poster" (Rationale) lands as the memorable close and is reused as the comic's closer — good deliberate echo, not accidental repetition.

### checklist.md
- Serves its operational purpose: eight numbered sections mirroring the source PDF, question-form checkable items, the traps split into the two named categories (Identity, Vague Prioritization).
- Nested checkboxes under "choosing intentionally between" (section 2) are a nice touch for a real working session.
- Heading level inconsistency with sibling checklists (see Minor); otherwise clean mechanics.

### comics.md
- Eight panels with a tight arc: poster hook → ignored poster problem → three test panels → behavior-first principle → values-in-use → "no poster needed" closer. The poster/worn-card prop is the through-line and stays consistent.
- All eight referenced panel images exist under assets/images/organizational-values/.
- Captions are one line, match their alt text, and compress the article's exact claims without adding new ones.
