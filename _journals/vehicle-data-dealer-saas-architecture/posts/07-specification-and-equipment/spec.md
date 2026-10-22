---
status: accepted
revised: 2026-10-22
---

# Spec: What Exactly Was Built: Specification, Trim and Equipment Data

## Intent

Show how a vehicle data and dealer SaaS platform turns a VIN or plate into a specification that valuations, adverts, reports and APIs can trust, including the edition (trim) and the factory options, and what that costs. The chapter argues that specification is three sourced layers (register, catalog, as-built) plus dealer assertions, resolved per attribute into a versioned view with an explicit state ("edition unknown" is legitimate), and that per-VIN build data should be bought for decisions, once per car, under a license that allows storing it. After reading, an architect can design a specification resolver, a purchase policy and a license-aware cache, and can explain why one product's guessed trim becomes every product's error.

Productscape bricks covered: `vidn` (Vehicle Identity and Specification: specification side; decoding identity is shared with `vehicle-identity`).

## Audience

Chief architects, data and platform leads of vehicle-data companies and dealer-software vendors, and product leaders who own appraisal, valuation or advert quality. They know APIs and data platforms; they need the domain: catalog levels, provider keys (HSN/TSN, cap Code, type approval, derivative ids), the catalog/as-built split, and the economics of paid build data.

## Success criteria

- [ ] Reader can name the three specification layers, their keys, costs and limits, with dated evidence (RDW open data, vPIC, DAT 2026 guide, JATO, Auto Trader taxonomy).
- [ ] Reader can sketch a resolver with fact store, catalog and crosswalk, purchase gate, build-data adapters, confirmation capture and portal mappers, and say which component owns what.
- [ ] Reader can explain per-attribute precedence and the resolution states, including "edition unknown", and how confidence becomes a dealer question.
- [ ] Reader can work through the Axleby €0.46-per-request economics (28.5 million fetches in 2026, 47% repurchases or duplicates) and the purchase-gate decision for one appraisal.
- [ ] Reader can state caching rules by fact type and why cache entitlement is a license property.
- [ ] Reader can handle duplicates, layer conflicts, wrong-vehicle data, imports, incomplete records, provider outages and catalog corrections.
- [ ] Reader can compare the approaches in a trade-off table and see what differs by market (input key, register richness, catalog keys, portal vocabulary).
- [ ] Reader will not mistake a VIN decode or a catalog feature list for the equipment of a specific car.

## Non-goals

- VIN structure, plate assignments, the identity graph and the AVK (`vehicle-identity`).
- Register access regimes, mutation feeds and Turnstile (`registers-and-official-data`).
- Generic ingestion, survivorship and golden records (`ingestion-and-entity-resolution`); the provenance envelope (`provenance-and-data-quality`).
- Option-adjustment models and valuation confidence (`valuation-engine`).
- Channel adapters and delivery semantics (`listing-syndication`); advert text (`merchandising`).
- License register mechanics (`data-licensing-and-governance`); metering and no-hit billing (`billing-and-metering`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No European provider publishes per-request prices or license clauses; the chapter presents caching limits as typical and the Axleby contract as fictional.
- Whether the RDW `catalogusprijs` includes factory options is undocumented in the dataset metadata; the chapter treats it as a weak signal.
- cap ID granularity: the product page says "unique to each vehicle"; the chapter follows industry usage (derivative level) and says so.
- J.D. Power ChromeData and Autovista primary pages were unreadable (HTTP 403); they appear only as marketing-level claims.

## Decision log

- **2026-10-22** — Framed the chapter around the €0.46 build-data economics rather than catalog modeling alone, because the purchase decision is where architecture, license and margin meet; rejected a "taxonomy first" structure as too descriptive.
- **2026-10-22** — Chose a layered fact model with per-attribute precedence over a single golden specification record, citing DAT's two-tier sources and Auto Trader's `factoryFitted` limits as evidence that layers mix even inside one provider.
- **2026-10-22** — Kept portal equipment mapping to one section with verified API evidence (mobile.de, AutoScout24, Auto Trader, Marktplaats) and handed adapters to `listing-syndication`.
- **2026-10-22** — Aligned the build-data economics with the ledger line from `scale-and-cost` (3.0% miss rate, 30-day retention, life-of-vehicle retention from July 2027 at about €0.58 a first fetch) instead of a smaller standalone figure; added only the trigger breakdown, the resolution-state shares and the Q4 2027 run rate to the ledger.

## Sources

- **Internal**
  - [[vehicle-identity]], [[registers-and-official-data]] — inputs to the resolver.
  - [[ingestion-and-entity-resolution]], [[provenance-and-data-quality]] — survivorship and provenance envelope.
  - [[valuation-engine]], [[listing-syndication]], [[merchandising]] — consumers of the resolved view.
  - [[data-licensing-and-governance]], [[billing-and-metering]] — license scope and no-hit billing.
  - `_research/brief-specification-history.md` (Part 1, 2.8, Part 3), `_research/brief-syndication-leads.md` (2.8), `_research/brief-case-autotrader-carfax-vwe.md`, `_research/productscape-digest.md` (`vidn`).
- **External**
  - RDW open data (queried 2026-10-22); NHTSA vPIC and 49 CFR 565; DVLA VES documentation; KBA central register page.
  - DAT Austria SilverDAT VIN guide (2026); JATO VINView; auto.dev OEM build data; Cap HPI cap Code.
  - Auto Trader UK developer documentation (taxonomy, features, factory codes, release notes 2025) and FY2023 results.
  - mobile.de Seller API, AutoScout24 Listing Creation API, Marktplaats API.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned the Golf Variant timeline with the canonical dates (appraised Sat 11 Sept, stocked in Tue 14 Sept 2027). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
