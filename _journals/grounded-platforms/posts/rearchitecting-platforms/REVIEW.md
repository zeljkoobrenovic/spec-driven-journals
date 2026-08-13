# Review: Rearchitecting Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

The strongest argument of the three sibling records reviewed this pass — "rearchitectures fail organizationally more often than technically" is set up and paid off cleanly, and the checklist is a genuinely runnable gate sequence ending in a proper go/no-go review. All spec criteria are met. Not quite publish-clean: Panel 4 of the comic names Vera and Kai but the rendered image shows both characters off-model, which breaks the journal's cast consistency and should be regenerated before publishing.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 1

### Blockers

- None.

### Major

- **[comics.md · Panel 4 image (comic-04-gate-it-like-an-investment.jpeg)]** The alt text names Vera and Kai, but the image is off-model for both: the woman has long dark-blue hair, a white blouse, and a skirt (the cast defines Vera as short gray-streaked hair, dark blazer over a t-shirt, black notebook), and Kai wears a teal jacket instead of his gray zip-up hoodie. Every other cast panel checked (operating/planning Panels 4 and 9, and this post's Panel 9) is on-model, so this panel visibly breaks the strip's character continuity at its most important beat — the principle panel. *Regenerate the panel with the cast description enforced.*

### Minor

- **[index.md · Statement, opening line]** "My operating model … has four gates" — but the four gates are never enumerated, and the section that follows has three groups ("Before the work starts" with four bullets, "How the target is set," "How the work stays honest"). If the gates are the first group's four bullets, the go/no-go review is itself one of them (a gate containing gates); if they are constraint → go/no-go → 12-month wins → annual review, the text never says so. *Name the four gates explicitly or rephrase the count.*
- **[checklist.md · §1 heading]** "Confirm a Re-architecture Is Actually Needed" hyphenates "Re-architecture" while the article, spec, and the rest of the checklist (including items inside §1) consistently write "rearchitecture." *Unify the spelling.*
- **[index.md · What This Means in Practice, leadership row]** The right-hand cell carries two ideas at once: "Approval in one budget meeting is commitment — protection is the test, and waiting is acceptable if the case is not yet strong." The waiting clause is something the record *does* say (checklist §11: "Be willing to wait…"), sitting awkwardly in the "does not say" column. *Split the waiting point out or move it to the left column's framing.*

### Nits

- **[index.md · Rationale ¶3]** "A rearchitecture costed only by the building team's headcount is **off by the larger half**" — evocative but imprecise on first read (off by more than half? missing the larger half?). The table's "the larger half is usually paid elsewhere" is clearer; consider aligning the Rationale phrasing with it.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (investment, constraint, 12-month wins, honest costs, stop-when-evidence-turns) |
| The go/no-go discipline survives | met | index.md · Statement "Before the work starts" (constraint, incremental over "v2", scrappy/scalable/robust + pioneer/settler/town planner, go/no-go review); checklist.md §§1, 13 |
| The delivery discipline survives | met | index.md · Statement "How the work stays honest" + Rationale ¶2; guardrails bullet; checklist.md §§2, 7, 9 |
| The cost and people side survives | met | index.md · Rationale ¶¶1, 3, 6 (migration accounting, org support, staffing/historical context, pioneer without shadow platforms); checklist.md §§8, 10–12 |
| Security-by-design survives | met | index.md · Statement "Security by design and by default" + Rationale ¶5; checklist.md §§5–6 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — milestone/migration discipline explicitly inherited from [[planning-and-delivery]] rather than restated; OSS/vendor content stays at the evaluation-criteria level (no technology picks); scope stays on platforms, not application rewrites.
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — 3–5-year horizon, 12-month production wins, three levels of success (audacious / valuable fallback / production proof), migration as the larger cost paid by consumer teams, annual stop/revise/delay review agree across article, checklist, and comic.
- **Terminology:** Consistent — "v2," "big bang," "shadow platform," "paved paths," "go/no-go," "production proof" travel intact; the only wobble is the checklist heading's "Re-architecture" (minor above).
- **Voice & tone:** Consistent first-person investment-discipline register; the comic's closer ("Would we start it today?") is the article's "Concretely" question verbatim in spirit.
- **Coverage parity:** Even. The comic carries constraint, graveyard, v2 island, gate, incremental, 12-month wins, migration bill, security-by-default, annual review; maturity/mindset (scrappy/settler/town planner) lives only in Statement + checklist §1, which fits its weight.

## Layer-by-layer notes

### Spec

- The most detailed spec of the three sibling records (six criteria), and each is checkable; the Decision log's "fails organizationally, not technically" framing note is exactly what the article delivers.
- Non-goals cleanly delegate the shared planning discipline to [[planning-and-delivery]] instead of duplicating it.

### index.md

- The Rationale sequence is tight: each paragraph owns one gate-side idea (organizational failure, 12-month survival mechanism, migration honesty, incremental over v2, security-as-structure, people-as-asset) with no beat repeated.
- The Anti-Patterns are memorably named (resume-driven rewrite, v2 island, zombie project) and each traces to a body claim.
- All five `[[…]]` cross-links resolve; all three figures exist on disk, captioned Figure 1–3, matching their alt text.
- The "four gates" count is the only structural blemish (minor above).

### checklist.md

- Reads as an actual gate sequence: need (§1) → goals (§§2–4) → security (§§5–6) → guardrails (§7) → costs (§8) → wins (§9) → people (§§10–12) → go/no-go (§13) → ongoing review (§14). The §13 question-form review is a strong closer before §14.
- Security sections (§5–6) carry the chapter's detail (secure-by-default capability list, paved-path prompts) that the article rightly compresses.

### comics.md

- All nine referenced panel images exist on disk; captions run Panel 1–9 and match their alt text; the arc mirrors the article (hook → graveyard → v2 island → gate → incremental → three levels → migration bill → paved path → annual question).
- Panel 9 is on-model for both cast members; Panel 4 is off-model for both (major finding above).

## Fixes applied (2026-08-13)

- comics.md · Panel 4 image (major) — fixed: panel regenerated with the cast restated explicitly in the prompt (Vera: short gray-streaked hair, dark blazer, black notebook; Kai: gray zip-up hoodie with gear pin, sticker-covered laptop, cable coil); both characters are now on-model.
- index.md · Statement, opening line — fixed: the four gates are now named explicitly ("a genuine constraint, a full go/no-go review before the work starts, a valuable production deliverable every 12 months, and an annual review with a stop option").
- checklist.md · §1 heading — fixed: "Confirm a Rearchitecture Is Actually Needed" (spelling unified with the rest of the record).
- index.md · What This Means in Practice, leadership row — fixed: the waiting clause moved to the left column ("— and be willing to wait if the case is not yet strong"); the right column now carries only the does-not-say framing.
- index.md · Rationale ¶3 — fixed: "off by the larger half" rephrased to "missing the larger half of the bill", aligned with the table's phrasing.
