---
status: accepted
revised: 2026-07-26
---

# Spec: Conway's Law

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I use Conway's law as an executive: systems mirror the
communication structures of the organizations that build them, so
organizational design is my most powerful architectural decision. The post
turns the *Team Topologies* "Conway's Law" checklist into an operating
principle: clarify the architecture we actually want before touching the org
chart, check whether the current structure could even produce it, use the
reverse Conway maneuver (shape team boundaries to match the target
architecture), enable team-scoped flow (bounded responsibility, loose
coupling, high cohesion), involve technical expertise in organization
design, restrict unnecessary cross-team communication as a design smell,
review tool choices for the interaction patterns they force, and avoid
naive uses of the law (too many small component teams, reorgs for headcount
or fiefdoms).

## Audience

My leadership bench and peer executives (so reorgs and team-boundary
decisions are legible as architectural moves, not political ones);
architects and engineering leaders comparing operating models.
First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states that systems mirror
      communication structures and that I design team structures to produce
      the architecture we want (the reverse Conway maneuver) in one
      paragraph.
- [ ] **The maneuver is explicit** — "design teams first, architecture
      follows" is argued, not just named.
- [ ] **Communication is reframed** — unnecessary cross-team communication
      is treated as a design smell, not a virtue; necessary paths are
      deliberate.
- [ ] **Tools and shared services appear** — shared tools, shared teams,
      and shared databases are named as coupling forces that shape
      architecture.
- [ ] **Naive uses are warned against** — too many small component teams,
      reorgs for headcount or fiefdoms, ignoring cognitive load.
- [ ] **The checklist survives intact** — all nine PDF sections reproduced
      in the Checklist tab (`checklist.md`).
- [ ] **Credit is explicit** — References name Skelton & Pais's *Team
      Topologies* and point to teamtopologies.com.

## Non-goals

- Not a microservices tutorial or a target architecture for any company.
- Not [[organizational-design]] — that record covers sizing and staffing
  the organization as a system; this one covers the architectural force the
  structure exerts.
- Not [[four-fundamental-team-topologies]] — that record names the team
  types; this one explains why team shape determines system shape at all.
- No claim that Conway's law is destiny — it is a force to be harnessed,
  not an excuse to stop designing.

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
  Conway's-law material through an executive lens and complements the
  Primer-grounded records.
- **2026-07-26** — Framed the record around the reverse Conway maneuver as
  the load-bearing idea: the law itself is descriptive; the executive move
  is to design the team structure that produces the architecture we want,
  and to treat communication paths and tool choices as architectural
  decisions.

## Sources

- **Internal**
  - `sources/checklists/appendix/team-topologies/Checklist_ Team
    Topologies _ Conway's Law.pdf` — the operating checklist; reproduced in
    the Checklist tab (`checklist.md`).
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies: Organizing Business
    and Technology Teams for Fast Flow* (IT Revolution Press, 2019) — the
    Conway's-law chapter this record distills.

## Changelog

- **2026-07-26** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/LEO cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-26** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec for the appendix record. Status `draft`.
  *(Željko, AI-mediated session)*
