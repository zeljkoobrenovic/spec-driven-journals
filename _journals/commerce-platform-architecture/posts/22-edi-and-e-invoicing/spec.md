---
status: accepted
revised: 2026-11-07
---

# Spec: Documents Between Companies: EDI, Punchout and E-Invoicing

> Working doc for chapter 22 of *ORDERED: Architecting Commerce Platforms*. Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Give a reader who has never seen an EDI message a working understanding of how companies trade by exchanging standard documents (order, despatch advice, invoice), why each document must be produced by a different internal system, and what the European e-invoicing mandates require by which date. The chapter's one durable claim: an EDI order is a channel into the same order record as a web order, the despatch advice must come from the warehouse's pack confirmation, and the invoice must come from the ERP's confirmed shipment, and every compliance chargeback in the public rule sets is a document generated from the wrong place. After reading, the reader can explain the ASN Chargeback at Kestrel & Pine, read a retailer's EDI purchasing conditions, and place their own company on the mandate calendar.

## Audience

Newcomers to commerce architecture. Benefits most: an integration engineer or product manager who inherits a wholesale channel and is asked why a retail chain deducted money, and a finance or engineering lead who hears "Peppol" for the first time. Also useful to an architect choosing between an EDI provider's portal, an integrated provider, in-house EDI and an e-document gateway.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (EDI, EDIFACT, EANCOM, X12, ORDERS, DESADV/ASN, INVOIC, CONTRL, GTIN, GLN, SSCC, AS2, VAN, Peppol, access point, four-corner model, mapping, chargeback, punchout, cXML, OCI, e-invoice, EN 16931, UBL, Peppol BIS Billing, clearance, iPaaS, OMS, idempotent).
- [ ] The "one honest source per document" rule is stated with a table (order record, order response, despatch advice, invoice) and tied to the ASN Chargeback.
- [ ] The mandate calendar carries official dates from primary sources for Belgium, Germany, France, Italy, Poland, the Netherlands and ViDA, each marked as of November 2026, and says which rows touch Kestrel & Pine.
- [ ] Bergzicht's spring reorder is worked with ledger numbers (6 April 2027, 240 units, 18 SKUs, €19,860, three pallets, delivery and INVOIC 9 April, due 9 May) and the W6 flow; the ASN Chargeback (€14,200, Q3 2026) is the scene.
- [ ] A requirements table (fresh, consistent, fast, available) and a trade-off table across the four choices are present; at least two mermaid diagrams (the document cycle as a sequence diagram, the Peppol four-corner model).
- [ ] The "Across Scale Stages" section with the four-stage table is present and specific per stage.
- [ ] The three take-away tiers are present and honest; Questions to Ask has 6–10 items; Sources are grouped with years.
- [ ] Article length between 4,000 and 6,500 words including tables.

## Non-goals

- B2B features (company accounts, contract pricing, quotes, approvals, punchout as a storefront feature): [[b2b-commerce]].
- The invoice as a legal document, VAT rules, credit notes and order-to-ledger posting: [[tax-invoicing-and-ledger]].
- What the ERP owns and the hub debate: [[erp-and-back-office-integration]].
- Idempotency, outbox, reconciliation jobs: [[events-consistency-and-reconciliation]].
- The regulatory calendar as a management practice and non-invoicing regulation: [[commerce-regulation]].
- The step-by-step wholesale order with the full failure path: [[journey-wholesale-order]].
- Warehouse pick and pack mechanics and SSCC label printing in the WMS: [[warehouse-and-fulfillment]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether Kestrel & Pine's Antwerp store makes it "established" in Belgium for the mandate is deliberately left to a tax adviser; the chapter states the ledger fact (Peppol invoices to Belgian business customers since January 2026) as a choice.
- Belgium's announced e-reporting phase (2028) and Poland's threshold reference year were not settled from primary pages and are omitted.
- The German issuing obligation from 1 January 2027 is stated as scheduled; if the transition periods are extended in 2027, the calendar needs an update.
- No official Walmart on-time-in-full policy page exists; the figures are trade press (2017) and a provider guide (2024).

## Decision log

- **2026-11-07** — Chose the ASN Chargeback as the scene and the "one honest source per document" rule as the spine, over a tour of EDI message segments, because the reader needs the ownership principle more than the syntax.
- **2026-11-07** — Put the mandate calendar in a single table with official dates and a "touches Kestrel & Pine" column, rather than a country-by-country narrative, so the Long Fuse pattern has a concrete artifact.
- **2026-11-07** — Kept punchout to one section (it belongs mostly to chapter 21) and framed it only as "another channel into the order record".
- **2026-11-07** — Rejected a separate "EDI providers compared" section; the provider market is covered by SPS Commerce's 10-K and Jumbo's two onboarding routes, which is enough for a newcomer.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the ASN Chargeback, Bergzicht, the EDI provider, Waypoint W6.
  - [[journey-wholesale-order]] — the full Bergzicht reorder path this chapter summarizes.
  - [[order-management]] — the OMS as the order hub that EDI orders enter from Q4 2027.
  - [[tax-invoicing-and-ledger]] — the invoice as a legal document.
  - [[commerce-regulation]] — the regulatory calendar.
- **External**
  - GS1 General Specifications Release 26.0 (2026); GS1 EANCOM manual (2021); GS1 EDI implementation survey (2021); X12 transaction sets; RFC 4130.
  - Jumbo purchasing conditions (2026-04-09), mechanized-DC guidelines (2025-10) and EDI supplier page; bol SSCC supplier page.
  - SPS Commerce Form 10-K for 2025; Talk Business (2017) and SPS Commerce (2024) on Walmart OTIF.
  - cXML User's Guide 1.2.037 (2018); TradeCentric on OCI (2026).
  - OpenPeppol About and BIS Billing 3.0 (3.0.21, 2026); European Commission "What is eInvoicing", "eInvoicing in Italy" and ViDA pages; einvoice.belgium.be (2024, 2025, FAQ); Bundesministerium der Finanzen FAQ; impots.gouv.fr; gov.pl KSeF; Rijksoverheid (2026-09-11); business.gov.nl.
  - Research brief `_research/brief-b2b-edi-erp.md` (Parts 1.5, 2, 3).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Belgian scope hedged per item 5, Bergzicht contract price no longer fixed at list, Belgian variant date left neutral pending item 12, acronyms expanded, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: named the Belgian Peppol example Ardennes Trail Co., Namur (40 Ridgewalker jackets, €3,800, ordered 21 April 2027, Peppol invoice 23 April, due 23 May; items 12 and 19), keeping the hedge on the Belgian mandate (items 5, 17). *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
