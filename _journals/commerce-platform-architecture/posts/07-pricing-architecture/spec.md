---
status: accepted
revised: 2026-11-07
---

# Spec: What Does It Cost? Price Lists, Contract Prices, Currencies and Tax

## Intent

Teach a reader new to commerce architecture that a price is selected by a rule from many candidates (market, currency, customer group, channel, quantity, validity, tax basis), that the engine that selects must be distinguished from the copies that show the result, and that in Europe the price history is a legal record. The spine is Kestrel & Pine's Price Drift of October 2026 (the German storefront at €179 for nine days, 410 orders, about €8,200 of margin, a marketplace parity warning), reconstructed as a silent campaign-restore failure, and the April 2027 decision that splits price ownership by kind: the platform for consumer prices and the campaign calendar, the ERP for wholesale and contract prices, every other system a consumer fed by effective-dated price events and reconciled daily. The EU price rules carry their official dates (Directive 98/6/EC of 16 February 1998; Directive 2019/2161 of 27 November 2019, applied from 28 May 2022; ACM supervision from 1 January 2023 and fines published 11 June 2024; the 2013, 2022 and 2026 marketplace decisions) so that the Long Fuse cannot be pleaded. After reading, the reader can inventory the prices in a landscape, name a source per kind, fix the moment of selection, and ask whether the system can answer the 30-day question.

## Audience

Newcomers: engineers, product managers, analysts and consultants at a merchant, a vendor or an agency. The engineer or product manager who owns the storefront, the marketplace connector or the ERP integration benefits most, because the chapter gives them the per-flow requirements table and the price-event contract. The finance or merchandising leader benefits from the tax-basis discussion and the Black Friday reference-price example.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone (price list, base, customer-specific, contract and tiered price, quote, selection rule, moment of selection, tax-inclusive and tax-exclusive, OSS, price parity, price control mechanism, Buy Box, repricer, price event); every acronym is expanded on first use.
- [x] The business problem (the Price Drift, the fake-discount fines) comes first; every component is tied to a business consequence.
- [x] The price dimensions appear in a table; the selection rule is illustrated with a diagram and sourced from commercetools, Adobe Commerce and SAP Commerce documentation; the moment-of-selection rule is stated with the SAP cart-creation-date case.
- [x] The EU rules are cited with official dates and the architectural reading (effective-dated history, 30-day reference, reference price as a syndicated field, channel rules as configuration).
- [x] Four arrangements (platform, ERP, pricing service, split by kind with events) are compared in a trade-off table; the recommendation names its three assumptions.
- [x] The "Across Scale Stages: When It Fits and When It Limits" section has the four-stage table and a judgement.
- [x] Kestrel & Pine numbers match the ledger (€199, €95, €58, 21% and 19% VAT nets, the Price Drift figures, order #1072455 on 13 April 2027 at 21:14, Bergzicht as largest wholesale customer); the Price Drift reconstruction, the eleven-prices inventory, the 2027 ownership decision and the Black Friday reference example are labeled illustrative or as this chapter's reconstruction.
- [x] The three take-away tiers are present and honest; eight questions to ask; a hand-off to [[commerce-promotions]]; two mermaid diagrams with captions; article under 6,500 words including tables.

## Non-goals

- Discounts, coupons, stacking rules, gift cards and discount allocation: [[commerce-promotions]].
- VAT rates, the OSS mechanics, reverse charge, tax engines and the invoice as a legal document: [[tax-invoicing-and-ledger]].
- Company accounts, quotes, approvals and credit limits as B2B objects: [[b2b-commerce]].
- Marketplace listing operations, fee schedules and Buy Box management as a channel practice: [[marketplaces-and-channel-integration]].
- EDI ORDERS and INVOIC document handling and price mismatches as chargebacks: [[edi-and-e-invoicing]].
- The event, idempotency and reconciliation mechanics that the price event relies on: [[events-consistency-and-reconciliation]].
- Consumer-law requirements beyond price indication and the regulatory calendar: [[commerce-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger gives no per-unit contract price for Bergzicht Outdoor, and the spring reorder's €19,860 for 240 units does not divide into list prices; the chapter states only that Bergzicht buys on a seasonal contract price list. [[journey-wholesale-order]] should set the per-SKU contract prices and append them to the ledger.
- The German VAT rate (19%) is stated from general knowledge as of November 2026, not from a fetched official page; a reviewer may wish to add a citation to the Commission's VAT rates page.
- The Bundeskartellamt's 5 February 2026 prohibition is under appeal; if it is overturned or confirmed, the sentence that says "not final" must change.
- Whether the platform keeps a queryable price history or only exports change events is left as an assumption; the chapter says both are acceptable if something keeps the history.
- [[erp-and-back-office-integration]]'s ledger line says the ERP "feeds no channel" under the finance-only rule, while this chapter has the ERP's wholesale and contract price lists reach the platform's B2B catalogs by price events (and [[b2b-commerce]] keeps pre-season terms in the ERP's customer price lists). The chapter treats contract prices as business-customer terms, which that rule lists as ERP-owned; a reviewer should confirm the two chapters agree on the direction of the wholesale price flow.

## Decision log

- **2026-11-07** — Chose "split by kind of price, with events" over a single pricing service as the recommendation, because the ledger's W4 keeps Kestrel & Pine on its SaaS platform and W5 moves prices by events, and because a pricing service for three euro markets would be the Giant's Boots; the pricing service remains the stated fallback when the three assumptions fail.
- **2026-11-07** — Reconstructed the Price Drift as a failed hourly push of the ERP's DE consumer price list by the partner-built ERP connector (changes only, not idempotent), because the ledger's "price-list sync had failed silently" needs a concrete mechanism a newcomer can picture, because [[erp-and-back-office-integration]]'s ledger line records that this connector "carried the DE price list", and because a lost change message is the generic Message in a Bottle for prices; the reconstruction is labeled as such.
- **2026-11-07** — Kept the Bergzicht contract price unspecified rather than inventing per-SKU prices that would have to reconcile with the spring reorder's total.
- **2026-11-07** — Used a hypothetical autumn 2027 campaign to work the 30-day rule rather than the 2026 Price Drift, because the drift was an error, not an announced reduction, and the rule applies to announced reductions.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Price Drift, the prices, the channels and the Waypoint standards.
  - [[product-information]] — the SKU the price attaches to; the content-versus-price cadence split.
  - `_research/brief-catalog-pricing-search.md` Part 2 — price lists and selection, tax-inclusive display, the Omnibus rule, marketplace price parity and control.
  - `_research/brief-b2b-edi-erp.md` — contract pricing, quotes as frozen prices, the ERP's ownership of wholesale price lists.
  - `_research/brief-marketplaces-channels-pos.md` section 2.4 — repricing, `PRICING_HEALTH`, the channel price as a derived price with a floor.
  - `_research/brief-checkout-payments-tax.md` section 7 — OSS from 1 July 2021 and the €10,000 threshold.
- **External**
  - Directive 98/6/EC (1998) and Directive (EU) 2019/2161 (2019) — the tax-inclusive selling price and the 30-day prior price, with dates of application.
  - § 11 PAngV (2022); ACM publications of 2022-12-06 and 2024-06-11 — national transposition and enforcement.
  - Bundeskartellamt (2013; case overview 2026) and European Commission IP/22/7777 (2022) — the marketplace price-parity and price-control decisions.
  - Shopify, commercetools, Adobe Commerce and SAP Commerce documentation (2018–2026) — price lists, selection rules, tier precedence, rounding and tax-inclusive display.
  - Amazon SP-API notification documentation and ChannelEngine (accessed 2026-11) — price-state signals and repricing with guardrails.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: applied consistency ruling 3 (ERP feeds no channel directly; wholesale and contract prices by event to B2B catalogs and the OMS), corrected the derived DE gross price and the Omnibus fine wording, hedged the 2026 Bundeskartellamt decision, expanded acronyms, trimmed from 7,006 to 6,496 words (marketplace-law, currency, tax and platform-evidence paragraphs tightened), timetoread 28. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
