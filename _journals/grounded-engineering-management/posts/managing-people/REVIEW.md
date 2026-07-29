# Review: Managing People

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, internally coherent record. The "no surprises" frame carries all four
files, the spec's criteria are all satisfied, every cross-link resolves, and
every figure and comic panel image exists on disk. Publish-ready after light
polish; the most useful fix is to settle on one canonical enumeration of the
"six mechanics," which currently varies between the highlight, the Statement,
and Figure 1.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · highlight vs. Statement vs. Figure 1]** The "six mechanics" are
  enumerated three different ways. The highlight lists deliberate start, 1:1s,
  feedback, development, delegation, underperformance; the Statement's six
  bullets split 1:1 cadence from 1:1 style and merge feedback+development and
  reviews+underperformance; Figure 1's alt/caption lists reviews but not
  underperformance or 1:1 style. Same count, different members — a careful
  reader who tries to map them will stumble. *Pick one canonical six and align
  the three lists.*
- **[index.md · Statement, bullet 6]** The last bullet does triple duty —
  reviews, underperformance, and coaching out — and is roughly twice the length
  of its siblings. Coaching out is also a named spec beat, which argues for its
  own bullet. *Split into two bullets (reviews / underperformance-and-coaching-out).*

### Nits

- **[index.md · Rationale]** Figure spacing is inconsistent: Figures 2 and 3
  are followed by two blank lines, Figure 1 by one. Cosmetic in output, but
  untidy in source.
- **[index.md · What This Means in Practice, table row 5]** "Documentation is a
  trap being built" is elliptical enough to need a second read; the other
  right-column entries parse in one pass. *E.g. "Documentation means a trap is
  being built."*
- **[checklist.md · §3, last item]** "Mix formats when useful, but protect
  privacy for sensitive discussions" has no echo anywhere in the article's 1:1
  material. Fine for a source-faithful checklist, but worth knowing it is a
  checklist-only beat.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The new-report start survives | met | index.md · Statement b.1, Rationale ¶1; checklist.md §1 |
| The 1:1 mechanics survive | met | index.md · Statement b.2–3, Rationale ¶2; checklist.md §2–3 |
| Feedback, development, and delegation survive | met | index.md · Statement b.4–5, Rationale ¶3–4; checklist.md §4–6 |
| Reviews and underperformance survive | met | index.md · Statement b.6, Rationale ¶5; checklist.md §7–9 |
| Credit is explicit | met | index.md · Authoritative References (book + Chapter 4 named) |

Non-goals respected: yes — no drift into [[management-101]] contract framing,
team-level concerns, the engineer-side review view, or HR process mechanics.
Drift: none; spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — the no-surprises rule, weekly-by-default
  1:1s, rescheduled-not-skipped, the 30/60/90 plan, and the "prepared for them
  to leave" test appear identically across index, checklist, and comic.
- **Terminology:** Consistent ("no surprises," "coaching out," "delegate
  ownership, not tasks"). Only the six-mechanics enumeration wobbles (see Minor).
- **Voice & tone:** Consistent first-person declarative in index; imperative
  checklist; narrator captions in comic — all within the journal's register.
- **Coverage parity:** Even. The comic compresses the arc correctly
  (talent-myth hook → blindsided review → hoarding → no-surprises principle →
  deliberate start → 1:1s/feedback → early hard conversation → boring review).
  Checklist §3's privacy item is the only checklist-only beat (nit).

## Layer-by-layer notes

### Spec
- Clean template use; criteria are genuinely checkable (each names concrete
  beats to find in the post) rather than intent-with-a-checkbox.
- Intent is one long semicolon-chained paragraph — dense but still shorter than
  the post; acceptable.
- Modalities section correctly leaves summary/dialog unchecked; Sources names
  the exact PDF (`Checklist_ MP _ Manager.pdf`), which exists.

### index.md
- House record shape fully followed; headings in Title Case; all five
  `[[…]]` links resolve (including the cross-journal [[career-conversations]],
  correctly annotated "people journal").
- Rationale paragraphs each carry one argument with a bold lead — strong,
  low-repetition writing; "confusion is an asset with an expiry date" and
  "a small tax on trust, levied repeatedly" are earning their place.
- All three figures exist on disk and captions match their alt text.

### checklist.md
- Faithful, runnable adaptation of the chapter checklist; ten numbered
  sections, well-formed task-list markdown; terminology matches the article.
- §10 self-check is a good closer and is referenced by the article's
  "How to Read This."

### comics.md
- Eight panels, all image files present; captions match alt text; VERA/ARLO
  cast and style block consistent with the journal's other comics.
- The arc mirrors the article without introducing new claims; "boring is the
  win" closer lands the article's "makes every formal moment boring" beat.
