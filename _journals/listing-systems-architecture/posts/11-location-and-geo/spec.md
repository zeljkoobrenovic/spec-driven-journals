---
status: accepted
revised: 2026-10-20
---

# Spec: Where Is It? Location, Geocoding and Privacy

## Intent

Show architects that a listing's location is a small subsystem, not a field: country-shaped address capture, geocoding with licence-bound outputs, a versioned gazetteer of places, geo indexes, a precision policy and quality and fraud signals. The chapter's central model is three representations per listing (a restricted precise point, a public point derived deterministically by policy, and stable place IDs with all ancestors). Once readers have it, they should be able to find where their own platform leaks private sellers' locations, where it holds coordinates its licences do not allow, and why their filters, maps and landing pages disagree.

## Audience

Chief and principal architects, search and data leads, and privacy and product leads of listing marketplaces, especially groups running several countries. They know search engines and geospatial basics. They need the marketplace-specific model, the licensing constraints and the privacy rules turned into architecture.

## Success criteria

- [ ] Reader can explain the three location representations, who reads each, and why the public point must be derived deterministically.
- [ ] Reader can state the distance rule (distances and distance sorting from the public point, rounded) and the trilateration risk behind it.
- [ ] Reader can compare geocoding providers and national registers by storage, display and share-alike terms, with dated sources.
- [ ] Reader can choose between engine-native geo types, geohash, H3, S2 and place-ID filters for a given job.
- [ ] Reader can resolve radius, polygon and place semantics (search origin, administrative versus curated places, bilingual names, cross-border search).
- [ ] The chapter works through the Rotterdam city bike, the Lyon apartment and the Barcelona fake-rental ring with numbers that match the ledger.
- [ ] The chapter includes a trade-off table, a vertical-differences table, at least two diagrams, a Chief Architect's view and design-review questions.

## Non-goals

- Polygon, isochrone and map-clustering query design and map ranking: [[map-search]].
- Parsing locations out of search queries: [[query-understanding]].
- The general enrichment pipeline and attribute provenance: [[normalization-and-enrichment]].
- Duplicate-detection algorithms beyond location as a blocking key: [[entity-resolution]].
- EXIF stripping and image processing: [[media-pipeline]].
- Erasure across copies and read-model design in general: [[listing-data-management]].
- The regulatory catalogue (DSA, GDPR detail): [[marketplace-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Google's historically cited latitude-longitude caching window was not found on the policy page fetched in October 2026; the chapter cites only the current page. Re-check the service-specific terms before print.
- Whether an enriched gazetteer built partly on OpenStreetMap is a "derivative database" under the ODbL is left to legal review; the chapter says so rather than answering it.
- Belgian, Polish, Portuguese and Spanish national address and cadastral registers were not verified in this session and are not named.
- A minimum-address-count rule for sparse areas is recommended without a published benchmark; consider adding one if a source appears.

## Decision log

- **2026-10-19** — Organized the chapter around three location representations rather than around providers or index types, because the privacy, licensing and filter-consistency failures all trace back to storing one field for every consumer.
- **2026-10-19** — Opened with a fictional Veldmark privacy complaint (distance and API leakage) instead of a search-quality bug, because it makes the precise/public split concrete and is the failure most readers have not considered.
- **2026-10-19** — Adopted a six-level precision scale (P0–P5) as a teaching device and as Veldmark's policy vocabulary; rejected using OSM admin levels, which vary by country.
- **2026-10-19** — Kept travel-time and polygon search to short summaries with links to [[map-search]] to avoid re-teaching what that chapter owns.

## Sources

- **Internal**
  - [[listing-aggregate]], [[categories-and-taxonomies]], [[media-pipeline]], [[entity-resolution]], [[map-search]], [[fraud-prevention]], [[multi-country-platforms]] — neighbouring ownership.
  - `_research/brief-listing-data-ingestion.md` Part 7 (address parsing, geocoding licences, hierarchies, H3/S2, obfuscation); `_research/brief-search-discovery.md` Part 3; `_research/brief-real-estate-portals.md` C.8 and D; `_research/brief-trust-safety-regulation.md` 5.10; `_research/productscape-digest.md` 5.3–5.5.
- **External**
  - Google Geocoding policies (2026), Mapbox Geocoding, OSMF Nominatim policy, OSM copyright — licensing constraints.
  - Airbnb location guidance (2025) — the documented obfuscation example.
  - Uber H3 (2018), H3 resolution table, S2 documentation, Elastic geo-shape docs — geo indexing.
  - Kadaster BAG, data.gouv.fr Base Adresse Nationale, OS Open UPRN — national registers.
  - GDPR Art. 4(1) — location data as personal data.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: country count corrected to eight (consistency-issues 19/23), Motorvane's markets completed in the cross-border example, copy count tied to Femke's erasure case, an unexplained acronym removed, reading time corrected. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,540 → 6,550 prose words; lead now ties the chapter to Part II's aggregate-and-subdomains model and names what it builds on; eight topic sentences brought forward or made concrete; no headings renamed, no sections moved; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: scene heading now "Five Answers" to match the five-row table; lead no longer says "four different ideas". *(AI-mediated session)*
