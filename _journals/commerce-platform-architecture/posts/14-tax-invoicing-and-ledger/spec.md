---
status: accepted
revised: 2026-11-07
---

# Spec: Tax, Invoices and the Books: From Order to Ledger

## Intent

Show a reader new to commerce how an order becomes tax, an invoice and ledger entries, and what the commerce system owes finance. The chapter states the three outcomes (right tax, valid invoice, books that match the bank), gives an entity–owner table for the documents that carry them, explains VAT at the level a Dutch merchant selling in three countries needs (rates, inclusive versus exclusive prices, OSS, reverse charge, the US contrast), separates tax as a promise at checkout from tax as the legal amount on the invoice, treats the invoice as a numbered immutable document corrected only by a credit note, gives e-invoicing mandates at a glance, shows what the ERP posts and when revenue counts, and makes the monthly three-way match (invoices, PSP payouts, bank) the proof that the shop and the books agree. Eva's order in the books and a Belgian wholesale invoice over Peppol are the worked examples. After reading, the reader can say which system in their landscape may issue an invoice, which facts decide tax, and which two reports to build first.

## Audience

Readers new to commerce architecture. The engineer or integration lead who owns the ERP connector (Noor Visser and Ruben Alves at Kestrel & Pine) benefits most; the finance director who closes the month is the second reader and the chapter is written so Sanne de Wit would recognize her own problems. Terms explained on first use: VAT, tax-inclusive and tax-exclusive, One Stop Shop, reverse charge, VIES, sales tax and economic nexus, tax engine, invoice, credit note, sequential numbering, e-invoice, Peppol, EN 16931, ledger, revenue recognition, refund liability, breakage, payout, reconciliation, three-way match, sub-ledger, idempotency.

## Success criteria

- [x] The opener is one sentence under "IN THIS CHAPTER, YOU WILL", followed immediately by exactly three KEY POINTS, the business and architect callouts and three failure patterns (The Boomerang, Schrödinger's Order, The Long Fuse) with chapter-specific reasons.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The business problem (month-end with four feeds, the Double Refund, the Three-Status Order, the Peppol rejection) comes before any component, and every component is tied to a business consequence.
- [x] Contains: an outcomes table, a document entity–owner table, a VAT rates table, a requirements table for tax flows, a journal-entries table, a reconciliation mismatch table, a trade-off table across the three design decisions, the "Across Scale Stages: When It Fits and When It Limits" table with a judgement, three mermaid diagrams with captions (tax determination, documents to ledger, Eva's order to the ledger as a sequence), a "When It Goes Wrong" section with detection and recovery, "What to Take Away" in three tiers, Questions to Ask, and grouped Sources and Evidence.
- [x] Eva's order uses ledger facts (13 April 2027, €199 jacket, 2 × €18 socks, €235, iDEAL, #1072455, shipped 14 April, exchange received 22 April, refund variant €199 by iDEAL reversal booked as a credit note); the VAT split (€194.21 net, €40.79 VAT; jacket €164.46/€34.54; socks €29.75/€6.25) is arithmetic at the NL 21% rate; the PSP fee, payout delay, invoice number and Ardennes Trail Co.'s order (40 jackets at €95, €3,800, 21–23 April, due 23 May) are labeled illustrative or assumption and appended to the ledger. The Double Refund (212 returns, €19,400) and the Three-Status Order (#1052877, six days) match the ledger.
- [x] Every regulatory and company claim is dated and sourced (EC, business.gov.nl, UStG and AO texts, PwC for Belgium with the caveat, Your Europe, OSS page, Belastingdienst invoice and retention pages, Wayfair, IFRS 15, Peppol, einvoice.belgium.be 2024, BMF FAQ, Rijksoverheid 2026-09-11, ViDA; Stripe, Adyen, Mollie, Odoo, Microsoft and Shopify documentation accessed 2026-11); the Avalara document-type statement and the IFRS return-liability reading are labeled as inference or the author's reading.
- [x] Payment mechanics stay in [[commerce-payments]], e-invoicing formats and mandates in depth in [[edi-and-e-invoicing]], the ERP-as-hub debate in [[erp-and-back-office-integration]]; depth on ledgers and reconciliation is delegated to RECONCILED's [[payments-to-ledger]], [[designing-financial-ledgers]] and [[traceability-and-reconciliation]].
- [x] Length within the 6,500-word cap including tables; the three take-away tiers are present and honest.

## Non-goals

- Authorization, capture, settlement, refunds and chargebacks as payment operations — [[commerce-payments]].
- EN 16931, UBL, Peppol BIS, XRechnung, clearance models and the country-by-country mandate table — [[edi-and-e-invoicing]].
- The ERP's role as integration hub, connectors as products, master data — [[erp-and-back-office-integration]].
- Discount allocation and gift-card mechanics — [[commerce-promotions]]; return policies and the refund flow — [[returns-and-exchanges]].
- Metric definitions and why dashboards and the ledger differ — [[commerce-data-and-analytics]].
- The regulatory calendar as a tool — [[commerce-regulation]].
- Ledger design, sub-ledgers and reconciliation as disciplines — RECONCILED.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Belgian VAT rates rest on PwC's summary because the FPS Finance page served a captcha; a reviewer with access should confirm the 21/12/6/0 structure.
- Avalara's sales-order versus sales-invoice document semantics are stated as inference because the developer pages did not render; replace with a citation if one can be fetched.
- The chapter states that marketplaces may collect VAT as deemed supplier only as a warning sign; the rule's scope (non-EU sellers and imports under the 2021 package) belongs to [[marketplaces-and-channel-integration]] and should be checked there.
- Whether Kestrel & Pine's PSP fee and payout delay should become canonical ledger facts for [[commerce-payments]] is for that writer; this chapter records them as assumptions.

## Decision log

- **2026-11-07** — Organized the chapter around three outcomes (tax, invoice, books) and the documents that carry them rather than around systems, because the newcomer's question is "what does finance need" and the systems differ per merchant; the entity–owner table then maps documents to owners.
- **2026-11-07** — Put the tax-at-checkout versus tax-at-invoice distinction in its own section rather than inside VAT basics, because it is the join with [[cart-and-checkout]] and the cause of most "the invoice differs" tickets.
- **2026-11-07** — Kept e-invoicing to one section of dates and one ownership rule (the issuing system holds the transmission status), leaving formats and the mandate table to [[edi-and-e-invoicing]], to avoid re-teaching Part V.
- **2026-11-07** — Chose a Belgian wholesale customer (now Ardennes Trail Co., Namur, per consistency item 19; first drafted as an unnamed Ghent customer) rather than Bergzicht for the Peppol example, because Bergzicht is Dutch and invoices by EDI INVOIC; the Belgian case is the one the ledger says has used Peppol since January 2026.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Eva's order and exchange, the Double Refund, the Three-Status Order, business lines, Peppol since January 2026, Waypoint W2 and W5.
  - `_research/brief-checkout-payments-tax.md` — Part 2 (payouts and refunds), Part 4.4 (reconciliation reports), Part 7 (VAT, OSS, US sales tax, tax engines, inclusive pricing), Part 8 (invoice content, immutability, retention, revenue recognition, postings and month-end).
  - `_research/brief-b2b-edi-erp.md` — Part 3 (e-invoicing stack and mandates), Part 4 (what the ERP does, the Business Central connector, ERP-as-hub, batch versus event).
  - [[meet-kestrel-and-pine]], [[cart-and-checkout]], [[commerce-payments]], [[edi-and-e-invoicing]], [[erp-and-back-office-integration]] — neighbouring contracts and the recurring order.
- **External**
  - European Commission (VAT rates, OSS, ViDA), Your Europe, business.gov.nl, Belastingdienst (invoice requirements, retention), UStG §§ 12, 14, 14b and AO § 147, PwC Belgium — tax and invoice rules.
  - IFRS 15 (IFRS Foundation); RevenueHub on breakage — revenue recognition.
  - OpenPeppol, FPS Finance Belgium (2024), German BMF FAQ, Rijksoverheid (2026) — e-invoicing dates.
  - Stripe, Adyen and Mollie documentation (accessed 2026-11) — payout reports, batch references, refund behavior.
  - Odoo 18.0 documentation, Microsoft Learn (2026), Shopify (2026) — ERP invoice behavior and connector practice.
  - *South Dakota v. Wayfair* (2018), Avalara and TaxJar pages — US sales tax and tax engines.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: invoice per shipment ruled (issues item 18); Belgian Peppol customer unified as Ardennes Trail Co. (item 19); #1052877 Not-invoiced mechanism aligned to items 2/14; revenue at delivery with month-end cut-off (item 1); Belgian mandate scope hedged; trimmed from 7,033 to 6,485 words. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: "consistent with ledger prices" now reads as Kestrel & Pine's wholesale price. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
