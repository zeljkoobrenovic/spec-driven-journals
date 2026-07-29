# Review: Business Collaboration

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a tight contract and the article satisfies all seven success criteria; the checklist reproduces the six PDF sections faithfully, and the comic carries the full arc with all eight panel images present. The single most important thing to address is a cross-modality framing wobble: the article and spec build the post around **four** trust-earning moves, while the comic numbers them as **three** deposits (folding "share context" and "evangelize" into one) — trivially fixed by recaptioning Panel 5 or dropping the ordinal numbering.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

- None.

### Major

- **[comics.md · Panels 4–6 captions]** The article's quotable core is a four-move formula (understand constraints, share context, evangelize, keep commitments — spec criterion 1), but the comic counts "First deposit / Second deposit / Third deposit," merging share-context and evangelize into one deposit. All four moves are present, yet a reader crossing tabs meets two different countings of the same formula. *Recaption Panel 5 (e.g. "Second and third deposits…") or drop the ordinals.*

### Minor

- **[index.md · Rationale, ¶4 "Executives change last, and matter most"]** The heading's "change last" claim is never argued in the paragraph — the body argues confidence must be built, not that executives are the last to change. *Either support the sequencing claim in a clause or soften the heading.*
- **[index.md · excerpt / highlight / Rationale ¶3]** The four-move list appears in full three times (front-matter excerpt, Principle highlight, and again in "The collaborative model has to be earned"). Excerpt-mirrors-highlight is house convention, but the third full recital in Rationale ¶3 could compress to gain variety. *Vary the phrasing or trim the third occurrence.*
- **[spec.md · Intent]** The second sentence is a ~90-word semicolon chain covering six distinct moves — hard to parse in one pass. *Break into two or three sentences.*

### Nits

- **[index.md · Rationale ¶1]** Tense wobble in the failure list: "the CEO **does not trust** the model, sales **made** commitments nobody scoped, or finance **sees** product as a cost center" — past tense among presents.
- **[checklist.md · Build Cross-Business Relationships]** "Identify the key stakeholders outside the product" — "outside the product" reads oddly; "outside the product organization" would be cleaner (verify against PDF wording before changing).
- **[index.md Figure 2 vs comics.md Panel 6]** The article's metaphor is a "trust ledger"; the comic shows a "trust-meter." Same idea, different prop — harmless, but one term would be tighter.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (four moves in one paragraph) | met | index.md · Principle highlight (uses "ticket-taking service"/"ivory tower" rather than the literal words "servitude"/"arrogance"; substance intact) |
| Necessary-but-not-sufficient survives | met | index.md · Statement bullet 1, Rationale ¶1; checklist.md · Understand the Context |
| Vocabulary point lands | met | index.md · Statement bullet 2, Rationale ¶2; checklist.md · nested sub-items |
| Both failure postures named | met | index.md · Anti-Patterns 1–2, Figure 1 |
| Transformation framing survives | met | index.md · Statement bullet 4, Rationale ¶4–5; checklist.md · Lead the Transformation |
| Checklist survives intact (six sections + nested sub-items) | met | checklist.md · six sections with the sensitivity-and-nuance sub-items (structure matches the spec's description; PDF not re-verified in this review) |
| Credit is explicit | met | index.md · Authoritative References (EMPOWERED + svpg.com essays) |

Non-goals respected: yes — RACI appears only inside an anti-pattern (which enforces the non-goal rather than breaching it); objectives-setting is deferred to [[team-objectives]]; the executive seat is deferred to the engineering journal; "partnership ≠ consensus" is explicit in the What This Means table.
Drift: none. Spec `status: accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent, with one exception — the four-moves vs three-deposits counting in the comic (the major finding above).
- **Terminology:** Consistent on the load-bearing terms (partnership of equals, ticket queue, empowered vs feature teams, "stakeholder management" retired). One small prop drift: trust *ledger* (article) vs trust-*meter* (comic).
- **Voice & tone:** Consistent — first-person declarative in the article, the same posture compressed into declarative captions in the comic; checklist is neutral imperative, appropriate to its form.
- **Coverage parity:** Even. The comic carries every load-bearing beat (both failure postures, the retirement of "stakeholder management," the deposits, executive mindset shift, transformation-as-ongoing in the closer). The checklist does not carry the trust-ledger/four-moves framing, but that is by design — the spec defines it as a faithful reproduction of the six PDF sections.

## Layer-by-layer notes

### Spec

- Follows the template fully; success criteria are genuinely checkable (each names a phrase or structure a reviewer can find in the post), and the decision log usefully records the swapped-source-PDF trap.
- Unchecked criteria checkboxes match the journal's convention (neighbor specs are identical), so not flagged.
- Only weakness is readability of the Intent's long semicolon-chained sentence.

### index.md

- Full house record shape (Status highlight → Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References), matching neighbors exactly. Headings are in Title Case; all three figures are captioned and their images exist; all five `[[cross-links]]` resolve (two cross-journal, three in-journal).
- Argument is well-supported; the deposit/withdrawal trust-ledger metaphor does real work and the What-it-says/does-not-say table is sharp (esp. "commitments are few and deliberate").
- Two soft spots: the unsupported "change last" heading claim and the triple recital of the four-move formula.

### checklist.md

- Achieves its purpose as an operational working checklist: six grouped sections of action bullets, nested sensitivity-and-nuance sub-items intact, italic pointer to the Article tab, `timetoread` front matter present.
- Bullets are imperative and scannable; nothing editorializes beyond the source structure — correct for a faithful PDF reproduction.

### comics.md

- Eight panels — a good count for the form; captions are one line each; every alt text matches its caption and image subject; all eight image files exist under `assets/images/business-collaboration/`.
- Cast and style block match the journal's shared VERA/MILA convention; the visual metaphor (tickets/wall → round table → deposits → gear) is consistent panel to panel with a clear hook–problem–principle–proof–closer arc.
- The only substantive issue is the deposit-numbering mismatch with the article (major finding).

## Fixes applied (2026-07-29)

- **[major · comics.md deposit numbering]** Fixed — Panel 5 recaptioned "Second and third deposits: share the context, evangelize the destination." and Panel 6 "Fourth deposit: rare commitments, always kept."; panel images verified first (no ordinal text baked into panels 4–6), so captions-only fix suffices.
- **[minor · index.md "Executives change last" heading]** Fixed — heading reworded to "Executive confidence has to be built, and it matters most.", matching the paragraph's actual argument (confidence built with results and transparency).
- **[minor · index.md third recital of four moves]** Fixed — Rationale ¶3 recital compressed to "They give it up when product demonstrably makes the four moves above — in practice, not on slides."
- **[minor · spec.md Intent semicolon chain]** Fixed — the ~90-word sentence split into four sentences (principle statement / necessary-but-not-sufficient / the three model moves / executives + transformation).
- **[nit · index.md Rationale ¶1 tense wobble]** Fixed — "sales made commitments" → "sales makes commitments", aligning with the surrounding present tense.
- **[nit · checklist.md "outside the product"]** Skipped — verified against the source PDF (`sources/empowered/Checklist_ PM _ Product Strategy.pdf`, the swapped file holding the Business Collaboration content): "Identify the key stakeholders outside the product." is verbatim, so left unchanged per the review's own condition.
- **[nit · trust ledger vs trust-meter]** Skipped — Panel 6's image visibly shows a gauge labeled "TRUST METER", so the alt text's "trust-meter" describes the actual prop; changing it to "trust ledger" would contradict the image (no regeneration in scope). Panel 6's caption mentions neither term.

Spec `revised:` bumped to 2026-07-29 with a Changelog entry.
