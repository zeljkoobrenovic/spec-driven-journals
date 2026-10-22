---
status: accepted
revised: 2026-10-22
---

# Spec: Field Kit: Templates for the Vehicle Platform Architect

## Intent

Give the reader a set of practical, copyable templates for the records a Chief Architect keeps when one group sells vehicle data (identity, specification, history, valuation, market data) and runs dealer SaaS (stock, pricing, syndication, leads, deals, register transactions). Each template comes from the chapter that teaches it, keeps that chapter's terms and fields, says where a field differs between the data half and the workflow half or between markets, and is filled in once with a short Axleby example whose numbers, names and dates match the owning chapter and the scenario ledger. A reader should be able to start from the design or decision on their desk, copy one record, see which fields carry identity, provenance, ownership and money, and know which mistakes make the record useless.

Productscape bricks covered: none directly. The page is the working form of decisions taught across Parts I–IX; the brick-by-brick mapping lives in [[domain-coverage]].

## Audience

Chief and enterprise architects of vehicle-data companies and dealer-software vendors, principal engineers, and the leads of data and valuation, partner integrations (channels, DMS, suppliers), platform and SRE, billing, and data governance. Product, commercial and legal leaders use Tools 1, 10, 11, 12 and 15 as discussion documents.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; three KEY POINTS; three failure patterns with exact names; `<br>`; a lead on how to use the templates; a table of contents (Tool | Use it when | Chapter).
- [x] Contains the sixteen templates in the PLAN contract, in that order, each as a `## Tool N` section with purpose and "use it when", a copyable table, checklist or fill-in block, an Axleby example, common mistakes and a Learn more `[[link]]` to the owning chapter.
- [x] Every template's fields come from the owning chapter: investment class, condition, scope and market flag ([[vehicle-capability-map]]); identifier, source of truth, four kinds of copy and contested rows ([[vehicle-bounded-contexts]]); envelope v1 fields and confidence tiers ([[provenance-and-data-quality]]); four validation layers and the Kilometra v2 clauses ([[ingestion-and-entity-resolution]]); model governance gates and segment status ([[valuation-engine]]); the channel profile list ([[listing-syndication]]); routing order and read-back ([[leads-and-crm]]); authority chain, Ambiguous state and probe ([[registration-and-trade-services]]); Hitch components and partner checklist ([[dms-integration]]); R1–R8 and the July 2027 record ([[tenancy-and-dealer-groups]]); five gates and entitlement rows ([[identity-access-and-entitlements]]); license classes, rule schema and grant lifecycle ([[data-licensing-and-governance]]); category blocks, outcome/freshness and version lifecycle ([[vehicle-data-apis]]); three-outcome journey SLOs and the dependency budget ([[reliability-and-dependencies]]); five sourcing options, four gates and the data-rights test ([[build-buy-or-partner]]); team versus forum records, decision rights and vetoes ([[organizing-engineering]]).
- [x] Axleby examples use ledger and chapter figures exactly: capability map v1 (39 capabilities; 13/21/5; 18/6/14; A3 specification P, Amber, Shared); entity–owner table v1 of 3 June 2027 (29 entities); build-data 28.5M fetches ≈€13.1M, 41% repurchases, ≈€0.58 first fetch, Q4 2027 13.5M ≈€7.8M; Kilometra 410,000 readings, 02:30 CET, €95,000 push quote, 91/92 batches, 96.8% of 4,100 pairs; EV replay week 3/week 5 at +5.8%, +2.4% by week 7, €1.1M → €0.3M; Velto hubs and the 1,460 leads; Brandsma's Corolla, 90 s timeout, 41 ambiguous outcomes on 30 June 2027; DriveDesk 1,900 rooftops and the 9–21 November 2027 outage; July 2027 tenancy decision; Lintvelt grant and €230,000; Fleetmoor €5.22 lookup; the 21 October 2027 sourcing register (flat fee €6.9M declined, review below 9M fetches); appraisal budget 0.83% vs 0.3%; event backbone record of 14 December 2027.
- [x] One mermaid diagram shows how the records reference each other; cross-links use only valid permalinks.
- [x] Short Sources and Evidence section with dated sources and the closing fictional-Axleby sentence; article at or under about 8,000 words excluding table separators.

## Non-goals

- Re-teaching the reasoning behind each template; each tool summarizes and links to its chapter.
- The event catalog ([[events-webhooks-and-sync]]), the impact graph ([[journey-data-correction]]) and metric definitions ([[dealer-and-data-economics]]), which are linked, not reproduced.
- Definitions of terms ([[glossary]]), the source list by topic ([[bibliography]]) and the brick-to-chapter map ([[domain-coverage]]).
- Downloadable file formats (spreadsheets, document templates).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[vehicle-capability-map]], [[vehicle-bounded-contexts]], [[build-buy-or-partner]] and [[organizing-engineering]] were being written in parallel; Tools 1, 2, 15 and 16 were first drafted from their PLAN contracts and then aligned with the finished chapters in the same session. Re-check field names if those chapters are revised.
- Tool 6's example uses AutoScout24's public documentation as accessed in October 2026; portal contracts change often and should be re-checked at each revision.

## Decision log

- **2026-10-22** — Chose the sixteen templates in the PLAN contract and no others, ordered by the book's parts, with the sourcing card and ADR last because they cite the others.
- **2026-10-22** — Replaced BOOKED's hotel-versus-home columns with a "which half, which market" convention stated once and applied where a field differs, rather than a column in every template, to stay inside the length cap.
- **2026-10-22** — Chose the One Dossier event backbone record as the ADR example because it changes owners and delivery paths across both halves and has a dated quarter-by-quarter consequence plan; the tenancy record already fills Tool 10.
- **2026-10-22** — Used a real portal (AutoScout24) for the channel adapter example because the chapter's profile fields are documented from its public API; all facts carry the access date, and no Axleby incident is attributed to it.

## Sources

- **Internal**
  - [[provenance-and-data-quality]], [[ingestion-and-entity-resolution]], [[specification-and-equipment]], [[scale-and-cost]] — envelope v1, Inlet, Kilometra contract v2, build-data purchase gate and cost.
  - [[valuation-engine]], [[listing-syndication]], [[leads-and-crm]], [[registration-and-trade-services]], [[dms-integration]] — model governance, channel profiles, routing, register transactions, Hitch.
  - [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[data-licensing-and-governance]], [[vehicle-data-apis]], [[reliability-and-dependencies]], [[events-webhooks-and-sync]] — tenancy record, gates and entitlements, Charter, Folio and v2, journey SLOs, event backbone.
  - `_research/scenario-ledger.md` and `PLAN.md` — canonical Axleby facts and the toolkit contract.
- **External**
  - AutoScout24 Listing Creation API documentation and changelog; mobile.de Seller API documentation (n.d., accessed 2026-10).
  - RDW information pack for recognized companies (2026); Regulation (EU) 2023/2854; W3C ODRL 2.2 (2018); Bitol Open Data Contract Standard; RFC 9457 (2023); Standard Webhooks; CloudEvents; Google SRE book (2016); AWS SaaS Lens (2023).
  - Michael Nygard, *Documenting Architecture Decisions* (2011); Andrew Harmel-Law (2021); Mitchell et al., *Model Cards for Model Reporting* (2019); Pang et al., *Zanzibar* (2019).
  - The BOOKED toolkit (`stays-marketplace-architecture/posts/toolkit/`) — page format and tool structure.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned the Sold rule (issues 24 and 31), DMS field ownership (issue 31a) and the fitness-function list with their owning chapters; corrected reading time. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: data-contract example calls the median batch gate insufficient and the per-workshop-chain check the fix (item 38); corrected redelivery unit to miles in the envelope example. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 0 conceptual figures (article-illustrator). *(AI-mediated session)*
