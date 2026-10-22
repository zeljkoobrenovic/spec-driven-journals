---
status: accepted
revised: 2026-10-22
---

# Spec: Who Owns What: Organizing Engineering for a Data and SaaS Platform

## Intent

Show which organizational design makes the book's architecture hold in a group that sells vehicle data and dealer software and was assembled by acquisition. The chapter applies Team Topologies to this domain: stream-aligned teams per dealer and data-client journey, data-product teams per vehicle-data domain, complicated-subsystem teams for identity resolution and valuation, platform teams for what every product would otherwise rebuild, and an enabling team that moves acquired products onto shared contracts. It defines ownership precisely (change authority, run responsibility, objective, external relationship, decision records), separates the **journey owner** from the **dependency owner**, and turns that split into adapter ownership, alert routing and on-call design for external dependencies. It covers architecture governance (advice process, decision records, forum, decision rights, ownership scorecard), product management for data products and the integration of acquired teams across five hubs. The reader should leave able to draw, test and govern a team map for a vehicle data and dealer SaaS platform.

Owns: **team topology (vehicle platform)**, **adapter ownership**, **journey owner / dependency owner**. Productscape bricks: none directly; this is a gap chapter **[ADDED]** that maps teams onto the bricks owned by other chapters.

## Audience

CTOs, chief architects, heads of engineering and platform leads of vehicle-data companies, dealer-software vendors and portals, especially groups integrating acquired products across countries. They know Team Topologies and SRE vocabulary; they need it applied to adapters, registers, DMS partners and data products.

## Success criteria

- [ ] Opens with an Axleby situation (the Zombie Golf seen as an ownership failure) and an April 2027 ownership census with numbers.
- [ ] Defines Conway's law, the four team types and three interaction modes with dated sources, the data-product team, and what "owns" means.
- [ ] Presents the 2027 team map (seven groups, about 300 engineers, five hubs) consistent with the ledger cast and systems, with a topology diagram.
- [ ] Compares adapter ownership models in a table and gives the adapter record fields with owners.
- [ ] Designs on-call for 75 external dependencies with rotation sizing (Google SRE), attribution-based routing, a sequence diagram, and working-time law (Matzak, C-344/19, BetrVG, WOR, FLSA, Polish Labour Code).
- [ ] Uses the DriveDesk Outage and the Lost Leads of Velto as tests of the new structure without contradicting their owning chapters.
- [ ] Covers governance (advice process, decision records, decision-rights table, forum diagram, ownership scorecard modeled on Cox's 2019 Well-Architected scorecard) and product management for data products.
- [ ] Includes failure handling, a trade-off table of org models, Across Markets, the Chief Architect's view and questions.

## Non-goals

- Portfolio integration sequencing and capability map v2 ([[one-platform-from-many-products]]).
- Sourcing decisions for adapters and aggregators ([[build-buy-or-partner]]).
- Migration mechanics for Connect XML and Lotwise Classic ([[modernizing-the-platform]]).
- SLO, dependency budget and observability design ([[reliability-and-dependencies]], [[observability-and-data-operations]]).
- The Cox company story ([[case-cox-automotive]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No automotive software group publishes its current team structure; the Cox, Auto Trader and AutoScout24 evidence is partial and partly old or vendor-authored.
- Belgian on-call and works-council rules and the post-Brexit UK treatment of EU working-time case law were not verified.
- The Polish Labour Code text was read from an unofficial consolidated source.

## Decision log

- **2026-10-22** — Opened with the Zombie Golf as an ownership failure rather than a technical one, so the chapter's question is "who owns the outcome", and used the DriveDesk Outage as the test of the new design.
- **2026-10-22** — Split ownership into journey owner and dependency owner; journey teams hold SLOs, integration teams hold adapters and partners; alerts route by attribution.
- **2026-10-22** — Chose few 24/7 rotations by harm class (platform SRE, integration duty, month-end register watch) over 24/7 per team, because all hubs share two time zones and EU working-time law limits tight stand-by.
- **2026-10-22** — Kept an Across Markets section although Part IX does not require it, because employment and co-determination rules change on-call and engineer metrics by country.

## Sources

- **Internal**
  - [[listing-syndication]], [[dms-integration]], [[leads-and-crm]], [[journey-lead-to-dms]], [[reliability-and-dependencies]], [[observability-and-data-operations]], [[case-cox-automotive]].
  - `_research/brief-platform-apis-operations.md`, `_research/brief-case-cox-cdk.md`, `_research/brief-case-autotrader-carfax-vwe.md`, `_research/scenario-ledger.md`.
- **External**
  - Conway (1968); Skelton and Pais, Team Topologies (2019); Dehghani (2019); Harmel-Law (2021); Nygard (2011); Google SRE book (2016).
  - Cox re:Invent 2019 session report; PlatformCon 2024; Apollo case study; Istio Auto Trader case study; AutoScout24 SLO post (2024).
  - CJEU C-518/15 (2018) and C-344/19 (2021); BetrVG §87; WOR art. 27; 29 CFR 785.17; Kodeks pracy art. 151⁵.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: 61 channel adapters; hedged the claim about pace versus documented cases. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
