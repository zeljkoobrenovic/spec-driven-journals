---
id: "ORG-PRIN-OBSERVABLE-BY-DEFAULT"
status: draft:gray
title: "Operational Principle: Observable by Default"
date: 2026-05-16
author: Organization Tech Strategy
permalink: observable-by-default
timetoread: 12 min
excerpt: "Every Organization service emits structured logs, useful metrics, and distributed traces from day one. Observability is not a feature added after an incident; it is a default property delivered by templates, libraries, and the platform. The goal is not dashboards; the goal is to answer 'what just happened, where, and why?' in minutes for any production system. Without observability, every other operational principle collapses into guesswork."
tags: operations, observability, logging, metrics, tracing, slos
logo: "assets/images/observable-by-default/logo.jpeg"
logo_credit: "Inspired by Charity Majors and the JLP Engineering Principles"
icon: "assets/icons/observable-by-default.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization services are **Observable by Default**. Structured logs, metrics, and traces are produced by every service from the day it is created, using shared shapes, shared destinations, and shared correlation. Observability is delivered by golden templates, libraries, and platform defaults, not bolted on after the first incident.

## Statement

Every Organization service emits:

* **Structured logs** in a consistent JSON shape, with shared fields (trace ID, span ID, service name, environment, correlation IDs).
* **Metrics** covering the four golden signals (latency, traffic, errors, saturation) plus business-relevant signals where relevant.
* **Distributed traces** with consistent trace propagation across service boundaries and asynchronous flows.
* **Health and readiness signals** aligned with the runtime.
* **Service-level objectives** for user-visible behaviour, not just internal metrics.

All three pillars flow through AWS-native destinations (CloudWatch and equivalents) with the option of additional overlays where justified.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Observability is a default. | Observability solves itself. |
| Use shared shapes and destinations. | Use exactly one observability tool. |
| Emit logs, metrics, and traces. | Emit everything possible. |
| SLOs frame what matters. | SLOs replace operational sense. |
| Observability supports debugging. | Observability is for dashboards. |

The principle is about answering questions in production, not about volume of telemetry.

## How to Apply This Principle

Use this principle to:

* Explain the difference between observability and having dashboards.
* Identify the questions logs, metrics, traces, and SLOs should answer during an incident.
* Design telemetry with shared shapes, correlation, and ownership from service creation.
* Recognise alert noise and unowned dashboards as reliability risks.

## Rationale

The most expensive minutes in an incident are the ones spent trying to figure out *what is happening*. The cost is paid in lost availability, lost customer trust, and lost engineering time. Observability is the only mitigation that reliably reduces those minutes.

Observability also pays compounding dividends outside incidents:

* Capacity planning becomes evidence-based.
* Performance regressions become detectable rather than felt.
* Deploys gain feedback loops via canary metrics and trace deltas.
* New joiners learn the system from real behaviour, not stories.

It only works if observability is *consistent*. Logs in five formats, metrics in three systems, and traces in none means each service is investigated differently. The principle is therefore as much about shared *shape* as about shared *coverage*.

Organization's wider stack supports this: AWS provides default destinations (CloudWatch, X-Ray) and integration with ECS, MSK, and AVIV Group's central tooling. Claude Code can be used to enforce observability patterns through Skills, templates, and CI checks.

## Implications

* **Templates emit telemetry from line one.** New service templates ship with structured logs, metrics, and traces enabled.
* **Shared library or shared sidecar.** Telemetry shape is enforced centrally, not negotiated per service.
* **Correlation IDs are propagated everywhere.** HTTP, Kafka, batch jobs, scheduled tasks.
* **Logs are structured.** Unstructured log lines are an exception, not a default.
* **High-cardinality events are first-class.** Wide events with many attributes are more useful than narrow events with rolled-up metrics alone.
* **SLOs are defined for user-visible behaviour.** Internal latency is a leading indicator, not a final goal.
* **Alerting is symptom-based.** Page on user impact, not on every internal anomaly.
* **Dashboards have owners.** A dashboard with no owner is a dashboard nobody trusts.

## Debugging Test

A service is observably healthy when an engineer who did not write it can answer these questions quickly during an incident:

* What changed recently?
* Which users, tenants, regions, or flows are affected?
* Where did the request or event go after it entered the system?
* Which downstream dependency is slow, failing, or saturated?
* Is the problem a deploy, data shape, dependency, load pattern, or configuration change?
* Is user-facing reliability inside or outside the SLO?
* What should be rolled back, disabled, scaled, or escalated?

If the answer requires guessing, asking the original author, or reading production code under pressure, the service is not observable enough.

## What This Means for Teams

For service teams:

* Use the standard logging library, the standard metrics conventions, and the standard tracing setup.
* Add structured event logs for the operations your service does for users, not only for the code paths.
* Define SLOs that reflect what your users (internal or external) actually care about.
* Treat alerts you mute as bugs in the alerting, not as background noise.

For platform and SRE roles:

* Own the templates, libraries, and platform defaults that deliver observability.
* Keep CloudWatch and any overlay tooling working together rather than competing.
* Provide patterns for trace propagation through MSK and asynchronous flows.

For tech leads:

* Block production launches that miss observability defaults.
* Push for SLO definition during design, not during the first incident.

## Anti-Patterns

* **Unstructured log spew.** Free-text log lines with no shared fields, requiring grep gymnastics to debug.
* **Metric explosion without meaning.** Hundreds of dashboards, none of which answer real questions.
* **Tracing in one service.** Distributed tracing that stops at the first hop, so the trace is no use distributed.
* **Alert fatigue.** Pagers tuned to ringing, so genuine incidents are lost in noise.
* **Owner-less dashboards.** A graveyard of dashboards left behind by ex-projects.
* **Bolt-on observability.** Logging and metrics added after an incident, then forgotten until the next.
* **Observability vendor lock-in by accident.** Telemetry that only works on one vendor's stack because shape was tied to the vendor.

## Examples

Aligned with the principle:

* A new ECS Fargate service ships with structured JSON logs, OpenTelemetry traces, and CloudWatch metrics from its first commit.
* Kafka producers and consumers propagate trace headers; a single trace links a user request to all downstream consumers.
* An SLO of "99.5% of search responses under 400ms" is defined alongside the service, with error budget burn alerts.
* Each service has an "owned dashboards" list in its README.

Out of alignment with the principle:

* A service ships with `print` statements as logs because "we'll add proper logging in a sprint".
* Three teams use three different trace propagation schemes; traces cannot be joined.
* Metrics exist but no SLOs are defined; on-call decides what is wrong by feel.
* Alerts trigger on every internal anomaly, half of them muted by default.

## Discussion Prompts

Use these prompts in readiness or incident reviews:

* What question could we not answer quickly in the last incident?
* Which dashboard, alert, or SLO has no clear owner?
* Where does trace or correlation context break across a service boundary?

## Related Principles

* [[production-ready]] - observability is a readiness item.
* [[cloud-native-on-aws]] - AWS-native observability is the default destination.
* [[evolutionary-systems]] - observability is required for safe incremental change.
* [[governance-as-code]] - observability defaults are enforced via templates and CI.
* [[ai-output-must-be-governed]] - AI-generated changes need observability to be safely validated.

## Scope and Revisiting

This principle applies to every Organization service, pipeline, and integration that runs in production or pre-production. It also applies to internal platforms whose failure would affect production.

It does not apply to one-off scripts or experiments with no production exposure, though even there structured logs are a habit worth keeping.

The principle should be revisited if:

* The AWS observability stack changes meaningfully (for example, a managed OpenTelemetry destination becomes standard).
* Cost of telemetry becomes a significant operational driver and requires reshaping defaults.
* A new compliance requirement forces specific retention or redaction patterns.

## Authoritative References

* Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering*, O'Reilly.
* Google SRE Workbook, [Implementing SLOs](https://sre.google/workbook/implementing-slos/).
* OpenTelemetry, [Specification](https://opentelemetry.io/docs/specs/).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
