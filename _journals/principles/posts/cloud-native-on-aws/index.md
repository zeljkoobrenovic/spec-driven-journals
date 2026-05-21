---
id: "ORG-PRIN-CLOUD-NATIVE-ON-AWS"
status: draft:gray
title: "Operational Principle: Cloud Native on AWS"
date: 2026-05-16
author: Organization Tech Strategy
permalink: cloud-native-on-aws
timetoread: 12 min
excerpt: "Organization is an AWS company. Build cloud-native by default: managed services where they remove operational toil, AWS-native primitives where they fit, and self-managed alternatives only when there is a written reason. Cloud-native means stateless, horizontally scalable, deployable through automation, and observable through standard AWS interfaces. It does not mean serverless-everywhere, multi-cloud-just-in-case, or rebuilding what AWS already does well."
tags: cloud, aws, managed-services, msk, ecs, fargate, operations
logo: "assets/images/cloud-native-on-aws/logo.jpeg"
logo_credit: "Inspired by Organization's AWS-centric tech-decisions log"
icon: "assets/icons/cloud-native-on-aws.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization builds on AWS using cloud-native patterns: stateless services, horizontal scaling, AWS-managed services where the value is clear, and AWS-native operational primitives (IAM, VPC, CloudWatch, Secrets Manager, MSK, ECS) by default. Deviations - self-managed alternatives, other clouds, or non-cloud-native shapes - require an ADR, not a preference.

## Statement

Cloud Native on AWS at Organization means:

* **AWS** is the strategic public cloud. Backend workloads consolidate there.
* **Managed services** are preferred where they remove operational toil without significantly worsening cost, control, or portability.
* **Stateless services** are the default; state lives in managed datastores and managed brokers.
* **Horizontal scaling** is the default growth model.
* **IAM, VPC, secrets, logs, metrics, traces** flow through AWS-native interfaces.
* **MSK, ECS Fargate, Ubuntu base images** are the chosen managed primitives for the backend.

A workload is cloud-native on AWS when it scales horizontally, deploys through automation, integrates with AWS-native observability, and depends on managed services for state.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| AWS is the strategic cloud. | Multi-cloud is forbidden under all circumstances. |
| Managed services are preferred. | Every workload must be serverless. |
| Stateless is the default service shape. | State is never allowed. |
| Use AWS-native primitives. | Avoid all third-party tools on AWS. |
| Deviations need an ADR. | Deviations are unwelcome. |

The principle commits to a primary cloud and a primary set of patterns. It does not mandate any single AWS product family for every workload.

## How to Apply This Principle

Use this principle to:

* Explain what "cloud-native on AWS" means beyond simply running in AWS.
* Choose managed AWS primitives when they reduce operational toil.
* Identify when self-managed infrastructure or another cloud needs an ADR.
* Separate workload fit from cloud-product preference.

## Rationale

Organization has consolidated on AWS via the AVIV Group contract for procurement leverage, scale, and a coherent operating model. That choice only pays off if the engineering posture matches it: cloud-native services on AWS get more out of the shared platform than near-cloud or anti-cloud designs do.

Cloud-native services are easier to:

* Scale predictably under load.
* Recover after instance, AZ, or even regional failure.
* Operate with shared tools and shared eyes.
* Secure through IAM and VPC primitives.
* Govern through tagging, organisations, and central guardrails.

Self-managed alternatives - self-hosted Kafka, self-managed Kubernetes, self-built secret stores - are valid in narrow cases, but they re-introduce operational work that the platform team would otherwise not need to do. Each one is a slow tax.

The principle does not push toward "serverless-everything". ECS Fargate was chosen over Lambda-everywhere because the workload shape is mostly long-running services, not bursty event-driven functions. The cloud-native pattern follows the workload, not the brochure.

## Implications

* **Stateless services first.** Persistent state lives in managed datastores (RDS, Aurora, DynamoDB, S3) or managed brokers (MSK), not on service instances.
* **Use ECS Fargate as the default runtime.** Containers, Ubuntu base, AWS-managed networking.
* **Use MSK as the default broker.** Kafka is the messaging backbone; MSK is the managed implementation.
* **Use AWS-native observability.** CloudWatch logs, metrics, X-Ray traces, with the option of overlaying additional tooling where justified.
* **Use IAM as the access primitive.** No homegrown auth between services unless there is no AWS-native option.
* **VPC and networking are inherited from AVIV Group** during the 6-12 month inheritance period and simplified deliberately afterwards.
* **Multi-AZ is the default for production workloads.** Multi-region is justified per workload.
* **Multi-cloud is by exception.** A workload may run elsewhere if there is a specific reason - data locality, regulatory, vendor - documented in an ADR.

## Decision Heuristics

When choosing a cloud shape, start from these questions:

* Can this workload run as a stateless container on ECS Fargate?
* Can state live in an AWS-managed datastore, broker, cache, or object store?
* Can access be expressed through IAM, VPC boundaries, and standard secrets handling?
* Can logs, metrics, traces, and alarms use the standard AWS observability path?
* Does the managed service remove more operational work than it adds in cost, limits, or lock-in?
* If a self-managed service is proposed, which operational burden is the team explicitly accepting?
* If another cloud is proposed, what requirement cannot be met inside AWS?

The expected answer is not always "AWS managed service". The expected behaviour is that non-AWS-native choices are made with their full operational cost visible.

## What This Means for Teams

For service teams:

* Default to ECS Fargate, MSK, and AWS-native datastores for new work.
* Avoid building stateful services unless the state genuinely belongs in the service.
* Use AWS Secrets Manager, AWS IAM, and standard observability paths.
* Prefer scaling out over scaling up; prefer multi-AZ over heroic single-AZ designs.

For platform and SRE roles:

* Provide the AWS-native primitives as golden paths.
* Curate where AWS-managed services are the right answer and where they are not.
* Track when an AWS service becomes available that obsoletes a self-managed alternative.

For tech leads:

* Use AWS-native first as a starting question, not a constraint.
* Bring proposals that diverge from AWS-native to the Architecture Advisory Forum early.

## Anti-Patterns

* **Just-in-case multi-cloud.** Building portability that no one will use, paying complexity tax every day for a hypothetical migration.
* **Bring-your-own everything.** Self-managed databases, brokers, and orchestrators on AWS instances when the managed equivalents would do.
* **Lift-and-shift forever.** Workloads moved to AWS but never refactored to use AWS-native primitives.
* **Stateful service drift.** Services accumulating state on local disk or in-process caches because the managed datastore "felt slow".
* **Serverless-everywhere by default.** Treating Lambda as the only valid AWS shape for every workload regardless of profile.
* **Cloud-native theatre.** Containers and Kubernetes adopted as "modern" while the design is still a single-node monolith.

## Examples

Aligned with the principle:

* A new backend service runs on ECS Fargate, talks to MSK, stores state in Aurora Postgres, uses Secrets Manager, and is observed through CloudWatch.
* A team chooses Aurora over a self-managed PostgreSQL because the managed-service trade-offs are acceptable.
* MSK is used as the Kafka backbone instead of Confluent Cloud or self-hosted Kafka because it stays inside the AVIV Group AWS contract.

Out of alignment with the principle:

* A team deploys a "Kafka cluster" on EC2 because they prefer it to MSK, with no ADR.
* A new database is introduced in a different cloud because a vendor demo was compelling.
* A service stores state on local Fargate disk to avoid the managed-database setup.

## Discussion Prompts

Use these prompts in onboarding or team reviews:

* Which part of our workload is genuinely special, and which part can follow the AWS golden path?
* What operational work are we accepting when we choose self-managed infrastructure?
* Which old lift-and-shift workload should be revisited for AWS-native simplification?

## Related Principles

* [[small-and-simple]] - managed services reduce operational complexity.
* [[evolutionary-systems]] - AWS-native primitives evolve with the platform.
* [[smarts-in-the-nodes]] - managed pipes are dumb on purpose; smarts stay in services.
* [[inherit-then-simplify]] - inherited AWS tooling is simplified, not abandoned.
* [[observable-by-default]] - AWS-native observability is the default.

## Scope and Revisiting

This principle applies to backend services, data pipelines, integrations, and supporting infrastructure that Organization operates.

It does not apply to client-side applications (web, mobile), to AVIV Group services that Organization consumes but does not run, or to genuinely on-premise systems that are out of scope.

The principle should be revisited if:

* The AVIV Group AWS relationship changes materially.
* A managed AWS service decision needs to be re-evaluated against a new alternative.
* Compliance or data-residency requirements force workloads off AWS in ways the current pattern cannot accommodate.

## Authoritative References

* AWS, [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).
* CNCF, [Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md).
* John Lewis Partnership, [Cloud Native Principle](https://engineering-principles.jlp.engineering/).
* Organization Tech Decisions Log, [Public Cloud: Consolidate on AWS via AVIV Group Contract](../tech-decisions-log/infra-tech-aws.html).
