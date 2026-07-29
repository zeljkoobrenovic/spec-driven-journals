# Review: Career Conversations

**Reviewed:** 2026-07-28 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, well-aligned post: the load-bearing facts (60/30–45 minutes,
the exactly-one-day-before reminder, the two-to-three development goals) are
consistent across spec, article, checklist, and comic, and the checklist reads
as genuinely runnable. The one substantive problem is a small but real
cross-modality drift the different-author risk predicted: the checklist adds
"consulting" to the five-years-out type-of-work list where the spec and
article both list seven items without it. Fix that one line and this is
publish-ready.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Major
- **[checklist.md · §3, "Five years out" bullet, line 29]** Lists the
  type-of-work options as "management, research, execution, leadership,
  communication, analytics, problem-solving, **consulting**" — an eighth item
  not present in spec.md (line 50) or index.md (lines 27, 49), both of which
  list exactly seven. Since the checklist was written by a different author,
  this reads as an unreviewed addition rather than a deliberate expansion.
  *Either drop "consulting" from the checklist or add it to the spec and
  article so the list matches everywhere.*

### Minor
- **[spec.md front matter vs index.md front matter]** spec.md declares
  `status: accepted` (line 2) but index.md's front matter is `status:
  draft:gray` (line 3) and the visible highlight reads `**Status**: DRAFT`
  (line 15). This is a journal-wide convention (every post in
  `grounded-people-management-tools` ships `draft:gray` regardless of its
  spec status), so it isn't unique to this post — but it is the kind of
  mismatch a reader comparing spec to post would flag. *Worth a one-line
  journal-level decision on whether front-matter `status` should ever track
  the spec, or is understood to always read `draft` pre-launch.*
- **[checklist.md · §1 "Setup", line 10]** "Frame it as a get-to-know-you
  conversation: their past career moves and a start on future development
  goals" undersells the article's actual framing. index.md (line 40) frames
  the announcement as "these are among my favorite conversations" — a warmer,
  more specific line that does real work in the article's Rationale section
  but has no echo in the checklist's script. Not wrong, just thinner than the
  source it's supposed to operationalize. *Consider folding the "favorite
  conversations" framing into the checklist script since it's a scripted
  line the manager is meant to say aloud.*

### Nits
- **[checklist.md · §1, line 8]** "someone early in their career" vs.
  index.md/spec.md's consistent "fresh out of school" — same meaning,
  different phrase. Minor terminology variance, not confusing, but the two
  authors' word choices show here.
- **[index.md · line 30 vs. line 65]** Figure 1 and Figure 3 both show a
  version of the conversation arc/loop (five-part loop vs. arc-to-goals);
  not a problem, but the two diagrams cover adjacent ground and a reader
  skimming captions only may not immediately see what distinguishes them.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight blockquote, line 17 |
| The mechanics survive (60/30–45 min, announce before scheduling, one-day-before reminder, no prep, résumé optional) | met | index.md Statement (lines 23–27) and checklist.md §1–2 |
| The conversation structure survives (history walk, five-years-out by type of work) | met, with the "consulting" discrepancy noted above | index.md Rationale (lines 47, 49); checklist.md §3 |
| The "why" discipline is explicit | met | index.md line 47, "What This Means" table line 59; checklist.md §3 intro line 22 |
| The wrap-up survives (recap, share notes, 2–3 goals, reference later) | met | index.md lines 62, 65; checklist.md §4–5 |
| Credit is explicit (Claire Hughes Johnson, Scaling People) | met | index.md "How to Read This" (line 34) and Authoritative References (line 90) |

Non-goals respected: yes. No modality claims the five-year projection is a
commitment (index.md line 75 anti-pattern, checklist.md line 18 explicit
disclaimer); no modality folds this into the weekly 1:1 or performance-review
cadence; `[[performance-reviews]]` and `[[coaching]]` are both correctly
scoped as separate, non-overlapping records in the Related Records section.

Drift: none beyond the checklist's single added list item noted above — not
enough on its own to warrant `status: drifted`, but worth fixing before it
compounds.

## Cross-modality alignment

- **Facts & framing:** consistent — 60/30–45 minutes, exactly-one-day-before
  reminder, "type of work not title," 2–3 development goals, and the
  no-commitment framing for the five-year answer all match across index,
  checklist, and comics.
- **Terminology:** consistent, with the one flagged addition ("consulting" in
  checklist.md only) and one minor phrasing variant ("fresh out of school"
  vs. "early in their career").
- **Voice & tone:** consistent given the form — checklist.md is
  appropriately terser and second-person-instructional, comics.md is
  appropriately visual-first, index.md carries the first-person rationale.
  No voice contradicts another.
- **Coverage parity:** even. Every load-bearing beat in index.md (early
  scheduling, pre-announcement, one-day reminder, no-prep/résumé-optional,
  history-walk structure, five-years-by-type-of-work, wrap-up goals,
  later-reference) appears in checklist.md. comics.md compresses to the
  highest-leverage beats only (thin context, status-only 1:1s, surprise
  hold, the tool, announce-then-remind, five-years-by-type, ask-why-not-
  diagnose, referenced-later) and correctly omits the no-prep/résumé detail
  as too granular for 8 panels — appropriate compression, not a gap.

## Layer-by-layer notes

### Spec
- Clean MADR-adjacent shape; all eight template sections present and none
  bloated. Success criteria are genuinely checkable (each names a concrete
  mechanic — timing, duration, list of work-types) rather than restating
  Intent as a checkbox.
- Non-goals are precise and do real disambiguating work, especially the
  `[[coaching]]`/`[[staffing]]` boundary against the product-management
  journal.
- Decision log and Changelog are both current and specific (names the
  practitioner-lens framing choice and the comics staging step).

### index.md
- Follows house record shape exactly: Status/Principle highlight →
  Statement → How to Read This → Rationale → What This Means in Practice →
  Anti-Patterns → Related Records → Scope and Revisiting → Authoritative
  References.
- Three figures are well-placed and each caption explains what the figure
  adds rather than restating the paragraph above it.
- All four `[[…]]` cross-links (`performance-reviews`, `manager-transitions`,
  `coaching`, `staffing`) resolve to existing posts (verified against
  `grounded-people-management-tools` and `grounded-product-management`
  configs).
- Rationale section runs slightly long in the "why" paragraph (line 47) —
  it re-explains the history-walk logic that the Statement bullet (line 27)
  already stated; not wasted (it's the required elaboration on why the
  mechanic works), but a reader who reads both bullet and paragraph gets the
  point twice.

### checklist.md
- Genuinely operational: every line is an action a manager can execute in
  order, phrased as scripted talking points where it matters (the reminder
  restatement, the five-year framing).
- Mirrors the article's five stages faithfully (Setup → Reminder →
  Conversation → Wrap-up → Afterward), a clean superset of the article's
  five-part Statement loop plus the "Afterward" follow-through the article
  covers in its "What This Means" table.
- The "consulting" addition (flagged above) is the one place the
  different-authorship shows as a factual drift rather than just phrasing.

### comics.md
- Eight panels, each with alt text and a one-line italic caption; captions
  do not simply restate the alt text — they add the interpretive point
  ("the hook," "the problem," "the wrong way," etc.), which is the right
  division of labor for this form.
- All eight referenced panel image files exist in
  `assets/images/career-conversations/`.
- Visual metaphor (VERA the seasoned executive, NOA the first-time manager)
  stays consistent panel to panel and matches the cast note in the HTML
  comment block.
- Comic's closing beat ("one deliberate hour, referenced months later, pays
  back for years," panel 8) directly echoes the spec's load-bearing
  sentence and index.md's principle — good coverage of the single most
  important idea in the terminal panel.

## Fixes applied (2026-07-28)

- Type-of-work list: polarity inverted — the source workbook includes "consulting", so it was added to the article and spec (the checklist already had it).
- Checklist Setup now carries the "among your favorite conversations" framing and matches the article's "fresh out of school" phrasing.
- Spec-vs-front-matter status (minor): skipped — `spec: accepted` with `post: draft:gray` is the journal-wide convention.
