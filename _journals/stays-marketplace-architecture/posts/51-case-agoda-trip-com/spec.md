---
status: accepted
revised: 2026-10-22
---

# Spec: Agoda and Trip.com: Asian OTAs at Scale

## Intent

Give chief architects a disciplined reading of two Asian OTAs whose public records differ sharply. Agoda has published dated, concrete engineering on the parts of an OTA most companies keep quiet: supply ingestion (push streams and QPS-capped pulls), an itinerary-keyed price cache with a 5:1 write-to-read load, risk-ordered multi-product booking, cross-data-center duplicate-booking prevention, and a post-booking service rebuilt as a modular monolith after a line-by-line port. Trip.com has published a filing (agency model, guaranteed-allotment and on-request contracts, hotel matching, incremental rate updates), one AI product announcement and infrastructure repositories (Apollo, X-Pipe, DRC). The case separates documented facts (with publication dates), the author's reading, and labeled inferences; says plainly where the evidence stops, especially for Trip.com; and ends by testing the book's patterns and Corvane's 2027 choices against the record.

Productscape domains touched (as a test of chapters, not as owner): TAM supply connectivity and ARI ingestion, availability and pricing cache, content mapping, checkout and reservation, platform foundations; the agency/merchant money model. The case owns no terms.

## Audience

Chief and principal architects, supply, pricing and booking leads, and platform leads of OTAs and travel groups, especially those adding Asia-Pacific supply or competing with these two companies. They know caching, sagas and multi-region systems; they need to know what is documented, what is not, and what it implies for their own design reviews.

## Success criteria

- [ ] Every Agoda and Trip.com claim carries a source and publication year; archived reads and pre-2023 evidence are flagged; inferences sit in a labeled callout or are marked "my reading".
- [ ] Agoda's price path is explained with the 2026 numbers (about 300,000 reads/s, 1.5–1.6 million writes/s, 1.5 TB, 72 SQL Server shards, 8 ms P99, three-hour re-warm, hit-ratio failover) and a diagram that marks the undocumented join.
- [ ] MPBE risk ordering, the 2024 deduplication design and BAPI's 2019–2026 history are each tied to a book pattern.
- [ ] Trip.com is limited to the 20-F, TripGenie and the three repositories, with the limits stated; the allotment/on-request inference is labeled and diagrammed as inference.
- [ ] Includes a trade-off table, failure modes, a "Where the Public Evidence Stops" table, a Chief Architect's view and 6–10 questions.
- [ ] Ends with a pattern-verdict table linking the owning chapters and a Corvane comparison table whose numbers match the ledger (Pricegrid hot tier and Black Friday, Brightwell, Concord, checkout attempt contract, Keystone Exit Plan, Ranking Policy v1).
- [ ] Stays within 5,000–7,000 words of article text.

## Non-goals

- Booking.com, the sibling Booking Holdings brand ([[case-booking-com]]); Expedia's Rapid and Vrbo ([[case-expedia-vrbo]]).
- Teaching price-cache design, staleness budgets or pull-supply budgets in general ([[availability-engine]], [[connectivity-and-channel-managers]]).
- Saga and idempotency design ([[checkout-orchestration]]); migration method ([[modernizing-a-live-marketplace]]); experimentation method ([[stays-experimentation]]).
- Any description of Agoda or Trip.com ranking, inventory locking or reservation state machines, which are not public.
- A "Setting the scene" or "Hotels and Homes" section (Part X format).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether PriceAggregator (2020) still runs in front of the 2026 Price Cache; whether the 2023 Price Delivery System and the Price Cache are layers of one path.
- Agoda Homes' current supply model; Agoda's ranking and any transparency statement.
- Trip.com's on-request confirmation flow, hotel matching method, and whether DRC replication carries hotel or reservation data.
- Part 2 of Agoda's deduplication post (2024) was not read.

## Decision log

- **2026-10-21** — Gave Agoda most of the space in proportion to evidence, and stated that proportion in the opening, instead of balancing the two companies artificially.
- **2026-10-21** — Added Trip.com's open-source repositories (Apollo, X-Pipe, DRC) as the only first-party technical artifacts, with the explicit warning that they do not show hotel or reservation design.
- **2026-10-21** — Read Agoda's 2024 deduplication post (archived copy), not in the briefs, because it is the clearest public example of a safeguard failing when traffic moves between data centers.
- **2026-10-21** — Kept Corvane to the final comparison, matching ledger facts only; no new canonical facts added.

## Sources

- **Internal**
  - [[availability-engine]], [[connectivity-and-channel-managers]], [[content-and-media]], [[checkout-orchestration]], [[modernizing-a-live-marketplace]], [[stays-experimentation]], [[stays-ranking]], [[global-scale-and-reliability]], [[merchant-and-agency-models]], [[case-expedia-vrbo]].
  - `_research/brief-expedia-agoda-tripcom.md` (Parts 6, 7, 9), `brief-availability-pricing.md`, `brief-platform-data-ml.md`, `brief-search-discovery.md`, `brief-host-partner-guest-service.md`; `scenario-ledger.md`.
- **External**
  - Agoda Engineering posts: 2023 (PDS, Kafka, p-values), 2024 (Kafka load balancing, booking deduplication), 2025 (MPBE, CTO interview, Kafka failover), 2026 (design system, flight connectors, Consul, Price Cache, BAPI); PriceAggregator, arXiv (2020); Agoda Supply API (n.d.); Agoda Growth Program (2025); Partner Portal release (2026).
  - Booking Holdings 10-K FY2025 (2026); Trip.com Group 20-F FY2025 (2026); TripGenie announcement (2023); Apollo, X-Pipe and DRC repositories (2016–2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Booking.com date-range contrast narrowed to B.XML; dead Agoda Supply API link flagged; OTA and TTL expanded; timetoread 31; Trip.com 20-F and Agoda posts re-verified. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,922 → 5,787 prose words; Failure Modes compressed to pointers into the body; trade-offs recap paragraph and repeated restatements in the Chief Architect's view cut; no headings changed. *(AI-mediated session)*

- **2026-10-22** — Agoda Supply API citation verified live; added read date 22 Oct 2026. *(AI-mediated session)*
