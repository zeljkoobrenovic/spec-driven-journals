# Review: Own Your Career

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The seven-habit structure survives intact in all three modalities, all five spec criteria are met, crosslinks resolve, and every figure and panel image exists. The comic is the best of the four in this batch — its arc (waiting → flat review → outsourcing → habits → doors open) is a genuinely tighter telling than the article's. The most important thing to address is small: the "manager as ally" habit is the only one of the seven that never gets a Rationale paragraph, even though the spec's decision log singles out the manager's reciprocal duty as a framing choice.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Rationale]** Five rationale paragraphs cover habits 1 (goals), 2 (finishing), 3 (work log), 4+5 (feedback), and 7 (pacing) — habit 6, "make your manager an ally," gets none. The trust→advocacy mechanism is asserted in the Statement ("Trust built this way is what my advocacy runs on") but never argued, though the comic gives it a full panel (7). *One short paragraph, or fold into the goals paragraph.*
- **[comics.md · cast comment]** Arlo is "an engineer newly stepping into management" — here he plays an engineer owning his IC career. Reused blurb from the management-track posts; affects panel-regeneration consistency. *Reword.*
- **[spec.md · Sources]** The internal source path is line-wrapped inside the code span (`Checklist_ TSEG _ Own Your` / `Career (1).pdf`), so the literal path as written doesn't match the file on disk. *Keep on one line.*

### Nits

- **[comics.md · Panel 8]** The caption shifts into Vera's first person ("I can open doors and advocate…") while all other captions are narrator third-person. Effective, but a deliberate voice break worth confirming.
- **[index.md · "What This Means in Practice", Concretely]** "a work log that is current within two weeks" sits oddly against the weekly cadence stated everywhere else (Statement b3, checklist §3, comic Panel 6's "fifteen minutes a week"). Not contradictory (it's a tolerance), but pick one number.
- **[index.md + spec.md · References]** "(Pragmatic Engineer, 2023)" vs the sibling pragmatic-tech-lead's "(self-published, 2023)" and older posts' "(2023)" — publisher attribution inconsistent across the journal.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (can't drive it for them; habit set) | met | index.md · highlight (goals, finishing, evidence, feedback, alliance, pacing all named) |
| All seven habit areas survive | met | index.md · Statement b1–b7; checklist.md §1–7 map one-to-one |
| The manager's side is explicit | met | index.md · highlight, Figure 1 caption, table row 1, Scope; [[management-101]] linked in How to Read This and Related Records |
| Work log's double use survives | met | index.md · Statement b3, Rationale ¶3 (extended to a third use — 1:1 backbone — consistently echoed in Figure 2 and comic Panel 6) |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no drift into [[management-101]]'s two-sided contract, [[performance-review-cycle]] mechanics, [[promotions]] case-building, or the manager-run [[career-conversations]]; each is linked and fenced exactly as the spec requires.
Drift: none. The article's third work-log use (1:1 backbone) goes slightly beyond the spec's "double use" — enrichment, not contradiction; not worth a status change. Spec `accepted` stands.

## Cross-modality alignment

- **Facts & framing:** Consistent — "a manager who has to guess your goals will guess wrong," the flat-review-as-missing-information reading, the fifteen-minutes-a-week log, and stretch/execute/coast all match across modalities.
- **Terminology:** Consistent — "habit set, not luck," "ally," "work log," "stretching, executing, coasting" recur verbatim.
- **Voice & tone:** Consistent and deliberate — manager first-person article; checklist in the engineer's first person exactly as the spec's Audience section prescribes; comic narrator (with the one Panel 8 voice break noted above).
- **Coverage parity:** Even. All seven habits appear in article and checklist; the comic compresses feedback (habits 4–5) into the Panel 4 wheel rather than giving them a panel — a fair cut for eight panels, and the wheel names them.

## Layer-by-layer notes

### Spec

- Clean contract; the seven-habit criterion enumerates sub-beats per habit, making verification mechanical.
- Non-goals are the best-drawn in the batch — four adjacent records, each with a one-line boundary.

### index.md

- House shape, Title Case headings correct, three figures on disk with matching alt/captions.
- Rationale ¶2 ("Reputation compounds from finishing, not from starting") and ¶3 (assembly vs. archaeology) are the strongest passages; the archaeology line is reused by the performance-review-cycle post, consistently.
- All five `[[…]]` crosslinks resolve (management-101, performance-review-cycle, promotions, feedback, career-conversations).

### checklist.md

- Seven numbered sections, ~45 items, first-person engineer voice throughout as announced — faithful, lightly condensed reproduction of the source checklist's structure.
- Well-formed task-list markdown; terminology matches the article exactly (e.g. "prioritize, stop, or say 'no'").

### comics.md

- All 8 panel images exist; captions match alt text; the door motif opens (Panel 1, ignored doors) and closes (Panel 8, held-open door) the arc — the strongest visual bookending in the batch.
- Panel 3's yarn-ball metaphor lands the "savior" anti-pattern without a word of jargon.
