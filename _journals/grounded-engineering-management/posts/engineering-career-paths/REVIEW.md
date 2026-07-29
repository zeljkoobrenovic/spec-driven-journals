# Review: Engineering Career Paths

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. This is the densest spec of the set (eight success criteria) and
the article meets all of them; the checklist is a faithful first-person
adaptation of the source PDF (verified against
`Checklist_ TSEG _ Eng Career Paths (1).pdf`), including its nested sub-lists,
which the site renderer supports. The most important thing to address is the
wobbling axis arithmetic in the "broader scoreboard" thread — "a dozen", "the
other nine", a ten-axis figure, and a fifteen-axis checklist don't quite agree.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · highlight + Rationale ¶6 + Figure 3 ↔ checklist.md · §7]** The
  axis counts don't line up: the article says "three axes of a dozen" and "the
  other nine" (internally consistent), Figure 3's alt text and caption say "ten
  career axes", and checklist §7 lists twelve axes beyond title/company/pay
  (fifteen total). Each is fine alone; together a careful reader trips. *Keep
  "a dozen" as idiom and stop counting in the figure caption, or align all
  three.*
- **[index.md · highlight, last sentence]** "isn't coaching; he's advertising" —
  the generic "he" is off-register for a journal otherwise written in the first
  person (and the advertising line already appears in [[changing-jobs]]'s
  rationale as "my coaching is advertising"). *"that's advertising" avoids both
  the pronoun and the cross-post echo.*
- **[checklist.md · §8 "Own your career development" ↔ spec.md · Non-goals]**
  §8 faithfully reproduces the PDF but is exactly the territory the spec fences
  off as "[not] [[own-your-career]]", and the article never echoes it — a
  checklist-only section that brushes a declared non-goal. *A pointer to
  [[own-your-career]] in §8 or the checklist intro resolves the tension without
  breaking source fidelity.*

### Nits

- **[index.md · Rationale ¶2]** "Tier-3 company" (hyphenated) vs the checklist's
  and Statement's "Tier 3" — pick one form.
- **[index.md · highlight]** "the tiers it doesn't pay" reads oddly — "the tiers
  it doesn't pay in" (or "at") parses cleaner.
- **[comics.md · Panel 3]** Introduces an uncast third character (the
  "salesman-like manager" with the flattering map); the cast block defines only
  VERA and ARLO. Works visually — note only if the cast list is meant to be
  exhaustive.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Company types survive | met | index.md · Statement bullet 1 (all 11 types); checklist.md · §1 |
| Ladder realism survives | met | index.md · Statement bullet 2, Rationale ¶3; checklist.md · §2 |
| Non-standard paths survive | met | index.md · Statement bullet 3, Rationale ¶4; checklist.md · §3 |
| Tiers and tradeoffs survive | met | index.md · Statement bullet 4, Rationale ¶5; checklist.md · §4–5 (per-tier detail lives here) |
| Profit vs cost center survives | met | index.md · Statement bullet 5, Rationale ¶5; checklist.md · §6 |
| Broader measures survive | met | index.md · Statement bullet 6, Rationale ¶6; checklist.md · §7 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: mostly — the article stays off the promotion campaign and
environment-adaptation records (cross-links only, all resolving:
own-your-career, promotions, changing-jobs, thriving-in-different-environments,
career-conversations). The one brush is checklist §8 against the
own-your-career non-goal (finding above) — source-driven, not authored drift.

Drift: none — spec `accepted` stands; the post delivers exactly the Intent's
"careers run on terrain" frame.

## Cross-modality alignment

- **Facts & framing:** consistent except the axis-count wobble (finding above).
  Company-type taxonomy, ladder shapes, tier structure, and profit/cost-center
  effects are identical across article, checklist, and comic.
- **Terminology:** consistent — "terrain", "flattering map", "highest realistic
  IC level", "terminal level", "full scoreboard" travel intact; comic panel
  titles reuse the article's anti-pattern names.
- **Voice & tone:** consistent — manager's voice in the article, engineer's
  first person in the checklist, per the spec's Audience section (one generic
  "he" in the highlight; finding above).
- **Coverage parity:** even for the spec's beats; checklist §8 is the one
  checklist-only section with no article echo (finding above).

## Layer-by-layer notes

### Spec

- The largest success-criteria set in this batch, but each criterion maps to one
  source section and is independently checkable — good contract discipline.
- Non-goals are well chosen (map vs. contract vs. move vs. adaptation), which is
  exactly why the checklist's §8 overlap is worth a pointer.

### index.md

- House shape fully observed; the six Statement bullets and six Rationale
  paragraphs mirror each other, and the says/does-not-say table is one of the
  best in the journal ("Cost-center work is a dead end — it can be excellent
  work; the game is different and learnable").
- "Honest maps beat flattering maps, even for retention" is the article's
  strongest paragraph and the comic's panel 7 carries it faithfully.
- All three figures exist on disk and are captioned.

### checklist.md

- Verified against the source PDF: all eight sections reproduced faithfully,
  first-personized, with the PDF's sub-lists (company types, career patterns,
  axes) preserved as nested bullets — well-formed markdown the renderer handles.
- Terminology matches the article exactly (tiers, tracks, terminal levels,
  profit/cost center).

### comics.md

- Eight panels, all image files present under
  `assets/images/engineering-career-paths/`; captions match alt text; the
  ladder-and-map metaphor is coherent from fog (panel 2) to full scoreboard
  (panel 8).
- Panel 6's two-desks contrast is an effective compression of the
  profit/cost-center rationale paragraph.

## Fixes applied (2026-07-29)

- **Verbatim self-repetition (cross-post echo)** — Highlight closing reworded to "isn't coaching; that's advertising", removing both the generic "he" and the near-verbatim echo of [[changing-jobs]]'s "my coaching is advertising".
