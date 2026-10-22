---
status: accepted
revised: 2026-10-22
---

# Spec: Mapping the Business: A Capability Map From Identify to Insight

## Intent

Show how to build and use a business capability map for a group that sells both vehicle data and dealer software: what the business must be able to do from Identify to Insight, which capabilities the data half and the workflow half should share, and how a heat map turns the map into investment, sharing and sourcing decisions. The reader should leave able to draw a two-level map of their own platform, classify each capability by investment class (differentiating, parity, commodity), condition and scope, and defend why the parity capabilities that carry keys (vehicle, account, usage, license) are shared first.

The chapter owns **capability map**, **heat map** and **shared capability**. It defines **Axleby's One Dossier capability map v1 (March 2027)** precisely, including its canonical counts, because [[one-platform-from-many-products]] defines v2 (December 2027) relative to it.

Productscape bricks covered: all 28 as the map (`rdwc`, `vidn`, `vhis`, `evsh`, `dmgc`, `mktd`, `valu`, `bpmc`, `dosr`, `occm`, `tapp`, `advf`, `dweb`, `admn`, `finc`, `rdwt`, `mats`, `impx`, `b2bt`, `vapi`, `fenr`, `mins`, `cool`, `fnnk`, `ctrv`, `iden`, `bill`, `dgov`), plus the eight capabilities the model lacks (identity resolution, ingestion and entity resolution, provenance and data quality, connected-vehicle data, DMS integration, events and webhooks, onboarding and configuration, observability and data operations).

## Audience

Chief and enterprise architects, CTOs and product directors of vehicle-data companies, dealer-software vendors and acquisitive groups who must decide what to share across products and where to invest, and who need a business-level artifact the board and CFO can read.

## Success criteria

- [ ] Defines capability, level 1/2/3, investment class, condition, scope and market flag in one table, and separates capabilities from systems, teams and products.
- [ ] Walks the reference model (28 blocks in five groups) with neutral names, states that it is the author's inference from public pages and never a company's architecture, and uses its inconsistencies (license checks at 3 blocks, metering at 5) as teaching points.
- [ ] Names the eight added capabilities with the reason and owning chapter, and the gaps deliberately left out (lease administration, marketplace payments, fraud as cross-cutting).
- [ ] Presents map v1 in full (6 domains, 39 capabilities, Axleby systems, class, condition, scope, market flag) with canonical counts that match the ledger line.
- [ ] Contains a promise table (latency, freshness, consistency, availability) for the shared capabilities on the critical path, with assumptions labeled.
- [ ] Uses dated public evidence (Cox Automotive 2014–2024, Auto Trader 2022–2025, CDK 2021) with an INFERENCE label where the reading goes beyond the sources.
- [ ] Covers how capability maps fail (org chart in disguise, duplicates, conflicting owners, incomplete, everything-differentiating, stale) with detection and recovery, and a trade-off table of mapping approaches.
- [ ] Shows which capabilities are market-specific and in what form (adapter, rule set, separate product), without a full "Across Markets" section.

## Non-goals

- Bounded contexts, entity–owner table and sources of truth ([[vehicle-bounded-contexts]]).
- Sourcing decisions per capability ([[build-buy-or-partner]]).
- Capability map v2 and the integration sequence ([[one-platform-from-many-products]]).
- Team design around capabilities ([[organizing-engineering]]).
- The block-by-block mapping of the reference model to chapters ([[domain-coverage]]).
- Economics behind the classes ([[dealer-and-data-economics]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Open Group's business-capabilities guide requires registration and was not read in full; the chapter cites it without quoting a definition. Ulrich Homann's 2006 MSDN paper is cited from secondary references.
- The "more than about a third differentiating" rule of thumb is the author's, labeled as an assumption; no published benchmark was found.
- Whether v2 should split register access into "plate lookups" (drifting to commodity) and "register transactions and validated mirror" (differentiating) is left to [[one-platform-from-many-products]].

## Decision log

- **2026-10-22** — Drew v1 at two levels only (6 domains, 39 capabilities) and left level 3 to v2, so that v2 has a defined place to add detail (valuation model vs serving, shared dossier timeline vs workflow screens).
- **2026-10-22** — Used two independent classifications (investment class and scope) plus a dated condition, because conflating "differentiating" with "shared" is what leaves parity capabilities such as accounts and metering duplicated.
- **2026-10-22** — Classified the vehicle dossier as shared (the book's thesis: the halves share the vehicle and the dossier) and kept consumer travel documents on the map as "not offered", consistent with Odolo's partner referrals in the ledger; mapped change-of-ownership prediction to Horizon.
- **2026-10-22** — Placed systems not yet built in March 2027 (Inlet, Hitch, Runway, Baseline, Meterline, Axleby ID, Gatekeeper) outside v1's system column, so v2 can show them arriving; Charter is shown "being built".

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-data-ecosystem]], [[dealer-and-data-economics]] — scenario, ecosystem map and economics the map builds on.
  - [[vehicle-identity]], [[registers-and-official-data]], [[specification-and-equipment]], [[vehicle-history]], [[valuation-engine]], [[listing-syndication]], [[dms-integration]], [[billing-and-metering]], [[data-licensing-and-governance]], [[identity-access-and-entitlements]] — owning chapters of mapped capabilities.
  - [[case-cox-automotive]], [[case-auto-trader-uk]], [[case-cdk-global]], [[case-vwe]], [[domain-coverage]].
- **External**
  - Cox Automotive formation release (2014), Bridge ID page (n.d., accessed 2026-10), PlatformCon talk (2024), Apollo customer story (n.d.).
  - Auto Trader Group FY2023 and FY2025 results (2023, 2025); CDK Global 10-K FY2021.
  - Regulation (EU) 2023/2854 (Data Act); RDW open data; TOGAF Series Guide: Business Capabilities.
  - Homann (2006); Evans, *Domain-Driven Design* (2003); Wardley, *Wardley Maps* (2016–2018).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: board is Axleby's (Harrowgate holds the majority), aligned identity and license-check latency assumptions with the owning chapters, clarified the class-by-scope cell, expanded VIN, B2B and DPIA. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
