---
status: accepted
revised: 2026-10-20
---

# Spec: How Listing Marketplaces Make Money

## Intent

Give architects a working model of how listing marketplaces earn revenue, and why that is an architecture question. The chapter catalogs ten monetization models: insertion fees, VAS, pro subscriptions with quotas, depth tiers, lead-based fees, transactional fees, advertising, data and SaaS, financing and insurance referrals, and consumer subscriptions. Each model comes with dated public evidence and published KPIs. The chapter then shows which systems each model requires and which liquidity it spends. After reading it, the reader should treat the *unit of charge* as the decision that selects the system of record. They should judge any proposal for a new revenue stream by its systems, its evidence of delivery and its liquidity guardrail, not by its business case alone.

## Audience

Chief architects, principal engineers and engineering directors at marketplace groups who are asked to "add a revenue stream" or to support a price-and-product event. Also product and monetization leaders who need to see what their models cost in systems. Readers know distributed systems. They may not know portal KPIs (ARPA, ARPR, yield, take rate) or how lead-based and outcome-based fees work.

## Success criteria

- [ ] Reader can name the ten models and, for each one, who pays, the unit of charge and the systems it requires.
- [ ] Reader can explain why a portal's published KPI denominator (ARPA, ARPR, yield per listing, revenue per visit, take rate) reveals its model, using dated sources.
- [ ] Reader can state what each model spends in liquidity and propose a guardrail metric for it.
- [ ] Reader understands the limits of pricing power, using Autotrader's FY26 forecourt decline and Deal Builder concerns and Hemnet's 2026 free entry-level formats, without unverified causes.
- [ ] Reader can explain why paid-product ROI needs causal measurement (OLX 2026 case).
- [ ] The Veldmark worked example uses ledger revenue figures, derives unit KPIs, and evaluates three proposals with explicit decisions. The proposals use the Essen Golf and Lyon apartment examples.
- [ ] Contains a trade-off table, a vertical-differences table, three mermaid diagrams, a Chief Architect's view, questions to ask and a Sources and Evidence section.
- [ ] No company's internal monetization architecture is presented as fact; the reference architecture is labeled as inference.

## Non-goals

- Designing the catalog, pricing engine, entitlements, quotas and billing: [[products-and-entitlements]].
- The ad stack, header bidding, consent and retail media: [[advertising-platforms]].
- Payments, shipping, buyer protection and the transactional pivot: [[transactions-and-payments]].
- Lead objects, conversations and lead routing: [[messaging-and-leads]].
- Paid-organic blending inside ranking: [[ranking]].
- Regulatory detail on paid-ranking disclosure: [[marketplace-regulation]].
- Network effects and liquidity metrics in depth: [[liquidity-and-network-effects]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- *(Resolved 2026-10-19.)* The editor corrected Safe Deal 2026 to 11.6M transactions and about €1.02B GMV, so the €75M of fees (buyer fees about €59M plus shipping-label margin about €16M) reconciles; the chapter now states the derived take rate of about 7.4%.
- The cause of Hemnet's 2026 volume decline is not verified; the chapter states only the published figures.
- No primary source was verified for pay-per-call products at major portals; the model is mentioned only within lead-based fees.

## Decision log

- **2026-10-19** — Organized the chapter around the unit of charge rather than around companies, because the unit maps directly to the system of record. Rejected a company-by-company tour, which belongs in Part IX.
- **2026-10-19** — Framed every model as "spending liquidity", with a guardrail table. This makes the monetization-versus-liquidity tension operational rather than rhetorical.
- **2026-10-19** — Used three proposals at an architecture advice forum as the worked example, instead of a single revenue-mix table, so that the chapter ends in decisions (defer, design without billing, regional pilot).
- **2026-10-19** — Kept advertising and transactions as short model sections that link out, to avoid re-teaching chapters 29 and 32.

## Sources

- **Internal**
  - [[meet-veldmark]] and the scenario ledger — revenue mix by brand, volumes, cast, Keybridge decision.
  - [[listing-aggregate]], [[ranking]], [[experimentation]], [[products-and-entitlements]] — boundaries this chapter links to.
- **External**
  - Rightmove FY2025 RNS (2026); Autotrader FY26 results (2026); CarGurus, Zillow and eBay 10-Ks for FY2025 (2026); REA FY26 (2026); Scout24 preliminary FY2025 (2026); Hemnet investor page (accessed 2026-10-19); Adevinta Annual Report 2023 (2024); Vinted price lists (2026) — KPIs and product mechanics.
  - OLX Tech posts on VAS LTR (2025) and causal inference for packages (2026) — paid visibility inside ranking and its measurement.
  - Rochet and Tirole (2003), Gurley (2012), a16z (2020) — price structure, fragmentation and marketplace metrics.
  - Directive (EU) 2019/2161 and Regulation (EU) 2019/1150 — paid-ranking disclosure.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Safe Deal take rate (about 7.4% on €1.02B GMV) added and the superseded 4.1M/€310M caveat removed from the spec, Golf duplicate breakdown aligned with messaging-and-leads, [[toolkit]] link restored, Vinted fee naming hedged, EU texts relinked to EUR-Lex. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
