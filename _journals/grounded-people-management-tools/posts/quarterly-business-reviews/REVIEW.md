# Review: Quarterly Business Reviews

**Reviewed:** 2026-07-28 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, tightly-grounded record — the six post-meeting truths, the
five delivery rules, and the document's hard limits survive intact and
consistently across all four files, and every `[[cross-link]]` and comic
panel image resolves. It is close to publish-ready. The one thing worth
fixing before calling it done: **checklist.md** item 2's "Be concise —
six-page narrative maximum" conflates the six-page *document* limit with the
two-page *narrative section* limit defined a few sections later in the same
file — a reader working section 2 in isolation gets the wrong number.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Blockers

None.

### Major

- **[checklist.md · section 2, "Be concise" bullet, line 20]** "Six-page
  narrative maximum" is imprecise: the six-page limit applies to the whole
  document, but the *narrative* section itself is capped at 2 pages (stated
  correctly in section 6's table and section 6's own checkbox at line 64).
  As written, a leader skimming section 2 could believe the narrative alone
  gets six pages. *Reword to "six pages total" or "document limited to six
  pages," reserving "narrative" for its own 2-page rule.*

### Minor

- **[comics.md · Panel 2 vs. Panel 3]** Two consecutive panels both attack
  "no pre-read / slides instead of a memo" — panel 2's caption ("the room
  narrates instead of discusses") and panel 3's caption ("a slide deck
  substitutes performance for rigor") land close enough to the same beat
  that the comic spends 2 of its 8 panels on one anti-pattern before the
  principle panel (4) even arrives. *Consider tightening panel 2 or 3, or
  differentiating the visual beat more sharply (timing vs. medium).*
- **[index.md · "Rationale" section]** The two-year-horizon paragraph
  (line 48) and the "Six statements" bullet (line 24) both restate "are we
  on track for where we said we'd be in two years" almost verbatim, and the
  opening Principle blockquote (line 17) states it a third time. Each
  instance earns its place contextually, but a reader moving straight
  through the article hits the same clause three times in the first page.
  *Fine as reinforcement of the quotable line, but worth a read-through to
  confirm it doesn't read as padding.*

### Nits

- **[comics.md · header line 1]** "in eight panels" — matches the sibling
  posts' convention exactly (verified against writing-okrs, team-charter,
  leadership-team-updates), no change needed; noting only because it's the
  kind of line worth double-checking on every new comic and this one passes.
- **[checklist.md · line 122 heading]** "top 5–10 goals, one page maximum"
  duplicates the table's own row-count intent — the table below only ships
  5 rows (Objective 1–5), which is correct as a fill-in template (leader
  adds rows up to 10), but a first-time user could read the 5 fixed rows as
  the hard cap rather than a floor. *Consider a one-line note that rows can
  be added up to 10, mirroring the appendix note pattern used elsewhere in
  the file.*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (two-year question + "candid assessment, not a summary of successes") | met | index.md · Status/Principle blockquote (line 17) |
| Six post-meeting truths survive | met | index.md · "Six statements" bullet (line 24) and Rationale (line 46); checklist.md · section 1 |
| The numbers survive (6 pages, ≤250 words, ≤2-page narrative, ≥50% strategy/outlook, ~2-year horizon, top 5–10 goals, ≥24h pre-read, reading time) | met, with one internal wording slip | index.md throughout; checklist.md sections 6–7 (see Major finding on "six-page narrative maximum" in section 2) |
| Document outline and tables survive (narrative, metrics, P&L, cross-functional focus areas, goal scoring, Appendix A tables) | met | checklist.md sections 6, 9–11 |
| Credit is explicit (Claire Hughes Johnson + Kailey Stockenbojer) | met | index.md · "How to Read This" (line 35) and "Authoritative References" (line 92–94) |

Non-goals respected: yes — no modality drifts into OKR-writing mechanics
([[writing-okrs]]), the lightweight update cadence ([[leadership-team-updates]]),
charter definition ([[team-charter]]), or metrics-design guidance
([[measuring-engineering-organizations]]); all four are correctly cited as
inputs/adjacent records, not redefined here.

Drift: none. Spec `status: accepted` is warranted — the one wording slip in
checklist.md is a phrasing bug, not a substantive departure from the spec's
intent, so it does not rise to `drifted`.

## Cross-modality alignment

- **Facts & framing:** consistent. All four files agree on the six
  post-meeting truths, the five delivery rules, the 250-word/2-page/6-page
  limits, the ≥24-hour pre-read, and the two-year metric horizon.
- **Terminology:** consistent, with one internal (not cross-modality) slip —
  see the Major finding on checklist.md's "six-page narrative" phrasing.
- **Voice & tone:** consistent first-person declarative register across
  spec, article, and checklist; comics.md's captions compress the same
  claims without introducing new framing.
- **Coverage parity:** even. Every load-bearing beat in index.md (document-
  as-artifact, six truths, candor, concision, two-year horizon, closing the
  loop) has a corresponding checklist section and a corresponding comic
  panel (panels 4–8 map directly onto the article's five Rationale
  paragraphs plus the closing-the-loop point).

## Layer-by-layer notes

### Spec

- Clean MADR-adjacent structure; all template sections present and used.
- Success criteria are genuinely checkable (each cites a specific mechanic,
  not vague intent prose) — this is a well-built contract.
- Sources section correctly attributes the internal workbook chapter and
  page range (pp. 30–41) and the external book; Decision log records the
  "written document as load-bearing artifact" framing choice clearly.
- No bloat; at 731 words it is proportionate to a ~2,076-word article.

### index.md

- Opens with the required Status/Principle highlight; body follows the
  house MADR order (Statement → How to Read This → Rationale → What This
  Means in Practice → Anti-Patterns → Related Records → Scope and
  Revisiting → Authoritative References) with no sections out of order.
- Figures (3) are captioned and numbered correctly, each paired with prose
  that motivates it rather than merely decorating.
- Section headings are in Title Case per house convention.
- All six `[[cross-links]]` under Related Records resolve to existing posts
  (writing-okrs, leadership-team-updates, team-charter,
  measuring-engineering-organizations, inspected-trust, unblocking-process).
- Minor repetition of the "two years" framing across three spots (see Minor
  finding above) — reinforcement more than redundancy, but worth a skim.

### checklist.md

- Fully operational: 13 numbered sections mirror the workbook's before/
  during/after structure plus the document outline, appendix tables, and
  retrospective — nothing from the spec's "document outline and tables"
  criterion is missing.
- Checkbox items are genuinely actionable (each names a concrete action,
  not a restated goal).
- The section-2 "six-page narrative maximum" phrasing is the one
  substantive issue found in this review (see Major).
- Table shapes (progress-on-goals, focus-area scoring, Appendix A) match
  the article's description one-for-one.

### comics.md

- 8 panels, matches sibling posts' convention and the spec's Modality
  checkbox.
- Cast (VERA/NOA) and style block match the shared journal-wide cast
  definition verified against writing-okrs, team-charter, and
  leadership-team-updates comics.md files.
- All 8 referenced panel image files exist on disk under
  `assets/images/quarterly-business-reviews/`.
- Captions are short and match their alt text and the article's beats;
  panel 6 correctly compresses the three numeric limits (250 words, 2
  pages, 6 pages) into one caption.
- Panels 2 and 3 sit close together thematically (see Minor finding) — the
  comic could tighten to leave more room for the six-truths payoff, though
  eight panels is the house standard and not overlong.

## Previous review

*(No prior REVIEW.md existed for this post — first review.)*
