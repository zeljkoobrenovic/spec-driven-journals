# Review: The Competent Software Engineer

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and the tightest of the Guidebook pair. The manager-voice/engineer-voice split the spec demands holds cleanly, the checklist is a faithful first-person adaptation of the source PDF (verified section-for-section, including the nine self-review questions), and all cross-links resolve. The most useful improvement: the 30–60 minute blocked rule — the record's signature beat — is restated in six places in the article alone; the third and fourth restatements (table row and Concretely paragraph, back to back) add no new information.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · "What This Means in Practice" table + closing paragraph]** The 30–60 minute rule appears in the excerpt, highlight, Statement bullet 2, Rationale ¶2, the table's second row, and the Concretely paragraph — six restatements, with the last two adjacent. *Let the table row carry it and trim the Concretely re-explanation to the "what have you tried?" move.*
- **[comics.md · cast block]** The shared cast blurb describes ARLO as "an engineer newly stepping into management," but in this post's story he is an early-career IC being coached on engineering competence. The panels themselves read fine, but the generation-driving description contradicts the role. *Adjust the cast line for the two career-ladder posts (e.g. "an early-career engineer").*
- **[checklist.md · §§8, 14, 18]** Several source items are merged into single multi-clause checkboxes (e.g. §8 "I build side projects, complete tutorials or structured training, and practice coding challenges when useful" fuses three PDF items; §18 similarly). A box you can only half-tick is less runnable. *Split the three-clause merges where each clause is independently checkable.*

### Nits

- **[index.md · Statement bullet 2]** The self-unblocking repertoire is an eight-item comma series inside one sentence — parseable but dense; a colon-introduced list or em-dash grouping would breathe better.
- **[index.md · Rationale ¶2]** "it is also how goodwill is built, and goodwill is a real currency I watch" — the repeated "goodwill" pivot is slightly clunky; one "goodwill" would do.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (names both layers, "both layers are learnable, so I coach them explicitly") |
| Delivery habits survive | met | index.md · Statement bullets 1–3, Rationale ¶¶1–2, Figure 2; checklist.md §§1–4 |
| Craft layer survives | met | index.md · Statement bullets 4–6, Rationale ¶¶3–4; checklist.md §§8–18 |
| Growth loop survives | met | index.md · Statement bullet 7, Rationale ¶¶2 and 5, Figure 3; checklist.md §§5–7, 19 |
| Voice split holds | met | index.md manager's voice throughout; checklist.md consistently "I …" |
| Credit is explicit | met | index.md · How to Read This + Authoritative References (Orosz 2023, chapters named) |

Non-goals respected: yes — senior-level shift, tech-lead expectations, career strategy, and manager-side mentoring are all linked out ([[well-rounded-senior-engineer]], [[own-your-career]], [[mentoring]]) rather than restated; [[pragmatic-tech-lead]] is correctly absent from the article per the spec's non-goal.
Drift: none. Spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — top-priority-per-week, the 30–60 minute rule with the same repertoire list, golden-path/edge-case breakdown, worst-case estimates, and the nine-question self-review match the source PDF and each other.
- **Terminology:** consistent ("the repertoire," "goodwill," "shippable pieces," "scaffolding" all recur; comic Panel 8 reuses the article's scaffolding metaphor exactly).
- **Voice & tone:** the deliberate split (manager's article, engineer's checklist) is executed cleanly; the comic narrates in the article's coaching register.
- **Coverage parity:** even. The checklist is much broader (19 sections vs. the article's seven-bullet compression), but that is the designed relationship; every article beat maps to a checklist section, and nothing in the checklist contradicts the article.

## Layer-by-layer notes

### Spec

- Strong contract: criteria name the exact beats (30–60 rule, safety nets, nine questions) so alignment was mechanically checkable. The voice-split criterion is a good example of a testable non-content requirement.
- Decision log records the journal's Guidebook convention — useful precedent for the sibling record.

### index.md

- House record shape fully observed; headings in Title Case; all five cross-links resolve (well-rounded-senior-engineer, own-your-career, mentoring, management-101, getting-things-done).
- All three figures exist on disk and are captioned; Figure 2 (blocked-rule timeline) is the highest-value one, matching the record's signature mechanic.
- Rationale ¶1's "already more valuable than a brilliant one who does not" is the strongest sentence in the piece; the Scope section's AI-assisted-development revisit trigger is a thoughtful touch.

### checklist.md

- Verified against `sources/software-engineering-guidebook/Checklist_ TSEG _ Competent  Software Engineer (1).pdf`: all sections present in source order (Getting Things Done → Coding → Software Development Skills → Tools → Quick Weekly Self-Review), nine self-review questions intact, first-person adaptation consistent.
- Condensation is mostly judicious; only the three-clause merges noted above cost runnability.

### comics.md

- Eight panels, all image files exist, captions match alt text; empty-shipped-column → scaffolding-comes-down arc tracks the article's argument beat for beat.
- Panel 6 compresses the repertoire well ("duck, docs, and search"); only the cast-blurb role mismatch (see Minor) needs attention.

## Fixes applied (2026-07-29)

- **Verbatim self-repetition** — trimmed the sixth restatement of the 30–60 minute rule: the Concretely paragraph now says "the blocked rule" so the adjacent table row carries the full statement.
