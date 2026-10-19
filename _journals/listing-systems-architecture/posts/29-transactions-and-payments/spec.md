---
status: accepted
revised: 2026-10-19
---

# Spec: Beyond the Contact: Payments, Shipping and Buyer Protection

## Intent

Explain when a classifieds marketplace should take part in the transaction, and what it then has to own. The chapter owns the terms *transactional pivot*, *marketplace payments* and *buyer protection*. It argues that the pivot is a per-category decision (items that ship, moderate prices, a fear of non-delivery, strangers on both sides), that a licensed payment provider's marketplace product should normally hold the money, and that the marketplace still owns six contexts: order, payment edge, fees, shipping, buyer protection and disputes, and the transaction ledger with tax reporting. It links to RECONCILED's payments chapters instead of re-teaching payments and reconciliation. After reading, an architect can judge a "let's go transactional" proposal, design the order state machine and its money boundaries, and name the regulatory switches it turns on.

## Audience

Chief architects, payments and marketplace engineering leads, and product and general managers of classifieds marketplaces considering or running in-platform payment, shipping and buyer protection.

## Success criteria

- [x] Defines the transactional pivot, marketplace payments, buyer protection, hold and release, payout, dispute versus chargeback and PUDO; links merchant of record and the payment lifecycle to [[payments-fundamentals]].
- [x] States when to take part in the transaction (four conditions) with dated public evidence: leboncoin, Kleinanzeigen, Marktplaats, OLX, Vinted, eBay, Adevinta's economics, Which?.
- [x] Compares payment models (provider marketplace product, specialist payment institution, own licence, off-platform) with documented provider behavior (Adyen, Stripe Connect, OPP, Vinted Pay) and the PSD2 commercial-agent point.
- [x] Architecture: six bounded contexts with events, a context diagram, an order state machine and design rules for availability, release, reconciliation, shipping, disputes and DAC7.
- [x] Veldmark worked examples with ledger numbers: the Rotterdam bike's pay-at-pickup order, a shipped Belgian order with a dispute, Safe Deal 2026 metrics, and the September 2027 forum decisions on Portugal, Motorvane and Hearthly Spain.
- [x] Trade-off table, vertical-differences table, failure modes, Chief Architect's view, questions to ask, Sources and Evidence.

## Non-goals

- The payment lifecycle, provider products in depth and ledger and reconciliation design ([[payments-fundamentals]], [[adyen]], [[stripe]], [[payments-to-ledger]], [[designing-financial-ledgers]]).
- Marketplace models and the endpoint ladder ([[marketplace-taxonomy]]); revenue models and KPIs ([[monetization-models]]).
- Contact-stage fraud and the message safety gate ([[fraud-prevention]], [[messaging-and-leads]]).
- DAC7 and DSA obligations in detail ([[marketplace-regulation]]); identity levels and payee verification ([[identity-and-verification]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Kleinanzeigen's provider: 2020–2023 sources name Online Payment Platform; its help page names Adyen in October 2026. When and why it changed is not public.
- Marktplaats' current Kopersbescherming terms and provider after 2022 are not verified; the chapter cites the 2022 description only.
- The exact reach of the PSD2 commercial-agent exclusion for marketplaces depends on contracts and jurisdiction; stated as a question for counsel.
- Several chapters written earlier (e.g. [[marketplace-regulation]]) cite the superseded 2026 Safe Deal volume of 4.1M orders and €310M GMV; the editor's ledger correction (11.6M orders, about €1.02B GMV) is used here.

## Decision log

- **2026-10-19** — Framed the pivot as a per-category decision with four conditions, rather than as a brand strategy, so it aligns with the marketplace profile register in [[marketplace-taxonomy]].
- **2026-10-19** — Organized the architecture as six bounded contexts beside the listing core, with the order owning availability and timers and the ledger receiving both order and money events.
- **2026-10-19** — Used three competing proposals (Portugal, Motorvane, Hearthly Spain) at one forum to show approve, narrow and decline outcomes; added Safe Deal 2026 operating metrics and the December 2026 clearing balance to the ledger.
- **2026-10-19** — Linked to RECONCILED for payments depth instead of re-teaching settlement and reconciliation.

## Sources

- **Internal**
  - [[meet-veldmark]], [[marketplace-taxonomy]], [[listing-aggregate]], [[event-driven-listings]], [[messaging-and-leads]], [[fraud-prevention]], [[identity-and-verification]], [[marketplace-regulation]], [[bounded-contexts]].
  - RECONCILED: [[payments-fundamentals]], [[adyen]], [[stripe]], [[payments-to-ledger]], [[designing-financial-ledgers]].
  - Research briefs: adevinta, olx, ebay-classifieds, monetization-economics, trust-safety-regulation, automotive.
- **External**
  - Adevinta annual reports 2019 and 2023, strategic report 2025, tech blog (2023); Kleinanzeigen Sicher bezahlen page; onlinemarketing.de (2020); t3n (2023); RetailTrends (2017); AVROTROS Radar (2022); Worldline (2022).
  - OLX Tech (2023); Prosus FY25; Vinted results, Vinted Pay and price list (2026); eBay 10-K (2026); Autotrader FY26; Car Dealer Magazine (2025); Which? (2024).
  - Adyen and Stripe Connect documentation; Directive (EU) 2015/2366 Art. 3; Belastingdienst DAC7 guidance.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Rotterdam bike order retimed to the canonical 14:02 reservation (offer 14:01), Kleinanzeigen carrier options and Vinted fee naming corrected from the live pages, PSD2 Art. 3(b) verified against the Official Journal. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
