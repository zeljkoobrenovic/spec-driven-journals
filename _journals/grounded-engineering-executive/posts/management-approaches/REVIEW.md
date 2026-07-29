# Review: Management Approaches

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All seven spec success criteria are met, the appendix framing is stated exactly where the spec wants it, and the nine-section checklist survives intact with the source's own numbering. The record covers a lot of ground by design, and mostly earns it; the one structural weak point is the final Rationale paragraph, which compresses four distinct checklist sections (getting stuck, manager partnership, scope, setting direction) into a single dense paragraph — the only place where the reader has to work hard.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Rationale, last paragraph ("Scope is impact, not headcount…")]** One paragraph carries four separate topics — the stuck-manager traps, the counter-moves, partnering with your manager, and setting direction when feedback goes scarce — via two very long serial-list sentences (~120 words). Every other Rationale paragraph handles one idea; this one handles four. *Split into two paragraphs (traps/counter-moves vs. manager partnership/direction) or promote one bolded lead per topic.*
- **[comics.md · whole strip]** The comic covers the highlight's four load-bearing approaches (policy, no-with-data, triage, ethics/hierarchy) but has no echo of the growth-plates style-switching beat or the scope-as-impact beat that Rationale ¶4–5 carry. Defensible compression given the decision log names the four headline approaches, but worth a deliberate call. *Confirm the omission is intended.*

### Nits
- **[checklist.md · Section 9, first line]** "For every recurring or unresolved problem, choose one:" is a plain bullet in a checkbox list — renders as an odd mixed list item; a non-bullet lead-in line would sit cleaner.
- **[checklist.md · Section 2]** "Identify whether the real constraint is capacity, prioritization, or relationships" — index.md's highlight names the triple as "velocity, prioritization, or relationships" while the Rationale says "capacity, prioritization, or relationships"; the two triples coexist across article and checklist. Harmless (velocity ≈ capacity) but slightly wobbly terminology.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (four approaches in one paragraph) | met | index.md · highlight (policy-over-exceptions, no-with-data, ethical profession, close-out/solve/delegate) |
| Appendix framing explicit (*An Elegant Puzzle*, executive lens) | met | index.md · How to Read This |
| Exception loop concrete (batch, refresh, churn anti-pattern) | met | index.md · Statement bullet 1 + Rationale ¶1 + Anti-Patterns ("Exception whack-a-mole," "Policy churn") |
| Saying no mechanical (velocity vs. prioritization, kanban, concrete debt) | met | index.md · Rationale ¶2 + Figure 2; checklist.md · Section 2 |
| Triage fork named (three options + consequence) | met | index.md · Statement bullet 4 + Figure 3 + "The heroic solver"; comics.md · Panel 5 |
| Checklist survives intact (all 9 PDF sections) | met | checklist.md · Sections 1–9, source grouping preserved |
| Credit explicit (*An Elegant Puzzle* + lethain origins) | met | index.md · Authoritative References |

Non-goals respected: yes — Primer-grounded themes are linked ([[inspected-trust]], [[calibrating-your-standards]], [[managing-energy]]) rather than restated; org design and systems thinking deferred to the appendix siblings; no career-ladder or promotion-process content (Section 7 stays on scope-vs-headcount, which the spec's Intent explicitly includes).
Drift: none. Spec status `accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — batching/refresh loop, kanban view, company→team→myself ordering, and the three-way triage match across all three modalities.
- **Terminology:** Largely consistent ("work the policy," "growth plates," "close out / solve / delegate"); one wobble between "velocity" and "capacity" as the first constraint (see Nit).
- **Voice & tone:** Consistent first-person declarative; checklist imperative; comic keeps the VERA/LEO register, with Leo as the exception-approving manager — apt casting for the manager-era material.
- **Coverage parity:** The four headline approaches are in full parity. Growth plates, stuck-manager traps, manager partnership, and setting direction live in article + checklist but not the comic (see Minor); checklist introduces no beat the article lacks.

## Layer-by-layer notes

### Spec
- Seven genuinely checkable criteria; the decision log records both structural choices (appendix grounding; keep the whole "Approaches" set rather than one theme) and the article honors them.
- Non-goals do heavy lifting for an appendix record that borders four other posts — and they hold.

### index.md
- House record shape and Title Case headings correct; all three figures resolve and are captioned; all six `[[…]]` cross-links resolve.
- Rationale ¶1–3 are excellent — each argues one approach with a real mechanism ("every grant erodes the policy's meaning and trains the organization that persistence beats process" is the record's best line).
- The seven-row "says / does not say" table is longer than siblings' but each row disarms a real misreading; it earns the length.
- The final Rationale paragraph's density is the main readability cost (see Minor).

### checklist.md
- The longest checklist in the reviewed set and properly so — nine numbered sections mirroring the source PDF, with the numbering preserved as the spec requires.
- Section 9's "use this method for a week and review" closer keeps the operational, runnable feel.
- Minor list-form and terminology nits noted above.

### comics.md
- Eight panels, all image files exist under `assets/images/management-approaches/`; alt text and captions agree.
- Strong first act: panels 1–3 tell the exception-whack-a-mole → batching story visually, the best single-concept sequence of the strip; the crossed-out desk-loop in Panel 5 matches Figure 3 exactly.
- Panel 8's "the philosophy is yours, and it keeps evolving" matches the checklist's "Revisit and evolve your philosophy over time" — good closer parity.
