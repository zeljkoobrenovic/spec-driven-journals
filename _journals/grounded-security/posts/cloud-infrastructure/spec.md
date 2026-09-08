---
status: accepted
revised: 2026-08-22
---

# Spec: Cloud Infrastructure

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the bar my organization holds its cloud estate to. The post turns the
Cloud Infrastructure chapter of the *Defensive Security Handbook* into an
operating record: the shared responsibility model is read correctly for
every service model — the provider secures the cloud infrastructure, we
secure our data, identities, configurations, and workloads; misconfiguration
is treated as the leading cloud risk and countered with continuous audits,
automated configuration monitoring, least privilege, and infrastructure as
code in source control behind code review and CI/CD security checks;
credentials and secrets are controlled with MFA on root and administrator
accounts and extended broadly, immediate offboarding, centralized identity
and SSO, no hardcoded secrets, repository scanning, a secrets service,
rotation, and an exposed-credential response process; IAM is least-privilege
RBAC with scoped roles, regular reviews, and alerts on privilege escalation;
the classic hygiene disciplines — inventory, patching, vulnerability
scanning, backups with tested restoration, DR planning, encryption, network
boundaries, log collection and monitoring — carry into the cloud under
recognized frameworks (CIS Controls, NIST CSF); architecture is deliberate,
using established patterns, tiering, segmentation, strict ACLs and security
groups, secured microservice and event-driven designs, provider reference
architectures, and the provider Well-Architected frameworks reassessed as
workloads change; detection is wired and tested — visibility, alerts, SIEM
centralization, cloud incident-response procedures, and alerts proven before
production reliance, with the chapter's AWS GuardDuty exercise
(SNS → GuardDuty → EventBridge → sample findings) as the worked example; and
compliance is treated as a baseline, not the end of the security program.

## Audience

Platform and infrastructure leads in my organization who own cloud accounts
(so they know the bar the estate is held to); security engineers auditing
cloud posture; peer executives who want to see what "the provider secures
the cloud, we secure what we put in it" concretely means. First-person
declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the shared-responsibility
      split, the misconfiguration-first threat model, the identity and IaC
      disciplines, tested detection, and closes with compliance-as-baseline.
- [x] **Service models and shared responsibility survive** — SaaS versus
      PaaS versus IaaS, what the provider secures per model, what the
      customer secures, the AWS/Azure/GCP shared-responsibility reviews, and
      the chapter's summary rule: the provider generally secures the cloud
      infrastructure while you secure your data, identities, configurations,
      and workloads.
- [x] **Misconfiguration prevention survives** — regular configuration
      audits, automated configuration monitoring with AWS Config, Azure
      Policy/Defender for Cloud, and Google Security Command Center named as
      the worked examples, least privilege, no overly permissive IAM roles,
      storage permissions, or firewall rules, IaC where possible, IaC in
      source control, code review before infrastructure changes deploy, and
      security checks in CI/CD pipelines.
- [x] **Credentials, secrets, and IAM survive** — strong password policies,
      a password vault, MFA on root and administrator accounts extended to
      all users where possible, immediate access removal on departure,
      centralized identity and SSO, no hardcoded secrets, repository
      scanning, a dedicated secrets service, regular rotation, and an
      exposed-credential response process; RBAC with job-scoped roles,
      regular permission reviews, removal of unused privileges, monitoring
      of privileged permission changes, and alerts on unexpected privilege
      escalation.
- [x] **Security hygiene survives** — cloud asset inventory, patching,
      continuous vulnerability scanning, backups of critical data with
      tested restoration, a disaster recovery plan, encryption of sensitive
      data, secured network boundaries (firewalls, VPNs, access controls),
      security log collection, retention, and monitoring, and recognized
      frameworks with CIS Controls and NIST CSF named.
- [x] **Architecture discipline survives** — established patterns over
      designed-from-scratch, three-tier separation where appropriate,
      segmentation so internal tiers are not internet-exposed, strict
      network ACLs and security groups, microservices considered where
      isolation and independent scaling pay with secured inter-service
      communication and dependency review, event-driven architecture with
      controls on producers, consumers, and channels, provider reference
      architectures as the starting point; the AWS, Azure, and Google Cloud
      Well-Architected/Architecture frameworks reviewed, security evaluated
      alongside reliability, performance, operations, and cost, and
      architecture reassessed as workloads and threats change.
- [x] **Detection and the GuardDuty exercise survive** — security-posture
      visibility, threat and vulnerability monitoring, alerts on important
      security events, SIEM centralization, cloud incident-response
      procedures, and testing alerts before relying on them; the full
      GuardDuty exercise (SNS topic and subscription, GuardDuty enablement
      and export frequency, the EventBridge rule to the SNS topic, sample
      findings generated and notifications verified end to end) reproduced
      in the checklist as the worked example of a tested detection pipeline.
- [x] **The final review survives** — the chapter's final security review,
      closing on compliance as a baseline, not the end of the program.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook*, the Cloud Infrastructure chapter checklist, and the
      frameworks the chapter names (CIS Controls, NIST CSF, the provider
      Well-Architected frameworks).

## Non-goals

- Not [[databases]] — cloud-hosted databases are held to that record's bar;
  this record covers the estate they run in.
- Not [[authentication]] — MFA, SSO, and centralized identity here apply to
  cloud accounts; the organization-wide identity model lives there.
- Not [[network-segmentation]] — tiering and ACLs here are cloud
  architecture; segmentation as a design discipline lives there.
- Not [[logging-and-monitoring]] — cloud logs and alerts feed the central
  pipeline; the pipeline itself lives there.
- Not [[compliance]] — this record adopts the chapter's closing rule that
  compliance is the baseline, not the program; the compliance frame itself
  lives there.
- Not a provider mandate — AWS, Azure, and GCP tools (AWS Config, Azure
  Policy/Defender for Cloud, Google Security Command Center, GuardDuty) are
  the worked examples; the commitments are stated at the capability level.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic *(added later with the visual layer)*

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Cloud Infrastructure chapter checklist of
  the *Defensive Security Handbook*, read through a practitioner-executive
  lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 14 _ Cloud Infrastructure.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the AWS GuardDuty exercise and the final
    security review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III; O'Reilly) — the Cloud Infrastructure
    chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
