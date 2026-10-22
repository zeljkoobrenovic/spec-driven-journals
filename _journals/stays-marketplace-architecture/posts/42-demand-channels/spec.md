---
status: accepted
revised: 2026-10-22
---

# Spec: Where Guests Come From: Web, Apps, Metasearch and Partner Distribution

## Intent

Show chief architects how the demand side of a stays marketplace should be built: own web and apps, search-engine landing pages, metasearch integrations and partner distribution APIs (affiliates, white label, travel agents, corporate travel). The chapter's argument is that **every channel is a client of one stay query, one offer computation and one reservation contract**, with a channel-specific adapter that owns rendering, feeds, quotas, payment flows and tracking but never its own price arithmetic or booking path. External channels need owned integration services, look-to-book contracts (quotas by traffic against revenue, retry budgets) and a click-and-quote record, and channels are judged on stayed, cancellation-adjusted contribution and on dependence on one external company. After reading, the reader can audit which channels compute their own prices, design a metasearch landing check, set partner quotas and report channel dependence.

Productscape domains covered: TAM `home` (Landing Assembly API, Merchandising Slot Orchestration, Session Recall), `deal` (presentation of offers in slots); HSM `insp` (category and destination landing assembly). Adds the gap PLAN marks **[ADDED]**: distribution and affiliates (metasearch integration, B2B distribution API).

## Audience

Chief and principal architects, distribution and marketing-technology leads, web and mobile platform leads and engineering directors at OTAs and hosted-stays platforms who own paid-channel performance, partner APIs or the web and app front ends. They know BFFs, caching and APIs; they need the stays-specific contracts (metasearch delivery modes and landing URLs, partner look-to-book, hosted-stays distribution limits) and the economics behind them.

## Success criteria

- [ ] Defines demand channel, metasearch integration, B2B distribution API and landing assembly, with a four-family channel table and a partner-form table.
- [ ] Gives an architecture with three adapters (BFF, metasearch integration, partner API) over shared contracts and a channel ledger, with a responsibilities and "must not" table and at least two diagrams.
- [ ] Uses dated, sourced evidence: Google hotel price documentation (delivery modes, live queries with deadline and EEA restriction, landing URL variables, hotel list feed, structured data), Expedia Rapid (flow, limits, rate limiting, Vrbo constraints), Booking.com Demand API payments, Booking.com 2026 rendering post, Airbnb 2021 server-driven UI, Agoda 2026 white label and 2023 affiliate cache load, Booking, Expedia, Airbnb and Trip.com filings, DMA.
- [ ] Works a Corvane example with ledger-consistent numbers: channel mix, shopping requests per channel reconciling to 1,400, search cost per channel reconciling to €44M, metasearch contribution per stayed reservation, and one Hotel Miradouro click re-quoted at landing.
- [ ] Explains click-time re-quoting using the displayed total in the landing URL, with a landing-outcome table tied to [[availability-engine]]'s mismatch causes.
- [ ] Includes the "Hotels and Homes" table and judges what to share (channel machinery, not channel strategy).
- [ ] Includes trade-offs, failure modes, Chief Architect's view, 6–10 questions and a hand-off to [[converging-two-marketplaces]].

## Non-goals

- Price accuracy definition, the offer kernel and the accuracy sampler ([[availability-engine]]).
- The search pipeline, index design and look-to-book latency budgets ([[stays-search-architecture]]); which places exist ([[destinations-and-maps]]).
- Ranking and paid-visibility disclosure ([[stays-ranking]]); promotion eligibility ([[promotions-and-loyalty]]).
- Bot defense, traffic classes and degradation modes ([[global-scale-and-reliability]]); attribution models ([[marketplace-intelligence]]).
- Card mechanics for corporate payments ([[stay-payments]]); parity regulation in depth ([[stays-regulation]]); AI assistants as a channel ([[ai-in-travel-stays]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No company has published its SEO landing-page architecture; the landing design is the author's recommendation. Revisit if a primary source appears.
- Google's Hotel Ads bidding models (cost per click versus commission per stay) were not verified from a fetched page; the chapter describes them only generically.
- Vacation-rental metasearch sites (HomeToGo, Holidu) were not verified and are not named.
- Expedia's Vrbo-in-Rapid pages are undated and describe a limited-partner product; check before citing figures.

## Decision log

- **2026-10-21** — Framed the Corvane thread as a CFO's dependence question (41% of gross reservations with one company's last click) rather than another accuracy incident, because [[availability-engine]] already owns the May 2027 downgrade.
- **2026-10-21** — Made click-time re-quoting from the landing URL's displayed total the chapter's central metasearch design, because the URL variables are documented and it turns accuracy from the engine's sample into the marketplace's own measure on every paid click.
- **2026-10-21** — Split shopping requests per reservation by channel (300 own, 650 metasearch, 450 affiliate API) so that look-to-book and search cost per channel reconcile with the ledger's 1,400 and €44M; appended to the ledger.
- **2026-10-21** — Kept Nookaway out of outbound distribution until 2029 and argued "share the channel machinery, not the channel strategy", based on Rapid's documented Vrbo constraints.

## Sources

- **Internal**
  - [[availability-engine]], [[stays-search-architecture]], [[stays-marketplace-economics]], [[destinations-and-maps]], [[global-scale-and-reliability]], [[marketplace-intelligence]], [[checkout-orchestration]], [[calendar-sync]], [[converging-two-marketplaces]].
  - `_research/brief-search-discovery.md`, `brief-expedia-agoda-tripcom.md`, `brief-booking-com.md`, `brief-platform-data-ml.md`, `brief-airbnb.md`; `productscape-digest.md`; `scenario-ledger.md`.
- **External**
  - Google for Developers, hotel prices documentation (2025–2026): delivery modes, query messages, landing page URLs, POS syntax, hotel list feed, structured data; Google Hotel Center price accuracy policy (n.d.).
  - Expedia Group Developer Hub, Rapid (n.d.): lodging flow, shopping, rate limiting, Vrbo guide and calendar.
  - Booking.com Developers, Demand API payments overview (n.d.).
  - Booking.com Engineering (2026), Airbnb Engineering (2021), Agoda Engineering (2026, 2023).
  - Booking Holdings, Expedia Group and Airbnb 10-Ks (2026); Trip.com 20-F (2026); Regulation (EU) 2022/1925 (DMA).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Hand-off now goes to part-9 before converging-two-marketplaces; timetoread corrected. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: dropped the checkout contract from the "every door" caption to match the diagram. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,030 → 6,666 prose words; lead now places the chapter as Part VIII's last (the platform's external clients) and points to converging-two-marketplaces; "AI assistants as the next partner" folded into the Chief Architect's long-term considerations; Failure Modes compressed to one-line pointers; decisions and "What to decide" no longer restate earlier sections; BFF definition cut (audience knows BFFs). *(AI-mediated session)*
