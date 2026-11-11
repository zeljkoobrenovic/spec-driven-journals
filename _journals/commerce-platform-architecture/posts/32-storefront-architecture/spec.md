---
status: accepted
revised: 2026-11-09
---

# Spec: Delivering the Storefront: Themes, Headless, Rendering and Performance

## Intent

Give a newcomer a working model of the storefront as an architectural component: a renderer of facts other systems own (catalog, prices, promotions, availability, search, content, cart), delivered through one of three rendering models (theme rendered by the platform; headless on the vendor's runtime; headless anywhere), under all of which checkout stays on the platform. The chapter's operating rule is "cache the shell, fetch the promise": content pages are cacheable per market, promises (price for an account, live stock, cart) are fetched live, and that split decides both ordinary performance and peak-day survival. It presents the Core Web Vitals and the business evidence behind them with dates and caveats, accessibility as a dated legal requirement, and a decision rule for headless (a shared front end across brands or countries, a content-led site, or a B2B portal the theme cannot express; never speed alone). The Kestrel & Pine thread is the headless rebuild the agency proposed in February 2027 and Noor Visser declined after measuring the storefront.

Technical SEO belongs to the storefront contract too: explain how public product pages become discoverable, how rendering and fresh product data support that, and who owns URLs, crawl controls, localization and product retirement. Keep the addition compact by shortening repeated rendering-model explanations; preserve the existing evidence and scenario.

## Audience

Readers new to commerce architecture. The engineer or product manager who receives a headless proposal from an agency, and the leader who must approve it, benefit most; the storefront engineer who inherits an agency-customized theme is the second reader. Terms defined in the chapter: storefront, theme, headless, storefront API, server-side vs client-side rendering, edge cache and CDN, incremental static regeneration and request collapsing, Core Web Vitals (LCP, INP, CLS), Lighthouse, CMS, PWA, WCAG, the European Accessibility Act.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The three rendering models are explained in plain words with dated vendor examples (Shopify's Storefront Renderer 2020 and Hydrogen/Oxygen docs 2026-10; BigCommerce Stencil; Salesforce PWA Kit; Adobe Cloud Service October 2026; Next.js Commerce; Alokai), and the chapter states explicitly that checkout stays on the platform under all three.
- [x] "Cache the shell, fetch the promise" is shown as a sequence diagram on Eva's product page and as a requirements table per page type (fresh, consistent, fast, peak-day posture), tying the Price Drift and the Oversell to cached promises.
- [x] Core Web Vitals carry their current thresholds and dates (web.dev updated 31 October 2024; INP since 12 March 2024), Google's own wording on ranking, and the business evidence with its caveats (Deloitte 2020 as six years old and commissioned; web.dev cases as self-selected).
- [x] A self-contained technical SEO section defines crawling, indexing and the relevant controls before examples; covers links and sitemaps, rendering, variants and filters, structured product data, localized pages, stock changes and retirement, ownership and monitoring; cites current primary guidance and links to product information, search and migration.
- [x] Accessibility appears as a dated obligation (WCAG 2.2, 12 December 2024; EAA application 28 June 2025; microenterprise exemption) with Kestrel & Pine placed in scope and its B2B portal out of consumer scope.
- [x] The trade-off table, the "Across Scale Stages" table and judgement, a "When it goes wrong" table, the three take-away tiers, Questions to ask and a hand-off to [[peak-load-and-reliability]] are present.
- [x] The Kestrel & Pine worked example gives the February 2027 proposal (illustrative €240,000, nine months), the measured vitals (LCP 2.1 s, INP 310 ms, CLS 0.08, illustrative), the four-part decision, the June 2027 result and the link to W4 and the 2029 review, consistent with the ledger.
- [x] Prose inside the 6,500-word cap: about 6,250 words excluding front matter and URL destinations.

## Non-goals

- On-site search relevance, filter behavior and merchandising — [[commerce-search-and-discovery]]; this chapter covers the resulting URLs' discoverability.
- Pricing display rules and tax-inclusive pricing — [[pricing-architecture]].
- The availability service and stock badges' source of truth — [[inventory-and-availability]].
- Cart, checkout orchestration and checkout extensibility — [[cart-and-checkout]].
- Extension mechanisms, app scopes and app governance — [[extensibility-and-app-ecosystems]]; this chapter only treats app scripts as a performance cause.
- Load testing, degradation ladders and the peak plan — [[peak-load-and-reliability]]; this chapter only establishes cacheability as the storefront's contribution.
- National transposition and enforcement of the Accessibility Act — [[commerce-regulation]].
- Agentic channels and catalog feeds for AI agents — [[ai-and-agentic-commerce]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The illustrative Core Web Vitals, the €240,000 proposal and the €38,000 performance pass are new ledger facts appended by this chapter; [[build-buy-or-assemble]] records the February 2027 platform review with its own illustrative figures, and a review pass should confirm the two February decisions read as one month's work.
- The 2027 peak plan's "hide the stock count, show in stock / low stock from a per-channel buffer" is stated here as the storefront's part; [[journey-peak-day]] and [[peak-load-and-reliability]] should carry the same wording.
- Hydrogen's framework list and Oxygen's plan availability are volatile; re-verify in a 2027 revision.

## Decision log

- **2026-11-09** — Add technical SEO as a storefront responsibility, with links from product information, search and migration. Distinguish a crawlable product snapshot from the live purchase validation; do not imply Google cannot execute JavaScript or that every retired URL should redirect.
- **2026-11-07** — Framed the chapter around "the storefront owns no fact" and the cache/promise split rather than around framework comparison, because the newcomer's decision is organizational (who renders, who runs it, what is fetched live), not which JavaScript framework to pick.
- **2026-11-07** — Put the performance evidence in one section with dates and caveats, and made "never for speed alone" the headless rule, because the agency pitch in the ledger scene leads with speed and the public evidence cannot support that lead.
- **2026-11-07** — Kept accessibility inside the chapter as a storefront requirement (theme and app blocks) rather than deferring it entirely to the regulation chapter, since the EAA's June 2025 date is the one storefront deadline a Dutch merchant of Kestrel & Pine's size cannot skip.
- **2026-11-07** — Chose three mermaid diagrams (dependencies, rendering models, the cached-page sequence) and no architecture diagram of a specific framework, keeping the chapter platform-neutral.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — the three storefronts in one tenant, the agency, the 41 apps, the 2026 peak hour, W1, W3, W4, Eva's jacket.
  - `_research/brief-platform-engineering-scale.md` (Part 4) — themes, headless frameworks, ISR, Core Web Vitals evidence, WCAG 2.2 and the EAA, PWAs.
  - `_research/brief-shopify.md` (Parts 2.5 and 3) — the Storefront Renderer, Online Store 2.0, Hydrogen and Oxygen, the Storefront API, performance guidance.
  - `_research/brief-platform-landscape.md` (Parts 1.2 and 1.3) — Adobe Commerce as a Cloud Service, Commerce.com's Q2 2026 results.
  - [[inventory-and-availability]], [[pricing-architecture]], [[cart-and-checkout]], [[extensibility-and-app-ecosystems]], [[peak-load-and-reliability]] — owning chapters for the facts the storefront renders.
- **External**
  - Google Search Central and Google Crawling Infrastructure, documentation accessed 2026-11-09 — ecommerce navigation and URLs, JavaScript rendering, merchant listings, faceted navigation, `noindex`, localized versions and site moves.
  - Shopify Engineering (August 2020, January 2022), Shopify Partners blog (June 2021, February 2023) and shopify.dev documentation (Hydrogen 2026-10, Storefront API, theme performance, app requirements; accessed November 2026) — the theme and vendor-runtime models.
  - Adobe Experience League (Cloud Service overview, 20 October 2026; Commerce Storefront), BigCommerce Stencil, Salesforce PWA Kit, Vercel (Next.js Commerce; ISR updated 28 August 2026), Alokai (Unified Data Layer) — the other models and the regeneration mechanism.
  - web.dev (Web Vitals updated 31 October 2024; INP blog 2024; PWA article; business-impact case studies), Google Search Central (Core Web Vitals page) — metrics, thresholds and ranking wording, verified in this session.
  - Deloitte Ireland for Google, *Milliseconds Make Millions* (24 March 2020) — the conversion study and its caveats.
  - W3C, WCAG 2.2 (12 December 2024); Directive (EU) 2019/882 (7 June 2019) — accessibility obligations.
  - Commerce.com 8-K exhibit 99.1 (6 August 2026) and the Nasdaq earnings-call summary (2026) — AI crawler hosting costs, labeled as a secondary attribution.

## Changelog

- **2026-11-09** — Added technical SEO and product discoverability, linked the related chapters, clarified public snapshots versus live purchase validation, and shortened repeated rendering explanations to control length. Sources checked against Google's documentation; status `accepted`.
- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: corrected Hydrogen and Oxygen quotations against the docs, Noor's timing (second month, not three weeks), expanded PIM, SFRA, B2B, D2C, POS, W3C, glossed edge runtime and Commerce.com, timetoread; item 13 wording kept neutral. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
