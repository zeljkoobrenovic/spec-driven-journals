---
status: accepted
revised: 2026-10-20
---

# Spec: Found by Google: Web, App and SEO Architecture for Listings

## Intent

Show that the customer-facing layer of a listing marketplace has two demanding clients — people on phones and search-engine crawlers — and that the crawler's contract (URLs, status codes, sitemaps, structured data, response times) must be designed like any other interface. The chapter should leave the reader able to design landing-page generation as a rule-based, stateful process, to drive listing-page responses and sitemaps from listing lifecycle events, to choose a rendering and composition model for public pages, and to put backends-for-frontends and server-driven forms behind the apps. It ends with the newest channel, AI search and answer engines, treated precisely and without hype.

## Audience

Chief architects, principal engineers and web, app and SEO leads at classifieds, real-estate, automotive and jobs marketplaces. They know HTTP, CDNs and front-end frameworks; they may not know how crawl budget, faceted-navigation rules and Google's spam policies constrain a marketplace's URL space, or why landing pages rather than listing pages are the durable SEO asset.

## Success criteria

- [x] Reader can explain crawl, render, index and rank, and why crawl budget binds for large listing sites (Google's documented thresholds and effect of slow or error responses).
- [x] Reader can define a landing page and landing page generation, and state the demand, supply, distinctness, depth and quality rules, with Google's faceted-navigation and scaled-content/doorway boundaries.
- [x] Reader can specify the HTTP response, page content and sitemap treatment for each listing lifecycle state, and explain why removal latency is a metric.
- [x] Reader can compare CSR, SSR, streaming SSR, static generation and dynamic rendering, and summarize the documented composition record (Zalando 2018, AutoScout24 2018, Subito 2023).
- [x] Reader can explain the BFF pattern, server-driven forms and deep-link parity for apps with slow release adoption.
- [x] Reader can state what Google documents about AI Overviews, AI Mode and Google-Extended, and why classifieds are less exposed than informational publishers.
- [x] The Tradeyard worked example uses ledger numbers (40M indexed URLs, 46% organic web sessions, the Rotterdam city bike, the bikes split on 1 November 2027) and shows the metric shift from indexed URLs to organic contacts.
- [x] At least three mermaid diagrams, a trade-off table, a vertical-differences table, Chief Architect's view, Questions to ask, dated sources.

## Non-goals

- Search indexing, aliases and reindexing ([[search-architecture]]); ranking and paid blending ([[ranking]]).
- The listing event stream and outbox ([[event-driven-listings]]).
- Taxonomy change process ([[categories-and-taxonomies]]); alert digests ([[saved-searches-and-alerts]]).
- Ad stack internals ([[advertising-platforms]]); bot management and capacity ([[reliability-and-scale]]).
- AI agents, licensing and agentic search ([[ai-in-listing-systems]]); URL migrations in brand consolidations ([[platform-consolidation]], [[modernization-and-migration]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No classifieds operator in the evidence documented its expired-listing SEO handling or organic traffic by page type; the lifecycle policy is a labeled inference. Replace or confirm when primary evidence appears.
- Whether in-platform payment pages (Safe Deal) qualify as Google "merchant listings" is left open deliberately.
- AI-assistant referral share and crawler policy evolve quickly; revisit the AI section in 2027.

## Decision log

- **2026-10-19** — Centered the chapter on landing pages as generated, stateful inventory rather than on tag-level SEO, because the URL space is where architecture decides traffic.
- **2026-10-19** — Recommended `410` after a grace period for most gone listings, with curated `200` pages only for proven demand; rejected permanent "sold" pages as a default because they produce Ghost Inventory in the index.
- **2026-10-19** — Presented page-level ownership with build-time shared components as the default, citing the Zalando and Subito record, rather than runtime micro-frontends.
- **2026-10-19** — Reported Google's 2025 retirement of vehicle listing rich results to argue for structured-data builders over template markup.

## Sources

- **Internal**
  - [[search-architecture]], [[event-driven-listings]], [[categories-and-taxonomies]], [[location-and-geo]], [[entity-resolution]] — neighboring contracts.
  - `_research/brief-platform-data-ml.md` (Part 7) and `_research/brief-search-discovery.md` (Part 12) — evidence and labeled inferences.
- **External**
  - Google Search Central pages on crawl budget, faceted navigation, sitemaps, robots meta tag, dynamic rendering, mobile-first indexing, spam policies, product and job-posting structured data, AI features, hreflang and the documentation changelog (2025–2026).
  - web.dev Web Vitals and the QuintoAndar INP case study (2024, 2025).
  - Adevinta Tech Blog (Subito microsites, 2023; SEO and AI answers, 2023); Zalando (2018); AutoScout24 (2018); Vinted (2019); Sam Newman on BFFs (2015); Cloudflare (2025); IndexNow; schema.org.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: corrected the Google 12 June 2025 quote, aligned the Lyon cluster canonical rule with entity-resolution, restored the [[part-8]] link, expanded acronyms, flagged 2019 Vinted evidence as older. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,899 → 7,912 prose words; lead now ties the chapter to Part VII's published contracts and names what it builds on and what uses it (roadmap paragraph replaced); 6 first sentences brought forward; 2 paragraphs split; headings unchanged; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: the apps-versus-web claim for large classifieds brands is now marked as the author's reading; Tradeyard's 57%/43% split leads. *(AI-mediated session)*
