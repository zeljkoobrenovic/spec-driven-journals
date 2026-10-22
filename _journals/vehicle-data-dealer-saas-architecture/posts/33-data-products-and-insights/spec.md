---
status: accepted
revised: 2026-10-22
---

# Spec: Selling Insight: Enrichment, Market Insight and Predictive Data Products

## Intent

Show how a vehicle data platform should build and sell its batch-shaped data products: file enrichment of client plate lists, aggregated market insight (cubes, dashboards, reports, data files) and predictive vehicle scores (change-of-ownership propensity and lead lists). These products carry the request path's controls (license, purpose, metering, correction) into bulk work. They need data-product contracts, a separate batch lane, short retention for client files, disclosure control in one serving layer, and a lawful basis for lead lists that a Dutch register-based business can defend. The chapter owns three terms: **enrichment job**, **insight cube** and **propensity score (vehicle)**.

Productscape bricks covered: `fenr` (Vehicle File Enrichment), `mins` (Market Insights and Performance Dashboards), `cool` (Change-of-Ownership Lead Scoring).

## Audience

Chief architects, data and ML leads and product directors of vehicle data companies who sell insight and enrichment to importers, lessors, insurers and dealer groups, and who must answer to a data protection officer about lead lists.

## Success criteria

- [ ] Reader can design an enrichment job with per-row statuses, snapshot-based resolution, chunked idempotent processing, per-row metering and 30-day deletion.
- [ ] Reader can define a source-eligibility table for an insight cube and explain why customer transaction data is excluded.
- [ ] Reader can specify threshold, dominance and complementary suppression rules, name the contributor per measure, and explain why fixed geographies stop differencing.
- [ ] Reader can explain why a plate-level propensity score is personal data and why match-in plus aggregate forecasts replaces territory lists (GDPR Art. 21, RDW's no-commercial-personal-data rule, ePrivacy Art. 13(2)).
- [ ] Reader can state the restatement policy for cubes and the delivery list that makes corrections reachable.
- [ ] Chapter includes the Axleby worked examples (Fleetmoor audit, Rooftop Benchmark complaint, Horizon DPIA, Meridal Import) with numbers consistent with the ledger.
- [ ] Across Markets table compares NL/BE, DE, UK, US with dated sources.

## Non-goals

- Sale detection, stand-time and market days' supply ([[market-data]]).
- The license register and purpose check mechanics ([[data-licensing-and-governance]]).
- The DPIA, controller/processor split and retention schedule in general ([[privacy-and-retention]]).
- Request-path API design ([[vehicle-data-apis]]) and events/webhooks ([[events-webhooks-and-sync]]).
- Valuation model governance ([[valuation-engine]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Belgium offers a vehicle-level open register dataset usable for ownership-change labels (not verified).
- DVSA MOT history API reuse terms for commercial products (not verified).
- Whether the Dutch Data Protection Authority has issued guidance on plate-level marketing scores (none found).

## Decision log

- **2026-10-22** — Treated all three bricks as one bulk platform with three shared gates (Charter on intake, disclosure control in the serving layer, file-exchange retention) instead of three separate product sections, because the controls are what the products share.
- **2026-10-22** — Made match-in plus aggregate forecasts the recommended lead-list design; rejected territory plate lists. VWE's documented plate/customer-file split is shown as the market precedent, without inferring its internals.
- **2026-10-22** — Aligned seller-attributed suppression with the market-data ledger rule (at least 5 rooftops and 20 cars) and added dominance and fixed market areas; rejected differential privacy as the default because importers reconcile against their own exact counts.
- **2026-10-22** — Limited Horizon to the Netherlands because only Dutch open data gives a daily vehicle-level ownership-change label without personal data.

## Sources

- **Internal**
  - [[market-data]] — Pulse v2, settled windows, the Lotwise cell rule.
  - [[registers-and-official-data]] — Turnstile mirror and snapshot diffs.
  - [[data-licensing-and-governance]] — Charter, the `change-of-ownership-propensity` purpose, trap records.
  - [[case-vwe]] — the lead-generator privacy seam.
  - [[scale-and-cost]] — the Saturday Batch and upstream budget broker.
- **External**
  - VWE lead-generator and Marktinzicht pages (n.d., accessed 2026-10).
  - Mobility Global information statement (2026); automotiveMastermind homepage.
  - GDPR, ePrivacy Directive, CJEU C-319/22, RDW privacy statement and open data, ICO ANPR guidance, DVLA INF266 (2022), DfT notes (2026), KBA statistics, DPPA.
  - Snowflake aggregation policies; AWS Clean Rooms aggregation rule; Data Mesh Manager; Bitol ODCS.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: removed code fences around mermaid blocks, added pre-2027 Horizon score retention (consistency item 22), expanded acronyms, American spelling. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: Horizon 90-day expiry enforced from September 2027 after the March 2027 redesign approval; old scores purged then (item 37). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
