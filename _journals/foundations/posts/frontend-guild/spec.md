---
status: draft
revised: 2026-05-20
---

# Spec: Frontend Guild as a Cross-Team Web Consortium

> Backfilled after the post. The companion record to [[backend-guild]],
> [[mobile-guild]], and [[genai-guild]] — same shape, different scope.

## Intent

Establish a Frontend Guild as a standing community of practice for **web
frontend** engineers across Organization teams, brands, and domains. The guild is
the organisation-wide web consortium that enables and empowers teams around
standards. The record should make the guild's purpose, mandate, and
boundaries (especially against mobile) legible enough that engineers can
decide where to take a given web concern.

## Audience

- **Web frontend engineers** across teams, brands, and domains who might
  join, contribute, or adopt guild standards.
- **Engineering managers and tech leads** trying to understand the guild's
  scope vs their own team's autonomy.
- **Mobile engineers** who need to know what is *not* in scope (mobile
  frontend is the Mobile Guild's job).
- **Architecture group + Chief Architect** as the receiving end of guild
  advice and proposals.
- **AI agents** cross-linking from other foundations.

## Success criteria

- [ ] Reader can state the guild's purpose, scope (web only), composition,
      mandate, and resources in their own words.
- [ ] Reader can distinguish "web consortium" from "standards body that
      mandates compliance" and "delivery team".
- [ ] Reader understands mobile frontend is explicitly out of scope, and
      knows the Mobile Guild exists for it.
- [ ] Reader sees the parallel with [[backend-guild]], [[mobile-guild]], and
      [[genai-guild]] and reads the four as one family of decisions.
- [ ] Reader can articulate when guilds coordinate vs absorb each other's
      scope (the web/mobile boundary).

## Non-goals

- Defining the design system, micro-frontend architecture, or other
  technical standards themselves — the guild *owns* those, the record does
  not pre-empt them.
- Creating an approval gate for frontend changes in delivery teams.
- Mandating that every team adopt every guild standard.
- Covering mobile frontend, which belongs to [[mobile-guild]].

## Open questions

- Exact Slack channel and AWS space naming — left to bootstrap.
- How "coordination" with the Mobile Guild works in practice when a topic
  genuinely spans both (e.g. design tokens shared across web and mobile).
- Whether the design-system working group becomes a long-lived sub-body of
  the guild or a separate record.

## Decision log

- **2026-05-20** — Kept the guild **advisory and contributory**, mirroring
  the other guilds. Considered standards-body authority that could mandate
  compliance; rejected because mandated standards die without grassroots
  ownership, and a consortium that earns adoption survives the next
  framework cycle.
- **2026-05-20** — Bounded scope to **web frontend** only. Considered
  folding mobile in for a single "frontend" body; rejected because mobile
  has materially different platforms, release cycles, and design
  constraints — better served by a dedicated [[mobile-guild]] with
  explicit coordination on shared topics.
- **2026-05-20** — Adopted **experimentation-first** documentation
  (working code in the guild's GitHub area first, prose after). Considered
  standards-first publication; rejected because frontend choices age
  fastest in this corpus and an experimentation-first cadence handles
  that better.
- **2026-05-20** — Membership **open to every Aviver**, small core
  organising group. Same trade-off as [[backend-guild]]: open membership
  with a sustaining core beats a closed roster.

## Sources

- **Internal**
  - [[backend-guild]] — sibling guild record; this spec was written to
    mirror its shape, with web-frontend-specific scope.
  - [[mobile-guild]] — sibling record; the web/mobile boundary in this
    spec was negotiated against it.
  - [[genai-guild]] — sibling record; informs the guild family pattern.
  - [[architecture-advisory-forum]] — destination for guild proposals
    that become decisions.
- **External**
  - Spotify guild/chapter/tribe model — pattern reference, not template.
  - Modern frontend platform writing (design systems, micro-frontends,
    white-label integration) — informs the topic surface the guild owns.

## Changelog

- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
