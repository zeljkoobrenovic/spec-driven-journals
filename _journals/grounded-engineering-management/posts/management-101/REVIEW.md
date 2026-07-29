# Review: Management 101

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The two-sided-contract framing is carried consistently across article, checklist, and comic; every spec criterion is met; the checklist was spot-checked against the source PDF (`Checklist_ MP _ Management 101.pdf`) and reproduces it faithfully, section for section and nearly word for word. The most useful improvement is a one-line framing fix: the checklist's "I" is the reader-as-report while the article's "I" is the executive, and nothing marks the switch.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · header note ↔ index.md]** The antecedent of "I" flips between tabs: in the article, "I" is the author-executive ("What I owe every report"); in the checklist, "I/me" is the reader-as-report ("Has regular 1:1s with me", "What I am responsible for as a report"). Faithful to the source PDF, but the italic header line does not mark the perspective, so a reader arriving from the article gets a one-beat jolt. *Extend the header note with a phrase like "run it from the report's chair."*

### Nits
- **[index.md · Rationale, para 5]** "Managers are imperfect; I ask reports to give theirs some grace" — "theirs" has to be decoded as "their manager"; "give their manager some grace" reads in one pass.
- **[index.md · front matter]** The `excerpt` restates the Principle highlight nearly clause for clause (~90 words twice). House pattern, cosmetic only. *(Grouped.)*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable — two-sided contract + resource-not-mind-reader | met | index.md · Status/Principle highlight |
| Manager side survives (1:1s, connection, feedback registers, growth, promotion clarity, stretch, advocacy, focus) | met | index.md · Statement bullets 1–5; checklist.md §1 (all 15 source items) |
| Report side survives (agenda, asks, speak up, own growth and boundaries) | met | index.md · Statement "What I ask every report to own"; checklist.md §2 |
| Working-with-a-manager guidance survives (solutions, advice, grace, own side, diagnose) | met | index.md · Rationale paras 4–5, Anti-Patterns; checklist.md §3 |
| Credit explicit — Fournier + Management 101 chapter | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes — no 1:1 cadence/tooling policy is set (the "Concretely" line asks that people can *name* their cadence, which stays on the right side of the fence), and the managing-people mechanics and own-your-career playbook are pointed at, not restated.
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. Contract-with-two-signatures, praise-public/criticism-private-and-prompt, mind-reader, manager-as-part-of-compensation all identical across article, checklist, and comic.
- **Terminology:** Consistent — "contract," "two signatures," "resource, not a mind reader" recur verbatim where they should.
- **Voice & tone:** Consistent register; the one seam is the article-vs-checklist "I" flip filed above.
- **Coverage parity:** Even. The comic carries the article's arc beat for beat (never-seen-good → calibrated to neglect → mind-reader → contract → manager side → report side → skill → compensation). Checklist §4 (self-assessment) has no article echo, which is fine — the article's "How to Read This" names it as checklist-only content.

## Layer-by-layer notes

### Spec
- Full template, tight, no bloat; the decision log's "two-sided contract rather than a what-good-managers-do list" entry is exactly the kind of framing decision a spec should record.
- All five criteria are checkable and check out.

### index.md
- Clean house shape (Statement → How to Read → Rationale → What This Means in Practice → Anti-Patterns → Related → Scope → References); Title Case headings throughout.
- The Rationale is genuinely argued, not asserted — the "1:1s are the load-bearing mechanism" paragraph is the strongest and justifies the checklist's item order explicitly.
- All four crosslinks resolve (`managing-people`, `mentoring`, `what-is-management`, `own-your-career`, plus `career-conversations` in the people journal). All three figures exist on disk and are captioned.

### checklist.md
- Verified against the source PDF: four sections, item texts reproduced essentially verbatim; numbered sections and well-formed task-list markdown. A faithful, runnable distillation.

### comics.md
- Eight panels, all image files present, captions match alt text, shared VERA/ARLO cast and style block.
- Panel 8's closer ("a good manager is a meaningful part of compensation — and this contract is what 'good' means") lands the article's final Rationale beat precisely.
