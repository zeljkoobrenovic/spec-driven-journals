---
status: accepted
revised: 2026-10-19
---

# Spec: Models in Production: ML Platforms and Use Cases

## Intent

Give architects of listing marketplaces a way to treat machine learning as a governed portfolio running on a shared platform, not as an accumulation of team-built models. The chapter classifies use cases by the decision a model makes (inform, order, gate, commit), describes the ML platform that marketplaces actually need (registry, serving modes, feature definitions, label pipelines, prediction logs, monitoring), treats the feature store as conditional, and uses the documented Zillow Offers wind-down to show why an estimate built to inform must not be used to commit money without a new validation regime. After reading it, the reader should be able to inventory their models, set governance by tier, and decide what the group platform must provide first.

## Audience

Chief and enterprise architects of marketplace groups, heads of data and ML, ML platform leads, and product leaders who own valuation, pricing or trust models. They know ML in general; they need the marketplace-specific decisions and the group-level governance.

## Success criteria

- [ ] Reader can place any marketplace model in one of four decision tiers and say what governance each tier requires (tier table, Chief Architect's view, lifecycle diagram).
- [ ] Reader can map the common use cases to lifecycle stage, tier, serving mode, label source and owning chapter (portfolio table).
- [ ] Reader can explain why most listing models should be scored on events and stored on the listing, and when an online feature store pays (serving-mode and feature-kind tables).
- [ ] Reader can name the label proxies of classifieds ML and their biases, and the four listing-specific drift sources.
- [ ] Reader can state the Zillow Offers facts from the SEC filings with dates and the four architectural lessons, labeled as interpretation.
- [ ] Reader can follow Valuo from estimate to pricing hint with the Lyon apartment's ledger numbers, the display rules, the Keybridge data exclusion and the label rule, and see why the guaranteed offer and lender license took different paths.
- [ ] Reader can weigh platform strategies (trade-off table) and understand the registration-first hybrid as the antidote to The Platform Mandate.
- [ ] Reader knows the AI Act's verified high-risk dates after the 2026 Digital Omnibus and why jobs and credit-adjacent uses matter.

## Non-goals

- Learning-to-rank design and paid-organic blending: owned by [[ranking]].
- Candidate generation and similar listings: owned by [[recommendations]].
- Risk scoring and fraud signals: owned by [[fraud-prevention]].
- Attribute extraction and enrichment pipelines: owned by [[normalization-and-enrichment]].
- Experiment design and interference: owned by [[experimentation]].
- Lakehouse, tracking plan and governed metrics: owned by [[data-platform]].
- Generative AI, agents and AI governance beyond models: owned by [[ai-in-listing-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether a property AVM used inside a mortgage decision falls under AI Act Annex III point 5(b) is unresolved; the chapter says so and leaves it to counsel.
- No classifieds company has publicly documented a feature store; if one appears, update the feature-store section.
- Motor price-rating methodologies (mobile.de, AutoScout24, Auto Trader UK) remain undocumented; the chapter offers a labeled reference-architecture inference only.
- Zillow Tech Hub posts are cited via the Medium publication (RSS-read); the individual floor-plan post URL could not be fetched directly.

## Decision log

- **2026-10-19** — Organized the chapter around decision tiers (inform, order, gate, commit) instead of a catalog of algorithms, because governance and validation depend on consequence of error, and Valuo shows one model in three tiers.
- **2026-10-19** — Presented the feature store as conditional, since none is documented at classifieds and most listing features are intrinsic to the listing record; logged features at prediction time are the default.
- **2026-10-19** — Made Valuo the single worked example, with Motorvane's Golf rating as a short second case of an undeclared consumer; added Veldmark's model inventory, ML platform decision and pricing-hint rules to the ledger.
- **2026-10-19** — Used the Digital Omnibus postponed dates (verified on the European Parliament Legislative Train, September 2026) rather than the original AI Act dates.

## Sources

- **Internal**
  - `_research/brief-platform-data-ml.md` Part 10 (ML platforms, AVMs, image ML) and Part 9 (experimentation).
  - `_research/brief-real-estate-portals.md` A.4, B.1, C.9, Part D (Meilleurs Agents, Zestimate, Zillow Offers, AVM rules).
  - `_research/brief-olx.md` 4.3–4.11 (LTR, embeddings, recommendations, delivery ML, data platform).
  - [[meet-veldmark]], [[entity-resolution]], [[categories-and-taxonomies]], [[experimentation]].
- **External**
  - Adevinta, OLX, Zillow and Uber engineering posts; Zillow SEC filings (2021, 2026).
  - EU AI Act Annex III; European Parliament Legislative Train on the Digital Omnibus on AI.
  - Sculley et al. (2015); Mitchell et al. (2018); Airbnb KDD 2018 pricing paper.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: hedged pre-2023 OLX and Airbnb evidence as possibly superseded, standardized Sources headings; verified Zillow 10-K, Digital Omnibus on AI and Annex III quotes. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
