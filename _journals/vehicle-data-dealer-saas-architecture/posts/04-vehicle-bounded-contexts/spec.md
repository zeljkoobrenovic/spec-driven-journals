---
status: accepted
revised: 2026-10-22
---

# Spec: Drawing the Lines: Bounded Contexts, Entities and Sources of Truth

## Intent

Give the book its boundary model: where service and team boundaries go on a platform that sells both vehicle data and dealer software, and which context is the source of truth for each principal entity. The chapter owns the **entity–owner table** (entity, identifier, source of truth, allowed copies, lifecycle), the **source of truth** concept (and its difference from system of record), the **context map** for the vehicle platform, and brief definitions of **stock item** and **vehicle dossier** (deep in [[inventory-and-vehicle-dossier]]). Because most later chapters already define their own entities, this chapter is the consistent synthesis: it records the board's decision on six rows where those chapters disagree (when a stock item is Sold, following consistency issue 24; stock unit vs stock item at DMS rooftops, tenant vs legal entity, golden record and current mileage, register authority, the three meanings of "customer"). The reader should leave able to draw the same table and map for their own platform and to classify every copy as a reference, a decision snapshot, an observation or a projection.

Productscape bricks covered (as a research map, not as company facts): all 28, mapped onto contexts — `rdwc`, `vidn`, `vhis`, `evsh`, `dmgc`, `mktd`, `valu`, `bpmc`, `dosr`, `occm`, `tapp`, `advf`, `dweb`, `admn`, `finc`, `rdwt`, `mats`, `impx`, `b2bt`, `vapi`, `fenr`, `mins`, `cool`, `fnnk`, `ctrv`, `iden`, `bill`, `dgov`; plus the model's data-asset ownership inconsistencies (digest §10.2, "store vs module ownership").

## Audience

Chief and enterprise architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors and dealer groups who must decide team and service boundaries, merge acquired products, or settle "who owns this field" disputes between a dealer product and a DMS.

## Success criteria

- [x] Defines bounded context, ubiquitous language, core/supporting/generic subdomains, source of truth vs system of record, and four kinds of copy, with dated sources (Evans 2015, Fowler 2014, Conway 1968).
- [x] Lists Axleby's contexts by family with subdomain type, 2027 home and target system, and owning hub.
- [x] Presents the entity–owner table for vehicle facts, dealer workflow and accounts/governance, consistent with the owning chapters and the ledger.
- [x] Records the six contested rows and the decision for each, with reasons.
- [x] Contains a context map (mermaid) naming conformist, ACL, open host and customer–supplier relationships, and a sequence diagram of one sale across contexts.
- [x] Contains a requirements table (consistency, latency, freshness, availability) for cross-boundary interactions, with assumptions labeled.
- [x] Covers failure handling: second writers, drifting copies, merges/splits/corrections, incomplete records, duplicates across boundaries, owner outages, boundary moves during migration.
- [x] Compares boundary-drawing approaches in a trade-off table with the requirements that justify the recommendation; notes market differences that move a boundary.

## Non-goals

- The inside of each context: identity graph ([[vehicle-identity]]), stock lifecycle and dossier ([[inventory-and-vehicle-dossier]]), desired-state syndication ([[listing-syndication]]), DMS adapters ([[dms-integration]]), event envelope and outbox ([[events-webhooks-and-sync]]), tenancy and authorization ([[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]]).
- The capability map and investment heat map ([[vehicle-capability-map]]).
- Integrating the acquired portfolio as a program ([[one-platform-from-many-products]]) and team design in depth ([[organizing-engineering]]).
- A full Parts II–VII "Across Markets" section (Part I); only market differences that move a boundary.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- `inventory-and-vehicle-dossier` still shows Reserved → Sold on "contract signed"; per consistency issue 24 (and decision 1 here) signing reserves and Sold follows the deal's conditions and invoice. Its reviewer should align the state table.
- `inventory-and-vehicle-dossier` names Velto's legal entities differently from `tenancy-and-dealer-groups` (both illustrative); this chapter avoids naming them.
- No public source describes any real company's context map; the Cox inference is labeled and should be re-checked against `case-cox-automotive` once its federation evidence is aligned (consistency issue 18).

## Decision log

- **2026-10-22** — Opened with the five meanings of "sold" rather than a generic DDD introduction, because polysemy is the test for a boundary and every reader recognizes the word.
- **2026-10-22** — Resolved six ownership disagreements between existing chapters (Sold trigger aligned with consistency issue 24, stock unit vs stock item, tenant vs legal entity, golden record attribution, authority register owner, prospect/buyer/tenant) and recorded them as the board's v1 decisions (3 June 2027).
- **2026-10-22** — Chose conformist relationships to the AVK and the tenant hierarchy, explicitly not a shared kernel, and ACLs at every external edge.
- **2026-10-22** — Used "Where Boundaries Differ by Market" instead of the Parts II–VII heading, as in `dealer-and-data-economics`.

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-identity]], [[registers-and-official-data]], [[specification-and-equipment]], [[vehicle-history]], [[ingestion-and-entity-resolution]], [[valuation-engine]], [[market-data]], [[inventory-and-vehicle-dossier]], [[listing-syndication]], [[leads-and-crm]], [[deals-and-sales-documents]], [[registration-and-trade-services]], [[dms-integration]], [[b2b-trade-and-remarketing]], [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[billing-and-metering]], [[data-licensing-and-governance]], [[events-webhooks-and-sync]].
- **External**
  - Evans, *Domain-Driven Design Reference* (2015); Fowler, "BoundedContext" (2014); Conway, "How Do Committees Invent?" (1968); Skelton and Pais, *Team Topologies* (2019); Vernon, "Effective Aggregate Design" (2011).
  - RDW base-register page (n.d.) and open-data metadata (queried 2026-10-22); Authenticom v. CDK (2017); CDK v. Brnovich (2021); STAR (2019).
  - mobile.de, AutoScout24 and Autotrader Connect API documentation (n.d., accessed 2026-10); PlatformCon 2024 Cox talk; Apollo Cox customer story (n.d.).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned the RDW row count with Part I, latency assumptions with vehicle-identity and data-licensing, Evans book year to 2003, expanded DDD and B2B. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
