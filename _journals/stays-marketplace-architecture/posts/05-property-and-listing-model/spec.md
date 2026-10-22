---
status: accepted
revised: 2026-10-21
---

# Spec: Hotels and Homes: Modeling What Is Being Sold

## Intent

Give the reader one supply model that works for both marketplace types: a physical layer (property, unit, spaces, beds) that both share, and a commercial layer that differs (room type, rate plan and product on the OTA side; listing on the hosted-stays side). The chapter must show why the unit is the identity that regulation, integrity and recovery need even where an OTA sells room-type pools, how occupancy, beds, attributes, location, policies, identifiers and versions attach to the right level, and what a group running both marketplaces should share (identifiers, vocabulary, taxonomy) and keep separate (the commercial models and their inventory engines). After reading, an architect can audit their own schema for attributes on the wrong level and for missing unit identity.

Productscape domains covered: TAM `invt` (supply core, supply integrity controls), TAM `cont` (content and policy studio: property content, room setup, amenities, policies); HSM `lista` (listing authoring and content). Gap filled: **property, unit and room-type catalog (system of record)**, which neither model has as a brick.

## Audience

Chief and principal architects, supply and connectivity leads, and engineering directors of OTAs, hosted-stays platforms, channel managers and vacation-rental PMS vendors who own or depend on the supply schema, and group architects deciding what two marketplaces should share.

## Success criteria

- [ ] Reader can define property, unit, room type, rate plan, product and listing, and say which layer (physical or commercial) each belongs to.
- [ ] Reader can explain the pool-versus-specific-unit difference and its consequences for inventory counting, recovery and regulatory reporting.
- [ ] Reader can model rooms within a home and multi-unit listings over shared units without independent calendars.
- [ ] Reader can place occupancy, beds, amenities, location fields and policies on the correct level, and state the rule that commercial occupancy may only narrow physical occupancy.
- [ ] Reader can state identifier rules (opaque, never recycled, issued by the owning system, external codes as cross-references) and the three versioning mechanisms (content versions, booking snapshots, effective-dated eligibility).
- [ ] Reader can compare four modeling options for a two-marketplace group and justify a shared physical core with separate commercial models, including when it is not worth it.
- [ ] Every company claim carries a dated source; inferences about internals are labeled; the Corvane example matches the ledger.

## Non-goals

- Rate plans in depth, restrictions, LOS and derived pricing, ARI storage ([[rates-and-availability-model]]).
- Content authoring, media pipeline, translation and cross-supplier property/room mapping ([[content-and-media]]).
- Connectivity messages, certification and reservation delivery ([[connectivity-and-channel-managers]], [[reservation-lifecycle]]).
- iCal and multichannel calendar sync ([[calendar-sync]]).
- The legal detail of STR registration and data sharing ([[stays-regulation]]); onboarding and readiness checks ([[partner-onboarding]]).
- The full one-platform-or-two decision ([[converging-two-marketplaces]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Airbnb's internal listing schema and Booking.com's internal storage of homes are not public; the chapter uses only partner-facing documentation as evidence of the problem. Revisit if either publishes engineering material.
- The Booking.com RMA code-normalization statement and PCT extensions were read from undated documentation in October 2026; re-check before a print edition.
- Whether OpenTravel-based reservation-modification messages carry unit assignment reliably across channel managers was not verified; the chapter presents unit assignment flow as design, not as documented practice.

## Decision log

- **2026-10-21** — Chose a two-layer model (physical vs commercial) as the organizing idea over a per-marketplace walkthrough, because it explains both the Hotel-Shaped Home failure and the convergence cases with one concept.
- **2026-10-21** — Chose the EU STR Regulation's per-unit reporting (Spain, after the 2026 Supreme Court ruling) as the Corvane trigger, because it forces the unit question on the OTA side with documented law rather than an invented incident.
- **2026-10-21** — Introduced a fictional manager, Costa Keys (Málaga, 38 apartments), and a group place registry decided on 12 May 2027, recorded in the scenario ledger; rejected "every apartment its own room type" and "listing model for both" as the alternatives in the trade-off table.
- **2026-10-21** — Kept rate plans brief and pointed to chapter 11, to avoid re-teaching ARI.

## Sources

- **Internal**
  - [[stays-bounded-contexts]] — supply context, offer and reservation aggregates.
  - [[rates-and-availability-model]], [[content-and-media]], [[stays-regulation]], [[reservation-lifecycle]] — neighbours this chapter hands off to.
  - `_research/brief-supply-connectivity.md`, `brief-availability-pricing.md`, `brief-expedia-agoda-tripcom.md`, `brief-trust-safety-regulation.md`, `productscape-digest.md` (§4.2, §5, §7.4, §10).
- **External**
  - Booking.com Connectivity documentation (room types, rate plans, roomrates, PCT and RMA code lists, amenities sunset for homes), n.d., read October 2026.
  - Expedia Group, Availability and Rates API introduction (2025) and Rapid Vrbo integration guide (n.d.).
  - Regulation (EU) 2024/1028 (CELEX 32024R1028) and the CGPJ note on Spanish Supreme Court judgment 620/2026.
  - Airbnb Tech, "Scaling beyond one" (2026); Airbnb Q2 2026 shareholder letter; Booking Holdings and Expedia Group FY2025 10-Ks.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed to under 8,500 words; separated the place registry from Waypoint (Waypoint writes geo enrichment to registry records) and linked the registry to capability map v1/v2; aligned the boutique-hotel pilot with the December 2027 routing decision; American spelling and quote fixes. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
