---
status: draft
revised: 2026-05-20
---

# Spec: Design Principle — Smarts in the Nodes, not the Network

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that business logic, routing decisions, and orchestration live
**inside the services** that own the work — not in the messaging
fabric, API gateway, service mesh, or BPM tool. Organization's
integration backbone (Kafka via MSK, ECS networking, AWS-native
components) stays **dumb pipes that move data reliably**. Smart
middleware feels powerful at first and becomes the most expensive,
least owned part of the platform within two years.

## Audience

- **Backend engineers** choosing where to put logic.
- **Architecture group** evaluating BPM, ESB, or service-mesh
  proposals.
- **Platform owners** of Kafka, gateways, meshes.

## Success criteria

- [ ] Reader can identify "smart middleware" anti-patterns (logic
      in gateway configuration, transformation in Kafka Streams
      pipelines, routing rules in BPM).
- [ ] Reader knows orchestration needs a **service with a name,
      owner, and SLA**.
- [ ] Reader sees Kafka and MSK as durable pipes, not logic.

## Non-goals

- Banning gateways, meshes, or BPM tools.
- Defining specific Kafka topic conventions.

## Open questions

- Where the line falls for cross-cutting concerns (auth, rate
  limiting) that genuinely belong in the fabric.

## Decision log

- **2026-05-20** — Chose **end-to-end principle** framing.
  Considered service-mesh-first; rejected because mesh-resident
  logic is the worst kind of hidden coupling.
- **2026-05-20** — Required orchestration to be **a named
  service**. Considered allowing tool-resident orchestration
  (BPM); rejected because BPM tools accumulate undocumented
  business rules that nobody owns.

## Sources

- **Internal**
  - [[evolutionary-systems]] — companion design principle.
  - [[small-and-simple]] — companion design principle.
  - [[infra-tech-stack-messaging]] — the Kafka/MSK target.
- **External**
  - JLP Engineering Principles "Smarts in the Nodes".
  - Saltzer, Reed, Clark — end-to-end argument in system design.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
