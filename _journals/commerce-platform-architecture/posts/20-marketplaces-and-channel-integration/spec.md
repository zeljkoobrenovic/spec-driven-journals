---
status: accepted
revised: 2026-11-07
---

# Spec: Selling on Someone Else's Platform: Marketplaces and Channel Integration

> Working doc for the post in this folder. The spec drives the post; the post is the artifact.

## Intent

Chapter 20 of *ORDERED* (Part V, CHANNELS) teaches a reader new to commerce architecture what it takes to list, sell and ship on a marketplace, and where marketplace orders and stock belong in the merchant's systems. It must leave the reader with one rule they can apply in a design review: the channel connector translates between the merchant's systems of record and the marketplaces, and it owns nothing (not product content, not the stock figure, not the order). It must also make the reader see the marketplace scorecard (cancellation, late shipment, tracking) as a freshness requirement on their own integrations, and the marketplace's API deprecation schedule as a dated contract clause someone must own.

## Audience

Newcomers: engineers, product managers, analysts and leaders who have joined a merchant that sells on marketplaces or a vendor that connects to them. The role that benefits most is the engineer or integration lead who inherits a channel connector and has to decide what it may hold; the ecommerce manager who owns the seller accounts benefits next, because the chapter turns the scorecard into integration requirements.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone: marketplace, listing, offer, buy box, commission, seller-fulfilled, marketplace-fulfilled, channel connector, channel allocation, available-to-promise, rate limit, feed, notification, idempotent, deprecation, price parity, repricing, shopping feed, retail media.
- [ ] The business problem comes first (reach in exchange for commission, rules and a scorecard) and every component is tied to a scorecard metric or a money consequence.
- [ ] The five flows (listings, stock, prices, orders, status back-flow) are described with a requirements table (freshness, consistency, failure when late) and the order lifecycle has a sequence diagram.
- [ ] Channel allocation is explained as "the number you send is a promise", with a policy table (shared pool, fixed, buffer, percentage, computed ATP) and marketplace-held stock modeled as an external location.
- [ ] Kestrel & Pine's thread matches the ledger: the Oversell's marketplace share and bol strike (illustrative, added to the ledger), the Deprecated Endpoint (February 2027, two days of stale stock to bol), the December 2026 ten-unit buffer (added to the ledger), W1 and W2 as the target state, and the marketplace variant of 13 April 2027 worked in both fulfillment models.
- [ ] Every company claim carries a year and a linked source; Amazon's and bol's thresholds, rate limits and deprecation policy, Zalando's ZEOS and Connected Retail, TikTok and Meta dates, and the DSA Article 30 date are all sourced; inferred mechanisms are labeled as the author's synthesis.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage and ends with the judgement that the mechanism scales with the number of order sources, not order volume.
- [ ] The three take-away tiers are present and honest; Questions to Ask has at least eight entries; the article stays within 4,000–6,500 words.

## Non-goals

- The availability calculation itself, reservations and safety stock: [[inventory-and-availability]] owns them; this chapter uses available-to-promise per channel as an input.
- The order record's state model and the OMS: [[order-management]] owns them; this chapter only decides where marketplace orders are created.
- API versioning discipline in general: [[api-contracts-and-versioning]] owns it; the chapter gives the marketplace case.
- Store stock and ship-from-store programs: [[stores-and-omnichannel]].
- Returns handling and refund reconciliation: [[returns-and-exchanges]]; the chapter only notes marketplace returns as an order-record event.
- Operating a marketplace (seller onboarding, payouts, ranking): LISTED's territory; the chapter defines the terms and points to [[marketplace-regulation]] and [[liquidity-and-network-effects]].
- Fee economics and margin reporting per channel: [[commerce-data-and-analytics]] and [[commerce-business-models]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Zalando's current partner commission and partner share of GMV were not verifiable; the chapter cites the 2021 share with an evidence-age note. Update if the 2025 annual report can be read.
- Typical connector sync intervals are not published; the chapter says "within minutes" as the target and labels the mechanism as the author's synthesis.
- Amazon's SP-API data protection policy (retention of buyer data after shipment) was not fetched; the chapter points to the Restricted Data Token and the privacy chapter without stating retention periods.

## Decision log

- **2026-11-07** — Organized the chapter around the connector-owns-nothing rule rather than around a vendor-by-vendor tour, because the reader needs one portable principle and the vendor facts change yearly; vendors appear as dated evidence for the principle.
- **2026-11-07** — Used the marketplace scorecard as the way into integration requirements (metrics to freshness per flow) instead of starting from APIs, so the business consequence precedes the technical detail, as the style guide requires.
- **2026-11-07** — Kept marketplace-operator architecture to one paragraph and pointed to LISTED, rejecting a longer Mirakl section; the book's reader is a merchant or vendor, not an operator.
- **2026-11-07** — Added two illustrative Kestrel & Pine facts (the Oversell's marketplace share and strike; the ten-unit buffer) to the ledger so chapters 10, 26 and Journey 4 can reuse them.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the marketplace line, the connector, the Oversell and the Deprecated Endpoint.
  - [[inventory-and-availability]] — available-to-promise and external locations.
  - [[order-management]] — the one order record (W2).
  - [[api-contracts-and-versioning]] — deprecation discipline.
  - [[pricing-architecture]] — channel price as a derived price.
  - `_research/brief-marketplaces-channels-pos.md` — the verified facts on Amazon, bol, Zalando, connectors, social channels and the DSA.
- **External**
  - Amazon SP-API documentation (rate limits, Orders, Feeds, Notifications, Tokens), accessed 2026-11 — API constraints and the events-over-polling guidance.
  - Amazon Order Performance Program policy (2026) and seller blog (2024) — performance thresholds.
  - bol Retailer API lifecycle, rate limits and partner platform standards, accessed 2026-11; partner news of 2026-11-03 — deprecation policy, strikes, the v10 retirement date.
  - Zalando corporate releases (2022, 2023, 2025), partner university page, TextilWirtschaft (2026) — ZFS, ZEOS, Connected Retail's end.
  - Bundeskartellamt press release (2013) — price parity and the marketplace as competitor.
  - Regulation (EU) 2022/2065 — Article 30 trader traceability.
  - TikTok newsroom (2026), PPC Land (2025) — social channels switching between feed and checkout.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, acronyms expanded on first use, Amazon 15% labeled as the US rate (item 7), unverified bol API version dropped, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: dropped "recorded in the ledger" from an illustrative label. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
