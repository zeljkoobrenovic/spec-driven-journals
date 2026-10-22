---
status: accepted
revised: 2026-10-22
---

# Spec: Expedia Group and Vrbo: Consolidating Brands Onto One Platform

## Intent

Give the reader the most precisely documented public case of a group running both an accommodation marketplace and a hosted-stays marketplace, and consolidating them. The case traces Expedia Group's record from the 2020 platform operating model through the Hotels.com (2022) and Vrbo (2023) front-end migrations, One Key, the May 2024 guidance cut attributed to Vrbo's re-platforming, and the "shared platform infrastructure" of the FY2025 10-K. It reads Expedia's Rapid and lodging supply documentation as evidence of what did **not** converge: Vrbo's single-unit, single-rate-plan, pre-paid offer with payment schedules, deposits, rental agreements, host lead time, an uncached availability calendar, a "legacy Vrbo checkout" path and cancellation settling. It separates documented fact (with dates), the author's reading and labeled inference; states where the evidence stops; and ends with a comparison to the book's patterns and Corvane's One Stay choices, with a costed Corvane consequence (the Nookaway-to-Stayline migration guardrail).

Productscape domains covered: none as owner (case study). The case tests the overlap matrix: front end and loyalty (TAM `home`, `deal`, `acct`; HSM `insp`), checkout (`book` in both), inventory and calendar (TAM `invt`, `cald`; HSM `cala`), connectivity (TAM `conn`; HSM `apix`), payments (`paym`), distribution (the [ADDED] distribution and affiliates domain).

## Audience

Chief and group architects, CTOs and engineering directors of travel groups that own or are acquiring a second marketplace type and are being asked to "put the brands on one platform".

## Success criteria

- [x] Reader can date each consolidation step (2020, 2021, 2022, 2023, 2024 guidance cut, 2026 shared infrastructure) from primary filings.
- [x] Reader can state precisely what the filings claim was merged (front end, loyalty, named shared services) and what they do not claim (supply, inventory, pricing).
- [x] Reader can list the Rapid hotel-vs-Vrbo contract differences and explain the four that carry architectural information (calendar, payments, `merchant_of_record` routing, cancellation settling).
- [x] Reader sees the quarterly lodging-vs-hotel growth gap and understands what it does and does not prove.
- [x] Every inference about Expedia's internals is labeled; the evidence gaps are tabled.
- [x] The comparison maps each finding to a book pattern with a `[[link]]`, and to a Corvane choice consistent with the ledger and chapters 42, 43 and 45.
- [x] Article stays near 7,000 words including tables.

## Non-goals

- Re-teaching the convergence decision and the shared-core register ([[converging-two-marketplaces]]).
- Migration method, parallel runs and cohort design ([[modernizing-a-live-marketplace]]).
- Partner distribution API design ([[demand-channels]]) and Expedia's ranking lineage ([[stays-ranking]]).
- Vacation-rental history before 2015 ([[two-stay-marketplaces]]).
- Agoda and Trip.com ([[case-agoda-trip-com]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Vrbo's supply connectivity API and iCalendar import interval remain undocumented; revisit if Expedia publishes them.
- The Rapid Vrbo pages are undated; re-check the "legacy Vrbo checkout" routing and the 265k/650k figures before the next edition.
- Whether Expedia's 2026 lodging ranking service serves Vrbo results is not public.

## Decision log

- **2026-10-21** — Read the partner documentation as the primary evidence of non-convergence, rather than speculating about internals; the filings only say "front end" and "shared platform infrastructure".
- **2026-10-21** — Used the quarterly lodging-vs-hotel growth gap (Q4 2023 to Q4 2024 releases) as the only public quantitative trace of the Vrbo slowdown, and limited the claim to what the arithmetic supports.
- **2026-10-21** — Omitted "Setting the scene" and a separate "Hotels and Homes" section (case-study format); the hotel-vs-home contrast is the core of the partner-API section.
- **2026-10-21** — Added one costed Corvane consequence (Nookaway's 2028 move to Stayline with a seasonal freeze and a 3% brand guardrail) instead of re-describing One Stay.

## Sources

- **Internal**
  - [[converging-two-marketplaces]] — One Stay register, engine by segment, storefront by brand.
  - [[modernizing-a-live-marketplace]] — Stayline for Nookaway in 2028; host/listing cohorts.
  - [[demand-channels]] — Gangway and the decision not to distribute Nookaway before 2029.
  - [[property-and-listing-model]] — Costa Keys and pooled apartments.
  - `_research/brief-expedia-agoda-tripcom.md` — Parts 1–3, 5 and 8.
- **External**
  - Expedia Group 10-K filings FY2022–FY2025 and earnings releases Q4 2023–Q4 2024 (SEC EDGAR).
  - Rapid Vrbo integration guide, vacation-rentals overview and availability calendar (fetched 21 October 2026).
  - Expedia lodging supply hub, AR and Booking Notification introductions (© 2025, archived copies).
  - Expedia Group Technology posts, 2026 (platform engineering, ML principles, ranking stack, Spark table).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: One Stay map v2 totals corrected to 23/6/20 over 49; Vrbo calendar wording corrected to "should be called on page load"; American spelling; timetoread 31. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,390 → 5,274 prose words; Failure Modes compressed to one-line pointers to the sections that argue them; four restating sentences cut; headings unchanged. *(AI-mediated session)*
