# Review: Platform as a Product

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready, with the journal's sharpest through-line: "mandatory usage is not product success" is stated in the spec, quoted in the highlight, argued in the Rationale, operationalized in checklist §2, and drawn as comic Panels 1–2. The most important thing to address: two beats the spec's criterion 4 explicitly names — outcome-defined features and internal marketing — exist only in the checklist, with no echo in the article; a reader of the Article tab would not know the record commits to either.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Measure and staff it honestly"]** The spec's criterion 4 names "outcome-defined features" and "internal marketing" among what must survive, but the article carries neither — they live only in checklist §12 and §13. The criterion is met across modalities, yet the article claims to be the distillation and silently drops two named commitments. *One clause each in the Statement (features defined by outcomes; the platform marketed internally) — or trim them from the spec criterion.*
- **[checklist.md · §11 "Create a Product Roadmap" vs. spec Non-goals]** The spec fences off roadmap *mechanics* to [[planning-and-delivery]] ("the roadmap appears here as a product artifact; the planning mechanics live there"), but §11 walks the full mechanics ladder — vision → obstacles → strategy → annual goals → quarterly milestones. Justified as source-chapter reproduction, but it sits in tension with the stated non-goal. *Acknowledge the overlap in the spec (e.g. "checklist §11 reproduces the chapter's roadmap steps; the planning discipline itself lives in planning-and-delivery").*
- **[index.md · "final pre-investment review" naming]** The article twice sends readers to "the final pre-investment review in the Checklist tab", but the checklist's heading is just "Final Review". Small findability gap in the record's most operational hand-off. *Rename the checklist heading "Final Pre-Investment Review" or match the article's wording to the heading.*

### Nits

- **[index.md · highlight]** "Adoption and migration are part of the product strategy from the beginning, impact metrics rather than activity metrics guide it, …" — the antecedent of "it" is loose (the strategy? the platform?). *E.g. "guide that strategy".*
- **[spec.md · Sources]** The internal PDF path wraps mid-filename ("Checklist_ PE _ Platform as a\n Product.pdf"), so the path cannot be copy-pasted as written — the Layer-1 "broken line-wrap" case. *Keep the filename on one line.*
- **[comics.md · Panel 5 caption]** "enthusiasm in a meeting counts for nothing" overstates the article's calibrated claim (enthusiasm is not *validation*; it is not worthless). Within comic register, but the strongest wording divergence in the set. *E.g. "counts as nothing — only committed time, effort, or budget does."*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (customers, mandatory usage, adoption/migration/impact as product work) |
| Customer-culture side survives | met | index.md · Statement "Know the customer" + Rationale; checklist.md §1–§2 |
| Product-discipline side survives | met | index.md · Statement "Practice product discipline" + Rationale + Figure 2; checklist.md §3–§6 |
| Adoption-and-measurement side survives | partial (met only across modalities) | index.md · Statement + Rationale + Figure 3; checklist.md §7–§15 — outcome-defined features (§12) and internal marketing (§13) have no article presence (see Minor) |
| Credit is explicit | met | index.md · Authoritative References; How to Read This |

Non-goals respected: mostly — one tension: checklist §11 edges into the roadmap/planning mechanics the spec assigns to [[planning-and-delivery]] (see Minor). No breaches of the four-pillars, operating-platforms, or tooling/vendor fences.
Drift: none substantive; spec `accepted` holds once the §11 overlap and the criterion-4 article gap are acknowledged.

## Cross-modality alignment

- **Facts & framing:** consistent — captive audience as risk, feature shop, real commitments over enthusiasm, change budget, impact vs. activity metrics, and reliability-as-trust appear with the same meaning everywhere; comic Panel 8 quotes the highlight's closing "failing slowly" bar.
- **Terminology:** consistent — "feature shop", "change budget", "impact / guardrail / product health", "captive audience" travel intact across all three modalities; the only naming mismatch is the Final Review heading noted above.
- **Voice & tone:** consistent; Panel 5's "counts for nothing" is the one register overstep (nit).
- **Coverage parity:** article is thinner than the checklist on outcome-defined features, internal marketing, and roadmap creation (all checklist-carried); the comic covers the highlight's full arc — captivity, shadow platform, feature shop, observation, validation, change budget, impact metrics, choice — with no invented beats.

## Layer-by-layer notes

### Spec

- Template-complete; the Decision log's framing note ("internal customers are captive, which makes product discipline harder, not optional") is exactly the load-bearing claim the modalities execute.
- Criterion 4 is the longest and most compound of the four — eight sub-items in one checkbox — which is where the partial slippage above hid. Splitting it would make future walks easier.

### index.md

- House shape observed; headings in Title Case; all five `[[…]]` cross-links resolve to existing permalinks; Figures 1–3 exist, are numbered and captioned, and alt text matches.
- The Rationale's opening paragraph (dashboards fine for years, then a competitor "built in anger") is the record's best argumentation — claim, mechanism, and observable alarm in four sentences.
- The What This Means in Practice table's says / does-not-say pairs are well calibrated, especially row 2's concession that mandates can be legitimate without being evidence.

### checklist.md

- Faithful and runnable; the Final Review's fourteen confirmations compress the whole record and align point-for-point with the article's "Concretely:" paragraph.
- Style diverges slightly from sibling checklists (Title Case section headings, terminal periods on items) — internally consistent, so noted here only as a journal-level observation, not a per-post finding.

### comics.md

- All eight referenced panel images exist in `assets/images/platform-as-a-product/`; captions run Panel 1–8; alt text matches captions and imagery; cast stays VERA/KAI with the shared cast/style block.
- The choice-vs-captivity metaphor is coherent from Panel 1's "ONLY OPTION" gate to Panel 8's freely chosen doorway — the strongest visual bookending of the three sibling comics reviewed.

## Fixes applied (2026-08-13)

- index.md · criterion-4 gaps (outcome-defined features, internal marketing) — fixed: Statement now carries both — internal marketing appended to the change-budget bullet, outcome-defined features appended to the product/engineering bullet.
- checklist.md · §11 vs. spec Non-goals — fixed: spec Non-goals now acknowledges the known overlap (checklist §11 reproduces the chapter's roadmap-creation steps; planning discipline stays with planning-and-delivery).
- index.md / checklist.md · "final pre-investment review" naming — fixed: checklist heading renamed "Final Pre-Investment Review"; the article's one loose "final review" mention aligned to the same phrase.
- index.md · highlight antecedent nit — fixed: "guide it" → "guide that strategy".
- spec.md · Sources line wrap — fixed: PDF filename now on one line.
- comics.md · Panel 5 caption — fixed: "counts for nothing" → "enthusiasm in a meeting is not validation" (calibrated to the article's claim; the reviewer's suggested tail would have duplicated the caption's existing "time, effort, or budget" clause).
