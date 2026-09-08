# Review: Introduction: Security as Records

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, summary.md, dialog.md

## Verdict

A publish-ready opener that does exactly what the spec asks: the charter is
stated in first person, the single-source structure (24 chapter checklists,
credit per record) is explicit, the Map links all 24 records in exactly the
config.yaml section order with the seams named in both directions, and the
reading guide covers all five audiences. All five success criteria are met,
every `[[link]]` resolves against the journal's slug set, both sibling-journal
relative links point at real journals, and the record-shape table names the
Checklist, TL;DR, and Conversation tabs without promising the not-yet-built
Comic tab. The only real defect found: the summary ran 524 words against the
journal's 300–500 band — now trimmed.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[summary.md · whole file]** 524 words, over the journal's 300–500 band
  for the TL;DR tab. The overrun sat in restatement (the five section names
  appear in the map bullet and again in full in the source bullet; "can read
  … and have" constructions). *Trim ~25 words without losing a commitment.*

### Nits

- **[summary.md · "What it costs" bullet 1]** "Written commitments are
  inspectable…" reads as a benefit filed under costs; the cost is that the
  public bar binds the author. *Reword to lead with the binding, not the
  inspectability.*
- **[dialog.md · whole file]** Ben addresses Ana as the author ("You run
  engineering…", "If you believe this stuff"), while Ana refers to "the
  author" / "this executive" in third person. This mixed register is the
  established family pattern (the grounded-platforms introduction dialog does
  exactly the same), so noted for awareness only.
- **[index.md · front matter `excerpt`]** The excerpt reprises the first KEY
  POINTS bullet nearly verbatim — the journal family's established pattern
  (grounded-platforms introduction does the same); noted only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Charter stated (operating model, first person, revisiting conditions) | met | index.md · KEY POINTS bullet 3 + "Why an Executive Writes…" + "Status and Revisiting" |
| Single-source structure explicit (24 checklists as ground truth, credit per record) | met | index.md · "Where the Material Comes From" |
| Map lists every record with `[[slug]]` links and names the seams | met | index.md · "The Map" — all 24 records, config order; seams paragraph runs both directions |
| Reading guide works for each audience | met | index.md · "How to Read This Journal" — all five audiences |
| Credit explicit (book + all three authors) | met | index.md · Authoritative References |

Non-goals respected: yes — no book summary, no risk-register/threat content,
sibling journals pointed at rather than covered. Modalities match the spec
(no checklist by design; comics deferred). Spec `status: accepted` is
correct; no drift.

## Cross-modality alignment

- **Facts & framing:** consistent — 24 records, five sections, draft-to-
  accepted lifecycle, "decided before the incident, in writing — or during
  the incident, in panic," and the risk-acceptance entitlement appear
  identically in article, summary, and dialog.
- **Coverage parity:** even; the dialog additionally carries the
  draft-status defense and the "book club with extra formatting" objection —
  both consistent with the article's claims.
- **Voice:** first-person-executive in article and summary; the dialog's
  third-person wobble is the family pattern (see Nits).

## Layer-by-layer notes

### Spec

- Well-formed against the template; the two decision-log entries (journal
  creation; five thematic sections over chapter order) capture the real
  structural decisions.

### index.md

- Map cross-checked against `config.yaml`: six config sections, the five
  post-intro sections reproduced with identical membership and order; all 24
  non-intro records linked exactly once in the Map.
- KEY POINTS follows the three-bullet essay-shape rule; `status: draft:gray`
  with no visible DRAFT banner matches the sibling journals' introduction
  convention (KEY POINTS posts carry no Status highlight).
- No icon/logo front matter, no image references — correct for the journal's
  current text-only stage.

### summary.md

- On form (lead, What changes, What it costs, What we are not doing, closing
  italics); over-length fixed, see below.

### dialog.md

- Ben's objections are the real ones (CISO delegation, one-page policy,
  book-report charge, why `draft`); Ana's answers carry the article's actual
  arguments and close on the charter line. No contradictions with article or
  summary.

## Fixes applied (2026-08-22)

- **[minor · summary.md]** Trimmed from 524 to ~500 words: author list
  shortened to "Brotherston, Berlin, and Reyor's", the duplicated five-section
  enumeration dropped from the source bullet (the map bullet retains the
  claim), "The introduction lists" → "Every record is listed", "my peers can
  read … and have the whole model" tightened, plus two single-word trims. No
  commitment removed.
- **[nit · summary.md "What it costs"]** First cost bullet reworded to "The
  commitments are binding once written: …" so it reads as a cost
  (accountability), not a benefit.
- **[nit · dialog.md voice]** Skipped — established family pattern across the
  grounded journals' introduction dialogs.
- **[nit · index.md excerpt]** Skipped — established house pattern.
