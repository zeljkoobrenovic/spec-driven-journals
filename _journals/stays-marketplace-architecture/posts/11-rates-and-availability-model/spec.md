---
status: accepted
revised: 2026-10-21
---

# Spec: Rooms, Rates and Restrictions: The ARI Data Model

## Intent

Give the reader a precise, reusable model of availability, rates and inventory (ARI) for both marketplace types, and the judgement to keep it small. The chapter argues that most ARI "data" is really rules (derivations, audience discounts, fees, restriction semantics), that the fact store should hold only independent facts with source and version, and that one stay evaluator must interpret restrictions and price composition for search, the property page and checkout. It closes by showing that hotels and homes need different stores but can share one vocabulary and one evaluator contract.

Productscape domains covered: TAM `invt` (Rate and Availability Core), `room` (Room Plan Resolver, Rate Condition Comparison), `cald` (Restriction Policy Engine); HSM `cala` (availability engine, stay restrictions), `pric` (pricing rules engine, LOS rules).

## Audience

Chief and principal architects, supply and connectivity leads, pricing and search engineers at OTAs and hosted-stays marketplaces. They know data modeling and caching; they need the travel-specific semantics (pricing types, derived rates, restriction flavors, cancellation and fee inclusion) and a defensible position on where variants and rules should live.

## Success criteria

- [x] Defines ARI, inventory vs availability, rate plan vs product, pricing types (standard, derived occupancy, occupancy-based, LOS) and derived rate, with documented API sources.
- [x] Explains each restriction (stay-through and on-arrival MinLOS/MaxLOS, exact stay, CTA, CTD, stop-sell, advance purchase) and works a candidate-stay table showing their effect.
- [x] Shows that derivation order and rounding change prices, with a worked numeric example.
- [x] Covers the nightly calendar of a home: nightly price, LOS and lead-time discounts, cleaning fee, minimum nights, check-in days, gap nights, pricing precedence.
- [x] Compares storage models (per-date rows, ranges, LOS matrix, rules over base series) with Corvane sizing.
- [x] Corvane worked example: Hotel Miradouro's 37 rate plans pruned to 17 by a stated rule; Carmen's calendar fields; numbers agree with the ledger.
- [x] Includes a trade-off table, the "Hotels and Homes" section with table and a share/do-not-share judgement, failure modes, Chief Architect's view, 8–10 questions, and dated sources.
- [x] At least two mermaid diagrams with captions.

## Non-goals

- Ingestion protocols, message ordering, certification and the €12 rate incident in full ([[connectivity-and-channel-managers]]).
- iCal and API sync mechanics and conflict windows ([[calendar-sync]]).
- Offer computation at search scale, caching and price accuracy ([[availability-engine]]).
- Overbooking, allotments, holds and concurrency ([[inventory-integrity]]).
- How prices are set, RMS and smart pricing ([[dynamic-pricing]]); promotions, member pricing and parity ([[promotions-and-loyalty]]).
- Tax rules and calculation ([[taxes-on-stays]]); cancellation execution ([[changes-and-cancellations]]).
- The property, room type and listing entities ([[property-and-listing-model]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether the EU Price Indication Directive's 30-day prior-price rule applies to accommodation strikethrough prices is unresolved; the chapter does not rely on it.
- Airbnb's Smart Pricing vs rule-set precedence is described inconsistently across its own pages; the chapter cites only the help-center version and flags the inconsistency.
- No public source describes how Booking.com, Expedia or Airbnb store ARI internally; the reference architecture is labeled as inference.

## Decision log

- **2026-10-21** — Framed the chapter around "facts vs rules" rather than a field-by-field schema, because the architectural decisions (derivation, audience prices, evaluator) matter more than column lists and are where Rate Plan Sprawl and Price Drift start.
- **2026-10-21** — Gave Miradouro's 37 rate plans an explicit breakdown (11 independent, 26 derived; derivations in three places) and a pruning rule (conditions and content may be rate plans; audience may not), so the recommendation is testable; resulting 17 plans and 74 products are recorded in the ledger.
- **2026-10-21** — Recommended "share vocabulary and evaluator contract, not the store" for hotels and homes, consistent with the One Stay "shared contracts, separate engines" decision; full argument left to [[converging-two-marketplaces]].
- **2026-10-21** — Rejected normalizing all prices to one tax-inclusion basis at the edge; store as received with flags, because display rules differ by market.

## Sources

- **Internal**
  - [[property-and-listing-model]], [[connectivity-and-channel-managers]], [[calendar-sync]] — upstream entities and ARI messages.
  - [[availability-engine]], [[inventory-integrity]], [[dynamic-pricing]], [[promotions-and-loyalty]] — downstream consumers of the model.
  - [[meet-corvane]] and the scenario ledger — Hotel Miradouro, Carmen's calendar, Tally, Almanac, Pricegrid, ARI volumes.
- **External**
  - Booking.com connectivity documentation (n.d., fetched 2026) — pricing types, rate relations, restriction fields, product caps.
  - Expedia Group Availability and Rates API (© 2025) and Rapid (n.d.) — inventory per room type, pricing models, cancellation windows, Vrbo single-unit calendar.
  - Agoda Engineering, price cache (2026) — itinerary-keyed, write-dominated reading side.
  - Agoda Supply API and Google Hotel Prices ARI (n.d.) — OpenTravel restriction encoding and date semantics.
  - Airbnb Help Center articles 99 and 1168 (n.d.); Ye et al., KDD 2018 — homes calendar rules and pricing precedence.
  - FTC fees rule (2025), CMA DMCC Act (2025), EU Consumer Rights Directive (2011) and UCPD guidance (2021) — total price and cancellation backdrop.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,306 to 8,493 words (repetition in In Practice, failure modes, worked example), fixed the materialization/ARI-volume claim, removed an unsourced Airbnb documentation claim and an unverified Booking.com room-type cap, timetoread 35 min. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
