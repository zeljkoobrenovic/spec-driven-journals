---
status: accepted
revised: 2026-10-22
---

# Spec: Is It Still Available? Availability Search, Caching and Price Accuracy

## Intent

Show chief architects how a stays marketplace answers "what can I book, and for how much" at look-to-book scale without lying to the guest. The chapter treats the availability engine as a **read model of supply truth with an explicit staleness budget**. One versioned offer-computation kernel is shared by every path that shows a price, a divergence sampler measures accuracy, and a price check at commitment turns staleness into a designed outcome. After reading, the reader can name the cell and key of their grid, separate staleness errors from arithmetic errors, and set freshness budgets and accuracy metrics with owners.

Productscape domains covered: TAM `srch` (Inventory Update Feed worker), `invt` (Rate and Availability Core as source of truth), `room` (Room Offer API); HSM `cala` (Availability engine, availability accuracy). Adds the gap the digest names: **availability/price cache for search**.

## Audience

Chief and principal architects, search and pricing leads, and engineering directors of OTAs and hosted-stays platforms who own search latency, metasearch performance or checkout conversion. They know caches and event streams; they need the stays-specific shape (stay-level restrictions, look-to-book, metasearch accuracy policies, consumer-law limits on price changes).

## Success criteria

- [ ] Defines availability engine, offer computation, price accuracy and cache staleness (age-based vs divergence-based) precisely.
- [ ] Explains why look-to-book forces cached answers, with Corvane's 1,400 requests per reservation and 21,000/64,000 lookups per second reconciled.
- [ ] Gives an architecture with component contracts (fan-out, grid builder, grid, offer API, on-demand path, kernel, price check, sampler), a cell-key design table and a freshness-strategy table.
- [ ] Uses dated, sourced public evidence (Agoda 2026 and 2023 posts and 2020 paper, Expedia Rapid, Expedia Group 2021, Airbnb 2026, Vrbo calendar, Google Hotel Center, Hotelbeds), with an explicit inference callout for Booking.com and Expedia internals.
- [ ] Works a Corvane example with ledger-consistent numbers: the May 2027 accuracy audit (9 points: 5.7 staleness, 2.8 arithmetic, 0.5 other), the Hotel Miradouro cell fan-out, and the pilot result.
- [ ] Covers price checks within the EU 2021 UCPD guidance and the FTC fees rule, with four contract rules.
- [ ] Includes the "Hotels and Homes" table and judges what to share (contract and kernel composition, not the engine).
- [ ] Includes trade-offs, failure modes, Chief Architect's view, 6–10 questions and a hand-off to [[inventory-integrity]].

## Non-goals

- The ARI data model, rate plans and restriction semantics in depth ([[rates-and-availability-model]]).
- Holds, concurrency control, overbooking and double booking ([[inventory-integrity]]).
- Retrieval, index design and ranking ([[stays-search-architecture]], [[stays-ranking]]).
- Total-price display and room comparison UI ([[property-page-and-room-selection]]).
- The checkout saga and idempotency ([[checkout-orchestration]]).
- Black Friday capacity engineering ([[global-scale-and-reliability]]); iCal mechanics ([[calendar-sync]]); tax determination ([[taxes-on-stays]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No first-party source describes how Booking.com, Expedia or Trip.com join availability into consumer search; the chapter labels its reference architecture as inference. Revisit if one is published.
- Google's Hotel Center mismatch-reason list is from search-index excerpts (2026), not a fetched page.
- The Agoda SmartTTL detail is reported from search excerpts of 2020 blog posts.

## Decision log

- **2026-10-21** — Framed the incident as a metasearch accuracy downgrade with a cause breakdown, rather than a single outage, so the chapter could separate staleness from arithmetic. The split (5.7 vs 2.8 points) carries the "one kernel" key point.
- **2026-10-21** — Reconciled the ledger's two look-to-book figures by defining 1,400 as shopping requests per gross reservation and 21,000/s as Pricegrid property-level reads (about ten per request); appended to the ledger.
- **2026-10-21** — Recommended keeping audience and currency out of the grid key and storing pre-composition offers, against the faster-read alternative of storing finished offers, because Corvane's audit errors came from duplicated composition.
- **2026-10-21** — Kept Black Friday 2027 as a short forward reference; its capacity story belongs to [[global-scale-and-reliability]].

## Sources

- **Internal**
  - [[rates-and-availability-model]], [[stays-marketplace-economics]], [[connectivity-and-channel-managers]] (the €12 rate), [[calendar-sync]] (iCal confidence), [[converging-two-marketplaces]] (One Stay sharing).
  - `_research/brief-availability-pricing.md`, `brief-expedia-agoda-tripcom.md`, `brief-booking-com.md`, `brief-search-discovery.md`, `brief-platform-data-ml.md`, `brief-supply-connectivity.md`; `productscape-digest.md`; `scenario-ledger.md`.
- **External**
  - Agoda Engineering, "How Agoda Scaled Its Price Cache with DragonflyDB" (2026) — write-heavy price cache, tiering, hit-ratio failover.
  - Zhang et al., "PriceAggregator" (Agoda, 2020) — QPS-budgeted supplier pulls.
  - Expedia Group Rapid documentation (n.d.) — shop, price check, book; rate limits by traffic vs revenue; Vrbo calendar without caching.
  - Abdool et al., "Applying Embedding-Based Retrieval to Airbnb Search" (2026) — precomputed availability and pricing with post-filter.
  - Google Hotel Center Price Accuracy Policy (n.d.) and delivery modes (2025).
  - European Commission UCPD guidance (2021); FTC fees rule FAQ (2025).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: lightly trimmed (8,939 → 8,683 words), aligned search volumes with the ledger (1,400 shopping requests, ~10 Pricegrid reads each), corrected the metasearch traffic share, replaced the "41,000 mapped bedbank properties" claim with the Brightwell Beds reference, removed an unsourced SmartTTL claim and flagged old evidence. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,082 → 6,947 prose words; opening now places the chapter as the read side of Part III; "Warming for peaks and event dates" moved from Measuring into Architecture; Booking.com latency subsection deleted (told in several other chapters) and its inference callout moved into the In Practice lead; sentence-level tightening. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass (needless test): 6,947 → 6,476 prose words (7,082 → 6,476 since HEAD, −9%); Failure Modes compressed to one-line bullets pointing to the sections that handle each failure; Chief Architect's view, look-to-book, cell-key, trade-offs and Hotels and Homes paragraphs trimmed where they restated earlier sections; Expedia "ladder" paragraph and the affiliate/scraper aside deleted; questions 8 and 9 merged; figure captions shortened. No headings renamed; spec criteria unchanged. *(AI-mediated session)*
- **2026-10-22** — Corrected the price-mismatch claim to match the chapter's audit (staleness 5.7 points, arithmetic 2.8): arithmetic is a large share, not most. *(AI-mediated session)*
