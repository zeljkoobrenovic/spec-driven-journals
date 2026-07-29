# Review: Written Exercises

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a tight, publish-ready record. The spec is a clean contract, the numbers
(3 hours, a few pages, 4×3=12, decision bands 11–12/8–10/7/≤6) hold exactly
consistent across spec, article, checklist, and comics, both rubric tables are
reproduced intact in the Checklist tab, and all eight comic panel images exist
and match their captions. The one thing worth a look before calling it done: the
decision-band numbers (11–12/8–10/7/≤6) are stated in full twice within a few
lines of each other in `index.md` (Statement bullet 5 and the second Rationale
paragraph) — a minor tightening opportunity, not a blocker.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

*(none)*

### Major

*(none)*

### Minor

- **[index.md · Statement bullet 5 vs. Rationale para. 4]** The full decision-band
  breakdown ("11–12 is a strong yes, 8–10 is a yes, 7 is a judgment call... 6 or
  below is a no") is spelled out twice almost verbatim, four paragraphs apart.
  *Consider having the Statement bullet state the principle and let Rationale
  carry the full numbers, or vice versa.*
- **[index.md · "What This Means in Practice" intro sentence]** "Concretely:
  before I open any candidate's submission..." repeats a claim already made in
  Rationale para. 4 ("I built the boundaries before I read anyone's submission")
  and in the Statement's closing sentence. Three restatements of "the rubric is
  written before I see the response" is one more than needed. *Trim the
  "Concretely" sentence or fold it into the table's framing instead of restating
  it.*

### Nits

- **[index.md · front matter]** `timetoread: 7 min` vs. `checklist.md`'s
  `timetoread: "6 min read"` — inconsistent string format ("7 min" vs. "6 min
  read"); harmless since it's not yet rendered, but worth aligning style if this
  field is ever surfaced.
- **[index.md · Anti-Patterns]** "Rewarding volume" bullet and "The unbounded
  take-home" bullet both make essentially the point that more pages is worse,
  from slightly different angles (scope discipline vs. communication failure) —
  fine as two anti-patterns, but the "fifteen-page response" example so closely
  echoes the "twenty pages" example in the Rationale's scope paragraph that a
  reader may feel they've read this anti-pattern already. Group mentally with
  the minor findings above; not worth a separate fix.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote, line 17 |
| Signal-before-scoring idea survives | met | index.md · Rationale para. 1 ("A well-built exercise is a signal...") and highlight |
| The numbers survive (3 hrs, few pages, 4×3=12, bands) | met | index.md (Statement, Rationale, table), checklist.md (§1, §4), comics.md (panels 5, 6) |
| Both rubric tables reproduced (bands + 4 skill tables) | met | checklist.md §4 (decision-band table) and §5–8 (four poor/good/excellent tables) |
| Product sense and data analysis precisely defined | met | index.md Rationale para. 4 ("so-whats," segment carried through); checklist.md §6–8 |
| Credit is explicit | met | index.md · Authoritative References; spec.md · Sources |

Non-goals respected: yes — no modality drifts into `interview-question-bank`
(live-conversation), `candidate-review` (combining scores into a final
decision), `interview-loop` (overall loop structure), or a generalized
non-PM rubric. The article explicitly scopes itself as PM-specific-but-adaptable
(Scope and Revisiting section), matching the spec's fourth non-goal.

Drift: none. Spec and post agree; this matches the Changelog's own note that
spec and post agree as of 2026-07-28.

## Cross-modality alignment

- **Facts & framing:** consistent. Scope (3 hrs / few pages / pre-read framing),
  the churn-and-retention prompt, the 4-skill/12-point rubric, and the four
  decision bands are identical in wording and numbers across index, checklist,
  and comics.
- **Terminology:** consistent — "judgment call," "so-whats," "customer sense
  carried through," and "pre-read" are used identically everywhere they appear.
- **Voice & tone:** consistent. First-person declarative in index.md; checklist
  is imperative/operational as its modality requires; comics captions are terse
  third-person scene descriptions in the journal's standard VERA/NOA register
  (cast and style block match every other post in this journal — not a finding).
- **Coverage parity:** even. The five-part operating model in index.md's
  Statement maps cleanly onto the comic's eight-panel arc (hook → problem →
  wrong way → principle → scope/prompt → rubric → cost of the score → free
  signal) and onto the checklist's four numbered sections. No modality
  introduces a beat the others lack.

## Layer-by-layer notes

### Spec

- Follows the template exactly (Intent, Audience, Success criteria, Non-goals,
  Modalities, Open questions, Decision log, Sources, Changelog).
- Success criteria are genuinely checkable — each names a specific fact,
  number, or table that must appear, not vague intent.
- Non-goals are precise and each points at a real sibling record; the fourth
  (general writing-skills rubric) correctly fences the PM-specific reference
  prompt from over-generalization.
- Sources cite the exact page range (70–72) and chapter; this is reproduced
  correctly in the article's Authoritative References and checklist's content.
- No bloat; Open questions correctly closed out as "None."

### index.md

- House record shape is complete and in the right order: Status/Principle
  highlight → Statement → How to Read This → Rationale → What This Means in
  Practice → Anti-Patterns → Related Records → Scope and Revisiting →
  Authoritative References.
- Section headings are correct Title Case throughout.
- Three figures, each captioned and numbered sequentially (1, 2, 3); all three
  referenced image files exist on disk.
- Cross-links `[[interview-loop]]`, `[[interview-question-bank]]`,
  `[[candidate-review]]`, `[[hiring]]` all resolve to real posts with matching
  titles in the build's crosslink index.
- Minor repetition of the decision-band numbers and the "written before I read
  a submission" point (see Minor findings above) is the only real drag on an
  otherwise tight, well-argued piece.

### checklist.md

- Both rubric tables from the spec are reproduced intact: the 12-point
  decision-band table (§4) and the four skill-scoring poor/good/excellent
  tables (§5–8).
- Numbered sections track the operating model in a natural build order: design
  → reference prompt → what's assessed → score.
- Checklist items are genuinely operational (imperative, checkable), not
  restated prose from the article.
- Sentence-case headings are the journal's established checklist convention
  (not a finding, per review scope).

### comics.md

- Eight panels, eight captions, eight image files — all present on disk under
  `assets/images/hiring-written-exercises/comic-01…08`.
- Cast and style block match the shared VERA/NOA convention used by every
  other post in this journal (not a finding).
- Visual metaphor is consistent panel to panel (scorecard, clipboard, packet
  motifs recur rather than reinventing per panel).
- Arc order mirrors the article's five-part operating model and adds only the
  narrative framing device (hook/problem/wrong-way) appropriate to the comic
  form — no beat introduced here is absent from index.md.

## Fixes applied (2026-07-29)

- **[minor: Statement bullet 5 vs. Rationale para. 4]** Fixed — Statement
  bullet 5 now states the principle ("maps to a fixed decision band, set
  before I read a single submission") without re-spelling all four numeric
  bands; Rationale para. 4 keeps the full 11–12/8–10/7/≤6 breakdown as the
  one place the numbers are spelled out.
- **[minor: "Concretely" sentence repeating the pre-read/rubric-before-reading
  point a third time]** Fixed — replaced with a sentence that frames the
  table as a practical handoff to a new interviewer ("resume closed, rubric
  anchors already fixed") instead of restating the same claim a third time.
- **[nit: `timetoread` "7 min" vs. checklist's "6 min read"]** Skipped —
  sibling-journal convention per fix policy; not a real inconsistency to fix.
- **[nit: "Rewarding volume" / "unbounded take-home" anti-patterns echoing the
  Rationale's "twenty pages" example]** Skipped — two distinct anti-patterns
  (scope discipline vs. communication failure) per the review's own read;
  not worth flattening into one.
