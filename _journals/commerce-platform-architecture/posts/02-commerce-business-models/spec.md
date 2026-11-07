---
status: accepted
revised: 2026-11-07
---

# Spec: Who Sells What to Whom: Business Models and the Economics That Shape Architecture

## Intent

Explain to a reader new to commerce why a brand selling to consumers, a wholesaler, a retailer with stores, a marketplace seller and a marketplace operator need different systems, and give them the two tools the rest of the book assumes: the unit economics of an order (conversion, basket, margin, returns, shipping, payment fees, acquisition cost, the peak) with what each number pulls on in the architecture, and the four scale stages (Starting, Growing, Omnichannel, Group) defined by the shape of the business rather than its revenue. The chapter owns **business model** (defined for architecture as "who makes which promise"), **scale stage** and **unit economics of an order**. After reading, the reader can fill in a who-makes-which-promise table for their own company's lines, read a vendor's price tiers as a map of expected decisions, and say which of the three arrangements (one stack, a stack per line, a shared core with line-specific edges) their merchant is in and should be in.

## Audience

Readers new to commerce architecture, with the product manager, analyst or consultant who has to turn a business plan into system requirements benefiting most, and the engineer who has only ever seen one business line close behind. Leaders deciding whether business lines or brands should share a stack get the trade-off table and the conditions. No commerce or finance vocabulary is assumed; seller of record, GMV, EDI-type sales, interchange, AOV and the model names are each explained once.

## Success criteria

- [x] Every business model (B2C, D2C, wholesale, B2B e-commerce, B2B2C, marketplace selling, marketplace operating, omnichannel, subscription) is defined in a table using a dated company or statistical source, and "seller of record", "GMV" and "EDI-type sales" are explained in plain words.
- [x] A promise-chain table says, per model, who captures the order, sets the price, is seller of record, holds stock, ships, handles returns and invoices, with the architectural consequence.
- [x] A unit-economics table gives each metric a plain definition, a dated public benchmark, Kestrel & Pine's ledger figure (or "not in the ledger") and the part of the platform it pulls on; every non-ledger, non-documented number is labeled *(assumption)*.
- [x] A worked example takes the Ridgewalker jacket (€199 consumer incl. 21% VAT, €95 wholesale excl. VAT, €58 landed cost) through the D2C, wholesale and marketplace lines to an illustrative contribution per unit, with assumptions labeled and the arithmetic correct.
- [x] The four scale stages are defined by shape, in a table with typical size, shape, models run, what becomes necessary and warning signs, matching the ledger's bands and Kestrel & Pine's 2016–2018 / 2019–2022 / 2023– path; vendor tiers (Shopify, Shopware) are cited as confirmation, dated n.d., accessed 2026-11.
- [x] Three arrangements (one stack, a stack per line, shared core with line-specific edges) are compared in a trade-off table with a conditional recommendation, tied to Waypoint's shape.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use; two mermaid diagrams with captions.
- [x] The three take-away tiers are present; 6–10 questions to ask; closes with a hand-off to [[commerce-capability-map]]; the article is at or under 6,500 words including tables.

## Non-goals

- The capability map and the suite vs best-of-breed question — [[commerce-capability-map]]; the system-of-record decision per fact — [[boundaries-and-systems-of-record]]; the platform vendors and their pricing models in depth — [[commerce-platform-landscape]].
- The mechanics of each model's systems: B2B accounts, contract prices and approvals — [[b2b-commerce]]; EDI — [[edi-and-e-invoicing]]; marketplace listings, orders and fees — [[marketplaces-and-channel-integration]]; POS and omnichannel fulfillment — [[stores-and-omnichannel]]; promotions and loyalty — [[commerce-promotions]].
- The scale-stage transitions as decisions (what to change when) — [[commerce-scaling-stages]]; build, buy or assemble and replatforming — [[build-buy-or-assemble]], [[replatforming-and-migration]]; peak engineering — [[peak-load-and-reliability]].
- Marketplace operating as a business (liquidity, ranking, regulation) — LISTED; the Amazon and Zalando cases — [[case-amazon]], [[case-zalando]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The worked example's per-order costs (parcel €5.50, cross-border parcel €7.50, return handling €7.50, marketing 12% and 5%, pallet share €0.60, iDEAL about €0.30) are labeled assumptions and are not in the ledger; if another chapter needs them canonically it should append them, and this chapter should then cite the ledger.
- Amazon's 15% referral fee is taken from its US pricing page; the German fee schedule was not verified. The chapter labels the marketplace line's fee as an assumption of the same order; [[marketplaces-and-channel-integration]] should replace it with a verified Amazon.de figure if one is found.
- No primary benchmark exists for retail technology spend as a share of revenue or for team size per stage; the chapter avoids both. The ledger's 5.4% is not presented as a benchmark.

## Decision log

- **2026-11-07** — Defined the models from annual reports and Eurostat rather than from vendor marketing, because the reader needs definitions that can be counted and checked; B2B2C is defined operationally from Zalando's partner-business description since no statistical definition exists.
- **2026-11-07** — Chose "who makes which promise" as the chapter's definition of a business model, so that the chapter builds directly on [[journey-of-an-order]] and feeds [[boundaries-and-systems-of-record]] rather than standing as a business-school detour.
- **2026-11-07** — Worked one jacket through three lines rather than giving a whole-company P&L, because contribution per unit is what makes the four heads of business lines' different requests legible to a newcomer; store economics are mentioned, not tabulated, to hold the length cap.
- **2026-11-07** — Folded the "Across Scale Stages" requirement (optional in Part I) into the section that defines the stages, with the required columns (typical, becomes necessary, warning signs), instead of adding a second stage table.
- **2026-11-07** — Cut the European market-size paragraph to two national series after the first draft exceeded the cap; the three series measure different things and the chapter's argument needs only "growth has normalized".

## Sources

- **Internal**
  - [[journey-of-an-order]] — the promises and handoffs the models are defined against.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the four business lines, prices, margins, return rates, peak figures, the Price Drift, the ASN Chargeback, the Store Stock Mirage, the Double Refund, the scale-stage bands.
  - `PLAN.md` contract 2 — scope, owned terms, neighbours.
  - `_research/brief-commerce-business-models.md` — definitions, market statistics, unit economics, seasonality, vendor tiers, PIM/OMS/WMS triggers.
  - `_research/brief-checkout-payments-tax.md` — VAT rates for the worked example.
- **External**
  - VF, Nike, Columbia, Target, Amazon, Shopify, Warby Parker annual reports (SEC, 2026); Zalando SE Annual Report 2025 — model definitions, margins, channel shares, GMV definition.
  - Eurostat, *E-commerce statistics (enterprises)*; US Census Bureau, *Quarterly Retail E-Commerce Sales*; HDE Online-Monitor; Thuiswinkel Markt Monitor; bevh — market shares and seasonality.
  - Littledata, Baymard Institute, NRF and Happy Returns, Coresight — conversion, abandonment, returns.
  - Regulation (EU) 2015/751; Stripe, Mollie, Adyen, Shopify Payments and Amazon pricing pages — payment and channel fees.
  - Shopify and Shopware pricing pages; Akeneo and an OMS vendor guide — tiers and hub triggers.
  - Adobe Analytics and Shopify BFCM releases; Retail Week on Hobbycraft — the peak.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: corrected Shopify's Basic price (€28, €21 paid yearly), moved Germany (2022) into the Growing stage, defined punchout, parity rules, repricing, tenancy and ASN, fixed the wholesale-contribution comparison and the Double Refund attribution. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: "Not in the ledger" cells and note rephrased so the reader is not pointed to the scenario ledger. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
