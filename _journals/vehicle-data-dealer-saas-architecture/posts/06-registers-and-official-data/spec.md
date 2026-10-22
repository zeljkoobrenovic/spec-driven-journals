---
status: accepted
revised: 2026-10-22
---

# Spec: The Authoritative Source: Vehicle Registers and Official Data Access

## Intent

Show how a vehicle data and dealer SaaS platform should connect to official vehicle registers, and what it owes them in return. The chapter explains what registers hold (registration, technical, inspection, status, odometer judgement, ownership change) and the four access regimes that decide what a platform may store and resell: open data, paid per-vehicle business access, provider and transaction access, and purpose-bound access to personal data. It compares those regimes in the Netherlands, Belgium, Germany, the UK and the US with dated official sources. It then turns them into a reference design: one register gateway with a mirror of bulk-permitted data, a mutation feed derived from snapshot diffs (or applied from published deltas), live calls for blocking facts, answer classes that keep "could not ask" apart from "no", a credential and quota monitor, and a purpose-tagged audit. The reader should leave able to decide, per fact, what to mirror and what to ask live, and to run register access as a governed group capability.

Owns: **authorized information provider** (a book term; the RDW's term is "provider"), **register gateway**, **register mirror**, **mutation feed**. Productscape bricks: `rdwc` (RDW Registry Connector and Vehicle Register: plate register API, register change consumer, session monitor, channel adapter), and the `rdwoutage` stressor.

## Audience

Chief architects, data-platform and integration leads, and product directors at vehicle-data providers, dealer-software vendors, lessors and insurers who read from or transact with registers. They know APIs, caches and event streams; they need the register-specific legal, access and failure picture per country.

## Success criteria

- [ ] Defines the four owned terms, and uses "authorized information provider" only as a plain-words book term, with the RDW's own "provider" wording and no claim of an official title (consistency issue 13).
- [ ] Gives a per-country access-regime picture with dated sources: RDW open data (CC0, no VIN, snapshot), paid per-plate access with theft status, the provider model and certificates; Car-Pass; KBA §39/§35 and the GKS; DVLA reasonable cause, KADOE, closed VES, DVSA MOT bulk and delta; NMVTIS and the DPPA.
- [ ] States that RDW open data is a plate-keyed snapshot whose changes must be derived by diffing, and that the DVSA MOT deltas are the only explicit change feed found (issue 14), with evidence of snapshot lag from a dated query.
- [ ] Presents Turnstile with at least two diagrams, a component table, a mirror-or-live rule per fact class and a consistency/latency/freshness/availability table.
- [ ] Works an Axleby example with numbers (the Three Copies inventory, the Brandsma near miss, the purchase-gate cost model) consistent with the ledger, and references the Month-End Register Outage without re-telling it; the register forbids completing a registration during an outage (issue 15).
- [ ] Covers duplicates, partial snapshots, mass changes, missed deltas, mirror/live conflicts, incomplete records, ambiguous timeouts, outages, credential expiry, quota exhaustion and regime changes.
- [ ] Includes trade-off tables (how much to mirror; provider seat or integration), the Across Markets table, the Chief Architect's view and 6–10 questions.

## Non-goals

- VIN and plate structure, the identity graph and plate-to-VIN resolution ([[vehicle-identity]]).
- Transaction types, the retry queue, proof documents and registration taxes ([[registration-and-trade-services]]); the full Month-End journey ([[journey-sale-to-registration]]).
- Odometer judgement and history assembly ([[vehicle-history]]); specification resolution from register technical data ([[specification-and-equipment]]).
- The license register and purpose engine in general ([[data-licensing-and-governance]]); journey SLOs and degraded modes across all dependencies ([[reliability-and-dependencies]]); GDPR lawful basis and retention ([[privacy-and-retention]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Belgian DIV access (WebDIV, partner channels) could not be read from a primary source; the chapter says the evidence stops at Car-Pass.
- The RDW does not document the open-data publication lag; the chapter infers it from owner-change date counts on 22 October 2026.
- Provider agreements with the RDW are not public; obligations beyond the public rules are labeled as inference.
- Final text of COM(2025) 179 and of the roadworthiness odometer article; when DVLA VES registration reopens.

## Decision log

- **2026-10-22** — Opened with a new local Axleby scene (three register copies and the 14 April 2027 Brandsma near miss) instead of re-telling the Month-End Register Outage, which [[registration-and-trade-services]] owns.
- **2026-10-22** — Verified directly against the RDW open-data API that awaiting-inspection status is withheld in open data and that the owner-change field holds only the latest change; both shaped the mirror-or-live rule.
- **2026-10-22** — Framed the mirror as a product (feed, files, webhooks) whose value is snapshot history, measured freshness and VIN resolution, not the CC0 data itself.
- **2026-10-22** — Treated Germany and the US as partner-adapter markets rather than register-adapter markets.

## Sources

Internal: [[meet-axleby]], [[vehicle-identity]], [[registration-and-trade-services]], [[vehicle-history]], [[data-licensing-and-governance]], [[reliability-and-dependencies]], [[case-vwe]].

External: RDW informatiemap (2026), provider list, open-data pages and leaflet, paid business-access page, privacy statement, open-data API (queried 2026-10-22); Car-Pass FAQ; KBA ZFZR page, §35/§39 StVG, KBA GKS brochure (2024); DVLA VES documentation, INF266 (2022); DVSA MOT history API documentation; 28 CFR 25.54, BJA NMVTIS pages, 18 U.S.C. § 2721; EPRS briefing on COM(2025) 179 (2026); Council roadworthiness compromise (2025); ACM VWE decision (2022).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: expanded DVLA, DVSA and DPPA on first use, harmonized RDW row count, dated register-change webhooks to Q3 2028, American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
