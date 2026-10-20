---
status: accepted
revised: 2026-10-20
---

# Spec: Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy

## Intent

Give the book's readers a shared vocabulary for marketplace models and prove that the model is an architecture decision, not a pricing decision. The chapter classifies marketplaces first by **endpoint** (where the platform's job ends: contact, lead, payment and delivery, guaranteed outcome) and then along five further axes (scope, seller type, item identity, money flow, risk ownership). It shows what each rung of the endpoint ladder adds to identity, bounded contexts, trust, ranking, monetization, data and regulation, and uses the documented record (leboncoin, Kleinanzeigen, Marktplaats, Vinted, eBay, Rightmove, Autotrader, Zillow, OLX, CarGurus) to show that marketplaces move along the ladder in both directions. After reading, an architect treats the model as an explicit, per-country, per-category profile held as configuration.

## Audience

Chief and enterprise architects of marketplace groups, principal engineers and product and engineering directors who must decide what a shared platform assumes about the marketplaces it serves, or who face a "let's go transactional" proposal.

## Success criteria

- [x] Defines classifieds, lead-generation marketplace, transactional marketplace, managed marketplace, horizontal and vertical precisely, with dated documented examples.
- [x] Presents the endpoint ladder in a table (endpoint, observability, monetization, money and risk, examples) and the six-axis marketplace profile.
- [x] Maps each model to its architectural consequences (identity, contexts, trust, ranking signal, monetization, data, regulatory switch) in one table.
- [x] Documents moves along the ladder in both directions with sources: category-gated transactional layers, OLX's pay-and-ship de-prioritization, Zillow Offers, OLX Autos and CarOffer retreats.
- [x] Veldmark worked example: the twenty-profile register with ledger numbers; city bike and Essen Golf on different rungs; the Tradeyard PL / Motorvane PL overlap; Keybridge as SaaS, not a marketplace.
- [x] Trade-off table for where the marketplace should end, plus a vertical-differences table.
- [x] At least two mermaid diagrams; Chief Architect's view; questions to ask; Sources and Evidence.

## Non-goals

- Liquidity and its metrics ([[liquidity-and-network-effects]]).
- Industry history and the formation of portfolios ([[industry-evolution]]).
- Full vertical comparison and the shared-versus-specific decision ([[vertical-requirements]]).
- Payment, shipping and buyer-protection design ([[transactions-and-payments]]); revenue models and KPIs in depth ([[monetization-models]]).
- Professional SaaS and neutrality design ([[professional-seller-tooling]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- DAC7's reach into classifieds with optional, partial in-platform payment is not settled; the chapter states it as a reading to confirm with counsel.
- ~~Safe Deal volume vs €75M revenue~~ — resolved 2026-10-19: the ledger now gives 11.6M transactions and ~€1.02B GMV; the chapter uses them and states the ~7% take rate.
- Kleinanzeigen's payment provider changed over time (OPP 2020–2023, Adyen per its current help page; see [[case-ebay-classifieds]]); the chapter does not name it.

## Decision log

- **2026-10-19** — Chose "endpoint" (where the job ends) as the primary axis over horizontal/vertical, because it predicts bounded contexts, observability and regulation more directly.
- **2026-10-19** — Added "managed marketplace" as a fourth rung and treated pro SaaS as an adjacent model off the ladder, so Keybridge and the iBuying/OLX Autos cases have a place.
- **2026-10-19** — Introduced the Veldmark "marketplace profile register" (twenty rows, brand × country × category group) as the chapter's architectural artifact, rather than a brand-level classification.
- **2026-10-19** — Resolved the Tradeyard PL / Motorvane PL overlap commercially (dealers move to Motorvane packages, syndicated to Tradeyard) to illustrate that model overlaps are commercial decisions with architectural consequences.

## Sources

- **Internal**
  - [[meet-veldmark]] — the fictional group and its four brands.
  - [[where-listing-systems-go-wrong]] — The Platform Mandate, The Scam Inbox, Vanity Liquidity.
  - Research briefs: monetization-economics, adevinta, olx, automotive, real-estate-portals, trust-safety-regulation; productscape digest.
- **External**
  - Adevinta annual reports 2019 and 2023, strategic report 2025 — revenue types, transactional history, convergence and decentralization.
  - Autotrader FY26, Rightmove FY2025, Zillow, CoStar, CarGurus and eBay 10-Ks — lead-generation and transactional economics, managed-model retreats.
  - Vinted 2025 results, price list and newsroom — transactional-first recommerce.
  - OLX Tech (2022, 2023), Prosus FY25, News24 (2023) — contact labels, Pay&Ship, OLX Autos.
  - Directive 2019/2161, DSA Art. 30, DAC7 guidance — regulatory switches.
  - Gurley (2012), Parker (2010), a16z (2020) — practitioner framing.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Safe Deal figures updated to 11.6M / ~€1.02B with take rate, DSA Art. 30 and Omnibus wording checked against the Official Journal, Golf raw vs deduplicated leads, Safe Deal profile count corrected. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,118 → 7,092 prose words; lead now states the chapter's place in Part I and the later chapters that use the marketplace profile; excerpt names all four rungs; Deal Builder/mobile.de subsection renamed "Pattern 4" to match the patterns list; DAC7 point split into its own paragraph; topic sentences tightened; no spec criteria changed. *(AI-mediated session)*
- **2026-10-20** — Retitled to name all four models the chapter covers, including managed marketplaces; permalink unchanged. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
