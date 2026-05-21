---
status: draft
revised: 2026-05-20
---

# Spec: Operational Principle — Observable by Default

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that every Organization service emits **structured logs, useful
metrics, and distributed traces from day one**. Observability is
delivered by golden templates, libraries, and platform defaults — not
bolted on after the first incident. The goal is not dashboards; it is
to answer "what just happened, where, and why?" in minutes for any
production system.

## Audience

- **Engineers** building new services.
- **Platform team** maintaining shared observability defaults.
- **On-call engineers** depending on the data.

## Success criteria

- [ ] Reader knows observability is a **default**, not a feature
      added later.
- [ ] Reader can name the three observability outputs (logs,
      metrics, traces).
- [ ] Reader knows the four golden signals (latency, traffic,
      errors, saturation).

## Non-goals

- Specifying the observability vendor.
- Defining specific dashboards (those are team-level).

## Open questions

- How strict to be about correlation-ID propagation across
  service boundaries.

## Decision log

- **2026-05-20** — Made observability a **default**, not a feature.
  Considered "observability when needed"; rejected because incidents
  need data that wasn't being collected.
- **2026-05-20** — Required **all three** (logs, metrics, traces),
  not just one. Considered metrics-only; rejected because each
  answers different debugging questions.

## Sources

- **Internal**
  - [[production-ready]] — companion operational principle.
- **External**
  - Charity Majors writing on observability.
  - SRE Book — four golden signals.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
