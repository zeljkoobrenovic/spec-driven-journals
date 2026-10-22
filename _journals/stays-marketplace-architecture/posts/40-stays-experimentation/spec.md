---
status: accepted
revised: 2026-10-21
---

# Spec: Testing Everything: Experimentation Platforms for Stays

## Intent

Show architects that an experimentation platform for a stays marketplace has to answer two questions that generic A/B tooling does not.

1. **When is the outcome known?** Bookings are promises that are canceled weeks later, so funnel experiments need a **delayed-outcome metric**, defined by an outcome, a maturation rule and a maturity share. They also need a two-stage readout: an early read on a validated surrogate and a final read on matured stays.
2. **Do treated and control units affect each other?** Guests compete for the same nights and hosts react to treatments, so visitor randomization overstates effects. That **marketplace interference** has to be designed for with cluster, market, switchback or encouragement designs.

The chapter owns both terms. It describes the platform components (registry, assignment with stays unit types, exposure log, outcome joiner, governed metrics, analysis, guardrails, decision record). It covers how to test pricing, ranking and partner features, including the legal limits. It recommends one shared group platform with per-brand defaults. After reading, a Chief Architect should be able to judge whether a reported experiment win is a stay or a mirage.

Productscape domains covered: TAM `mkli` (Experiment and Causal Analysis Layer), TAM `deal` (Treatment Experimentation Controls), HSM `data` (Experimentation and recommendation layer).

## Audience

Chief architects, data and experimentation platform leads, data scientists, and search, pricing and product leads at OTAs and hosted-stays marketplaces. They know A/B testing basics. They need the stays-specific failure of those basics and the platform design that fixes it.

## Success criteria

- [ ] Reader can define randomization unit, trigger and counterfactual exposure, OEC, guardrail, delayed-outcome metric (outcome, maturation rule, maturity share), surrogate, marketplace interference (three channels) and global treatment effect.
- [ ] Reader can draw the platform's components (Figure 2) and state the stays-specific requirement of each, including exposure-log retention and unit types.
- [ ] Reader can explain the two-stage readout, surrogate validation (the surrogate ledger) and the role of short and long-term holdouts.
- [ ] Reader can cite dated interference evidence (Holtz et al. 2020: 32.60%; Johari et al. 2021: market balance) and choose a design with Figure 3 and the design trade-off table, including why switchbacks fit stays poorly.
- [ ] Reader can describe documented practice at Booking.com (2017, 2026), Airbnb (2014–2026) and Agoda (2023) with dates, and does not attribute undocumented internals.
- [ ] Reader can explain the limits on price, ranking, partner and interface experiments (Omnibus personalized-price disclosure, DSA Art. 25, CPC commitments) as review classes.
- [ ] The Corvane case shows Roomstead's badge as a delayed-outcome problem and Nookaway's as an interference problem, with tables, and ends in the dated Experimentation Standard v1.
- [ ] The Hotels and Homes table and judgement say: share the platform, keep defaults per brand.

## Non-goals

- Governed metrics, the warehouse and partner analytics: owned by [[marketplace-intelligence]].
- Model training, serving, feature platforms and the cancellation-prediction model itself: owned by [[stays-ml-platform]].
- Ranking design and Ranking Policy v1: owned by [[stays-ranking]].
- Pricing models and Smart Rate guardrails: owned by [[dynamic-pricing]]; promotion funding and holdouts: [[promotions-and-loyalty]].
- The full regulatory map: owned by [[stays-regulation]].
- Statistical derivations; the chapter names techniques and cites sources.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Agoda's lenient p-value post was read from an archived copy (per the OTA brief); recheck the live URL before print.
- Whether a randomized guest-level price test counts as "personalised" pricing under CRD Art. 6(1)(ea) is presented as an open legal question, not settled law.
- The Airbnb "variance reduction for sparse and delayed outcomes" and "Beyond the Experiment Window" papers were seen only as titles on Airbnb's research pages; the chapter cites them as such. Read them before any expansion.
- Booking.com's and Airbnb's standard OECs for funnel experiments are not public; the chapter says so.
- Booking windows, power figures and the badge results are illustrative Corvane numbers (added to the ledger).

## Decision log

- **2026-10-21** — Built the Corvane case as one treatment on two brands with opposite failures, so the chapter's two owned terms each get a concrete anchor: Roomstead (delayed outcome, interference negligible) and Nookaway (interference, delayed outcome small).
- **2026-10-21** — Recommended a predicted-stay surrogate from the cancellation model for early reads, with an automatic final read at 85% maturity, rather than waiting months for every decision. The surrogate ledger makes its error visible.
- **2026-10-21** — Recommended "enforce through defaults and registry, review by class" as a middle position between Booking.com's documented education-first culture and central approval, arguing that a merging group needs the platform to carry more rules.
- **2026-10-21** — Chose Trialroom as the base of the group platform and ported Flipside's cluster module, consistent with the ledger's two-platform starting point and One Stay's shared data platform.

## Sources

- **Internal**
  - `_research/brief-platform-data-ml.md` Part 7 — experimentation platforms; OTA vs hosted-stays interference.
  - `_research/brief-booking-com.md` §2.5–2.6 — ET, experimentation quality, voluntary adoption, KDD 2019 lessons.
  - `_research/brief-airbnb.md` Part 7 — ERF, Minerva, interleaving, research list.
  - `_research/brief-expedia-agoda-tripcom.md` §6.4, §6.8 — Agoda thresholds and A/B migration.
  - `_research/brief-availability-pricing.md` Part 12 — Omnibus personalized pricing, CPC commitments.
  - [[stays-ranking]], [[promotions-and-loyalty]], [[dynamic-pricing]], [[personalization-and-recommendations]], [[marketplace-intelligence]], [[stays-ml-platform]].
- **External**
  - Booking.com: Lopez Kaufman et al. (2017); booking.ai posts on quality, hypotheses, outliers and voluntary adoption (2026).
  - Airbnb: ERF (2014), Minerva (2021), Holtz et al. (2020), Zhang et al. (2025), research publications page and 2025 year in review.
  - Johari et al. (2020/2021); Bojinov et al. (2020); Zeng et al. (2026); Deng et al. CUPED (2013); Kohavi, Tang, Xu (2020).
  - Directive (EU) 2019/2161; Regulation (EU) 2022/2065 Art. 25 (fetched 21 October 2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Added capability map v2 outcome (experimentation and ML shared engines); flagged the 2017 Booking.com paper's age; timetoread corrected. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
