# Review: Engineering Strategy

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All five spec success criteria are met, the checklist reproduces all ten source sections, all three figures and all eight comic panel images exist on disk, all five cross-links resolve, and the spec changelog is current. The strongest article in the reviewed set — every Rationale paragraph earns its claim with a mechanism, and the "vision statement wearing a strategy costume" line threads article, excerpt, and comic. The one real finding: several checklist items bundle two or three distinct actions into a single checkbox, making them less operationally checkable than the journal's other checklists.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · Writing Process, Launch, Ongoing Review]** Multiple items bundle several actions into one checkbox — e.g. "Identify 3–5 trusted stakeholders for early feedback; iterate the diagnosis 1:1 with them; refine guiding policies with them" (three actions), "Set a short feedback window (about one week), finalize the document, and send a formal announcement" (three), "Policies are being followed; exceptions are handled consistently; the escalation process works" (three). A user can complete one clause and not the others, so the box is un-checkable as written; the journal's other checklists keep one action per item. *Split the semicolon/comma-chained items.*

### Nits
- **[checklist.md · Ongoing Review]** Items are phrased as state assertions ("Policies are being followed") while the rest of the file uses imperatives or first-person commitments — a register wobble within one file.
- **[index.md · front matter]** The `excerpt` restates the Principle highlight nearly verbatim (same pattern as the journal's other posts; house convention, but trimmable).
- **[index.md · Statement, bullet 4]** One sentence carries five process elements (working group, skeptics, socialization, feedback window, review cadence); parseable but the densest line in the piece.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (write-personally, enforce-what-you-publish) | met | index.md · Principle highlight |
| Kernel explicit with per-policy quality bar (applicable / enforced / leverage-creating) | met | index.md · Statement bullets 2–3, Figures 1–2; checklist.md · Structure + Quality Check |
| Process visible (working group, skeptics, socialize-before-announce, short window, review cadence) | met | index.md · Statement bullet 4 + Rationale "Socializing beats announcing" + Anti-Patterns "Strategy frozen in time" (2 months / annual) |
| Checklist survives intact (all ten PDF sections) | met | checklist.md · Before You Start → Ongoing Review, all ten present incl. Missing Company Strategy |
| Credit explicit (Primer + lethain.com essay) | met | index.md · Authoritative References (plus Rumelt, per the spec's Sources) |

Non-goals respected: yes — the record repeatedly states it is the production process, not a strategy document ("This record describes how I produce a strategy — it is not a strategy itself"); planning is fenced off to [[planning]] with the strategy-constrains/planning-allocates distinction; no company-specific content appears.
Drift: none. Spec `status: accepted` is accurate; changelog is current through image generation.

## Cross-modality alignment

- **Facts & framing:** consistent — kernel structure, four preconditions, three-gate quality bar, socialize-before-announce, ~one-week window, two-month impact review + annual refresh, and the missing-company-strategy move agree across article and checklist; the comic carries the same three-gate and skeptics beats.
- **Terminology:** consistent — "diagnosis / guiding policies / coherent actions," "applicable, enforced, leverage-creating," "vision statement wearing a strategy costume," "shelf-ware/shelf" used the same way across all three surfaces.
- **Voice & tone:** consistent first-person executive register; shared VERA/LEO cast with the "Comic panel:" alt-text prefix.
- **Coverage parity:** good — the comic compresses out the missing-company-strategy beat and the launch mechanics (window, cadence), closing instead on "only publish what you will enforce"; both beats are fully carried by article and checklist. No modality introduces a beat the spec lacks.

## Layer-by-layer notes

### Spec
- Full template, no bloat; the decision log records the two structural calls (checklist moved to its own modality; Rumelt vocabulary kept rather than a house taxonomy) with reasons.
- Success criteria are individually checkable and the checklist criterion enumerates the exact ten sections — verification was mechanical.
- Changelog is current; no dangling open questions.

### index.md
- House shape and Title Case headings correct; the four-precondition opening is a strong structural choice that the checklist mirrors as "Before You Start."
- Rationale is the best-argued in the reviewed set: "Delegated strategy is dead strategy" and "Policies without enforcement are decoration" both supply concrete failure mechanisms and examples ("'We value quality' is not applicable in a trade-off").
- The practice table's right-hand column does real work — each "does not say" preempts a plausible misreading (centralization, forbidden exceptions, referendum launches).
- Repetition of the applicable/enforced/leverage-creating triple across highlight, Statement, Rationale, and figure caption is deliberate load-bearing repetition, not redundancy.

### checklist.md
- All ten source sections present and phase-ordered exactly as the spec requires; concrete numbers preserved (3–5 stakeholders, 2–3 external executives, ~one week, ~two months).
- The Guiding Policies section's three-area breakdown (resource allocation / fundamental rules / decision-making model) matches the article's late-table paragraph precisely.
- The bundled multi-action items (minor above) are the file's only real weakness; the Missing Company Strategy section's italic lead-in is handled cleanly (unlike the stray bullet in engineering-onboarding's quick-start).

### comics.md
- Eight panels, strong arc: vision poster → costume reveal → kernel → committee shelfware → write-it-yourself → three gates → meet the skeptics → thin signed document. The costume gag in Panel 2 translates the article's signature metaphor exactly.
- All eight referenced images exist under `assets/images/engineering-strategy/`; captions match alt texts.
- Panel 8's "single thin signed document" quietly carries the article's "the bar keeps the document honest — and short" point — a nice visual compression.
