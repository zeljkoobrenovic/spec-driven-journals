---
status: draft
revised: 2026-05-20
---

# Spec: Ownership Clarification Plan

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Operationalise [[policy]] P5: every major system, platform surface, and
legacy estate gets **one accountable owner**. Where ownership is
genuinely shared, separate operational owner from decision owner
explicitly. First wave focuses on three named hotspots: legacy AWS
estate, delivery tooling estate, and shared legacy messaging /
integration surfaces (Kafka, RabbitMQ). Avoid "clarify everything at
once" failure mode by naming specific first-wave targets.

## Audience

- **Engineering leadership** assigning owners.
- **Platform owners** of the three hotspot areas.
- **[[operate]] forum** tracking ownership clarification progress.
- **Strategy owner** ensuring no major surface stays unowned.

## Success criteria

- [ ] Reader can name the three first-wave hotspots.
- [ ] Reader knows the distinction between **operational owner**
      and **decision owner** for genuinely shared platforms.
- [ ] Reader understands "legacy without an owner is not
      acceptable".
- [ ] Reader sees why this plan names specific hotspots rather than
      clarifying everything at once.

## Non-goals

- Naming individual humans as owners (organisational concern).
- Replacing existing functional team structures.
- A complete ownership map for the entire estate.

## Open questions

- Process for handling disputed ownership claims.
- How to surface "legacy without an owner" candidates
  systematically.

## Decision log

- **2026-05-20** — Chose **named first-wave hotspots**, not
  organisation-wide clarification. Considered tackling ownership
  uniformly; rejected because "everything at once" tends to produce
  nothing.
- **2026-05-20** — Separated **operational vs decision owner** for
  shared platforms. Considered a single owner role; rejected
  because shared platforms have legitimate distinct operational and
  decisional concerns.
- **2026-05-20** — Stated **legacy without an owner is not
  acceptable**. Considered allowing legacy to stay unowned;
  rejected because unowned legacy is the primary cause of
  ownership-related delivery drag.

## Sources

- **Internal**
  - [[policy]] — P5 ownership clarity.
  - [[implications]] — implication 6 (ownership clarity is part of
    technical work).
  - [[diagnosis]] — unclear ownership evidence.
  - [[operate]] — the mechanisms that surface ownership work.
- **External**
  - Team Topologies (Skelton & Pais) — informs the
    operational-vs-decision split.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
