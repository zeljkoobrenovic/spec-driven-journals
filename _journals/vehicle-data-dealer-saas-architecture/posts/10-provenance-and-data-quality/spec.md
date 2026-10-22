---
status: accepted
revised: 2026-10-22
---

# Spec: Where Did This Fact Come From? Provenance, Freshness and Data Quality

## Intent

Show how a vehicle data and dealer SaaS platform knows, shows and governs the source, age, license and quality of every fact it sells. The chapter defines the provenance envelope (source, source class, source record and batch, observed-at, recorded-at, license, confidence, derivation, status, version) and argues that it is stored with the fact, with batch-level fields by reference. It teaches bitemporal facts (valid time vs transaction time) and the four kinds of change (new observation, late observation, correction, retraction). It sets freshness SLOs per data class and decision, splitting source lag from platform lag and introducing coverage-through for accumulating facts. It covers quality dimensions and accuracy against named ground truth, supplier data contracts with a commercial half (units, correction references, provenance fields, remedies), source scorecards, fact-level and dataset-level lineage (OpenLineage), and how provenance and license-driven attribution surface in reports, dossiers and API metadata. The reader should leave able to answer "what did we tell this client on that date, and why?" with a query.

Productscape bricks covered: `dgov` (lineage), `vidn` (specification facts with source lineage), `vhis` (history facts with source and date). [ADDED: data quality operations.]

## Audience

Chief architects, data platform leads and principal engineers at vehicle-data companies and dealer-software vendors who own fact stores, supplier relationships and data APIs, and who must defend sold facts to clients, consumers, courts and regulators.

## Success criteria

- [ ] Defines and owns provenance envelope, bitemporal fact, freshness SLO and data contract (vehicle); defines fact version, valid time, transaction time and source scorecard.
- [ ] Gives the envelope as a field table with reasons, a storage-cost comparison with labeled assumptions, and confidence tiers aligned with Anchor's identity tiers.
- [ ] Shows the four kinds of change and a worked bitemporal vehicle (MOT reading, wrong Kilometra version, correction) answering four as-of questions.
- [ ] Gives a freshness SLO table per data class with breach behavior, and separates source lag, pipeline lag and age at use.
- [ ] Shows a supplier contract excerpt that traces each clause to the Odometer Correction, consistent with consistency issue 17 (per-chain check, not the median gate).
- [ ] Works an Axleby example with ledger numbers (2,870 vehicles, 11 days, 96 consumer reports, 1,180 adverts) and the Rijnstaal re-run (six days vs 40 minutes).
- [ ] Includes failure handling, two trade-off tables, a requirements table, Across Markets with a table, the Chief Architect's view and Questions to ask; cites W3C PROV, OpenLineage, ODCS, ISO/IEC 25012, SQL:2011, GDPR Art. 5(1)(d), 16 and 19, DVSA, RDW and NMVTIS sources with dates.
- [ ] Two mermaid diagrams pass the render check; article under 8,000 words.

## Non-goals

- Landing, validation layers, entity resolution and survivorship rules: [[ingestion-and-entity-resolution]].
- Freshness and distribution monitors, the batch gate and alert routing: [[observability-and-data-operations]].
- History event types, odometer judgement and report wording: [[vehicle-history]].
- License register, purpose checks and access audit: [[data-licensing-and-governance]].
- The impact graph and correction propagation: [[journey-data-correction]].
- API metadata contract and webhooks: [[vehicle-data-apis]], [[events-webhooks-and-sync]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No vehicle-data company publishes a per-fact provenance or bitemporal model; the architecture is labeled as the author's inference. Revisit if a primary source appears.
- DVSA MOT data reuse terms beyond the documentation's Open Government License were not verified.
- The EU roadworthiness revision (2025/0097(COD)) was not adopted as of October 2026; update the Across Markets paragraph when it is.
- Storage figures for the envelope (2.5 billion fact versions, 600 vs 90 bytes) are assumptions.

## Decision log

- **2026-10-22** — Set the scene on a client's "what did you tell us on 17 May?" letter rather than on the Odometer Correction itself, so the chapter argues for transaction time from a dispute, and leaves detection to observability and propagation to the journey chapter.
- **2026-10-22** — Reused Anchor's four confidence tiers (Confirmed, Corroborated, Asserted, Suspect) for facts, so the book has one confidence vocabulary.
- **2026-10-22** — Separated provenance (internal truth) from attribution (what the license lets the product say), using the RDW open-data rule against attributing data to the RDW as the documented example.
- **2026-10-22** — Kept the machine-checkable contract and monitors in observability and added the commercial half of the supplier contract here, to avoid repeating the batch gate.

## Sources

- **Internal**
  - [[meet-axleby]], [[ingestion-and-entity-resolution]], [[vehicle-history]], [[vehicle-identity]], [[registers-and-official-data]], [[valuation-engine]], [[billing-and-metering]], [[observability-and-data-operations]], [[reliability-and-dependencies]], [[journey-data-correction]].
- **External**
  - W3C PROV-DM (2013); OpenLineage object model (v1.54.0); Open Data Contract Standard (Bitol); ISO/IEC 25012 via the ISO 25000 portal.
  - Fowler, "Bitemporal History" (2021); Kulkarni and Michels, "Temporal features in SQL:2011" (2012).
  - GDPR Art. 5(1)(d), 16, 19 (CELEX 32016R0679).
  - DVSA MOT history API specification and bulk download page; RDW open data metadata and terms; Car-Pass FAQ; KBA; 28 CFR 25.54–25.56; DOJ NMVTIS consumer page; Council text ST 15613/25.
  - Auto Trader UK help centre (forecast accuracy, 2024, updated 2026); Carfax (archived 2025); AutoScout24 DataRunner (2023).
  - Research briefs: `brief-platform-apis-operations.md` (Parts 3, 7, 8), `brief-specification-history.md` (Parts 2.3, 3), `brief-connected-data-privacy-regulation.md` (Parts 5, 7, 8).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: register freshness target aligned with the daily snapshot model, worked vehicle's import date fixed to precede its May 2027 calls, acronyms expanded. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: envelope example's value_as_delivered for version 2 now carries unit mi (version 1 carried km, the error); American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
