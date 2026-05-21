---
status: draft
revised: 2026-05-20
---

# Spec: Current State and Problem

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Define the **current-state problem**: three architecture paradigms
(.NET/TFS monolith, Java/GitLab microservices with self-managed Kafka,
Node.js/GitHub serverless), three repository ecosystems, hidden
legacy behaviour, and too much operational variation. Establish that
the technology problem is **modernization from a fragmented baseline**
— not a lack of AI tools.

## Audience

- **Engineering leadership** validating the diagnosis.
- **Tech leads** of the three estate paradigms.
- **Strategy reviewers** sanity-checking the baseline.

## Success criteria

- [ ] Reader can name the three architecture paradigms.
- [ ] Reader knows the problem is **fragmentation**, not lack of AI.
- [ ] Reader knows baseline data must be collected for measurement.

## Non-goals

- Prescribing the modernization path (covered downstream).
- Listing every legacy system.

## Open questions

- What baseline metrics matter most.

## Decision log

- **2026-05-20** — Framed problem as **modernization from
  fragmentation**, not lack-of-AI. Considered AI-readiness framing;
  rejected because it leads to "buy more AI" responses.

## Sources

- **Internal**
  - [[introduction]] — the framing.
  - [[strategic-principles]] — how to respond.
  - [[strategy-by-landscape]] — per-paradigm strategies.
- **External**
  - Strangler Fig pattern (Martin Fowler).

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
