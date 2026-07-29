# Review: Balanced Roadmap

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready-minus-one post. The spec is a tight contract, the article argues allocation-before-ranking cleanly in the house voice, the checklist reproduces all nine source sections faithfully, and the comic has a coherent eight-panel arc with every image present on disk. The single most important thing to address is the Panel 5 comic image: its allocation bar is labeled **GROWTH / MAINTAIN / EXPLORE** instead of innovation / iteration / operation — the load-bearing panel of the comic visibly contradicts the terminology every other modality (and Panel 4 of the same comic) establishes. Regenerate that panel; the rest is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 3

### Blockers

- None. All three figure images and all eight panel images exist under `assets/images/balanced-roadmap/`, and all three `[[…]]` cross-links (`outcomes`, `product-strategy`, `planning`) resolve.

### Major

- **[comics.md · Panel 5 image (`comic-05-set-the-allocation.jpeg`)]** The rendered allocation bar's three segments are labeled "GROWTH", "MAINTAIN", "EXPLORE" (and one ranked list below reads "EXPLORES"), contradicting the innovation / iteration / operation categories established in Panel 4, the article, and the checklist. The caption and alt text are fine; the image is not. *Regenerate the panel with the correct three category labels (or unlabeled segments).*

### Minor

- **[index.md / checklist.md / comics.md · throughout]** The third category wobbles between singular and plural: "operation" (Statement, checklist headings) vs "operations" (excerpt "operations from being eaten", Rationale "no iteration or operations", checklist bullet "innovation, iteration, and operations", comic Panel 3 caption). *Pick one form — the Statement's singular "operation" — and align.*
- **[index.md · Statement, lifecycle bullet]** The article compresses the checklist's five lifecycle stages to four, silently dropping the post-alpha/launch stage ("further iteration to address early feedback"). The spec criterion "each stage with its allocation lean" is therefore only fully met via the Checklist tab. *Either add the missing stage or accept the compression knowingly.*
- **[index.md · Rationale, "Each category needs its own prioritization method"]** The paragraph is three very long sentences; the operation sentence (~60 words) carries two embedded lists (capacity coverage and bug-policy types) and is hard to parse in one pass. *Split the operation sentence in two.*
- **[index.md · Rationale para 2 + Scope and Revisiting]** "I revisit the split quarterly or when the business context changes" appears nearly verbatim in both places. *Keep it in Scope and Revisiting; trim the Rationale mention.*

### Nits

- **[checklist.md · "Pick an Allocation Based on Product Lifecycle"]** Slash spacing is inconsistent: "Pre-alpha / idea" and "Beta / approaching product-market fit" vs "Post-alpha/launch".
- **[checklist.md · "Classify Every Roadmap Item"]** "add value for customers or businesses" — the article says "customers or the business"; "businesses" reads as a typo unless it is verbatim from the PDF.
- **[spec.md · Changelog]** The latest entry still describes the comic as staged "with pending panel blocks" and the article with "inline illustration placeholders staged"; both are now final generated images, with no changelog line recording the generation step. Cosmetic staleness, not drift.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight (one paragraph, states allocate-before-rank) |
| Three categories explicit, each with its method | met | index.md · Statement bullets 2 and 5; Rationale "Each category needs its own prioritization method" |
| Allocation-before-ranking is argued | met | index.md · Rationale paras 1–2 (rigged ranking of unlike work; allocation as the real decision) |
| Lifecycle tuning survives | partial in index, met overall | index.md Statement covers 4 of 5 stages; checklist.md "Pick an Allocation Based on Product Lifecycle" covers all 5 |
| Both failure modes appear | met | index.md · Rationale para 3 + Figure 2; comics.md Panels 1–3 |
| Checklist survives intact (nine sections) | met | checklist.md · nine H2 sections matching the PDF outline |
| Credit is explicit | met | index.md · Authoritative References (Foster & Nerlikar, *Build What Matters*) |

Non-goals respected: yes — no template/tool recommendation; boundaries with [[product-strategy]], [[outcomes]], and [[planning]] are stated explicitly in How to Read This and Related Records; the 40/40/20 figure in the Rationale is clearly hedged as an example ("say,"), so no universal-percentage claim.

Drift: none. Spec `status: accepted` remains correct; only the Changelog is cosmetically stale (see nit).

## Cross-modality alignment

- **Facts & framing:** Consistent — same three categories, same per-category methods (milestone-driven / RICE-reviewed / reserved capacity + bug policy), same intake-process framing, same two failure modes in article and comic.
- **Terminology:** Mostly consistent; the singular/plural "operation(s)" wobble (minor above) and the Panel 5 image's foreign labels (major above) are the two exceptions.
- **Voice & tone:** Consistent — first-person declarative in the article, neutral imperative in the checklist, and the comic keeps VERA as the principle-carrier and MILA as the learner, matching the journal's cast convention.
- **Coverage parity:** Even. Every load-bearing article beat (both failure modes, classification, allocation-first, stakeholder intake, vision payoff) appears compressed in the comic; the checklist carries the full nine-section source. The comic's closer line "the allocation is the strategy, made visible" is a light new framing the article never uses, but it is a fair compression of the Rationale, not a new claim.
- **Stale propagation:** No signs — figures, checklist, and comic all reflect the current article.

## Layer-by-layer notes

### Spec

- Follows the template fully; all eight sections plus Changelog present. Success criteria are genuinely checkable (quotable highlight, three categories, nine sections, explicit credit) — no Intent-prose-with-a-checkbox.
- Non-goals do real fencing work, naming the three adjacent records and the no-universal-percentage rule; the article honors all of them.
- Decision log captures the load-bearing framing choice ("allocate before you rank" as the spine). Only weakness: the Changelog stopped one step short of the finished visuals.

### index.md

- House record shape is correct and complete: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice (says / does-not-say table) → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References. Headings are in proper Title Case.
- The Rationale is the strongest section — "the allocation is the real decision; the ranking is bookkeeping" and "both failure modes are allocation failures" are crisp, quotable claims that each get an actual argument.
- Three figures are present, captioned, numbered, and resolve; the says/does-not-say table and the seven anti-patterns are well matched to the argument with no orphans.
- Main prose weaknesses: the overloaded per-category-methods paragraph and the quarterly-revisit repetition (minor findings above).

### checklist.md

- Judged as an operational working checklist, it does its job: nine grouped sections, every bullet an actionable check, bold category/stage names as scan anchors, and a correct one-line pointer to the Article tab for rationale.
- The final section ("Review Before Finalizing the Roadmap") is properly phrased as review questions rather than actions — a good fit for its gate-keeping purpose.
- Only cosmetic issues: slash spacing and the "businesses" wording (nits above).

### comics.md

- Sound eight-panel arc: hook (all-reactive board) → problem (vision never scheduled) → mirror failure (ivory tower) → principle (classify) → mechanism (allocate first) → defense (intake) → payoff (milestones toward vision) → closer. Captions are short, match their alt text, and the VERA/MILA cast block is present and consistent.
- All eight referenced panel images exist on disk; spot-checks show Panels 1, 4, and 8 match their captions and speech bubbles are on-message.
- Panel 5 is the one real problem: the image's segment labels contradict the post's category names (major above).

## Fixes applied (2026-07-29)

- **[major · Panel 5 image]** Fixed — regenerated `comic-05-set-the-allocation.jpeg` via the explainer-comics generator (gemini-3-pro-image-preview); the allocation bar now reads INNOVATION / ITERATION / OPERATION, verified visually on the first attempt; same filename, VERA/MILA cast and style consistent with neighboring panels.
- **[minor · operation/operations wobble]** Fixed — normalized to singular "operation" for the category name in index.md (excerpt, Rationale ivory-tower sentence, says/does-not-say table row, two anti-patterns) and comics.md (Panel 3 caption); checklist.md line "innovation, iteration, and operations" left as-is after verifying it is verbatim from the source PDF.
- **[minor · missing lifecycle stage]** Fixed — Statement lifecycle bullet now carries all five stages, adding the post-alpha/launch stage ("a freshly launched product iterates further to address early feedback").
- **[minor · overloaded operation sentence]** Fixed — split the ~60-word Rationale sentence into two (capacity coverage sentence + bug-policy sentence).
- **[minor · quarterly-revisit repetition]** Fixed — removed the "I revisit the split quarterly..." sentence from Rationale para 2; kept the mention in Scope and Revisiting.
- **[nit · checklist slash spacing]** Fixed — "Post-alpha/launch" normalized to "Post-alpha / launch" (formatting only; wording unchanged).
- **[nit · "customers or businesses"]** Skipped — verified verbatim against the source PDF ("add value for customers or businesses"); checklist wording preserved.
- **[nit · stale spec Changelog]** Fixed — added a 2026-07-29 Changelog entry recording final figures/panels and the Panel 5 regeneration; bumped `revised:` to 2026-07-29.
