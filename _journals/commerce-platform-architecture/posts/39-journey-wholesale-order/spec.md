---
status: accepted
revised: 2026-11-07
---

# Spec: Journey 3: A Chain Reorders by EDI, From Order to Invoice

## Intent

Show the reader what changes when the buyer is a company that orders by message, receives by pallet and pays thirty days later. The chapter walks Bergzicht Outdoor's spring reorder (240 units, 6 April 2027) through Kestrel & Pine's late-2027 target architecture, from the EDI order message to the matched bank transfer, as one step table and one sequence diagram, and makes one argument: each wholesale document has its own system of truth (the order record in the OMS, the despatch advice in the WMS's pack confirmation, the invoice in the ERP), and the ASN Chargeback of Q3 2026 happened because the despatch advice was written by the wrong system. The Belgian customer's Peppol invoice runs as the variant, so the reader sees that e-invoicing mandates change the invoice's format and transport, not its owner. A short section shows the same order on the January 2027 landscape.

## Audience

Readers new to commerce architecture, and in particular anyone who meets EDI for the first time as a wall of capital letters: the integration engineer handed a trading-partner guideline, the product manager asked why a deduction appeared, the finance analyst matching a short payment. The chapter explains every message (ORDERS, CONTRL, ORDRSP, DESADV, INVOIC, RECADV), every identifier (GTIN, GLN, SSCC), the Peppol stack (access point, four-corner model, EN 16931, UBL, BIS Billing 3.0) and the B2B money terms (payment terms, receivable, cash application, dunning, credit limit, four-way match, reverse charge) in one clause each.

## Success criteria

- [x] Every ledger fact of Bergzicht's reorder (date, units, SKU count, value, pallets, DESADV at pack confirmation, delivery and INVOIC on 9 April, payment due 9 May) and of the ASN Chargeback (€14,200, Q3 2026, SSCC labels not matching the DESADV) is stated exactly; PO numbers, GLNs, pack times and the credit limit are labeled illustrative.
- [x] The chapter says it is set in the late-2027 target architecture with W1, W2, W3 and W6 in force, and shows the January 2027 path in a comparison table.
- [x] A step table with step, system, data, promise made, what could fail here and chapter, from ORDERS received to cash application.
- [x] At least one sequence diagram plus further mermaid diagrams with captions; one diagram contrasts the January and late-2027 source of the DESADV.
- [x] A requirements table for the handoffs; the ASN Chargeback walked as mechanism, detection, recovery and residual failures; the Peppol invoice variant with a dated account of the Belgian mandate and an EDI-INVOIC-versus-Peppol table.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] Every retailer, standards-body, provider and regulatory claim carries a source and a date; Bergzicht's conditions are stated as fictional and shaped on public ones (Jumbo, bol, Walmart).
- [x] The three take-away tiers are present; 6–10 questions to ask; a hand-off to [[journey-peak-day]].
- [x] Body at or under 6,500 words including tables.

## Non-goals

- Teaching B2B commerce features (company accounts, contract pricing, quotes, approvals, credit limits) in depth: [[b2b-commerce]].
- EDI standards, transports, providers, mapping and the e-invoicing calendar in depth: [[edi-and-e-invoicing]]; the regulatory calendar: [[commerce-regulation]].
- The ERP's role and the hub debate: [[erp-and-back-office-integration]]; invoicing, credit notes and the ledger: [[tax-invoicing-and-ledger]].
- Warehouse operations beyond the pallet, SSCC and DESADV steps: [[warehouse-and-fulfillment]].
- Punchout and procurement integration, and the marketplace variant of a wholesale-like order.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Kestrel & Pine's own position under the Belgian e-invoicing mandate: the ledger says it sends Peppol invoices to Belgian business customers since January 2026 and operates an Antwerp store; whether its Belgian establishment brings any of its invoices into the obligation's scope is not decided by the chapter and should be checked by a reviewer with the official FAQ.
- The ledger's €19,860 for 240 units does not resolve to list wholesale prices (€95 and €57), so the chapter states that Bergzicht buys at contract prices without giving a per-line split; chapters 07 and 21 should keep the same reading.
- The EDI cut-over date (EDI and manual wholesale orders through the OMS from 8 December 2027) comes from the [[replatforming-and-migration]] ledger addition; the chapter's "late 2027" wording depends on it.

## Decision log

- **2026-11-07** — Made the despatch advice, not the order, the chapter's centre of gravity, because the ledger's failure path and the public retailer rules (Jumbo, bol) both turn on it; the alternative, a symmetric walk giving each document equal weight, would have buried the one lesson wholesale teaches that the consumer journey cannot.
- **2026-11-07** — Walked the ASN Chargeback on the January landscape as it happened and then listed what W6 changes and what can still go wrong, rather than describing only the fixed state, so the reader sees a failure's mechanism and not only its remedy.
- **2026-11-07** — Invented one small Belgian customer (Ardennes Trail Co.) for the Peppol variant rather than making Bergzicht Belgian, because the ledger fixes Bergzicht as Dutch and the variant needs an intra-EU supply at 0% with reverse charge to show what differs.
- **2026-11-07** — Kept the money leg (terms, receivable, cash application, dunning) inside this chapter rather than deferring it wholly to chapter 14, because a newcomer's model of "payment" is a PSP event and the wholesale journey is the place that model breaks.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Bergzicht, the reorder, the ASN Chargeback, W6, and the additions by chapter (OMS cut-over dates).
  - `PLAN.md` — the Part IX contract for chapter 39 and the neighbouring contracts for chapters 21, 22, 23 and 14.
  - `_research/style-guide.md` — page format, callouts, evidence discipline, valid permalinks.
  - `_research/brief-b2b-edi-erp.md`, `_research/brief-checkout-payments-tax.md`, `_research/brief-integration-and-data.md` — the verified EDI, e-invoicing, ERP, invoicing and idempotency facts cited.
  - [[meet-kestrel-and-pine]], [[journey-consumer-order]] — the landscape and the shared steps said once there.
- **External**
  - GS1 General Specifications 26.0 (2026), GS1 EANCOM manual (2021), GS1 EDI survey (2021), X12 transaction sets, RFC 4130 — the standards and identifiers.
  - Jumbo DC guidelines (2025) and purchasing conditions (2026), bol SSCC page, Walmart OTIF reporting (2017, 2024), SPS Commerce 10-K (2026) — buyer rules, penalties and the provider model.
  - OpenPeppol (BIS Billing 3.0.21, 2026), FPS Finance Belgium (2024–2025), German BMF FAQ, Dutch government announcement (2026-09-11), European Commission ViDA and cross-border VAT pages — the e-invoicing facts.
  - Microsoft Learn (2026-10-14), Shopify Admin API 2026-10, Manhattan, OneStock (2026), Stripe, Odoo 18.0, IFRS 15, Regulation (EU) 2024/886 — ownership of terms, platform modeling of terms, warehouse order streaming, the hub argument, idempotency, invoice immutability, revenue recognition and instant transfers.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Peppol variant aligned with chapter 14 (Ardennes Trail Co., 40 Ridgewalker jackets, €3,800, 21–23 April; consistency item 19). *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: ASN Chargeback mechanism aligned with chapter 22, Belgian mandate hedged (items 5/17), American spelling. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
