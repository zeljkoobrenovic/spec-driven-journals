---
status: accepted
revised: 2026-10-22
---

# Spec: Trader to Trader: B2B Exchanges, Auctions and Lease Remarketing

## Intent

Show how a vehicle data and dealer SaaS platform should support trade between businesses: dealers, traders, exporters, lessors, rental companies and auction houses. The chapter separates wholesale channels from retail advertising by one property, whether a click or a hammer binds the seller, and builds the design on it: an exclusive, time-bounded right-to-sell lease per vehicle with fencing tokens, trade listings with audiences and tiers, buyer matching, auction hand-offs as partner contracts with status and reconciliation, and a trade deal whose release conditions (payment, VAT basis, register action, export proof) gate collection. For lessors it treats the de-fleet as a pipeline known months ahead and the digital return as the evidence moment whose findings drive the lessee charge, the buyer condition report and the reserve.

Owns: **trade listing**, **de-fleet**, **digital return**, **auction hand-off**. Productscape bricks: `b2bt` (B2B Trade and Stock Exchange; trade matcher, trade offer store, auction partner adapter), plus the `lease-remarket-returned-vehicles` journey (with `dmgc`, `valu`, `rdwt` handled by their own chapters).

## Audience

Chief architects, product and engineering leads of dealer software vendors, remarketing platforms, lessors and dealer groups that build or integrate trade exchanges and auction hand-offs. They know concurrency control, idempotency and partner integration; they need the trade-specific binding rules, lessor workflow, VAT and register gates and partner-contract terms.

## Success criteria

- [ ] Defines trade listing, de-fleet, digital return and auction hand-off, and contrasts trade listings with consumer adverts in a table that makes binding concurrency explicit.
- [ ] Describes the wholesale channels with dated public evidence (NADA 2025, OPENLANE 2025 10-K, CarMax, Hertz, Ayvens, Autorola, Manheim UK, VNA 2025 lease fleet, ATC sold to Autorola on 1 February 2026) and labels inferences about real companies.
- [ ] Presents the architecture with a component-responsibility table, at least two diagrams (pipeline, right-to-sell state machine, auction hand-off sequence) and a consistency/latency/freshness/availability table.
- [ ] Works an Axleby example with ledger-consistent numbers: Tradefloor 48,000 deals, Fleetmoor 14,000 returns (8,600 on Tradefloor in 2026), the Twice-Sold Returns incident (8 June 2027), and ties to the EV Overvaluation, the Margin-Scheme Error and Gauge without contradicting their owning chapters.
- [ ] Covers duplicate sales, late partner results after lease expiry, duplicate result messages, incomplete returns, conflicting condition evidence, payment without register confirmation, ambiguous timeouts, partner outages, valuation drift and buyer default.
- [ ] Compares double-sale prevention options and own/partner/no-auction options in trade-off tables, with the conditions under which the recommendation changes.
- [ ] Includes "Across Markets: What Changes by Country" with NL/BE, DE, UK and US columns and a common-versus-adapter judgement.
- [ ] Ends with the Chief Architect's view, 6–10 questions and a hand-off to [[tenancy-and-dealer-groups]].

## Non-goals

- Inspection capture, grading rubrics, damage estimates and reconditioning cost ([[condition-and-damage]]); battery certificates ([[ev-battery-health]]).
- Register transactions, export paperwork and registration taxes in detail ([[registration-and-trade-services]]); invoices and the margin scheme ([[deals-and-sales-documents]]).
- Trade values and drift monitoring ([[valuation-engine]]); appraisal and bid limits in the lane ([[vehicle-acquisition]]).
- Marketplace liquidity theory ([[liquidity-and-network-effects]]) and payment services ([[payments-fundamentals]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No single published lease-return standard was verified for the Netherlands, Belgium or Germany; only the UK BVRLA guides were.
- Auction partners' arbitration and withdrawal-confirmation terms (Autorola, Manheim, OPENLANE) were not read; the chapter states the requirement, not their terms.
- Belgian register steps in a trade sale and German deregistration practice before export are industry practice, not verified sources.
- Whether partner auction results may be licensed into valuation is a commercial question per partner.

## Decision log

- **2026-10-22** — Made the right to sell an exclusive lease with fencing tokens the chapter's central concept, because binding B2B channels turn the consumer-portal concurrency of [[listing-syndication]] into double contracts, and Axleby cannot cancel partner auction sales.
- **2026-10-22** — Opened with a new incident, the Twice-Sold Returns (17 cars, 8 June 2027), rather than reusing the EV Overvaluation or the Margin-Scheme Error, which are owned elsewhere and are cited as supporting symptoms.
- **2026-10-22** — Positioned Handback as the return-and-settlement workflow over Gauge and Lotwise Inspect, after [[condition-and-damage]] took capture and rubrics and handed settlement and trade disputes to this chapter.
- **2026-10-22** — Kept buyers' money out of Axleby (seller-direct payment plus release conditions) and named the threshold at which to revisit.

## Sources

- **Internal**
  - [[inventory-and-vehicle-dossier]] — disposition on the stock item.
  - [[valuation-engine]] — the EV Overvaluation and Tradefloor no-sale rates.
  - [[deals-and-sales-documents]] — the Margin-Scheme Error and VAT regime.
  - [[condition-and-damage]], [[ev-battery-health]] — Gauge, Inspect and verified battery certificates.
  - [[case-vwe]], [[case-cox-automotive]] — ATC sale; Axleby owns no auctions.
  - `_research/brief-dealer-workflows-economics.md`, `_research/brief-valuation-market-condition.md`, `_research/brief-case-autotrader-carfax-vwe.md`, `_research/brief-identity-registers.md`, `_research/scenario-ledger.md`.
- **External**
  - OPENLANE, Hertz, CarMax and Carvana annual reports (2026); Ayvens FY2025 results (2026); NADA Data 2025.
  - Journal de l'Automobile on the ATC sale (5 February 2026); Autorola and Manheim UK sites; VNA lease fleet figures (6 March 2026).
  - Directive 2006/112/EC and Directive (EU) 2018/1910 (Article 138); RDW trade-stock and *informatiemap* pages; GOV.UK and HMRC guidance; BVRLA fair wear and tear guides.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Inline dated links added for NADA, CarMax, VNA, OPENLANE, Hertz and Ayvens claims; acronyms expanded; American spelling; outage link corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
