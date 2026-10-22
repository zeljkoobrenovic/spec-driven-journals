---
status: accepted
revised: 2026-10-22
---

# Spec: The Stock Book: Inventory Management and the Vehicle Dossier

## Intent

Answer the question: **what is the system of record for a dealer's car while it is in stock, and how should its lifecycle be modeled?** The chapter separates the shared vehicle (keyed by the AVK) from the tenant's stock item (one stay), defines the vehicle dossier as the aggregate that every dealer module hangs on, models the stock lifecycle as a small commercial state machine with parallel tracks (preparation, advertising, register, financing), and settles ownership with the DMS field by field. After reading, an architect can draw the dossier's boundary, write its state table and guards, define field ownership for a DMS integration, and design for concurrent writers and a DMS outage.

Productscape bricks covered: `dosr` (Vehicle Dossier and Workflow Hub: dossier store, orchestrator, timeline, documents) and `occm` (stock store: stock items, cost, target margin, price history). The chapter argues for one consistency boundary for stock item and dossier, with pricing advice and signals outside it.

Owns: **vehicle dossier**, **stock lifecycle**, **stock item**.

## Audience

Chief architects, principal engineers and product leaders of dealer-software vendors and dealer groups who must decide what their stock system owns, how it relates to the DMS, and how modules (pricing, syndication, deals, register transactions) attach to it.

## Success criteria

- [ ] Reader can state the difference between vehicle, stock item and vehicle dossier, with keys, owners and lifetimes, and why the stock item references the vehicle by AVK, not plate.
- [ ] Reader can apply "reference current facts, snapshot decision inputs" and explain how it prevents The Sticky Error.
- [ ] Reader can draw the commercial lifecycle (nine states, guards, events) and explain why advertising, preparation, register and financing are tracks, and how Reserved/Sold/Written off force advertising to "withdrawn" in the same transaction.
- [ ] Reader can distinguish location, rooftop and legal-entity moves and model each.
- [ ] Reader can fill a field-ownership table for an independent without a DMS and a franchised dealer with one, and explain why Reserved is always dossier-owned.
- [ ] Article includes an Axleby worked example with ledger-consistent numbers (the Octavia, the Q1 2027 audit, the DriveDesk Outage), a requirements table, trade-off tables, an Across Markets table with sourced rows, three or more mermaid diagrams, failure handling and Questions to ask.
- [ ] Every company and regulatory claim carries a dated source; Axleby numbers and latency targets are labeled.

## Non-goals

- Appraisal, maximum purchase price and offers ([[vehicle-acquisition]]).
- Price setting, repricing and signals ([[used-car-pricing]]).
- Advert content and channel sync mechanics ([[merchandising]], [[listing-syndication]]).
- Deals, margin-scheme invoicing and financing ([[deals-and-sales-documents]]).
- Register transaction mechanics and retry queues ([[registration-and-trade-services]]).
- DMS adapter design, certification and access history ([[dms-integration]]).
- Tenant hierarchy and isolation in depth ([[tenancy-and-dealer-groups]]); retention schedules ([[privacy-and-retention]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Belgian stock register status: no trade-stock register comparable to the Dutch *bedrijfsvoorraad* was found; whether Belgian plates follow the holder rather than the car was not verified in this session (web-search quota exhausted). The market table avoids the claim.
- UK and US trade plates are mentioned but not examined.
- German "stock is commonly deregistered" is labeled industry practice; no primary statistic.

## Decision log

- **2026-10-22** — Removed "advertised" from the commercial state machine and made it a track, against the dealer vocabulary of ten states, because a car is routinely advertised while in reconditioning; the coupling rule (Reserved/Sold/Written off force "withdrawn") ties it back to the Zombie Golf.
- **2026-10-22** — Chose one consistency boundary for stock item and dossier, departing from the Productscape split of `dosr` and `occm`, because the lifecycle guards span state, cost and timeline; pricing stays outside.
- **2026-10-22** — Chose a same-transaction timeline over full event sourcing, given the Lotwise Classic migration path; event sourcing stays as an option in the trade-off table.
- **2026-10-22** — Chose field-level system-of-record over dossier-only or DMS-only, with Reserved always dossier-owned and Sold DMS-owned for franchised dealers.

## Sources

- **Internal**
  - [[meet-axleby]] — Velto, DriveDesk, Lotwise Classic, One Dossier timing, Zombie Golf and DriveDesk Outage.
  - [[vehicle-identity]] — AVK and plate assignments.
  - [[dms-integration]], [[listing-syndication]], [[deals-and-sales-documents]] — neighboring owners.
  - `_research/brief-dealer-workflows-economics.md`, `_research/brief-dms-integration.md`, `_research/productscape-digest.md` (bricks `dosr`, `occm`).
- **External**
  - AutoNation 10-K 2025 (2026), CarMax 10-K FY2026 (2026), Carvana 10-K 2025 (2026), Sonic 10-Q Q2 2024, AutoNation 10-Q Q2 2024 — cost per car, recon hubs, inventory system entry, validation before resync.
  - Directive 2006/112/EC; HMRC margin-scheme guidance (2021); Consumer Rights Act 2015 s22; 49 CFR 580.8; FTC Used Car Rule guide; FZV §16 and §41; Ondernemersplein *erkenning bedrijfsvoorraad*; Vlaanderen.be *handelaarsplaat*; Car-Pass FAQ.
  - Vaughn Vernon, *Effective Aggregate Design* (2011) — aggregate boundaries around consistency rules.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned Reserved/Sold with items 24 and 31 (signing reserves; Sold on conditions met and invoice), tenant vs legal entity, DMS accounting stock unit, Velto entity naming; American spelling. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (toward, neighboring). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
