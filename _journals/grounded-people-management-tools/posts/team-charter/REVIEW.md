# Review: Team Charter

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Solid, well-grounded post: the eight charter sections and the foundations
self-test are transcribed accurately from the workbook (verified against
`sources/Scaling-People-Workbooks_PDF_23_03_05.pdf`, pp. 15–23), the checklist
mirrors the article's structure section by section as the spec requires, and
the comic's eight panels track the article's real beats. It is close to
publish-ready. The one thing to fix before that: the article's "Related
Records" list — and the excerpt/tags — reach further than the spec's Non-goals
allow, most visibly in leaning on `[[measuring-engineering-organizations]]`
and `[[organizational-values]]`, two cross-journal links the spec never
mentions and that pull the piece slightly outside its own stated scope.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 3 · nit 3

### Major
- **[index.md · "Related Records"]** Two of the six related-record links
  (`[[organizational-values]]`, `[[measuring-engineering-organizations]]`)
  point to a different journal (`grounded-engineering-executive`) and are not
  named anywhere in spec.md's Non-goals, Sources, or Decision log — they
  resolve correctly (both targets exist) but their inclusion is undocumented
  scope-creep relative to the contract. *Either add them to the spec's
  Sources/Non-goals as intentional cross-journal ties, or drop them.*
- **[checklist.md · §9 heading, spec Success criteria]** The spec's success
  criterion says the foundations table "is reproduced ... with the workbook's
  pointed guidance," but the workbook's actual instruction line ("How easily
  can you complete it... Is this information documented anywhere in your
  division, and is it easy to find?") is only partially carried — the
  checklist keeps the "imagine how your teams and reports must feel" line but
  drops the "is this documented anywhere... easy to find" framing that the
  article's Rationale section (and its own bullet list) leans on heavily.
  *Minor content-completeness gap between spec claim and checklist body — add
  the missing sentence or soften the criterion's wording.*

### Minor
- **[checklist.md · §9 heading]** "Organizational Foundations self-test" is
  Title Case while every other checklist heading in this post (and the
  journal's other checklists, e.g. `writing-okrs/checklist.md`) is sentence
  case. *Retitle "9. Organizational foundations self-test" for consistency,
  unless the capital-letter workbook proper-noun is intentional (it is
  capitalized in the source PDF's own section header).*
- **[index.md · Rationale, metrics paragraph]** "Metrics without targets are
  decoration" (paragraph opener) and the Anti-Patterns bullet "Metrics without
  targets" restate the identical claim with near-identical wording twice in
  one article; a reader hits the same sentence shape twice within ~30 lines.
  *Vary one restatement or let Anti-Patterns cross-refer instead of repeat.*
- **[index.md · Statement vs Rationale]** The Statement bullet "Every metric
  carries a target, not just a name" and the Rationale's "Metrics without
  targets are decoration" both lead with the same point before the checklist
  even gets to it a third time (§4's bolded "no metric without a number").
  Three near-identical framings of one idea across one modality is more
  repetition than the point needs. *Trim one instance, or let each occurrence
  add a new angle instead of re-stating the rule.*

### Nits
- **[spec.md · Success criteria]** "the foundations self-test survives
  intact" bullet and "the runnable tool ships" bullet both describe
  `checklist.md`'s structure — slightly overlapping checkboxes rather than
  two independently falsifiable criteria.
- **[index.md · Rationale, interfaces paragraph]** "five items, three items in
  the worked example" is a slightly awkward inline aside; consider "(five and
  three items, respectively, in the worked example)" for smoother parsing.
  Also double-check against the source: the worked example actually lists
  **six** provided interfaces (Login code, 2FA infrastructure, Session
  infrastructure, Login/email challenge, Dashboard auditing models, Account
  recovery/password reset flow) and **three** dependent interfaces — the
  article's "five items" undercounts the provided-interfaces list by one.
- **[comics.md · Panel 7 caption]** "my own trouble filling in the table"
  switches to first person inside an otherwise third-person/character-facing
  caption style used in Panels 1–6 and 8 ("Noa watches...", "Vera and Noa
  pin..."); a small voice wobble in an otherwise consistent caption register.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight blockquote, lines 15–17 |
| All eight charter sections survive, grounded in worked example | met | index.md Statement/Rationale; checklist.md §1–8, each with a worked example |
| Metric discipline explicit (measures + target) | met | index.md Rationale ¶3; checklist.md §4 table + "no metric without a number" |
| Foundations self-test survives intact, three-column/five-row, with pointed guidance and documented-and-findable requirement | partial | checklist.md §9 table matches source rows/columns and keeps the "imagine how your teams... must feel" line, but the "is this documented... easy to find" framing from the source is thinned relative to how much weight index.md's Rationale puts on "documented and findable" |
| Runnable tool ships, mirrors charter structure section by section, ends with self-test + publish step | met | checklist.md §1–8 mirror index.md's eight sections in order; §9 self-test; §10 publish and maintain |
| Credit explicit (Scaling People + workbooks) | met | index.md Authoritative References; checklist.md byline note; spec.md Sources |

Non-goals respected: yes for writing-okrs, quarterly-business-reviews,
operating-principles, and team-design/topology (none of these bleed into the
post). Partial breach: the two cross-journal `[[…]]` links noted above sit
outside anything the spec names as in-scope material — not a Non-goal
violation by letter, but undocumented scope the spec should either claim or
the post should drop.

Drift: none rising to `status: drifted` — the post substantially matches its
spec. The one gap (foundations-table framing, above) is small enough to close
with a checklist tweak rather than a spec rewrite.

## Cross-modality alignment

- **Facts & framing:** Consistent. The mission/vision/metrics/interfaces
  worked-example language matches verbatim (or near-verbatim, correctly
  case-adjusted for mid-sentence quoting) between index.md and checklist.md,
  and both match the source PDF.
- **Terminology:** Consistent — "provided interfaces" / "dependent
  interfaces," "target value," "foundations table," and "DRI" are used
  identically across index.md, checklist.md, and comics.md.
- **Voice & tone:** Consistent first-person declarative in index.md and
  checklist.md; comics.md is appropriately terser and visual, with the one
  first-person caption wobble noted above (Panel 7).
- **Coverage parity:** Even. All eight charter sections plus the foundations
  self-test appear in both index.md and checklist.md; the comic's eight
  panels each map to a real beat (adrift team → five answers → stale
  onboarding slide → eight sections → target value → two-way interfaces →
  hard-to-fill table → published/findable), with no invented beat and nothing
  load-bearing left uncovered.

## Layer-by-layer notes

### Spec
- Clean MADR-adjacent shape, all template sections present and short.
- Success criteria are mostly checkable; two (foundations-table and
  runnable-tool criteria) overlap slightly on describing `checklist.md`'s
  shape rather than being fully independent checks.
- Non-goals are crisp and each correctly distinguishes this record from its
  three sibling records — no overlap confusion.
- Decision log records the "documented, not remembered" framing choice
  clearly; Sources correctly cites the PDF page ranges (verified accurate:
  pp. 15–22 charter, p. 23 foundations self-test).

### index.md
- Faithful to the source material; the "boring sentence forecloses drift"
  argument in Rationale ¶1 is a genuine, well-supported claim, not filler.
- Table in "What This Means in Practice" is well-formed and follows the
  journal's own convention exactly (title matches every sibling post).
- Minor repetition on the metrics-without-targets point (flagged above,
  three near-identical statements across Statement/Rationale/checklist).
- Provided-interfaces count in Rationale ¶4 ("five items") is one short of
  the worked example's actual six-item list (flagged as a nit).
- Cross-links: four of six resolve within journal-standard sibling records
  cleanly; two reach into `grounded-engineering-executive` without spec
  cover (flagged as major).

### checklist.md
- Mirrors the article's eight sections in the same order, then adds the
  self-test and a "publish and maintain" closing section exactly as the spec
  requires.
- Worked examples are accurate transcriptions of the source PDF, including
  the metrics table's "Measuring / Target value" shape.
- §9 heading capitalization breaks the sentence-case pattern used by every
  other heading in this file (nit/minor, see above).
- §9 keeps the workbook's "imagine how your teams and reports must feel"
  line but does not carry forward the source's "is this information
  documented anywhere... and is it easy to find" sentence, which the article
  treats as load-bearing (Rationale ¶4 leans on "documented and findable").

### comics.md
- Eight panels, each with a short caption and matching alt text; all eight
  referenced image files exist under `assets/images/team-charter/`.
- Visual metaphor (clipboard, whiteboard, target-value bracket, two-column
  interface list, blank table cell, homepage board) stays consistent and
  escalates logically from problem to resolution.
- Panel 7's caption briefly shifts to first person ("my own trouble") inside
  an otherwise third-person caption style (nit).

## Previous review

*(No prior REVIEW.md existed for this post.)*

## Fixes applied (2026-07-29)

- **[Major, index.md Related Records]** Added the two cross-journal links
  (`[[organizational-values]]`, `[[measuring-engineering-organizations]]`) to
  spec.md's Non-goals as intentional cross-journal ties, with a one-line
  rationale for each, instead of dropping them from the article.
- **[Major, checklist.md §9]** Restored the workbook's "is this information
  documented anywhere in your division, and is it easy to find?" question to
  the foundations self-test intro line, ahead of the "imagine how your teams
  and reports must feel" sentence.
- **[Minor, checklist.md §9 heading]** Retitled "9. Organizational Foundations
  self-test" to sentence case ("9. Organizational foundations self-test") for
  consistency with every other heading in this checklist.
- **[Minor, index.md Rationale metrics paragraph]** Reworked the "Metrics
  without targets are decoration" opener to argue *why* a target matters
  (accountability — an unmeasured number can never be wrong, so no one can be
  held to it) instead of restating the Anti-Patterns bullet's wording.
- **[Minor, index.md Statement vs Rationale]** Left as-is: the Statement
  bullet, the reworked Rationale opener, and checklist §4's bolded line now
  each carry a distinct angle (the rule itself, why it matters, the runnable
  check) rather than three restatements of the same sentence — resolved as
  part of the metrics-paragraph fix above.
- **[Nit, spec.md Success criteria]** Skipped — the "foundations self-test"
  and "runnable tool" criteria overlapping slightly on describing
  `checklist.md`'s shape is a matter of taste, not a defect; splitting them
  further would add spec bulk without a clearer independent check.
- **[Nit, index.md Rationale interfaces paragraph]** Fixed both parts: the
  provided-interfaces count corrected from "five items" to the workbook's
  actual six (Login code, 2FA infrastructure, Session infrastructure,
  Login/email challenge, Dashboard auditing models, Account recovery/password
  reset flow), and the phrasing smoothed to "six and three items,
  respectively, in the worked example."
- **[Nit, comics.md Panel 7 caption]** Changed "my own trouble filling in the
  table" to "trouble filling in the table" to match the third-person/
  character-facing register of the other seven captions, without contradicting
  what the panel image shows.
