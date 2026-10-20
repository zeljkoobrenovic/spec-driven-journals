---
status: accepted
revised: 2026-10-20
---

# Spec: eBay Classifieds Group: Shared Platforms, Local Brands and a Sale

## Intent

Use the public record of eBay Classifieds Group (eCG), from eBay's first classifieds acquisitions in 2004 to the 2021 sale to Adevinta and the brand separation that followed, as a tested case of a federated marketplace group with a thin shared layer. The page must show which layers eCG shared (a coordinated search-engine choice, a group PaaS, a motors-vertical supply platform with published contracts, one external payments provider, a regional Benelux platform), what stayed local, and what the sale exposed: transitional services written into a competition remedy, and years of rebrand and replatforming work on the brands Adevinta kept. It must keep documented fact, the author's reading and labeled inference visibly apart, and end by testing the book's patterns and Veldmark's Common Ground choices against the case. After reading, a Chief Architect should prefer shared interfaces that can be handed over, keep a per-brand dependency register, and share the professional supply side of verticals before consumer products.

## Audience

Chief and enterprise architects of marketplace groups, platform and search leads, and engineering directors who integrate acquired marketplaces or prepare one for sale. They know platforms, search engines and Kafka; they need the evidence trail and the judgement.

## Success criteria

- [ ] A dated timeline replaces the Veldmark scene; every company fact carries a source and publication year, with old evidence flagged as describing replaced systems.
- [ ] The shared layers are described one by one with their interface type, and summarized in a layer map table.
- [ ] Inferences (MoVe's tenants, a possible shared generalist platform, carve-out shape) appear only in `INFERENCE, NOT DOCUMENTED` callouts or labeled figures; unverified internal platform names are not printed.
- [ ] The 2021 sale facts (US$9.2 billion, €130–165 million synergies, CMA transitional services, divestment dates) agree with [[case-adevinta]], and Adevinta's post-2021 strategy is linked, not retold.
- [ ] An explicit "Where the Public Evidence Stops" section.
- [ ] A trade-off table, a vertical-differences table, at least two mermaid diagrams, a Chief Architect's view, 6–10 questions and grouped sources.
- [ ] The final comparison covers the book's patterns and Veldmark's 2027 decisions, using only ledger facts.

## Non-goals

- Not a company profile, valuation or judgement on eBay's portfolio strategy.
- Does not retell Adevinta's integration, convergence and decentralization after 2021 ([[case-adevinta]]).
- Does not re-teach tenancy models ([[multi-country-platforms]]), consolidation sequencing ([[platform-consolidation]]), migration patterns ([[modernization-and-migration]]) or payment design ([[transactions-and-payments]]).
- Does not describe Gumtree, Kijiji or Vivanuncios engineering, for which no first-hand public source was found.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Which brands, other than Canada's receivers, used MoVe, and did mobile.de?
- Did eCG run a shared generalist platform for its smaller horizontals? Names circulating for it remain unverified.
- Scope and duration of the Gumtree UK transitional services.
- Identity of Kleinanzeigen's 2025 "new system" and its relation to any Adevinta platform.
- When Kleinanzeigen's buyer-protection provider changed from Online Payment Platform to Adyen.
- Ownership of Gumtree UK, Gumtree Australia and Kijiji Canada after 2024 (volatile).

## Decision log

- **2026-10-19** — Organized the case around shared layers and their interface types (agreement, external provider, published contract, undocumented parent dependency) rather than by brand, because the interface type is what predicted separation cost at the sale.
- **2026-10-19** — Upgraded MoVe from brief-level inference to documented fact for the Canadian tenant after re-reading the webhook-receiver README, which names Kijiji.ca and kijijiautos.ca as receivers; kept other tenants as inference.
- **2026-10-19** — Used Kleinanzeigen's 2019 and 2025 posts as the deepest engineering evidence but refused to link the 2025 migration to Adevinta's convergence plan, which the post does not mention.
- **2026-10-19** — For the Veldmark comparison, used a hypothetical 2029 Tradeyard Portugal sale built only from ledger dates (Adevinta's case used Hearthly), so the two cases test different shared capabilities; no ledger facts added.

## Sources

- **Internal**
  - [[case-adevinta]] — post-2021 story and payment flows, kept consistent.
  - [[multi-country-platforms]], [[platform-consolidation]], [[listing-ingestion]], [[search-architecture]], [[event-driven-listings]], [[modernization-and-migration]], [[ranking]], [[long-term-evolution]] — patterns tested.
  - `_research/brief-ebay-classifieds.md` (primary), `brief-adevinta.md`, `brief-search-discovery.md`, `brief-platform-data-ml.md`; scenario ledger.
- **External**
  - eBay SEC filings 2004 and 2020; eBay Inc. releases 2008, 2015, 2016 (re-verified 19 October 2026).
  - UK CMA decision ME/6897/20, 2021 (re-verified; transitional services offered by eBay for Gumtree UK).
  - Adevinta releases 2021–2023 (Gumtree UK and Australia sales re-verified).
  - Marktplaats Technology 2015/2017; Berlin Tech Blog 2018–2026 (2019 Kafka and 2025 migration posts re-verified); eBayClassifiedsGroup GitHub (MoVe READMEs re-verified); HashiConf 2018 (re-verified).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 10 load-bearing claims (SEC 2004/2020, CMA decision, Worldline, MoVe, Australia sale, rebrand); dated OPP at Kleinanzeigen to July 2023 (t3n) and the Adyen switch as after that; added Shpock buyer and acceptance date; tied the worked question to the tenancy model exit paths; American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,695 → 6,702 words (fact-dense case, structure only); opening now states the chapter's Part IX question (how thin a shared layer can be, what a sale exposes) and its feed into the Veldmark comparison; Phase 1's two subsection headings removed; six paragraphs re-led with their point; worked question split in two. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Trade-offs heading capitalized as in the 45 chapters. *(AI-mediated session)*
