---
status: accepted
revised: 2026-10-21
---

# Spec: From Sign-Up to First Booking: Partner and Host Onboarding

## Intent

Chapter 6 of BOOKED (Part II, SUPPLY). It answers: how do properties and hosts join a stays marketplace, get verified and become bookable? It argues three things. First, onboarding creates master data about supply, so the platform should model party, supply unit, authority and payout account as separate records. Second, verification gates should be ordered by the harm they prevent: guest-protecting checks before activation, money checks before payout, billing checks before invoicing. Third, activation is a continuous, explainable decision made by a readiness service over named, versioned checks, and it can run backwards. The chapter owns **activation**, **readiness check** and **KYB for partners**. After reading, an architect can design the gates, the activation state machine and the activation API for both marketplace types and say what a group should share.

Productscape domains covered: TAM `onbo` (Partner Onboarding & Verification); HSM `hono` (Host Onboarding & Verification). It also touches the gap the digest names: a partner master record with legal hierarchy and contract terms.

## Audience

Chief architects, principal engineers and supply or trust engineering leads at OTAs and hosted-stays platforms. They know distributed systems but may not know KYB, DAC7, DSA trader traceability or STR registration duties. They should leave with a gate model, a readiness-service design and an API checklist they can take into a design review.

## Success criteria

- [ ] The supply-party model (party, supply unit, authority, payout and billing account) is defined, and the chapter explains why the records must stay separate.
- [ ] KYC, KYB, right to sell, tax identity and registration numbers are defined, with dated regulatory sources (AMLD/AMLR, DSA Article 30, DAC7, Regulation (EU) 2024/1028, the Spanish Supreme Court ruling, NYC Local Law 18).
- [ ] A gate table ties each check to the harm it prevents and to what it must hold before (bookable, first payout, first invoice).
- [ ] An activation state machine with reason codes, and a readiness-service contract with owners, severity, versions and three evaluation triggers.
- [ ] Activation API design rules, including per-unit results and partial success for bulk.
- [ ] Documented examples are dated and sourced: Booking.com property statuses and check-then-open flow, its 2026 onboarding agent; Airbnb verification and the new-host payout timing; the 2023–2025 partner-account takeover campaigns.
- [ ] Corvane worked examples agree with the ledger: Hotel Torre de Ferro (9 days to 2) and Carmen's re-verification; the 340-unit Maré Alta bulk migration with 41 blocked units.
- [ ] Trade-off tables, a "Hotels and Homes" comparison table with a sharing judgement, Failure modes, Chief Architect's view and Questions to ask.

## Non-goals

- Property, room-type and listing data model: [[property-and-listing-model]].
- Content quality, media and duplicate or property mapping: [[content-and-media]].
- Connectivity protocols and certification of channel managers: [[connectivity-and-channel-managers]].
- Day-to-day extranet and host tools, co-host roles: [[extranets-and-host-tools]].
- Fraud typology and detection models: [[travel-fraud]]; identity levels and IAM: [[identity-accounts-and-access]].
- The full regulatory map and market policy registry design: [[stays-regulation]]; tax reporting content: [[taxes-on-stays]]; payout mechanics: [[payouts-and-settlement]].
- New-listing ranking cold start: [[stays-ranking]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Booking.com's location-verification procedure for new properties is a help topic that was not read; the chapter does not describe it.
- Booking.com status names such as "SB: Pending Fraud Blacklist check" are listed without definitions; the chapter uses them only as evidence that such states exist.
- Whether verification of payee can be relied on for platform payout batches depends on each PSP's offering; the chapter treats it as one input at account setup.
- National registration rules (Andalusia, Portugal) were not verified in detail; the Maré Alta example avoids stating Portuguese law.

## Decision log

- **2026-10-21** — Framed onboarding around risk-ordered gates, not funnel steps, because the contract's "readiness checks" and "fraud at onboarding" only make sense when each check is tied to a harm. A funnel-optimization framing was rejected as duplicating the economics chapter.
- **2026-10-21** — Used Carmen's 2027 re-verification as the hosted-stays example, because Carmen has been on Nookaway since 2019 (ledger). A fresh sign-up would have contradicted the ledger.
- **2026-10-21** — Added a fictional bulk migration (Maré Alta Stays, 340 units) to cover "professional host migration in bulk" and the activation API with per-unit results.
- **2026-10-21** — Recommended sharing the supply-party layer (verification, party records, readiness service, policy registry) across brands while keeping separate funnels. This is consistent with One Stay's "supply models not shared" scope, because party verification is not the supply model.

## Sources

- **Internal**
  - [[property-and-listing-model]], [[stays-regulation]], [[travel-fraud]], [[identity-accounts-and-access]], [[payouts-and-settlement]], [[taxes-on-stays]], [[meet-corvane]] — neighbour contracts and terminology.
  - `_research/brief-host-partner-guest-service.md`, `brief-trust-safety-regulation.md`, `brief-supply-connectivity.md`, `brief-booking-com.md`, `brief-payments-finance-tax.md`, `productscape-digest.md` (bricks `onbo`, `hono`, stressor `licn`).
- **External**
  - Booking.com Connectivity documentation: property statuses, preparing a property to be open/bookable, OTA_HotelSummaryNotif, understanding payouts (fetched 2026-10-21).
  - Barchukova et al., *From Static Help Content to a RAG-Based Onboarding Agent for Partners*, booking.ai, 2026.
  - Airbnb help articles 1237 and 2909; Airbnb FY2025 10-K; *An update on identity verification*, 2023.
  - Regulations (EU) 2024/1028, 2022/2065, 2024/1624, 2024/886; Directives (EU) 2021/514 and 2015/849.
  - Secureworks (2023), Krebs on Security (2024), Microsoft Threat Intelligence (2025) on partner-account takeover.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed to 8,499 words, added the "From Onboarding to Content" hand-off heading, tied the supply-party recommendation to capability maps v1/v2, dated the Spanish removals, expanded acronyms, American spelling, verified Booking.com statuses, Airbnb payout terms and the Spanish Supreme Court ruling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
