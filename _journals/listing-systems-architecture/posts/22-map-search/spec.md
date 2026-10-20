---
status: accepted
revised: 2026-10-20
---

# Spec: Searching by Place: Map, Polygon and Commute Search

## Intent

Show architects how to build location-centric discovery for verticals where place is the main filter. The chapter should change the reader's model in three ways. First, the map is a separate product with its own query mix, clustering, caching and evaluation, not a list with pins. Second, every way a buyer says "here" (radius, viewport, drawn polygon, named area, travel time) should be compiled server-side into a small set of engine primitives by one owner. Third, precision and privacy rules, duplicate collapsing and the routing provider's commercial terms are design inputs that decide the architecture.

## Audience

Chief architects, search and platform leads, and product and engineering directors of property, automotive and general classifieds marketplaces. They know search engines and maps as users and implementers; they need the marketplace-specific design: what to build where, what it costs at peak, and which rules to make platform invariants.

## Success criteria

- [x] Reader can name the five place expressions, their engine primitives and their cost and cacheability (table).
- [x] Reader can explain, with dated Airbnb evidence, why map ranking and evaluation differ from list ranking, and that applying it to portals is an inference.
- [x] Reader can sketch the component architecture (geo query compiler, place and boundary service, isochrone service, tile cache, neighborhood data) with at least two diagrams.
- [x] Reader can compare server-side, client-side and vector-tile clustering and state the public-point rule for aggregations.
- [x] Reader can list the polygon normalization steps and the two commute patterns (isochrone filter, per-listing travel time), and explain why routing pricing and license terms are architectural constraints (Rightmove/TravelTime, Mapbox limits, Valhalla).
- [x] Veldmark worked example (Hearthly draw-your-area, the Lyon apartment as one canonical-property pin) uses ledger-consistent numbers.
- [x] Trade-off table, vertical-differences table, failure modes, Chief Architect's view and 6–10 review questions are present.
- [x] Every company claim carries a dated source; undocumented internals (Rightmove, Idealista, Zillow draw search) are stated as not public.

## Non-goals

- Geocoding, address models, location precision policy and geo index choice (H3/S2) — owned by [[location-and-geo]]; summarized and linked.
- Engine choice, index topology and reindexing — [[search-architecture]].
- Ranking models and paid-placement blending in depth — [[ranking]].
- Saved polygon searches and alerts — [[saved-searches-and-alerts]].
- Duplicate clustering algorithms — [[entity-resolution]].
- General capacity and degradation model — [[reliability-and-scale]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No primary engineering source was found for draw-on-map search at Rightmove, Idealista or Zillow, or for Zillow's commute computation; revisit if one is published.
- Whether OpenSearch offers an equivalent of Elasticsearch's vector tile search API was not verified; the chapter tells readers to check current documentation.
- The TravelTime case study is undated vendor marketing; a dated Rightmove source on My Places would be stronger.

## Decision log

- **2026-10-19** — Centered the chapter on a server-side geo query compiler as the single owner of place semantics, rather than organizing it by query type, because the cost, privacy and caching rules all hang on that seam.
- **2026-10-19** — Used Airbnb's map-ranking papers as the main public evidence, labeled the transfer to property portals as inference, because no portal has published comparable map evaluation work.
- **2026-10-19** — Made the canonical property the map unit in the Lyon example to tie the Duplicate Echo to a visible map symptom; entity resolution itself stays in its own chapter.
- **2026-10-19** — Treated the routing provider's commercial model as an architectural constraint (Rightmove/TravelTime, Mapbox limits) instead of a procurement footnote.

## Sources

- **Internal**
  - [[location-and-geo]] — public point, place IDs, H3 resolutions.
  - [[search-architecture]], [[ranking]], [[entity-resolution]], [[saved-searches-and-alerts]], [[reliability-and-scale]], [[meet-veldmark]].
  - `_research/brief-search-discovery.md` Part 3; `_research/brief-listing-data-ingestion.md` Part 7; `_research/scenario-ledger.md`.
- **External**
  - Haldar et al., *Learning to Rank for Maps at Airbnb* (arXiv, 2024); Airbnb Tech 2025 year in review; Airbnb EBR paper (arXiv, 2026).
  - TravelTime, Rightmove case study (n.d.); HousingWire on Zillow commute search (2024); Elastic Rightmove case study (2025); Google Cloud press release on Rightmove (2021).
  - Elastic geo-shape, geotile grid and vector tile documentation; OpenSearch geohex grid; Mapbox Isochrone API; Valhalla isochrone service; Mapbox Supercluster; Uber H3 (2018); 24 CFR §100.75.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: American spelling (license), Zillow 2024 claim corrected (no schools), Hearthly agency precision and Valuo training aligned with the ledger, H3 res-7 size fixed, writer-brief wording removed, acronyms expanded, timetoread 36 min. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 6 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Architecture heading now names the design (a geo query compiler in front of the engine). *(AI-mediated session)*
