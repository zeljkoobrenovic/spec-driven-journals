---
status: accepted
revised: 2026-10-21
---

# Spec: Searching Dates, Not Documents: Search Architecture for Stays

## Intent

Explain how search must be built when every query carries dates, a party and a price computed per request. The chapter defines the stays search pipeline (destination resolution, candidate retrieval, exact availability and offer selection, stay pricing, ranking, presentation), argues for a two-layer index (slow content fields plus a coarse availability projection, with exact prices kept outside the index), shows why filters, facets and price sorts are correct only after the availability join, and works through flexible dates, multi-room and group searches, latency budgets and partner traffic. It ends with the group-level question that opens Part IV for Corvane: what can a hotel marketplace and a homes marketplace share in search? The answer: the query and result contract, filter vocabulary, destination service, price composition and platform operations; not indexes, availability layers or rankers.

It owns **availability-aware search**, **flexible search** and the **stays search pipeline**.

Productscape domains covered: TAM `srch` (search index and facet engine, inventory update feed), TAM `home` (landing assembly, briefly; owned by [[demand-channels]]); HSM `srch` (search index and relevance engine), HSM `insp` (category and flexible-destination browsing). The digest's missing edge `srch` → `cala` (search without availability) is supplied by the availability projector.

## Audience

Chief architects, search and platform leads, and principal engineers of OTAs and hosted-stays marketplaces who must decide where availability and price enter search, how stale each may be, and what to share across brands. They know search engines; they need the stays-specific consequences.

## Success criteria

- [ ] Reader can name the pipeline stages, their candidate counts and cost per candidate, and the two boundaries (retrieval vs exact check; pricing vs presentation) that carry most of the design.
- [ ] Reader can explain the two-layer index and the availability projector, size an availability summary for homes and for hotels, and say which direction the summary should fail in.
- [ ] Reader can decide where each filter is evaluated (content, offer selection, after pricing), including rate-plan filters that change which offer represents a property.
- [ ] Reader can explain why flexible-date search needs precomputed availability, with numbers.
- [ ] Reader sees dated public evidence (Airbnb 2022–2026, Agoda 2023/2026, Expedia 2021/2024/filings, Booking.com 2019/2025/2026) and the explicit gaps (Booking.com's availability search is undocumented).
- [ ] The Corvane worked example agrees with the ledger (Roomstead and Nookaway systems, volumes, the Novak total €1,271.20) and shows before/after numbers.
- [ ] The Hotels and Homes table and the "one search for two marketplaces?" judgement are specific, not symmetric filler.
- [ ] Trade-off table, four diagrams, failure modes, Chief Architect's view, questions to ask and sources are present.

## Non-goals

- Availability computation, price caching, staleness measurement and metasearch price accuracy ([[availability-engine]]).
- The ARI data model and restriction semantics ([[rates-and-availability-model]]).
- Destination graph, geo indexing, map viewport search ([[destinations-and-maps]]).
- Ranking objectives, learning to rank, paid visibility and ranking transparency ([[stays-ranking]]).
- Personalization and saved intent ([[personalization-and-recommendations]]).
- Total-price display rules on the property page ([[property-page-and-room-selection]]).
- Metasearch feeds, landing pages and B2B distribution APIs ([[demand-channels]]).
- Platform-wide degradation and peak handling ([[global-scale-and-reliability]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source describes how Booking.com, Expedia, Agoda or Trip.com join availability into destination search; the reference design stays labeled as such until one appears.
- Whether Corvane consolidates search engines (Elasticsearch 8 vs OpenSearch) in 2028 is left to [[converging-two-marketplaces]] and [[organizing-stays-engineering]].
- The ledger's Roomstead "1,400 availability lookups per gross reservation" does not reconcile with 21,000 lookups/s and 45 million reservations; this chapter uses only the per-second figures.

## Decision log

- **2026-10-21** — Framed the chapter around one query run through both brands (13 May 2027) rather than an incident, because the chapter's question is architectural (what depends on what is sold) and the neighbours already own the incidents.
- **2026-10-21** — Made the availability projector and the two-layer index the central mechanism, rather than engine choice, because it is where hotel and home search diverge and where the public evidence (Airbnb flexible-date precompute, Agoda itinerary-keyed cache) points.
- **2026-10-21** — Recommended shared contract plus federated engines for cross-brand search instead of a merged index, citing Expedia's documented Vrbo re-platforming slowdown with the cause explicitly labeled as inference.
- **2026-10-21** — Kept cache internals and price accuracy in [[availability-engine]]; this chapter covers only how search consumes them.

## Sources

- **Internal**
  - [[rates-and-availability-model]], [[availability-engine]], [[calendar-sync]] — availability semantics and caches the pipeline consumes.
  - [[destinations-and-maps]], [[stays-ranking]], [[property-page-and-room-selection]] — neighbouring stages.
  - `_research/brief-search-discovery.md`, `brief-availability-pricing.md`, `brief-expedia-agoda-tripcom.md`, `brief-booking-com.md`, `brief-airbnb.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Abdool et al., *Applying Embedding-Based Retrieval to Airbnb Search* (arXiv, 2026) — staged pipeline, flexible-date precompute, update rates.
  - Agoda Engineering, *How Agoda Scaled Its Price Cache with DragonflyDB* (2026) — itinerary-keyed OTA price cache.
  - Expedia Group Technology, *Learning to Rank at Expedia Group* (2024) and Rapid API documentation — candidate generation, multi-room limits, partner rate limits, Vrbo calendar API.
  - Expedia Group 10-K FY2022, Q1 2024 results, 10-K FY2025 — front-end consolidation and Vrbo re-platforming.
  - Airbnb, *2022 Summer Release* and *Total price display is now standard globally* (2025) — flexible search, categories, total price in search.
  - FTC Rule on Unfair or Deceptive Fees (2025); Directive 2005/29/EC — total price in search.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed 9,006 to 8,492 words; Waypoint approval aligned to June 2027; Nookaway rectangle aligned to the ledger (stretched to Cascais, takes in Almada, Seixal and Barreiro); 1,400 shopping-request wording added; old evidence flagged. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
