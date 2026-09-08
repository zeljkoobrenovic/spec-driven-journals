---
status: accepted
revised: 2026-08-22
---

# Spec: Asset Management and Documentation

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of asset management in my organization: an ongoing security
program — not a one-time inventory exercise — built on one authoritative
source of truth. The post turns the "Asset Management and Documentation"
chapter of the *Defensive Security Handbook* into an operating record: every
asset has an owner, a criticality, and a risk rating; a rich inventory schema
spans network equipment, servers, endpoints, users and accounts,
applications, cloud assets, and certificates and domains; data is classified
and business owners are interviewed; criticality and risk connect the
inventory to security operations (patching, remediation, monitoring, incident
response, backup, access reviews); the asset lifecycle is managed end to end
— procure, deploy, manage, decommission — with verified data destruction at
disposal; discovery, reconciliation, and expiration alerting are automated
but validated before being trusted; unmanaged assets are treated as process
failures to investigate; and the program runs on a monthly/quarterly/annual
review rhythm. The load-bearing test: the inventory answers security
questions in minutes — which assets a new vulnerability affects, who owns a
critical system, what faces the internet — and is actively used for security
decisions, not simply maintained as documentation.

## Audience

Security and IT leaders in my organization who own or audit the asset
inventory (so they know the bar); infrastructure and cloud teams whose
resources must reconcile to the source of truth; peer executives who want to
see why "you cannot defend what you do not know you have" is an operating
commitment, not a slogan. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the program shape (one
      source of truth, owners on everything, full asset-class coverage,
      lifecycle to verified destruction, validated automation) and the final
      validation test: security questions answered in minutes, inventory
      used for decisions.
- [x] **Program-not-project framing survives** — scope and objectives
      defined, asset management as an ongoing security process, owners or
      custodians on every asset or group, naming conventions, documented
      process, executive sponsor, cross-functional team.
- [x] **Single source of truth survives** — one authoritative system, teams
      know which it is, integration over duplication, write access defined,
      backed up, versioned, regularly reviewed; repository sized to the
      organization with a plan to migrate before basic tools break down.
- [x] **Schema and classification survive** — the full inventory schema
      (ID through last-verification date); the data-classification scheme
      with handling, access, encryption, sharing, retention, and disposal
      requirements; the business/data-owner interview questions.
- [x] **Criticality and risk connect to operations** — business impact and
      compromise impact assessed, documented ratings, and inventory data
      driving patching, remediation, monitoring, labeling, incident
      response, backup, access reviews, testing, and lifecycle decisions.
- [x] **Every asset class survives** — network equipment, servers, desktops
      and endpoints, users and accounts (including privileged, service, and
      shared accounts), applications, cloud assets (monitoring/logging,
      users and secrets, network, databases, compute and storage, IAM
      policies), certificates and domains including dangling-DNS review.
- [x] **Lifecycle survives** — procure, deploy (default credentials
      replaced, patched, scanned, encrypted), manage (change tracking),
      decommission (revoke access, sanitize, verify, certify); secure
      disposal of storage media with approved destruction methods.
- [x] **Automation with validation survives** — automated discovery (ARP,
      DHCP, scanning, SNMP, OS interfaces), integrations (vulnerability
      scanners, endpoint management, IAM, cloud, IaC), change tracking,
      expiration and anomaly alerting, reporting — with automated data
      validated before being treated as authoritative, and unmanaged assets
      investigated and their bypass process corrected.
- [x] **Review rhythm and final validation survive** — the monthly,
      quarterly, and annual review cadences and the full final program
      validation question set reproduced in the checklist.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the "Asset Management and Documentation" chapter
      checklist.

## Non-goals

- Not [[security-program]] — the one-time baseline sweep that grounds the
  program lives there; this record makes knowing-what-we-have a standing
  capability.
- Not [[vulnerability-management]] — vulnerability data is integrated with
  asset records here; the scan-triage-remediate loop lives there.
- Not [[cloud-infrastructure]] — cloud assets are inventoried here; cloud
  hardening and guardrails live there.
- Not [[endpoints]] — endpoints are inventoried here; endpoint hardening
  lives there.
- Not [[policies]] — the asset-management and disposal policies referenced
  here get their document discipline there.
- Not a CMDB product selection — the record commits to one authoritative
  system sized to the organization, not to a tool.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the visual layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the "Asset Management and Documentation"
  chapter checklist of the *Defensive Security Handbook* (Lee Brotherston,
  Amanda Berlin, and William F. Reyor III), read through a
  practitioner-executive lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 02 _ Asset Management and Documentation.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final program validation.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the "Asset Management and
    Documentation" chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
