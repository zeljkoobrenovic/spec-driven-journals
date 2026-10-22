---
status: accepted
revised: 2026-10-22
---

# Spec: Where Exactly? Destinations, Geo and Map Search

## Intent

Show chief architects how a stays marketplace should understand places and let guests browse by map. The chapter argues for one versioned, owned **destination graph** that serves search, landing pages, pricing features, tax and regulation. It separates a place's official boundary from the **search area** actually searched (cells built from where guests book), and treats the map as a separate result surface: **viewport search** with dates, pin selection as a ranking decision, and **approximate location** for homes derived once from the exact address. After reading, the reader can audit their own place data, map pipeline and home-location privacy.

Productscape domains covered: TAM `dest` (Destination Discovery), `mapb` (Map-Based Stay Browser), `geoa` (Geo & Localization Services); HSM `srch` (map browse and geo-intent layer).

## Audience

Chief and enterprise architects, search and discovery leads, and platform leads of OTA-style and hosted-stays marketplaces who own (or inherit) place data, maps and the geographic side of compliance. They know search engines and spatial indexes in general; they need the stays-specific design decisions and evidence.

## Success criteria

- [ ] Reader can define place, destination, destination graph, place resolution, search area, viewport search and approximate location, and tell them apart.
- [ ] Reader can explain, with Airbnb's dated evidence (2024, 2026), why a learned or curated set of cells beats an official polygon or a rectangle as the search area.
- [ ] Reader can design viewport search where the tile cache holds only date-free geography and pins show bookable total prices.
- [ ] Reader can explain why map pin selection differs from list ranking (Airbnb 2024 map attention findings) and hand objectives to `stays-ranking`.
- [ ] Reader can design approximate location (stored public point, no per-request jitter, no exact point in the search index) while keeping jurisdictions computed from the exact point.
- [ ] Reader can weigh map tile and places vendors on cost and license terms (Google pricing and Places storage policy, OSM tile policy, self-hosted tiles).
- [ ] The Corvane thread ("Lisbon" means four things; the Novaks' search) uses ledger numbers and stays consistent.
- [ ] The Hotels and Homes section gives a specific comparison and a judgement on what to share.

## Non-goals

- The search pipeline, availability join and latency budgets — `stays-search-architecture`.
- Ranking objectives, learning to rank, commission and transparency governance — `stays-ranking`.
- General map mechanics already taught in LISTED: tile caching, clustering, drawn polygons, isochrones — `map-search`.
- Tourist-tax rates and short-term-rental rules themselves — `taxes-on-stays`, `stays-regulation`.
- Supplier property mapping and deduplication — `property-and-listing-model`.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No OTA has published map-ranking or destination-graph engineering beyond Expedia's partner Geography API; revisit if Booking.com, Expedia or Agoda publish.
- No primary source documents how hosted-stays platforms compute approximate locations; the chapter presents its design as recommendation. Verify if a platform documents its method.
- Lisbon tourist-tax rate and rules are taken from the ledger and should be verified by `taxes-on-stays`.

## Decision log

- **2026-10-21** — Framed the chapter around the separation of place (legal, official) from search area (behavioral, tunable) rather than around spatial indexes, because that separation is the decision architects get wrong; indexes are covered as supporting detail.
- **2026-10-21** — Linked to LISTED `map-search` for tiles, clustering and isochrones instead of re-teaching them; this chapter adds dates, pin pricing, map ranking and home privacy.
- **2026-10-21** — Introduced Waypoint (group destination graph and resolver) as Corvane's shared service, consistent with One Stay's "shared contracts, separate engines" stance: places shared, search areas and ranking per brand.
- **2026-10-21** — Used Expedia's Rapid Geography API (fetched October 2026) as the public reference for destination-graph shape, since no OTA engineering post on place data was found.

## Sources

- **Internal**
  - [[stays-search-architecture]] — the pipeline this chapter feeds.
  - [[stays-ranking]] — owns ranking objectives, including map surfaces.
  - [[stays-regulation]], [[taxes-on-stays]] — consumers of jurisdiction data.
  - [[map-search]] (LISTED) — general map-search mechanics.
  - `_research/brief-search-discovery.md` (Part 2, Part 7), `_research/productscape-digest.md` (`dest`, `mapb`, `geoa`), `_research/scenario-ledger.md`.
- **External**
  - Airbnb: Learning to Rank for Maps (2024), Transforming Location Retrieval (2024), High Precision Audience Expansion via Extreme Classification (2026).
  - Expedia Group Developer Hub, Rapid Geography API docs (n.d., fetched October 2026).
  - S2 Geometry and H3 documentation; Google Maps Platform pricing and Places policies (October 2026); OSMF Tile Usage Policy; Protomaps PMTiles; MapLibre.
  - Regulation (EU) 2024/1028; Directive (EU) 2019/2161.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed 9,330 to 8,497 words; worked-example retrieval count aligned with stays-search-architecture (2,600); target design marked as planned for late 2028. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,637 → 6,220 prose words; deleted the recap-only Failure Modes section; opening now names what the chapter builds on and feeds; repeated sentences cut in Architecture, Approximate Location, Chief Architect's view and the hand-off. *(AI-mediated session)*
- **2026-10-22** — Restored Failure Modes as one-line bullets (house shape). *(AI-mediated session)*
