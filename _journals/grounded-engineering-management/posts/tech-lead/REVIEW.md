# Review: Tech Lead

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready, and the strongest Rationale of the four Manager's Path openers — the make/delegate/escalate and ambiguity-into-sequence paragraphs argue rather than assert. Every spec criterion is met and all assets and crosslinks check out. The most important thing to address is a set of small parity gaps between article and checklist: the article's pointer to the Checklist tab omits two of its ten sections, and the checklist's "Personal growth" beat surfaces in the article only as a clause in Scope and Revisiting.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 1

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · How to Read This]** The enumerated checklist contents ("role and mindset, technical leadership, planning, project management, team duties, communication, process judgment, and the reflection questions") name eight parts, but checklist.md has ten sections — "Team effectiveness" (§7) and "Personal growth" (§9) are missing from the list. *Extend the enumeration or make it non-exhaustive ("…and more").*
- **[checklist.md §9 ↔ index.md]** The personal-growth/career-honesty beat ("assess honestly whether I want to stay on the technical track, grow as a tech lead, or move into management") appears in the article only as a clause in Scope and Revisiting — the Statement and Rationale never carry it, so the checklist introduces a beat the article barely sets up. *One sentence in the Statement's first bullet or a short Rationale clause would restore parity.*
- **[index.md · excerpt / highlight / Statement bullet 2 / Rationale para 2 / Practice table row 2]** The bottleneck-vs-hands-off pair is restated in near-identical wording five times before Anti-Patterns names it twice more (The bottleneck, The absentee architect). The ADR shape expects echo, but this beat repeats more verbatim than any other. *Vary or trim one of the Statement/Rationale restatements.*

### Nits
- **[index.md · front matter]** The `excerpt` restates the Principle highlight nearly clause for clause. House pattern, cosmetic only. *(Grouped.)*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable — team outcomes, no formal authority, bottleneck/hands-off avoided | met | index.md · Status/Principle highlight |
| Decision discipline survives (make/delegate/escalate, team input, critical systems/dependencies/risks) | met | index.md · Statement bullet 2, Rationale para 2, Figure 2; checklist.md §2 |
| Planning discipline survives (deliverables, parallel/sequential, critical/optional, ambiguity, revisit, premortem + launch + rollback, early status) | met | index.md · Statement bullet 3, Rationale para 3, Figure 3; checklist.md §§3–4 |
| Team-side duties survive (unblock not hoard, delegate to grow, focus time, no heroics, represent outward) | met | index.md · Statement bullets 4–5, Rationale para 4; checklist.md §§5–7 |
| Process stance survives (tool not substitute, no perfect process, people over rules, self-regulating over policing) | met | index.md · Statement bullet 6, Rationale para 5; checklist.md §8 |
| Credit explicit — Fournier + Tech Lead chapter | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes — the engineer-side view is delegated to `[[pragmatic-tech-lead]]` with the distinction stated twice, people management is explicitly fenced ("guidance yes, performance management no"), and the managing-a-team rung is pointed forward to, not described.
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. Team outcomes over personal output, influence without authority, the sorted-decision discipline, premortem/launch/rollback, and the accepted cost (slower personal technical progress) are identical across all three modalities.
- **Terminology:** Consistent — "make, delegate, or escalate," "bottleneck," "hands-off"/"absentee," "premortem," "rollback plan" recur verbatim; comic Panel 8's "without preparation" quotes the article's "Concretely" test exactly.
- **Voice & tone:** Consistent; shared VERA/ARLO cast, same register as the sibling comics.
- **Coverage parity:** Good on the load-bearing beats. Two article beats are compressed out of the comic — the process-as-tool stance and outward representation — defensible for an eight-panel form. The checklist-vs-article gap on personal growth is filed above as a finding.

## Layer-by-layer notes

### Spec
- Full template; the Intent paragraph doubles as an accurate article outline. Five substantive criteria plus credit, all checkable, all met.
- The decision log records the central framing choice (bottleneck/hands-off as the failure axis) and the deliberate split from `[[pragmatic-tech-lead]]` — exactly what a future editor needs.

### index.md
- The Rationale is the post's strength: each paragraph earns its claim, and "heroics are a debt instrument" and "trust runs on being consulted" are memorable without being empty.
- All four crosslinks resolve (`pragmatic-tech-lead`, `mentoring`, `management-101`, `managing-a-team`); all three figures exist on disk and are captioned; Title Case headings throughout.
- The "Concretely" paragraph gives a genuinely inspectable test (visible plan, premortem/rollback before launch, the no-preparation decision-sorting answer) — the best practice-anchor of the four posts reviewed.

### checklist.md
- Ten numbered sections, well-formed task-list markdown, first-person from the tech lead's chair — consistent with the journal's checklist convention (the "I" is the role-holder, not the author). Nothing reads invented against the named source PDF; not independently re-verified page-for-page (the sibling Management 101 PDF spot-check confirmed the journal's verbatim-reproduction pattern).
- §10's reflection questions are questions rendered as checkboxes — faithful to the source and workable, though they check "considered" rather than "done."

### comics.md
- Eight panels, all image files present, captions match alt text, consistent cast/style.
- The arc (title arrives → project drifts → bottleneck-or-ghost → team outcomes on influence → sorting → plan/premortem/rollback → the cost → the closer) mirrors the article's argument order almost one-to-one; Panel 7 carrying the "slower personal progress" cost is the right beat to keep.

## Fixes applied (2026-07-29)

- **Checklist-only spec beat** — the personal-growth/career-honesty beat (checklist §9) now has an article echo: one sentence added to the Statement's first bullet ("Holding the rung is also how an engineer finds out, honestly, whether they want to stay on the technical track, grow as a tech lead, or move into management").
- **Verbatim self-repetition** — trimmed the bottleneck/hands-off restatement from Statement bullet 2 ("— sitting neither at the bottleneck extreme nor the hands-off one" removed); the beat keeps its strongest sites in the Principle highlight, Rationale para 2, and Anti-Patterns.
