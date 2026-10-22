---
status: accepted
revised: 2026-10-21
---

# Spec: Ordering the Results: Ranking for Guests, Partners and the Marketplace

## Intent

Show architects that the order of a stays results page is a system with separable parts, not a sort setting, and that in a stays marketplace it serves three parties: the guest, the partner or host, and the marketplace that earns different amounts from different properties. The chapter argues for four things. The relevance model should be trained on the **honored stay** (not clicks or gross bookings), because cancellations and host failures are common and delayed. Every commercial, program and reliability rule belongs in a **separate, bounded, versioned policy layer** with reason codes, never inside the model. A **ranking log** records features as served, offers, positions and reasons. The public description of ranking parameters is **generated from the policy configuration**. It owns learning to rank for stays, program-driven visibility and ranking transparency, and names Pay-to-Rank Creep as the failure it prevents. After reading it, a Chief Architect should know what to standardize across two marketplaces (the machinery) and what to leave to each brand (models and policy values).

Productscape domains covered: TAM `srch` (Ranking and Eligibility Pipeline; Filter and Explainability Controls), HSM `srch` (search index and relevance engine), with links to TAM `mkli` and HSM `data` for ranking signals.

## Audience

Chief architects, search and ranking leads, data science leads and commercial product owners of OTAs and hosted-stays marketplaces. They know search engines, ML and A/B testing. They need the stays-specific shape of ranking: offers instead of documents, delayed and reversible outcomes, paid partner programs, and EU ranking law.

## Success criteria

- [ ] Reader can define ranking (the Omnibus definition), default sort, relevance model, ranking policy, commercial adjustment, program-driven visibility and ranking transparency, and explain what a candidate is on each marketplace type.
- [ ] Reader can compare labels (click, gross booking, net booking, honored stay, problem-free stay) and justify a multi-task honored-stay target with dated evidence from Booking.com (2025), Airbnb (2023, 2025) and Expedia (2024).
- [ ] Reader can draw the five-component ranking function (Figure 1) and state each component's contract, including "the relevance model must not read commission".
- [ ] Reader can summarize the documented LTR record of Airbnb, Expedia Group and Booking.com with dates, and explain position bias, new-supply exposure, diversity and map-versus-list ranking.
- [ ] Reader can compare five designs for commercial influence and explain why multipliers are excluded.
- [ ] Reader can map P2B Art. 5, Omnibus Art. 7(4a) and Annex I 11a, DSA Arts. 17, 26, 27 and 38, DMA Art. 5(3) and CJEU C-264/23 to engineering consequences, and knows the CNMC (2024) and AGCM (2026) cases.
- [ ] The Corvane case runs from the Prinsenkade complaint and the ranking archaeology to Ranking Policy v1, with a worked search, an experiment table and a dated go-live, plus Nookaway's calendar-confidence alternative to a blanket demotion.
- [ ] The Hotels and Homes table and judgement say what to share (machinery) and what not to (models, policy values).

## Non-goals

- Retrieval, index design and the search pipeline: owned by [[stays-search-architecture]].
- Price caching, offer computation and price accuracy: owned by [[availability-engine]].
- Viewport search and geo indexing: owned by [[destinations-and-maps]].
- Personalization, sequence models and recommendations: owned by [[personalization-and-recommendations]].
- Funding and mechanics of member prices and promotions: owned by [[promotions-and-loyalty]].
- Experiment design and interference: owned by [[stays-experimentation]]; model governance: [[stays-ml-platform]].
- The full regulatory map: owned by [[stays-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The CNMC fine and its suspension rest on secondary reports (TechCrunch 2024, Hosteltur 2025); no ruling on the merits was found. Recheck before print.
- The AGCM investigation (22 April 2026) is open; update if it concludes.
- Whether a commission-uplift program is "payment specifically for achieving higher ranking" under Omnibus Annex I 11a, and whether an automatic reliability demotion triggers DSA Art. 17, are presented as the author's judgement, not settled law.
- The DSA designation list was checked on 21 October 2026 (Booking.com B.V. listed; Airbnb and Expedia not). Recheck before print.
- Booking.com's current ranking model and the mechanics of its paid programs are not public; the chapter cites only the disclosure page and dated sources.
- Nookaway's calendar-confidence analysis numbers are chapter-local illustrations; [[calendar-sync]] may refine them.

## Decision log

- **2026-10-21** — Opened with a partner complaint (Hotel Prinsenkade) and a dated "ranking archaeology" table rather than an algorithm survey, so Pay-to-Rank Creep is shown as accretion of individually reasonable rules. Reused the King's Day overbooking without changing ledger facts.
- **2026-10-21** — Made the honored stay the label and put reliability in the model's host-failure head, but kept commission and program effects in the policy layer. A value-weighted objective inside the model was rejected as undisclosable.
- **2026-10-21** — Defined Front Row v1 as "at most three positions, only past candidates less than 10% more relevant", so the effect of payment is a single sentence a partner and a regulator can read; reported the program revenue loss (−11%) beside the gains.
- **2026-10-21** — Recommended GBDT LambdaMART-style ranking as the default with conditions for moving to neural rankers, grounded in the Airbnb lineage and Booking.com's 2019 latency finding.

## Sources

- **Internal**
  - `_research/brief-search-discovery.md` Parts 1, 4 and 5 — ranking lineage, disclosure, regulation.
  - `_research/brief-booking-com.md` Parts 4–5 — "How we work", DSA, DMA, CNMC, CJEU.
  - `_research/brief-expedia-agoda-tripcom.md` Part 4 — Expedia LTR, Juggler, serving.
  - `_research/brief-airbnb.md` Part 5 — current stack and hosted-stays ranking properties.
  - `_research/brief-host-partner-guest-service.md` Part 3 — OTA partner programs; AGCM.
  - `_research/brief-trust-safety-regulation.md` Part 9 — DSA, DMA, P2B, Omnibus.
  - [[stays-search-architecture]], [[availability-engine]], [[inventory-integrity]], [[calendar-sync]], [[personalization-and-recommendations]].
- **External**
  - Booking.com, *How we work* (2025) — ranking signals and commercial factors.
  - Expedia Group Tech, *The Juggler Model* (2023) and *Channel-Smart Property Search* (2024) — business adjustments as a separate stage.
  - Airbnb ranking papers 2018–2026 — labels, position bias, diversity, maps, support need, interleaving.
  - Regulation (EU) 2019/1150, Directive (EU) 2019/2161, Regulation (EU) 2022/2065, Regulation (EU) 2022/1925 (official texts, fetched 21 October 2026).
  - AGCM PS13115 (2026) — Preferred Partner investigation.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed 9,225 to 8,500 words; renamed Visibility Plus to Front Row (name clash with LISTED); added tier commission and participant counts from the ledger; removed uncited sources. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
