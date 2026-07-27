---
status: accepted
revised: 2026-07-26
---

# Spec: Team-First Thinking

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I treat teams as the unit of everything: the long-lived, stable
team — not the individual — is the basic unit of delivery, ownership, and
reward in my organization. The post turns the *Team Topologies* "Team-First
Thinking" checklist into an operating principle: keep teams small (5–9
people) and long-lived; assign work to teams, never directly to individuals;
give every system exactly one owning team (stewards, not private owners);
reward the whole team; treat team cognitive load — intrinsic, extraneous,
germane — as the budget every domain assignment and software boundary must
fit within; publish a Team API so other teams can interact without insider
knowledge; and back it all with strong engineering practices, because
team-first design does not work without them.

## Audience

My leadership bench and peer executives (so assignment, ownership, and
reward decisions are legible as team-level system moves); engineering
leaders comparing operating models. First-person declarative.

## Success criteria

- [ ] **Principle is quotable** — highlight states "the team, not the
      individual, is the unit of delivery" and "cognitive load is the
      budget" in one paragraph.
- [ ] **The numbers survive** — teams of 5–9; too-large warning signs
      (slower decisions, weaker trust, coordination friction); one complex
      domain per team, never plus extras; no multiple complicated domains
      on one team.
- [ ] **Cognitive load is explicit** — intrinsic, extraneous, and germane
      load each appear with the matching executive move (accept / eliminate
      / protect).
- [ ] **Ownership is sharp** — exactly one owning team per system;
      stewardship, not private ownership; contribution via agreed paths.
- [ ] **Team API is concrete** — what a team exposes (code, docs, working
      practices, communication channels, roadmap) and the usability test.
- [ ] **The checklist survives intact** — all fifteen PDF sections
      reproduced in the Checklist tab (`checklist.md`), numbers preserved.
- [ ] **Credit is explicit** — References name Skelton & Pais's *Team
      Topologies* and point to the authors' materials at teamtopologies.com.

## Non-goals

- Not the four team types or three interaction modes — that is
  [[static-team-topologies]] and its siblings.
- Not fracture planes or how to draw boundaries — that is
  [[team-first-boundaries]]; this record establishes *why* the team is the
  unit those boundaries serve.
- Not [[organizational-design]] — that record covers sizing and state
  diagnosis in Larson's frame; this one covers the team-first stance
  underneath it.
- No claim that team-first design works without engineering foundations —
  the book is explicit that it does not, and so is this record.

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
  *The Engineering Executive's Primer*. The record reads the book through
  an executive lens and complements the Primer-grounded records.
- **2026-07-26** — Framed the record around two load-bearing ideas: the
  team as the unit of delivery/ownership/reward, and cognitive load as the
  budget every assignment must fit within. The Team API and engineering
  practices are consequences of those two, not a separate list.

## Sources

- **Internal**
  - `sources/checklists/appendix/team-topologies/Checklist_ Team
    Topologies _ Team-First Thinking.pdf` — the operating checklist;
    reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Matthew Skelton & Manuel Pais, *Team Topologies: Organizing Business
    and Technology Teams for Fast Flow* (IT Revolution Press, 2019) — the
    team-first chapters this record distills.

## Changelog

- **2026-07-26** — Comics modality staged (`comics.md`, Comic tab, shared
  VERA/LEO cast) with pending panel blocks; inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-26** — Article and checklist written from this spec; spec and
  post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-26** — Initial spec for the appendix record. Status `draft`.
  *(Željko, AI-mediated session)*
