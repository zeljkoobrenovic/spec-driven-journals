# Review: Building Great Platform Teams

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and the cleanest of its siblings. The "imbalance kills teams more than lack of talent" framing carries every modality, spec ↔ post alignment is complete, and the checklist's nineteen sections map back to the article's terminology with no drift. The most important thing to address is small: the "Interview for the actual work" bullet in the Statement is a five-clause fragment that asks too much of a first-pass reader.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Interview for the actual work" bullet]** One comma-chained fragment carries five distinct interview components (platform design, inverted design, coding, behavioral, empathy); it cannot be parsed in one pass. *Split into two sentences or a short sub-list, as the Rationale's interview paragraph already does more readably.*
- **[index.md · Statement vs. checklist §16]** The spec's criterion 5 includes "TPMs **and supporting roles** only when genuinely required", and checklist §16 covers developer advocates, technical writers, and support engineers — but the article's role enumeration ("reliability engineers, specialists, product managers, TPMs") never names the supporting roles; only the "disconnected evangelist" anti-pattern gestures at them. *One clause in the Statement's product-roles bullet ("— the same bar applies to advocates, writers, and support engineers") would close the gap.*

### Nits

- **[checklist.md · §7]** "Possible specialties include networking, kernels, performance, and storage" is a statement, not an actionable checkbox — it renders as a checkable item with nothing to do. *Fold it into the preceding item as a parenthetical.*
- **[index.md · excerpt vs. highlight]** Near-verbatim duplication — journal convention, noted only for completeness.
- **[comics.md · Panel 1 caption]** "one hiring profile is the bug" is compressed to the edge of readability for a reader who has not seen the article's "composition bug" phrasing. *E.g. "a single hiring profile is the failure mode."*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (mixed team, two failure modes, earned roles, empathy bar) |
| Composition guidance survives | met | index.md · Statement + Rationale + Figure 2; checklist.md §1–§3 |
| Role expectations survive | met | index.md · Statement (hiring bullets); checklist.md §4–§7 |
| Hiring and career machinery survives | met | index.md · Statement + Rationale (interviews, ladders, promotion evidence); checklist.md §8–§12 |
| Leadership and culture guidance survives | met | index.md · Statement (leadership bullets); checklist.md §13–§18 (supporting roles: checklist-heavy — see Minor) |
| Credit is explicit | met | index.md · Authoritative References; How to Read This |

Non-goals respected: yes — team formation stays with [[getting-started]], operational discipline with [[operating-platforms]], product operating mode with [[platform-as-a-product]]; no compensation/leveling policy content beyond how platform work is evaluated.
Drift: none. Spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — the two failure modes, equal reward for both kinds of work, need-gated roles, job-shaped interviews, and outcome-based promotion evidence appear identically everywhere they appear.
- **Terminology:** consistent — "too much systems" / "too much development", "inverted design interview", "customer empathy as a hiring bar" travel intact into checklist and comic; Panel 3 even reuses the article's "spends its customers' trust to entertain itself" verbatim.
- **Voice & tone:** consistent across all three modalities.
- **Coverage parity:** good — the comic compresses out the manager-hiring and culture-recognition beats (defensible at eight panels since the highlight carries neither as a headline claim); supporting roles are checklist-heavy as noted.

## Layer-by-layer notes

### Spec

- Template-complete; the Decision log usefully records the framing bet (imbalance as the primary failure cause) so a future editor knows what is load-bearing.
- Success criteria are enumerated tightly enough to walk one-by-one — the best-specified contract of the three sibling records reviewed.

### index.md

- House shape observed end to end; headings in Title Case; all five `[[…]]` cross-links resolve to existing permalinks; Figures 1–3 exist, are numbered and captioned, and alt text matches.
- The Rationale's paired-pathology structure ("glue that never becomes a platform" / "architecture nobody can operate") is the article's strongest asset and is mirrored in Figure 2 and comic Panels 2–3 — a model of cross-modality propagation.
- The What This Means in Practice table introduces "at most one systems-oriented addition" from checklist §8; supported, not drift.

### checklist.md

- Nineteen sections, imperative and runnable; §19's final health check is a faithful compression of the whole record and matches the article's "Concretely:" paragraph point for point.
- No internal contradictions found; the only non-actionable item is the §7 nit above.

### comics.md

- All eight referenced panel images exist in `assets/images/building-platform-teams/`; captions run Panel 1–8; alt text matches captions; cast stays VERA/KAI with the shared cast/style block.
- Panel arc (clones → two pathologies → mixed team → interviews → promotion → earned roles → empathy) tracks the article's argument order cleanly.

## Fixes applied (2026-08-13)

- index.md · "Interview for the actual work" bullet — fixed: split the five-clause fragment into two sentences (design interviews; then coding / behavioral / empathy).
- index.md · supporting roles gap vs. checklist §16 — fixed: product-roles bullet now extends the need bar to supporting roles (developer advocates, technical writers, support engineers).
- checklist.md · §7 non-actionable item — fixed: folded "Possible specialties include…" into the preceding hire-only-on-need item as a parenthetical.
- index.md · excerpt vs. highlight duplication — skipped: reviewer notes it as journal convention, flagged for completeness only; no change requested.
- comics.md · Panel 1 caption — fixed: reworded to "a single hiring profile is the failure mode."
