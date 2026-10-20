---
status: accepted
revised: 2026-10-20
---

# Spec: Testing a Two-Sided Market: Experimentation Platforms

## Intent

Show marketplace architects why ordinary A/B testing misleads in two-sided markets and what platform and method make experiments trustworthy. The chapter defines interference, explains which randomization unit fits which mechanism (buyer, seller or listing, two-sided, cluster, switchback, geographic), lays out the four components of an experimentation platform (assignment, exposure, governed metrics, analysis engine), and turns guardrails and review of ranking and pricing experiments into governance. The Veldmark bump-price test that reported +18% and delivered about −2.5% carries the argument.

## Audience

Chief architects, heads of data and experimentation, search and monetization leads, and product directors in listing marketplaces. They should leave able to pick a randomization unit for a proposed change, specify what the assignment service and exposure log must support, name the guardrails a monetization or ranking test needs, and set up a review process for price and visibility experiments.

## Success criteria

- [ ] Reader can define SUTVA, interference, cluster randomization and guardrail metric, and recognize a transfer between groups mistaken for an effect.
- [ ] Reader can name the four platform components and the marketplace-specific requirements of each (unit types, layers, server-side pricing assignment, two-sided exposure, cluster-aware inference).
- [ ] Reader can choose between buyer-side, listing-side, two-sided, cluster, switchback and geographic designs using the mechanism of the change and which side is scarce.
- [ ] Reader can explain the control-trend and congestion guardrails and why liquidity guardrails apply to revenue tests.
- [ ] Reader can describe the legal and commercial cautions for price experiments.
- [ ] Every company and research claim carries a dated source; Veldmark numbers are internally consistent and agree with the ledger and the ranking chapter.

## Non-goals

- Governed metric definitions and exposure event design ([[data-platform]]).
- Ranking models, offline evaluation and the ranking guardrail list in detail ([[ranking]]).
- Model lifecycle and governance ([[ml-platform]]).
- Monetization model design and package economics ([[monetization-models]], [[products-and-entitlements]]).
- Regulatory detail of personalized pricing and P2B ([[marketplace-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No classifieds company has published an interference-aware design (cluster or two-sided) for its own experiments; the chapter relies on Airbnb research and Veldmark. Revisit if one appears.
- Whether randomized consumer price tests trigger the personalized-price information duty is stated as a question for counsel; confirm against the consolidated Consumer Rights Directive.
- DoorDash's 2018 switchback post could not be retrieved; it is cited as widely reported only.

## Decision log

- **2026-10-19** — Built the chapter on a seller-randomized bump-price test, because a paid visibility product sells a congestible resource and shows interference more clearly than a ranking model change (which [[ranking]] already uses for its cluster experiment).
- **2026-10-19** — Recommended centralizing the stats engine and metrics before tools, following Adevinta's documented Fisher → Nightingale → Houston path, rather than a single-vendor standardization.
- **2026-10-19** — Ran the Veldmark retest in Tradeyard Belgium rather than the Netherlands so that it did not overlap the ranking-policy cluster experiment, illustrating experiment layers.
- **2026-10-19** — Reported the retest's wider intervals explicitly, to make the power cost of cluster designs part of the lesson.

## Sources

- **Internal**
  - [[data-platform]] — exposure event, governed metrics, provisional and final values.
  - [[ranking]] — ranking guardrails and the Sept–Oct 2027 cluster experiment.
  - [[ml-platform]] — district-randomized Hearthly pricing hint.
  - [[monetization-models]] — OLX causal evidence and paid-product measurement.
  - `_research/brief-platform-data-ml.md` Part 9; `_research/brief-search-discovery.md` Part 7; `_research/brief-monetization-economics.md` 5.3 and 6.2.
- **External**
  - Adevinta Tech Blog (2023–2024) — Fisher, Houston, benchmark, streaming results, ten tools to one.
  - Zalando Engineering (2021) — SRM and platform evolution.
  - Johari et al. (2020); Holtz et al. (2020); Bojinov et al. (2020) — interference and designs.
  - Deng et al. (2013) CUPED; Johari, Pekelis and Walsh (2015) always-valid inference; Beasley (2023) safe testing at Vinted.
  - Zhang et al. (2025) Airbnb interleaving; eBay (2020) unified promoted ranking; OLX (2026) causal package analysis.
  - Kohavi, Tang and Xu (2020) — general practice.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: verified the Omnibus personalized-price duty against the Official Journal text (Art. 6(1)(ea) CRD), corrected the Fisher/Nightingale claim, dated the eBay 2020 evidence. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
