---
status: accepted
revised: 2026-10-22
---

# Spec: Protecting Dealers and Data: Security for a Vehicle Data Platform

## Intent

Show what threatens a platform that sells vehicle facts by the call and runs the daily work of thousands of dealers, and which defenses belong in its architecture rather than in its tooling. The chapter builds a vehicle-specific threat model (plate and VIN enumeration, BOLA in dealer APIs, credential stuffing at dealer logins, API key leakage by integrators, ransomware with the June 2024 CDK Global attack as industry context, supply-chain risk from channel and DMS adapters, insider misuse, register-transaction fraud) and designs the controls: enumeration defense on lookup paths, scoped credentials and their lifecycle, step-up authentication for high-risk dealer actions, segmentation by cell and adapter zone, secrets, immutable backups and restore drills. It explains what the FTC Safeguards Rule asks of US dealers' vendors, what ISO/IEC 27001 and SOC 2 do and do not prove, and how NIS2 (and the Dutch *Cyberbeveiligingswet*) changes the incident runbook. After reading, an architect can say for each endpoint whether it needs an object check or enumeration defense, and can write a credential policy.

Productscape bricks covered: `iden` (accounts, credentials, MFA), `vapi` (data API access, keys, rate limits).

## Audience

Chief architects, security leads and principal engineers at vehicle-data providers and dealer-software vendors, including those with consumer check products. They should leave with a threat model they can adapt, a layered design for lookup endpoints, a scoped-credential policy and a view of which regulatory clocks apply.

## Success criteria

- [ ] The chapter defines **enumeration defense** and **scoped credential** precisely and distinguishes object authorization (BOLA) from licensed lookup of any object.
- [ ] The Plate Enumeration Attack (August 2027: 3,800 addresses, about 9 million requests, 6 days, leaked trial keys, Odolo free check and JSON API) is told with timeline, detection signal, what leaked and what changed.
- [ ] A threat-model table names entry point, reach, Axleby exposure, controls and owning chapter for each threat.
- [ ] At least three mermaid diagrams: the layered lookup path, the credential lifecycle, the security zones.
- [ ] A requirements table gives consistency, latency, freshness and fail mode for security controls.
- [ ] FTC Safeguards, ISO 27001/SOC 2 and NIS2 are covered with dated primary sources; NIS2 scope for SaaS is labeled as a legal judgement.
- [ ] Failure handling covers distributed walks, conflicting revocation, incomplete inventory, partial control failure, partner compromise and own-cell compromise.
- [ ] The Across Markets table distinguishes cybersecurity law, reporting clocks, assurance and plate sensitivity by market.

## Non-goals

- Authentication mechanisms, SSO, SCIM, ReBAC and API credential types in depth: [[identity-access-and-entitlements]].
- Tenant context propagation, RLS and leak tests: [[tenancy-and-dealer-groups]].
- License register and purpose check: [[data-licensing-and-governance]].
- Upstream cost and spend-cap economics: [[scale-and-cost]].
- Degraded modes and DMS outage handling: [[reliability-and-dependencies]], [[dms-integration]].
- Lawful basis, retention and breach assessment under GDPR: [[privacy-and-retention]].
- What consumers may see in a check: [[consumer-vehicle-checks]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether a vertical dealer-SaaS or data-API provider is a NIS2 "cloud computing service" is unsettled; the chapter states Axleby's counsel's conservative reading as fiction and labels the general point as inference.
- Belgium's national NIS2 text and the UK Cyber Security and Resilience Bill's current stage were not verified.
- CDK's containment architecture is undocumented; the cell argument is labeled as inference.

## Decision log

- **2026-10-22** — Split "plate lookup" security into object authorization vs enumeration defense, because a data product legitimately answers about any car.
- **2026-10-22** — Made the Odolo teaser (history and damage counts) the valuable leak, so the response tier, not the rate limit, is the central control.
- **2026-10-22** — Used the no-hit rate from Meterline outcomes as the detection signal, tying security to the metering design.
- **2026-10-22** — Treated NIS2 via the Dutch Cbw (in force 15 August 2026) and Implementing Regulation 2024/2690 to show a concrete 24-hour early-warning step in the runbook.

## Sources

- **Internal**
  - [[meet-axleby]], `_research/scenario-ledger.md` — the Plate Enumeration Attack, DriveDesk Outage, systems.
  - `_research/brief-platform-apis-operations.md` Part 6; `brief-saas-tenancy-billing.md` Part 8; `brief-connected-data-privacy-regulation.md` 5.2, 6.2; `brief-dms-integration.md` Parts 3 and 6.
  - [[identity-access-and-entitlements]], [[tenancy-and-dealer-groups]], [[scale-and-cost]], [[onboarding-and-configuration]], [[dms-integration]].
- **External**
  - OWASP API Security Top 10 (2023): API1, API2, API4, API7, API9.
  - CISA #StopRansomware Guide (2023); GitHub secret scanning partner program.
  - FTC Safeguards Rule FAQ (2025), guidance (2024), 16 CFR 314.4.
  - NIS2 (CELEX 32022L2555); Implementing Regulation (EU) 2024/2690; NCSC Netherlands on the Cbw; BSI NIS2 page; UK DSIT CSR Bill page.
  - Sam Curry's automotive write-ups (2023, 2024); CyberScoop, BleepingComputer, TechTarget on CDK (2024).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: NIS2 early-warning criterion spelled out; buzzword removed; Cbw date and Kia write-up verified; timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
