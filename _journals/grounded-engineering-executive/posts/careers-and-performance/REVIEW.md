# Review: Careers, Hiring, and Performance

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The spec is one of the stronger contracts in the journal (seven individually checkable criteria, an explicit appendix-record decision, a clean boundary with [[hiring]]), and every criterion is met. All three article figures and all eight comic panel images exist on disk; all six cross-links resolve. The most useful fix is small: the Statement announces a four-part operating model while the Principle highlight lists five instruments (cold sourcing is the odd one out), and the spec's changelog still says the comic images are "pending generation" when they exist.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement]** "My operating model has four parts" — but the Principle highlight (and the spec's Intent) enumerate five instruments: funnel, loops, **cold sourcing**, ladders, calibration. Cold sourcing gets no Statement bullet and first appears in the Rationale ("Referral networks reproduce themselves"), so a reader checking the highlight against the Statement finds a missing part. *Either add a fifth bullet or fold cold sourcing into the funnel bullet explicitly.*
- **[spec.md · Changelog, 2026-07-26 entry]** "Comics modality staged … images pending generation" — all eight panel images (and the three article figures) now exist, so the changelog's latest entry misstates the post's state. *Add a changelog line recording the image generation.*

### Nits
- **[checklist.md · headings]** Top-level sections use `##` where the sibling post `calibrating-your-standards/checklist.md` uses `###` — a cross-post rendering inconsistency in the Checklist tab's heading sizes.
- **[comics.md · alt text]** Alt texts here drop the "Comic panel:" prefix that the `calibrating-your-standards` comic uses — another cross-post consistency nit, not a defect within this post.
- **[index.md · What This Means in Practice, para after table]** The second emphasized practice packs sponsor/mission/ladder/role-models/calibration into one 60-word sentence with two nested lists; parseable but dense. *Consider splitting after "task offloading."*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (luck-reduction thesis in one paragraph) | met | index.md · Principle highlight |
| Funnel concrete (4 stages + instrumentation + extended funnel) | met | index.md · Statement bullet 1, Rationale para 2, Figure 2; checklist.md · Hiring Funnel |
| Calibration stance explicit (ladder not each other; no curve; read reviews; safety) | met | index.md · Statement bullet 4 + Rationale para 5; checklist.md · Calibration |
| Immediate feedback stated | met | index.md · highlight + Rationale final para; checklist.md · Performance Cycles |
| Boundary with [[hiring]] stated | met | index.md · How to Read This, para 2 |
| Checklist survives intact (all 8 PDF sections, incl. 10–20 candidates, annual refresh) | met | checklist.md · all eight sections present; Interview Loop Design has both numbers |
| Credit explicit (*An Elegant Puzzle* + lethain.com origins) | met | index.md · Authoritative References |

Non-goals respected: yes — no compensation philosophy, no specific ladder document, no HR/legal guidance, and the "reduces luck's share, does not eliminate it" boundary is stated verbatim in the practice table (row 1).
Drift: none of substance; only the stale changelog entry noted above. Spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** consistent — luck-as-default-allocator thesis, four-stage funnel extended past the offer, rubrics-over-puzzles, ladder-not-each-other calibration, and no-surprise cycles appear identically in article, checklist, and comic.
- **Terminology:** consistent — "identify → motivate → evaluate → close," "against the ladder, not against each other," "a summary, not a surprise/ambush" recur verbatim or near-verbatim across surfaces.
- **Voice & tone:** consistent first-person executive register; the comic's VERA/LEO framing matches the journal cast.
- **Coverage parity:** good — the comic compresses cold sourcing, career-level risks, and specialized roles out entirely, which is acceptable for an eight-panel form; the checklist carries all of them. Every comic beat traces to an article section.

## Layer-by-layer notes

### Spec
- Excellent decision log: the appendix-record framing, the [[hiring]] boundary, and the luck-reduction unifying frame are each recorded with rationale — the third explains why this is one principle rather than four.
- Success criteria name concrete artifacts (specific numbers, named sections), which made this review's Layer 3 nearly mechanical — the intended property of a good contract.
- Only defect is the stale final changelog entry (images "pending").

### index.md
- House shape and Title Case headings correct; matches `inspected-trust`/`managing-energy` section order.
- The Rationale is the strongest section: six paragraphs, each one argument, each with a mechanism ("the loudest recent story wins," "calibration becomes a courtroom").
- Eight anti-patterns, all concrete and named memorably ("The cycle-time ambush," "Stack ranking by another name").
- The Statement's four-vs-five mismatch with the highlight is the only structural wrinkle (flagged above).

### checklist.md
- The longest checklist in the set reviewed, but faithfully mirrors all eight source-PDF sections with sensible sub-grouping; the non-checkbox bullets under "Risks to Consider" and "Benefits to Validate" are appropriate (considerations, not actions).
- Concrete numbers required by the spec (10–20 candidates, annual refresh) are present under Interview Loop Design.
- `##` heading depth differs from sibling checklists (nit above).

### comics.md
- Eight panels with a clean arc: hook → problem (dice) → principle (gears) → funnel → rubrics → ladder → feedback → closer (retired die). The die/gear metaphor is consistent and pays off in the final panel.
- All eight referenced images exist under `assets/images/careers-and-performance/`; captions match alt texts.
- Panel captions stay within one line each, appropriate to the form.
