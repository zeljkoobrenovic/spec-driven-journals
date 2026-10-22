---
status: accepted
revised: 2026-10-22
---

# Spec: From Many Sources to One Record: Ingestion, Normalization and Entity Resolution

## Intent

Show how vehicle data should enter a vehicle data and dealer SaaS platform and become one record per vehicle. The chapter compares batch and event-driven ingestion against explicit requirements (freshness, volume, cost, replay, completeness, ordering, blast radius), with labeled assumptions. It then teaches the stages of one ingestion pipeline: an immutable landing zone, layered contract validation with quarantine, normalization that keeps original values, tiered entity resolution (VIN, plate at observation date, probabilistic with a review band), and a golden record computed from per-source records under versioned survivorship rules. The reader should leave able to defend "batch at the edge, events inside", to recognize that schema checks alone would not stop a wrong-unit file, and to insist that the golden record is a rebuildable view.

Productscape bricks covered: `vhis` (history assembler: parallel queries, event deduplication), `mktd` (ownership-change ingest, listing matcher), `vidn` (specification resolver as a survivorship problem). [ADDED: generic ingestion platform.]

## Audience

Chief architects, data platform leads and principal engineers at vehicle-data companies and dealer-software vendors who own supplier, register, advert and dealer-input pipelines, and who must decide how those pipelines are shared across products and acquisitions.

## Success criteria

- [ ] Contains an explicit batch vs event-driven comparison table tied to stated requirements, with assumptions labeled, and a per-source decision table for Axleby.
- [ ] Defines and owns ingestion pipeline, quarantine, survivorship rule and golden record; defines landing zone, source record and match decision.
- [ ] Shows a four-layer validation model (delivery, schema, semantics, distribution) and why the distribution layer catches the Odometer Correction class of error.
- [ ] Presents resolution tiers with plate-at-observation-date resolution tied to the Cloned Plate, and cites Fellegi–Sunter and Splink for probabilistic linkage.
- [ ] Gives a survivorship table and distinguishes single-valued attributes from event sets.
- [ ] Works an Axleby example with ledger-consistent numbers (2,870 vehicles, 11 days, 6,140 valuations, 412 reports, 1,180 adverts) and a replay of the May 2027 batch.
- [ ] Includes failure handling (duplicates, partial files, drift, conflicts, incomplete records, wrong merges, outages, replay overload), a trade-off table, Across Markets, the Chief Architect's view and Questions to ask.
- [ ] Has three mermaid diagrams that pass the render check; article under 8,000 words.

## Non-goals

- VIN structure, plate assignments, merge and split in the identity graph: [[vehicle-identity]].
- Register access regimes and mutation feeds: [[registers-and-official-data]].
- Provenance envelope, bitemporal model, freshness SLOs and data contracts: [[provenance-and-data-quality]].
- How the Odometer Correction propagated through products and was corrected downstream: [[journey-data-correction]].
- Advert harvesting, its legal limits and sale detection: [[market-data]].
- Outbox and webhook delivery: [[events-webhooks-and-sync]]; license enforcement: [[data-licensing-and-governance]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No vehicle-data company publishes how it resolves supplier and advert records to vehicles; the recommended architecture is labeled as the author's inference. Revisit if a primary source appears.
- Thresholds (0.5% segment failure rate, review band of about 200 a day) are illustrative; a later edition could show how to tune them from audit samples.

## Decision log

- **2026-10-22** — Set the scene after the Odometer Correction and framed it as "the file was on time", so the batch vs event comparison argues from requirements rather than fashion; rejected a scene where streaming fixes the problem.
- **2026-10-22** — Named Axleby's shared ingestion pipeline **Inlet** (specified July 2027) and added it to the ledger, so later chapters can refer to one pipeline.
- **2026-10-22** — Kept dealer and consumer resolution to one paragraph with links, to keep the chapter on vehicles; linked LISTED's `entity-resolution` for clustering depth instead of re-teaching it.
- **2026-10-22** — Treated request-time lookups (build data, theft checks) as a fourth ingestion mode, because they land and resolve like files and carry most per-call cost.

## Sources

- **Internal**
  - [[meet-axleby]] — systems, volumes and the recurring worked examples.
  - [[vehicle-identity]], [[vehicle-history]], [[provenance-and-data-quality]], [[journey-data-correction]] — neighboring ownership.
  - [[entity-resolution]] (LISTED) — clustering and governance of listing matches.
- **External**
  - Kreps, "Questioning the Lambda Architecture" (O'Reilly, 2014) — reprocessing by replay.
  - Fellegi and Sunter (1969); Splink documentation and Linacre et al. (2022) — probabilistic linkage.
  - Auto Trader UK Engineering (2026), AutoScout24 DataRunner (2023), AWS posts on Cox Automotive (2020, 2024) — public pipeline evidence.
  - RDW open data metadata and license, DVLA, DVSA, KBA, Car-Pass pages — Across Markets source landscape.
  - Research briefs: `brief-platform-apis-operations.md` (Part 3), `brief-specification-history.md` (Part 3), `brief-connected-data-privacy-regulation.md` (Part 7).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned the Dutch register feed with the snapshot-diff mutation feed owned by registers-and-official-data (consistency item 14), golden record materialized beside Anchor (item 31c), American spelling. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (neighboring). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
