# Review: Product Vision and Principles

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article is well argued in the journal's
first-person register, the checklist is a faithful reproduction of the source
PDF (verified against `sources/empowered/Checklist_ PM _ Product Vision and
Principles.pdf` — all eleven sections, every item present, "3–10 years"
preserved), and the comic tells the same story with a clean eight-panel arc
and a good Panel 2/Panel 8 bookend. All three article figures and all eight
comic panel images exist under `assets/`, and all four `[[…]]` cross-links
resolve (three in-journal, one cross-journal to `grounded-engineering-executive`).
The single most important thing to address: the spec's first success criterion
asks the highlight to state the quotable phrase "principles decide the small
stuff so the vision can decide the big stuff," but that phrase lives only in
the Rationale — either fold it into the highlight or relax the criterion.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Status/Principle highlight (line 17) vs spec.md · Success criterion 1]**
  The spec requires the highlight to state both quotable phrases; "one shared
  vision, 3–10 years out, inspiring enough to recruit with" is there, but
  "principles decide the small stuff so the vision can decide the big stuff"
  appears only as the topic sentence of the last Rationale paragraph (line 49).
  The highlight conveys the substance ("decided consistently at team level
  without escalation") but not the quotable form. *Either add the phrase to the
  highlight or soften the criterion's wording; author's call.*
- **[index.md · Rationale, third paragraph ("A vision nobody sells…", line 45)]**
  The heaviest paragraph in the post: it carries four beats in one block —
  ownership (head of product / design & tech leadership / CEO), communication
  craft, the visiontype/storyboard/video artifacts, and recruiting. Each beat is
  good; together they overload one paragraph while the neighbors carry one beat
  each. *Consider splitting ownership from communication-and-recruiting.*
- **[index.md · Rationale, second paragraph (line 40)]** Serial independent
  clauses joined by commas: "I prefer sharing the vision over sharing detailed
  roadmaps, I avoid locking into promises too early, and when…" — reads as a
  comma splice until the "and" arrives. *Semicolons, or "I prefer … and avoid
  …".*
- **[comics.md · panel arc]** Two spec-level beats have no echo in the comic:
  validation / "reasoned leap of faith" (spec Success criterion 5) and explicit
  ethics (part of criterion 4, and in the article's highlight: "including the
  ethical ones"). Eight terse panels cannot carry everything, and the primary
  obligation falls on `index` (which carries both) — but ethics is load-bearing
  enough that Panel 6's guardrails caption could nod to it. *Optional: mention
  ethics in the Panel 6 caption; accept the validation omission.*

### Nits

- **[comics.md · Panel 8 caption (line 32)]** Double terminal punctuation:
  "…'where is this going?'." — drop the trailing period.
- **[checklist.md · Build the Right Ownership (line 38)]** "Involve the design
  closely in shaping the vision" is awkward English ("the design" → "design" or
  "design leadership"). It is verbatim from the source PDF, and the spec asks
  for the checklist to survive intact — but note the file already normalizes
  the PDF's "vision type" to "visiontype" (line 47), so light normalization has
  precedent. Author's call which fidelity wins.
- **[index.md · lines 27, 64, 66]** Hyphenation drift in the retelling motif:
  "re-telling" (Statement) vs "Retell … retell" (table row) — pick one form.
  ("Re-communicate" is used consistently in both index and checklist.)

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | partial | index.md · highlight has phrase 1; phrase 2 only in Rationale (line 49) |
| North-star role explicit | met | index.md · Statement bullets 1 & 3, Rationale ¶1, Figure 1, practice table |
| The horizon survives | met | index.md · Rationale ¶2, Figure 2, practice table, anti-patterns ("roadmap in a gown", "vision sprawl") |
| Principles carry weight | met | index.md · Rationale ¶5, Figure 3; checklist.md · sections 9–10 |
| Validation is honest | met | index.md · Rationale ¶4; checklist.md · Validate the Vision Appropriately |
| Checklist survives intact | met | checklist.md · all 11 PDF sections verified against the source PDF; "3–10 years" preserved (section numbering dropped per journal-wide convention) |
| Credit is explicit | met | index.md · Authoritative References (Cagan & Jones, svpg.com) |

Non-goals respected: yes. No vision-template content; the
[[customer-journey-vision]] boundary is drawn explicitly in How to Read This
and Related Records; strategy is delegated to [[empowered-product-strategy]];
the roadmap is treated as a boundary, not replaced.

Drift: none substantive. Spec `status: accepted` is fair; the one partial
criterion above is a wording-level gap, not a direction change.

## Cross-modality alignment

- **Facts & framing:** Consistent — "3–10 years," one shared vision, no
  per-team visions, strategy/architecture/topology steering by the star, and
  the unused escalation ladder all match across article, checklist, and comic.
  Figure 1 (three ships toward a star) and Panel 5 depict the same image.
- **Terminology:** Consistent — "north star," "guardrails" (Figure 3 caption ↔
  Panel 6 caption), "reasoned leap of faith" (index ↔ checklist), "visiontype"
  normalized the same way in index, checklist, and spec.
- **Voice & tone:** Consistent — first-person declarative in the article,
  imperative checklist per journal convention, VERA/MILA cast in the comic
  matching the journal's shared cast block.
- **Coverage parity:** Nearly even. The comic skips the validation and ethics
  beats (see Minor finding); the checklist covers everything the article
  argues, and the article introduces nothing the checklist lacks.

## Layer-by-layer notes

### Spec

- Follows the template fully: Intent, Audience, Success criteria, Non-goals,
  Modalities, Open questions, Decision log, Sources, Changelog all present and
  short. Criteria are checkable; no bloat; no dangling open questions.
- The Decision log's boundary entry ([[customer-journey-vision]] vs Cagan's
  pairing) is genuinely useful and is honored in the article verbatim.
- Modalities checkboxes match the files on disk (checklist + comics present,
  summary/dialog absent per journal policy).

### index.md

- House record shape intact: status highlight, Statement → How to Read This →
  Rationale → What This Means in Practice → Anti-Patterns → Related Records →
  Scope and Revisiting → Authoritative References. Headings in Title Case;
  "What This Means in Practice" matches the other 14 posts in this journal.
- All three figures exist and are captioned; the says/does-not-say table is a
  strong compression of the argument; the seven anti-patterns each map to a
  Rationale beat ("The roadmap in a gown" is a memorable coinage).
- The five Rationale paragraphs have bolded topic sentences that could be read
  alone as a summary — good skimmability. The third paragraph is the one that
  overloads (see Minor finding).
- `status: draft:gray` with **Status: DRAFT** matches all 15 posts in the
  journal — a journal-wide state, not a per-post inconsistency.

### checklist.md

- Verified line-by-line against the source PDF: all eleven sections, all items,
  same order, "3–10 years" bolded and preserved. Section numbering dropped,
  matching every sibling checklist in the journal.
- Two deliberate-looking normalizations from the PDF: "vision type" →
  "visiontype" (Cagan's term) — fine; "Involve the design closely" kept
  verbatim — see nit.
- The italic pointer line to the Article tab matches the journal's convention.

### comics.md

- Eight panels, correct arc for the form: hook (fragmentation) → problem
  (recruiting silence) → principle → boundary (not a roadmap) → north star →
  guardrails → retelling → closer. The "where is this going?" bookend between
  Panels 2 and 8 is the comic's best move.
- All eight referenced images exist under
  `assets/images/product-vision-and-principles/`; alt text matches captions;
  the cast/style comment block matches the journal's VERA/MILA convention.
- Captions are one line each and follow the label pattern ("The hook:",
  "The principle:", …) — fits the modality's terseness bar.

## Fixes applied (2026-07-29)

- **[minor · index.md highlight vs spec criterion 1]** Fixed — folded "the
  principles decide the small stuff so the vision can decide the big stuff"
  into the highlight's principles sentence (phrase also retained as the
  Rationale ¶5 topic sentence); spec criterion now met as written, so spec
  untouched.
- **[minor · index.md Rationale ¶3 overload]** Fixed — split into two
  paragraphs: "The vision needs real owners, all the way to the top."
  (ownership) and "A vision nobody sells is a document, not a tool."
  (communication craft, artifacts, recruiting).
- **[minor · index.md Rationale ¶2 comma splice]** Fixed — "I prefer sharing
  the vision over sharing detailed roadmaps and avoid locking into promises
  too early; when a forward-looking commitment…".
- **[minor · comics.md missing ethics/validation beats]** Fixed (partial, per
  reviewer suggestion) — Panel 6 caption now reads "…small trade-offs —
  including the ethical ones — so nothing needs to escalate" (caption only,
  no image regeneration); validation omission accepted as recommended.
- **[nit · comics.md Panel 8 double punctuation]** Fixed — dropped the
  trailing period after "'where is this going?'".
- **[nit · checklist.md "Involve the design closely"]** Skipped — verified via
  pdftotext that the source PDF reads "Involve the design closely in shaping
  the vision" verbatim; PDF fidelity wins, wording kept.
- **[nit · index.md hyphenation drift]** Fixed — "re-telling" → "retelling"
  in the Statement bullet, matching "retell" in the practice table and the
  comic's "The retelling" label.
