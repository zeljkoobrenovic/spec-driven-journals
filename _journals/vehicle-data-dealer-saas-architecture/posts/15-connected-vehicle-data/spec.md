---
status: accepted
revised: 2026-10-22
---

# Spec: Data From the Car Itself: Connected Vehicles, Telematics and the EU Data Act

## Intent

Answer the chapter question from PLAN.md: **what does connected-vehicle data change for a vehicle data platform, and how should it be integrated?** The chapter argues that connected data is the first large vehicle-data source whose usage rights attach to one vehicle and one user rather than to a supplier contract. Three moves follow. First, model the right as a **consent grant per vehicle** (user, data holder, route, recipient, purpose, categories, legal basis, validity, state) and stamp its id on every reading. Second, keep **purpose-scoped telemetry** apart from **shared history**, and move readings between them only through a versioned **promotion** step that the grant allows. Third, treat coverage as partial and revocation as a first-class path: the car can refuse activation, readings can be stale repeats, and an ownership change ends the grant.

After reading, an architect can explain what the EU Data Act (Art. 3(2) seller/lessor duty since 12 September 2025; Art. 3(1) design duty for products placed on the market after 12 September 2026; Arts. 4–6 and 8–9), the Commission's September 2025 vehicle-data guidance, type-approval RMI and SERMI, ePrivacy and the GDPR require of a receiving platform, compare access routes, and design the consent registry, connectors and promotion into the history event model of `vehicle-history`.

The chapter owns **connected-vehicle data**, **data holder** and **consent grant (vehicle)**. Productscape bricks covered: **none** (a gap in the model; the chapter is marked [ADDED] in PLAN.md).

## Audience

Chief architects, data and integration leads of vehicle-data providers, dealer-software vendors and lessors who are deciding whether and how to take manufacturer data. They know event pipelines and OAuth; they need the legal mechanics stated precisely (who owes what, from when), the route landscape, and a data model that keeps purpose binding enforceable.

## Success criteria

- [ ] Defines connected-vehicle data, user, data holder, third party, readily available data and consent grant (vehicle), with the Commission guidance's in-scope/out-of-scope table (odometer and fault codes in; driving scores out).
- [ ] States the Data Act's dates and duties in a table, including the dealer/lessor Art. 3(2) duty and the receiving party's Art. 6 purpose binding.
- [ ] Compares access routes (manufacturer backend, consumer-consented aggregator, fleet-cleared aggregator, OBD reader, statutory channel) on consent model, latency, coverage and use.
- [ ] Shows the architecture (Mandate, Signalyard, promotion service, Tracewell, Charter) with three mermaid diagrams, a grant record table, a signal-to-event mapping and a requirements table.
- [ ] Works the Fleetmoor odometer pilot with ledger-consistent numbers, including the revocation failure on sales outside Tradefloor.
- [ ] Covers failure handling: ownership change, duplicates across routes, stale repeats, conflicts with official readings, incomplete coverage, route outages, schema change, trade-secret suspension.
- [ ] Contains a trade-off table and a specific, sourced Across Markets table (NL/BE, DE, UK, US) with a judgement on common core vs market rule sets.
- [ ] Every legal and company claim carries a dated primary or labeled secondary source; aggregator coverage figures are labeled vendor claims.

## Non-goals

- The history event model, odometer judgement and report snapshots ([[vehicle-history]]).
- Generic ingestion, validation layers and entity resolution ([[ingestion-and-entity-resolution]]).
- Battery state of health, certificates and the battery passport ([[ev-battery-health]]).
- The license and purpose register in depth ([[data-licensing-and-governance]]); controller/processor split, retention schedules and erasure propagation ([[privacy-and-retention]]).
- Deal documents and their delivery ([[deals-and-sales-documents]]); appraisal workflow ([[vehicle-acquisition]]); return inspections ([[condition-and-damage]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether the Commission's compensation guidelines under Data Act Art. 9(5) have been adopted, and what they say about per-vehicle pricing.
- Which national authorities NL, BE and DE designated under the Data Act, and their first decisions on vehicle data.
- How dealers are delivering Art. 3(2) pre-contract information in practice; whether manufacturers publish it per model.
- Whether a lessee (also a "user" under Art. 2(12)) can object to the lessor's history-contribution purpose.
- Final text of the EU roadworthiness revision (2025/0097(COD)); in negotiation in October 2026.
- UK SERMI start date (1 April 2026) rests on a trade-press report via the research brief; not read in primary form.
- Manufacturer data marketplaces' own terms and prices were not verified.

## Decision log

- **2026-10-22** — Chose a lessor fleet pilot (Fleetmoor) rather than a consumer appraisal as the scene, because the lessor is clearly the Data Act "user" and the purpose question (remarketing vs shared history) is sharper.
- **2026-10-22** — Coined "consent grant (vehicle)" as a deliberately broad record that stores which legal basis applies (Data Act request, ePrivacy consent, GDPR basis, fleet contract), instead of calling everything "consent".
- **2026-10-22** — Recommended the telemetry–history split with a governed promotion step (monthly plus event-date readings) over either "never promote" or "promote everything", tying it to Art. 6(1) and to the trust ranking in `vehicle-history`.
- **2026-10-22** — Kept GDPR roles and retention to short pointers and linked `privacy-and-retention` and `data-licensing-and-governance`, to avoid re-teaching them.

## Sources

- **Internal**
  - [[meet-axleby]] and `_research/scenario-ledger.md` — Fleetmoor, Tradefloor, Tracewell, Turnstile, Charter, Meterline, the Odometer Correction.
  - [[vehicle-history]], [[ingestion-and-entity-resolution]] — event model, source classes, validation layers.
  - `_research/brief-connected-data-privacy-regulation.md` (Parts 1–6, 8), `_research/brief-specification-history.md` (2.3, Council text), `_research/brief-valuation-market-condition.md` (Part 6).
- **External**
  - Regulation (EU) 2023/2854; Commission guidance C/2025/5026; Regulation (EU) 2018/858; Delegated Regulation (EU) 2021/1244; CJEU C-319/22.
  - EDPB Guidelines 01/2020 v2.0; TDDDG § 25; PECR regulation 6 (as substituted 2026).
  - Council note ST 15613/25; EP Legislative Observatory 2025/0097(COD).
  - Smartcar and High Mobility developer documentation; Car-Pass; FIGIEFA.
  - FTC GM/OnStar order (2026); California CCPA page; Texas v. GM press reports (2024).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: acronyms expanded (FRAND, GNSS, TDDDG, PECR, ICO), Trade-Offs heading aligned, timetoread corrected to 32 min, source headings aligned. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (enrollment) outside source entries. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
