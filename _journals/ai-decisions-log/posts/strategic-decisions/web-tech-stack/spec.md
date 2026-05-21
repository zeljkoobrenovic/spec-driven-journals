---
status: draft
revised: 2026-05-20
---

# Spec: Web Tech Stack — Start from AVIV's Golden Path, Own the Fork

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Adopt AVIV Group's current Web Golden Path (React, TypeScript, Gemini
Design System, Unified Frontend) as the **starting point**, while making
clear that Organization takes **its own source copies** of the Gemini Design
System and Unified Frontend and operates them as Organization-owned
platforms from day one. Alignment with AVIV is a fast start, not a
standing commitment.

## Audience

- **Web engineers** picking up the inherited stack and design system.
- **Web tech leads** managing the fork relationship with AVIV.
- **Engineering leadership** sizing the "own the platforms from day
  one" posture.
- **AVIV Group web teams** as the upstream relationship counterparty.

## Success criteria

- [ ] Reader can name the four baseline choices: React, TypeScript,
      Gemini Design System, Unified Frontend.
- [ ] Reader knows Organization **copies the source** of Gemini and
      Unified Frontend and owns the forks from day one.
- [ ] Reader understands **no automatic upstream relationship** —
      AVIV changes do not become Organization changes by default.
- [ ] Reader sees the parallel with [[mobile-tech-stack]] — same
      "start from AVIV, own the fork" shape.
- [ ] The post stays focused as an ADR and does not absorb build-tool,
      contribution-model, release, or implementation-guide detail.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Choosing a different UI framework (Vue, Angular, Svelte) as
  default.
- A standing commitment to follow AVIV Group's future web stack
  changes.
- Defining specific React, TypeScript, or build-tool versions.
- Detailing the upstream/downstream contribution model.

## Open questions

- Mechanism for selectively porting AVIV Gemini / Unified Frontend
  changes.
- Whether and when to consider alternatives to React or TypeScript.

## Decision log

- **2026-05-20** — Refocused the post around the baseline decision,
  Organization-owned platform copies, exception criteria, and revisit
  triggers. Kept terminology as an appendix instead of inline
  explanation.
- **2026-05-20** — Chose **AVIV's Web Golden Path as starting point**.
  Considered green-field stack selection; rejected because inherited
  components already exist and a rewrite would delay product work.
- **2026-05-20** — Took **source copies, Organization-owned**, of Gemini
  Design System and Unified Frontend. Considered consuming them as
  shared upstream packages; rejected because Organization needs ownership
  of release cycles and roadmap decisions from day one.
- **2026-05-20** — Made the alignment **a starting point, not a
  standing commitment**. Same trade-off as in [[mobile-tech-stack]].

## Sources

- **Internal**
  - [[mobile-tech-stack]] — sibling record with the same shape
    (mobile, not web).
  - [[frontend-guild]] — the web community of practice this baseline
    feeds into.
- **External**
  - React, TypeScript documentation.
  - AVIV Group internal Web Golden Path documentation (Gemini Design
    System, Unified Frontend).

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure
  and added end vocabulary appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
