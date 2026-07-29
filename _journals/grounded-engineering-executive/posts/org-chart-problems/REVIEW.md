# Review: The Problem with Org Charts

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and argumentatively one of the sharpest records in the appendix: the three-structures model is genuinely load-bearing, "decisions decay as they climb" and "reorgs are surgery, not spring cleaning" carry the executive stance well, and all seven spec success criteria are met. All eleven images resolve and all five cross-links point at real posts. The main note is a Statement/Rationale asymmetry: cognitive load is a full Rationale beat and checklist section but is missing from the Statement's five parts.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement vs Rationale]** The Statement promises "five parts," but the Rationale develops six bolded beats — cognitive load ("the sizing constraint the chart cannot see") is a full paragraph and a full checklist section, yet absent from the Statement's list. A skim reader gets an incomplete model from the section meant to state it. *Either add a sixth bullet or fold cognitive load into the "Design for the flow of change" bullet explicitly.*
- **[spec.md · Changelog, 2026-07-26 top entry]** The latest entry says comics was "staged … with pending panel blocks" and illustrations were "placeholders staged" — both are now complete (all images exist on disk), with no completion entry, so the spec's history ends on a pending state. *Add a completion line.*

### Nits
- **[index.md · excerpt vs highlight]** The excerpt leads with "filing system" (matching the spec Intent and the comic's closer) while the highlight blockquote says "snapshot drawn for reporting and compliance" — content-equivalent, but the journal's convention is near-identical excerpt/highlight wording, and "filing system" is the phrase the other modalities key on.
- **[checklist.md · headings]** Sections use `##` where the Primer-grounded checklists use `###` (consistent with the other appendix record, inconsistent with the rest of the journal).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote ("The org chart is not the organization" + "I design for the flow of change") |
| The three structures are explicit | met | index.md · Statement bullet 1 + Rationale ¶3 + Figure 2; gap-as-diagnostic in Rationale ¶1 ("data, not disobedience") |
| Conway's Law and Dunbar's number survive | met | index.md · Rationale ¶2 (architecture + interactions together) and ¶5 (Dunbar, cognitive capacity) + checklist.md · Cognitive Load and Team Boundaries |
| Decisions in context | met | index.md · Rationale ¶4 ("decisions decay as they climb") + practice paragraph (returning decisions with trust made explicit) |
| Redesign discipline | met | index.md · Rationale ¶6 + contrast table row 6 (compelling reason, options, timing) |
| The checklist survives intact | met | checklist.md — all four PDF sections present (team design foundations; org charts & communication flow; cognitive load & boundaries; overall review) |
| Credit is explicit | met | index.md · Authoritative References (Skelton & Pais; teamtopologies.com) |

Non-goals respected: yes — no team-type/interaction-mode taxonomy (deferred to siblings), no sizing/sequencing territory from [[organizational-design]], the chart is explicitly *not* banned (Statement bullet 1, contrast table row 1), and no company-specific reorg proposal.
Drift: none of substance — only the changelog's pending-state ending (see Minor finding). Spec `status: accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — three structures, Conway mirroring, flow-of-change design, decision decay, and redesign discipline appear identically in article and checklist; the comic compresses the same six beats.
- **Terminology:** Largely consistent — "flow of change," "decisions decay as they climb," "the chart draws only the first [structure]" recur across modalities; the one wobble is "filing system" vs "snapshot" between excerpt and highlight (see Nit).
- **Voice & tone:** Consistent first-person register; the comic's Vera-peels-back-the-chart arc matches the article's map-vs-territory stance.
- **Coverage parity:** Nearly even. The comic carries six of the article's beats well; cognitive load and redesign discipline are absent from the comic — acceptable compressions for eight panels, and both are fully carried by the checklist.

## Layer-by-layer notes

### Spec
- Strong contract: seven criteria, each checkable; the decision log names the load-bearing idea (the chart/communication gap) and records the appendix grounding, both faithfully mirrored in How to Read This.
- Modalities prose is already accurate here ("Summary/dialog may be added later"); only the changelog ends on a stale pending state.

### index.md
- House shape intact; headings in Title Case; three figures present and captioned; five cross-links, all resolving.
- The Rationale argues rather than asserts throughout — "data, not disobedience," the four-way-coupling example for Conway, and the more-communication-is-not-better inversion give the record real teeth.
- The concrete practice paragraph after the contrast table ("reorg proposals that arrive as rearranged boxes go back with the question…") is an effective landing move other records in the journal lack.
- Statement/Rationale beat-count asymmetry around cognitive load (see Minor finding).

### checklist.md
- All four source sections preserved; the Overall Review Checklist's interrogative items work well as the "recurring instrument" the article's Scope section points at.
- The middle section (Org Charts and Communication Flow) is long (15 items) and mixes diagnosis, design, and redesign-discipline items — faithful to the source, but the least scannable stretch of the file.

### comics.md
- Eight panels, all image files present under `assets/images/org-chart-problems/`; captions match alt text; the peel-back-the-chart and context-sticky-notes-falling-off-the-ladder metaphors are the strongest visual beats in the six-post set.
- Panel 8's chart-in-the-drawer closer lands the "filing system" line — and matches the excerpt's wording, reinforcing the excerpt/highlight nit above.
