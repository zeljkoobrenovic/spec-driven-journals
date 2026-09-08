# Review: Cost, Performance, and Scalability

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a tight, checkable contract; all nine
success criteria are met; the checklist is a faithful, complete adaptation of the
source chapter checklist (all 12 sections plus the final review, no invented
obligations); all eight cross-links resolve; all 13 referenced images (3 figures,
9 panels, logo) exist. The single most important thing to address is a small
consistency wobble in the loop's canonical phrasing — the front-matter excerpt
drops the "buy capacity" stage and comic panel 6's caption names a stage its
image does not show.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 4

### Blockers

- None.

### Major

- None.

### Minor

- **[comics.md · Panel 6]** The caption names the five-stage loop ("baseline,
  rightsize, scale, buy capacity at the right price, measure") but the generated
  image and the alt text show a four-station loop (baseline, rightsize, scale,
  measure — the speech bubble even reads "Baseline, rightsize, scale, measure.
  Repeat."). *Trim the caption to the four stages shown, or regenerate the panel
  with a fifth station.*
- **[index.md · front-matter `excerpt` vs highlight/Figure 1]** The loop is
  phrased three ways: the excerpt says "baseline, rightsize, scale, measure,
  repeat" (drops "buy capacity at the right price"), the highlight and summary
  say "baseline, rightsize, scale, buy capacity at the right price, measure,
  repeat," and Figure 1's caption says "baseline, rightsize, **autoscale**, buy
  capacity at the right price, measure." *Pick one canonical five-stage phrasing
  and use it everywhere.*

### Nits

- **[dialog.md · "The Loop, Not the Project", Ana's baseline answer]** "That
  exercise is in the Checklist tab **verbatim**" — the spec says "reproduced,
  adapted." The items are in fact verbatim (only the section title is reframed),
  so this is defensible, but "near-verbatim" or dropping the adverb would remove
  the tension.
- **[checklist.md · §7]** The spot-exclusion sub-items are plain bullets while
  comparable sub-lists (§2 labels, §4 bound types, §5 custom metrics) are
  checkboxes. Semantically defensible (they are examples, not tasks), but
  inconsistent within the file — §5's "considered, such as" list got checkboxes.
- **[index.md · "The Reference Stack" heading]** Sibling `policy-as-code` uses
  "Reference Stack" without the article. Cosmetic; the journal has no strict
  norm yet.
- **[index.md · after Figures 2 and 3]** Doubled blank lines after the figure
  captions (lines 97–98, 103–104). No render effect; tidy when next edited.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (three outcomes, loop framing, running test all present) |
| Goals and trade-offs survive | met | index.md · Statement ("Goals and trade-offs come first"); checklist.md §1 |
| Cost observability survives | met | index.md · Statement + Reference Stack table; checklist.md §2 |
| Baseline and rightsizing survive | met | index.md · Statement (baseline/profile/rightsize bullets); checklist.md §3–4 |
| Autoscaling survives | met | index.md · Statement + Rationale ("Autoscaling is a performance instrument…"); checklist.md §5–6 |
| Capacity mix survives | met | index.md · Statement + Figure 2; checklist.md §7 |
| Governance, anomalies, CI/CD gates survive | met | index.md · Statement + Rationale + Figure 3; checklist.md §8–10 |
| Measurement and worked exercise survive | met | index.md · "The loop closes"; checklist.md §11–12 + Final Review (30% exercise reproduced) |
| Credit is explicit | met | index.md · Authoritative References; summary.md footer; spec Sources |

Non-goals respected: yes — enforcement machinery, telemetry stack, pipeline,
onboarding quotas, and FinOps org design are all deferred to the named sibling
records in every modality; the summary and dialog restate the boundaries
explicitly.

Drift: none. Spec `status: accepted` is accurate; the post `draft:gray` status
matches its visible DRAFT highlight and Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — SLOs-before-savings, attribution as the
  behavioral mechanism, the never-list for spot, the commitment trap, and the
  pull-request-not-invoice framing appear identically everywhere. Only the loop
  phrasing wobbles (minor finding above).
- **Terminology:** consistent — "broken at a discount," "the team that sees its
  own number is the team that fixes it," "a cost story without a baseline is an
  anecdote," and the anti-pattern names (spot roulette, commitment trap,
  month-end surprise, quota-free commons, savings project) travel intact across
  article, summary, dialog, and comic.
- **Voice & tone:** consistent — first-person declarative in article and
  summary; Ana/Ben split matches the journal (Ben presses, Ana carries);
  VERA/KAI comic cast per house convention.
- **Coverage parity:** even — every Statement group (goals, observability,
  baseline, rightsizing/scaling, capacity mix, governance/anomalies, gates,
  measurement) is carried by checklist, summary, and dialog; the comic compresses
  to the SLO-first principle, attribution, the loop, tested autoscaling, and the
  savings-project failure, which is the right subset for the form.

## Layer-by-layer notes

### Spec

- All template sections present; the nine success criteria are genuinely
  checkable (each names concrete source items to survive), non-goals fence off
  exactly the five neighboring records, and the decision log explains the two
  real editorial moves (continuous-loop framing; capability-level commitments).
- No bloat, no dangling open questions; changelog and `revised:` are current.

### index.md

- House record shape followed exactly (sibling heading order matches); headings
  are Title Case; all eight `[[…]]` targets resolve to permalinks in this
  journal; all three figures exist and are captioned.
- The Rationale is the strongest section — each paragraph earns a distinct
  point (ordering, attribution, baseline, autoscaling trust, stability classes,
  gates, loop) with no repetition between them.
- The What-it-does-not-say column consistently guards against the over-rotation
  failure mode (blame chargeback, asphyxiation rightsizing, blanket blocking),
  which gives the record its executive credibility.

### checklist.md

- Faithful to the source: all 12 source sections plus the final review are
  present, item-for-item, in source order; the only adaptations are the reframed
  §12 title ("The Worked Exercise: A 30% Reduction Round" for "Exercise 12.3
  Completion Checklist") and the added `[[policy-as-code]]` cross-reference —
  both appropriate. No invented obligations.
- Runnable as written; the intro line correctly routes rationale to the Article
  tab and licenses tool substitution.

### summary.md

- ~450 words, within the modality target; leads with the three-outcomes decision
  statement; the What-it-costs section honestly names the standing obligations
  and the savings deliberately left on the table — the part a leader most needs.
- Footer follows the journal's established italic-roman title convention.

### dialog.md

- Ben's skeptical positions are real (annual savings projects, untested HPA,
  spot war stories, pipelines that teach routing-around) and each gets a
  substantive answer rather than a brush-off; the gaming-quotas revisit trigger
  surfacing as a concession is a nice touch.
- Sounds spoken throughout; the closing exchange ("a subscription to
  surprises") lands the record's test without lecturing.

### comics.md

- Nine panels with a clean arc (hook → problem → wrong way → principle → two
  how-it-plays-out beats → loop → cost → closer); all nine image files exist;
  captions are single sentences matching their alt text except panel 6 (minor
  finding above); cast and style block match the journal convention.

## Fixes applied (2026-08-20)

- **[minor · comics.md]** Panel 6 caption trimmed to the four stages the image
  actually shows ("The loop: baseline, rightsize, scale, measure — then run it
  again"), matching the alt text and the speech bubble. Caption trim preferred
  over regeneration per orchestrator direction; image text is clean.
- **[minor · index.md]** Canonical five-stage loop phrasing fixed as "baseline,
  rightsize, scale, buy capacity at the right price, measure, repeat" (the
  phrasing the highlight, summary, and dialog already used): the front-matter
  excerpt now carries the full five stages, and Figure 1's caption says "scale"
  instead of "autoscale". Figure 1's alt text keeps "autoscale" because it
  describes the literal diagram, whose station label reads AUTOSCALE.
- **[nit · dialog.md]** "in the Checklist tab verbatim" → "near-verbatim",
  removing the tension with the spec's "reproduced, adapted".
- **[nit · checklist.md]** §7 spot-exclusion sub-items converted from plain
  bullets to checkboxes, matching the §2/§4/§5 sub-list convention.
- **[nit · index.md]** "The Reference Stack" heading → "Reference Stack",
  matching 9 of the 11 sibling Reference Implementation posts that have the
  section.
- **[nit · index.md]** Doubled blank lines after the Figure 2 and Figure 3
  captions collapsed to single blank lines.
