---
status: accepted
revised: 2026-10-22
---

# Spec: Mapping the Business: Capability Maps for Two Marketplaces

## Intent

Give the reader a method and a worked result for mapping the business capabilities of an OTA-style accommodation marketplace and a hosted-stays marketplace side by side, and for deciding per capability what a group running both should share. The chapter walks the two Productscape reference models (TAM: Traveler Experience, Partner Operations, Marketplace Foundations; HSM: Guest Experience, Host Success, Marketplace Foundations) as **generic** models, never as descriptions of Booking.com or Airbnb, and without quoting their KPI values. It shows that matching must be by meaning (only five shared identifiers, one of which, `trst`, means different things), that the result is "one guest spine, two supply sides", and that the most important capabilities are the cross-cutting ones neither model draws. It names all seven [ADDED] capabilities from PLAN.md with the reason each was added. It ends with a three-grade sharing rule (shared engine, shared contract with separate engines, brand-specific) and Corvane's One Stay capability map, which hands off to the bounded-contexts chapter.

Productscape domains covered: **all** bricks of both models, at map level (34 TAM, 21 HSM), through the overlap matrix; the residuality stressors (`licn`, `insv`, `fire`/`evac`, `coho`) as map tests. [ADDED] capabilities named: content mapping, channel management for hosts, loyalty, notifications platform, tax engine, customer data platform, distribution and affiliates (plus the `domain-coverage` page).

## Audience

Group and enterprise architects, chief architects and CTOs of travel groups that own (or are acquiring) a second marketplace type, and product and engineering directors who must argue for or against sharing a capability.

## Success criteria

- [x] Reader can define capability, capability map, reference model, overlap matrix, and shared vs specific capability, including the shared-contract grade.
- [x] Reader can describe both reference models' structure and investment emphasis, presented as generic models with no KPI values and no real-company program names.
- [x] Reader can explain why matching by name fails (`trst`, `conn`/`apix`, `cald`/`cala`, pricing, payments) and state the overlap counts (12 same, 15 partial, 7 TAM-only, 3 HSM-only).
- [x] Reader can name all seven [ADDED] capabilities, the trace of each in the models, why it was added and the owning chapter.
- [x] Reader can test a map with its dependencies (the repaired spine) and with stressors.
- [x] Reader can apply the sharing decision rule and reproduce Corvane's 16 / 6 / 26 result for the 48-capability One Stay map.
- [x] Every company claim carries a dated source; the Expedia inference is labeled; Corvane numbers match the ledger.

## Non-goals

- Service and team boundaries, aggregates and context maps ([[stays-bounded-contexts]], [[organizing-stays-engineering]]).
- The full one-platform-or-two decision and its sequencing ([[converging-two-marketplaces]]).
- The supply model in depth ([[property-and-listing-model]]); each [ADDED] capability in depth (its owning chapter).
- Unit economics and metrics ([[stays-marketplace-economics]]).
- The brick-by-brick coverage table ([[domain-coverage]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company publishes its capability map; the "In practice" section relies on filings and engineering posts about what was consolidated. Revisit if Expedia or Booking.com publishes more on back-end supply consolidation.
- The TOGAF capability guide sits behind a login and is cited in paraphrase, as in LISTED.
- The 48-capability map is Corvane's; [[domain-coverage]] must stay consistent with the overlap counts here.

## Decision log

- **2026-10-21** — Organized the chapter around matching by meaning rather than a per-model walkthrough, because the models share only five identifiers and that mismatch is the chapter's main lesson.
- **2026-10-21** — Introduced a three-grade sharing rule (shared engine, shared contract, brand-specific) instead of LISTED's share/keep split, because the offer and reservation contracts in the ledger's One Stay scope need the middle grade.
- **2026-10-21** — Set the Corvane example in February–March 2027 (forum on 23 March, before the April board approval) and kept later decisions (place registry, offer kernel, payment arrangement) as forward references, to stay consistent with the ledger timeline.
- **2026-10-21** — Rejected quoting model KPI values or competitor statistics from the digest; used only VERIFIED facts from the briefs.

## Sources

- **Internal**
  - [[stays-bounded-contexts]], [[property-and-listing-model]], [[availability-engine]], [[content-and-media]], [[calendar-sync]], [[promotions-and-loyalty]], [[trip-and-messaging]], [[taxes-on-stays]], [[marketplace-intelligence]], [[demand-channels]], [[domain-coverage]].
  - `_research/productscape-digest.md` (all sections), `brief-expedia-agoda-tripcom.md`, `brief-booking-com.md`, `brief-airbnb.md`, `brief-payments-finance-tax.md`, `scenario-ledger.md`.
- **External**
  - Expedia Group 10-Ks FY2022, FY2023, FY2025 and Q1 2024 earnings release.
  - Booking Holdings FY2025 10-K; Booking.com Connectivity APIs documentation (n.d.).
  - Airbnb Engineering, "Pay as a Local" (2026) and "Scaling beyond one" (2026); Airbnb Q2 2026 shareholder letter.
  - The Open Group, TOGAF Series Guide: Business Capabilities (2022); Conway (1968); Lewis and Fowler (2014); O'Reilly, *Residues* (2024); DDD Crew, Core Domain Charts.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,869 to 8,495 words; the 16/6/26 map presented as capability map v1 (March 2027) with a pointer to v2 (49 = 23/6/20, December 2027) in converging-two-marketplaces; experimentation cell linked to the September 2027 standard; Expedia migration dates corrected (Hotels.com 2022, Vrbo 2023). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,167 → 5,187 prose words; opening now names the economics chapter it builds on and the bounded-contexts and convergence chapters that use it; 2 headings renamed (Concepts, Scoring Capabilities); 4 needless sentences cut; 4 paragraph openings made to state their point. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 5,167 → 4,844 prose words (HEAD → now, −6.3%); Concepts term table folded into one sentence; three rows of the differences table (availability truth, money, protection) merged into the "same name misleads" table; Failure Modes compressed to one-line bullets that point to their sections; repeated points cut from the lead, the five argued cells, the Scoring section and the Chief Architect's view; 4 needless paragraphs deleted. *(AI-mediated session)*
