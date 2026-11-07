---
status: accepted
revised: 2026-11-07
---

# Spec: Build, Buy or Assemble: Choosing and Changing Platforms

## Intent

Give a reader new to commerce architecture a way to make, or judge, the most expensive decision in the field: how to cover the commerce capability map with a suite, a hosted platform plus apps, a composable assembly, custom code or a mix, and how to price each option honestly over three years. The chapter's two durable moves are a rule for what to build (only what customers choose you for and nobody sells; buy the rest; own the joins) and a total-cost-of-ownership table that puts the lines vendors omit (people who own integrations, agency after the build, revenue at risk, exit) next to the subscription. Kestrel & Pine's February 2027 platform review and the Waypoint W4 decision ("stay and surround") are the spine, so the reader sees that keeping a hosted platform and adding an OMS, a PIM and an availability service beside it is a deliberate architecture, not indecision.

## Audience

Newcomers to commerce architecture. The role that benefits most is the engineering lead or architect asked, like Noor Visser, to recommend on a platform they did not choose; product managers and finance partners who must read a vendor quote and a TCO benefit next. All commerce terms (SaaS, suite, composable, MACH, headless, GMV, OMS, PIM, WMS, ERP, PSP, iPaaS, 3PL, POS) and architecture terms (TCO, lock-in, exit cost, system of record, ADR) are defined on first use.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The four shapes (suite, hosted platform plus apps, composable assembly, custom build) plus the two mixes (ERP-centred, specialist group) and the "stay and surround" shape are each explained in a paragraph a newcomer can follow, with a comparison table and a trade-off table.
- [x] The differentiation-against-commodity rule is stated and applied capability by capability to Kestrel & Pine in a table.
- [x] A worked three-year TCO table compares the three 2027 options with ledger prices (platform €2,300, agency €14,000, €2.6M spend, Waypoint €1.1M) and every non-ledger figure labeled as an assumption; the subscription line is shown to be the smallest.
- [x] Exit cost and lock-in are treated with dated evidence: Shopify's terms (2026-10-20) and the Data Act's switching rules (applicable 2025-09-12; no switching charges from 2027-01-12), with the open legal question stated as open.
- [x] At least two mermaid diagrams with captions; an "Across Scale Stages" table with the four ledger stages and a judgement; a "When it goes wrong" section with detection and recovery; Questions to ask.
- [x] The three take-away tiers are present and honest; the chapter closes with a hand-off to [[replatforming-and-migration]].
- [x] Article at or under 6,500 words before Sources and Evidence; the WHY IT MATTERS callout is two sentences; exactly three KEY POINTS.

## Non-goals

- The platform landscape itself, vendor by vendor, with pricing pages and the 2023–2026 timeline — [[commerce-platform-landscape]]; the composable movement's history — [[case-composable-movement]].
- How to migrate once the decision is made: strangler seams, parallel runs, cutover, rollback, the Target, Finish Line and M&S cases — [[replatforming-and-migration]].
- The scale stages as a model and the multi-brand platform decision — [[commerce-scaling-stages]].
- Ownership maps, vendor management, contracts and agency relationships in depth — [[organizing-commerce-engineering]].
- Architecture styles (monolith, microservices, composable as a style) — [[commerce-architecture-styles]]; app governance and the Forked Platform mechanics — [[extensibility-and-app-ecosystems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The OMS (with availability module) and PIM subscription figures (€4,500 and €1,800 a month) and the implementation figures (€320K, €110K, €150K) are this chapter's illustrative assumptions inside the €1.1M Waypoint budget; they were appended to the ledger so [[order-management]] and [[product-information]] can reuse them, but a reviewer should check those chapters did not set different figures in parallel.
- Whether hosted commerce platforms fall under the Data Act's switching provisions is unsettled as of November 2026; revisit when guidance or a first case appears.
- Suite pricing as "1–3% of GMV" is an industry belief relayed by a competitor's page, not a vendor statement; the TCO table labels it so. If a suite vendor publishes pricing, replace the assumption.

## Decision log

- **2026-11-07** — Built the chapter around the February 2027 review with three concrete proposals (agency: composable rebuild; ERP partner: suite; Noor: stay and surround) rather than an abstract taxonomy, so the TCO table has three real columns. Rejected a four-column table with custom build, because no one at a €48M merchant proposes it and the column would be filler.
- **2026-11-07** — Priced the TCO as incremental cost over today's run-rate, leaving out lines common to all options (ERP, WMS, connector, returns portal, iPaaS, payment processing), so the comparison is readable and the assumptions are few. Rejected a full absolute TCO, which would have required inventing salary and PSP figures the ledger does not hold.
- **2026-11-07** — Used the Marks & Spencer 2014 figure (M&S.com down 8.1% in one quarter after relaunch, trading statement of 8 July 2014) as the revenue-at-risk assumption rather than an invented percentage, and flagged its age.
- **2026-11-07** — Kept the "Across Scale Stages" section although Part X is outside the required range, because the build/buy/assemble answer changes with stage and the section is where that is said.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — prices, the 2026 spend, the Waypoint budget and W1–W5; `PLAN.md` contract 41; `_research/style-guide.md`.
  - `_research/brief-commerce-business-models.md` (Part 5: TCO components, replatforming stories, Data Act; Part 6.2: ADRs) and `_research/brief-platform-landscape.md` (Parts 1–4 and 6: categories, specialist layers, MACH, pricing models, vendor claims).
  - [[commerce-platform-landscape]], [[commerce-capability-map]], [[boundaries-and-systems-of-record]], [[replatforming-and-migration]], [[commerce-scaling-stages]], [[organizing-commerce-engineering]], [[meet-kestrel-and-pine]].
- **External**
  - Shopify, *Ecommerce Replatforming and Migration Guide for 2026* (2026-03-18) — the vendor's own cost list.
  - Shopify Terms of Service (2026-10-20); Shopify pricing and Plus plan pages (accessed 2026-11); Shopware, Saleor and BigCommerce pricing pages (accessed 2026-11) — pricing models and contract terms.
  - Regulation (EU) 2023/2854 (Data Act) — switching rights and charges.
  - commercetools (2026-01-21), Adobe Experience League (2026-10-21), Commerce.com SEC exhibit (2026-08-06), MACH Alliance (2026-02-18), TechCrunch (2025-02-26) — the vendors' turn to layers.
  - Nygard, *Documenting Architecture Decisions* (2011) — the ADR format.
  - CNBC/Reuters on Marks & Spencer (2014-07-08); InternetNews (2009) and MPR News (2011) on Target — the revenue-at-risk assumption and the build decision.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: February 2027 pitches aligned with ruling 13a (consultancy composable, agency headless; suite costed by Noor). *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
