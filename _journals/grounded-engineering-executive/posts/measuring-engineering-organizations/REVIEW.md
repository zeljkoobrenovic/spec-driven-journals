# Review: Measuring Engineering Organizations

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The audience-shaped framing is carried cleanly through all three modalities, the spec's success criteria are all met, every image reference (three figures, eight comic panels) resolves, and all four cross-links point at real posts. The only things worth touching are small: a stale sentence in the spec's Modalities section and a little compression in the fourth Rationale paragraph.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[spec.md · Modalities]** The prose sentence "Summary/dialog/comics may be added later per journal policy" is stale — comics has shipped (checkbox `[x]`, Changelog 2026-07-26 confirms). *Reword to cover only summary/dialog.*
- **[index.md · Rationale, ¶4 "Trust in data…"]** The paragraph carries three beats (data-confidence loop, metrics-can't-replace-trust, don't-wait-for-perfect-data); the last two are restated nearly verbatim in Anti-Patterns ("Metrics as a substitute for trust", "Waiting for perfect data"). *Trim the paragraph's last two sentences or let Anti-Patterns carry them alone.*

### Nits
- **[index.md · Figure 3]** Alt text says "Five-step circular loop" while the adjacent paragraph enumerates roughly seven practices — alt/caption and prose are slightly out of sync.
- **[comics.md · Panel 6 caption]** "measure what feeds decisions, start easy to build trust, one initiative at a time" compresses three sequencing rules into one caption — fine for the form, but the panel image (stepping stones) only depicts the third; caption slightly outruns the visual.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Rationale is argued, not asserted | met | index.md · Rationale (audience/metric, optimization vs impact, teams not individuals — each argued) |
| The checklist survives intact | met | checklist.md — all six source sections present (yourself: plan/operate/optimize/inspire; stakeholders: CEO-board/Finance/strategic/tactical; sequencing; antipatterns; data confidence; ongoing mindset) |
| Anti-patterns are concrete (≥3) | met | index.md · Anti-Patterns (six, including all three examples the spec names) |
| Credit is explicit | met | index.md · Authoritative References (Primer + lethain.com essay) |

Non-goals respected: yes — no planning-cycle mechanics (deferred to [[planning]]), no individual-inspection territory (deferred to [[inspected-trust]]), no tooling/vendor prescriptions.
Drift: none. Spec `status: accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — the four audiences, the optimization-vs-impact boundary, teams-not-individuals, and the sequencing rules appear identically in article, checklist, and comic.
- **Terminology:** Consistent — "optimization theater," "the audience determines the metric," and "measuring something imperfect beats measuring nothing" recur verbatim across modalities.
- **Voice & tone:** Consistent first-person operating-principle register; the comic's VERA/LEO frame matches the journal's house cast.
- **Coverage parity:** Even. Every index beat has a checklist group and a comic panel; the comic's eight panels map cleanly onto hook → problem → wrong way → principle → line held → sequencing → data trust → closer.

## Layer-by-layer notes

### Spec
- Well-formed contract: all template sections present, criteria genuinely checkable (each names a verifiable artifact), decision log explains the audience-first framing choice.
- One stale prose line in Modalities (see Minor finding); checkboxes and Changelog are already correct.

### index.md
- Clean house shape: Status/Principle highlight, Statement → How to Read This → Rationale → contrast table → Anti-Patterns → Related Records → Scope → References. Headings in Title Case.
- Rationale argues rather than asserts; the "reuse is an efficiency, not an excuse" line does good work distinguishing the principle from siloed dashboards.
- Slight redundancy between Rationale ¶4 and the first two Anti-Patterns (see Minor finding).
- All three figures exist on disk and are captioned and numbered.

### checklist.md
- Serves its purpose as an operational working checklist: audience-first grouping mirrors the spec's required PDF structure exactly; items are imperative, checkable actions.
- The italic preamble correctly routes readers to the Article tab for rationale — good separation of duties between tabs.

### comics.md
- Eight panels, all image files present under `assets/images/measuring-engineering-organizations/`. Captions match alt text; visual metaphor (Vera correcting Leo's dashboard instincts) is consistent panel to panel.
- Caption lengths fit the form; the arc lands the article's closer ("imperfect beats nothing") as the final panel.
