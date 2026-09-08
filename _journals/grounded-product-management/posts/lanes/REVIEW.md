# Review: Lanes

**Reviewed:** 2026-08-14 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong record: the reframing of the pyramid critique as a consequence of "where
the work happens," and the explicit reconciliation with [[outcomes]]'s pyramids
(causal model vs roll-up, with the removal test), give it a clear argumentative
spine. Publish-ready. The most useful fix: back the checklist's ownership item
and the Statement's cross-team-lanes claim with a sentence of rationale each, so
neither modality carries an obligation the article never argues.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Minor
- **[checklist.md · Keep Roll-Ups in Their Place]** "Ownership shown on
  alignment artifacts matches people actually working on the thing" has no
  backing anywhere in the article — the ownership point (from the source's
  "if someone owns something, make it clear") never made it into the Rationale.
  *Either add one sentence to the article or drop the item.*
- **[index.md · Statement, bullet 5 area]** "Big cross-team efforts get lanes of
  their own" appears in the Statement and the practice table but is never
  developed in the Rationale — the only Statement bullet without body support.
  *One sentence in the scale paragraph would close it.*
- **[index.md · At scale / Anti-Patterns]** The absolutes stack up: "no roll-up
  review ever pressure-tests anything" and "No one ever has." Rhetorically true
  to the source's register, but as a first-person operating record one hedge
  ("that I have seen") would cost nothing. *Author's call.*

### Nits
- **[index.md · How to Read This]** "the first in this journal grounded not in a
  book but in a practitioner essay" — accurate (it is the section opener), but
  all five Operating Takes records share the property; consider "part of the
  first section grounded…" so the sentence stays true if section order changes.
- **[index.md · after Figures 2–3]** Double blank lines left by the figure
  generator (cosmetic only; rendering unaffected).
- **[comics.md · Panel 7]** The "small robot" reviewing lane cards is not in the
  `comic-style` cast block; it renders fine but is the one cast deviation in the
  journal's comics.

## Spec ↔ post alignment

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index · highlight |
| Pyramid critique fair but firm | met | index · Statement b3, "Labels" ¶, practice table |
| NSF stance lands | met | index · "North Star Framework" ¶ (workshop evidence retold) |
| Scale argument appears | met | index · Statement b5 + "At scale" ¶; "costing you millions" retort lands in comics Panel 7 |
| Tension with [[outcomes]] addressed | met | index · "does not contradict" ¶ + Figure 3 |
| Checklist is operational | met | checklist · 5 sections (spec's 4 + roll-ups) |
| Credit is explicit | met | index · Authoritative References |

Non-goals respected: yes — no roadmap mechanics, no org design, no OKR tutorial.
Drift: none; spec `accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — 150 teams / 450–600 lanes, the removal test,
  and "lanes for months or quarters" match across article, checklist, and comic.
- **Terminology:** consistent ("lanes", "deckware", "roll-up", "pressure-test").
- **Voice & tone:** consistent first-person declarative; comic captions match.
- **Coverage parity:** even, except the checklist's ownership item (above),
  which exists only there.

## Layer-by-layer notes

### Spec
- Clean template use; checkable criteria; the decision log usefully records the
  five-record grouping rationale (this is the canonical copy the other four
  specs point at).

### index.md
- MADR order intact; headings Title Case; all three figures captioned and
  resolving; cross-links resolve (verified in the last build).
- The excerpt mirrors the highlight nearly verbatim — house convention, not a
  finding.

### checklist.md
- Well-grouped, one action per bullet, genuinely runnable; "Test Lane Quality"
  is the strongest section (each item is a real test, including the removal
  test).

### comics.md
- Eight panels, hook → problem → principle → scale → closer arc; captions match
  alt text; all panel images exist on disk; cast/style block byte-identical to
  the journal's other comics.

## Fixes applied (2026-08-14)

- **fixed** — ownership sentence added to the "Labels" paragraph; the checklist's ownership item is now backed by the article.
- **fixed** — cross-team lanes developed in the "At scale" paragraph (lanes of their own for bets that cross teams).
- **fixed** — "no roll-up review ever pressure-tests anything" hedged to "…I have seen"; the Anti-Patterns "No one ever has." kept for punch (author-call as noted).
- **fixed** — "the first in this journal" → "opens the first section of this journal".
- **fixed** — double blank lines collapsed.
- **skipped** — comic Panel 7 robot: harmless one-panel deviation; regeneration not warranted.
