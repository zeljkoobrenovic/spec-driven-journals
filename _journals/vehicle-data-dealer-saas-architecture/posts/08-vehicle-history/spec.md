---
status: accepted
revised: 2026-10-22
---

# Spec: What Happened to This Car: Damage, Odometer, Title and Service History

## Intent

Answer the chapter question from PLAN.md: **how do you assemble a vehicle history that buyers and dealers can rely on?** The chapter argues for three moves. First, store history as typed, sourced, dated, person-free events per vehicle. Second, compute judgements (odometer judgement, damage summary, title-brand summary) as versioned derived views with source-trust rankings. Third, issue every report as a stored, dated snapshot with explicit coverage and cautious wording, so corrections can supersede it. After reading, an architect can design or review the history event store, the assembler, the rollback rule and the report discipline, and can tell "no record found" from "clean".

The chapter owns **history event**, **history report**, **odometer judgement** and **title brand**. Productscape brick covered: **`vhis`** (Vehicle History Intelligence: history report view, history API, history assembler with the no-damage-no-charge rule, history store).

## Audience

Chief architects, principal engineers and data leads of vehicle-data providers and dealer-software vendors who build or buy history data. They know event stores and fan-out; they need the domain: what each event type means, how sources differ by country and trust, why rollback detection produces false positives, and how wording and liability shape the data model.

## Success criteria

- [ ] Defines history event, history report, odometer judgement and title brand precisely, with the event-type table (assertion, sources, permanence, volatility).
- [ ] Explains the RDW's three-state odometer judgement from primary sources, and why a commercial history service cannot reuse the naive "any decrease" rule.
- [ ] Gives a classifying rollback rule (unit artefact, isolated outlier, country hop, sustained step-down) with a worked Axleby example and a state diagram.
- [ ] Shows the Tracewell architecture (connectors, event store, judgement engine, assembler, snapshot store) with at least two mermaid diagrams and a requirements table per interaction.
- [ ] Treats "no record found" vs "clean" as a three-valued data-model problem, with a wording table.
- [ ] Defines hit classes for no-hit-no-fee and links the No-Hit Credit without retelling it.
- [ ] Covers failure handling: duplicates, wrong-vehicle events, conflicts, incomplete history, batch errors, late data, fan-out partial failure, outages, register corrections.
- [ ] Contains a specific, sourced "Across Markets" table (NL/BE, DE, UK, US) and a judgement on common core vs market adapters.

## Non-goals

- Plate/VIN identity and the Cloned Plate fix ([[vehicle-identity]]).
- Register access regimes, provider obligations and the register gateway ([[registers-and-official-data]]).
- Generic ingestion, quarantine and entity-resolution mechanics ([[ingestion-and-entity-resolution]]).
- Bitemporal modeling and provenance envelope in depth ([[provenance-and-data-quality]]).
- The end-to-end Odometer Correction journey ([[journey-data-correction]]).
- Consumer product design and funnel ([[consumer-vehicle-checks]]); metering mechanics ([[billing-and-metering]]); license enforcement ([[data-licensing-and-governance]]); retention and erasure ([[privacy-and-retention]]); connected-car access ([[connected-vehicle-data]]); condition inspections and damage estimation ([[condition-and-damage]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The final text of the EU roadworthiness revision (2025/0097(COD)) and its odometer article was not public; revisit when adopted.
- How Dutch insurers report total losses to the RDW, and the legal basis of the WOK status, were not verified.
- UK write-off categories rest on a secondary source; the ABI code of practice was not read.
- German third-party access to KBA odometer readings was not verified; the chapter relies on the RDW's 2026 statement that German readings are registered and checked comparably.
- Carfax's full Buyback Guarantee terms were not readable; only the archived "About" page wording is used.

## Decision log

- **2026-10-22** — Chose the dealer's own mistyped appraisal reading (Sietse Brandsma's Volvo) as the scene, over a supplier error, because it shows first-party data as a history source and complements the Odometer Correction (a supplier batch error owned by `journey-data-correction`).
- **2026-10-22** — Recommended showing the register's judgement and the platform's own signal side by side, rather than either alone, because the RDW judgement carries legal weight but cannot see commercial, foreign or first-party readings.
- **2026-10-22** — Kept privacy to one paragraph (person-free event schema) and linked `privacy-and-retention`, to avoid re-teaching GDPR here.
- **2026-10-22** — Used the RDW's 2025–2026 Belgian and German reading takeover (verified on rdw.nl) as the primary public evidence for the country-hop pattern, instead of the older 2017 European Parliament figures alone.

## Sources

- **Internal**
  - [[meet-axleby]] — Tracewell, report volumes, prices, Kilometra, the Odometer Correction and No-Hit Credit figures.
  - [[vehicle-identity]], [[registers-and-official-data]], [[provenance-and-data-quality]] — neighboring ownership.
  - `_research/brief-specification-history.md` (Part 2 and 3), `_research/brief-connected-data-privacy-regulation.md` (5.2–5.4, 6.1, 7.1–7.4).
- **External**
  - RDW pages on odometer judgements, registration moments, corrections, Belgian and German readings (2025–2026); RDW open data (queried 2026-10-22).
  - US DOJ NMVTIS pages; eCFR 49 CFR 580.5, 580.17, 573.15.
  - Car-Pass homepage and FAQ; DVSA MOT history API; KBA ZFZR page.
  - Carfax (archived 2025 "About" page), Mobility Global information statement (2026), Experian AutoCheck score (2025), HPI.
  - European Parliament odometer study (2017); Council note 15613/25 (2025); CJEU C-319/22 (2023).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Q1 audit counted as reports (per ledger), acronyms expanded, unverified OVI label removed, American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
