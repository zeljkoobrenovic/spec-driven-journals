---
status: accepted
revised: 2026-10-22
---

# Spec: Part V — SAAS: Tenants, Access and the Commercial Model

## Intent

Orient the reader to Part V: tenancy, identity, configuration, billing and licensing form one control plane, shared by every product and owned once, in which commercial facts are recorded as evidence. Frame the part through the tenant directory, Axleby ID and Gatekeeper, Runway and Baseline, Meterline and Charter, and the incidents the chapters use (the Cross-Tenant Lead, Velto's 322 logins, Velto's 199-day onboarding, the No-Hit Credit, the License Breach).

Productscape bricks: the union of the part's chapters (iden, dosr, bill, dgov).

## Audience

Chief architects, platform and SaaS engineering leaders, and finance-systems and data-governance leads.

## Success criteria

- [ ] Opens with the standard callouts, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names.
- [ ] States the argument (one control plane) and why it matters most for an acquired portfolio.
- [ ] Axleby numbers match the ledger and chapters (112 leads, 3 dealers, 47 minutes; 322 logins; 199 days; €186,000 to 41 clients; five months of resale).
- [ ] One mermaid diagram with a Figure caption.
- [ ] One paragraph per chapter in config order, each linking the chapter, saying what it decides and naming its case.
- [ ] Hands off to [[tenancy-and-dealer-groups]]; [[b2b-trade-and-remarketing]] hands off here.
- [ ] Body after the callouts stays short (about 500–800 words; the whole page about 900–1,050, in line with BOOKED and LISTED part introductions).

## Non-goals

Teaching tenancy models, authorization, onboarding, rating or license enforcement (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-22: Failure patterns: The Tenant Blur, The Acquisition Archipelago and License Blindness; The Unmetered Call is left to [[billing-and-metering]], the only chapter where it is central.
- 2026-10-22: The Acquisition Archipelago is named because every chapter of the part uses it.
- 2026-10-22: The diagram shows the control plane beneath the products rather than a request flow.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, Setting the Scene sections and closing paragraphs of [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[onboarding-and-configuration]], [[billing-and-metering]] and [[data-licensing-and-governance]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
