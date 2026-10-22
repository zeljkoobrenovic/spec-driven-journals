---
status: accepted
revised: 2026-10-21
---

# Spec: Peaks, Regions and Languages: Global Scale and Reliability

## Intent

Show chief architects how to keep a global stays platform fast, available, localized and affordable when demand arrives in peaks and failures arrive together. The chapter argues for four moves. Set **journey SLOs** on search, book, pay and deliver, and count correctness (price held, reservation acknowledged, calendar closed elsewhere) as reliability. Design named **degradation modes** and edge **traffic classes** before the peak, distinct from a business-rule **disruption mode**. **Replicate reads, home the writes**: browsing can run active-active, but inventory, calendars and reservations need one writer per entity and a rehearsed failover. Measure **cost per booking** as an architecture metric beside latency. Localization is treated as a market context resolved once per request. After reading, the reader can write journey SLOs, a degradation ladder and a disaster-scenario table for their own platform.

Productscape domains covered: TAM `geoa` (Geo and Localization Services: Localization and Market Context; disruption boundaries); platform foundations across both models (the digest lists `geoa` and `idam` as foundations no stream covers). Adds the gaps the digest implies: journey SLOs, degradation modes and cost-to-serve, which neither model has as a brick.

## Audience

Chief and principal architects, platform-engineering and SRE leads, and engineering directors of OTAs and hosted-stays platforms who own availability, capacity plans, cloud spend or campaign readiness. They know SLOs, CDNs and multi-region patterns; they need the stays-specific shape (look-to-book, price-cache hit rates under campaign traffic, partner and bot traffic, reservation delivery, one-unit calendars).

## Success criteria

- [ ] Defines journey SLO (fast, definite, correct), degradation mode vs disruption mode, and cost per booking, with the four journeys tabulated.
- [ ] Tells Black Friday 2027 with ledger-consistent numbers (96,000 reads/s, about 9,600 shopping requests/s, hit rate 94% → 71%, 40 minutes of degradation) and a mechanism (campaign dates outside the 180-day hot tier).
- [ ] Gives Corvane journey SLO targets with owners, a degradation ladder (state diagram plus table with a "what never changes" column) and an edge traffic-class table.
- [ ] Explains read/write topologies with dated public evidence (Booking.com 2024 MySQL slides, Agoda 2025 and 2026 posts) and a labeled inference; maps Corvane's estate against it, including Nookaway's single region.
- [ ] Covers data residency (GDPR Chapter V, 2023 adequacy decision) and localization as a market context, linking the 0.8-point FX mismatch.
- [ ] Works a cost-per-booking example for both brands and the Black Friday capacity-vs-degradation trade-off.
- [ ] Includes a disaster-scenario table reusing ledger incidents, a trade-off table, the "Hotels and Homes" table with a sharing judgement, failure modes, the Chief Architect's view, 10 questions and a hand-off to [[marketplace-intelligence]].

## Non-goals

- Price-cache design, cell keys and accuracy measurement ([[availability-engine]]).
- Search pipeline stages and latency budget ([[stays-search-architecture]]); map rules ([[destinations-and-maps]]).
- Event backbone, outbox and replay ([[event-driven-stays]]).
- Cancellation policy and extenuating circumstances ([[changes-and-cancellations]]); payment routing and second acquirers ([[stay-payments]]).
- Metasearch integrations and affiliate APIs as products ([[demand-channels]]); GDPR and regulation in depth ([[stays-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No company publishes front-door search QPS or Black Friday multiples; the chapter says so and uses only internal throughput figures as orders of magnitude.
- No public source describes an active-active booking write path at a major stays platform; Agoda's booking-deduplication posts were not readable. Revisit if they become available.
- The Booking.com latency-conversion figure comes from a 2019 secondary summary of the KDD paper.

## Decision log

- **2026-10-21** — Made Black Friday a planned, successful degradation with one flaw (an affiliate retry storm), not an outage, so the chapter teaches designed degradation and retry budgets rather than heroics.
- **2026-10-21** — Explained the hit-rate fall by campaign target dates outside Pricegrid's 180-day hot tier, consistent with the availability-engine cell design, and derived miss load (about 27,800/s vs a 12,000/s on-demand ceiling).
- **2026-10-21** — Separated degradation mode (capacity) from disruption mode (business rules) so dynamic-pricing's and changes-and-cancellations' disruption flag has one home.
- **2026-10-21** — Introduced cost-per-booking figures for both brands (appended to the ledger) to make degradation-vs-capacity a quantified decision.

## Sources

- **Internal**
  - [[availability-engine]], [[stays-search-architecture]], [[destinations-and-maps]], [[property-page-and-room-selection]], [[connectivity-and-channel-managers]], [[calendar-sync]], [[stay-payments]], [[checkout-orchestration]], [[dynamic-pricing]].
  - `_research/brief-platform-data-ml.md`, `brief-booking-com.md`, `brief-expedia-agoda-tripcom.md`, `brief-availability-pricing.md`; `productscape-digest.md`; `scenario-ledger.md`.
- **External**
  - Google, *The Site Reliability Workbook*, "Implementing SLOs" (2018); FinOps Foundation, Unit Economics (n.d.).
  - Booking.com Engineering (2026, capacity testing; 2026, Node.js cost); Androulidakis, SREcon24 EMEA (2024).
  - Agoda Engineering (2023 Price Delivery System; 2025 Kafka failover; 2025 CTO interview; 2026 Consul; 2026 price cache).
  - Airbnb Engineering (2026 workload replay); Airbnb, Booking Holdings and Expedia 10-Ks for FY2025 (2026); Expedia Rapid rate limiting (n.d.).
  - Imperva 2025 Bad Bot Report (2025); GDPR (2016); Commission Implementing Decision (EU) 2023/1795 (2023); Google Hotel Center Price Accuracy Policy (n.d.).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Roomstead search and availability cost aligned with stays-marketplace-economics (€44M, about 46%, €0.0007 per shopping request). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
