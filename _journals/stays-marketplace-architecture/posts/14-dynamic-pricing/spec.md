---
status: accepted
revised: 2026-10-22
---

# Spec: Setting the Price of a Night: Revenue Management and Smart Pricing

## Intent

Answer the chapter's question: who sets the price of a night, with what data, and how much should the marketplace intervene? The chapter shows that the answer differs by marketplace type. Hotels price with their own revenue management, so an accommodation marketplace mostly receives prices, checks them and gives insight. Hosts rarely have a revenue manager, so a hosted-stays marketplace recommends prices and, with the host's consent, sets them. Once the marketplace writes prices, it owns a consequential model. That model needs a precedence resolver with provenance, a guardrail layer kept separate from the model, a measurement design based on holdouts, and a named owner who can freeze it. The chapter owns **revenue management**, **rate recommendation**, **comp set** and **smart pricing**.

Productscape domains covered: TAM `rate` (Rate Recommendation Engine: comp-set and demand models, guardrails); HSM `pric` (Pricing & Discounts: rules engine and pricing guidance layer).

## Audience

Chief architects, pricing and data/ML leads, and product and engineering directors at OTAs and hosted-stays marketplaces. They should leave able to decide what pricing role their marketplace takes, which components it needs, and how to govern a price-setting model.

## Success criteria

- [x] Defines revenue management, RMS, BAR, ADR, RevPAR, RevPAN, booking curve, comp set, smart pricing and rate recommendation, and expands every acronym.
- [x] Uses dated, sourced public evidence: IDeaS and Duetto (RMS), Airbnb 2015/2018 pricing papers, the Smart Pricing help page and the 2024–2025 tool figures, PriceLabs, Expedia Rev+ (secondary), the Agoda Partner Portal (2026), Airbnb's 2026 forecasting posts, and Booking.com's price-load bounds.
- [x] Presents a reference architecture with at least two diagrams: components, the precedence resolver and the daily recomputation with its guardrail gate.
- [x] Works through a Corvane example with numbers that match the ledger: the Smart Rate cut on the Santo António weekend during the ATC strike, the summer 2026 comparison, the Novaks' August price, and the €12 rate as a comp-set anomaly check.
- [x] Includes a trade-off table of marketplace pricing roles (pass-through, insight, recommendation, automatic, marketplace-set), with the author's judgement and the conditions under which it does not hold.
- [x] Includes a "Hotels and Homes" table and a clear judgement: share the demand layer, keep the engines separate, wall off Corvane Connect data.
- [x] Covers regulation and ethics: total price and drip pricing (EU, US, UK), Omnibus personalized-pricing disclosure, strikethrough prices, algorithmic-pricing coordination (*Gibson v. Cendyn*, 2025), and emergencies.
- [x] Covers model governance: owner, objective, shock replay, output monitoring, reversibility and review.

## Non-goals

- The ARI data model, rate plans and derived rates ([[rates-and-availability-model]]).
- Offer computation, price caching and price accuracy ([[availability-engine]]).
- Promotions, member prices, partner programs and rate parity ([[promotions-and-loyalty]]).
- Total-price display and the property page ([[property-page-and-room-selection]]).
- ML platform internals, feature stores and AI Act governance across models ([[stays-ml-platform]]).
- Experiment designs for marketplace interference ([[stays-experimentation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should Roomstead ever offer automatic pricing to Partner Hub hotels without an RMS, or should it stay advisory only?
- The EU competition-law position on marketplace price recommendations to competing hosts has no accommodation-specific case; revisit if one appears.
- Airbnb's current Smart Pricing model and recalculation cadence are not public; update if Airbnb publishes.
- The Expedia Rev+ details rest on secondary sources (2019, 2025).

## Decision log

- **2026-10-21** — Framed the chapter around "who writes the price" (precedence resolver plus provenance) rather than around pricing algorithms. The architectural risk lies in competing writers and missing governance, not in model choice.
- **2026-10-21** — Made the Corvane incident a *governance* failure (no cumulative cap, no shock hold during the ATC strike weekend) rather than a model-accuracy failure, and tied it to the ledger's ATC strike example.
- **2026-10-21** — Set the host's RevPAN as the objective and excluded acceptance rate as a success metric. Rejected occupancy or booking volume as targets, because they move the marketplace's interest into prices it sets for others.
- **2026-10-21** — Recommended sharing the demand layer across brands but not the pricing engine. A single group engine was rejected because it would reproduce The Hotel-Shaped Home.

## Sources

- **Internal**
  - [[rates-and-availability-model]], [[availability-engine]], [[inventory-integrity]] — upstream Part III chapters.
  - [[promotions-and-loyalty]] — next chapter; owns discounts and parity.
  - `_research/brief-availability-pricing.md` Parts 2, 11, 12; `brief-airbnb.md` Part 6; `brief-host-partner-guest-service.md` §2.2–2.4; `brief-platform-data-ml.md` §6.1; `productscape-digest.md` (TAM `rate`, HSM `pric`).
- **External**
  - Ye et al., "Customized Regression Model for Airbnb Dynamic Pricing", KDD 2018 — the booking-probability pricing model.
  - Airbnb Help Center article 1168 (Smart Pricing) — precedence and the emergency switch-off.
  - Airbnb Engineering, 2026 forecasting posts — structural breaks and the refit/respecify/hold choice.
  - *Gibson v. Cendyn Group*, Ninth Circuit, 15 August 2025 — algorithmic pricing and competition law.
  - FTC fees rule FAQ (2025), UCPD and its 2021 guidance, Omnibus Directive (2019) — price presentation and personalization.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,044 to under 8,500 words (condensed Airbnb/vendor evidence, the €12 recap and failure-mode repeats), fixed Hotel Miradouro pricing to match the ledger (RMS via PMS, not a spreadsheet), aligned model tiering with Kiln, verified Gibson v. Cendyn and the Agoda Partner Portal release. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,834 → 6,780 prose words; folded the third lead paragraph into the second; turned question and teaser openers (demand signals, second complaint, total price) into claims; trimmed restatements. No headings changed; spec unchanged. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 6,780 → 6,492 prose words (6,834 → 6,492 since HEAD, −5%; the converted Failure Modes table now counts as prose); Failure Modes table turned into one-line bullets pointing to the sections that handle each failure; Chief Architect's view compressed to the decisions not already argued in the body; marketplace-interest mechanism moved into In Practice Step 1 and the trade-offs bullet shortened; repeated Airbnb emergency quote dropped from the ethics section. No headings changed; spec unchanged. *(AI-mediated session)*
