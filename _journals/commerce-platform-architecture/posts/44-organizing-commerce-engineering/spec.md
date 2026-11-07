---
status: accepted
revised: 2026-11-07
---

# Spec: Who Builds and Who Owns: Teams, Vendors, Agencies and Governance

## Intent

Answer, for a merchant that buys most of its systems, who should own each system, integration and app, and how a small team works with an agency and a dozen vendors without losing control of the facts it sells on. The chapter makes the ownership map (one row per system, integration and app, with business owner, technical owner, builder and vendor, what it may write, contract, dependencies and monitoring) the merchant's first governance artifact; compares four team shapes (by system, by journey, by layer, agency-led) with Team Topologies' vocabulary and recommends journey teams plus an integration pair for ten to twenty people; states rules for agencies and partners from the public partner economics; gives a vendor card with dated versioning, deprecation, rate-limit, export and residency facts; describes governance light enough to be followed (ADRs, five standing rules, a weekly architecture hour); explains the merchant's product manager; covers environments, release management, feature flags and AI coding tools; and shows team shape by scale stage. After reading, a newcomer can draw an ownership map, choose a team shape for their size, and write the clauses that keep an agency or vendor from becoming a Lynchpin.

## Audience

Readers new to commerce architecture. The new engineering lead or head of digital who inherits an agency, a partner-built connector and a dozen vendor contracts benefits most; product managers and operations leads who must decide who to call when a flow fails benefit next. Terms defined on first use: own (the five duties), system of record, integration contract, ADR, sandbox, API version, stream-aligned team, platform team, scope, SLO and SLA, deprecation.

## Success criteria

- [x] The ownership map is specified as a table of columns with the reason for each, plus two rules (every row has an internal technical owner; one writer per fact); Kestrel & Pine's tallies (34 integrations: 14 iPaaS, 9 agency, 6 vendor, 5 unowned; 41 apps: 6 unused, 3 writing inventory) are consistent with the ledger and appended to it.
- [x] Four team-shape options are each described in a paragraph a newcomer can follow, compared in a trade-off table, and the recommendation (journey teams plus an integration pair) states its size conditions; Conway 1968, Team Topologies 2019, Vogels 2006, Jacobs 2020 and Uber 2020 are dated and age-flagged.
- [x] Agency and partner rules rest on the public partner economics (Shopify partner earnings and tiers, accessed 2026-11) and are labeled as the author's judgement where no study exists; the ERP partner's connector and the agency's nine scripts are handled in the Kestrel & Pine example.
- [x] A vendor card table carries dated facts: Shopify ToS 2026-10-20, quarterly API versions with twelve-month support, Adobe three-year support and 2027-06-01 enforcement, WooCommerce no-guarantee, rate limits by plan, Scripts retired 2026-06-30, Data Act switching from 2027-01-12 (open question flagged), SRE SLO/SLA, commercetools regions.
- [x] Governance section includes Nygard's ADR (2011), Waypoint W1–W8 as ADRs, a standing-rules table mapped to failure patterns, and the architecture hour; the product manager's role is stated as the order's journey vs the vendor's GMV.
- [x] Engineering practices cite Shopify development stores, Stripe sandboxes, Adobe Cloud Pro, Zalando's marked test orders (2020), Hodgson's toggles (2017) and the AI evidence (DORA 2024 and 2025, METR 2025, Shopify memo 2025) with the stability finding as the commerce-relevant one.
- [x] An "Across Scale Stages: When It Fits and When It Limits" table gives the team shape, integration ownership, what becomes necessary and warning signs per stage, with Kestrel & Pine's row and a judgement (change the team shape one stage before the landscape).
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; two mermaid diagrams with captions; "When it goes wrong" with detection and recovery; the three take-away tiers; Questions to ask; Sources and Evidence grouped and dated; article text within the 6,500-word cap.

## Non-goals

- The integration inventory and integration styles themselves — [[integration-styles]]; contracts, idempotency and reconciliation mechanics — [[events-consistency-and-reconciliation]]; API versioning and webhooks in depth — [[api-contracts-and-versioning]].
- App scopes, app review and the Forked Platform — [[extensibility-and-app-ecosystems]]; rate limits and tenancy — [[multi-tenancy-and-isolation]].
- Build, buy or assemble, total cost of ownership and exit cost — [[build-buy-or-assemble]]; the peak plan and switch-off list — [[peak-load-and-reliability]].
- The scale stages as a model — [[commerce-scaling-stages]]; the vendor-side organization of Shopify, Amazon and Zalando — [[part-11]].
- Agentic AI and what agents need from owners — [[ai-and-agentic-commerce]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No dated practitioner study of merchant–agency engineering practice in the Netherlands, Belgium or Germany was found; the agency rules are the author's judgement and say so.
- No vendor SLA document (Shopify Plus, commercetools, SAP) could be fetched; the chapter advises asking for the actual agreement rather than quoting uptime figures.
- Whether hosted commerce platforms are "data processing services" under the Data Act is open; the vendor card flags it.
- The 2027 team shape and the ownership-map tallies are new canonical Kestrel & Pine facts; chapters 24 (integration inventory) and 31 (app governance) should reuse them rather than restate different numbers.

## Decision log

- **2026-11-07** — Made the ownership map, not the team shape, the spine, because the contract names it as the chapter's owned term and because the Kestrel & Pine incidents attach to blank cells in a map more convincingly than to an organization chart.
- **2026-11-07** — Mapped Team Topologies to a merchant as journey teams plus an integration *pair* rather than an integration team, to avoid recommending the bottleneck the by-layer option warns of at 14 people; stated the under-eight-engineers condition.
- **2026-11-07** — Used Shopify's partner economics as the only verified evidence of agency incentives and avoided generalizing to other vendors' programs; the Hobbycraft 2022 example is presented as agency-sourced and outcome-free.
- **2026-11-07** — Kept the AI coding tools section brief and evidence-led (DORA, METR, the Shopify memo), with the stability finding as the commerce-specific lesson, rather than recommending tooling.
- **2026-11-07** — Appended the ownership-map tallies and the April 2027 team shape to the ledger so later chapters agree on counts and team names.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — team of 14, cast and owners, systems, 34 integrations, 41 apps, the Deprecated Endpoint, the Price Drift, the App That Wrote Stock, Waypoint W1–W8.
  - `PLAN.md` — contract 44 and neighbouring contracts 24, 26, 31, 33, 41, 43.
  - `_research/brief-commerce-business-models.md` — Team Topologies, Nygard, partner economics, vendor management, product management, AI tools.
  - `_research/brief-platform-engineering-scale.md` — Conway, Vogels, Zalando, Uber, environments, versioning, feature flags, team topologies applied, agencies, AI evidence.
  - [[commerce-scaling-stages]] — the stage definitions used in the stage table.
- **External**
  - Shopify Help Center (partner earnings, partner tiers, Script Editor), Shopify developer documentation (development stores, API versioning, rate limits), Shopify Terms of Service (2026).
  - Adobe Experience League (lifecycle policy, Cloud Pro architecture); WooCommerce developer documentation; Stripe documentation; commercetools documentation.
  - Conway (1968); Skelton and Pais, *Team Topologies* (2019); Nygard (2011); Hodgson (2017); Google SRE book (2017).
  - AWS blog on Vogels (2006); Jacobs (2020); Uber Engineering (2020); Zalando Engineering (2020).
  - DORA 2024 and 2025 reports; METR (2025); CNBC on the Shopify memo (2025).
  - Retail Technology Innovation Hub on Hobbycraft (2022); Regulation (EU) 2023/2854.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: unowned-integration counts dated per item 16, Deprecated Endpoint date and discovery aligned, app count per item 10. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
