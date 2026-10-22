---
status: accepted
revised: 2026-10-22
---

# Spec: Buying Right: Trade-In Appraisal, Sourcing and Maximum Purchase Price

## Intent

Answer the question: **how should a platform support buying a car at the right price, from the customer's driveway to the auction lane?** The chapter separates the appraisal (evidence and judgement at a point in time) from the purchase offer (a versioned, expiring commitment) and from the stock item (created only on purchase). It turns the maximum purchase price, defined in [[valuation-engine]], into a buying decision: computed by a pure, versioned calculator from the dealer's policy, solved on the car's VAT basis, and taken from a cautious point of the valuation range when confidence is thin or the segment is under watch. It covers acquisition channels, offline-capable capture as an installable web app, entry validation, offer validity in time and distance, handover checks and the exactly-once hand-off to the dossier and the register stock-in.

Productscape bricks covered: `tapp` (trade-in appraisal reports: guided inspection, composer, appraisal store) and `occm` (the buying PWA: plate scan on the lot or at auction with maximum purchase price). The chapter argues for one appraisal service with two capture modes (desk and lane) instead of separate modules.

Owns: **appraisal**, **trade-in**, **purchase offer**.

## Audience

Chief architects, principal engineers and product leaders of dealer-software vendors, dealer groups with central buying desks, and remarketing platforms who design appraisal, buying and offer workflows.

## Success criteria

- [ ] Reader can list the six acquisition channels with their typical VAT basis and explain why the seller's VAT status changes the maximum purchase price.
- [ ] Reader can compute a margin-scheme MPP with the VAT gross-up and explain why the calculator must be a pure, versioned function.
- [ ] Reader can state the confidence rule (which point of the valuation range the MPP uses per segment status) and link it to the EV Overvaluation.
- [ ] Reader can draw the offer lifecycle and justify immutable versions, validity in days and distance, listed conditions and the handover check.
- [ ] Reader can design offline capture (client ids, outbox, server-owned decisions) and name the browser constraints that shape it.
- [ ] Article includes the Axleby worked example (Golf Variant at Brandsma) with ledger-consistent numbers, a requirements table, a failure table, trade-off tables, an Across Markets table and three mermaid diagrams.
- [ ] Every company, regulatory and platform claim carries a dated source; Axleby numbers and thresholds are labeled.

## Non-goals

- Valuation methods, ledger, back-testing and drift monitoring ([[valuation-engine]]).
- Inspection standards, damage estimation and reconditioning cost models ([[condition-and-damage]]); battery health ([[ev-battery-health]]).
- Specification resolution and the build-data purchase gate ([[specification-and-equipment]]).
- The stock item, lifecycle and cost layers after purchase ([[inventory-and-vehicle-dossier]]).
- Margin-scheme invoicing and trade-in netting in the deal ([[deals-and-sales-documents]]).
- Register transaction mechanics, BPM calculation and import paperwork ([[registration-and-trade-services]]); B2B exchanges and auctions as platforms ([[b2b-trade-and-remarketing]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No public offer-validity convention was found for the Netherlands, Belgium, Germany or the UK; the table says so.
- Belgian register action at purchase (DIV) was not verified from primary sources.
- UK outstanding-finance checks and US lien payoff are labeled industry practice; no primary source was read.
- The WebKit storage evidence dates from 2020; current Safari behavior should be rechecked before a capture design relies on it.

## Decision log

- **2026-10-22** — Kept the appraisal as its own aggregate, separate from the stock item, consistent with [[inventory-and-vehicle-dossier]] treating *Appraised* as a proposed stay; the stock item starts at *Purchased*.
- **2026-10-22** — Merged the Productscape `tapp` and `occm` buying-PWA bricks into one appraisal service with desk and lane modes, so buying discipline is identical across channels.
- **2026-10-22** — Made the VAT gross-up explicit in the MPP formula, because the margin scheme makes the buying ceiling depend on whom the dealer buys from.
- **2026-10-22** — Reused the Golf Variant from [[specification-and-equipment]] (€23,750 retail, September 2027) as the worked example, so the two chapters tell one appraisal.

## Sources

- **Internal**
  - [[meet-axleby]], [[dealer-and-data-economics]] (holding-cost assumptions), [[valuation-engine]] (MPP, segment status, EV Overvaluation), [[specification-and-equipment]] (€750 threshold, Golf Variant), [[vehicle-history]] (Volvo V60 odometer), [[inventory-and-vehicle-dossier]], [[deals-and-sales-documents]], [[billing-and-metering]].
  - `_research/brief-dealer-workflows-economics.md`, `_research/brief-valuation-market-condition.md`, `_research/brief-identity-registers.md`, `_research/productscape-digest.md` (bricks `tapp`, `occm`).
- **External**
  - AutoNation 10-K 2025 (2026), CarMax 10-K FY2026 (2026), Carvana 10-K 2025 (2026), OPENLANE 10-K 2025 (2026), KBB value definitions, Cox Automotive vAuto–UVeye release (2026), vAuto recon-estimate content, DAT SilverDAT valuateFinance description (2024), NADA Data 2025 (2026).
  - Directive 2006/112/EC; RDW stock-in and odometer pages; GOV.UK sold/bought vehicle; 49 CFR 580.5; 49 USC 30502; §39 StVG; Car-Pass.
  - WebKit blog (2020) on script-writable storage; MDN Background Synchronization API.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned the Golf Variant timeline with consistency item 28 (appraised Sat 11 Sept at 61,240 km, offer limit 61,740 km, handover 61,302 km three days later); American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
