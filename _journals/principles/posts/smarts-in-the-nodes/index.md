---
id: "ORG-PRIN-SMARTS-IN-THE-NODES"
status: draft:gray
title: "Design Principle: Smarts in the Nodes, not the Network"
date: 2026-05-16
author: Organization Tech Strategy
permalink: smarts-in-the-nodes
timetoread: 12 min
excerpt: "Put business logic, routing decisions, and orchestration inside the services that own the work, not in the messaging fabric, API gateway, service mesh, or BPM tool that connects them. Organization's integration backbone - Kafka via Amazon MSK, ECS networking, AWS-native components - should remain dumb pipes that move data reliably. Smart middleware feels powerful at first and becomes the most expensive, least owned part of the platform within two years."
tags: design, decoupling, messaging, kafka, integration, choreography
logo: "assets/images/smarts-in-the-nodes/logo.jpeg"
logo_credit: "Inspired by the JLP Engineering Principles 'Smarts in the Nodes' principle"
icon: "assets/icons/smarts-in-the-nodes.png"
---

> **Status**: DRAFT
>
> **Principle**: Business behaviour lives in services that own a domain. The fabric that connects services - message brokers, gateways, meshes, integration tools - moves data and enforces transport-level concerns. It does not make business decisions. When orchestration is needed, it lives in a service that has a name, an owner, and an SLA, not in configuration on a middleware product.

## Statement

Organization designs follow the **end-to-end principle**: behaviour belongs at the endpoints, not in the network or middleware between them. Concretely:

* Services own their domain logic, including validation, routing, and orchestration.
* Kafka and MSK are durable, ordered pipes. They do not transform, enrich, or branch business data based on rules buried in configuration.
* API gateways and service meshes handle transport: TLS, authentication, retries, rate limits, traffic shaping. They do not contain feature logic.
* Choreography between autonomous services is preferred over centralised orchestration in a tool.
* Where orchestration is genuinely needed, it lives in a *service*, not in a vendor.

## How to Read This Principle

This principle is often confused with "no middleware" or "no orchestration". It is neither.

| What it says | What it does **not** say |
| --- | --- |
| Business logic belongs in services. | Middleware should not exist. |
| Orchestration goes in a service if needed. | Orchestration is forbidden. |
| Gateways and meshes do transport concerns. | Gateways and meshes are useless. |
| Choreography is the default. | Choreography solves all problems. |
| Kafka is a dumb, durable pipe. | Stream processing is forbidden. |

The principle is about *where decisions live*. A retry policy in a service mesh is fine. A branching workflow in the same mesh is not.

## How to Apply This Principle

Use this principle to:

* Distinguish transport concerns from business behaviour.
* Decide whether logic belongs in a service, broker, gateway, mesh, or workflow engine.
* Recognise when smart middleware is eroding ownership and observability.
* Explain why named services are safer homes for orchestration than anonymous configuration.

## Rationale

Smart middleware fails predictably for three reasons.

First, **ownership erodes**. Middleware tends to belong to a platform team, a vendor, or "everyone". Business rules placed in it are owned by no team that delivers product outcomes. When the rules need to change, the platform team becomes a bottleneck.

Second, **operational opacity grows**. Logic expressed in middleware configuration is harder to test, debug, and trace than logic expressed in service code. Failures present as routing anomalies instead of business errors.

Third, **lock-in deepens**. Smart middleware is hardest to leave: contracts grow inside it, runtime behaviour depends on it, and the cost of moving rises faster than the cost of staying. The next generation of platforms then has to either keep the smart middleware or accept a difficult migration.

Organization's tech stack pushes the opposite direction. Amazon MSK was chosen as a Kafka backbone for its durable log model, not its integration features. ECS Fargate keeps deployment and runtime concerns simple and node-shaped. Backend services on .NET are expected to do their own work, not to delegate it to an integration platform.

## Implications

* **Kafka topics carry domain events, not commands wrapped in middleware logic.** Producers describe what happened; consumers decide what to do.
* **No business rules in the broker.** Topic configuration covers retention, partitioning, and ordering. It does not encode routing decisions.
* **No business logic in the gateway or mesh.** Authentication, rate limiting, retries, and traffic policy yes; "if customer is German, route to service X" no.
* **Choreographed flows by default.** Each service reacts to events relevant to its domain.
* **When orchestration is needed, build a service for it.** Give it a name, an owner, and operational metrics, the same as any other service.
* **Workflow tools are services, not platforms.** If a workflow engine is used, it is owned by the team whose domain it serves; it does not become a shared dumping ground.
* **Stream processing is allowed for transport-shaped work** (filtering, joining, fan-out). It is not the place to put domain decisions.

## Placement Test

Before putting logic into a broker, gateway, mesh, workflow engine, or integration tool, ask:

* Which team owns the business rule?
* Can that team test, deploy, observe, and roll back the rule where it lives?
* Would a domain expert know to look in this place for the behaviour?
* Is the logic transport-shaped, or is it deciding product behaviour?
* Does moving the logic into middleware reduce coupling, or hide it?
* What happens when the rule needs to change urgently during an incident?
* Can the behaviour be represented as a named service instead?

If the rule needs domain language to explain it, it probably belongs in a domain service. If it can be explained as transport policy, middleware may be the right place.

## What This Means for Teams

For service teams:

* Treat your service as the only place your domain logic lives.
* Subscribe to the events you need and decide what to do with them inside your own code.
* Resist patterns that hide business behaviour in broker, gateway, or mesh configuration.
* When you need orchestration across multiple services, propose it as a service of its own, with an ADR.

For platform and integration teams:

* Keep Kafka and MSK as a managed, well-operated, *dumb* backbone.
* Keep API gateways and service meshes focused on transport-level concerns.
* Refuse change requests that would push business logic into the platform; redirect them to the service that should own the rule.

For tech leads:

* Watch for "let's just add it in the broker / gateway / mesh" shortcuts in design discussions.
* Push back on shared workflow tools that quietly grow into business-rules databases.
* Track which team would own a proposed rule before it gets added to any middleware.

## Anti-Patterns

* **Enterprise Service Bus revival.** A central component that knows the entire estate's routing, transformation, and orchestration rules.
* **Smart broker.** Business rules placed in Kafka Streams topologies, broker plugins, or proprietary middleware features.
* **Gateway-as-application.** API gateway configuration grows to include feature toggles, rewrites, and conditional flows that should live in services.
* **Mesh-as-router.** A service mesh that makes routing decisions based on business attributes rather than transport concerns.
* **Orchestration tool sprawl.** A workflow product adopted "just for one flow" that ends up containing the company's process model.
* **Hidden coupling via shared schemas.** Every service depends on one big shared schema in the broker, making the broker the de facto monolith.

## Examples

Aligned with the principle:

* A pricing service consumes listing-events from Kafka and computes prices internally. The broker does not know about pricing.
* The API gateway authenticates calls, applies rate limits, and forwards traffic. It does not run feature flags.
* A small orchestrator service exists to coordinate a checkout flow, owned by the checkout team, deployed and on-called like any other service.
* The service mesh handles mTLS and retries; routing-by-tenant lives in the service that knows what a tenant is.

Out of alignment with the principle:

* A Kafka Streams application that *only* the platform team can change, encoding domain rules the platform team does not understand.
* An integration product that grows to host most of the company's business logic, becoming the most fragile system in the estate.
* "Customer-aware" routing in the gateway that requires gateway operators to understand customer segments.
* A workflow tool that becomes the system of record for half the domain because it was easier than building services.

## Discussion Prompts

Use these prompts in integration reviews:

* Which part of this design is transport policy, and which part is business behaviour?
* Who can safely change the rule when product behaviour changes?
* Would naming a service make ownership and observability clearer than middleware configuration?

## Related Principles

* [[small-and-simple]] - smart middleware grows complex faster than smart services.
* [[evolutionary-systems]] - logic in services is easier to evolve than logic in vendor configuration.
* [[decisions-stay-with-teams]] - middleware-hosted logic erodes ownership.
* [[cloud-native-on-aws]] - prefer dumb, managed pipes from AWS over smart proprietary middleware.

## Scope and Revisiting

This principle applies to all integration between Organization services, including events, APIs, and batch flows. It applies to integration with AVIV Group and third parties insofar as Organization controls the integration layer.

It does not apply to product-level workflow exposed to users; that is the service's job to design.

The principle should be revisited if:

* A managed orchestration capability becomes simpler to own than the equivalent custom service.
* The cost of running many small services becomes higher than the cost of a centralised, smart middleware.
* The Kafka backbone evolves to support genuinely first-class, well-owned stream processing.

## Authoritative References

* J. H. Saltzer, D. P. Reed, D. D. Clark, *End-to-End Arguments in System Design*, ACM Transactions on Computer Systems, 1984.
* Sam Newman, *Building Microservices*, O'Reilly.
* John Lewis Partnership, [Smarts in the Nodes not the Network Principle](https://engineering-principles.jlp.engineering/).
* Martin Fowler, [Microservices and the First Law of Distributed Objects](https://martinfowler.com/articles/microservices.html).
