---
status: draft
revised: 2026-05-20
---

# Spec: Operational Principle — Cloud Native on AWS

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization builds on AWS using cloud-native patterns:
stateless services, horizontal scaling, AWS-managed services where
the value is clear, AWS-native operational primitives by default.
Deviations (self-managed alternatives, other clouds, non-cloud-native
shapes) require an ADR. Cloud-native does **not** mean
serverless-everywhere, multi-cloud-just-in-case, or rebuilding what
AWS already does well.

## Audience

- **Engineers** designing new services.
- **Architecture group** evaluating non-AWS or self-managed
  exceptions.
- **Operations team** owning the AWS-native primitives.

## Success criteria

- [ ] Reader can name the cloud-native attributes (stateless,
      horizontal, managed-where-valuable, AWS-native primitives).
- [ ] Reader knows what cloud-native does **not** mean.
- [ ] Reader knows deviations require an ADR.

## Non-goals

- Serverless-first architecture.
- Multi-cloud strategy.
- Banning self-managed components.

## Open questions

- Concrete bar for "self-managed has clear reason".

## Decision log

- **2026-05-20** — Chose **AWS-managed services where valuable**.
  Considered self-managed-by-default for control; rejected because
  the operational overhead outweighs control gains for most
  Organization workloads.
- **2026-05-20** — Stated what cloud-native is **not**. Considered
  positive-only definition; rejected because "cloud-native" is
  routinely misread as serverless-everywhere.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the cloud target.
  - [[infra-tech-stack-compute]] — the compute default.
  - [[infra-tech-stack-messaging]] — the messaging default.
- **External**
  - CNCF Cloud Native definition.
  - AWS Well-Architected Framework.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
