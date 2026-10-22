---
status: accepted
revised: 2026-10-22
---

# Spec: What Is It Worth? Building and Governing a Valuation Engine

## Intent

Show chief architects how to build a valuation engine whose answers dealers, lessors and data clients can act on, and which stays honest when one market segment moves. The chapter argues three things. A valuation is a **typed, evidenced answer**: value type, basis, range, confidence flag, adjustment lines, comparables and model version, with "no valuation" as a legitimate result. The **valuation ledger**, linked to the offers, purchases and sales that follow, is the backbone for accuracy, explanation, correction and evidence. **Drift must be monitored per segment with leading indicators**, because realized sale prices arrive a stock turn late, and automated buying decisions need a per-segment circuit breaker. After reading, the reader can define the contract, the ledger schema, a back-test suite and a segment drift policy for their own engine.

Productscape bricks covered: `valu` (Valuation Engine: valuation API, calculator, model store, valuation ledger). It touches `occm` (pricing advisor), `tapp` (appraisal composer) and `bpmc` (BPM's dependency on market value) only as consumers.

## Audience

Chief and principal architects, data and ML leads, and product directors of vehicle-data companies, dealer-software vendors, portals and lessors who own or buy valuations. They know ML serving and event streams. They need the automotive specifics: value types, maximum purchase price, guide-value licensing, ground-truth scarcity in Europe, and the 2021–2024 price shocks as drift evidence.

## Success criteria

- [x] Defines the owned terms precisely: valuation ledger, maximum purchase price, valuation confidence, back-test; distinguishes the value types with published definitions (KBB, Auto Trader UK, DAT).
- [x] Works the EV Overvaluation (2026: 9.5% average, 14 weeks) with ledger-consistent numbers and a clear mechanism: global metric dilution, outcome lag of a stock turn (58 days), equal-weight training window.
- [x] Gives an architecture with components, a requirements table (latency, freshness, consistency, availability per interaction) and three mermaid diagrams.
- [x] Uses dated public evidence (Manheim MMR 2026 and MUVVI methodology 2023, KBB, Auto Trader 2023–2026, DAT 2024, Cox 2022, Hertz 2024, Zillow 2021–22, Carvana 2026), states Auto Trader's accuracy caveat, and labels inference about real companies.
- [x] Covers failure handling: duplicates, conflicting inputs, incomplete records, thin evidence, cloud-link and provider outages, partial batch failures, corrected inputs (Odometer Correction), segment drift.
- [x] Compares sourcing approaches in a trade-off table and states the conditions for the hybrid.
- [x] Includes "Across Markets: What Changes by Country" with NL/BE, DE, UK, US and a judgement on common versus market-specific parts.
- [x] Includes the EU AI Act position (Annex III point 5, Article 4, Article 113 dates) with an explicit counsel caveat.

## Non-goals

- Advert harvesting, sale detection, stand-time and the database-right case law ([[market-data]]).
- Condition capture, damage estimation and reconditioning cost ([[condition-and-damage]]); battery state of health measurement ([[ev-battery-health]]).
- The appraisal workflow, offers and their expiry ([[vehicle-acquisition]]); setting and changing retail prices ([[used-car-pricing]]).
- Specification resolution and option catalogs ([[specification-and-equipment]]); odometer judgements ([[vehicle-history]]).
- BPM calculation methods ([[registration-and-trade-services]]); the full correction journey ([[journey-data-correction]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No provider publishes segment-level error against transaction prices; the chapter says so. Revisit if one does.
- ~~The AI Act timetable may change through the Digital Omnibus~~ Resolved 2026-10-22: Regulation (EU) 2026/1744 adopted; dates updated to 2 December 2027 (Annex III) and 2 August 2028 (Article 6(1)).
- Belgian valuation providers and any regulatory use of values in Belgium were not verified.
- Whether battery-passport state-of-health data will be accessible to valuation providers is owned by [[ev-battery-health]].

## Decision log

- **2026-10-22** — Set the scene as a January 2027 review of the 2026 EV Overvaluation, with an April 2027 replay of the window, rather than a new 2027 incident, because the ledger assigns that incident to this chapter and it carries all three key points.
- **2026-10-22** — Explained the 14 weeks by three mechanisms (global metric dilution, a stock turn of outcome lag, equal-weight training) instead of "the model was bad", so the fix is architectural: segment monitors, leading indicators, circuit breakers.
- **2026-10-22** — Kept the nightly stock recomputation of about 350,000 cars out of the ledger, as stock signals, to agree with the editor's ledger note on valuation counts.
- **2026-10-22** — Treated Vantage as consuming Tracewell's derived odometer rather than the dealer's raw entry, to agree with [[vehicle-history]].

## Sources

- **Internal**
  - [[meet-axleby]] — Vantage, the EV Overvaluation, cast and volumes.
  - [[vehicle-history]], [[specification-and-equipment]] — odometer judgement and edition confidence as valuation inputs.
  - [[dealer-and-data-economics]] — valuation error relative to dealer gross.
  - [[case-auto-trader-uk]], [[case-cox-automotive]] — public valuation businesses.
- **External**
  - Manheim, *MMR Help* (2026) and *Used Vehicle Value Index methodology* (2023) — method, sparse-data rule, outliers.
  - Kelley Blue Book, *Definitions of our values* (n.d.) — value types, Instant Cash Offer.
  - Auto Trader UK help center (2024–2026) and results releases (2023, 2026) — API surface, exclusions, accuracy caveat, ML valuations.
  - Auto Trader Retail Price Index releases (2022–2024); Cox Automotive MUVVI releases (2022, 2024) — drift evidence.
  - DAT, *Produktbeschreibung SilverDAT valuateFinance* (2024) — method and disclaimer.
  - Hertz 8-K (2024); Zillow 8-K and 10-K (2021–22); Carvana 10-K (2026); Vroom (2024) — cautionary analogues.
  - Regulation (EU) 2024/1689 (AI Act) — Annex III point 5, Articles 4 and 113.
  - Madhusudhanan et al., *ProbSAINT* (2024) — uncertainty in used-car pricing.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: AI Act high-risk dates updated to Regulation (EU) 2026/1744 (2 December 2027 / 2 August 2028), Appraise rooftop count corrected to about 4,800, old sources flagged, VRM expanded. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: One Dossier question put to the company board (March 2027), not an architecture board, which first met in April 2027. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
