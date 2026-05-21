---
status: draft
revised: 2026-05-20
---

# Spec: Mobile Tech Stack — Start from AVIV's Native Baseline, Own the Apps

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Adopt AVIV Group's current native mobile baseline (Swift + SwiftUI on
iOS, Kotlin + Jetpack Compose on Android) as the **starting point**,
while making clear that Organization takes **its own source copies** and
operates them as Organization-owned product codebases from day one.
Alignment with AVIV is a fast start, not a standing commitment to
follow future AVIV mobile stack changes.

## Audience

- **Mobile engineers** picking up the inherited iOS and Android
  codebases.
- **Mobile tech leads** managing the fork relationship with AVIV.
- **Engineering leadership** sizing the "own the apps from day one"
  posture.
- **AVIV Group mobile teams** as the upstream relationship counterparty.

## Success criteria

- [ ] Reader can name the four baseline choices: Swift, SwiftUI,
      Kotlin, Jetpack Compose.
- [ ] Reader knows Organization **copies the source** and owns its forks
      from day one.
- [ ] Reader understands there is **no automatic upstream
      relationship** — AVIV changes do not become Organization changes
      by default.
- [ ] Reader sees the parallel with [[web-tech-stack]] — same
      "start from AVIV, own the fork" shape.
- [ ] The post stays focused as an ADR and does not absorb release
      runbook, SDK, architecture, or upstream-contribution detail.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Cross-platform stacks (Kotlin Multiplatform, React Native, Flutter)
  as a default.
- A standing commitment to follow AVIV Group's future mobile stack
  changes.
- Choosing specific SDKs, third-party libraries, or release tooling.
- Defining the upstream/downstream contribution model in detail.

## Open questions

- Process for selectively porting AVIV changes — opt-in mechanism
  and decision criteria.
- Whether and when to consider cross-platform alternatives.

## Decision log

- **2026-05-20** — Refocused the post around the baseline decision,
  source-copy ownership, exception criteria, and revisit triggers.
  Kept terminology as an appendix instead of inline explanation.
- **2026-05-20** — Chose **AVIV's native baseline as starting point**.
  Considered a green-field mobile stack; rejected because the
  inherited apps already exist and a rewrite would delay product work
  for no clear gain.
- **2026-05-20** — Took **source copies, Organization-owned**, not a
  shared codebase with AVIV. Considered a shared upstream; rejected
  because Organization needs ownership of release cycles, dependency
  upgrades, and roadmap decisions from day one.
- **2026-05-20** — Made the alignment **a starting point, not a
  standing commitment**. Considered binding Organization to AVIV's future
  stack; rejected because that would create coupled drift risk.

## Sources

- **Internal**
  - [[web-tech-stack]] — sibling record with the same shape (web,
    not mobile).
  - [[mobile-guild]] — the community of practice this baseline feeds
    into.
- **External**
  - Apple Swift, SwiftUI documentation.
  - Kotlin and Jetpack Compose documentation.
  - AVIV Group internal mobile platform documentation.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure
  and added end vocabulary appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
