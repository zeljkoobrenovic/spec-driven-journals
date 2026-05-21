---
status: draft
revised: 2026-05-20
---

# Spec: Backend Guild as a Cross-Team Community of Practice

> Backfilled after the post. Captures the contract this record holds the
> organisation to, so future revisions stay anchored.

## Intent

Establish a Backend Guild as a standing community of practice for backend and
distributed-systems engineers across Organization teams, brands, and domains —
without turning it into a governance body. The record should make the
guild's purpose, mandate, and resourcing legible enough that any engineer can
decide whether and how to participate.

## Audience

- **Backend engineers** across teams, brands, and domains who might join,
  contribute, or pull from the guild's golden paths.
- **Engineering managers and tech leads** trying to understand what the guild
  is and isn't responsible for relative to their team.
- **Architecture group + Chief Architect** as the receiving end of guild
  advice and proposals.
- **AI agents** picking up the file to extend or cross-link from other
  foundations.

## Success criteria

- [ ] Reader can state the guild's purpose, composition, mandate, and
      resources in their own words.
- [ ] Reader can distinguish the guild from a delivery team, an architecture
      review board, and a procurement function.
- [ ] Reader knows the guild is advisory and contributory, not decisional.
- [ ] Reader can locate the Slack channel, repos, and AWS space (or
      understand they exist and are dedicated).
- [ ] Reader recognises the parallel shape with [[frontend-guild]],
      [[mobile-guild]], and [[genai-guild]] without confusing scopes.

## Non-goals

- Defining backend golden paths themselves. The record establishes the body
  that owns them, not the paths.
- Creating an approval gate for backend changes in delivery teams.
- Standardising backend tech choices across all teams.
- Replacing the [[architecture-advisory-forum]] as the venue for
  cross-team architecture advice.

## Open questions

- Concrete naming for the Slack channel and the AWS space — left to
  bootstrap.
- How the guild interacts with domain-specific architecture working groups
  (overlap or hand-off?).
- Whether external thought-leadership coordination should be its own record
  later.

## Decision log

- **2026-05-20** — Kept the guild **advisory and contributory**, not a
  governance body. Considered a decision-making board to give it teeth;
  rejected because it would duplicate the [[architecture-advisory-forum]]
  and undermine team-owned decisions.
- **2026-05-20** — Scoped the guild to **backend and distributed
  systems**. Considered a broader "platform" scope including
  infrastructure and devex; rejected because it would blur the boundary
  with the platform team and dilute the guild's centre of gravity.
- **2026-05-20** — Made guild membership **open to every Aviver**.
  Considered a fixed roster for accountability; rejected because closed
  membership turns guilds into ad-hoc architecture boards in practice.
- **2026-05-20** — Provisioned a **dedicated AWS account or space**.
  Considered shared sandbox accounts; rejected because reference
  implementations need owned space and shared sandboxes blur ownership.
- **2026-05-20** — Adopted a **bi-weekly cadence** rather than monthly or
  weekly. Bi-weekly is the rhythm most likely to sustain without becoming
  a calendar burden or losing momentum.

## Sources

- **Internal**
  - [[frontend-guild]] — companion guild record; same shape, different
    scope.
  - [[mobile-guild]] — companion guild record.
  - [[genai-guild]] — companion guild record with a four-pillar mandate.
  - [[architecture-advisory-forum]] — the forum where guild proposals
    surface as ADRs. Boundary between the guild (community of practice)
    and the AAF (advice ritual) was checked against this record.
  - [[ai-mediated-authoring]] — the workflow this spec was authored
    through.
- **External**
  - Spotify's guild/chapter/tribe model — read as inspiration, not
    template. The "advisory only" framing here is deliberately distinct
    from Spotify's "chapter lead" authority.
  - Andrew Harmel-Law, *Scaling the Practice of Architecture,
    Conversationally* — informs the advice-process framing the guild
    operates inside.

## Changelog

- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
