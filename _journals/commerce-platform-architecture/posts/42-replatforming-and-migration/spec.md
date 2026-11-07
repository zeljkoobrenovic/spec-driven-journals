---
status: accepted
revised: 2026-11-07
---

# Spec: Moving Without Burning the Bridge: Replatforming and Migration

## Intent

Teach a reader new to commerce architecture how to move a platform, or a hub beside it, without a single cutover date and no way back. The chapter grounds the danger in three dated, sourced public failures (Target 2011, Finish Line 2012, Marks & Spencer 2014, with Hobbycraft 2013 as the avoided case), names the pattern (The Burned Bridge), and then builds the alternative: strangler seams by channel, capability and traffic slice; shadow and parallel runs with a reconciliation that explains differences; data migration treated as five separate migrations (products, customers, orders, gift cards and credit, URLs) plus the integrations; cutover criteria and a rehearsed rollback; the old owner kept operable through one peak. Kestrel & Pine's 2027 PIM and OMS introductions are the worked example, phased seam by seam around the Black Friday freeze, so the reader sees that "stay and surround" still involves migrations and that they are planned the same way.

## Audience

Newcomers to commerce architecture. The engineering lead or integration engineer who will plan or run a hub introduction or a replatforming benefits most; product managers, operations leads and finance partners who must sign off go/no-go criteria, gift-card balances and the change freeze benefit next. Terms defined on first use: replatforming, strangler fig, transitional architecture, event interception, divert the flow, legacy mimic, canary, dark launch, feature parity, parallel run, dual write, idempotency, cutover, rollback, change freeze, system of record, OMS, PIM, WMS, iPaaS, SKU, GTIN, EDI.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The Target (decision 2009-08-07; outages 2011-09-13 and 2011-10-25), Finish Line (switch 2012-11-19; reverted after 17 days; about $3M) and Marks & Spencer (statement 2014-07-08; M&S.com down 8.1%) cases are dated, sourced, flagged for evidence age, and their unconfirmed causes stated as unconfirmed.
- [x] The Burned Bridge is named and defined from the cases; the strangler approach is explained with Fowler (2004/2024) and the Thoughtworks patterns (2021/2024), with Zalando's 2015–2016 router-fronted rebuild as the public commerce example.
- [x] A requirements table by migration phase (shadow, parallel run, divert one seam, divert all, decommission) with owner, freshness, consistency check, latency and availability; parallel runs and dual writes distinguished, with the App That Wrote Stock as the warning.
- [x] A data-migration table covering products, prices, customers, orders, gift cards and credit, URLs and integrations, each with its trap and its check; order history imported as history, not re-created.
- [x] The Kestrel & Pine worked example gives the PIM (July–September 2027) and OMS (August 2027–January 2028) phases with dates, the smallest-channel-first order, the Black Friday 2027 freeze, and reconciliation findings labeled illustrative.
- [x] At least two mermaid diagrams (a strangler flowchart and a cutover sequence diagram) with captions; an "Across Scale Stages" table and judgement; a "When it goes wrong" section with detection and recovery; Questions to ask; the three take-away tiers; a hand-off to [[commerce-scaling-stages]].
- [x] Article at or under 6,500 words before Sources and Evidence; WHY IT MATTERS is two sentences; exactly three KEY POINTS.

## Non-goals

- Whether to replatform at all, the TCO of the options and exit cost — [[build-buy-or-assemble]].
- The OMS's and PIM's own design (state models, availability computation, product model) — [[order-management]], [[inventory-and-availability]], [[product-information]].
- Reconciliation and idempotency mechanics in depth — [[events-consistency-and-reconciliation]], [[integration-styles]]; API deprecation practice — [[api-contracts-and-versioning]].
- Peak planning and load testing for the migrated system — [[peak-load-and-reliability]], [[journey-peak-day]].
- The architectural histories of Amazon and Zalando beyond the migration shape — [[case-amazon]], [[case-zalando]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The OMS phase dates (shadow in August, parallel run 1–14 September, marketplace seam 15 September, D2C seam 13 October, freeze 15 November–5 December, wholesale seam 8 December, decommission January 2028) and the PIM phases (load July, DE storefront August, NL/BE and connector September) were appended to the ledger; [[order-management]] and [[product-information]] may have set their own; a reviewer should reconcile.
- Target's 2011 relaunch date is given by trade press as August 2011 (one outlet says 23 August); the chapter says "August 2011" and does not state a day. The root cause of the outages remains unconfirmed.
- Retail Week's Hobbycraft and M&S pieces are paywalled beyond the lead; the M&S figure is corroborated by CNBC/Reuters, the Hobbycraft quote rests on the brief's verification of the lead.

## Decision log

- **2026-11-07** — Opened with three documented failures rather than with method, because the reader needs to believe the Burned Bridge is real before investing in seams and reconciliations; chose only cases with a verifiable chain of events and refused ASOS and Boots, for which the brief found no sourced outcome.
- **2026-11-07** — Made the OMS introduction, not a hypothetical replatforming, the worked example, because W4 rules out replatforming and the OMS is the migration Kestrel & Pine actually runs in 2027; the marketplace channel (43,000 orders a year) moves first because it is the smallest.
- **2026-11-07** — Treated dual writes as the opposite of a parallel run rather than a variant, and tied the warning to the App That Wrote Stock, so the newcomer does not leave thinking "write to both" is the safe option.
- **2026-11-07** — Kept the "Across Scale Stages" section although Part X is outside the required range; the judgement that technique is constant while the migrated thing changes is the stage-specific content.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Waypoint W2, W3, W5; volumes; the stock reconciliation of May 2027; the App That Wrote Stock; the Deprecated Endpoint. `PLAN.md` contract 42; `_research/style-guide.md`.
  - `_research/brief-commerce-business-models.md` (Part 5.2–5.4: replatforming stories, strangler and legacy displacement, Data Act) and `_research/brief-cases-amazon-zalando.md` (B1, B4, Part C: Zalando's fragment-by-fragment rebuild, Connected Retail wind-down, incremental migration styles).
  - [[build-buy-or-assemble]], [[order-management]], [[product-information]], [[events-consistency-and-reconciliation]], [[integration-styles]], [[api-contracts-and-versioning]], [[peak-load-and-reliability]], [[meet-kestrel-and-pine]].
- **External**
  - InternetNews (2009-08-07), MPR News/AP (2011-09-13, 2011-10-25) — Target's build decision and outages.
  - Retail Dive (2013-01-08) — Finish Line's reversion to a platform "kept operable".
  - CNBC/Reuters (2014-07-08), Retail Week (2014-07-10) — Marks & Spencer's 8.1% fall; Retail Week (2013-02-19) — Hobbycraft's deferred launch.
  - Fowler, *Strangler Fig Application* (2024, orig. 2004); Cartwright, Horn, Lewis, *Patterns of Legacy Displacement* (2021, rev. 2024) — the method.
  - Zalando Engineering (2015-10-16, 2016-10-05); FashionUnited (2026-04-23) — the public commerce example and the channel retired with notice.
  - Help Net Security (2020) — Magento 1 end of life; Shopify (2026-03-18) — migration costs; Regulation (EU) 2023/2854 — exportable data.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: OMS order-number family aligned with chapter 13. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
