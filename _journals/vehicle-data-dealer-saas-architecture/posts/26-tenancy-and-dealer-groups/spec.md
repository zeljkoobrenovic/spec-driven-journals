---
status: accepted
revised: 2026-10-22
---

# Spec: Dealers, Groups and Rooftops: Tenancy Models for Dealer SaaS

## Intent

Show how a dealer SaaS platform should define and isolate tenants when its customers range from one-rooftop independents to 46-rooftop groups that buy, sell and reorganize sites. The chapter separates tenancy as a data model (what a tenant is; the hierarchy of organization, legal entity, region, rooftop and department; mandatory tenant ids) from tenancy as infrastructure (pool, silo, bridge, cells), and compares the infrastructure models explicitly against stated requirements (isolation, cost to serve, noisy neighbors, compliance, enterprise demands, restructuring, blast radius, one product) with labeled assumptions. It then covers tenant context propagation through every layer, row-level security and its gaps, per-tenant keys, cross-tenant features and their rules, restructuring (rooftop transfer, tenant merge, internal reorganization), tenant-aware observability and cost attribution. After reading, an architect can write a tenancy decision record for their own platform.

Productscape bricks covered: `iden` (customer account hierarchy: companies, branches, users; the tenancy gap noted in the digest).

## Audience

Chief architects, principal engineers and platform leads of dealer-software vendors and vehicle-data groups, especially those who inherited several products with different tenant models through acquisition. They should leave with a tenant definition, a layered isolation checklist, and a requirements-driven way to answer "do we need a dedicated environment for this customer?"

## Success criteria

- [ ] The reader can state why the tenant should be the contracting organization with rooftops as versioned children, and when that breaks.
- [ ] The chapter contains an explicit pool vs silo vs bridge comparison against at least seven named requirements, with assumptions labeled.
- [ ] The Cross-Tenant Lead (June 2027: 112 leads, 3 dealers, 47 minutes, ICO report) is told with its root cause and each layered control that would have stopped it.
- [ ] Tenant context propagation covers edge, services, caches, database (RLS and the MySQL gap), search, events, objects, telemetry and egress.
- [ ] Cross-tenant features (group views, stock transfer, Tradefloor, lessor returns, external members, benchmarks) each have a stated rule.
- [ ] Restructuring covers rooftop transfer with a data-class table, tenant merge, and Velto's reorganization tied to the Lost Leads.
- [ ] Failure handling covers exposure, duplicates, missing context, conflicts, incomplete records, partial failure, stale permissions, control-plane outage and noisy neighbors.
- [ ] The Across Markets table distinguishes hierarchy attributes, breach clocks, works-council rules and switching law by market.

## Non-goals

- Authentication, SSO, SCIM, RBAC/ABAC/ReBAC and entitlements in depth: [[identity-access-and-entitlements]].
- Onboarding stages, configuration as data and group policy inheritance: [[onboarding-and-configuration]].
- Usage events, rating and invoices: [[billing-and-metering]].
- Cost-to-serve arithmetic and FinOps: [[scale-and-cost]].
- Telemetry architecture and support tooling: [[observability-and-data-operations]].
- Lead routing journey details: [[journey-lead-to-dms]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- How European dealer-software vendors model groups and rooftops is not publicly documented; the chapter states this gap rather than filling it.
- CDK's 2024 containment architecture is unknown; the cell argument is labeled as inference.
- Silo-clone cost (€6,000 per month) and pooled cost (€11 per rooftop per month) are assumptions; [[scale-and-cost]] may refine them.

## Decision log

- **2026-10-22** — Chose "tenant = contracting organization" over "tenant = rooftop" as the book's position, because dealer-group features outnumber rooftop sales and splits can be designed as one operation.
- **2026-10-22** — Framed blast radius as a cell decision rather than a silo decision, using the CDK 2024 incident as industry context with an explicit inference callout.
- **2026-10-22** — Treated per-tenant encryption as "silo inside the pool" (wrapped data keys, dedicated KMS key as an option) to show bridge applied per component, with dated AWS KMS pricing.
- **2026-10-22** — Named Lotwise Classic's MySQL estate (no native RLS) as the honest weak spot instead of presenting a uniform RLS story.

## Sources

- **Internal**
  - [[meet-axleby]], `_research/scenario-ledger.md` — Velto, Showroomly, the Cross-Tenant Lead, the Lost Leads of Velto, volumes.
  - `_research/brief-saas-tenancy-billing.md` Parts 1, 2, 5, 8, 9; `_research/brief-platform-apis-operations.md` Parts 5, 6.3, 7.
  - [[identity-access-and-entitlements]], [[onboarding-and-configuration]], [[billing-and-metering]], [[journey-lead-to-dms]].
- **External**
  - AWS SaaS Lens (2023) and tenant isolation whitepaper (2020) — silo, pool, bridge, tier-based isolation.
  - Microsoft Azure Architecture Center (2024–2025) — tenancy models, lifecycle, noisy neighbor, consumption measurement.
  - PostgreSQL 18 documentation; Doctrine ORM filters; Citus multi-tenant guide — data isolation mechanics.
  - GDPR Art. 33, EU Data Act, FTC Safeguards Rule, BetrVG §87, WOR art. 27 — market obligations.
  - AP report on CDK Global (2024); Van Mossel annual report (2025).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Lost Leads of Velto aligned to the editor line (hub-sized stock under old rooftop codes), Velto legal entities captioned as two of seven, Velto stock 2,650, American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
