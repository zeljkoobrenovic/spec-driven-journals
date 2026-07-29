# Review: Compensation Conversations

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a solid, well-grounded record — the workbook source (pages 111–112) is
faithfully distilled, the five-part Statement and three-phase outline survive
intact across the article and the checklist, and every image reference (3
figures, 8 comic panels, 1 logo) resolves to a real file. The most important
thing to address before treating this as publish-ready is the Statement vs.
Rationale near-duplication in `index.md` (the "stay in the room" beat is
restated almost verbatim rather than developed), and the spec's Non-goals
section over-claims a `[[career-conversations]]` boundary it never actually
lists as a non-goal, while the post cross-links to it as a "Related Record."

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

None.

### Major

- **[index.md · Statement bullet 5 vs. Rationale para. 4]** The "stay in the
  room" idea is stated almost word-for-word twice: bullet 5 ("I expect
  emotion, I own the result, and I empathize without apologizing for it or
  promising a future I can't guarantee") and the Rationale paragraph beginning
  "When expectations don't align, my job is to stay, not to soften" repeat the
  same clause structure and near-identical phrasing rather than the Rationale
  adding new reasoning the way the other four Rationale paragraphs do relative
  to their Statement bullets. *Rework the Rationale paragraph to argue* why
  *staying matters (trust cost of softening) rather than re-listing* what *to
  do, which the Statement already covered.*

### Minor

- **[spec.md · Non-goals]** Lists three explicit non-goals
  ([[performance-reviews]], [[managing-underperformance]],
  [[careers-and-performance]]) but the post's Related Records adds a fourth
  cross-link, [[career-conversations]], with no corresponding non-goal entry
  explaining the boundary. Not wrong, but the spec's Non-goals section doesn't
  fully anticipate the post's actual link set. *Add a short non-goal line for
  career-conversations, or drop the link if the boundary isn't worth stating.*
- **[index.md · "What This Means in Practice" table, row 4]** "Owning the
  result means apologizing for it or promising a different future outcome."
  restates the same "don't apologize / don't over-promise" pairing a third
  time (after Statement bullet 5 and the Rationale paragraph flagged above).
  Each individual restatement is house-style (Statement → Rationale → table →
  Anti-Patterns is the journal's normal pattern), but this specific beat gets
  four total passes (Statement, Rationale, table, Anti-Patterns) versus two or
  three for the others. *Consider tightening the table row to the "what it does
  not say" contrast only, without re-deriving the whole rule.*
- **[checklist.md · section 7 vs. workbook]** The workbook page 112 includes a
  "Notes" field alongside the outline; the checklist's "After the conversation"
  section captures the follow-up and continuity intent but doesn't explicitly
  carry a "capture notes for the next cycle" line distinct from "record what was
  discussed" (which is close but slightly different from a running notes field).
  Very small gap against the source, not against the spec. *Optional: fold a
  one-line "keep notes I can reuse next cycle" bullet in if closer workbook
  parity is wanted.*

### Nits

- **[index.md · Rationale, "Owning the message means flexing..." paragraph]**
  "I usually don't know which one I'll need until the conversation starts" is
  slightly informal against the surrounding declarative register (only place
  in the article using "usually" as a hedge). Minor tone wobble, not worth more
  than a glance.
- **[comics.md · Panel 7 alt text vs. caption]** Alt text says "not apologizing"
  while the caption says "without apologizing or over-promising" — caption adds
  the over-promising beat the alt text omits. Both are accurate, just not
  perfectly mirrored; group with other alt/caption phrasing nits if a pass is
  done later.
- **[checklist.md · heading 4–6 numbering]** "Run the conversation — Phase 1/2/3"
  headings restate "Run the conversation" three times in a row where a reader
  is already inside that block; a shared parent heading ("6. Run the
  conversation") with sub-bullets Phase 1/2/3 would read slightly cleaner, but
  the current form still parses fine and mirrors the workbook's own three-part
  outline structure.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (own the message, not "the system decided") | met | index.md · highlight blockquote, Statement bullet 1, Anti-Patterns first entry |
| Individual-level prep is explicit (career stage, last uplevel, last increase, likely expectation) | met | index.md · Statement bullet 2, Rationale para. 2; checklist.md · section 2 table + bullets |
| Three-phase outline survives (understanding → outcome → discussion) | met | index.md · Statement bullet 4; checklist.md · sections 4–6, in that order |
| Hard-conversation guidance is precise (own the result, empathize, don't apologize, don't promise unguaranteeable futures) | met | index.md · Statement bullet 5, Rationale para. 4, table row 4, Anti-Patterns; checklist.md · section 3 |
| "Communicate even when nothing changes" and "say I don't know" survive as distinct commitments | met | index.md · Rationale para. 5, table rows 5–6, Anti-Patterns; checklist.md · section 3 and Phase 1/2 |
| Checklist reproduces workbook mechanics (timeline/resources, individual prep fields, three-phase outline as running sections) | met | checklist.md · sections 1, 2, 4–6 |

Non-goals respected: yes for the three named ([[performance-reviews]],
[[managing-underperformance]], [[careers-and-performance]]) — the post keeps
to delivering the outcome and doesn't drift into calibration, written review
content, or the underperformance path. One gap noted above: the post links
[[career-conversations]] without the spec having anticipated that boundary
(minor, not a breach of stated non-goals since none was violated — just an
incomplete list).

Drift: none material. All six success criteria are met. The minor Non-goals
gap doesn't rise to `status: drifted` — it's an omission in the spec's list,
not a contradiction between spec and post.

## Cross-modality alignment

- **Facts & framing:** consistent. The five-part operating model, the four
  individual-prep fields, and the three-phase outline appear identically
  across index.md, checklist.md, and comics.md with no contradicting details.
- **Terminology:** consistent. "Own the message" / "own the result," "check for
  understanding / describe the outcome / open it up for discussion," and "I
  don't know... circle back" are used with the same wording in all three files.
- **Voice & tone:** consistent for the article and checklist (first-person,
  declarative, matches the journal's other posts). Comics.md is appropriately
  terser and third-person-narrated (VERA/NOA), which is the modality's normal
  register, not a drift.
- **Coverage parity:** even. All eight comic panels map cleanly onto load-bearing
  beats from the article (unexplained number → system-decided → guessing →
  individual prep fields → three-phase outline → "I don't know" → own it,
  don't soften it → trust earned in person), and the checklist's seven sections
  cover the same ground operationally. No modality introduces a beat absent
  from the others.

## Layer-by-layer notes

### Spec

- Follows the template exactly: Intent, Audience, Success criteria, Non-goals,
  Modalities, Open questions (empty, correctly so), Decision log, Sources,
  Changelog all present and in order.
- Success criteria are genuinely checkable — each names a specific phrase or
  structural element to verify, not vague intent restated with a checkbox.
- Not bloated: comparable in length to the post's Statement + Rationale, no
  accreted duplication.
- One internal gap: Non-goals lists three boundary records but the post's
  Related Records section links a fourth ([[career-conversations]]); see Minor
  finding above.

### index.md

- Follows house record shape fully: Status/Principle highlight, Statement →
  How to Read This → Rationale → What This Means in Practice → Anti-Patterns →
  Related Records → Scope and Revisiting → Authoritative References, matching
  performance-reviews.md's section order exactly.
- All three figure images resolve; captions are informative and distinct from
  each other.
- All four `[[…]]` cross-links resolve to real permalinks (performance-reviews,
  managing-underperformance, careers-and-performance in the sibling
  grounded-engineering-executive journal, career-conversations).
- The Statement-Rationale-table-Anti-Patterns quadruple restatement pattern is
  the journal's norm, but the "stay in the room / don't apologize" beat gets
  more verbatim repetition than the other four beats — see Major finding.

### checklist.md

- Faithfully reproduces the workbook's structure section by section: timeline
  and resources, individual prep (with a genuinely useful per-person table),
  "be prepared to own the message," and the three-phase outline as its own
  numbered sections, plus an added "after the conversation" follow-up section
  that isn't in the workbook but is a reasonable operational extension.
  Sentence-case headings match the journal convention.
- Checkbox items are concrete and runnable — each is something a manager can
  literally tick off before or during a conversation, not restated principle.
- Small gap against the workbook's "Notes" field (see Minor finding); not
  spec-mandated, so not a real deficiency.

### comics.md

- Eight panels, each with a one-line caption under 25 words — fits the
  modality's terse form well.
- Visual metaphor is consistent panel to panel (the system-box motif in Panel
  2 versus Panel 8's "system box small and off to the side" is a nice visual
  callback showing the arc).
- All eight referenced panel image files exist under
  `assets/images/compensation-conversations/`.
- One small alt-text/caption mismatch in Panel 7 (see Nit above); otherwise
  alt text and captions agree throughout.

## Fixes applied (2026-07-29)

- **[Major, index.md Rationale]** Reworked the "stay in the room" Rationale
  paragraph to argue *why* staying matters (softening costs more trust than
  a plain delivery; an apology implies the process was wrong, a hedged
  promise spends credibility on an outcome that isn't guaranteed) instead of
  re-listing the Statement's "own it / don't apologize / don't promise"
  clause structure.
- **[Minor, spec.md Non-goals]** Added a `[[career-conversations]]` non-goal
  line so the spec's Non-goals section anticipates the post's fourth
  Related Records link.
- **[Minor, checklist.md §7]** Added a "keep notes I can reuse next cycle"
  bullet to After the conversation, carrying the workbook's Notes field
  forward as its own line distinct from "record what was discussed."
- **[Nit, comics.md Panel 7]** Aligned alt text with the caption by adding
  "or over-promising" — wording is true regardless of what the drawn panel
  shows, so no image regeneration needed.
- **[Nit, index.md Rationale "usually" hedge]** Skipped — the review flagged
  this as a minor tone wobble not worth more than a glance; leaving as-is
  per the brief's scope (not one of the four requested fixes, and too small
  to warrant an independent edit).
- **[Nit, checklist.md headings 4–6]** Skipped — restructuring "Run the
  conversation — Phase 1/2/3" into a shared parent heading with sub-bullets
  is a structural reorganization beyond the four requested fixes and the
  review itself calls the current form acceptable ("still parses fine").
- **[Minor, index.md practice-table row 4]** Skipped — not one of the four
  requested fixes; the review itself notes each individual restatement is
  house-style, and the Rationale rework above already reduces the repeat
  count for this beat.
