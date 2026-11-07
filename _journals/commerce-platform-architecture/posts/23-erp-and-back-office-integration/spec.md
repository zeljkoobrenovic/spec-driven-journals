---
status: accepted
revised: 2026-11-07
---

# Spec: The Back Office: ERP Integration and Who Is the Hub

> Working doc for chapter 23 of *ORDERED: Architecting Commerce Platforms*. Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Explain to a reader who has never opened an ERP what it does in a commerce business (ledger, purchasing, inventory valuation, master data), what flows between it and the commerce systems in which direction and at what cadence, and how to decide whether the ERP, the commerce platform, an OMS or nothing should be the integration hub. The chapter's durable claims: the ERP should be the system of record for finance and never the system a storefront waits on ("finance can be batch, availability cannot"); "who is the hub" is a scale-stage decision with three honest answers and one accident; and the connector an ERP partner builds is a contract the merchant must own. After reading, the reader can explain Waypoint's finance-only rule, read a vendor connector's documentation as an entity–owner table, and spot an ERP sitting in a real-time path.

## Audience

Newcomers to commerce architecture. Benefits most: an engineer or product manager who inherits "the ERP integration" and a finance lead who wants to know why month-end takes eleven days; also an architect weighing an ERP-centered suite against a platform-plus-OMS assembly.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (ERP, ledger, posting, inventory valuation, costing method, master data, master data ownership, system of record, integration hub, OMS, PIM, WMS, PSP, iPaaS, connector, event, batch, idempotent, reconciliation, available-to-promise).
- [ ] The four jobs of the ERP are stated in a table with what each needs from commerce and gives back; the quantity-vs-value distinction (WMS vs ERP) is explicit and sourced to IAS 2 and Business Central's costing documentation.
- [ ] The flows table (orders, shipments, payments, invoices, products, stock, customers) gives direction, system of record and cadence; a requirements table (fresh, consistent, fast, available) follows, with availability marked "not from the ERP".
- [ ] The hub debate is a four-row table (ERP, commerce platform, OMS, iPaaS/no hub) with fits and breaks, sourced to Sana, Business Central, OneStock and the Kestrel & Pine baseline; Waypoint's finance-only rule is presented as the OMS-as-hub position written as an ownership rule, consistent with W1–W5.
- [ ] Business Central's Shopify connector is used as a dated (2026) example of a vendor encoding ownership in configuration, with an INFERENCE label on the judgement that its inventory rule is wrong at Kestrel & Pine's size.
- [ ] Eva's order is worked in the books with ledger numbers (€235, €199 + 2 × €18, 21% VAT, landed cost €58, the €199 credit note in the exchange), with the PSP fee labeled as an assumption; the Three-Status Order, Price Drift, Oversell and Double Refund are used consistently with the ledger.
- [ ] At least two mermaid diagrams, a trade-off table, the "Across Scale Stages" section with its table, "When it goes wrong", the three take-away tiers, 6–10 questions, grouped sources.
- [ ] Article length between 4,000 and 6,500 words including tables.

## Non-goals

- The invoice as a legal document, VAT, revenue recognition and order-to-ledger detail: [[tax-invoicing-and-ledger]]; payout reconciliation: `payments-to-ledger` in the finance book.
- EDI documents and e-invoicing mandates: [[edi-and-e-invoicing]].
- Integration styles, the iPaaS as a tool and the integration inventory: [[integration-styles]]; idempotency, outbox, reconciliation mechanics: [[events-consistency-and-reconciliation]].
- The OMS's internal state model and order orchestration: [[order-management]]; ATP and stock events: [[inventory-and-availability]]; the PIM: [[product-information]].
- The ERP-centered platform category as a market (Odoo, JTL, PlentyONE, NetSuite): [[commerce-platform-landscape]].
- Vendor and partner management as an organizational question: [[organizing-commerce-engineering]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- NetSuite/SuiteCommerce could not be fetched for the brief; the chapter makes no feature claims about it.
- The Business Central connector's first release date is inferred from Shopify's 2021 "early 2022" announcement; no Microsoft release note was read.
- The chapter's "finance-only rule" restates W1–W5 for the ERP; if a later chapter needs the ERP to feed anything to a channel (for example expected stock for pre-orders), the ledger addition should be extended rather than contradicted.

## Decision log

- **2026-11-07** — Chose the partner-built connector as the scene and the finance-only rule as the spine, over a tour of ERP modules, because the newcomer's practical problem is the undocumented integration, not the ERP's feature list.
- **2026-11-07** — Presented the hub debate as four options including "no hub" (the iPaaS accident), because Kestrel & Pine's baseline is the fourth case and the book's reader is most likely to be living in it.
- **2026-11-07** — Used Microsoft's connector documentation as the main dated example rather than an ERP vendor's marketing, because it is the only public source that states ownership per entity in configuration terms.
- **2026-11-07** — Kept Eva's order in the books to the postings a newcomer can follow (revenue, VAT, cost, fee, credit note) and sent the payout-reconciliation depth to the finance book.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the ERP since 2023, the partner-built connector, the incidents, Waypoint W1–W5.
  - [[boundaries-and-systems-of-record]] — ownership per fact; the entity–owner table this chapter applies to the back office.
  - [[order-management]] — the OMS as order hub.
  - [[integration-styles]] and [[events-consistency-and-reconciliation]] — the iPaaS, events, batch and reconciliation.
  - [[edi-and-e-invoicing]] and [[tax-invoicing-and-ledger]] — invoices out of the ERP.
- **External**
  - Microsoft Learn, Business Central Shopify Connector pages (get started, items, inventory, customers, orders; September–October 2026) and costing methods (March 2026).
  - Shopify, Global ERP Program announcement (14 October 2021) and "ERP Integration: Methods, Benefits, and Examples" (updated 28 August 2026).
  - SAP Learning, S/4HANA Cloud with SAP Commerce Cloud integration journey (n.d.).
  - OneStock, "OMS vs ERP" (2026); Sana Commerce home page; Akeneo "What is a PIM?"; Exact and AFAS product pages (all accessed November 2026).
  - IFRS Foundation, IAS 2 Inventories.
  - Research briefs `_research/brief-b2b-edi-erp.md` (Part 4), `_research/brief-platform-landscape.md` (1.6) and `_research/brief-integration-and-data.md` (1.4–1.6).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: feeds-no-channel-directly wording and price ownership split per item 3, revenue recognized at delivery per item 1, Price Drift mechanism aligned with the ledger, Black Friday day figure corrected, acronyms expanded. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
