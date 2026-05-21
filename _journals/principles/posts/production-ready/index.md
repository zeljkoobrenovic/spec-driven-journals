---
id: "ORG-PRIN-PRODUCTION-READY"
status: draft:gray
title: "Operational Principle: Production Ready"
date: 2026-05-16
author: Organization Tech Strategy
permalink: production-ready
timetoread: 12 min
excerpt: "A service is not done when it works in staging. It is done when it is fit to run in production. That means observability, health checks, secrets handling, deploy and rollback, capacity, on-call ownership, runbooks, security defaults, and data-protection considerations are all in place before traffic flows. Production-readiness is a property of the *service*, validated against an explicit checklist, owned by the team that runs it. It is not a stage in a release plan."
tags: operations, production, sre, on-call, observability, reliability
logo: "assets/images/production-ready/logo.jpeg"
logo_credit: "Inspired by the JLP Engineering Principles 'Production Ready' principle"
icon: "assets/icons/production-ready.png"
---

> **Status**: DRAFT
>
> **Principle**: An Organization service is **Production Ready** when it can be operated safely and recoverably by the team that owns it. Production-readiness is checked against an explicit list, signed off by the owning team, and refreshed on a regular cadence. Services that fail the list do not receive production traffic, regardless of how complete the features are.

## Statement

Production Ready means a service has:

* **Ownership**: a named team, an on-call rotation, and a documented escalation path.
* **Observability**: structured logs, metrics, and traces with consistent shapes.
* **Health**: liveness and readiness checks aligned with the runtime.
* **Deployability**: automated build, deploy, and rollback through CI/CD.
* **Configurability**: secrets and configuration loaded from approved sources.
* **Resilience**: documented behaviour under partial failure, retries, timeouts.
* **Capacity**: known limits and a known scaling strategy.
* **Security**: authentication, authorisation, transport, and dependency hygiene.
* **Data**: classification of data handled, retention, and protection.
* **Runbooks**: written, current, and discoverable.

A service that ships without these is not "early"; it is *not production ready*.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Readiness is a checklist on the service. | Readiness is a one-time gate at launch. |
| The owning team confirms readiness. | A central team approves readiness. |
| The bar is consistent across services. | The bar is identical regardless of risk. |
| Production-readiness can be lost. | Once granted, it is permanent. |
| The list is small enough to read. | The list grows freely. |

The point is to make readiness a property maintained by the team, not a stage in a release process.

## How to Apply This Principle

Use this principle to:

* Explain why feature completeness is not production readiness.
* Evaluate a service against ownership, observability, deployability, resilience, security, data, and runbook expectations.
* Treat readiness as a maintained property rather than a launch ceremony.
* Recognise when a service has lost production readiness after going live.

## Rationale

Outages, near-misses, and slow incidents share root causes that are often unglamorous: a missing log line, an unowned alert, a deploy that cannot be rolled back, a runbook that links to a deleted document, a secret in a config file. None of those root causes are technically hard to fix. They go unfixed because they are nobody's main job, until they are an incident.

A Production Ready checklist makes the unglamorous explicit. It puts the responsibility for each item on the team that runs the service. It removes the ambiguity about whether a service is "ready enough" by replacing taste with a list.

The principle aligns with the way Organization's platform is shaping up. ECS Fargate provides standard places to wire health checks, observability, and deploy. AWS provides standard places to manage secrets and access. The platform's job is to make the readiness items easy to satisfy; the team's job is to satisfy them.

## Implications

* **A platform-supported checklist exists.** It is short, current, and reflects what is genuinely needed.
* **Readiness is the owning team's call.** A team confirms its own service against the list and is accountable for the answer.
* **Going live requires readiness.** Production traffic is gated by the readiness state.
* **Readiness can be revoked.** A service that loses ownership, stops emitting metrics, or accumulates unanswered alerts is no longer ready.
* **Risk shapes scope, not standards.** A higher-risk service may need more, but never less than the baseline.
* **Defaults satisfy most items.** Templates, base images, and platform defaults should pre-satisfy logging, metrics, health checks, deploy, and secrets.
* **Runbooks live near the service.** Stored in the repository or a known location, kept current, written for the person paged at 3am.

## Readiness Tests

Before production traffic flows, the owning team should be able to demonstrate readiness rather than assert it.

Useful tests:

* Can a new engineer find the owner, runbook, dashboards, alerts, and escalation path in five minutes?
* Can the team deploy and roll back without manual infrastructure work?
* Can the service lose a dependency and fail in the documented way?
* Can an on-call engineer distinguish "service is down" from "dependency is down" from "traffic changed"?
* Are secrets rotated through the approved path?
* Are data classification, retention, and deletion responsibilities clear?
* Has the team practiced at least one likely failure mode?

Production-ready is not a promise that nothing will fail. It is evidence that the team can understand, contain, and recover from failure.

## What This Means for Teams

For service teams:

* Use the platform defaults so most items are satisfied without custom work.
* Treat the readiness checklist as a small, ongoing job, not a launch gate.
* Practice rollback regularly enough that you trust it.
* Run game days for non-trivial services.
* When your service changes shape - new data, new traffic, new dependencies - re-check readiness.

For platform and SRE roles:

* Maintain the readiness checklist as a real, working document.
* Make the items cheap to satisfy via defaults, templates, and tooling.
* Detect drift: services without ownership, stale runbooks, silent alerts.
* Treat readiness as a shared signal, not a stick.

For tech leads:

* Build readiness into delivery plans, not after them.
* Block launches that materially miss readiness; do not let them slide on the promise of a follow-up.

## Anti-Patterns

* **"Production-ready means features work."** Features in staging are not the same as a service in production.
* **Launch and forget.** A service goes live and never has its readiness re-checked.
* **Orphan services.** Services in production with no named owner; their on-call is "whoever notices".
* **Vanity dashboards.** Metrics that look impressive but are unrelated to user-facing reliability.
* **Runbooks as wishes.** "Restart and see" is not a runbook.
* **Untested rollback.** Rollback exists in theory; nobody has run it under pressure.
* **Secret in a file.** Secrets in config files because the secret store felt like extra work.
* **Readiness theatre.** A checkbox exercise that says yes regardless of the actual state.

## Examples

Aligned with the principle:

* A new backend service ships on .NET, ECS Fargate, Ubuntu base, with structured logs, metrics, traces, health checks, and rollback wired up before launch.
* Secrets come from AWS Secrets Manager via the standard pattern.
* A runbook in the service repo lists the top five alerts and the first action for each.
* The team runs a quarterly game day and refreshes the runbook based on what they learned.

Out of alignment with the principle:

* A service ships with logs but no metrics or traces because "we'll add them later".
* On-call is "whoever was last in the repo".
* Rollback has not been used in production in 18 months and nobody is sure it still works.
* A runbook page is the original launch slide deck.

## Discussion Prompts

Use these prompts before launch and after incidents:

* What would the on-call engineer need at 3am that is still missing?
* Which readiness item are we treating as follow-up work, and what risk does that create?
* How would we prove rollback, escalation, and observability work before traffic arrives?

## Related Principles

* [[observable-by-default]] - readiness depends on visible signals.
* [[cloud-native-on-aws]] - readiness uses AWS-native primitives where they exist.
* [[capabilities-follow-ownership]] - services in production must have a named owner.
* [[governance-as-code]] - readiness items should be enforced by automation where possible.

## Scope and Revisiting

This principle applies to every service that receives production traffic, processes production data, or is part of a production-critical pipeline. It applies whether the service is owned by an Organization product team or maintained from an AVIV Group inheritance.

It does not apply to internal experiments, ad-hoc scripts, or sandboxes with no production data and no production traffic.

The principle should be revisited if:

* The platform changes shape enough that the checklist needs major re-shaping (for example, a move to a different runtime).
* Major regulatory or compliance requirements add or remove items.
* Repeated incidents reveal that the current checklist is missing a category.

## Authoritative References

* Google SRE Book, [Service Best Practices and Readiness Reviews](https://sre.google/sre-book/).
* Susan J. Fowler, *Production-Ready Microservices*, O'Reilly.
* John Lewis Partnership, [Production Ready Principle](https://engineering-principles.jlp.engineering/).
* AWS, [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
