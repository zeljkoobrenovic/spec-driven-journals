---
status: accepted
revised: 2026-10-20
---

# Spec: Ranking for Two Sides: Relevance, Freshness and Paid Visibility

## Intent

Show architects that the order of a results page is a system with separable parts, not a sort setting. A relevance model estimates buyer action. A separately owned, versioned ranking policy applies freshness, paid placement, diversity, exploration and trust rules. A ranking log records what was served and why. The chapter owns learning to rank, paid-organic blending and ranking transparency. It argues that Paid-Rank Drift comes from rules hidden as engine boost multipliers that are each tested alone. The remedy is layering, a relevance floor with a cap on paid positions, delivery accounting, two-sided labels and guardrails, and transparency generated from configuration. After reading it, a Chief Architect should know what to standardize across brands (the machinery) and what to leave local (the models and the policy values).

## Audience

Chief architects, search and ranking leads, data science leads and monetization product leads in listing marketplaces. They know search engines and A/B testing. They need the marketplace-specific shape of ranking: two sides, rare and delayed conversions, paid visibility and EU ranking law.

## Success criteria

- [ ] Reader can define ranking (the Omnibus definition), sort order, relevance model, ranking policy and exposure, and can place each signal family with its owner, update rate and risk (signal table).
- [ ] Reader can draw the four-stage ranking function and state each component's contract, including "the relevance model must not read entitlements" (Figure 2, responsibility table).
- [ ] Reader can explain bump mechanics (a separate sort timestamp, not a lifecycle transition), reposting as a free bump, and freshness decay.
- [ ] Reader can choose labels and a model family for LTR, and explain features as served, position bias correction (Joachims 2017) and exploration for new listings.
- [ ] Reader can compare fixed slots, multipliers, separate auction plus merge, and unified ranking with a floor (eBay 2020), and explains delivery accounting and the OLX selection-bias lesson.
- [ ] Reader can map P2B Art. 5, Omnibus Annex I 11a and Art. 7(4a), and DSA Arts. 17, 26, 27 and 38 to engineering consequences, including "demotion is a restriction".
- [ ] Reader can pick evaluation methods (offline replay, interleaving, cluster randomization) and the seven guardrails.
- [ ] The Veldmark Tradeyard case runs from boost archaeology to ranking policy v1, with an experiment result table and a dated go-live.

## Non-goals

- Engine choice, index design, update storms and reindexing: owned by [[search-architecture]].
- Query parsing, synonyms and hybrid retrieval: owned by [[query-understanding]].
- Product catalog, entitlement ledger and sold-versus-delivered reconciliation: owned by [[products-and-entitlements]]. Revenue models: owned by [[monetization-models]].
- Interference designs in depth: owned by [[experimentation]]. Model governance: owned by [[ml-platform]].
- The full regulatory map: owned by [[marketplace-regulation]]. Map-specific ranking: owned by [[map-search]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- P2B repeal: the 19 November 2025 proposal is still pending as of October 2026. Recheck its status before print.
- Does a promoted listing bought by a private seller count as an "advertisement" under DSA Art. 26? The chapter labels this as a legal judgment and takes the prudent reading.
- The DSA article texts were read from an unofficial mirror. Check the wording against EUR-Lex.
- The leboncoin re-ranker figures rest on secondary sources, because the primary Medium post returned 403.
- No classifieds operator has published its bump mechanics or seller-exposure caps. The chapter presents those as industry practice and recommendation.

## Decision log

- **2026-10-19** — Built the chapter around the separation of the relevance model from the ranking policy, rather than around algorithms. The Paid-Rank Drift failure is organizational and architectural, and an algorithm survey would not show it.
- **2026-10-19** — Told the Veldmark case as "boost archaeology", a dated table of five accreted rules, so that the mechanism of drift is concrete. Reused the Rotterdam city bike (position 14; first contact came from saved searches) without changing any ledger fact.
- **2026-10-19** — Recommended GBDT LambdaMART-style ranking as the default and neural re-rankers conditionally, grounded in mobile.de (2024) and the Airbnb lineage. A neural-first recommendation was rejected.
- **2026-10-19** — Made the experiment cluster-randomized (category × region) and reported a revenue cost (−2.5% VAS revenue per search) alongside the gains, to keep the trade-off honest.

## Sources

- **Internal**
  - `_research/brief-search-discovery.md` Parts 5–8 — LTR lineage, blending, position bias, evaluation.
  - `_research/brief-monetization-economics.md` 5.1–5.3, 9.2–9.3 — paid products, OLX VAS LTR and causal measurement, P2B and Omnibus text.
  - `_research/brief-trust-safety-regulation.md` 5.1–5.6 — DSA Arts. 17, 26, 27; demotion as restriction; P2B repeal proposal.
  - `_research/brief-platform-data-ml.md` Part 9 — interference designs.
  - [[search-architecture]], [[products-and-entitlements]], [[experimentation]], [[marketplace-regulation]], [[recommendations]].
- **External**
  - eBay (2020) on unified promoted-listing ranking; OLX Engineering (2025, 2026); mobile.de at Berlin Buzzwords (2024); Airbnb papers (2018–2026); Joachims et al. (2017); Singh and Joachims (2018); Johari et al. (2020).
  - Regulation (EU) 2019/1150 Art. 5 and Directive (EU) 2019/2161 and Regulation (EU) 2022/2065 Arts. 17, 26, 27 and 38 (Official Journal texts via the EU Publications Office, checked 19 Oct 2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: verified P2B, Omnibus and DSA quotes against Official Journal texts and repointed sources; completed the Omnibus ranking definition; expanded VAS, LTR, P2B and UCPD on first use; timetoread 36 min. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,911 → 6,954 prose words; lead now states the chapter's place in Part IV and what depends on it; 2 headings renamed ("What Ranking Is: Prominence, Not a Sort", "Architecture: Model, Policy Layer and Ranking Log"); exposure paragraph split; first sentences sharpened; spec success criterion repointed from Figure 1 to Figure 2 (the pipeline figure became Figure 2 when illustrations were added). *(AI-mediated session)*
