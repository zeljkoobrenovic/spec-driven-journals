# Review: Meetings

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The portfolio framing (one shared quality bar, cancellation question as refrain) is carried consistently across article, checklist, and comic; all spec success criteria are met, all seven comic panels and three figures resolve on disk, and all five cross-links point at real posts. The most important fix is a garbled checklist item under Ownership & Leadership that reads as the opposite of its intent.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · Ownership & Leadership, first item]** "Clear the meeting owner for each recurring session." reads as an instruction to *remove* the owner. *Reword to "Clear meeting owner for each recurring session."*
- **[spec.md · Modalities]** The prose sentence "Summary/dialog/comics may be added later per journal policy" is stale — comics has shipped (checkbox `[x]`, Changelog 2026-07-26). *Reword to cover only summary/dialog.*

### Nits
- **[checklist.md · Weekly Incident Review]** "Discussion over the presentation." — stray "the"; elsewhere (Quality Bar, index table) the phrase is "discussion over presentation".
- **[index.md · Statement, bullet 2]** The "small core cadence" bullet packs the full supporting orbit (1:1s, skip-levels, execution reviews, show-and-tells, tech talks, all-hands) into one long sentence — parseable, but the densest moment in the post.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (purposeful cadence, document-anchored, cancellation question) |
| Rationale is argued, not asserted | met | index.md · Rationale ¶1 (gap-filling vs default, cost argument) and ¶2 (documents + discussion vs presentation) |
| The checklist survives intact | met | checklist.md — all six source sections present (foundations; core cadence; additional high-value meetings; scaling; ownership & leadership; quality bar) |
| Anti-patterns are concrete (≥3) | met | index.md · Anti-Patterns (six, including the spec's three named examples: status theater, premature split, recorded Q&A) |
| Credit is explicit | met | index.md · Authoritative References (Primer + lethain.com essay) |

Non-goals respected: yes — async/written communication deferred to [[internal-communication]], general process ownership deferred to [[run-engineering-processes]], no company-specific calendar (days/durations/attendees explicitly out of scope in How to Read This and Scope).
Drift: none. Spec `status: accepted` remains accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — the five purposes, the four-weekly/three-monthly core, document anchoring, the no-recording Q&A stance, and split-on-context-not-headcount appear identically in article and checklist; the comic compresses them faithfully.
- **Terminology:** Consistent — "status theater," "purpose before existence," "documents anchor, discussion decides," and the cancellation question recur verbatim across modalities.
- **Voice & tone:** Consistent first-person operating-principle register; comic uses the house VERA/LEO cast and matches the article's stance.
- **Coverage parity:** Even. The comic (7 panels) carries hook → cost → status theater → purposes → documents → immortal meetings → cancellation question; the only index beats it skips (Q&A safety, scaling) are appropriately left to the fuller modalities.

## Layer-by-layer notes

### Spec
- Solid contract: checkable criteria that each name a verifiable artifact; the decision log usefully records why the portfolio framing beat a meeting-by-meeting how-to.
- Same stale Modalities sentence as sibling specs (see Minor finding); checkboxes and Changelog are already correct.

### index.md
- House shape intact (Status/Principle highlight, Statement → How to Read This → Rationale → contrast table → Anti-Patterns → Related Records → Scope → References); headings in Title Case.
- The "most expensive communication instrument" cost argument gives the gap-filling rule a real foundation rather than an assertion; the Q&A-safety paragraph is a genuinely argued beat (recording → no real questions).
- The cancellation question works as a deliberate refrain (highlight, quality bar, Anti-Patterns closer, Scope) without tipping into repetition.
- Five cross-links, all resolving; three figures present and captioned.

### checklist.md
- Serves its operational purpose well: per-meeting sub-checklists under the core cadence make it genuinely runnable, and nested sub-items (Q&A tooling, manager-meeting format) preserve the source PDF's detail.
- Two wording slips (see Minor/Nit findings); otherwise items are imperative and checkable.
- The Quality Bar section's lead-in line ("For every meeting, ask:") is a plain bullet between checkbox lists — renders fine, slightly inconsistent formatting.

### comics.md
- Seven panels, all image files present under `assets/images/meetings/`; captions match alt text; VERA/LEO metaphor consistent (Vera correcting Leo's calendar-accretion instincts).
- Panel 6 merges two article anti-patterns (ownerless + immortal meetings) into one caption — a fair compression for the form.
- The closer lands the article's refrain (the cancellation question) as the final panel, mirroring the index structure.
