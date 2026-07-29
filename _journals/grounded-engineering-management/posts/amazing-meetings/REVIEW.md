# Review: Amazing Meetings

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The "one primary purpose as design constraint" framing does real work — the article shows *why* the taxonomy matters (the purposes' requirements conflict) instead of just listing it, and the gut-check-as-standing-filter elevation is the record's best original move. The checklist is a near-verbatim, verified reproduction of the source PDF, all cross-links resolve, and every figure and panel image exists. The most useful improvement is comic Panel 3's caption, which leans on an article phrase ("the loop") that a comic-first reader has no way to decode.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[comics.md · Panel 3 caption]** "observers are not free, and the loop has cheaper channels" — "the loop" only makes sense if you have read the article's "keep them in the loop" line; standalone (and comics are read standalone) it is cryptic. *Say it plainly: "keeping people in the loop is what written summaries are for."*
- **[index.md · Practice table row 4 vs Rationale ¶3 / Anti-Patterns "Live ramp-up"]** The same claim is quantified two ways: the table says context gets delivered "in the first twenty minutes", the Rationale and Anti-Patterns say the meeting "spends its first half" on it. Not a contradiction, but the numbers should agree in a record this precise. *Pick one.*
- **[index.md · Statement bullet 4]** Six facilitation moves in one semicolon chain (encourage dissent; formats for quieter people; watch interruptions; make space; directed questions; limit overtalking) — the densest bullet in the Statement. *Split into safety vs airtime, mirroring checklist §5 and §6.*

### Nits

- **[index.md · Statement bullet 6]** The gut-check attendee list drops "a feeling of being welcomed", which the source PDF and checklist §9 both include — a small fidelity trim in the article's summary; the checklist carries it in full.
- **[index.md · Scope and Revisiting]** The revisit trigger "if a quarter passes without a single recurring meeting being restructured or cancelled" assumes there is always at least one meeting worth killing per quarter — deliberate forcing function or over-strong heuristic; worth an author look. (Grouped: no grammar or markdown errors found in any file.)

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (one purpose everything serves; gut-check close) | met | index.md · highlight |
| The five purposes survive (with success stateable, not too many things) | met | index.md · Statement bullet 1, Rationale ¶1, Figure 1; checklist.md §1–2; comics.md Panels 2, 4 |
| Design choices follow purpose (format, attendees, agenda/pre-reads, capture planned) | met | index.md · Statement bullets 2–3, Rationale ¶2–3; checklist.md §3–4; comics.md Panel 5 |
| Facilitation is active (safety, quieter formats, interruptions, directed questions, overtalking) | met | index.md · Statement bullet 4, Rationale ¶4, Figure 2; checklist.md §5–6; comics.md Panel 6 |
| Close and per-purpose checks survive (summary, owners/timelines, five check blocks) | met (five purpose-specific blocks live in checklist §8, referenced from How to Read This; Rationale ¶1 samples three of them) | index.md · Statement bullet 5, Rationale ¶5; checklist.md §7–8; comics.md Panel 8 |
| Gut-check survives (good use of time, truly needed, me personally) | met | index.md · Statement bullet 6, Rationale ¶5, Figure 3; checklist.md §9; comics.md Panel 7 |
| Credit is explicit | met | index.md · How to Read This + Authoritative References |

Non-goals respected: yes — the executive calendar, the execution system, and 1:1/team rhythm are cross-linked, not covered; the gut-check on personal attendance stays within single-meeting scope.
Drift: none. Spec `accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. The five purposes, the everything-meeting, the audience-meeting, active airtime management, owners-and-timelines, and the gut-check filter appear across article, checklist, and comic with the same meaning; comic Panel 8's "negative space" calendar matches the article's "my calendar shows the negative space too."
- **Terminology:** Consistent — "primary purpose", "gut-check", "airtime", "owners and timelines", "extraneous" travel intact across all three modalities.
- **Voice & tone:** Consistent; the comic's second-person register is the journal's standard VERA/ARLO frame.
- **Coverage parity:** Even. The comic compresses preparation and the per-purpose checks into Panels 5 and 4 respectively (reasonable for eight panels); no modality introduces a beat the spec lacks.

## Layer-by-layer notes

### Spec

- Well-formed; seven criteria, all individually checkable; the decision-log entry ("one primary purpose as the design constraint … gut-check elevated to a standing cancellation discipline") is exactly what the article delivers — strong spec-to-post fidelity.
- Intent is a single ~120-word sentence-paragraph — within house norms for this journal but at the outer edge of it.
- All three Non-goal slugs resolve (meetings in the executive journal; the other two in-journal).

### index.md

- House shape followed exactly; Title Case headings; Rationale ¶1's argument that the purposes' *requirements conflict* is the record's best passage — it justifies the taxonomy instead of merely importing it.
- All three figures exist and are captioned; all four Related Records cross-links resolve.
- Weaknesses are local: the twenty-minutes/first-half wobble and the overloaded facilitation bullet.

### checklist.md

- Verified near-verbatim against `Checklist_ MoaM _ Meetings (1).pdf`: nine numbered sections plus the five purpose-specific blocks and the final gut-check, all items present (including "a feeling of being welcomed"), first-person adaptation only, well-formed task lists.
- The italic "Run the block that matches this meeting's primary purpose" instruction in §8 is a good operational touch not in the source.

### comics.md

- Eight panels, standard arc; captions match alt text; all eight image files exist on disk.
- Panel 7 (deleting your own cobwebbed meeting) is the strongest beat — it makes the gut-check personal, which the article only states.
- Panel 3's caption is the one standalone-comprehension gap (see minor).

## Fixes applied (2026-07-29)

- **Comic caption fix** — Panel 3 caption no longer leans on the article-only phrase "the loop has cheaper channels"; it now reads "keeping people in the loop is what written summaries are for", per the review's suggested plain wording.
