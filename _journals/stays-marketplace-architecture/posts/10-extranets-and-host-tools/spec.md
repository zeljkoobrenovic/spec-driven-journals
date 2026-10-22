---
status: accepted
revised: 2026-10-21
---

# Spec: Running the Supply Side: Extranets, Host Tools and Operations

## Intent

Show that the hotel extranet and the host app are not front ends over their own data but clients of one partner back-end, and that the hard problems of the supply-side workspace are architectural: who owns each field when the extranet, a channel manager, a PMS and an assistant all write to it; how delegation to staff, co-hosts, cleaners and software is modeled; how reservation exceptions become owned work items; how turnover and access codes follow reservation changes; and why partner analytics must share metric definitions with ranking and programs. After reading, an architect can design or review a partner workspace and decide what a two-marketplace group should share across its supply products (the spine) and what it should keep separate (the products and supply editing).

Productscape domains covered: TAM `extr` (Partner Extranet), `rsrv` (Reservation Inbox & Operations), `perf` (Partner Performance Analytics); HSM `opco` (Turnover & Operations Coordination), `coho` (Co-host Network & Permissions), `host` (Host Performance & Earnings); residuality stressor HSM `coho`.

## Audience

Chief and principal architects, supply and partner-platform engineering leads, and product directors of extranets and host apps at OTAs, hosted-stays marketplaces and groups that run both. They know distributed systems; they need the supply-side domain and its failure modes.

## Success criteria

- [x] Defines extranet, host app, co-host, reservation exception, turnover task and partner analytics, and owns extranet, co-host, turnover task and partner analytics.
- [x] Presents a field-ownership table and the rule that human-tool overrides on connected supply are restrictive, expiring and logged, with the Miradouro closure as the worked case.
- [x] Presents a delegation model (party, target, role and scope, validity, separate money roles) grounded in Airbnb's documented co-host permission levels and the HSM `coho` residue, with the Alfama Keys worked example and payout arithmetic that matches the ledger's fee model.
- [x] Treats reservation exceptions as work items with owners, deadlines and escalation, using Booking.com's documented 30-minute fallback.
- [x] Explains turnover tasks and access codes as derived resources driven by versioned reservation events, and states a build-versus-ecosystem judgement.
- [x] Shows the architectural obligations of partner analytics and programs (shared metrics, explainable ranking, privacy of benchmarks, auditable eligibility; AGCM 2026).
- [x] Includes trade-off tables, the "Hotels and Homes" comparison with a sharing judgement, failure modes, the Chief Architect's view and design-review questions; four mermaid diagrams.
- [x] Every company claim is dated and sourced; inferences are labeled.

## Non-goals

- The reservation state machine and delivery protocols ([[reservation-lifecycle]], [[connectivity-and-channel-managers]]).
- Messaging and notification platform internals ([[trip-and-messaging]]).
- Authentication, sessions and the policy engine ([[identity-accounts-and-access]]).
- Extranet account takeover detection and the phishing-wave incident ([[travel-fraud]]).
- Commercial design of partner programs and loyalty ([[promotions-and-loyalty]]); ranking internals ([[stays-ranking]]); quality programs ([[reviews-and-reputation]]).
- Onboarding and verification flows ([[partner-onboarding]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source describes how Booking.com's extranet, Pulse and Connectivity APIs share a back-end, or how Expedia Partner Central works internally; the chapter labels its reference design as inference.
- Booking.com's extranet role model and current MFA enforcement for all partners are not documented in primary sources.
- No marketplace has published a turnover-scheduling system; the build-versus-ecosystem judgement rests on that absence.

## Decision log

- **2026-10-21** — Framed the chapter around "one partner back-end, many clients" and field ownership rather than a feature tour of extranet screens, because the documented API-versus-extranet rules (single channel of reply, PMS owns the lock) show the real design problem.
- **2026-10-21** — Used two Corvane incidents (shared logins exposed by a step-up rollout; a Partner Hub closure overwritten by a full sync) instead of reusing a ledger incident, because none of the recurring examples is about supply tools; the November 2027 phishing wave is referenced, not retold.
- **2026-10-21** — Chose "two products on a shared spine" as Corvane's decision, consistent with One Stay (shared identity, messaging, data; separate supply models and connectivity).
- **2026-10-21** — Kept turnover operations minimal in the marketplace and pushed professionals to the PMS ecosystem, since no primary source shows a marketplace-run cleaning system.

## Sources

- **Internal**
  - [[meet-corvane]], [[connectivity-and-channel-managers]], [[calendar-sync]], [[reservation-lifecycle]], [[identity-accounts-and-access]], [[travel-fraud]] — scenario and neighbouring ownership.
  - `_research/brief-host-partner-guest-service.md`, `brief-airbnb.md`, `brief-booking-com.md`, `brief-trust-safety-regulation.md`, `productscape-digest.md` (bricks `extr`, `rsrv`, `perf`, `opco`, `coho`, `host`).
- **External**
  - Airbnb Help Center articles 1243, 1534 (co-host permissions, fetched 21 October 2026), 1237, 4163, 829; Airbnb API Terms (2025); Airbnb newsroom (2024) and shareholder letters (2025, 2026).
  - Booking.com Connectivity API documentation (reservations, messaging, API list); Pulse page; Preferred Partner Programme page.
  - Expedia Group partner blog (2025) and EXPLORE 2024 release; Agoda Partner Portal announcement (2026) and Growth Program page (2025).
  - AGCM PS13115 (22 April 2026); KrebsOnSecurity (2024); Sophos/Secureworks (2023).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: renamed the Miradouro closure room type to "Twin" (ledger room types), named Courier and Gauge, American spelling, light trim to 8,494 words, timetoread 37. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
