---
status: accepted
revised: 2026-11-07
---

# Spec: What Are We Selling? Products, Variants and the Catalog

## Intent

Give a reader new to commerce architecture the product model (product, variant, SKU, GTIN, option, attribute set, taxonomy, bundle, digital good, lifecycle, translation) and the ownership question behind it: which system may change which field of product data and how every other system learns of it. The chapter's spine is Kestrel & Pine's three copies of product data (platform, ERP item master, spreadsheets, plus the connector's fourth) and Waypoint decision W3, the PIM introduced in Q3 2027 as the system of record for content while the ERP keeps identity and cost. After reading, the reader can recognize the four arrangements of product data in any merchant's landscape, say when a PIM earns its place and when it is the Giant's Boots, and treat syndication as an integration with a rejection loop rather than as a feed.

## Audience

Newcomers: engineers, product managers, analysts and consultants who have just joined a merchant, a vendor or an agency. The product manager or engineer handed "the catalog" or "the marketplace listings" as a responsibility benefits most, because the chapter gives them the ownership table and the questions to ask before touching a tool. The leader approving a PIM purchase benefits from the trade-off table and the scale-stage test.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym (SKU, GTIN, EAN, PIM, ERP, WMS, EDI, CE) is expanded on first use.
- [x] The business problem (a season typed four times, listings declined, untranslated launches) comes before any component; every component is tied to a business consequence.
- [x] The four identifiers are distinguished in a table and the immutability rule for SKU and GTIN is stated with its documented sources (Shopify, commercetools, schema.org, GS1).
- [x] An attribute-level ownership table names a system of record per kind of product data, with price and stock explicitly handed to [[pricing-architecture]] and [[inventory-and-availability]].
- [x] Four arrangements (platform as catalog, ERP as master, spreadsheets with discipline, PIM) are explained and compared in a trade-off table; the PIM threshold is stated as "more than one producer and more than one consumer" and labeled as the author's judgement.
- [x] The "Across Scale Stages: When It Fits and When It Limits" section has the four-stage table with typical, necessary and warning-sign columns, followed by a judgement.
- [x] Kestrel & Pine numbers match the ledger (3,400 products, 26,000 variants, 17,000 active, 1,200 per season, €58 landed cost, GTINs since 2021, W3 in Q3 2027, the Deprecated Endpoint of February 2027); local scene numbers (310 untranslated variants, 140 declined listings, two-day import) are labeled illustrative.
- [x] Dated public evidence appears with years in the sentence (Shopify 2,048 variants 2025-10-15; commercetools Modular Catalog 2026-09-29; Microsoft Business Central connector 2026-10-16; Google Merchant Center and bol rules accessed 2026-11); no inferred internals of any real company.
- [x] The three take-away tiers are present and honest; eight questions to ask; a hand-off to [[pricing-architecture]]; two mermaid diagrams with captions; article under 6,500 words including tables.

## Non-goals

- Prices, price lists and tax-inclusive display: [[pricing-architecture]].
- Stock, available-to-promise and the oversell: [[inventory-and-availability]].
- The search index, facets and relevance built on attributes: [[commerce-search-and-discovery]].
- Marketplace listing operations, order import and channel allocation: [[marketplaces-and-channel-integration]].
- Master data management across customers, suppliers and locations, and the cross-reference table as a product: [[identity-and-master-data]].
- The ERP's role as a hub and the ERP partner's connector: [[erp-and-back-office-integration]].
- Promotions, bundle discount allocation and gift-card liabilities: [[commerce-promotions]] and [[tax-invoicing-and-ledger]].
- Migration mechanics for the PIM introduction: [[replatforming-and-migration]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter assigns logistic attributes (weight, dimensions, customs code) to the ERP; [[warehouse-and-fulfillment]] may prefer the WMS to measure and own them at first receipt. Reconcile when that chapter is written.
- The PIM go-live sequence follows the ledger line appended by [[replatforming-and-migration]] (loaded July 2027 with 1,900 conflicting variants resolved, DE storefront first consumer in August, NL/BE and the connector in September); this chapter adds only that Spring/Summer 2028 is the first season built in the PIM, and both lines should be kept in step if either chapter changes.
- GS1's own site blocked fetching; the GTIN format facts rest on a GS1 support article and an encyclopaedia page. A reviewer with access to the GTIN Management Standard could replace the secondary citation.

## Decision log

- **2026-11-07** — Chose attribute-level ownership (a table per kind of data) over product-level ownership ("the PIM owns the product") as the chapter's central device, because the ledger's three copies exist precisely because identity, cost and content have different natural owners, and because the Business Central connector documentation shows the per-field direction as a documented setting.
- **2026-11-07** — Opened the scene with a season launch rather than with a single incident, because the ledger gives no product-data incident with numbers and a launch shows all four copies and all four producing teams at once; the scene's numbers are labeled illustrative.
- **2026-11-07** — Kept vendor PIM descriptions to two short quotations (Akeneo, Pimcore) and stated the PIM threshold as the author's judgement, since no independent study of when a PIM pays off was found.
- **2026-11-07** — Dropped GS1 Digital Link and Sunrise 2027 from the article for length; they belong in [[stores-and-omnichannel]] (2D codes at the point of sale) if anywhere.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the three copies, the catalog figures, W3 and the Deprecated Endpoint.
  - [[boundaries-and-systems-of-record]] — the system-of-record concept this chapter applies per attribute.
  - `_research/brief-catalog-pricing-search.md` Part 1 — product model, variant limits, taxonomies, PIM vendor pages, syndication rules.
  - `_research/brief-b2b-edi-erp.md` section 4.5 — the ERP, PIM and commerce ownership table.
  - `_research/brief-integration-and-data.md` — the Business Central Shopify connector's per-field direction.
- **External**
  - Shopify developer documentation and changelog (2024–2025) — the product, option and variant model; the 2,048-variant limit.
  - commercetools documentation and release notes (2026) — immutable SKUs, staged and published data, Classic and Modular catalogs.
  - schema.org *Product* (v30.1, 2026) and GS1 support (2024) — standard definitions of variant groups and the GTIN.
  - Google Merchant Center product data specification and bol Retailer API documentation (accessed 2026-11) — channel validation rules.
  - Microsoft Learn, Business Central Shopify connector (2026-10) — "decide which system is the system of record for product data".
  - Akeneo and Pimcore (accessed 2026-11) — vendor definitions of PIM.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: expanded acronyms and terms on first use, fixed the year Kestrel & Pine crossed the PIM threshold, dated volatile platform limits, removed internal ledger references, timetoread 30. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
