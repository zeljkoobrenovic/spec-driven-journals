---
status: accepted
revised: 2026-10-22
---

# Spec: Reading the Market: Advert Harvesting, Sale Detection and Transaction Data

## Intent

Show chief architects how to build a market data lake that valuation, pricing and insight products can rely on, from sources the platform does not control and may not freely use. The chapter argues three things. **A de-listing is evidence of a sale, not a sale**: model listing lifecycles, cluster listings into market vehicles across portals, relists and rooftops, and infer outcomes with confidence, confirmed by register changes or first-party dealer sales where a market provides them. **Every observation carries its source and its rights**: the EU database right (*Innoweb* 2013, *Ryanair* 2015, *CV-Online* 2021), the UK and US positions, terms of use and competition law on dealer data decide what may be harvested and shown, so provenance and rights tags per observation and a purge path are architecture. **Publish coverage with every statistic**: one match rate hides where the market is invisible; stand-time needs survival estimation; segment statistics need minimum evidence and fallbacks. After reading, the reader can define a source policy, an outcome-state model for sale detection, the metric definitions and a coverage contract for their own platform.

Productscape bricks covered: `mktd` (Market and Transaction Data Lake: advert harvester, ownership-change ingest, listing matcher, market warehouse, portal data adapter, market query API). Touches `valu` and `mins` only as consumers.

## Audience

Chief and principal architects, data and ML leads, and product directors at vehicle-data companies, dealer-software vendors, portals and lessors who build or buy market data. They know data lakes and entity resolution. They need the automotive specifics: what each source sees, how portals duplicate each other, what registers reveal per country, and where the legal lines run.

## Success criteria

- [x] Defines the owned terms: market data lake, sale detection, stand-time (distinct from days-to-turn), market days' supply; plus market observation, listing, market vehicle, segment and coverage.
- [x] Works "Pulse and the 61 percent match rate" with ledger-consistent numbers (2.3 million observations a day, 61% match) broken down by market and source, and a worked Dutch de-listing audit with an explicit cancellation-of-errors example.
- [x] Covers legal limits with primary sources: Directive 96/9/EC, *Innoweb*, *Ryanair*, *CV-Online*, UK SI 1997/3032 reg. 16, *Feist*, *hiQ*, EU Horizontal Guidelines 2023 on information exchange; with a not-legal-advice caveat.
- [x] Covers portal consolidation (AutoScout24 with AutoTrack and Gaspedaal.nl, November 2025; shared and exported listings) and its effect on duplicates and source concentration.
- [x] Gives an architecture with components, a requirements table and three mermaid diagrams (duplicate sources, architecture, outcome states).
- [x] Covers failure handling: missing harvests, upstream outages (Cox's CDK-outage normalization; DriveDesk Outage), conflicting observations, incomplete records, late corrections, source withdrawal, idempotent retries.
- [x] Includes trade-off tables (sources, sale definitions) and "Across Markets: What Changes by Country" with NL, BE, DE, UK and US columns.

## Non-goals

- Matching tiers, landing and quarantine mechanics ([[ingestion-and-entity-resolution]]); VIN and plate identity ([[vehicle-identity]]); the register mirror ([[registers-and-official-data]]).
- How valuations use comparables and drift signals ([[valuation-engine]]); dealer price signals ([[used-car-pricing]]); insight products for data clients ([[data-products-and-insights]]).
- License register and enforcement mechanics ([[data-licensing-and-governance]]); personal-data retention ([[privacy-and-retention]]).
- Channel publishing and delete semantics ([[listing-syndication]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No provider publishes how it infers sales from de-listings or the precision of that inference; revisit if one does.
- Whether Belgian per-vehicle registration changes are available to market-data providers was not verified.
- UK and US competition-law treatment of dealer price aggregation was not reviewed.
- Whether the Netherlands' consolidated portal group will restrict data exports or feeds after November 2025 is open; watch AutoScout24's changelog.

## Decision log

- **2026-10-22** — Set the scene as a February–April 2027 audit triggered by the EV Overvaluation review, so the chapter hands cleanly to [[valuation-engine]] and reuses its leading-signal finding rather than inventing a new incident.
- **2026-10-22** — Decomposed the ledger's 61% by market (NL 86%, BE 40%, DE 38%, UK 73%) and source (1.55M harvested, 0.35M partner feeds, 0.40M first-party), and appended these to the ledger as canonical.
- **2026-10-22** — Kept Axleby's harvesting sources generic ("a portal group") and made the real portals appear only in documented facts, so no reader takes Axleby's fictional harvest as a claim about real portals' data.
- **2026-10-22** — Excluded Axleby Trade's customer transactions from market statistics, to model the purpose rule that [[data-licensing-and-governance]] enforces.

## Sources

- **Internal**
  - [[meet-axleby]] — Pulse volumes and the 61% match rate.
  - [[valuation-engine]] — the EV Overvaluation and Pulse's leading signals.
  - [[ingestion-and-entity-resolution]] — matching tiers and Inlet.
  - [[listing-syndication]] — Relay and portal-as-syndicator channels.
  - [[case-vwe]], [[case-auto-trader-uk]], [[case-cox-automotive]] — market structure and data moats.
- **External**
  - Directive 96/9/EC; CJEU C-202/12 (2013), C-30/14 (2015), C-762/19 (2021); UK SI 1997/3032; *Feist* (1991); Proskauer on *hiQ* (2022).
  - European Commission Horizontal Guidelines (2023), paras 391–394.
  - Cox Automotive used retail sales December 2025 (2026) and days' supply (2022); Manheim MMR Help (2026); Auto Trader UK Vehicle Metrics (2024–26) and RPI June 2023.
  - Emerce (2025); AutoScout24 Listing Creation API (n.d., to 2026-10); Bundeskartellamt (2026).
  - RDW open data metadata (2026); KBA *Besitzumschreibungen* (n.d.); SMMT used car sales (n.d.); DVLA INF266 (2022).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: flagged two sources older than three years (Cox 2022 days' supply, Auto Trader 2023 index method); relabeled the segment minimum-evidence rule as an Axleby rule, not an assumption. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: One Dossier request put to the company board (March 2027), not an architecture board, which first met in April 2027. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
