---
status: accepted
revised: 2026-10-22
---

# Spec: From Signed Contract to First Sale: Onboarding, Migration and Configuration

## Intent

Show how a vehicle data and dealer SaaS group should onboard dealers, dealer groups and data clients, migrate them from a previous tool, and configure the product per tenant without forking it. The chapter argues three things: onboarding is a measured pipeline of states whose long poles are third parties (register authority, DMS approval, portal feed hand-over), not data import; migration is a re-runnable, identity-first import closed by a signed reconciliation and a once-only channel hand-over; and customer requests are met by versioned, inherited configuration and out-of-process extension points, never by code branches.

Productscape bricks covered (as a research map, not company fact): `iden` (account administration: companies, branches, users, module subscriptions, register authorizations as onboarding inputs) and `dosr` (the dossier as the target of migrated stock and transfer events).

Owns the terms: **tenant configuration**, **extension point**, **time to first advert**.

## Audience

Chief architects, platform and product engineering leaders of dealer-software vendors and vehicle-data companies who run onboarding of groups and data clients, and who are under pressure from large customers to customize. They should leave with a stage model, a migration design, a configuration design and a fork policy they can take to a design review.

## Success criteria

- [ ] Defines onboarding stages with exit evidence, owners and external parties, and defines time to first advert precisely (per rooftop, channel-confirmed) with companion metrics.
- [ ] Presents the Velto onboarding (2026) with stage timings and failures, and the Hartley migration (Q4 2027) with the classification of 14 tenant-specific code paths; numbers consistent with the scenario ledger.
- [ ] Describes the migration toolkit (staging, VIN resolution through Anchor, idempotent upsert, signed reconciliation) and the channel hand-over protocol.
- [ ] Describes configuration as typed, versioned, effective-dated, validated data with group-to-rooftop inheritance, locks, simulation and version stamps on decisions; separates configuration from entitlements, release flags and market packs.
- [ ] Contains a lever table (settings → forks), a requirements table, a failure-handling table, a trade-off table and the Across Markets table.
- [ ] Uses only dated public evidence for real companies (Auto Trader 2026, Lithia/Pinewood 2025, Cox Bridge Federation, Keyloop, Salesforce, ServiceNow community, EU Data Act) with no invented internals.
- [ ] Includes at least three mermaid diagrams with captions, and links to neighboring chapters instead of re-teaching them.

## Non-goals

- Tenant hierarchy, isolation models and tenant restructuring ([[tenancy-and-dealer-groups]]).
- Authentication, SSO, SCIM, roles, entitlements and register authority as authorization ([[identity-access-and-entitlements]]).
- Pricing, usage events and invoicing ([[billing-and-metering]]).
- License and purpose register details ([[data-licensing-and-governance]]).
- Relay's desired-state syndication model ([[listing-syndication]]) and DMS adapter design ([[dms-integration]]).
- Connect XML to JSON API migration ([[modernizing-the-platform]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Germany's register-authority model for dealers is stated as judgement (no single national dealer recognition); verify against KBA or registration-office sources in a review pass.
- Whether portals generally accept only one feed supplier per dealer account is stated as common practice, not documented; look for portal partner documentation.
- German e-invoicing dates come from a KPMG summary, not from the BMF.

## Decision log

- **2026-10-22** — Velto's onboarding placed in May–November 2026 (before the February 2027 Zombie Golf, which requires Velto to be on Lotwise) and examined through a January 2027 retrospective, keeping the chapter set in 2027.
- **2026-10-22** — "The Hartley migration" interpreted as moving an existing Showroomly customer onto Axleby ID and the shared configuration service (Q4 2027 pilot), consistent with the ledger's Year 2–3 plan for Showroomly; used to show unwinding tenant-specific code.
- **2026-10-22** — New fictional control-plane components named Runway (onboarding orchestrator) and Baseline (configuration service); recorded in the scenario ledger.
- **2026-10-22** — Policy recommended: no tenant-conditional code and no in-process customer code; extension through webhooks, partner API, customer-hosted callouts and templates.

## Sources

- Internal: [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[billing-and-metering]], [[listing-syndication]], [[dms-integration]], [[vehicle-identity]], [[journey-lead-to-dms]], [[data-licensing-and-governance]], [[vehicle-platform-security]], [[multi-country-platforms]].
- Research briefs: `brief-saas-tenancy-billing.md` (Parts 4–6, 7.5, 8.5, 9), `brief-dealer-workflows-economics.md` (Parts 2, 7, 10), `brief-dms-integration.md` (Parts 4 and 7).
- External: Regulation (EU) 2023/2854 (Data Act); Auto Trader Group FY2026 results; Auto Remarketing on Pinewood and Lithia (2025); Cox Automotive Bridge Federation; Keyloop developer portal; Salesforce multitenant architecture; ServiceNow community on skipped records (2024); Hodgson, Feature Toggles (2017); Ondernemersplein on the Dutch trade-stock recognition.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: tenant registry renamed tenant directory, recognition held per legal entity, declined stand-time request made consistent with the 17/4/2 split, Lost Leads wording aligned, acronyms and American spelling. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (neighboring). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
