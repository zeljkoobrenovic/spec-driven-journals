# Review: Policy as Code Implementation

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A clean, publish-ready record. The spec is a tight contract with source-mapped criteria, and every criterion is met — the "one policy source, three gates" framing carries consistently through all five modalities. The checklist is a faithful, item-by-item reproduction of the source's 11 sections plus Final Validation, with no invented obligations. All 12 referenced images (3 figures, 9 panels) exist and match their captions; all 7 `[[cross-links]]` resolve. The most important thing to address is small: the word "documental" in the practice section, and a mildly noisy generated image in comic panel 4.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

None.

### Major

None.

### Minor

- **[index.md · What This Means in Practice, closing paragraph]** "The proof is operational, not documental" — "documental" is a non-standard word that lands oddly in an otherwise plain-spoken record. *Suggest "not documentary" or "not on paper."*
- **[index.md · Rationale ¶2 + Anti-Patterns "The split brain"]** The vivid phrase "green pipelines and red deployments" appears twice in the same article ("developers get green pipelines and red deployments" in Rationale; "Green pipelines, red deployments" in the anti-pattern). One of the two tellings should own it. *Vary the anti-pattern's wording or trim the Rationale echo.*
- **[comics.md · Panel 4 image]** The generated image renders the three gate labels (DESK / PULL REQUEST / ADMISSION) twice — once above and once below the gates — an image-generation artifact that adds visual noise. The lower row's "SAME EVALUATION" brace carries the point, so it still reads, but a regeneration would be cleaner. *Regenerate with a single label row if the panel is revisited.*

### Nits

- **[index.md · Figures 2 and 3]** A double blank line after each caption before the next heading — cosmetic only, no render effect.
- **[comics.md · Panel 2 caption/alt]** "at 5 PM on Friday" is a dramatization the article does not use (the article says "an interrupted afternoon"). Harmless color, noted for completeness.
- **[index.md · How to Read This]** The tab enumeration names Checklist, TL;DR, and Conversation but not the Comic tab. This matches the whole journal (no article in `grounded-platforms` mentions the Comic tab), so it is a journal-level convention question, not a post defect.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (one source/three gates, floor, progressive, visible, closing test) | met | index.md · highlight blockquote |
| Admission setup survives (§1, §3) | met | checklist.md §1, §3; index.md · Statement gate 3 |
| Core policy floor survives (§2) | met | checklist.md §2; index.md · Statement "A core policy floor" |
| Progressive enforcement survives (§4) | met | checklist.md §4; index.md · Statement + Rationale |
| Shift-left survives (§5–§6) | met | checklist.md §5–§6; index.md · Statement gates 1–2 |
| Compliance visibility survives (§7–§8, §11) | met | checklist.md §7, §8, §11; index.md · "Compliance made visible" |
| Governance integration survives (§9) | met | checklist.md §9; index.md · "Policy in the wider governance map" |
| Demo exercise and final validation survive | met | checklist.md §10, §12; index.md · practice paragraph states the bar as definition of done |
| Tools are the worked example, not the mandate | met | index.md · reference-stack table in How to Read This; capability-level commitments throughout |
| Credit is explicit | met | index.md · Authoritative References; summary.md closer; spec Sources |

Non-goals respected: yes — the article defers identity/network/secrets/supply chain to [[platform-security]], pipeline architecture to [[cicd-as-a-platform-service]], the metrics stack to [[observability-implementation]], and the cluster baseline to [[platform-creation]]; no Rego tutorial content appears, and every modality names the stack as reference, not mandate.
Drift: none. Spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. The floor's contents (requests/limits, no root, no privileged, read-only FS where appropriate, capabilities like `SYS_ADMIN`, approved registries, human-readable messages) are identical across index, checklist, summary, and dialog. The dashboard panel list (totals, by constraint, by namespace, compliance rate, remediation trend) matches everywhere.
- **Terminology:** Consistent. "One policy source, three gates," "backstop," "audit before enforce," "tollbooth, not a guardrail," and the anti-pattern names (compliance PDF, big-bang deny, split brain, eternal audit, permanent exemption, Kubernetes hammer) are reused verbatim by dialog and comics. Small harmless inversion: summary and dialog section-head it as "Three Gates, One Source."
- **Voice & tone:** Consistent first-person declarative in index/summary; Ana/Ben split matches the journal's register (Ben presses with lived failure modes, Ana carries the record); comic captions stay in the house voice.
- **Coverage parity:** Even. Every load-bearing beat of the index (three gates, floor, message-as-UI, progressive enforcement, exemption review, visibility, governance map, ownership, closing test) appears in summary, dialog, and comics at appropriate compression. No modality introduces a beat the spec lacks.
- **Stale propagation:** None found — the comics addition (per spec changelog) is reflected in the spec's Modalities section and the panels track the article's argument order.

## Layer-by-layer notes

### Spec

- Strong contract: ten success criteria, each checkable and mapped to specific source checklist sections — easy to audit, and the audit passes.
- Decision log genuinely records rejected alternatives (tool-first framing, binary enforcement), not just choices.
- Non-goals double as boundary declarations against four sibling records, all of which the article honors.

### index.md

- House record shape fully present and headings correctly Title Cased; the Statement's five-bullet "one source, three gates" block is the strongest section — the whole record hangs off it cleanly.
- Rationale earns each commitment: cost-of-feedback gradient for the gates, message-as-user-interface for remediation text, audit-as-phase (with the enforce-or-retire exit) for progressive enforcement. The "cuts both ways" caveat on audit mode is a good example of the record arguing against its own failure mode.
- Anti-Patterns list (nine, all named) is vivid and maps one-to-one onto the Rationale — at the cost of the one "green pipelines, red deployments" doublet flagged above.
- Scope and Revisiting gives four concrete, observable revisit triggers — better than the generic "revisit annually" pattern.
- All three figures exist, match their alt text and captions, and illustrate real structure (gates, lifecycle loop, governance layers) rather than decoration.

### checklist.md

- Verified line-by-line against the extracted source text: all 11 sections plus Final Validation reproduced completely and in order; no items dropped, no obligations invented. Wording adaptations are trivial ("Add clear, human-readable violation messages **to every policy**" strengthens in the article's direction).
- Framing intro and the closing bolded test ("same policy source… tells its developer what to change") tie the checklist back to the article's principle — good glue.
- Runnable as-is: items are imperative, single-action, and ordered install → policies → constraints → enforcement → shift-left → CI/CD → monitoring → dashboard → governance → demo → validation.

### summary.md

- On target: ~450 words, leads with the decision, and the What changes / What it costs / What we are not doing structure gives a leader the commitment, the price, and the boundaries without the mechanics.
- The costs section is honest (owned lifecycle, deliberate slowness, review-cadence obligation) rather than a sales pitch — matches the journal's register.

### dialog.md

- Ben's objections are real practitioner objections (rotting split-brain CI, the Tuesday enforce-flip, audit-mode parking lot, dashboard-as-shame-leaderboard) — each sets up a beat the record actually answers, so the dialog never becomes a lecture.
- Ana's closing "done is both: blocked at admission, and explained in a sentence a developer can fix before lunch" is a strong compression of the final-validation bar.
- Ana's opening turn is dense (four claims plus a cross-link in one breath) but within the journal's register.

### comics.md

- Nine panels, correct arc (hook → problem → wrong way → principle → mechanism → cost → closer); every referenced image exists under `assets/images/policy-as-code/`; captions match alt text and (spot-checked panels 4 and 9) the rendered images.
- Cast block matches the journal's VERA/KAI convention; visual metaphor (gates, floorboards, the anthropomorphic policy scroll asked to explain itself) stays consistent panel to panel.
- Panel 4's duplicated label row is the only visual defect (minor, above).

## Fixes applied (2026-08-20)

- **[minor · index.md]** "not documental" → "not on paper" in the closing practice paragraph.
- **[minor · index.md]** "green pipelines and red deployments" doublet resolved: Rationale ¶2 rephrased to "pipelines that pass and deployments that bounce"; the anti-pattern "The split brain" now owns the phrase.
- **[minor · comics.md]** Panel 4 regenerated (one attempt, clean on first try) with a prompt constraining the diagram to a single label row (POLICY + DESK / PR / ADMISSION, each exactly once) and the speech bubble as the only other text. New asset `comic-04-one-source-three-gates-v2.jpeg`; figure line and alt text updated; old jpeg removed from post assets and `docs/`.
- **[nit · index.md]** Double blank lines after Figure 2 and Figure 3 captions collapsed to single.
- **[nit · comics.md]** Panel 2 "at 5 PM on Friday" — skipped: review marks it harmless color, and the rendered image depicts the Friday-evening bounce, so trimming the caption would create a caption↔image mismatch.
- **[nit · index.md]** How to Read This not naming the Comic tab — skipped: journal-wide convention, decided by orchestrator.
