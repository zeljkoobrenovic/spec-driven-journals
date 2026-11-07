---
status: accepted
revised: 2026-11-07
---

# Spec: What Changes at Each Scale: From First Store to Group

## Intent

Give the reader one map of the four scale stages (Starting, Growing, Omnichannel, Group) that the rest of the book refers to, so that the "Across Scale Stages" tables of Parts II–VIII can be read as rows of a single picture. The chapter defines a stage as a shape (channels and stock locations), not a revenue band; shows per stage the typical systems, where order and stock truth live, the integration style, who builds, the fees and thresholds met, the decisions that become necessary, the failure patterns that strike and the signals of transition; works the Group stage's share-or-separate question for multi-brand and multi-country groups; and prices Kestrel & Pine's own path 2016–2027 so the reader sees that most Omnichannel incidents are Growing-stage designs still running. After reading, a newcomer can place a merchant on the map by shape, name the signals that a stage is ending, and sort a program's decisions by the stage they belong to.

## Audience

Readers new to commerce architecture. The engineering lead or architect who, like Noor Visser, inherits systems bought at earlier stages and must explain to a board which decisions are for the company it is benefits most; product managers and consultants who need to read a vendor's price list as a map of expectations benefit next. Every commerce and architecture term the chapter uses (channel, stock location, 3PL, POS, ERP, OMS, PIM, WMS, EDI, GMV, system of record, iPaaS, tenant) is defined in a clause when it first appears.

## Success criteria

- [x] One big stage-by-stage table is the centrepiece, with the four ledger stages as columns and rows for shape, channels, storefront, order record, stock truth, product data, fulfillment, finance, integration style, team, fees, peak, necessary decisions, failure patterns, transition signals and Kestrel & Pine's years; every row links to the chapter that owns it.
- [x] Stages are defined by shape, with the ledger's revenue bands presented as markers; vendor tiering evidence (Shopify plans and gateway fee, Shopware's €1M GMV line, BigCommerce's GMV-assigned tiers) is dated "accessed 2026-11" and the mechanism, not the numbers, is the lesson.
- [x] A requirements table by stage for stock, order status and price states how fresh each fact must be, with illustrative latencies labeled as assumptions and ledger incidents as the failures.
- [x] Each stage has its own section with dated public evidence (Shopify 10-K 2025, Business Central connector 2026, Eurostat 2024 EDI share, Target 10-K 2025, Akeneo guidance, Fowler 2015, Shopify 2019, MACH 2026, VF 10-K 2026, Zalando AR 2025, Jacobs 2020, Uber 2020), with sources older than three years flagged.
- [x] A transition-signals table maps each signal to the failure pattern it precedes and to a Kestrel & Pine incident; a Group-stage decision table says what to share and what to keep separate, with conditions.
- [x] Kestrel & Pine's path is priced from the ledger (the four incidents' direct cost, about €138,000; the illustrative €135,000-per-half-point payment-fee arithmetic on €27.0M online revenue), and the April 2027 stage map scene is consistent with Waypoint and the 2029 review.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] Two mermaid diagrams with captions (the four stages with leftovers; the transition state diagram); "When it goes wrong" covers too early, too late and sideways with detection and recovery; the three take-away tiers are present; Questions to ask; Sources and Evidence grouped and dated; article text within the 6,500-word cap.

## Non-goals

- The economics of each business model and the per-order unit economics — [[commerce-business-models]] owns them; this chapter uses them only as fee thresholds.
- The mechanics of any single capability's scale table (ATP, OMS, PIM, WMS, EDI, integration standards) — owned by [[inventory-and-availability]], [[order-management]], [[product-information]], [[warehouse-and-fulfillment]], [[edi-and-e-invoicing]] and [[events-consistency-and-reconciliation]].
- The build/buy/assemble decision and total cost of ownership — [[build-buy-or-assemble]]; replatforming and migration mechanics — [[replatforming-and-migration]]; architecture styles and the Giant's Boots in depth — [[commerce-architecture-styles]].
- Team shape by stage beyond one row of the map — [[organizing-commerce-engineering]].
- Tenancy and extensibility at vendor scale — [[multi-tenancy-and-isolation]], [[extensibility-and-app-ecosystems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public survey of commerce system counts or team sizes by revenue band was found; the map's shapes are a composite and the chapter says so. A reviewer may know a primary source (Avasant's retail chapter is paywalled).
- The 2–4% retail IT-spend range is judgement from secondary sources; Kestrel & Pine's 5.4% is presented against it as a judgement, not a benchmark.
- Whether hosted commerce platforms are "data processing services" under the Data Act (switching charges prohibited from 12 January 2027) is an open legal question; the chapter presents it as such.
- Later chapters may add stage-specific facts (illustrative latencies, 2027 peak-plan numbers) that a review pass should fold into the map.

## Decision log

- **2026-11-07** — Built the map from the ledger's stage definitions, the briefs' evidence (fee cliffs, plan thresholds, OMS/PIM/WMS triggers) and Kestrel & Pine's own path rather than from other chapters' tables, because most of those chapters do not exist yet; rows are linked to their owning chapters so a later pass can reconcile.
- **2026-11-07** — Chose one big sixteen-row table over four per-stage tables, as the contract asks, and added a separate requirements-by-stage table and a transition-signals table rather than overloading the map's cells.
- **2026-11-07** — Set the Kestrel & Pine scene as an April 2027 board "stage map" that places the company in stage 3 and names the stage-4 signals as not planned for 2027–2028, so the chapter can discuss the Group stage without contradicting Waypoint's scope or the 2029 review; appended to the ledger.
- **2026-11-07** — Used Zalando's ABOUT YOU consolidation and VF Corporation's multi-brand DTC figure as the only real-company Group-stage evidence, and Jacobs 2020 and Uber 2020 as cautions, with evidence-age flags; declined to infer any company's internal multi-brand architecture.
- **2026-11-07** — Did not use a required "Across Scale Stages" heading, since the whole chapter is that section for the book; the centrepiece heading says so.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — stages, systems, incidents, Waypoint, costs, timeline.
  - `PLAN.md` — contract 43 and the owning chapters for each row.
  - `_research/brief-commerce-business-models.md` — vendor tiers, OMS/PIM/WMS triggers, IT-spend caveat, Data Act, team-shape judgement.
  - `_research/brief-platform-landscape.md` — pricing models and thresholds, specialist layers, MACH survey, the composable turn.
  - `_research/brief-platform-engineering-scale.md` — Fowler, Shopify, Zalando, Uber, Segment evidence; stage implications.
  - [[meet-kestrel-and-pine]] — the growth timeline by stage.
- **External**
  - Shopify pricing, Plus plan and enterprise pages; Shopify 10-K FY2025 — plan distribution and fee tiers.
  - Shopware and BigCommerce pricing pages; Picqer pricing — GMV and per-order thresholds.
  - Eurostat enterprise e-commerce statistics (2024 data) — EDI-type vs web sales.
  - Target 10-K FY2025; VF Corporation 10-K FY2026; Zalando Annual Report 2025 — omnichannel and group evidence.
  - Microsoft Learn, Business Central Shopify Connector (2026) — ERP-as-hub at the Growing stage.
  - Akeneo, "Top 3 signs you need a PIM" — PIM triggers (vendor content).
  - Fowler, *MonolithFirst* (2015); Shopify Engineering (2019); Jacobs (2020); Uber Engineering (2020); Segment (2018); MACH Alliance research (2026) — style and scale cautions.
  - Regulation (EU) 2023/2854 (Data Act) — switching charges.
  - Avasant, IT Spending and Staffing Benchmarks 2025/2026, Retail — benchmark exists, paywalled.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: incident attribution made consistent (eight of ten), incident-cost period corrected, American spelling. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
