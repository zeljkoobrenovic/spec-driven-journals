---
status: accepted
revised: 2026-08-13
---

# Spec: Growing Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the growth model I hold platforms to: a platform grows **adoption**,
not merely functionality, and it grows along three balanced dimensions —
reach (who uses it), breadth (how much of the problem space it covers), and
depth (how complete and polished the key capabilities are). The post turns
the "Growing Platforms" chapter of Gregor Hohpe's *Platform Strategy* into
an operating principle: platforms move through a product lifecycle (Explore
→ Expand → Extract), win or lose on the new user's first hour (minimize the
cliff, avoid the hockey stick), protect cohesion through a roadmap that
triages requests on business impact and strategy fit, and scale **down** via
tiers and slices as deliberately as they scale up. The load-bearing idea:
an internal platform nobody is forced to use lives or dies on voluntary
adoption, so growth is a product discipline, not a feature race.

## Audience

Platform product owners and platform leads accountable for adoption (so
they know the growth dimensions and the triage bar I hold roadmaps to);
platform engineers tempted to equate growth with features; peer executives
comparing platform operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states adoption over
      functionality, the reach/breadth/depth balance, the lifecycle, the
      on-ramp, roadmap-protected cohesion, and scaling down via tiers and
      slices.
- [x] **The three growth dimensions survive** — market reach, platform
      breadth, platform depth; balanced rather than maximized one at a time;
      no "perfect platform for one customer" before broader adoption.
- [x] **The lifecycle survives** — Explore (validate that users value the
      platform, not merely that the technology works), Expand (remove
      adoption obstacles, self-service, documentation), Extract (economics
      and scale) — and reassessing team, skills, and leadership between
      phases.
- [x] **The on-ramp survives** — new-user perspective, minimizing the
      initial cliff, familiar concepts, sensible defaults and templates,
      simple tasks easy and complex tasks possible, no hockey-stick
      experience, painless gear-shifts, and escape hatches.
- [x] **The roadmap triage survives** — requests evaluated on business
      impact × roadmap fit; decline low-impact misfits and explain the
      principles; no professional-services team for one customer; existing
      users treated as a biased sample; a credible published roadmap.
- [x] **Tiering and slicing survive** — scale down as well as up, vertical
      tiers and horizontal slices on shared assets, each defined around a
      clear use case with transparent trade-offs.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the "Growing Platforms" chapter.

## Non-goals

- Not [[platform-as-a-product]] — that record establishes the product
  operating mode for platform teams; this one covers the specific growth
  and adoption discipline inside that mode.
- Not [[implementing-platforms]] — the machinery that makes self-service
  and low cognitive load technically possible lives there; this record
  covers growing the use of that machinery.
- Not [[platform-success]] — the definition of what platform success looks
  like lives there; this record is about the path that gets a platform
  there.
- Not a mandate policy — this record deliberately does not cover forcing
  adoption through decree; its whole premise is voluntary adoption.

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

- **2026-08-12** — Grounded in the "Growing Platforms" chapter of Gregor
  Hohpe, *Platform Strategy: Innovation Through Harmonization* (Leanpub,
  2024), via its chapter checklist — read through a practitioner-executive
  lens, as with every record in this journal.
- **2026-08-12** — Framed around "grow adoption, not functionality" as the
  spine, with reach/breadth/depth, the lifecycle, the on-ramp, roadmap
  triage, and tiering as the supporting mechanisms — the chapter's
  distinctive claim is that platform growth is a product discipline, not a
  feature race.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Growing
    Platforms.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — the "Growing Platforms" chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
