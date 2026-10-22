---
status: accepted
revised: 2026-10-22
---

# Spec: Remembering the Traveler: Personalization, Recommendations and Saved Intent

## Intent

Chapter 19 of BOOKED, in Part IV (Discovery). It answers: how do stays marketplaces personalize a rare, high-stakes purchase, and what architecture keeps saved intent useful and honest? The chapter argues that the unit worth modeling is the **trip intent**, not the user profile. Saved intent (wishlists, saved searches, price alerts) is a promise about price and availability, so every alert and recommendation must be re-priced as a total through the live pricing path. Personalization must prove its value with holdouts, and keep a maintained non-profiling path. The reader leaves with a component model (intent capture, trip intent store, embeddings and candidate generation, recommendation service, alert evaluator), the rules for alerts, and a view on what a two-brand group should share.

Productscape domains covered: TAM `pers` (Personalization & Recommendations), `ssav` (Saved Searches & Price Alerts), `home` (Session Recall and Intent Recovery); HSM `wish` (Wishlists & Sharing), `insp` (intent recovery and recirculation).

Owns: **trip intent**, **wishlist**, **price alert**, **listing embedding**.

## Audience

Chief architects, search and relevance leads, ML and data platform leads, and product directors of OTAs and hosted-stays marketplaces who must decide who owns saved intent, how recommendations are priced and measured, and what to share across brands.

## Success criteria

- [ ] Reader can define trip intent, wishlist, price alert and listing embedding, and explain why trip intent beats the user profile for stays.
- [ ] Reader can draw the five-component personalization architecture and state the two key boundaries (intent store holds no prices; recommendations are enriched with live prices before display).
- [ ] Reader can design a price alert evaluator (poll vs event-triggered) with the seven rules, and size its load on the pricing path using the Roomstead example.
- [ ] Reader can explain cold start for guests (group signals, proximity features) and for listings (content vectors, neighbor initialization, exposure policy), with dated sources.
- [ ] Reader can map GDPR, ePrivacy, DSA Articles 27 and 38, and the Omnibus personalized-price disclosure to concrete system requirements.
- [ ] Reader can set up a holdout that separates incremental bookings from attributed ones (Nookaway 5% alert holdout).
- [ ] The Novak worked example matches the ledger (€145 × 7, €70 cleaning, €130.20 fee, €56 tax, €1,271.20, 25%).
- [ ] The "Hotels and Homes" table is specific (what is saved, what changes, substitutes, cold start, repeat behavior) and ends with a share/not-share judgement.

## Non-goals

- Search pipeline, flexible search and index design: [[stays-search-architecture]].
- Learning to rank, position bias, ranking transparency and program-driven visibility: [[stays-ranking]].
- Total price display, drip pricing and fee disclosure: [[property-page-and-room-selection]].
- Notification channels, routing and messaging: [[trip-and-messaging]].
- Traveler profiles, accounts and Corvane ID: [[identity-accounts-and-access]].
- Feature platforms and model governance: [[stays-ml-platform]]; experiment methods for delayed outcomes: [[stays-experimentation]].
- Member pricing and loyalty: [[promotions-and-loyalty]]; landing pages and metasearch: [[demand-channels]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether any OTA (Booking.com, Expedia, Agoda, Trip.com) has published how price alerts or saved searches are evaluated; none was found, so the alert evaluator designs are labeled as the author's reference architecture.
- Airbnb's 2018 embedding paper body (training data sizes, cold-start method) could not be fetched; the chapter cites only its abstract-level claims and describes neighbor initialization as industry practice.
- Whether Corvane's Roomstead crosses the DSA very-large-platform threshold is deliberately left open; the chapter recommends the non-profiling path regardless.

## Decision log

- **2026-10-21** — Framed the chapter around trip intent rather than user profiles, because the documented evidence (Booking.com's continuous cold start, Airbnb's guest-journey work) shows the current trip carries most of the signal in stays.
- **2026-10-21** — Made "no unpriced promise" the central architectural rule, linking saved intent to the Price Drift and Phantom Availability failure patterns, rather than treating alerts as a CRM feature.
- **2026-10-21** — Corvane decision: share the trip intent store, alert evaluator and notification platform under One Stay; keep recommendation models per brand; cross-brand intent only by guest-chosen linking. Rejected one shared recommender because supply models differ (The Hotel-Shaped Home).
- **2026-10-21** — Cut a documented-record timeline table and a batch/streaming comparison table to stay within length; the evidence remains in the prose.

## Sources

- **Internal**
  - [[stays-search-architecture]], [[stays-ranking]], [[property-page-and-room-selection]], [[trip-and-messaging]], [[identity-accounts-and-access]], [[stays-ml-platform]], [[stays-experimentation]], [[stays-regulation]], [[inventory-integrity]], [[global-scale-and-reliability]].
  - `_research/brief-search-discovery.md` (Part 6), `brief-airbnb.md` (Part 5), `brief-platform-data-ml.md` (Part 6), `productscape-digest.md` (`pers`, `ssav`, `home`, `wish`, `insp`), `scenario-ledger.md` (worked example 10).
- **External**
  - Airbnb: Grbovic and Cheng (KDD 2018); Haldar et al. (2020); Tan et al. (2023); Abdool et al. (2026); Zha et al. (2026); Hou et al. (2026, Chronon real-time); Jiang et al. (2026, proximity features).
  - Booking.com: Bernardi et al. (2015, continuous cold start); KDD 2019 lessons (Colyer summary); Recommendation Platform enrichment (2025); "How we work" (2025).
  - Expedia Group: property-search learning to rank (2024).
  - EU law: DSA Arts. 3(s), 27, 38; GDPR Arts. 4(4), 9, 21; ePrivacy Arts. 5(3), 13(2); Omnibus Directive recital 45.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: light trim 8,927 to 8,885 words; fee-revenue estimate now uses the realized 14.4% take rate. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,204 → 6,761 prose words; opening now places the chapter in Part IV between ranking and the property page; Failure Modes trimmed to the three failures not covered earlier; Chief Architect's view condensed; no headings renamed. *(AI-mediated session)*
