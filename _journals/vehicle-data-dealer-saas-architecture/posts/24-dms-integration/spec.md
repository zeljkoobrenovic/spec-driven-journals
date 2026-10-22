---
status: accepted
revised: 2026-10-22
---

# Spec: Living With the DMS: Dealer Management System Integration

## Intent

Show how a dealer SaaS platform should integrate with dealer management systems (DMS) it does not control. The chapter defines what a DMS owns and why it holds the system of record for the dealer's books. It explains how US and European DMS ecosystems control access, from Reynolds' RCI (2003) through the 2015 closing of CDK, the Authenticom litigation, Arizona's dealer-data law and the 2024 Tekion suit. It then turns the evidence into a reference architecture: field ownership per rooftop type, one DMS adapter per family behind an anti-corruption layer, a time-bounded cross-reference map, idempotent versioned upserts, write-back commands with receipts, nightly reconciliation, an authorization register and a degraded mode. The reader should leave able to design, review and govern DMS integrations so that a DMS outage, a vendor's change of terms or a silent rejection does not stop the dealer.

Owns: **DMS**, **certified interface**, **DMS adapter**. Productscape bricks: none; this is a gap chapter **[ADDED]** (digest gap 2: DMS integration and dealer system landscape, `dhld` "DMS integrations live" KPI, `ivnd` channel).

## Audience

Chief architects, integration and platform leads, and product directors of dealer software vendors, portals and dealer groups that must connect to CDK, Reynolds, Tekion, Keyloop, Pinewood, incadea, CROSS or local DMS products. They know APIs, queues and idempotency. They need the DMS-specific ownership, access, contract and failure picture.

## Success criteria

- [ ] Defines DMS, certified interface and DMS adapter, and gives a field-level ownership table that differs for franchised dealers, independents with a light DMS, and independents without one.
- [ ] Gives a dated, sourced history of DMS access disputes (RCI 2003, 2015 agreements, Authenticom 2017, Arizona law upheld 2021, $100m settlement 2024, Tekion 2024) without the non-existent "2018 consent", and a program table (Fortellis, RCI, Opentrack, APC, Keyloop Open Platform).
- [ ] Compares six access patterns, including aggregators and scraping, and explains why scraping is never a foundation.
- [ ] Presents the Hitch architecture with at least one diagram, a component-responsibility table and a consistency/latency/freshness/availability table per interaction.
- [ ] Uses the June 2024 CDK outage from customers' SEC filings (Sonic, Lithia, AutoNation, Group 1), with the internals of CDK's recovery labeled as inference.
- [ ] Works the DriveDesk Outage (November 2027, 12 days, 1,900 rooftops) with a timeline, degraded-mode states and reconciliation numbers, and ties the Zombie Golf and the Lost Leads of Velto to the integration layer without contradicting their owners.
- [ ] Covers duplicates, conflicting updates, incomplete records, ambiguous timeouts, silent acceptance, partial files, schema drift, credential revocation, vendor outage and certification change.
- [ ] Includes the "Across Markets" table, trade-off tables, partner-contract terms, dealer data ownership (Arizona, GDPR roles, EU Data Act switching), the Chief Architect's view and 6–10 questions.

## Non-goals

- Lead normalization, routing and CRM design ([[leads-and-crm]]); the end-to-end lead journey ([[journey-lead-to-dms]]).
- Stock lifecycle and dossier aggregate ([[inventory-and-vehicle-dossier]]); deal documents and margin VAT ([[deals-and-sales-documents]]).
- Event envelopes, outbox and webhook signing ([[events-webhooks-and-sync]]); general dependency budgets and SLOs ([[reliability-and-dependencies]]).
- Ransomware defense of the platform itself ([[vehicle-platform-security]]); the CDK company story ([[case-cdk-global]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Current fees, certification lead times and contract terms of Fortellis, RCI, Opentrack, APC and Keyloop's program are not public; the chapter says so.
- Belgian DMS vendors and German market shares could not be verified.
- Outcomes of Tekion v. CDK and the AutoLoop vendor class are not verified as of 2026.
- Whether SaaS DMS products fall within the Data Act's switching obligations in practice is a legal interpretation.

## Decision log

- **2026-10-22** — Opened with the Zombie Golf's DMS root cause (a stock-number change on an inter-rooftop transfer) rather than with the outage, so the chapter's question is identity and ownership first and availability second; the DriveDesk Outage became the worked example in "In Practice".
- **2026-10-22** — Named the integration layer **Hitch** and recorded it, Axleby's connected-rooftop counts and the outage timeline in the ledger so the reliability and journey chapters can reuse them.
- **2026-10-22** — Made field ownership switchable per rooftop (DMS-owned stock for franchised dealers, Lotwise-owned for independents) instead of choosing one system of record, because Axleby's customer mix is 62% independents and 31% franchised.
- **2026-10-22** — Treated scraping as a dated, dealer-signed bridge at most, citing the court record rather than a moral argument.

## Sources

- **Internal**
  - [[listing-syndication]] — the Zombie Golf and delete propagation.
  - [[journey-lead-to-dms]] — the Lost Leads of Velto.
  - [[reliability-and-dependencies]] — degraded modes and game days.
  - [[inventory-and-vehicle-dossier]] — the dossier aggregate this chapter feeds.
  - `_research/brief-dms-integration.md`, `_research/brief-case-cox-cdk.md`, `_research/brief-platform-apis-operations.md`, `_research/brief-saas-tenancy-billing.md`, `_research/scenario-ledger.md`.
- **External**
  - Authenticom v. CDK Global (7th Cir., 2017) and CDK Global v. Brnovich (9th Cir., 2021) — access history and dealer data law.
  - Sonic, Lithia, AutoNation and Group 1 SEC filings (2024) — the CDK outage as dealers reported it.
  - Regulation (EU) 2023/2854 (Data Act) — switching rights and charges.
  - Fortellis, Tekion APC, Keyloop Developer, RCI and STAR documentation — program and standard shapes.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Accounting stock unit vs stock item distinguished per item 31(a); Lost Leads wording aligned to item 27; acronyms expanded. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
