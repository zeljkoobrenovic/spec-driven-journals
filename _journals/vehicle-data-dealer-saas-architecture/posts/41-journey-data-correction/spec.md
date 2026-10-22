---
status: accepted
revised: 2026-10-22
---

# Spec: A Fact Was Wrong: Propagating a Vehicle Data Correction

## Intent

Answer the contract question: when a supplier corrects a vehicle fact, how does the correction reach every place the fact spread? The chapter walks the Odometer Correction of May 2027 end to end as a Part VIII journey. It covers detection (with the canonical per-workshop-chain gate, consistency issue 17), containment through *disputed* fact versions, the bitemporal correction, the impact graph as write-time edges kept by each owning store, the per-artifact policy (recompute live state; supersede or annotate issued artifacts; propose, never make, dealer decisions), notices to dealers, consumers and data clients with the audience taken from the access audit, legal and reputational handling, and audit and closure of a correction case. The reader should leave able to design a correction journey whose containment time, fan-out time, residuals and evidence time can be stated.

Owns: **correction event**, **impact graph**. Productscape bricks touched (no new ones): `vhis` (history and odometer corrections), `valu`, `advf`, `vapi`, `dgov`, `dosr`.

## Audience

Chief architects, data and platform leads, and product owners at vehicle-data providers and dealer-software vendors who already store facts with provenance and now need the operational path for when a fact is wrong.

## Success criteria

- [ ] Contains a sequence diagram of the journey, a timeline table of the 2027 incident against the target design, and a step table with owner, identifiers, consistency and latency per hop.
- [ ] Defines correction, retraction, disputed, correction case, correction event, impact edge, impact graph, issued vs live artifact.
- [ ] Gives the per-artifact-class policy table (recompute / successor / supersede / re-propose / thin notice / restate) with the ledger numbers (2,870; 6,140; 412/96; 1,180; 307/41; 19/2,310).
- [ ] Follows the per-segment batch gate as canonical (median gate insufficient) per consistency issue 17.
- [ ] Covers at least four failure cases, including the three named in the contract (correction before original, correction to an already-overwritten fact, client ignores the webhook), with detection and recovery.
- [ ] Cites dated evidence for register correction procedures (RDW, Car-Pass, DVSA MOT, 49 CFR 580.5), GDPR Art. 5(1)(d) and 19, the Digital Content Directive Art. 14, the Consumer Rights Act 2015 s. 42, and webhook contracts.
- [ ] Includes trade-off tables, a metrics table, "What Changes in Another Market", the Chief Architect's view, questions and sources; article at or under 8,000 words.

## Non-goals

- Bitemporal modeling and the provenance envelope ([[provenance-and-data-quality]]); batch validation, quarantine and replay ([[ingestion-and-entity-resolution]]).
- Odometer judgement rules and report wording ([[vehicle-history]]); the valuation ledger's design ([[valuation-engine]]).
- The event backbone, webhook delivery contract and catalog ([[events-webhooks-and-sync]]); data-quality monitoring ([[observability-and-data-operations]]).
- Erasure propagation and the controller/processor analysis ([[privacy-and-retention]]); credit rating rules ([[billing-and-metering]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- How amended MOT test records appear in the DVSA daily delta files is not documented; the chapter labels its assumption as an inference.
- No vehicle-data company publishes how it propagates corrections; the federated impact graph is the author's reference architecture.
- US state consumer law and history providers' buyback terms were not studied in depth.

## Decision log

- **2026-10-22** — Told the incident as it happened (wait for the supplier, overwrite in place, eleven days of manual analysis) beside the target design in one timeline table, so every design element answers a measured cost.
- **2026-10-22** — Chose a federated impact graph (write-time edges in each owning store, adapters registered in Retrace) over a central lineage graph; dataset-level lineage judged too coarse.
- **2026-10-22** — Made containment (*disputed* versions) an explicit step before correction, and made outcome links in the valuation ledger the filter for dealer notices (6,140 → 286).
- **2026-10-22** — Added a worked vehicle (Venlo Volvo XC60) whose current value was protected by a newer reading but whose history and report were wrong, to show why impact starts from superseded versions; used the 118 wrong plate matches as a second, retraction-type case.

## Sources

- **Internal**
  - [[provenance-and-data-quality]], [[ingestion-and-entity-resolution]], [[vehicle-history]], [[valuation-engine]], [[merchandising]], [[events-webhooks-and-sync]], [[observability-and-data-operations]], [[privacy-and-retention]].
  - `_research/brief-specification-history.md`, `_research/brief-platform-apis-operations.md`, `_research/brief-connected-data-privacy-regulation.md`, `_research/scenario-ledger.md`, `_research/consistency-issues.md` (item 17).
- **External**
  - RDW *Tellerstand corrigeren*; Car-Pass FAQ; GOV.UK *Fix mistakes on your MOT record*; 49 CFR 580.5.
  - GDPR (Regulation (EU) 2016/679) Art. 5(1)(d), 16, 19; Directive (EU) 2019/770 Art. 14; Consumer Rights Act 2015 s. 42; CCPA.
  - Stripe webhooks; Standard Webhooks; OpenLineage object model; Fowler, *Bitemporal History* (2021).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: failure-pattern callout uses the house em dash; item 17 batch-gate wording confirmed. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
