---
status: accepted
revised: 2026-10-20
---

# Spec: Recommendations for Inventory That Disappears

## Intent

Show architects that recommendation in a listing marketplace is shaped mainly by inventory churn, not by algorithm choice. Every listing starts cold, and every recommendation can point to an item that is already gone. The chapter owns candidate generation, similar listings and cold start. It argues for a four-stage pipeline: several candidate sources, at least one of them content-based; one serving-time filter on the same status read model as search; a contact-optimized re-ranker; and a policy layer for dealer caps, diversity and exploration. All of it is kept live by the listing event stream. It also covers evaluation beyond click-through (coverage, novelty, concentration) and the consent and regulatory limits on personalization. After reading it, a Chief Architect knows what to share across brands (the status model, the serving infrastructure, the logs, consent lineage) and what to leave local (the models and the policy values).

## Audience

Chief architects, recommendation and ML leads, discovery product owners and data protection leads in listing marketplaces. They know recommender basics. They need the marketplace-specific failure modes and the architecture that avoids them.

## Success criteria

- [ ] Reader can list the recommendation surfaces and state, for each, its anchor, latency budget, freshness need and outcome metric (surface table).
- [ ] Reader can explain why retail recommender assumptions fail for listings, with FINN.no (2018) and OLX Jobs (2023) evidence.
- [ ] Reader can compare content-based, item-item CF, factorization and graph methods, session models, embeddings and bandits under churn, and cite the Airbnb, Zillow, Adevinta, Vinted and OLX cases with years.
- [ ] Reader can draw the generate–filter–re-rank–policy pipeline and the event-driven removal path (Figures 1 and 2), and can state the "render from the live read model" and "same status model as search" rules.
- [ ] Reader can address the three forms of cold start and the feedback loops specific to listings.
- [ ] Reader can choose offline and online metrics and guardrails, and explain why click-through misleads.
- [ ] Reader can name the consent, DSA Art. 27 and 38, fair-housing and retention constraints, and the cross-brand data decision.
- [ ] The Veldmark Motorvane case runs from the Essen Golf problem to the rebuild and its results, consistent with the ledger (26-hour feed removal, 31 VIN-decoded attributes).

## Non-goals

- Search ranking, LTR training details and paid blending: owned by [[ranking]].
- Saved-search matching and alert fan-out: owned by [[saved-searches-and-alerts]].
- Feature stores, model governance and the ML platform: owned by [[ml-platform]].
- The listing event contract and outbox: owned by [[event-driven-listings]]. Tracking plan and consent propagation: owned by [[data-platform]].
- Interference designs: owned by [[experimentation]]. Agentic and AI channels: owned by [[ai-in-listing-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Airbnb KDD 2018 details (the cold-start averaging of nearby listing embeddings, corpus sizes, the +21% similar-listing CTR) appear only in secondary sources. The ACM text could not be fetched, so the chapter cites the abstract-level claims only.
- The Zillow 2021 post is cited through the Medium RSS feed, because the post's own page was blocked.
- The ePrivacy and GDPR statements are kept at the level of general principle. Lucía Ortega's role in the scenario stands in for counsel review.
- ~~The DSA wording was read from an unofficial mirror.~~ Resolved 19 Oct 2026: Articles 27 and 38 checked against the Official Journal text.

## Decision log

- **2026-10-19** — Organized the chapter around churn and availability rather than a survey of algorithms. The failure mode readers meet in practice is Ghost Inventory in carousels and e-mails, not a weak model.
- **2026-10-19** — Used the canonical Essen Golf and its 26-hour feed removal as the problem case. Added local, non-canonical carousel statistics and a September 2027 A/B result. The click-through decrease was kept visible in the results, to make the metric argument concrete.
- **2026-10-19** — Kept Motorvane on Elasticsearch 8 with filtered kNN, in line with the ledger's 2029 search review. A design that waits for the shared OpenSearch platform was rejected.
- **2026-10-19** — Treated cross-brand recommendation data as a governed, opt-in decision, linked to Veldmark ID (2028) and the Keybridge neutrality commitment, rather than as a technical capability.

## Sources

- **Internal**
  - `_research/brief-search-discovery.md` Parts 9–10 and 13 — recommendation evidence and listing-specific challenges.
  - `_research/brief-real-estate-portals.md` B.1 — Zillow similar-home embeddings (2021).
  - `_research/brief-platform-data-ml.md` Parts 8–10 — tracking, experimentation, feature-store caution.
  - `_research/brief-trust-safety-regulation.md` 5.1 and the fair-housing section — DSA Art. 27 and fair-housing advertising.
  - [[ranking]], [[event-driven-listings]], [[publication-pipeline]], [[ml-platform]], [[data-platform]].
- **External**
  - Vinted Engineering (2023, 2025); Adevinta (2022); Zillow Tech Hub (2021); Airbnb papers and posts (2018, 2020, 2025, 2026); FINN.no (2018); OLX Jobs (2023); GRU4Rec (2015).
  - Elastic filtered kNN documentation and DSA Art. 38 (fetched this session).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Golf leads labeled raw (23) vs deduplicated (19), sale time added, DSA Arts. 27/38 checked against the Official Journal (Art. 27 small-enterprise exemption noted), Zillow source linked to the 2021 post, old evidence flagged, acronyms expanded. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,820 → 5,855 words; lead now ties the chapter to Part IV and names map search and alerts as reusers of the availability rule; "Methods and Their Fit" renamed "Methods Under Churn"; two two-point paragraphs split; vague openers replaced with the Motorvane 7%-of-leads figure and stated points. *(AI-mediated session)*
