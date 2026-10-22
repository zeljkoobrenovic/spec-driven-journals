---
status: accepted
revised: 2026-10-22
---

# Spec: Build, Buy or Partner: Sourcing Vehicle Data and Platform Capabilities

## Intent

Give the Chief Architect of a vehicle data and dealer SaaS group a method for deciding, per capability, whether to build, adopt open source, buy, license data or partner, and show the method applied across both halves of the platform. The chapter argues that generic "build what differentiates" rules are too coarse for an industry whose product is largely other people's data. It proposes four ordered gates (supply, data rights, judgement and liability, cost curve at volume) and a data-rights test for every licensed source or vendor that receives the platform's data. It synthesizes sourcing choices that earlier chapters made one at a time (build data, history sources, valuation, damage estimation, CRM, DMS, portals, auctions, lending, billing, identity) into one sourcing register, without contradicting them. The reader should leave able to write a sourcing decision record with requirements, assumptions, exit and review trigger, and to refuse a cheap source that fails the data-rights test.

Owns: **sourcing decision**, **data-rights test**. Productscape bricks touched (as sourcing decisions, not as designs): `vidn` and `module-spec-partner-adapter` (specification and partner data), `vhis` (history sources), `valu` (valuation), `dmgc` (damage calculation), `finc` (financing partner), `b2bt` and `module-auction-partner-adapter` (auction partners), `iden` (identity), `dgov` (license governance).

## Audience

Chief and enterprise architects, CTOs, data and platform leads, and procurement or finance partners at vehicle-data companies, dealer-software vendors and dealer groups who sign supplier and partner contracts. They know build-versus-buy frameworks in general; they need the data-licensing and partner-integration specifics of this industry and a worked register they can copy.

## Success criteria

- [ ] Defines the five sourcing options (build, adopt, buy, license, partner, plus acquire as a pointer) and the two owned terms, with Axleby examples.
- [ ] Presents the four gates with a mermaid decision diagram, a criteria table and a nine-question data-rights test tied to Axleby cases (retention, scope, derivation, redistribution, training, billing basis, evidence, exit, personal data).
- [ ] Shows the "own the seam, rent the commodity" architecture (canonical services, budget broker, Charter, adapters) in a second diagram and a per-dependency requirements table (consistency, latency, freshness, failure behavior) with assumptions labeled.
- [ ] Gives explicit build-versus-buy comparisons with numbers for build data (flat fee vs per request, ledger-consistent), history sources, valuation, damage estimation, CRM, DMS, portals/auctions/lending, billing and identity, each tied to stated requirements and labeled assumptions.
- [ ] Synthesizes an Axleby sourcing register consistent with the ledger and with [[specification-and-equipment]], [[scale-and-cost]], [[valuation-engine]], [[condition-and-damage]], [[leads-and-crm]], [[dms-integration]], [[billing-and-metering]] and [[identity-access-and-entitlements]].
- [ ] Uses dated public evidence (JATO, DAT, VWE, Carfax/Mobility Global, Auto Trader, Cox/incadea/Volaris, CDK/Keyloop, Autorola/ATC, J.D. Power/Autovista, Stripe/Metronome, Keycloak, Auth0, DORA, Data Act) without inferring internals.
- [ ] Covers sourcing failure modes (outage, price rise, supplier acquisition, license termination, duplicate purchases, incomplete answers billed, partner false success, vendor drift) with detection and recovery; trade-off table; market comparison; Chief Architect's view; 6–10 questions.

## Non-goals

- Integration of acquired products and capability map v2 ([[one-platform-from-many-products]]).
- Detailed design of any sourced capability; each belongs to its own chapter (linked).
- License register mechanics and misuse detection ([[data-licensing-and-governance]]).
- Unit-cost analysis and the budget broker's design ([[scale-and-cost]]).
- Team ownership of adapters ([[organizing-engineering]]).
- AI agent governance ([[ai-in-dealer-workflows]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No European build-data or valuation provider publishes per-call prices; the chapter's flat-fee, guide-value, CIAM and billing-product costs are labeled assumptions and should be checked against any later public pricing.
- Whether Odolo UK should resell a UK history provider's finished report is left open; the ledger does not settle UK history sourcing.
- German register access (the KBA large-customer interface) remains an open decision in the ledger.
- Supplier ownership changes quickly (Autovista, AutoTrack/Gaspedaal, ATC, Carfax); dates should be rechecked at each edition.

## Decision log

- **2026-10-22** — Framed the chapter as four ordered gates rather than a weighted scoring matrix, so supply constraints and data rights are settled before cost, which matches how Axleby's expensive mistakes (30-day retention, License Breach) actually happened.
- **2026-10-22** — Opened with four concurrent proposals (flat-fee build data, internal catalog, white-label CRM, billing platform) so each worked comparison answers a concrete decision; outcomes stay consistent with earlier chapters' choices.
- **2026-10-22** — Treated "adopt open source" as its own option, because identity (Keycloak, OpenFGA) is neither built nor bought and the distinction changes exit and operating cost.
- **2026-10-22** — Kept the "Across Markets" section although Part IX does not require it, because supplier sets differ more by country than almost any other topic.

## Sources

- **Internal**
  - [[specification-and-equipment]], [[scale-and-cost]] — build-data costs, retention renegotiation, purchase gate.
  - [[vehicle-history]], [[ingestion-and-entity-resolution]], [[provenance-and-data-quality]] — history sources, Kilometra contract v2.
  - [[valuation-engine]], [[condition-and-damage]] — valuation and damage sourcing.
  - [[leads-and-crm]], [[dms-integration]], [[listing-syndication]], [[b2b-trade-and-remarketing]] — partner integrations.
  - [[billing-and-metering]], [[identity-access-and-entitlements]], [[data-licensing-and-governance]].
  - [[case-cox-automotive]], [[case-vwe]].
  - `_research/brief-case-cox-cdk.md`, `_research/brief-case-autotrader-carfax-vwe.md`, `_research/brief-valuation-market-condition.md`, `_research/brief-saas-tenancy-billing.md`, `_research/scenario-ledger.md`.
- **External**
  - JATO VINView (n.d.); DAT Austria VIN guide (2026); DAT SilverDAT valuateFinance (2024); VWE API documentation and Occasion Manager (n.d.); Mobility Global information statement (2026); Auto Trader results FY2023 and FY2025; CDK Global 10-K (2021); Volaris (2022); Cox Automotive fact sheet (2018); Stripe meters and Metronome (2026); Keycloak 26 (2024); Auth0 Organizations (n.d.); Regulation (EU) 2022/2554 (DORA); Regulation (EU) 2023/2854 (Data Act).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: figures checked against the ledger (build data, EV Overvaluation, Merelstad, Tradefloor); Stripe claim verified; American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
