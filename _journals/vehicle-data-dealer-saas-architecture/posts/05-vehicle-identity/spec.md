---
status: accepted
revised: 2026-10-22
---

# Spec: Which Car Is This? VINs, Plates and the Vehicle Identity Graph

## Intent

Show how a vehicle data and dealer SaaS platform should identify one physical car across plates, VINs, countries and sources, so that every fact it sells lands on the right vehicle and every correction can follow it. The chapter argues for an internal surrogate vehicle key anchored to the VIN, plates as time-bounded assignments resolved as of a date, confidence tiers that products obey, and merges and splits as published, audited events. It grounds the argument in the VIN standards (US and EU), what a plate identifies in each market, documented cloning and re-identification practice, and how registers and agencies expose identifiers. Axleby's Cloned Plate is the opening story; the One Dossier re-keying of Lotwise stock to the AVK is the worked example.

Productscape bricks covered: `vidn` (identity part of decode and resolve), `rdwc` (the plate register as an identity source). Specification decoding, register access and generic entity resolution are handed to neighboring chapters.

## Audience

Chief architects, data-platform leads and principal engineers of vehicle-data companies and dealer-software vendors who must choose a vehicle key, migrate products onto it, or explain why a report described the wrong car. They should leave able to design the identity graph, its resolution interface and its tiers, and to judge an existing platform's identity model in a review.

## Success criteria

- [ ] VIN structure is given for the US (49 CFR 565) and the EU (Regulation 19/2011) with the check-digit difference, worked on a sample VIN, and its consequence for validators.
- [ ] What a plate follows is stated for NL, BE, DE, UK and US with sources, and the plate assignment is defined as a time-bounded edge.
- [ ] The identity graph (vehicle node, VIN observation, registration episode, plate assignment, identity events), the resolution interface and confidence tiers with product rules are specified, with three mermaid diagrams (graph, lifecycle, resolution sequence).
- [ ] Merge and split are defined as events with tombstones and redirects; propagation is handed to `journey-data-correction`.
- [ ] A requirements table (consistency, latency, freshness, availability) and plate-to-VIN caching rules, including "never cache unavailable as not found".
- [ ] Failure handling covers duplicates, conflicts, incomplete records, retries, partial failures, outages and fraud signals.
- [ ] A trade-off table of key choices and a recommendation on identifiers exposed to clients.
- [ ] "Across Markets" table with five columns and a judgement on common model versus market adapters; Axleby numbers match the ledger.

## Non-goals

- Register access regimes, mirrors and mutation feeds ([[registers-and-official-data]]).
- Decoding a VIN into edition and options ([[specification-and-equipment]]).
- Probabilistic matching, survivorship and golden records in general ([[ingestion-and-entity-resolution]]).
- Correction propagation end to end ([[journey-data-correction]]); privacy status of plates and VINs ([[privacy-and-retention]]); enumeration defense ([[vehicle-platform-security]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The successor to Regulation (EU) 19/2011 under Regulation (EU) 2019/2144 was not read; confirm the VIN rules carried over.
- ISO 3779/3780 texts were not accessible; the US small-maker threshold differs between sources (500 in the CFR text quoted by one brief, 1,000 per Wikipedia).
- No public plate-cloning figures were found for NL, BE or DE; the FBI 2009 VIN-cloning page was unreachable and is cited through Wikipedia.
- Belgian plate and register facts rest on secondary sources (DIV pages not readable).

## Decision log

- **2026-10-22** — Chose a surrogate key anchored to the VIN over a VIN key, because typos, provisional vehicles and clones all require identity to change without re-keying every product.
- **2026-10-22** — Made confidence tiers a product contract (which products may act on which tier) rather than a score, so the chapter's recommendation is enforceable in reviews.
- **2026-10-22** — Kept probabilistic matching out of scope beyond one paragraph; vehicle identity is mostly deterministic and the machinery belongs to `ingestion-and-entity-resolution`.
- **2026-10-22** — Split the Across Markets table into five columns because the Netherlands and Belgium differ fundamentally on what a plate follows.

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-bounded-contexts]], [[registers-and-official-data]], [[specification-and-equipment]], [[vehicle-history]], [[ingestion-and-entity-resolution]], [[journey-data-correction]], [[vehicle-data-apis]], [[privacy-and-retention]].
  - `_research/brief-identity-registers.md` (Parts 1, 3, 6, 7, 9), `_research/brief-specification-history.md` (1.1, 1.2, 1.6), `_research/scenario-ledger.md`, `_research/consistency-issues.md`.
- **External**
  - 49 CFR 565; Regulation (EU) 19/2011; Directive 1999/37/EC; EPRS briefing on COM(2025) 179 (2026).
  - RDW open data metadata and information pack (2026); DVLA VES description; DVSA MOT history OpenAPI specification; GOV.UK pages on private plates, VINs and Q plates; NHTSA vPIC; 28 CFR 25.54.
  - BBC News on car cloning (October 2025); Wikipedia pages on VINs, car cloning and national plates (2026).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: American spelling, RDW row count harmonized with Part II, 118 retained-plate matches dated to the later replay, BBC figure attributed. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in spec (neighboring). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
