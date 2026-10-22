---
status: accepted
revised: 2026-10-22
---

# Spec: Condition Changes Everything: Inspection, Damage Estimation and Reconditioning Cost

## Intent

Show chief architects how to capture vehicle condition and price it into buying, selling, lease-return and trade decisions. The chapter argues three things. Condition should be **stored as evidence and derived as views**: observations (photos with capture metadata and hashes, measurements) support findings located on a panel map, and grades, lessee charges, damage estimates and reconditioning costs are computed from confirmed findings by versioned rubrics. A **damage estimate is not a reconditioning cost**: insurer-grade estimating prices repair to pre-damage condition with manufacturer data, while recon cost prices what a given dealer will actually spend, and must be calibrated against linked actuals. **AI damage detection is a second opinion** with its own state, confidence and model version, measured on the platform's own confirmed findings because vendors publish no accuracy figures. After reading, the reader can design a condition service, its finding lifecycle, its image pipeline and its feed into the maximum purchase price without double-counting condition.

Productscape bricks covered: `dmgc` (Damage Calculation: capture UI, damage API, case store, estimating adapter) and the inspection part of `tapp` (Trade-in Appraisal Reports: guided capture, condition notes, photos). The appraisal composer and offer belong to [[vehicle-acquisition]].

## Audience

Chief and principal architects, product directors and data leads at dealer-software vendors, lessors, B2B trade platforms and vehicle-data companies. They know object storage, mobile sync and ML serving. They need the automotive specifics: wear versus damage, grading scales, estimating ecosystems, reconditioning economics, lease-return disputes and the Dutch BPM valuation-report rules.

## Success criteria

- [x] Defines the owned terms precisely: condition report, damage estimate, reconditioning cost, plus inspection, observation, finding and grade; separates evidence, findings and views.
- [x] Works the Fleetmoor return inspection with Axleby numbers (Q1 2027 baseline: 21% contested charges, 11.7% buyer claims; the Peugeot 308 with four derived views; Q4 2027 pilot results), consistent with the ledger and with [[b2b-trade-and-remarketing]] (8,600 Tradefloor sales in 2026, Handback prototype in October–November 2027) and [[vehicle-acquisition]] (rebuilt Appraise from June 2027).
- [x] Shows how condition enters the maximum purchase price twice (recon cost and recon time, using the €8.8 per car-day holding cost) and how the reconditionable/residual tag prevents double counting with [[valuation-engine]].
- [x] Gives an architecture (Gauge and Lotwise Inspect, shared by return centers, Appraise, the stock-in check and Handback) with components, a requirements table and three mermaid diagrams (finding lifecycle, components, condition-to-decision flow).
- [x] Uses dated, sourced public evidence (BVRLA, Manheim 2014, Cox/UVeye 2026, DAT FastTrackAI and weDAT, Solera Qapter, Tractable, ProovStation, CarDD 2022, CarMax and Carvana 2026, SRA 2026, RDW open data, GOV.UK MOT), states that no vendor publishes accuracy, and labels inference.
- [x] Covers failure handling: duplicate uploads and findings, conflicting inspections, incomplete inspections, wrong vehicle, provider outages, model updates, partial uploads, version changes mid-dispute, missing actuals.
- [x] Includes trade-off tables for capture and for pricing, and "Across Markets: What Changes by Country" with NL/BE, DE, UK, US.

## Non-goals

- Valuation methods, the valuation ledger and drift ([[valuation-engine]]); market data ([[market-data]]).
- The appraisal workflow, purchase offers and their expiry ([[vehicle-acquisition]]); the stock lifecycle and the reconditioning stage track ([[inventory-and-vehicle-dossier]]).
- Damage settlement procedures with lessees, B2B claim deadlines and auction hand-off ([[b2b-trade-and-remarketing]]).
- Battery state of health ([[ev-battery-health]]); fault codes and telematics ([[connected-vehicle-data]]); insurer damage records in history reports ([[vehicle-history]]).
- BPM calculation ([[registration-and-trade-services]]); retention policy in general ([[privacy-and-retention]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- BVRLA thresholds, NAAA grading guidelines and any Dutch or Belgian industry-wide lease-return standard were not read in primary form; the chapter treats return standards as licensed or customer-supplied rubric content.
- No vendor publishes damage-detection accuracy; revisit if one does.
- German lease-return expert practice and per-vehicle periodic-inspection data in Germany are marked as not verified.
- Whether Gauge findings may be shown to later owners or in consumer reports is left to [[data-licensing-and-governance]].

## Decision log

- **2026-10-22** — Built the scene on one car seen by three parties (lessor return, Tradefloor report, buying dealer) rather than on aggregate statistics alone, so the evidence-versus-grade problem is concrete and the four derived views can be shown on the same findings.
- **2026-10-22** — Named the repair-cost catalog provider generically in the Axleby example, because the ledger does not name one; real estimating vendors appear only in the documented-evidence sections.
- **2026-10-22** — Kept Handback (return settlement) and Appraise (appraisal and offer) as owners of their workflows and made Gauge, with Lotwise Inspect for capture, the shared evidence model and rubric engine, agreed with the parallel [[b2b-trade-and-remarketing]] and [[vehicle-acquisition]] chapters.
- **2026-10-22** — Introduced the reconditionable/residual tag to reconcile the valuation chapter's condition line with recon cost in the maximum purchase price, rather than changing the valuation chapter.
- **2026-10-22** — Verified Solera Qapter, DAT weDAT and UVeye by direct fetch of their own pages (the research brief could not); they are described only by their vendor statements.

## Sources

- **Internal**
  - [[meet-axleby]] — Fleetmoor, Tradefloor, cast.
  - [[valuation-engine]] — maximum purchase price, condition line, valuation ledger.
  - [[dealer-and-data-economics]] — holding cost per car-day, recon in front-end gross, vAuto variance.
  - [[inventory-and-vehicle-dossier]] — recon lines on the stock item, preparation track.
  - [[vehicle-history]] — report snapshots and versioning; summary events into Tracewell.
- **External**
  - BVRLA Fair Wear and Tear pages (n.d.) — wear versus damage; return inspection.
  - Manheim (2014), Cap HPI via Fleet News (2011), Auto Trader help center (2024–2026) — grading scales.
  - Cox Automotive/UVeye (2026), DAT FastTrackAI and weDAT (n.d.), Solera Qapter (n.d.), Tractable (n.d.), ProovStation (n.d.), CarDD (2022) — capture and detection.
  - SRA (2026) — BPM valuation reports and extra checks on claimed damage; RDW open data and GOV.UK MOT history — official inspection evidence.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: timetoread corrected to 35 min, "author's translation" wording, source group headings aligned with the house style. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
