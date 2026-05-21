---
status: draft
revised: 2026-05-20
---

# Spec: Roadmap for AI-Assisted Modernization

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Provide a **phased rollout plan**: establish policy and standards,
teach teams the workflow, build reusable capabilities, scale adoption,
and **measure whether complexity is actually going down**. The last
phase is the test — if complexity isn't going down, the strategy
isn't working.

## Audience

- **Engineering leadership** sequencing the rollout.
- **AI Engineering Enablement** owning per-phase work.
- **Teams** consuming each phase.

## Success criteria

- [ ] Reader can name the phases.
- [ ] Reader knows the **measurement gate** at the end.
- [ ] Reader knows "complexity going down" is the success metric,
      not AI activity.

## Non-goals

- Specifying exact dates.
- Replacing tactical project planning.

## Open questions

- Concrete metrics for "complexity going down".

## Decision log

- **2026-05-20** — Made **measurement** the last phase.
  Considered making it parallel; rejected because measurement
  without rollout is theoretical.
- **2026-05-20** — Used **complexity reduction** as success metric.
  Considered AI activity / generated code; rejected because activity
  != outcome.

## Sources

- **Internal**
  - [[strategic-principles]] — what's being rolled out.
  - [[claude-code-enablement]] — what's being built.
  - [[operating-model]] — who runs it.
- **External**
  - DORA Accelerate — informs the measurement framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
