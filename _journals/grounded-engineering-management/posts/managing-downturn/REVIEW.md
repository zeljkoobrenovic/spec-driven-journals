# Review: Managing a Downturn

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is tight and every success criterion is met; the article's three-stage ordering (own head → team's emotional state → machinery) is well argued and the checklist is a faithful reproduction of the source PDF (verified against `sources/making-of-a-manager/Checklist_ MoaM _ Managing Downturn (1).pdf`). The single most important thing to address: the source's section 3, "Build trust intentionally" — with its distinctive beats "explain how the team got here," "own my part honestly," "ask the team for help explicitly" — exists only in the checklist; the article's six-part Statement and the spec's Intent both skip it, even though trust is the record's load-bearing idea.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement / Rationale]** The source checklist's section 3 ("Build trust intentionally") has no echo in the article: "explain how the team got here," "own my part honestly," and "ask the team for help explicitly" appear nowhere in index.md, though the checklist carries them as a full numbered section and the record's thesis is trust. *Add one clause to the Statement (or a Rationale sentence) on intentional trust-building/owning your part.* (The spec's Intent shares the gap, so this is coverage parity, not drift.)
- **[index.md · Statement, bullet 5]** The "Handle layoffs and hard news" bullet is a 70+-word sentence with seven serial clauses — the hardest-to-parse line in the piece. *Split into two sentences (layoffs discipline / other hard news).*
- **[index.md · Statement bullet 6 + "What This Means in Practice" closing paragraph]** The weekly-rhythm item list is enumerated twice nearly in full (restate priority, deprioritized, risks, facts, questions, overload, recognition). *Second occurrence could compress to "the weekly rhythm runs without fail."*

### Nits

- **[index.md · Rationale ¶1]** "The two stories to drop are precise" — odd predicate; the stories are precisely *named*, not precise.
- **[index.md · front matter]** The excerpt is ~90 words — long for an index card, and it substantially duplicates the highlight blockquote's phrasing.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (leads with own head, lands on trust deepening) |
| Self-management sequence survives | met | index.md · Statement bullet 1, Rationale ¶1; checklist.md §1 |
| Emotional-signal read survives | met | index.md · Statement bullet 2, Rationale ¶2; checklist.md §2 |
| Communication cadence survives | met | index.md · Statement bullet 3, Rationale ¶3, Figure 2; checklist.md §4 |
| Scarcity-mode prioritization survives | met | index.md · Statement bullet 4, Rationale ¶4, Figure 3; checklist.md §§5–6 |
| Layoffs and hard-news scripts survive | met | index.md · Statement bullets 5–6, Rationale ¶5; checklist.md §§7–10 |
| Credit is explicit | met | index.md · How to Read This + Authoritative References |

Non-goals respected: yes — no drift into general self-management ([[managing-yourself]] is linked, not restated), ordinary-times prioritization, or severance/legal territory.
Drift: none. Spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — the two dropped stories, the know/don't-know/next-update cadence, one-top-goal scarcity mode, and the trust-deepens closer are identical across article, checklist, and comic.
- **Terminology:** consistent ("rumor gap," "scarcity mode," "stop-doing list," "fake optimism" recur verbatim).
- **Voice & tone:** consistent; the comic's second-person captions ("trust deepens when you show up honestly") are an acceptable form shift from the article's first person.
- **Coverage parity:** one gap — checklist §3 "Build trust intentionally" has no article echo (see Minor findings). Everything else in the checklist maps to an article beat.

## Layer-by-layer notes

### Spec

- Well-formed against the template; criteria are genuinely checkable (each names concrete beats that either survive or don't).
- Decision log usefully records *why* the ordering is the frame — the strongest part of the spec.
- Intent enumerates the machinery but omits the source's trust-building section; if the article is amended per the Minor finding, update Intent in the same pass.

### index.md

- House record shape fully observed: highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → References; headings in Title Case.
- All four `[[…]]` cross-links resolve to existing permalinks (managing-yourself, getting-things-done, nurturing-culture, feedback).
- All three figures exist on disk and are captioned; captions add interpretation rather than repeating alt text.
- Anti-patterns are specific and earn their place ("the slow, comfortable layoff," "forgetting the survivors").

### checklist.md

- Faithful, section-for-section, item-for-item reproduction of the source PDF (11 sections; verified). Well-formed task-list markdown; hard-news sub-groups render cleanly.
- First-person adaptation ("Stop telling myself…") is consistent; section headings keep the source's imperative form, which reads fine as a working checklist.

### comics.md

- Eight panels, all image files exist on disk; captions match their alt text; the VERA/ARLO cast and the storm-cloud → bridge visual arc are consistent.
- The hook → problem → wrong way → principle → mechanics → cost → closer beat structure mirrors the article's argument accurately, ending on the same quotable closer.

## Fixes applied (2026-07-29)

- **Checklist-only spec beats** — added a trust-building clause to Statement bullet 3 in index.md (explain how the team got here, own my part honestly, ask the team for help explicitly), closing the checklist §3 coverage gap.
- **Verbatim self-repetition** — compressed the second full enumeration of the weekly-rhythm items in the Concretely paragraph to "the weekly rhythm runs without fail"; Statement bullet 6 remains the single full listing.
