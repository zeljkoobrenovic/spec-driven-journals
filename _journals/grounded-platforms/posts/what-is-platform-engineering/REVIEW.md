# Review: What Is Platform Engineering

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the stronger arguments in the journal: the swamp
diagnosis, the product stance, and the leverage test are stated crisply, every
success criterion is met, and the comic mirrors the article beat for beat. The
single most important thing to address is coverage parity: the checklist's
section 8 (Build the Right Platform Team — infrastructure/DevTools/DevOps/SRE
role guidance) has no echo in the article or the spec's success criteria, so a
tenth of the runnable tool is contractually invisible.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[checklist.md · §8 "Build the Right Platform Team" vs index.md/spec.md]**
  The team-composition section (role-by-role balance for infrastructure,
  DevTools, DevOps, SRE engineers) appears only in the checklist — the
  article's Statement, Rationale, and the spec's success criteria never touch
  team shape, and it overlaps [[building-platform-teams]] territory the spec
  does not fence. *Either add a one-line team beat to the article (a Statement
  bullet or Related Records note pointing at [[building-platform-teams]]) or a
  spec criterion acknowledging the section.*
- **[index.md · How to Read This]** "The runnable version — foundations, swamp
  reduction, product practice, and the success criteria — lives in the
  Checklist tab" names 4 of the checklist's 10 sections, silently omitting
  migrations, "you build it, you run it", team, glue, and innovation.
  *Reword as a characterization rather than an enumeration ("from foundations
  through the success criteria").*
- **[index.md · Rationale ¶1]** "until half of engineering time goes to
  integration glue" states a specific quantity as fact with no support, and
  the comic (Panel 2) repeats it. *Hedge it ("an ever-growing share") or own
  it as illustrative.*

### Nits

- **[index.md · Statement, leverage bullet]** "directly-owned primitives" —
  the -ly adverb compound should be unhyphenated ("directly owned").
- **[index.md · front matter]** The excerpt is three long sentences (~90
  words); within house norms but at the top of the range for an index card.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (complexity, internal product, leverage test) | met | index.md · Status/Principle highlight |
| Swamp diagnosis survives | met | index.md · Statement bullet 2, Rationale ¶1; checklist.md · §2 |
| Product stance survives | met | index.md · Statement bullets 1/3/4, Rationale ¶3; checklist.md · §3–4 |
| Operating stance survives | met | index.md · Statement bullets 5–6, Rationale ¶4–5; checklist.md · §6–7 |
| Innovation stays possible | met | index.md · Rationale ¶6 + "Shadow-platform whack-a-mole" anti-pattern; checklist.md · §9 |
| Credit explicit | met | index.md · Authoritative References (Fournier & Nowland, introductory chapter) |

Non-goals respected: yes — the boundary/curation material stays at
definition level (four-pillars territory is motivated, not defined), no
getting-started mechanics, no product-operating deep dive, no tooling
positions (Terraform appears only as the source's named failure mode).
Drift: none beyond the §8 parity gap noted above; spec `accepted` remains
fair if that gap is accepted as source fidelity.

## Cross-modality alignment

- **Facts & framing:** consistent — swamp, ticket bureau, mandate,
  internal product, hide-vs-relocate, central migrations, leverage test
  appear with the same claims in article, checklist, and comic. The one
  shared soft spot is the "half of engineering time" figure (article ¶1,
  comic Panel 2).
- **Terminology:** consistent — "over-general swamp," "paved path,"
  "ticket-driven service bureau"/"Terraform writing service," "you build it,
  you run it," "leverage" carry across all three files.
- **Voice & tone:** consistent — first-person accountable-executive register
  in the article; checklist in neutral imperative (appropriate for a runnable
  tool); comic compresses without changing position.
- **Coverage parity:** even except checklist §8 (team composition), which has
  no article or spec echo — see the minor finding.

## Layer-by-layer notes

### Spec

- Template-complete; the six success criteria are concrete and verifiable,
  and the Non-goals do real work fencing off three sibling records.
- The decision-log entry ("lead with the swamp, hold to a leverage test, not
  a feature list") is exactly the shape the article delivers — a good
  contract.
- Gap: the criteria under-describe the checklist (nothing covers §5 glue
  reduction or §8 team), which is how the parity gap slipped through.

### index.md

- House record shape is fully observed: highlight, Statement → How to Read
  This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope and Revisiting → References; headings are correctly Title Case.
- The Rationale is the strongest section — "nobody chooses the swamp;
  organizations accumulate it one sensible choice at a time" and "a platform
  without boundaries is just the swamp with a logo" set up every later claim.
- The contrast table and Anti-Patterns cover the same failure modes without
  feeling duplicative — the table states the boundary, the anti-patterns
  dramatize it. Good division of labor.
- All five `[[…]]` cross-links resolve to existing posts; all three figures
  exist on disk and are captioned.

### checklist.md

- Ten sections, consistently imperative, terminology matches the article
  (swamp, glue, paved path, leverage). Reads as genuinely runnable.
- §10 Success Criteria aligns exactly with the article's leverage test and
  Scope-and-Revisiting triggers — a nice closed loop.
- §8 is the only section without an article anchor (see finding).

### comics.md

- Eight panels, captions run Panel 1–8, all eight images exist in
  `assets/images/what-is-platform-engineering/`, alt text matches captions,
  VERA/KAI cast and shared style block intact.
- Beat structure (hook → problem → wrong way ×2 → principle → mechanism →
  economics → closer) tracks the article's Rationale order faithfully; the
  two "wrong way" panels map cleanly onto the ticket-bureau and mandate
  anti-patterns.

## Fixes applied (2026-08-13)

- checklist.md · §8 vs index.md/spec.md — fixed: added a Related Records line pointing at [[building-platform-teams]] for the team-composition section, and a spec success criterion covering the checklist's full breadth (glue reduction §5 and team composition §8); `revised:` bumped and Changelog line added.
- index.md · How to Read This — fixed: reworded the checklist pointer as a characterization ("from platform foundations through the success criteria") instead of a partial enumeration.
- index.md · Rationale ¶1 — fixed: hedged "half of engineering time" to "an ever-growing share of engineering time"; comic Panel 2 caption updated to match (text-only, no panel regeneration — image content was not flagged).
- index.md · Statement, leverage bullet — fixed: "directly-owned" → "directly owned".
- index.md · front matter excerpt — skipped: reviewer notes it is within house norms; shortening would cut substance for no flagged defect.
- index.md · figure caption spacing — fixed: collapsed the double blank lines after Figures 1–3 (flagged as a sibling occurrence in the introduction review's spacing nit).
