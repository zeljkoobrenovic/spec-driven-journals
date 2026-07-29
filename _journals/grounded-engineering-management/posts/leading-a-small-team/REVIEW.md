# Review: Leading a Small Team

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The trust-as-channel framing and the diagnosis-before-treatment move give the article a clear spine, the checklist reproduces the source PDF faithfully, and the comic carries the article's beats without contradiction. All spec success criteria are met, all six cross-links resolve, and every figure and panel image exists on disk. The single most useful improvement is trimming the opening highlight — at ~130 words in four chained sentences it strains the spec's own "quotable" bar.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · opening highlight]** The Principle blockquote runs ~130 words across four long sentences, packing all seven Statement elements into one block. The spec's first criterion is "Principle is quotable"; this is comprehensive rather than quotable. *Consider cutting to the trust foundation + test + diagnosis, letting the Statement carry the full list.*
- **[index.md · excerpt, highlight, Statement bullet 7, Practice table row 6, Anti-Patterns "Making it work forever"]** The exact phrase "quickly and respectfully" appears five times in one file. The house shape legitimately revisits beats, but the verbatim phrase repetition is noticeable on a straight read. *Vary the wording in two or three of the five spots.*
- **[index.md · Statement bullets 2–3]** Bullet 2 ("invest regular time in each of them") and bullet 3 (the weekly 1:1) overlap — the regular-time commitment is restated as the 1:1 one bullet later, and "ask more questions instead of jumping straight to advice" (bullet 2) is really 1:1 behavior that the Rationale also treats under the 1:1 paragraph. *Tighten bullet 2 to the person-not-performer stance.*

### Nits

- **[index.md · excerpt]** The excerpt is a single ~90-word two-sentence block — long for an index card; the second sentence alone would carry it.
- **[index.md · Statement bullet 3]** The bullet mixes the agenda list and three quoted questions into one dense run; a colon-separated split or the questions on their own line would ease parsing. (Grouped: no grammar or markdown errors found anywhere in the four files.)

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (trust, "work for me again", growth 1:1s, transparency, diagnosis, strengths, exits) | met (see minor on length) | index.md · highlight |
| The 1:1 shape survives (weekly, priorities/growth/obstacles, questions first, three questions) | met | index.md · Statement bullet 3, Rationale ¶2; checklist.md §2–3 |
| The diagnosis survives (skill/motivation/fit before acting) | met | index.md · Statement bullet 4, Rationale ¶3, Figure 2; checklist.md §4; comics.md Panel 6 |
| The strengths stance survives | met | index.md · Statement bullet 6, Rationale ¶4, Figure 3; checklist.md §6 |
| Culture and fit survive (no brilliant jerks, divider, better-fit first, quick respectful exits) | met | index.md · Statement bullet 7, Rationale ¶5; checklist.md §7–8; comics.md Panel 7 |
| Credit is explicit (Zhuo, Portfolio/Penguin, 2019) | met | index.md · How to Read This + Authoritative References |

Non-goals respected: yes — feedback craft, the ramp, growing-team scale, and the deep career conversation are all referenced but not covered; "share feedback in both directions" stays at the level the spec allows.
Drift: none. Spec `accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. The trust foundation, the "work for me again" test, the status-meeting anti-pattern, the diagnosis tree, and the quick-respectful exit all appear in article, checklist, and comic with the same meaning.
- **Terminology:** Consistent — "skill, motivation, or fit", "brilliant jerks", "divider", "status-meeting 1:1" are used identically across files.
- **Voice & tone:** Consistent. The comic's second-person VERA/ARLO teaching frame ("scored by them, not by you") is the journal's standard comic register, not a drift from the first-person article.
- **Coverage parity:** Even. The comic compresses vulnerability/accountability and strengths investment out (reasonable for eight panels); the checklist's §9 "Keep the big picture in mind" carries source-PDF beats (outcomes through people, people-then-process) the article delegates to [[what-is-management]] — acceptable since the checklist reproduces the source.

## Layer-by-layer notes

### Spec

- Well-formed against the template; all sections present, criteria concrete and individually checkable, no dangling open questions.
- Decision log usefully records the framing choice (trust as information channel; diagnosis as second load-bearing move) — the article visibly delivers both.
- Non-goals name four adjacent records; all four slugs resolve to real permalinks.

### index.md

- House record shape followed exactly (highlight → Statement → How to Read This → Rationale → Practice table → Anti-Patterns → Related → Scope → References); headings in Title Case.
- Rationale paragraphs each earn their place and map 1:1 to Statement bullets; the "cheapest feedback"-style bolded openers make it skimmable.
- All three figures exist on disk and are captioned; all six `[[…]]` cross-links resolve (five in-journal, career-conversations in the people journal).
- Main weaknesses are the highlight's length and the small verbatim repetitions noted above.

### checklist.md

- Faithful, near-verbatim reproduction of `Checklist_ MoaM _ Leading a Small Team (1).pdf` (spot-checked against the PDF): same nine groups, same items, first-person adaptation only.
- Sections numbered 1–9 as required; task-list markdown well-formed throughout; terminology matches the article.

### comics.md

- Eight panels, standard hook→problem→wrong-way→principle→how→mechanic→cost→closer arc; captions match their alt text; all eight image files exist.
- Visual metaphor (foundation block, diagnosis tree, open door) is consistent panel to panel and mirrors the article's Figures 1–2.

## Fixes applied (2026-07-29)

- **Overlong opening highlight** — tightened the Principle blockquote from ~130 to ~85 words: kept the trust foundation, the "work for me again" test, and the skill/motivation/fit diagnosis; the full seven-element list now lives only in the Statement.
- **Verbatim self-repetition** — "quickly and respectfully" reduced from five sites to two: dropped from the highlight (via the tightening above) and reworded in the excerpt ("move the person on promptly and with respect"); kept verbatim in Statement bullet 7 and Practice table row 6 (whose right column quotes "quickly").
