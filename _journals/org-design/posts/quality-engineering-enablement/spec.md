---
status: draft
revised: 2026-05-20
---

# Spec: Quality Engineering as Enablement

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization treats quality as a **team-owned engineering
responsibility**, supported by quality engineering enablement. QA is
**not** a late release gate that receives finished work. Quality
engineers help teams design risk-based test strategies, automate
confidence, improve observability, run exploratory testing, and
strengthen release discipline.

## Audience

- **Product engineering teams** owning quality.
- **Quality engineers** providing enablement.
- **Tech leads** designing test strategies.
- **Release managers** evaluating release readiness.

## Success criteria

- [ ] Reader knows quality is **team-owned**, not QA-gated.
- [ ] Reader can describe the QE role as **enablement**, not
      gatekeeping.
- [ ] Reader sees the connection to [[jira-workflow-standards]] split
      QA queue (which still applies as enablement, not gatekeeping).

## Non-goals

- Eliminating QA expertise — it lives in QE enablement.
- Replacing testing in CI.

## Open questions

- How to staff QE enablement (centralised vs embedded).

## Decision log

- **2026-05-20** — Treated quality as **team-owned**. Considered
  centralised QA gating; rejected because gating decouples quality
  from team accountability.

## Sources

- **Internal**
  - [[jira-workflow-standards]] — the QA workflow shape.
  - [[production-ready]] — quality is part of production-readiness.
- **External**
  - Modern Testing (Alan Page, Brent Jensen) — quality engineering
    pattern.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
