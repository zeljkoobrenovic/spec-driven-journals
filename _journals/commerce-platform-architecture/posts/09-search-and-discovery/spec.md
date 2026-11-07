---
status: accepted
revised: 2026-11-07
---

# Spec: Finding the Product: Search, Navigation and Merchandising

## Intent

Teach a reader who has never looked behind a search box that search, navigation, merchandising and recommendations all sit on one derived copy of the catalog, the prices, the availability and the reviews, and that the quality of discovery is decided by what feeds that copy and how fresh each feed is, not by the engine. After reading, the reader can diagnose a zero-result query as a data gap, decide which facts belong in the index and which must be fetched at query time, treat merchandising rules and synonyms as owned, dated data, explain hybrid and semantic retrieval in plain words without buying into vendor lift claims, enforce B2B assortments in the search service, and run reviews as discovery data with the provenance the Omnibus Directive and the FTC rule require.

## Audience

Readers new to commerce architecture. The product manager or ecommerce manager who owns the storefront's search and the engineer who will build or buy the indexing pipeline benefit most; catalog owners learn why facets fail without attributes; anyone evaluating a search or review vendor gets the questions to ask.

## Success criteria

- [x] Opens with a one-sentence "IN THIS CHAPTER, YOU WILL", exactly three KEY POINTS, the business and architect callouts, and three failure patterns (The Phantom Stock, The Message in a Bottle, The Lynchpin).
- [x] The "waterproof jacket" zero-results problem is told with illustrative figures (31% of sessions, 9.4% zero-result rate, synonyms March 2027, PIM attribute Q3 2027, 4.1% by Q4 2027) consistent with the ledger's "no PIM" fact and appended to the ledger; the Black Friday "in stock" staleness ties to the Oversell.
- [x] A reader new to the field can define every term from the chapter alone: search index, indexing, staleness, relevance, ranking, facet, merchandising rule, synonym set, typo tolerance, personalization, collaborative filtering, vector or semantic search, hybrid search, reciprocal rank fusion, embedding, assortment, contract price, zero-result rate, click position, PIM, stock event.
- [x] Two mermaid diagrams with captions: the index as a copy of four sources with merchandising and ranking overlays, and the review pipeline from delivery to index and feeds.
- [x] Tables: three ways of finding; what goes in the index vs fetched fresh; a requirements table (freshness, consistency, latency, availability); a trade-off table across three choices; the "Across Scale Stages: When It Fits and When It Limits" table with the four ledger stages.
- [x] Reviews and ratings covered as discovery and trust data: collection tied to orders, moderation on policy not sentiment, incentives disclosed, ranking parameters documented, with Directive 2019/2161 (applied 28 May 2022) and the FTC rule of 14 August 2024 cited.
- [x] LISTED's [[search-architecture]] and [[ranking]] are linked for depth, not re-taught; AI search is introductory and hands off to [[ai-and-agentic-commerce]].
- [x] Every company claim dated and sourced; vendor conversion lifts presented as "the vendor reports"; Baymard's method caveat stated; the three take-away tiers present; 6–10 questions; hand-off to [[inventory-and-availability]]; article at or under 6,500 words from front matter to Sources, including tables.

## Non-goals

- The product model, attributes and the PIM itself — [[product-information]]; the price and prior price — [[pricing-architecture]] and [[commerce-promotions]].
- Availability computation, reservations and stock events — [[inventory-and-availability]].
- Engine internals (sharding, replication, index topology, query planning) — LISTED's [[search-architecture]]; two-sided and paid ranking — LISTED's [[ranking]].
- Agentic commerce, conversational agents and merchant readiness for them — [[ai-and-agentic-commerce]].
- Marketplace-owned reviews and listing content rules — [[marketplaces-and-channel-integration]]; B2B account and pricing models — [[b2b-commerce]].
- Storefront rendering, caching and page performance — [[storefront-architecture]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The FTC fake-reviews rule's effective date (reported as 21 October 2024) could not be read from the Federal Register in research; the chapter cites only the 14 August 2024 announcement.
- Kestrel & Pine's reviews app is unnamed and its export format invented; if a later chapter ([[extensibility-and-app-ecosystems]]) inventories the 41 apps, it should list the reviews app and the pre-order app consistently with this chapter.
- Whether store associates should query the same search service (endless aisle) is asserted here as an Omnichannel need; [[stores-and-omnichannel]] should confirm or qualify it.

## Decision log

- **2026-11-07** — Made "the index is a copy" the spine, organized around which facts are in the index versus fetched at query time, because that one decision explains the stale-stock failure, the B2B price designs and embedding staleness at once.
- **2026-11-07** — Kept engines and ranking introductory and linked LISTED's `search-architecture` and `ranking`, as the contract directs.
- **2026-11-07** — Added reviews as a full section with its own diagram (the contract was updated), with the legal content in one paragraph.
- **2026-11-07** — Chose a Kestrel & Pine plan with no new vendor to make the "data before engine" argument concrete; dated the synonym fix to March 2027 so Eva's April search works on the ledger's timeline.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — catalog counts, the no-PIM fact, the sync chain, Black Friday, Waypoint W1, W3, W5 and W8, Eva's order.
  - `_research/brief-catalog-pricing-search.md` Parts 2.3 and 4; `_research/brief-ai-agentic-commerce.md` 1.1 and 5.1; `_research/brief-security-privacy-regulation.md` 3.1 and 3.12 — index, engines, rules, metrics, B2B search, AI retrieval, review law.
  - [[product-information]], [[inventory-and-availability]], [[commerce-promotions]], [[b2b-commerce]], [[ai-and-agentic-commerce]] — neighbours whose terms this chapter uses briefly.
- **External**
  - commercetools, Algolia, Shopify, Elastic and OpenSearch documentation (accessed 2026-11); Algolia NeuralSearch release (2023); Shopify changelog (2024) — indexing, limits, rules, metrics, hybrid retrieval.
  - Nigam et al., *Semantic Product Search* (KDD 2019); Amazon Science (2019); Baymard Institute (2024–2026) — evidence on retrieval, baselines and search usability.
  - Directive (EU) 2019/2161; FTC press release of 2024-08-14; schema.org Product v30.1 — review provenance, ranking transparency, aggregate ratings.
  - Zalando press release (2023-04-19) and Q3 2026 results — conversational search as a dated example.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: fixed the timing of the Q1 search report against the March synonym fix, expanded acronyms, removed internal ledger references, timetoread 28. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
