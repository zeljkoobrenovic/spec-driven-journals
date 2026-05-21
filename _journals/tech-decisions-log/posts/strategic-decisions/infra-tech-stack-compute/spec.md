---
status: draft
revised: 2026-05-20
---

# Spec: Compute Infrastructure — Docker, ECS Fargate, Ubuntu Base Images

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Commit Organization to a **simple, mainstream, AWS-native compute pattern**:
Docker containers on AWS ECS with the Fargate launch type, using Ubuntu
as the foundational base image. Three orthogonal choices (packaging,
orchestration, hosting model) made together to remove diversity and
prevent fragmentation across Lambda, EKS, EC2, and self-managed
Kubernetes.

## Audience

- **Backend engineers** packaging a new service.
- **Platform / devex team** maintaining base images and templates.
- **Architecture group** evaluating exception requests for Lambda,
  EKS, or EC2.
- **Cost-conscious leadership** sizing the Fargate spend vs alternatives.

## Success criteria

- [ ] Reader can separate **packaging** (Docker + Ubuntu),
      **orchestration** (ECS), and **hosting model** (Fargate).
- [ ] Reader knows ECS Fargate is the **default**; alternatives need
      written exceptions.
- [ ] Reader understands why **ECS over EKS**: easier to own,
      sufficient for Organization's needs.
- [ ] Reader can connect to [[infra-tech-aws]] (provider) and
      [[backend-tech-stack-framework]] (.NET runs here).
- [ ] The post stays focused as an ADR and does not absorb service
      template, deployment-module, runbook, or learning-path detail.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Lambda or serverless function patterns as a default.
- Self-managed Kubernetes or EKS as default orchestration.
- Choosing service templates, IaC tools, or CI/CD pipelines.
- Dictating image-size or build-pipeline optimisations.

## Open questions

- Concrete criteria for an "approved exception" (latency-sensitive
  Lambda, GPU workloads, anything else).
- Migration plan for services currently on non-default compute.

## Decision log

- **2026-05-20** — Refocused the post around the ECS Fargate default,
  the included operational expectations, exception criteria, and
  revisit triggers. Kept terminology as an appendix instead of inline
  explanation.
- **2026-05-20** — Chose **ECS Fargate** as default. Considered EKS;
  rejected because Kubernetes operational complexity exceeds
  Organization's needs and ECS is sufficient.
- **2026-05-20** — Chose **Ubuntu** as base image. Considered Alpine
  for size; rejected because Alpine's musl libc surfaces subtle
  compatibility issues with mainstream runtimes that cost more
  engineer-hours than the smaller image saves.
- **2026-05-20** — Default **does not** include Lambda. Considered
  Lambda-first for event-driven workloads; rejected because
  serverless-only architectures fragment the runtime story and Kafka
  consumers fit poorly with cold-start patterns.
- **2026-05-20** — Default **does not** include EC2 launch type for
  general workloads. Considered EC2 for cost reasons; rejected
  because owning EC2 fleets is exactly the operational overhead
  Fargate removes.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the cloud target this builds on.
  - [[infra-tech-stack-aws-foundation]] — the foundation it runs on.
  - [[infra-tech-stack-messaging]] — Kafka clients run on this
    compute.
  - [[backend-tech-stack-framework]] — the .NET services that target
    this compute.
- **External**
  - AWS ECS and Fargate documentation.
  - Docker official image guidance for production deployments.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed learning/checklist material, and moved vocabulary to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
