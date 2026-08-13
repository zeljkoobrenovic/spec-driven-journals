---
status: accepted
revised: 2026-08-13
---

# Spec: Designing Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the design doctrine I hold every internal platform to: a platform is a
fruit salad, not a fruit basket — its value comes from integration, defaults,
and reduced toil, not from cataloging tools. The post turns the "Designing
Platform" chapter checklist of Gregor Hohpe's *Platform Strategy* into an
operating principle: use the 7 Cs as trade-off dimensions rather than a
maximization recipe; earn every horizontal capability with concrete user
benefit; let the platform float on its evolving base by retiring commoditized
functionality; refuse grim wrappers and build abstractions that speak a
higher-level vocabulary without becoming illusions; and design for failure,
because abstractions break down hardest when things go wrong. The load-bearing
idea: an abstraction that hides essential complexity has not simplified
anything — it has just moved the bill.

## Audience

Platform architects and leads who design our internal platforms; engineers
proposing new platform capabilities, wrappers, or abstractions; peer
executives comparing platform design doctrines. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight commits to fruit salad over fruit
      basket, abstractions over illusions, floating over sinking, and
      designing for the unhappy path.
- [x] **The 7 Cs survive as trade-offs** — cohesion, closure, completeness,
      consistency, commensurate value, connectedness, captivity — explicitly
      as dimensions to weigh and document, not qualities to maximize.
- [x] **The architecture tests survive** — vertical components joined by
      horizontal capabilities that each earn their existence through reuse,
      governance, or operations; float-or-sink discipline against the base
      platform.
- [x] **The wrapper and abstraction warnings survive** — configuration,
      hooks, and tracking before any new wrapper; abstractions grounded in a
      real domain; essential complexity (failures, latency, cost) stays
      visible.
- [x] **Design-for-failure survives** — errors traceable to their origin,
      open-the-hood access to lower layers, documented failure modes, and
      people who still understand the underlying technology.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the designing-platforms chapter.

## Non-goals

- Not [[understanding-platforms]] — that record covers what platforms are and
  why harmonization beats standardization; this one assumes the platform is
  justified and governs how it is designed.
- Not [[implementing-platforms]] — build/buy choices, sizing, and delivery
  mechanics live there; this record is the design quality bar those
  implementations must meet.
- Not [[organizing-for-platforms]] — team shape, roles, and engagement models
  are that record's subject; here they appear only as the people needed to
  diagnose cross-layer failures.
- Not a technology catalog — no positions on specific IDPs, clouds, or
  orchestrators.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Grounded in the "Designing Platform" chapter checklist of
  Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
  (Leanpub, 2024) — read through a practitioner-executive lens, as with every
  record in this journal.
- **2026-08-12** — Framed around the fruit-salad test and the
  abstraction-vs-illusion line rather than a design-pattern tour: the
  chapter's distinctive claim is that platform value comes from integration
  choices and honest abstractions, so the record commits to those as the
  quality bar.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Designing Platforms.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — the designing-platforms chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
