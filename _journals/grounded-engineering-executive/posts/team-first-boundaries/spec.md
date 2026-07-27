---
status: accepted
revised: 2026-07-26
---

# Spec: Team-First Boundaries

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I draw software boundaries as an executive: I size boundaries to
team cognitive load, not to architectural fashion or the current org chart.
The post turns the *Team Topologies* "Team-First Boundaries" checklist into
an operating principle: start with the team rather than the architecture,
hunt the hidden monoliths that couple teams invisibly (application, joined
database, shared build, coordinated release, one-size-fits-all
standardization), split systems along natural fracture planes — business
domain first, then regulatory compliance, change cadence, team location,
risk profile, performance isolation, technology, and user personas — and
validate every proposed boundary against independent test, deploy, and
operate criteria before approving it.

## Audience

My leadership bench, architects, and peer executives (so boundary and
reorg-adjacent decisions are legible as flow decisions, not turf ones);
engineering leaders comparing operating models. First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states "size boundaries to team
      cognitive load" and "split along fracture planes, business domain
      first" in one paragraph.
- [ ] **The hidden monoliths are explicit** — application, joined database,
      shared build, coordinated release, and standardization coupling each
      appear as a named trap.
- [ ] **All eight fracture planes survive** — business domain, regulatory
      compliance, change cadence, team location, risk profile, performance
      isolation, technology, and user personas, with business domain argued
      as the default.
- [ ] **Validation is a gate, not a vibe** — the independent test / deploy /
      observe / operate criteria and the distributed-monolith warning are
      stated as the approval test.
- [ ] **The checklist survives intact** — all six PDF sections (including
      every fracture-plane subsection) reproduced in the Checklist tab
      (`checklist.md`).
- [ ] **Credit is explicit** — References name Skelton & Pais's *Team
      Topologies* and point to teamtopologies.com.

## Non-goals

- Not a microservices tutorial or a decomposition recipe for any specific
  system.
- Not [[organizational-design]] — that record covers sizing and staffing
  the teams; this one covers sizing the software each team owns.
- Not [[conways-law]] — that record covers the org–architecture mirroring
  force itself; this one covers where to cut the software given that force.
- No claim that smaller is always better — a boundary that fits one team's
  cognitive load is the goal, not maximal fragmentation.

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
  *The Engineering Executive's Primer*. The record reads the book's
  team-first boundary material through an executive lens and complements
  the Primer-grounded records.
- **2026-07-26** — Framed the record around cognitive load as the sizing
  unit: hidden monoliths and fracture planes are the diagnostic and the
  cure, and the validation criteria are the approval gate — not a separate
  architecture checklist.

## Sources

- **Internal**
  - `sources/checklists/appendix/team-topologies/Checklist_ Team
    Topologies _ Team-First Boundaries.pdf` — the operating checklist;
    reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies: Organizing Business
    and Technology Teams for Fast Flow* (IT Revolution Press, 2019) — the
    team-first boundaries chapter this record distills.

## Changelog

- **2026-07-26** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/LEO cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-26** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec for the appendix record. Status `draft`.
  *(Željko, AI-mediated session)*
