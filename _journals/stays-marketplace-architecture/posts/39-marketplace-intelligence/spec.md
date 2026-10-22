---
status: accepted
revised: 2026-10-22
---

# Spec: Knowing the Marketplace: Data Platform, Metrics and Partner Insight

## Intent

Show that the hard problem of marketplace intelligence in a stays group is shared meaning, not data volume. A "booking" is a family of metrics with different time bases (created, net of cancellations in the period, cancellation-adjusted by cohort, stayed, honored), and every consumer — board reporting, experiments, ranking labels, partner dashboards, regulatory exports — must read one governed definition. The chapter gives the reference architecture (collection and consent gate, event backbone, lakehouse, data products, metric layer, partner insight read model), the governance that makes it work (owners, tiers, reconciliation to the ledger), and the specific design of partner insight, where hotels' business data and hosts' personal data need different privacy rules. After reading, an architect can design or review a stays group's data platform and decide what to share across brands.

Productscape domains covered: TAM `mkli` (Marketplace Intelligence), `perf` (Partner Performance Analytics); HSM `data` (Marketplace Intelligence & Experimentation), `host` (Host Performance & Earnings). Added domains: customer data platform and consent management; data platform (event backbone, lakehouse); platform regulatory reporting (data side).

## Audience

Chief and principal architects, heads of data and analytics platforms, finance and BI leads, and product leads for partner and host analytics at OTAs, hosted-stays marketplaces and groups that run both.

## Success criteria

- [x] Defines and owns governed metric, data product and partner insight; defines behavioral and business events, event taxonomy, metric layer, attribution and CDP.
- [x] Presents the booking metric family with time bases, anchored in the published definitions of Airbnb and Booking Holdings (FY2025 10-Ks), and shows that Corvane's ledger GBV is stay-based.
- [x] Corvane worked example "two definitions of booking" with ledger-consistent numbers (51.0M mixed vs 51.9M created vs 36.0M stayed; 34% of room nights vs 13% of reservations; Miradouro 268/231/191).
- [x] Reference architecture with a component table and at least two diagrams (illustrated); consent treated as data with ePrivacy, GDPR and DMA citations.
- [x] Partner insight: shared definitions with ranking and programs, benchmark privacy and competition rules, ranking-log explanations, DMA Art. 6(10); hosts as natural persons.
- [x] STR activity data (Regulation (EU) 2024/1028) designed as a reconciled data product.
- [x] Trade-off table, "Hotels and Homes" section with judgement, failure modes, Chief Architect's view, questions, hand-off to [[stays-experimentation]].
- [x] Every company claim dated and sourced; inferences labeled.

## Non-goals

- Experiment design, interference and delayed outcomes ([[stays-experimentation]]).
- Feature platforms, model training and serving ([[stays-ml-platform]]).
- Event backbone internals, outbox and CDC ([[event-driven-stays]]).
- Channel architecture and metasearch integration ([[demand-channels]]).
- DAC7 and tax reporting ([[taxes-on-stays]]); STR compliance design and the regulatory map ([[stays-regulation]]).
- Extranet and host-app surfaces ([[extranets-and-host-tools]]); ranking internals and the ranking log ([[stays-ranking]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- How Booking.com meets DMA Article 6(10) is not documented; the chapter labels its view as inference.
- Minerva's current state at Airbnb is not public (source from 2021).
- Which Member States operate live single digital entry points, and the Commission's API specification, were not verified; the chapter stays generic.
- Benchmark thresholds (minimum group sizes, dominance caps) are illustrative; no marketplace publishes its own.

## Decision log

- **2026-10-21** — Built the chapter around the booking metric family and its time bases, because the ledger itself mixes bases (34% of room nights vs 13% of reservations; stay-based GBV) and public definitions (Airbnb, Booking Holdings) show the same ambiguity.
- **2026-10-21** — Named Corvane's metric layer Gauge and placed the decision in the July 2027 forum, consistent with the October 2027 workspace decision that the partner analytics read model sits on the group metric layer.
- **2026-10-21** — Treated hosts' performance data as personal data with stricter benchmark rules, the sharpest hotel-versus-home difference for this topic.
- **2026-10-21** — Kept Corvane Connect's data as a separate domain, following the May 2027 neutrality rule.

## Sources

- **Internal**
  - [[meet-corvane]], [[extranets-and-host-tools]], [[stays-ranking]], [[dynamic-pricing]], [[personalization-and-recommendations]], [[connectivity-and-channel-managers]], [[taxes-on-stays]], [[refunds-and-reconciliation]].
  - `_research/brief-platform-data-ml.md`, `brief-host-partner-guest-service.md`, `brief-trust-safety-regulation.md`, `productscape-digest.md` (bricks `mkli`, `perf`, `data`, `host`; gaps: consent, data platform).
- **External**
  - Airbnb Form 10-K FY2025 (2026); Booking Holdings Form 10-K FY2025 (2026); Airbnb Minerva (2021) and multi-product data architecture (2026); Booking.com BDX migration (2026) and semantic-layer post (2026); Agoda Kafka (2023, 2025); Agoda Partner Portal (2026); Booking.com Connectivity API list.
  - Regulation (EU) 2024/1028; DMA (EU) 2022/1925 Arts. 5(2), 6(10); GDPR; Directive 2009/136/EC (ePrivacy Art. 5(3)); DAC7.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Gauge/Flipside sentence aligned with Experimentation Standard v1 (Sept 2027); timetoread corrected. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,809 → 6,414 prose words; opening now places the chapter in Part VIII; Failure Modes compressed to pointer bullets; Chief Architect's "Decide" list folded into one paragraph; one design-review question and Booking.com's migration reasons cut; no headings renamed. *(AI-mediated session)*
