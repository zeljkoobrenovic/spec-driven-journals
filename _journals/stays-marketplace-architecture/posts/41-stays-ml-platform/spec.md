---
status: accepted
revised: 2026-10-22
---

# Spec: Models in Production: ML Platforms and Use Cases for Stays

## Intent

Show architects that the hard problems of machine learning in a stays marketplace are platform and governance problems, not modeling problems. The chapter maps the ML use-case portfolio of both marketplace types by the **decision each model drives** and the cost of a wrong answer, then takes apart the platform that runs them: a **feature platform** that defines features once and computes them point-in-time correct for training and serving, training and evaluation with delayed and reversible labels, three serving modes, monitoring of outputs as well as inputs, and a group **shock register** (disruption signal with declared hold, widen, exclude or stop behavior). It owns **ML platform (stays)**, **feature platform** and **model governance (stays)**, with a four-tier consequence classification where a model's tier is the highest tier of any consumer and every new consumer needs an approved use. It maps the EU AI Act (as amended by the 2026 AI Omnibus), GDPR Article 22, the Geo-blocking Regulation and the Omnibus Directive's personalized-price disclosure onto stays use cases. After reading it, a Chief Architect knows what to share across two marketplaces (machinery, registry, disruption signal, destination features) and what not to (models, entity keys).

Productscape domains covered: TAM `mkli` (decisioning models), TAM `rate` (pricing and forecasting models), HSM `data`.

## Audience

Chief architects, heads of data and ML platform, ML engineering leads and product owners of OTAs and hosted-stays marketplaces. They know ML basics, feature stores and model serving. They need the stays-specific shape: delayed and reversible labels, shocks, third-party consequences and the regulatory map for consequential models.

## Success criteria

- [ ] Reader can define ML platform, feature, feature platform vs feature store, point-in-time correctness, training-serving skew, drift types and model governance, and explain why stays labels are delayed, reversible and censored.
- [ ] Reader can place each stays use case (ranking, recommendations, pricing, cancellation prediction, forecasting, fraud, screening, freshness, matching, content, translation, routing, host acceptance) by decision, serving mode, label delay, cost of error and owning chapter.
- [ ] Reader can draw the platform (Figure 1) and the one-definition, two-computation feature path (Figure 2), citing dated public evidence from Airbnb (Chronon 2024, 2026), Booking.com (2019 lessons, 2026 feature platform), Expedia Group (2026) and Agoda (2020, 2026).
- [ ] Reader can apply the four-tier consequence classification and the "tier of the highest consumer" rule.
- [ ] Reader can state what the AI Act does and does not classify as high-risk for stays (Annex III 1(a), 4(b), 5(b); Article 5(1)(c); Article 50) with current application dates, and why GDPR Art. 22, Geo-blocking and personalized-price disclosure bite first on guest-level decisions.
- [ ] The Corvane case runs from Tideline's reuse and the ATC strike drift (96 relocations, €38,400) to Kiln and Tideline v2 with a before/after table.
- [ ] The Hotels and Homes table and judgement say what to share and what not to.

## Non-goals

- Learning to rank, labels for ranking and the ranking policy layer: [[stays-ranking]].
- Smart pricing models and guardrails: [[dynamic-pricing]].
- Recommendations and embeddings: [[personalization-and-recommendations]].
- Data platform, governed metrics, demand forecasting as a data product: [[marketplace-intelligence]].
- Experiment design, delayed-outcome metrics and interference: [[stays-experimentation]].
- Reservation screening and fraud models in depth: [[stays-trust-and-safety]], [[travel-fraud]].
- Generative AI assistants, agents and their evaluation: [[ai-in-travel-stays]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- AI Act dates follow the European Commission page (AI Omnibus in force 27 July 2026; Annex III high-risk obligations from 2 December 2027). The Omnibus's Official Journal reference was not fetched; recheck before print.
- Whether support-agent routing falls under Annex III 4(b), and whether Article 6(3) derogations apply, is the author's reading, not settled law.
- Airbnb Bighead and Zipline are not cited: no readable primary source in this session.
- Booking.com's Arize AI use rests on a booking.ai feed item (July 2026); the post itself was not read in full.
- Corvane numbers for Tideline, Kiln and the 226-model inventory are chapter-local illustrations, recorded in the ledger.

## Decision log

- **2026-10-21** — Built the Corvane case around reuse of one model (finance forecast → partner tool → proposed guest-level decision) rather than a model bug, so the "tier of the highest consumer" rule and approved uses are motivated by an incident. Reused the ATC strike weekend without changing its ledger numbers.
- **2026-10-21** — Made shock handling a platform capability (one disruption signal, declared behavior per model), generalizing Smart Rate's shock hold from [[dynamic-pricing]] instead of re-teaching it.
- **2026-10-21** — Recommended adopting an open-source feature platform (Corvane chooses Chronon) over building one; kept models with decision owners and machinery with the platform team.
- **2026-10-21** — Treated the AI Act as narrower than commonly assumed for stays and put GDPR Art. 22, Geo-blocking and personalized-price disclosure first for guest-level decisions; rejected a use-case-by-use-case legal survey as owned by [[stays-regulation]].

## Sources

- **Internal**
  - `_research/brief-platform-data-ml.md` Parts 5, 6, 8 and 11 — Chronon, Booking.com 2019 lessons, Expedia, Agoda, COVID forecasting, synthesis.
  - `_research/brief-airbnb.md` Parts 5–7; `_research/brief-booking-com.md` 2.6; `_research/brief-expedia-agoda-tripcom.md` 6.3–6.4; `_research/brief-trust-safety-regulation.md` Part 4.
  - [[dynamic-pricing]], [[stays-ranking]], [[personalization-and-recommendations]], [[stays-search-architecture]], [[calendar-sync]], [[content-and-media]].
- **External**
  - Airbnb Engineering, Chronon (2024, 2026) and COVID forecasting posts (2026) — feature platform, refit/respecify/hold.
  - AWS Database Blog, Booking.com feature platform (2026) — online/offline store design and scale.
  - Regulation (EU) 2024/1689 (Articles 5, 50; Annex III), European Commission AI Act page (AI Omnibus, live October 2026), Regulations (EU) 2016/679 and 2018/302, Directive (EU) 2019/2161.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Added capability map v2 outcome for ML; flagged the 2018 Airbnb pricing paper's age; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,356 → 6,030 prose words; opening ties the chapter to Part VIII's "share the machinery, not the meaning"; Failure Modes compressed to one-line pointers; Chief Architect's view no longer restates the Kiln decisions; repeated transitions and recaps cut. Spec unchanged. *(AI-mediated session)*
