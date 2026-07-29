# Review: Mentoring

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The "designed first leadership role" framing is carried cleanly through all three modalities, every spec criterion is met, all crosslinks (including the cross-journal `engineering-onboarding`) resolve, and all figure and panel images exist on disk. The most useful improvement is placement: Figure 3 (the intern-project quadrant) sits under "What This Means in Practice" next to a paragraph that never mentions interns, a section away from the variant it illustrates.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · What This Means in Practice · Figure 3]** The intern-project quadrant figure follows the "Concretely:" paragraph, which says nothing about interns; the beat it illustrates lives in Statement bullet 4 and one table row above. The figure reads as orphaned where it stands. *Move it up beside the intern table row, or into the Statement's variants bullet.*

### Nits
- **[index.md · Statement, bullet 5]** Bullets 1–4 describe "the mentor"; bullet 5 switches to "I" (the executive who matches and resources). Deliberate — "How to Read This" explains the author's chair — but the switch inside one list is momentarily jarring; a lead-in like "On my side:" would smooth it.
- **[index.md · front matter]** The `excerpt` restates the Principle highlight's beats nearly verbatim. House pattern, cosmetic only. *(Grouped.)*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable — designed role, prep before day one, taper, saying no beats doing it badly | met | index.md · Status/Principle highlight |
| Pre-day-one preparation survives (purpose, success, environment/access, docs, milestone-sliced project, check-in plan) | met | index.md · Statement bullet 1; checklist.md §1 |
| Conduct survives (orientation, listening, confusion/overload, docs-first, independence, small corrections) | met | index.md · Statement bullets 2–3, Rationale para 3; checklist.md §§2–3 |
| Variants survive (intern: real/specific/non-urgent/sized/presented; new hire: docs actively improved, relationships, how things really get done) | met | index.md · Statement bullet 4, Practice table, Figure 3; checklist.md §§4–5 |
| Close survives (review, reflect, feed back into onboarding, connections and next steps) | met | index.md · Statement bullet 5, "Concretely" para; checklist.md §8 |
| Credit explicit — Fournier + Mentoring chapter | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes — no manager mechanics (explicitly fenced in Related Records), no tech-lead territory, and onboarding is plugged into via `[[engineering-onboarding]]` rather than defined.
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. Lost-first-week-is-permanent-data, milestone-sliced project as curriculum, calibrated withdrawal, refusal allowed, close-the-loop — identical across article, checklist, and comic.
- **Terminology:** Consistent — "designed," "taper"/"calibrated withdrawal," "milestone-sliced," "say no" recur where they should; the comic's "'just grab me whenever'" quotes the article's vague-relationship anti-pattern verbatim.
- **Voice & tone:** Consistent; comic uses the shared VERA/ARLO cast and register.
- **Coverage parity:** Mostly even. The comic compresses the intern/new-hire variants out entirely (its eight panels carry the generic arc) — defensible for the form, and the checklist carries both variants in full. Within the article, the variants get Statement + table coverage but no Rationale paragraph of their own; the "why non-urgent" argument lives only in the anti-pattern bullet. Worth knowing, below finding threshold.

## Layer-by-layer notes

### Spec
- Full template; the Intent paragraph is long but earns it — it is effectively the article's outline and every clause in it landed in the post.
- Six criteria, all checkable, all met; the decision log records the load-bearing framing choice (lead with preparation and taper, not feel-good aspects).

### index.md
- Strong Rationale — "fails in the setup far more often than in the relationship" and "a bad mentor is worse than no mentor" are argued, not asserted, and both map to specific checklist sections.
- All four crosslinks resolve; all three figures exist on disk and are captioned (placement of Figure 3 filed above).
- Title Case headings and the house record shape throughout.

### checklist.md
- Eight numbered sections, well-formed task-list markdown, terminology matching the article; structure mirrors the article's five-part Statement plus mindset/pitfalls. Nothing reads invented against the named source PDF; not independently re-verified page-for-page (the sibling Management 101 PDF spot-check confirmed the journal's verbatim-reproduction pattern).

### comics.md
- Eight panels, all image files present, captions match alt text, consistent cast/style.
- The arc (surprise assignment → lost first week → "grab me whenever" → designed before day one → orientation → taper → say no → close the loop) tracks the article exactly; Panel 7 correctly carries the refusal-is-allowed beat, the record's most distinctive claim.
