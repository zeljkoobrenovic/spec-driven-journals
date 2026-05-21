---
status: draft
revised: 2026-05-20
---

# Spec: Mobile Guild as a Cross-Team Mobile Consortium

> Backfilled after the post. Companion to [[backend-guild]],
> [[frontend-guild]], and [[genai-guild]]; mirrors the Frontend Guild shape
> with mobile-specific scope.

## Intent

Establish a Mobile Guild as a standing community of practice for **mobile**
engineers (native iOS, native Android, cross-platform stacks, mobile shells)
across Organization teams, brands, and domains. The guild is the
organisation-wide mobile consortium that enables and empowers teams around
standards. The record should make purpose, mandate, and boundaries (against
web frontend) legible enough that engineers can decide where a given mobile
concern lives.

## Audience

- **Mobile engineers** across teams, brands, and domains.
- **Engineering managers and tech leads** sizing the guild's scope against
  their team's autonomy.
- **Web frontend engineers** who need to know mobile is out of scope for
  [[frontend-guild]] and lives here instead.
- **Architecture group + Chief Architect** as the receiving end of guild
  advice and proposals.
- **AI agents** cross-linking from other foundations.

## Success criteria

- [ ] Reader can state the guild's purpose, scope (mobile only), composition,
      mandate, and resources in their own words.
- [ ] Reader understands that native iOS, native Android, cross-platform
      stacks, and mobile-specific shells are all in scope; web is not.
- [ ] Reader can distinguish "mobile consortium" from "delivery team",
      "standards body that mandates compliance", and "platform team".
- [ ] Reader sees the parallel with the other three guild records and reads
      them as one family of decisions.
- [ ] Reader knows where to take topics that span web and mobile (explicit
      coordination, not absorption).

## Non-goals

- Defining the mobile design system, app architecture, or release model
  themselves — the guild *owns* those once chartered.
- Creating an approval gate for mobile changes in delivery teams.
- Covering web frontend, which belongs to [[frontend-guild]].
- Mandating native vs cross-platform tooling choices.

## Open questions

- Naming of the Slack channel and AWS space — bootstrap-time decision.
- Whether cross-platform stacks (Kotlin Multiplatform, React Native, Flutter)
  get their own sub-working-groups inside the guild.
- How store-delivery and release tooling sits with platform/devex vs the
  guild.

## Decision log

- **2026-05-20** — Kept the guild **advisory and contributory**, mirroring
  [[backend-guild]] and [[frontend-guild]]. Considered standards-body
  authority for native platforms; rejected because Apple's and Google's
  own conventions dominate, and the guild's value is in shared practice,
  not a competing rule set.
- **2026-05-20** — Bounded scope to **mobile only** — native iOS,
  native Android, cross-platform stacks, mobile shells. Considered
  folding web into "frontend"; rejected for the same reason
  [[frontend-guild]] excludes mobile (different platforms, release
  cycles, design constraints).
- **2026-05-20** — Treated **cross-platform stacks** (Kotlin
  Multiplatform, React Native, Flutter) as in scope. Considered scoping
  to native only; rejected because cross-platform decisions are exactly
  the kind of cross-team topic the guild exists to host.
- **2026-05-20** — Membership **open to every Aviver**, small core
  organising group. Same trade-off as the other guilds.

## Sources

- **Internal**
  - [[backend-guild]] — sibling guild record; this spec mirrors its
    shape with mobile-specific scope.
  - [[frontend-guild]] — sibling record; the web/mobile boundary in this
    spec was negotiated against it.
  - [[genai-guild]] — sibling record; informs the guild family pattern.
  - [[architecture-advisory-forum]] — destination for guild proposals
    that become decisions.
- **External**
  - Spotify guild/chapter/tribe model — pattern reference, not template.
  - Apple Human Interface Guidelines, Material Design — the
    platform-native conventions the guild operates inside.

## Changelog

- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
