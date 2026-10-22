---
status: accepted
revised: 2026-10-22
---

# Spec: Part VI — DISTRIBUTION: APIs, Events and Data Products

## Intent

Orient the reader to Part VI: how vehicle facts leave the platform through four doors (data API, events and webhooks, bulk data products, consumer checks), and why each door must carry the same controls outward — outcome, freshness, provenance, license, recipient record and a correction path. Frame the part through the Axleby cases the chapters actually use: Fleetmoor Lease's disagreeing answers, the No-Hit Credit, one sold car along eight paths, the rural postcode benchmark and the Horizon privacy assessment, and Odolo's four complaints.

Productscape bricks: the union of the part's chapters (see PLAN for [[vehicle-data-apis]], [[events-webhooks-and-sync]], [[data-products-and-insights]] and [[consumer-vehicle-checks]]).

## Audience

Chief architects, data-product and API platform leads, and engineering directors responsible for how vehicle data is sold and synchronized.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS THIS PART ADDRESSES callout using exact pattern names linked to where-vehicle-platforms-go-wrong.html.
- [ ] States the argument (one platform with several doors, one layer of controls) and why copies that leave cannot be called back.
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter by `[[permalink]]` and saying what it decides and which case drives it.
- [ ] Axleby facts match the ledger and the chapters (€186,000 to 41 clients, 640 API clients, Zombie Golf 4 portals / 4 days, €16 million insight and enrichment, 2.1 million free checks a month, 96 consumer reports, about 9 million requests).
- [ ] Ends with a hand-off to [[vehicle-data-apis]]; 500–800 words of body.

## Non-goals

Teaching API design, event delivery, disclosure control or consumer law (the chapters own them); metering mechanics ([[billing-and-metering]]) and license enforcement ([[data-licensing-and-governance]]); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-22: Mirrors BOOKED's and this book's Part II introduction: opening callouts, a short lead, one mermaid diagram and a paragraph-per-chapter list.
- 2026-10-22: Failure patterns: The Unmetered Call, The Sticky Error and License Blindness, the three that recur across the part's chapter callouts; Provenance Amnesia and The Zombie Listing are left to the chapters.
- 2026-10-22: The diagram shows four doors drawing on one controls layer that records recipients, so corrections can follow delivered copies.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads and Setting the Scene sections of [[vehicle-data-apis]], [[events-webhooks-and-sync]], [[data-products-and-insights]] and [[consumer-vehicle-checks]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
