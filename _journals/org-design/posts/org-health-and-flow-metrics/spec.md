---
status: draft
revised: 2026-05-20
---

# Spec: Organisation Health and Flow Metrics

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization uses a **balanced** engineering health and flow
measurement system: product outcomes, delivery flow, reliability,
quality, developer experience, team health — reviewed together.
Metrics are used to **improve the system of work**, not to rank
individuals, maximise activity, or create a single productivity
score.

## Audience

- **Engineering leadership** reviewing metrics.
- **Engineering managers** using metrics for team improvement.
- **Teams** receiving feedback from metrics.
- **HR** ensuring metrics don't become surveillance.

## Success criteria

- [ ] Reader can name the **six dimensions** (product, delivery,
      reliability, quality, devex, team health).
- [ ] Reader knows metrics are for **system improvement**, not
      individual surveillance.
- [ ] Reader knows there is **no single productivity score**.

## Non-goals

- Specifying exact metrics.
- Defining individual performance criteria (separate concern).

## Open questions

- How to weight the six dimensions when they conflict.

## Decision log

- **2026-05-20** — Chose **balanced** measurement over single score.
  Considered a productivity-score-of-engineering; rejected because
  single scores invite gaming.
- **2026-05-20** — Made metrics **for systems, not individuals**.
  Considered individual scoring; rejected because that destroys
  trust without improving outcomes.

## Sources

- **Internal**
  - [[goal-setting-and-planning-cadence]] — companion framework.
  - [[performance-feedback-and-review]] — kept separate.
- **External**
  - DORA Accelerate metrics, SPACE framework, DevEx framework.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
