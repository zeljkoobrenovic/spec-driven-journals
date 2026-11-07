---
status: accepted
revised: 2026-11-07
---

# Spec: Stores Are Systems Too: Point of Sale and Omnichannel Fulfillment

> Working doc for chapter 17 of *ORDERED: Architecting Commerce Platforms* (Part IV — FULFILLMENT). Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Readers new to commerce architecture usually see a store as a building with a till in it, not as a second commerce system with its own vendor, data model, offline behavior and tax rules. This chapter makes the store visible as a stock location, an order source and an identity source, explains how click-and-collect, ship-from-store, return-in-store and endless aisle actually work as promises against store stock, and gives the reader a way to decide between the platform's own POS and a specialist POS integrated through an order hub. After reading it, the reader can look at a click-and-collect pilot and say where the promise is made, where the commitment is made, and why the two must be different moments.

## Audience

Newcomers to commerce architecture. The roles that benefit most: a product manager or engineer asked to "add click-and-collect" to a web platform, a head of operations who owns stores and is being sold "unified commerce", and an architect weighing a POS replacement. Readers should leave able to define POS, terminal, fiscalization, store stock as a location, the four omnichannel services and unified commerce, and to name the three design options for an honest store-stock promise (threshold, confirmation, count).

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (POS, terminal, fiscal receipt, TSE, GKS, P2PE, system of record, availability service, OMS, fulfillment order, sourcing, click-and-collect, ship-from-store, return-in-store, endless aisle, unified commerce, idempotent, RFID), with every acronym expanded on first use.
- [ ] The business problem (the Store Stock Mirage: 37 broken promises at Utrecht in December 2026) comes before any component, and every component is tied to a business consequence.
- [ ] The two constraints that make a POS a different product (offline operation and fiscalization) are explained with dated vendor and regulatory sources, and the fiscal table is correct for DE, BE, IT and NL as of November 2026, including that Belgium's certified register applies to hospitality only.
- [ ] The four omnichannel services are presented as the same three problems (availability, sourcing, staff tooling) with a requirements table, and click-and-collect separates the promise (buffered availability) from the commitment (staff confirmation).
- [ ] Four POS integration choices are compared in a trade-off table, and the recommendation is tied to the number of fiscal regimes and the weight of the stores; Waypoint W4's deferral to 2028 is explained, not changed.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage and ends with a judgement.
- [ ] At least two mermaid diagrams, a Kestrel & Pine worked example with ledger numbers (six stores, 1,800 variants, 118,000 transactions, €6.0M, 37 items, W1/W2/W4), a "When it goes wrong" section, the three take-away tiers, 6–10 questions, and grouped Sources and Evidence are present.
- [ ] No vendor is presented as the answer; every vendor definition of unified commerce is attributed.

## Non-goals

- The availability calculation, buffers per channel and the oversell mechanics in general: [[inventory-and-availability]].
- The order state machine and the OMS as a product category: [[order-management]].
- Return policies, dispositions and refund reconciliation: [[returns-and-exchanges]]; only return-in-store's refund-path risk is covered here.
- Customer matching and the golden record: [[identity-and-master-data]]; this chapter only names the join keys a store can offer.
- Terminal payments, settlement and payout reconciliation: [[commerce-payments]]; PCI scope in depth: [[commerce-security]].
- The regulatory calendar as a practice: [[commerce-regulation]].
- Marketplace programs that use store stock as a channel business: [[marketplaces-and-channel-integration]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No open, dated European adoption figure for click-and-collect or ship-from-store after 2020 was found; the chapter uses 2016 and 2018 surveys as order-of-magnitude history. Replace if a primary 2024–2026 source appears.
- No analyst (Gartner/Forrester) definition of unified commerce could be fetched; the chapter attributes every definition to a vendor. Add an analyst definition if one becomes available.
- The ledger says "Belgian fiscal receipt rules apply" to Antwerp; the chapter reads this as general VAT receipt and record-keeping rules, since the certified register applies to hospitality only. Confirm that reading with the ledger owner if a later chapter needs Antwerp's receipt rules in detail.

## Decision log

- **2026-11-07** — Chose the Store Stock Mirage and the deferred POS decision (W4) as the spine rather than a feature tour of POS products, because the chapter's job is to show how a store joins the architecture, and the deferral is the clearest example of "fix the joins before the till".
- **2026-11-07** — Framed the four omnichannel services as three shared problems (availability, sourcing, staff tooling) rather than four separate how-tos, so that a newcomer sees one design rather than four features.
- **2026-11-07** — Included a country fiscalization table even though Kestrel & Pine has no German store, because fiscal rules are the strongest reason the platform's POS is sometimes not an option, and a German store is the realistic next step for the fictional merchant.
- **2026-11-07** — Kept the Three-Status Order and the Double Refund as cross-references only; their full treatment belongs to chapters 13, 18 and 19.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the store facts, the Store Stock Mirage, the Waypoint decisions W1, W2 and W4.
  - [[inventory-and-availability]] — the availability service and buffer vocabulary the chapter relies on.
  - [[order-management]] — the OMS, sourcing and the fulfillment order.
  - [[identity-and-master-data]] — the Familiar Stranger and store customer matching.
  - [[returns-and-exchanges]] and [[commerce-payments]] — the refund path and terminal settlement.
  - `_research/brief-marketplaces-channels-pos.md` (Parts 4 and 5) and `_research/brief-inventory-fulfillment-returns.md` (Parts 1–3) — the verified vendor, regulatory and research facts.
- **External**
  - Shopify, Square, Lightspeed, Vendit, Adyen product and help pages (accessed 2026-11) — POS features, offline rules, unified-commerce definitions.
  - § 146a AO and KassenSichV (Germany), FPS Finance GKS pages (Belgium), Agenzia delle Entrate 2019 release (Italy), Belastingdienst brochure (Netherlands) — fiscalization.
  - DeHoratius and Raman 2008; Auburn RFID Lab 2018 via Retail Dive — store inventory accuracy.
  - UPS 2016 and Savills 2018 surveys — adoption history.
  - TextilWirtschaft 2026 and FashionUnited 2021 — Zalando Connected Retail.
  - Adobe Commerce, Shopify and Kibo documentation (2026) — routing to stores and the fulfillment order.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, SaaS/RFID/PCI DSS/ELSTER defined at first use, KassenSichV amendment date verified, source headings normalized. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document references rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
