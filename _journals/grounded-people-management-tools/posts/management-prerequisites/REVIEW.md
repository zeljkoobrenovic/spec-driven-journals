# Review: Management Prerequisites

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Solid, well-grounded opening record for the journal — the workbook source is credited clearly, the cadences are reproduced correctly everywhere they matter, and the checklist stands on its own as a runnable tool. It is close to publish-ready. The one thing to fix first: Panel 6 of the comic pairs the "results and how" scorecard with the wrong cadence ("every three to six months"), which belongs to bidirectional feedback, not the formal performance conversation the panel is illustrating — a factual mismatch against both index.md and checklist.md.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 2 · nit 1

### Major
- **[comics.md · Panel 6 alt text]** The RESULTS/HOW scorecard panel is captioned with "a calendar marked every three to six months" — but per index.md's Statement and Rationale, "results and how" is the formal performance conversation, on the 3/6/12-month cadence, not the 3–6-month bidirectional feedback cadence. As written the panel visually attaches the wrong clock to the right idea. *Change the calendar caption to "every 3, 6, or 12 months."*
- **[index.md · Statement + Rationale]** Legal responsibilities never gets a standalone treatment in index.md — it is folded as a trailing clause into the "bar applies upward" bullet (Statement, bullet 6) and again tacked onto the end of the division-infrastructure paragraph (Rationale, last sentence). The spec's own framing ("five layers... each get explicit treatment") and checklist.md (`## 1. Legal responsibilities`, its own top-level group) both treat it as its own layer. Index.md's argument body is the one place it reads as an afterthought rather than a layer. *Consider a standalone sentence or sub-bullet for legal responsibilities rather than appending it to "upward."*

### Minor
- **[checklist.md vs. index.md, layer count]** Related to the point above: checklist.md's 5 groups map cleanly onto the spec's 5 layers, but index.md's Statement compresses to 6 bullets where the "layers" don't line up 1:1 with the checklist's groups (bullet 1 is framing, not a layer; legal is absent as its own bullet). A reader toggling between tabs has to work to see the correspondence. *Not urgent, but worth noting since spec ties a success criterion directly to "all five layers... explicit treatment."*
- **[index.md · Related Records]** Six cross-links are listed but only four are covered by the spec's Non-goals ([[performance-reviews]], [[writing-okrs]], [[compensation-conversations]], [[interview-loop]]). [[working-with-me]] and [[meetings]] are fine additions but aren't mentioned anywhere in the spec's Non-goals or Intent, so a reader auditing spec-to-post alignment has no signal they're coming. *No fix needed — just flagging that the spec's Non-goals list under-covers the actual Related Records set.*

### Nits
- **[index.md · line 56, table]** "Never rescheduled — life happens; a pattern of rescheduling is the failure, not one exception" is slightly indirect for a "what it does not say" cell; every other row states the negative claim directly. Minor stylistic outlier, not wrong.

## Spec ↔ post alignment

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md, Status/Principle blockquote |
| The cadences survive | met | index.md Statement + Rationale; checklist.md groups 2–3 |
| Results AND how | met | index.md Statement bullet 3, Rationale para 3; checklist.md items in group 2 |
| All five layers present | partial | checklist.md cleanly (5 groups); index.md folds legal into the "upward" bullet rather than giving it standalone treatment |
| The checklist survives intact | met | checklist.md, all 5 groups reproduced |
| Credit is explicit | met | index.md "How to Read This" and "Authoritative References" |

Non-goals respected: yes — no modality drifts into performance-review mechanics, OKR-writing mechanics, compensation conversation content, or interview-loop design; legal compliance is named as a requirement, not enumerated.

Drift: minor only (the legal-responsibilities layer treatment above). Not enough to warrant `status: drifted` on the spec — recommend a light touch-up to index.md's Statement/Rationale instead.

## Cross-modality alignment

- **Facts & framing:** consistent except the one cadence mismatch in comics.md Panel 6 (noted above). Cadences (weekly/biweekly 1:1s, quarterly goals, 3–6 month feedback, 3/6/12-month formal conversations, weekly/biweekly team meetings) match the workbook grounding and are identical across index.md and checklist.md.
- **Terminology:** consistent — "prerequisites," "pass/fail," "results and *how*," "rarely rescheduled" all recur with the same wording across index.md, checklist.md, and comics.md captions.
- **Voice & tone:** consistent first-person declarative register across index.md and checklist.md; comics.md captions compress the same voice appropriately for the form.
- **Coverage parity:** even. All five checklist groups have a corresponding beat in index.md's Statement/Rationale, and the comic's 8 panels touch the toolbox metaphor, the theater-on-fiction rationale, the rescheduled-1:1 anti-pattern, the pass/fail framing, the two-sided agenda, results-and-how, division infrastructure, and the upward-applies anti-pattern — a fair sampling of the load-bearing beats, appropriately compressed for 8 panels.

## Layer-by-layer notes

### Spec
- Clean, on-template, all sections present; Success criteria are genuinely checkable (each names a specific artifact or fact to verify against).
- Non-goals are precise and correctly scoped against sibling records ([[performance-reviews]], [[writing-okrs]], [[compensation-conversations]], [[interview-loop]]) but do not mention [[working-with-me]] or [[meetings]], both of which end up as Related Records in index.md — minor spec/post coverage gap, not a contradiction.
- Decision log is short and gives real rationale (why "entry bar" over "maturity model") rather than restating the Intent.

### index.md
- Follows house record shape exactly: Status/Principle → Statement → How to Read This → Rationale → practice table → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Headings are correct Title Case throughout.
- The amplifier metaphor (Rationale para 1) is strong and distinct from the "pass/fail" framing (Statement bullet 1, Principle blockquote) — reinforcement rather than redundancy, appropriate for an opening/foundational record.
- The one structural weak point is legal responsibilities never getting a standalone paragraph or bullet (see Major finding above) — it reads as an afterthought relative to how prominently checklist.md and the spec treat it.
- Figures (3) are captioned correctly and reinforce distinct ideas (layered stack, amplifier, cadence clock) rather than repeating one visual.

### checklist.md
- Clean operational tool: five numbered groups, sentence-case headings (per journal convention, not a finding), unchecked boxes throughout as expected for a template.
- Faithfully reproduces the workbook's Management Prerequisites Checklist; item wording matches index.md's Statement/Rationale claims one-for-one (e.g., "shorten the cycle the faster your company is changing" mirrors the Rationale's phrasing).
- Legal responsibilities correctly gets its own group here (group 1) — this is the modality where the "five layers" claim actually holds structurally, in contrast to index.md.

### comics.md
- 8 panels, matches journal-wide convention exactly; all 8 panel image files exist on disk.
- Cast and style block consistent with journal convention (VERA + one other named character per post).
- Panel 6 has the cadence mismatch described above (Major finding) — otherwise each panel's caption matches a real claim from index.md, and the visual metaphors (toolbox, turnstile, scorecard, binders shelf) are distinct from panel to panel without reuse.
- Panel 8's framing ("the exempt manager is the one anti-pattern with no excuse") is a fair compression of index.md's Anti-Patterns list entry "The exempt manager."

## Fixes applied (2026-07-29)

- **[comics.md · Panel 6 alt text, major]** Fixed — reworded the calendar detail in the alt text from "every three to six months" to "a recurring review date," so the results-and-how idea no longer ties to a specific cadence number the image may not show, without introducing a different number that carries the same risk.
- **[index.md · legal responsibilities, major]** Fixed — added a short standalone Rationale paragraph ("Legal responsibilities are their own layer, not a footnote.") giving legal responsibilities its own treatment, rather than leaving it as a trailing clause on the division-infrastructure paragraph. Left the Statement bullet 6 mention as-is (it's the "bar applies upward" bullet plus a legal-awareness sentence, not a redundant new bullet) since the brief called for a brief standalone treatment in Rationale, not a restructure of Statement.
- **[checklist.md vs. index.md, layer count, minor]** Skipped as a separate fix — review marked this "not urgent," and the Rationale addition above gives legal responsibilities the standalone weight the finding was about, narrowing the gap without restructuring the six-bullet Statement.
- **[index.md · Related Records vs. spec Non-goals, minor]** Skipped — review explicitly says "no fix needed," just flagging that spec Non-goals under-covers [[working-with-me]] and [[meetings]]. No action taken.
- **[index.md · line 56 table cell, nit]** Fixed — reworded "Never rescheduled — life happens; a pattern of rescheduling is the failure, not one exception" to lead with the direct negative claim ("A pattern of rescheduling..."), matching the phrasing pattern of the other rows in the table.
