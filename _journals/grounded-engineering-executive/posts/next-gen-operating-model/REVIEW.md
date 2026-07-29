# Review: The Next-Generation Operating Model

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A well-executed capstone record: the synthesis framing is explicit, the five-move getting-started sequence is clean, and the "vocabulary plus a feedback loop" line gives the whole appendix a memorable spine. All images resolve and all six cross-links point at real posts. The one thing to fix before publishing is the comic's visible step-numbering gap — captions jump from "Step three" to "Step five," which reads as an error rather than a compression.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Blockers
- None.

### Major
- **[comics.md · Panels 3–6]** The captions number the getting-started moves ("Step one" … "Step three") and then jump to "Step five: practice sensing" in Panel 6 — step four (close capability gaps) is silently skipped, so the numbered sequence reads as a mistake to anyone who counts. *Either add a capability-gaps beat, renumber, or drop the explicit numbering from the captions.*

### Minor
- **[spec.md · Changelog, 2026-07-26 top entry]** The latest entry says comics was "staged … with pending panel blocks" and illustrations were "placeholders staged" — both are now complete (all images exist on disk), but no completion entry follows, so the spec's history ends on a pending state. *Add a completion line.*
- **[index.md · Rationale, Figure 2]** The getting-started-path figure sits at the end of Rationale, one section before the sequence it illustrates is introduced (What This Means in Practice). *Move the figure into the sequence section or add a forward-pointing sentence.*

### Nits
- **[checklist.md · headings]** Sections use `##` where sibling checklists (measuring, meetings, M&A) use `###` — renders fine, but inconsistent within the journal.
- **[checklist.md · Diagnose Current Delivery Problems]** Items are phrased as desired end-states ("Teams are not disengaged or overloaded") under a "Diagnose problems" heading — checking a box asserts absence of the problem, which reads slightly inverted for a diagnosis section.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (four types, three modes, cognitive load, Conway, sensing — plus the "vocabulary plus a feedback loop" close) |
| The synthesis is explicit | met | index.md · Statement (assembles all five pieces) + How to Read This ("read it first, as the map, or last, as the capstone") |
| The getting-started sequence survives | met | index.md · What This Means in Practice (five numbered moves in spec order, framed as "a sequence, not a menu") |
| The readiness check is present | met | checklist.md · Final Readiness Check (all dimensions) + index.md · move 5 ("the final readiness check is never 'done'") — satisfied across modalities |
| The checklist survives intact | met | checklist.md — all twelve PDF sections present, including the nested stream types under Identify Streams of Change |
| Credit is explicit | met | index.md · Authoritative References (Skelton & Pais, IT Revolution Press, 2019; teamtopologies.com) |

Non-goals respected: yes — individual pieces are deferred to [[four-fundamental-team-topologies]], [[team-interaction-modes]], [[conways-law]]; no target org chart; the platform appears only as a starting move; the "never finished" property is affirmatively carried (Scope: "if the topology has not changed in a year, I treat that as a finding").
Drift: none of substance — the only spec staleness is the changelog ending on a "staged/pending" state (see Minor finding). Spec `status: accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — four types, three modes, cognitive-load boundaries, deliberate Conway, sensing, and the five-move sequence match across article and checklist; the comic carries the same spine minus step four (see Major finding).
- **Terminology:** Consistent — "thinnest viable platform," "streams of change," "sensing," "a model everyone can name" recur verbatim across modalities.
- **Voice & tone:** Consistent first-person register; comic keeps the house VERA/LEO dynamic and the puzzle metaphor mirrors the article's "assembles the pieces" framing.
- **Coverage parity:** Nearly even; the comic omits the capability-gaps move and the organizational-conditions beat — the latter is fine for the form, the former is exposed by the caption numbering.

## Layer-by-layer notes

### Spec
- Good contract for a synthesis record: the decision log states both the appendix grounding (Team Topologies, not the Primer) and the capstone role, which the article's How to Read This faithfully mirrors.
- Unlike sibling specs, the Modalities prose here is already accurate ("Summary/dialog may be added later"); only the changelog's pending-state ending is stale.

### index.md
- House shape intact; headings in Title Case; three figures present and captioned; six cross-links, all resolving.
- The Rationale's second paragraph ("The pieces only work together") is the strongest passage — it argues the anti-piecemeal claim with concrete failure modes per missing piece rather than asserting it.
- The contrast table earns its six rows; "a department wearing a costume" and "topology without practices is a diagram" are effective compressions.
- Figure 2 placement slightly ahead of its section (see Minor finding).

### checklist.md
- Longest checklist in the set (12 sections) and appropriately so for a synthesis record; the 5-min timetoread matches its length.
- Items are imperative and checkable; nested stream types preserved as the spec requires.
- Two formatting inconsistencies vs sibling checklists (heading level, diagnosis phrasing) — see Nits.

### comics.md
- Eight panels, all image files present under `assets/images/next-gen-operating-model/`; captions match alt text; the scattered-puzzle → assembled-puzzle frame is a strong visual arc that bookends the synthesis idea.
- The step-numbering skip (Major finding) is the only real flaw; Panel 8's "assembled — and never quite finished" closer lands the record's defining property well.
