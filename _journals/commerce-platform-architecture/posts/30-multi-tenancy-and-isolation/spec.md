---
status: accepted
revised: 2026-11-07
---

# Spec: Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation

## Intent

Explain to a reader new to commerce architecture how a hosted commerce platform serves thousands of merchants on shared systems (pool, silo and bridge models; tenant identifiers, routing, pods and shards; governor limits; regions) and, above all, why a merchant should care: the rate limit is the tenancy mechanism a merchant meets, every app and connector spends from one per-store budget, the noisiest neighbour on a peak day is often the merchant's own app, and every specialist SaaS the merchant rents is a tenancy arrangement whose peak day is shared. After reading, the reader can inventory the spenders of their API budget, decide whether several markets or brands belong in one tenant or several, and put four questions to every vendor: unit of isolation, limits and their changes, region, busiest day.

## Audience

Newcomers to commerce architecture. The integration engineer or engineering lead preparing a peak plan on a hosted platform benefits most; the product manager or executive deciding between one tenant and several for new countries or brands benefits next. The chapter assumes general software literacy and defines tenant, multi-tenancy, isolation, sharding, pod, rate limit, noisy neighbour, pool, silo, bridge, governor limit, data residency, webhook, app, merchant of record, WMS, OMS, PIM, PSP and iPaaS where they first appear.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The three tenancy models are defined from the AWS SaaS Lens, with a diagram, before any vendor example; the noisy-neighbour problem is tied to pooling.
- [x] Shopify's pods and shard balancing (2018, 2021), Salesforce's metadata-driven pool and governor limits, and commercetools' projects and regions are reported with dates, evidence ages and a labeled inference where the public record stops (post-2021 pod topology).
- [x] Rate limits are presented as a tenancy tool with a table of four published models (Shopify, Amazon SP-API, BigCommerce, commercetools) dated November 2026 and flagged volatile, and the merchant consequence (per app per store; the vendor may lower limits; checkout and buyers protected first) is explicit.
- [x] A requirements table covers four flows of Eva's order (browsing, checkout, order to WMS, stock sync) with who owns capacity, what is metered, what the merchant controls and peak behaviour.
- [x] The one-tenant-or-many decision has an options table and a stated rule; specialist SaaS tenancy (WMS, returns, PIM, connector) and residency per component are covered; the four vendor questions are stated.
- [x] The Kestrel & Pine thread agrees with the ledger and with [[peak-load-and-reliability]]: the order flow throttled by the WMS vendor's limit and sharing the platform's per-app-per-store budget with the apps, the 2027 plan's 60 orders a minute forecast, W1, W2, W5, the app audit; new illustrative figures (budget shares, the WMS limit, the EU region, one tenant confirmed) are labeled and appended to the ledger.
- [x] "Across Scale Stages: When It Fits and When It Limits" with a specific table and judgement; three mermaid diagrams with captions; "When it goes wrong" with detection and recovery; the three take-away tiers; eight Questions to ask; a hand-off to [[extensibility-and-app-ecosystems]]; article at or under 6,500 words including tables.

## Non-goals

- Peak planning, load testing, queues, backpressure and the degradation ladder — [[peak-load-and-reliability]] and [[journey-peak-day]].
- Apps, scopes, app review and app governance — [[extensibility-and-app-ecosystems]]; API versioning and webhook contracts in depth — [[api-contracts-and-versioning]].
- Internal architecture styles (monolith, microservices, composable) — [[commerce-architecture-styles]].
- GDPR, controller and processor roles, cross-border transfers — [[privacy-and-customer-data]]; the multi-brand platform decision as a strategy question — [[commerce-scaling-stages]].
- Shopify as a full case — [[case-shopify]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Shopify's pod topology after the Google Cloud migration and current pod or shard counts are undocumented (last first-party description 2021); the chapter labels this as an inference and a reviewer should check for newer posts.
- All rate-limit figures are volatile; the chapter dates them to November 2026. A revision should re-check Shopify, Amazon SP-API, BigCommerce and commercetools pages.
- The illustrative WMS limit (about 60 calls a minute per customer) and budget shares (about 55% stock sync and apps, 20% order flow, about 1,900 throttles) were chosen to agree with chapter 33's account; if [[journey-peak-day]] quantifies the evening differently, the ledger line should be reconciled.

## Decision log

- **2026-11-07** — Opened with the merchant's side (two rate limits on one evening) rather than with the vendor's mechanisms, because the contract asks the chapter to explain why a merchant should care, not only how vendors build it; vendor mechanisms follow as the machinery behind the error code.
- **2026-11-07** — Treated the rate limit as the central tenancy concept for merchants and gave it a four-vendor table, rather than organizing the chapter around pods, which merchants cannot see or influence.
- **2026-11-07** — Aligned the Kestrel & Pine thread with chapter 33's canonical account (the order flow throttled by the WMS vendor's limit, sharing the platform budget with every installed app) and added only illustrative shares and the per-component region list, rather than inventing a separate incident.
- **2026-11-07** — Included specialist SaaS tenancy (WMS, returns portal, PIM) as a section of its own, with Picqer's public per-order pricing as the example of volume metering, because the contract names "tenancy in specialist SaaS" and the Black Friday throttle came from the WMS side.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the systems landscape, the Black Friday figures, the apps, W1, W2, W5.
  - [[peak-load-and-reliability]] — the canonical account of the order flow and the 2027 peak plan this chapter must agree with.
  - `_research/brief-platform-engineering-scale.md` (Part 2 and 5.1) and `_research/brief-shopify.md` (Parts 1, 2.3, 4.6, 5.4, 5.6) — the dated vendor evidence; `_research/brief-platform-landscape.md` (1.2, 1.6, Part 2) — Adobe's deployment options, Shopware's plugin rule and Picqer's pricing.
- **External**
  - AWS Well-Architected SaaS Lens, *Silo, pool, and bridge models* and *Noisy neighbor* (accessed 2026-11) — the tenancy vocabulary.
  - Shopify Engineering, *A Pods Architecture to Allow Shopify to Scale* (2018) and *MySQL Database Shard Balancing at Terabyte Scale* (2021); Shopify 10-K FY2025 (2026) — pods, shards, shop moves, "single branch", the merchant definition.
  - Shopify developer documentation on rate limits, the Storefront API, webhooks and Markets (accessed 2026-11); the 2018 flash-sale changelog — the merchant-facing mechanisms.
  - Salesforce Architects, *Platform Multitenant Architecture* (accessed 2026-11); commercetools *General Concepts* and *API Limits* (accessed 2026-11); Amazon SP-API *Usage Plans and Rate Limits* (accessed 2026-11); BigCommerce *API rate limits* (accessed 2026-11) — the other vendors' models.
  - Adobe Experience League (2026), Shopware developer documentation (accessed 2026-11), Picqer pricing (accessed 2026-11) — the silo-to-pool spectrum and volume metering.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: expanded SaaS, AWS, ERP, OMS, PIM, 3PL and HTTP 429, corrected the Shopify stability quote ('may'), aligned the 2027 fallback with the ten-unit marketplace buffer, FY2025 report naming, American spelling, timetoread. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
