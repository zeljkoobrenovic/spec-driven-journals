---
status: accepted
revised: 2026-11-07
---

# Spec: Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals

> Working doc for the post in this folder. The spec drives the post; the post is the artifact.

## Intent

Chapter 21 of *ORDERED* (Part V, CHANNELS) teaches a reader new to commerce architecture what changes when the buyer is a company: the customer becomes an organization with locations, people and roles; the price becomes a layered, negotiated promise with a validity date; payment becomes a terms-and-credit decision; and the order can arrive by portal, e-mail, EDI or punchout. The reader should leave able to name the B2B objects every platform shares, to say which system should own the company account, the prices and the credit limit, and to read a merchant's share of hand-keyed wholesale orders as a list of missing integrations rather than missing features.

## Audience

Newcomers who have joined a brand, wholesaler, manufacturer or commerce vendor with a business-customer channel. The role that benefits most is the engineer or architect asked to "move wholesale onto the portal" and who must decide what the portal reads from the ERP; product managers choosing between a B2C platform's B2B features and a dedicated B2B platform benefit next.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone: B2B, company account, contract pricing, tiered pricing, quote, approval workflow, payment terms, credit limit, pre-season order, assortment, punchout, cXML, OCI, B2B2C, system of record, idempotent.
- [ ] The business problem comes first (the 38% of orders keyed by hand and why) and each object or flow is tied to a money or time consequence.
- [ ] The shared object model is shown with a sourced cross-platform table (Shopify, commercetools, SAP, Adobe, BigCommerce, OroCommerce) and a diagram; the ownership table names a system of record per fact with the reason; a requirements table covers price lookup, credit check, order creation, stock promise and invoice.
- [ ] Price layering and "which wins" is explained, with the quote as a frozen price sourced to commercetools and Adobe; VAT treatment is stated as practice and handed to [[tax-invoicing-and-ledger]].
- [ ] Kestrel & Pine's thread matches the ledger: 1,100 accounts, €12.0M, 9,400 orders, €1,277 average, 62% portal and 38% keyed, the ERP owning terms and credit, W2 as the target; the reasons behind the 38% and the De Kaap Buitensport example (credit limit €15,000, 5% pre-season terms, the February 2027 order) are added to the ledger as illustrative facts.
- [ ] EDI detail is kept to a link to [[edi-and-e-invoicing]]; punchout is one paragraph with the rule that a punchout cart is not an order.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage and ends with the judgement that the channel outgrows the platform when the facts the checkout needs stop living in the platform.
- [ ] The three take-away tiers are present and honest; Questions to Ask has at least eight entries; the article stays within 4,000–6,500 words.

## Non-goals

- EDI messages, transports, identifiers, chargebacks and e-invoicing mandates: [[edi-and-e-invoicing]].
- The ERP's role, the hub debate and batch versus event integration with ERPs: [[erp-and-back-office-integration]].
- Price computation, price lists and the pricing engine in general: [[pricing-architecture]]; this chapter covers only the B2B layering rule and the quote.
- VAT rules, invoice numbering and the ledger: [[tax-invoicing-and-ledger]].
- Wholesale fulfillment (cartons, pallets, SSCC labels): [[warehouse-and-fulfillment]].
- Customer identity matching across systems: [[identity-and-master-data]].
- The end-to-end wholesale order: [[journey-wholesale-order]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether Shopify offers a native quote object in late 2026 could not be confirmed; the chapter states that none was found and that draft orders are the documented mechanism.
- The date of Shopify's B2B plan expansion beyond Plus is not given on the help page; the chapter says "recent and undated".
- No European B2B e-commerce market figure meeting the sourcing standard was found; the chapter cites US figures with their differing definitions.
- The intra-EU VAT treatment of business supplies is stated as common practice without a linked official source (the Commission's VIES and cross-border VAT pages returned 404 in this session); chapter 14 should carry the citation.

## Decision log

- **2026-11-07** — Built the chapter around ownership (who holds the company, the price, the credit) rather than around a feature comparison, because every platform surveyed can hold all three and the reader's decision is which one should.
- **2026-11-07** — Used the 38% of hand-keyed orders as the organizing measure and invented ledger-consistent reasons for it (pre-season terms in the ERP, no credit check, two order records), so that the recommendation is a list of integrations the reader can check.
- **2026-11-07** — Added a second fictional wholesale account (De Kaap Buitensport) because Bergzicht is the EDI example owned by chapter 22 and the portal path needed its own worked order with a credit-limit hold.
- **2026-11-07** — Kept punchout to one paragraph and a row in the trade-off table rather than a section, since the contract says "briefly" and chapter 22 owns procurement integration.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the wholesale line, the portal, the 38%, the ERP's role, W2.
  - [[edi-and-e-invoicing]] — the document channel this chapter hands off to.
  - [[erp-and-back-office-integration]] — ERP ownership and the hub debate.
  - [[pricing-architecture]] — the pricing source the B2B layers sit on.
  - [[tax-invoicing-and-ledger]] — VAT and invoices.
  - `_research/brief-b2b-edi-erp.md` — the verified platform, market and procurement facts.
- **External**
  - Shopify Help Center and developer documentation (B2B, catalogs, payment terms), accessed 2026-11 — the native B2B model and plan constraints.
  - commercetools documentation (Business Units, Quotes, Approval Rules and Flows), accessed 2026-11 — the most explicit public object model for quoting and approval.
  - Adobe Commerce B2B guide (2026-10-01) and purchase-order flow — purchase orders and the frozen-price rule.
  - BigCommerce B2B Edition documentation, accessed 2026-11 — net terms, available credit, API deprecation.
  - SAP Spartacus B2B documentation — budgets, cost centers and approval (with an evidence-age note).
  - Microsoft Learn, Business Central Shopify connector (2026-10-14) — the system-of-record advice for customers, terms and credit.
  - OroCommerce and Sana Commerce pages — dedicated B2B and ERP-driven alternatives.
  - cXML User's Guide (2018) and TradeCentric (2026) — punchout.
  - Forrester (2022) and Digital Commerce 360 (2024, 2026) — market size with definitions.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, ERP publishes wholesale and contract prices as events and feeds no channel directly (item 3), credit-check figure corrected to the discounted order, acronyms expanded, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: dropped "recorded in the ledger" from illustrative labels. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
