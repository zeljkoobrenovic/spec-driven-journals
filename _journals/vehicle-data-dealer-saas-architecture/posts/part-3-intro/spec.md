---
status: accepted
revised: 2026-10-22
---

# Spec: Part III — VALUE: Market Data, Valuation and Condition

## Intent

Orient the reader to Part III: value is an estimate built on partial evidence, and the platform must show how partial. Frame the part through Pulse, Vantage and its valuation ledger, Gauge, the battery-health service, Mandate and Signalyard, with the EV Overvaluation as the thread and each chapter's own case (61% match rate, Fleetmoor's return inspections, the two ID.3 certificates, Fleetmoor's connected-odometer request).

Productscape bricks: the union of the part's chapters (mktd, valu, dmgc, tapp inspection, evsh; connected-vehicle data is a gap the book adds).

## Audience

Chief architects, heads of data and valuation, and engineering directors responsible for market data, pricing models, inspection and EV products.

## Success criteria

- [ ] Opens with the standard callouts, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names.
- [ ] States the argument (value as an evidenced estimate on partial inputs; measured against outcomes per segment) and the thread from market data to connected data.
- [ ] Axleby numbers match the ledger and chapters (61% match, 68% of de-listings were sales, 9.5% for 14 weeks, Fleetmoor's BEV no-sale rate 18% → 41%, 21% contested charges, 94% vs 87%).
- [ ] One mermaid diagram with a Figure caption.
- [ ] One paragraph per chapter in config order, each linking the chapter, saying what it decides and naming its case.
- [ ] Hands off to [[market-data]]; [[provenance-and-data-quality]] hands off here.
- [ ] Body after the callouts stays short (about 500–800 words; the whole page about 900–1,050, in line with BOOKED and LISTED part introductions).

## Non-goals

Teaching harvesting law, valuation modeling, damage estimating, battery testing or the EU Data Act (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-22: Thread chosen: the EV Overvaluation, because it touches market data (leading signal), valuation (drift), trade (reserve prices) and the battery chapter.
- 2026-10-22: Failure patterns: The Confident Valuation, Provenance Amnesia and License Blindness; Spec Guesswork and The Sticky Error are left to the chapters.
- 2026-10-22: The diagram shows evidence flowing into Vantage and outcomes flowing back through the ledger, the loop the part recommends.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, Setting the Scene sections and closing paragraphs of [[market-data]], [[valuation-engine]], [[condition-and-damage]], [[ev-battery-health]] and [[connected-vehicle-data]]; the Fleetmoor no-sale figures come from [[b2b-trade-and-remarketing]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
