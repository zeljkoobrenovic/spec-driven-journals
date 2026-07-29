---
status: accepted
revised: 2026-07-29
---

# Spec: Static Team Topologies

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I choose team structures as an executive: from the known catalog
of team patterns and anti-patterns, judged against our own context — never
by copying another company's model. The post turns the *Team Topologies*
"Static Team Topologies" checklist into an operating principle: intentional,
long-lived team design over ad-hoc formation and constant reshuffling;
organizing for flow of change (minimal handoffs, fast production feedback);
naming the anti-patterns (over-the-wall handoffs, disposable project teams,
the DevOps silo, cargo-culting the Spotify model); selecting a topology by
organization size, software scale, engineering and cultural maturity, and
Conway's law; the conditions under which stream-aligned/product teams,
platform support, feature teams, and SRE each work; and managing
dependencies and silos so the structure serves flow.

## Audience

My leadership bench and peer executives (so team-design decisions are
legible as pattern-plus-context choices, not fashion); engineering leaders
tempted to import a famous company's org chart. First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states "patterns are a catalog,
      context is the selector" and names ad-hoc design and constant
      reshuffling as the two quiet delivery killers in one paragraph.
- [ ] **Context factors are explicit** — organization size, software scale,
      technical and cultural maturity, engineering discipline
      (automation/testing/deployment/monitoring), and Conway's law all
      appear as selection criteria.
- [ ] **Anti-patterns are named** — ad-hoc team design, constant
      reshuffling, over-the-wall handoffs, disposable project teams, the
      DevOps team as a new silo, and blind model-copying each appear.
- [ ] **The conditional patterns are conditional** — feature teams require
      high engineering maturity and trust; SRE requires scale that
      justifies it; product teams require a compatible support system.
- [ ] **The checklist survives intact** — all eleven PDF sections
      reproduced in the Checklist tab (`checklist.md`).
- [ ] **Credit is explicit** — References name Skelton & Pais, *Team
      Topologies* (IT Revolution Press, 2019) and teamtopologies.com.

## Non-goals

- Not a description of the four fundamental topologies — that is
  [[four-fundamental-team-topologies]]; this record is about choosing from
  the wider pattern catalog and avoiding the anti-patterns.
- Not [[team-interaction-modes]] — how teams collaborate once chosen.
- Not [[evolve-team-structures]] — how topologies change over time; this
  record notes evolution but does not develop it.
- Not [[organizational-design]] — team sizing and investment sequencing;
  this record covers which shapes to pick, not how big to make them.
- No claim that any single topology is "best" — the book's point is that
  none is.

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

- **2026-07-26** — This is an **appendix record**: grounded in Matthew
  Skelton & Manuel Pais, *Team Topologies: Organizing Business and
  Technology Teams for Fast Flow* (IT Revolution Press, 2019) rather than
  *The Engineering Executive's Primer*. The record reads the book's static
  team patterns through an executive lens and complements the
  Primer-grounded records.
- **2026-07-26** — Framed the record around "patterns are a catalog,
  context is the selector" — the anti-pattern of copying another company's
  model (the Spotify cargo cult) is the foil; the context-fit judgment
  (size, maturity, Conway's law) is the load-bearing idea.

## Sources

- **Internal**
  - `sources/checklists/appendix/team-topologies/Checklist_ Team
    Topologies _ Static Team Topologies.pdf` — the operating checklist;
    reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies: Organizing Business
    and Technology Teams for Fast Flow* (IT Revolution Press, 2019) — the
    static-topologies chapters this record distills.

## Changelog

- **2026-07-29** — Changelog reconciled: comic panel images and article
  illustrations are generated and in place; nothing remains staged or
  pending. *(Željko, AI-mediated session)*
- **2026-07-26** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/LEO cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-26** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec for the appendix record. Status `draft`.
  *(Željko, AI-mediated session)*
