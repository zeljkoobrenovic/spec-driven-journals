---
status: draft
revised: 2026-05-20
---

# Spec: Backend Blueprint and Convergence Plan

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Define the **default shape** for new and evolving product backend work:
conventional microservice model, standard AWS patterns, clear bounded
contexts, explicit owner, service-owned data, synchronous API by
default, selective async only when justified. Backend fragmentation is
the strongest architectural mismatch in [[diagnosis]] and the main
technical focus of [[policy]] P2; this is the most important per-area
blueprint in the strategy.

## Audience

- **Backend engineers** building new services.
- **Tech leads** evaluating exception requests.
- **Architecture group** reviewing convergence proposals.
- **Domain owners** of overlap-zone systems being converged.

## Success criteria

- [ ] Reader can name the **six default attributes** of a
      strategy-compliant service (bounded context, contract, owner,
      data, sync, justified async).
- [ ] Reader knows three first-wave convergence targets: overlap
      zones, shared messaging surfaces, shared-database coupling.
- [ ] Reader can state the four refusals: new paradigm,
      shared-database coupling, serverless-first product backend,
      new messaging pattern without reason.
- [ ] Reader can apply the "definition of done for a
      strategy-compliant service" checklist.

## Non-goals

- Naming specific systems to converge.
- A target service count.
- Replacing existing serverless components that already work and
  have clear ownership.

## Open questions

- Exact criteria for "justified async" — needs examples that
  reviewers can pattern-match against.
- Migration path for monolithic systems that don't fit the bounded-
  context shape.

## Decision log

- **2026-05-20** — Chose **conventional microservice** as default.
  Considered serverless-first; rejected because cold-start and
  vendor-lock-in friction outweighs the simplicity for the target
  workload shape.
- **2026-05-20** — Made **synchronous API the default**, async
  only-when-justified. Considered event-driven by default; rejected
  because event-driven architectures look simple until you debug
  them.
- **2026-05-20** — Required **service-owned data**. Considered
  shared databases for high-traffic reads; rejected because
  shared-database coupling is exactly the fragmentation the strategy
  wants to remove.
- **2026-05-20** — Wrote **four refusals**, not just defaults.
  Considered relying on the policy refusal list; rejected because
  backend-specific refusals need backend-specific language.

## Sources

- **Internal**
  - [[diagnosis]] — backend fragmentation evidence.
  - [[policy]] — P2 backend convergence.
  - [[backend-tech-stack-framework]] — the .NET runtime target.
  - [[infra-tech-stack-compute]] — the compute target.
  - [[infra-tech-stack-messaging]] — the messaging target.
- **External**
  - Microservices literature (Newman, Richardson) — informs the
    "conventional" defaults.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
