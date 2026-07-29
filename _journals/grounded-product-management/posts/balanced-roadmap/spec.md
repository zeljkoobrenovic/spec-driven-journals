---
status: accepted
revised: 2026-07-29
---

# Spec: Balanced Roadmap

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I keep a product roadmap balanced instead of letting it be
captured by whoever shouts loudest. The post turns the *Build What Matters*
"Balanced Roadmap" checklist into an operating principle: confirm why the
roadmap exists (connecting near-term changes to milestones and the vision),
classify every item as innovation, iteration, or operation, set a top-down
allocation across the three categories *before* ranking individual projects,
tune the allocation to the product's lifecycle stage, prioritize within each
category with a method fit for that category (milestone-driven for
innovation, RICE-style scoring for iteration, reserved capacity and an
explicit bug policy for operation), run stakeholder requests through a real
intake process, and review the finished roadmap against the vision before
finalizing it.

## Audience

My product leadership bench and peer executives (so roadmap trade-offs are
legible as deliberate allocation, not favoritism); PMs who need to defend
their roadmap under stakeholder pressure; engineering leaders who want to
know why operational work has protected capacity. First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states "allocate across
      innovation, iteration, and operation before ranking anything" in one
      paragraph.
- [ ] **The three categories are explicit** — innovation, iteration, and
      operation each appear with their definition and their own
      prioritization method.
- [ ] **Allocation-before-ranking is argued** — top-down allocation as the
      defense against loud stakeholders and against comparing unlike work.
- [ ] **Lifecycle tuning survives** — pre-alpha through steady state, each
      stage with its allocation lean.
- [ ] **Both failure modes appear** — the all-reactive roadmap and the
      ivory-tower all-vision roadmap, flanking the balanced middle.
- [ ] **The checklist survives intact** — all nine PDF sections reproduced
      in the Checklist tab (`checklist.md`).
- [ ] **Credit is explicit** — References name Foster & Nerlikar's *Build
      What Matters*.

## Non-goals

- Not a roadmap template or a specific tool recommendation.
- Not [[product-strategy]] — that record covers where the milestones come
  from; this one covers how the roadmap balances work against them.
- Not [[outcomes]] — that record covers measuring what shipped work
  achieves; this one covers what gets onto the roadmap at all.
- Not annual planning mechanics — those live in the engineering journal's
  [[planning]] record; this record is about what the product roadmap
  contains.
- No claim of a universally correct allocation percentage — the split is a
  deliberate, revisited decision, not a constant.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab). Summary/dialog may be added later per
journal policy.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-27** — This record is grounded in Ben Foster & Rajesh Nerlikar,
  *Build What Matters: Delivering Key Outcomes with Vision-Led Product
  Management* (Lioncrest Publishing, 2020), read through a
  practitioner-executive lens. This journal is the product-management
  counterpart to the engineering-executive journal grounded in Larson's
  books.
- **2026-07-27** — Framed the record around "allocate before you rank" —
  the innovation / iteration / operation classification is the load-bearing
  idea; the per-category prioritization methods and the stakeholder intake
  process are consequences of it, not a separate list.

## Sources

- **Internal**
  - `sources/build-what-matters/Checklist_ Build What Matters _ Balanced
    Roadmap.pdf` — the operating checklist; reproduced in the Checklist tab
    (`checklist.md`).
- **External**
  - Ben Foster & Rajesh Nerlikar, *Build What Matters: Delivering Key
    Outcomes with Vision-Led Product Management* (Lioncrest Publishing,
    2020) — the balanced-roadmap chapter this record distills.

## Changelog

- **2026-07-29** — Post-review fixes applied. Article figures and all eight
  comic panels are final generated images (the 2026-07-27 "pending panel
  blocks / staged placeholders" state is superseded); Panel 5 regenerated so
  the allocation bar reads innovation / iteration / operation; category name
  normalized to singular "operation" across modalities; the five-stage
  lifecycle restored in the article's Statement. *(Željko, AI-mediated
  session)*
- **2026-07-27** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/MILA cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-27** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-27** — Initial spec. Status `draft`. *(Željko, AI-mediated
  session)*
