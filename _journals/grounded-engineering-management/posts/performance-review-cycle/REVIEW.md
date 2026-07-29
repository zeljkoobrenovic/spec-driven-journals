# Review: Performance Reviews (performance-review-cycle)

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Content-wise publish-ready: all six spec criteria are met, the checklist is a verified faithful reproduction of the source PDF (spot-checked page by page), crosslinks resolve, and all figures and panel images exist. One major issue should be fixed before publishing: the post's title, "Performance Reviews," is identical to the people-journal record `performance-reviews` that this post crosslinks as "the other side of the same cycle." Because `[[…]]` link text is generated from the target's title, links to these two different records render identically everywhere, and readers cannot tell the manager-side and engineer-side records apart.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

- None.

### Major

- **[index.md · front matter `title:` (and spec.md title)]** Title "Performance Reviews" collides exactly with the people-journal record `performance-reviews` ("Performance Reviews"). The build renders `[[slug]]` links using the target's title, so `[[performance-review-cycle]]` and `[[performance-reviews]]` produce identical link text across the whole site — this post's own Related Records has to append a manual "(people journal)" note to disambiguate, and inbound links from [[own-your-career]] and [[promotions]] have no such note. The `id` and `permalink` already say "cycle." *Retitle distinctly, e.g. "Working the Performance Review Cycle" (permalink stays stable; every inbound link text updates automatically).*

### Minor

- **[comics.md · Panel 5]** Caption asks "'would achieving these exceed expectations?'" — dropping "meet or" from the question the article calls "the question the source insists on" and enforces verbatim ("would achieving these goals meet or exceed expectations?"). The shortened form changes the calibration semantics. *Restore "meet or exceed."*
- **[comics.md · cast comment]** Arlo is "an engineer newly stepping into management" — here he plays an engineer working his own review cycle. Reused blurb from the management-track posts; affects panel-regeneration consistency. *Reword.*
- **[spec.md · Sources]** The internal source path is line-wrapped inside the code span (`Checklist_ TSEG _ Performance` / `Reviews (1).pdf`), so the literal path as written doesn't match the file on disk. *Keep on one line.*

### Nits

- **[index.md · Rationale ¶3]** "watch for helping others growing at the expense of core responsibilities" — tangled gerund; the source's phrasing ("spending too much time helping others at the expense of…") is cleaner, and the article's own Statement b4 already has a better version ("helping that grows at the expense of…").
- **[comics.md · Panel 7]** "The cost:" label doesn't fit the content — assembling a self-review from artifacts is the payoff, not a cost.
- **[index.md + spec.md · References]** "(Pragmatic Engineer, 2023)" vs the sibling pragmatic-tech-lead's "(self-published, 2023)" and older posts' "(2023)" — publisher attribution inconsistent across the journal.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (written all year; end is too late) | met | index.md · highlight ("the meeting at the end only reads it out") |
| Early phase survives | met | index.md · Statement b1–b2, Rationale ¶1–2, Figures 1–2; checklist.md §1 |
| Habit phase survives | met | index.md · Statement b3–b5, Rationale ¶3; checklist.md §2 |
| Preparation phase survives | met | index.md · Statement b6, Rationale ¶4; checklist.md §3 |
| Interpretation phase survives (all 8 biases) | met | index.md · Statement b7, Rationale ¶5, Figure 3; checklist.md §4 (bias list matches the PDF verbatim) |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no calibration-gaming advice anywhere (the table explicitly disowns it: "understanding the system is transparency"); manager-side review writing stays deferred to [[performance-reviews]]; promotion-case building deferred to [[promotions]].
Drift: none. Spec `accepted` status stands. (The title collision is a naming defect, not spec drift.)

## Cross-modality alignment

- **Facts & framing:** Consistent — verified against the source PDF: the four phases, the endorse-and-record goal pipeline, the meets-or-exceeds question (except comic Panel 5, minor above), weekly/biweekly wins, bounded glue work, and the eight rater biases all match.
- **Terminology:** Consistent — "written all year," "calibration," "glue work," "snapshot, not the career," "same side" recur verbatim across article, checklist, and comic.
- **Voice & tone:** Consistent — manager first-person article; checklist addresses the engineer directly in the imperative, as the spec's Audience prescribes; comic narrator voice.
- **Coverage parity:** Even. All four phases appear in every modality; the comic's gate/film-strip metaphors map directly onto Figures 1 and 3 — the tightest article↔comic figure alignment in the batch.

## Layer-by-layer notes

### Spec

- Strong contract: four phase criteria mirror the source's four sections, each enumerating its sub-beats, so verification is mechanical.
- Non-goals include a behavioral fence ("no advice on gaming calibration") that the post visibly honors — a good pattern.
- Spec heading "# Spec: Performance Reviews" inherits the title-collision problem (major above).

### index.md

- House shape, Title Case headings correct, three figures on disk with matching alt/captions.
- Rationale ¶1 ("information has a deadline") and ¶5 ("measurements taken with an imperfect instrument") are the strongest framings; the "assembly rather than archaeology" beat is shared consistently with [[own-your-career]].
- All four `[[…]]` crosslinks resolve (performance-reviews, own-your-career, promotions, management-101).

### checklist.md

- Verified against `sources/software-engineering-guidebook/Checklist_ TSEG _ Performance Reviews (1).pdf`: all four sections reproduced in order, near-verbatim, with only benign merges (e.g. "who makes the final review decision, and who gives input" combines two source items; "feedback from peers, praise, and positive feedback" combines two).
- Well-formed task-list markdown; four numbered sections whose names match the source's emphasis ("Start early," "strong habits," "Prepare," "During and after").

### comics.md

- All 8 panel images exist; captions match alt text; the calibration-door metaphor is used twice (closed in Panel 2, still open in Panel 7) to carry the record's central deadline argument — effective.
- Panel 8 ends on "examined together from the same side," landing the spec's same-side criterion in the closer.

## Fixes applied (2026-07-29)

- **Major (title collision)** — already fixed centrally: retitled "Working the Performance Review Cycle"; verified present in index.md front matter, not redone here.
- **Comic caption fix** — Panel 5 caption restored to the verbatim source question: "would achieving these meet or exceed expectations?" ("meet or" had been dropped); caption text only, image untouched.
- **Comic caption fix** — Panel 7 label "The cost:" changed to "The payoff:" (assembling the self-review from artifacts is the payoff); caption text only, image untouched.

Skipped: cast blurb, spec source-path line-wrap, Orosz attribution — fixed centrally; Rationale ¶3 gerund nit — outside the flagged fix categories.
