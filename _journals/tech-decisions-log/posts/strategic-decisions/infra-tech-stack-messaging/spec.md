---
status: draft
revised: 2026-05-20
---

# Spec: Messaging Infrastructure — Amazon MSK as the Kafka Backbone

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Commit Organization to **Amazon MSK** as the strategic Kafka backbone for
backend messaging, with SQS / SNS / EventBridge available for narrow
use cases but not the default. Make the **skills-investment cost**
explicit — Kafka is genuinely new to Organization, and building expertise
is part of the cost of this decision, not a footnote.

## Audience

- **Backend engineers** choosing between Kafka, SQS, SNS, and
  EventBridge for a given integration.
- **Architecture group** evaluating exceptions toward Pulsar, Kinesis,
  or Confluent Cloud.
- **Engineering leadership** sizing the Kafka skills-investment.
- **Data and analytics teams** consuming event streams downstream.

## Success criteria

- [ ] Reader knows **MSK (managed Kafka)** is the default for durable
      event streams and async service-to-service integration.
- [ ] Reader can identify when SQS / SNS / EventBridge is acceptable
      (simple queues, AWS-native fan-out, AWS-service event routing).
- [ ] Reader sees Kafka skills-investment as part of the decision,
      not a hidden surprise.
- [ ] Reader can trace dependencies to [[infra-tech-aws]] and
      [[infra-tech-stack-compute]].
- [ ] The post stays focused as an ADR and does not absorb topic
      design, schema-governance, consumer implementation, or learning
      path detail.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Self-managed Kafka on EC2 or third-party Kafka-as-a-Service.
- Choosing schema registry, serialization formats, or topic naming
  conventions.
- Defining the migration plan from existing messaging.
- Dictating consumer/producer client library specifics.

## Open questions

- Concrete training plan for Kafka expertise (timeline, mentors,
  reference implementations).
- Where the SQS / SNS / EventBridge boundary sits in practice —
  guidelines on "narrow well-justified use case".

## Decision log

- **2026-05-20** — Refocused the post around the MSK default,
  Kafka/SQS/SNS/EventBridge boundary, skill cost, exception criteria,
  and revisit triggers. Kept terminology as an appendix instead of
  inline explanation.
- **2026-05-20** — Chose **Amazon MSK** as the Kafka provider.
  Considered Confluent Cloud; rejected because it sits outside the
  AVIV Group AWS contract and operating model, raising commercial
  and integration friction. Considered self-managed Kafka on EC2;
  rejected because Organization has neither the in-house expertise nor
  the desire to operate Kafka infrastructure.
- **2026-05-20** — Made **Kafka the default** for async integration.
  Considered SQS/SNS as the default; rejected because Kafka's durable
  log model is the better fit for the event-driven backend shape this
  ADR series is building toward.
- **2026-05-20** — Kept **SQS, SNS, EventBridge** as accepted narrow
  options. Considered banning them; rejected because they are the
  right tool for specific use cases (simple queues, AWS-native
  routing) and a Kafka-only world adds friction without value.
- **2026-05-20** — Explicitly accepted the **skills-investment cost**
  in the decision body, not as a footnote. Considered downplaying it;
  rejected because hidden costs surface later as surprises.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the cloud target.
  - [[infra-tech-stack-compute]] — where Kafka clients run.
  - [[backend-tech-stack-framework]] — the .NET clients that produce
    and consume Kafka events.
- **External**
  - Amazon MSK documentation.
  - Apache Kafka documentation and protocol reference.
  - Confluent Cloud (considered and rejected).

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed tutorial/learning-path material, and moved vocabulary to an
  end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
