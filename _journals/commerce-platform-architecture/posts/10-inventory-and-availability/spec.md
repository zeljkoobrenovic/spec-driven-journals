---
status: accepted
revised: 2026-11-07
---

# Spec: Is It in Stock? Inventory, Availability and the Promise You Can Keep

> Working doc for the post in this folder. Lives next to `index.md`, versioned
> in git, surfaced as a "View spec" link in the rendered post. The spec drives
> the post; the post is the artifact.

## Intent

Chapter 10 of *ORDERED* (contract 10 in `PLAN.md`) answers one question for a reader new to commerce: what does "in stock" mean, who computes it, and how do you avoid selling what you do not have? The reader should leave able to separate the counted fact (on hand) from the claims against it (committed, reserved, held back) and the derivation (available-to-promise), to say when a unit becomes "promised" and what each choice costs, to explain why multi-location and multi-channel selling need an availability service with per-channel buffers and wholesale allocations, and to name the causes of an oversell (several writers, periodic copying, reservation windows, wrong counts). The Black Friday Oversell is the spine: the chapter reconstructs it and shows what Waypoint decision W1 (WMS as system of record for physical stock, an availability service bought as an OMS module, stock events replacing the hourly chain) would have changed.

## Audience

Newcomers to commerce architecture: engineers, product managers, analysts and leaders in their first months at a merchant, vendor or agency. The reader who benefits most is the integration or back-end engineer who inherits a stock sync and needs to know which system should own which number before touching it. Operations and e-commerce managers get the vocabulary for a sensible conversation about buffers and oversells.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (on hand, committed, reserved, safety stock, incoming, ATP, allocation, backorder, pre-order, location, channel, stock event, queue, webhook, system of record, eventual consistency, idempotent, cycle count, WMS, ERP, POS, 3PL, SKU, OMS), with every acronym expanded on first use.
- [ ] The business problem (the €96,000 Oversell, 1,340 units, 1,120 orders) comes before any component, and every component is tied to a business consequence.
- [ ] The ATP arithmetic is stated as industry practice, and the four-vendor vocabulary table is labeled as the author's alignment.
- [ ] The reservation-moment trade-off (cart, order, fulfillment) is a table with conditions, citing commercetools' three inventory modes and 10-second window, Adobe's reservations and Shopify's committed state, each dated.
- [ ] The availability-service component table, a requirements table (freshness, consistency, latency, availability per interaction) with assumptions labeled, and at least two mermaid diagrams are present.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table has specific, non-symmetric content for all four stages, with Kestrel & Pine's path as a reference.
- [ ] A Kestrel & Pine worked example reconstructs the Oversell with ledger numbers and shows W1's effect, with illustrative additions (channel split, buffers) labeled.
- [ ] "When it goes wrong" covers duplicates, out-of-order events, snapshot overwrite, two writers, outages, identifier mismatch and wrong counts with detection and recovery; the three take-away tiers are present; 8–10 questions; a Sources and Evidence section with dated entries.

## Non-goals

- Cart and checkout orchestration, including what the cart calls and when ([[cart-and-checkout]]).
- Order sourcing and routing rules in depth, split shipments and the OMS as a product category ([[order-management]]).
- Warehouse operations: receiving, picking, cycle counting mechanics, the fulfillment order contract ([[warehouse-and-fulfillment]]).
- Store stock, click-and-collect and ship-from-store mechanics ([[stores-and-omnichannel]]); marketplace stock allocation mechanics and fulfillment programs as channels ([[marketplaces-and-channel-integration]]).
- Idempotency, outbox, retries and reconciliation design in depth ([[events-consistency-and-reconciliation]]); bounded contexts and the entity–owner table ([[boundaries-and-systems-of-record]]).
- Inventory valuation and purchasing ([[erp-and-back-office-integration]]); wholesale commercial terms ([[b2b-commerce]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The Shopify changelog adding `safety_stock`, `damaged` and `quality_control` (2023) could not be fetched; the chapter says so. Re-verify when the page is available.
- The ASCM/APICS ATP definition is paraphrased as industry practice, not quoted; replace with a quotation if the dictionary becomes fetchable.
- The illustrative per-channel buffers (3 marketplace, 1 storefront) and the 790/550 channel split of the Oversell are new ledger additions; later chapters (marketplaces, peak-day journey) should reuse rather than restate them.

## Decision log

- **2026-11-07** — Made the Oversell reconstruction (an illustrative timeline with ledger totals) the opening scene rather than a vocabulary lecture, so the business problem precedes every term; rejected opening with the ATP formula.
- **2026-11-07** — Chose four options (platform stock, stock master plus sync, availability service, provider pool) over a two-way "sync vs events" framing, because the Growing-stage reader's real choice is the second option and the Group-stage reader's is the fourth.
- **2026-11-07** — Kept the vendor evidence inside the explanatory sections and reduced "In practice" to the one empirical finding (DeHoratius and Raman) plus the worked example, to stay within the length cap without dropping evidence.
- **2026-11-07** — Left sourcing rules, split shipments and the OMS to chapter 13, and idempotency and reconciliation design to chapter 25, naming both at the handoff points rather than re-teaching them.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the systems landscape, the sync chain, the Oversell and the App That Wrote Stock, W1.
  - [[boundaries-and-systems-of-record]] — the system-of-record idea the chapter uses for on hand.
  - [[order-management]] — sourcing, split shipments and the OMS whose module hosts the availability service.
  - [[events-consistency-and-reconciliation]] — idempotency, ordering and reconciliation, referenced not re-taught.
  - `_research/brief-inventory-fulfillment-returns.md` (Part 1), `_research/brief-integration-and-data.md` (Parts 1–2, 5.3), `_research/brief-shopify.md` (4.4, 5.4) — the factual base.
- **External**
  - Shopify developer documentation and changelogs (inventory quantities; POS states 2023-02-09; reserved to committed 2026-08-05; fulfillment services; webhooks) — vocabulary, arithmetic, semantics change, hourly polling, delivery not guaranteed.
  - commercetools API documentation (inventory, carts, inventory APIs overview) — inventory modes, reservation expiry, 10-second window.
  - Adobe Commerce Inventory Management documentation (2026-08) — sources, stocks, reservations, sourcing algorithms.
  - SAP Commerce 2205 StockService Javadoc (2022) — reserve and release per warehouse.
  - Microsoft Learn, Business Central and Shopify inventory sync (2026-10-14) — compare-then-send sync.
  - Picqer API documentation — stock-changed webhook.
  - Confluent blog, Walmart inventory (2020-05-04) — one partition per item and store.
  - Zalando SE, ZEOS and NEXT (2024-11-21); letter to shareholders 2025 (2026-03-12) — shared stock pool.
  - DeHoratius and Raman, *Management Science* (2008) — inventory record inaccuracy.
  - Directive 2011/83/EU, Article 18 — 30-day delivery rule.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: aligned the Oversell timeline with the 21:05 manual zeroing in the connector, corrected the ZEOS quote, removed the internal research-brief citation and ledger references, confirmed the 41-app count (ruling 10), made the post-Waypoint stock path explicit (WMS events via the iPaaS, not the ERP). *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: stock writers before Waypoint aligned to six (WMS feed via the ERP's hourly sync, hand edits in ERP and platform, three apps), four of them automated flows (consistency item 22). *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
