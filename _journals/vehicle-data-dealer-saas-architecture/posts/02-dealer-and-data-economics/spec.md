---
status: accepted
revised: 2026-10-22
---

# Spec: Margins, Days and Lookups: The Economics of Dealers, Data and SaaS

## Intent

Show how the three businesses on a vehicle data and dealer SaaS platform make money (the used-car dealer, the vehicle-data provider and the dealer-software vendor) and turn each economic quantity into a requirement the architecture must meet and an event it must record. The reader should leave able to compute gross per unit, holding cost per day, cost per lookup and revenue per rooftop for their own context, and to explain why publish delay, valuation error, no-hit rules and missing cost tags are economic problems before they are technical ones. The chapter owns **days-to-turn**, **gross per unit**, **cost per lookup**, **rooftop pricing** and a brief definition of **no-hit-no-fee** (deep treatment in [[billing-and-metering]]).

Productscape bricks covered: `bill` (economics of subscriptions, per-report and per-transaction fees, no-hit-no-fee) and `occm` (stock and pricing metrics: days in stock, gross, price position).

## Audience

Chief architects, principal engineers and engineering leaders of vehicle-data companies and dealer-software vendors who are handed targets ("lookups under two seconds", "publish within fifteen minutes") and need to know where the targets come from, and product and finance leaders who need the platform to answer margin, invoice and churn questions.

## Success criteria

- [ ] Defines gross per unit (front-end and back-end), days-to-turn and its relatives (days listed, days' supply, time to line), holding cost, cost per lookup, no-hit-no-fee, rooftop pricing, GRR, NRR and cost to serve.
- [ ] Works a dealer unit P&L (Brandsma) with labeled assumptions, including the EU margin scheme, and derives holding cost per car-day.
- [ ] Separates owned, derived and rented data costs and shows a per-call margin table where a call can lose money on first fetch.
- [ ] Shows Lotwise revenue per rooftop and pull-through across brands, consistent with the ledger.
- [ ] Contains a requirements table (latency, freshness, consistency, availability) derived from the economics, with at least three worked derivations.
- [ ] Covers failure handling for economic records: duplicates, conflicts, incomplete records, retries, partial failures, outages, definition drift.
- [ ] Compares pricing models in a trade-off table with the architecture each requires, and states a conditional recommendation.
- [ ] Every company claim carries a dated source; Axleby is labeled fictional; assumptions are labeled.

## Non-goals

- Metering pipeline, rating engine, invoicing and revenue recognition design ([[billing-and-metering]]).
- Pricing algorithms and repricing rules ([[used-car-pricing]]); valuation modeling ([[valuation-engine]]).
- Tenant hierarchy and entitlements ([[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]]).
- License terms and purpose checks ([[data-licensing-and-governance]]); infrastructure cost management ([[scale-and-cost]]).
- A full "Across Markets" section (Part I); market differences are shown only where evidenced.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source gives European dealer gross per unit or dealer-software spend per rooftop; the chapter relies on US filings and Auto Trader's ARPR. Revisit if BOVAG, DAT or a listed European group publishes such figures.
- Holding-cost assumptions (1.5% depreciation a month, 6% funding) should be checked against a market index per country when the valuation chapter is written.
- Germany's e-invoicing dates rest on a secondary summary of the BMF letter.

## Decision log

- **2026-10-22** — Anchored the dealer economics in US filings (AutoNation, CarMax, Carvana, Penske, OPENLANE) because they are the only audited per-unit sources, and said explicitly that European groups do not publish comparable figures.
- **2026-10-22** — Used the ledger's editor breakdown of Lotwise revenue per rooftop (€1,110: modules €540, data usage €180, group add-ons €190, finance referrals €120, integration fees €80) and its lookup mix (70% internal, external at about €0.13) instead of an earlier draft split that conflicted with `deals-and-sales-documents`; cost per lookup figures follow `scale-and-cost` (€0.031 average).
- **2026-10-22** — Presented velocity pricing as a documented historical practice, with Pollak's 2023 reversal (consistency issue 9). Avoided the disputed AutoNation CDK-outage per-share figure (issue 10).
- **2026-10-22** — Used "Where the Economics Differ by Market" instead of the Parts II–VII "Across Markets" heading, since Part I chapters do not require it.

## Sources

- **Internal**
  - [[meet-axleby]] — prices, volumes, incidents and cast.
  - [[vehicle-data-ecosystem]] — participants and value chain this chapter builds on.
  - [[billing-and-metering]], [[used-car-pricing]], [[inventory-and-vehicle-dossier]], [[data-licensing-and-governance]] — chapters that take the requirements further.
- **External**
  - AutoNation, CarMax, Carvana, Penske and OPENLANE 10-Ks (2026) — gross per unit, days' supply, floorplan.
  - Auto Trader Group FY2026 results (2026); Mobility Global 10-Q (2026); CDK Global 10-K FY2021 — rooftop pricing evidence.
  - VAT Directive 2006/112/EC; HMRC margin-scheme guidance (2021); Directive (EU) 2023/2225 — tax and finance rules.
  - VWE and Car-Pass product pages (accessed 2026-10) — per-lookup licensed data and no-charge-on-empty rules.
  - Microsoft Learn on pricing models and measuring consumption (2024); FinOps Foundation unit economics — cost to serve and cost per transaction.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: dated the Brandsma month to 2026 (Sales Admin added January 2027), fixed the month-end outage example to register calls and confirmation billing, spelling and figure spacing. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
