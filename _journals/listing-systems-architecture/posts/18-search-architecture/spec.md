---
status: accepted
revised: 2026-10-20
---

# Spec: Search Architecture for Listings: Indices, Freshness and Scale

## Intent

Give architects a structural model of the search layer of a listing marketplace: the index as a rebuildable read model of the listing stream, the listing search document, index topology, the write path (near-real-time indexing, ordering, update storms, removal latency), the read path (facets, caching, latency budgets), zero-downtime reindexing and capacity planning for evening peaks. The chapter should leave the reader able to judge an engine choice by workload fit rather than benchmarks, and convinced that a stable search contract matters more than the engine behind it. It opens Part IV's technical chapters and hands off to [[query-understanding]].

## Audience

Chief and principal architects, search platform leads and engineering directors of classifieds, real-estate and automotive marketplaces, including those running several engines after acquisitions. They know Elasticsearch, Solr and Kafka; they need listing-specific design reasoning and dated evidence.

## Success criteria

- [ ] Reader can explain why the index must be rebuildable from the event stream and system of record, and how a quarterly rebuild drill detects Index-as-Database.
- [ ] Reader can design a listing search document, including the promotion rule for typed versus flattened attributes and the mapping-limit reason for it.
- [ ] Reader can choose an index topology using the three questions (cross-boundary queries, analyzers, load skew).
- [ ] Reader can name the update-storm mitigations and explain external versioning with a listing-owned sequence, including Vinted's partition-count lesson.
- [ ] Reader can separate insertion and removal latency and set an index share of the publication budget.
- [ ] Reader can explain why facets go on their own path, with Vinted's dated figures.
- [ ] Reader can run an alias-swap reindex with a live stream safely and knows why Tradeyard's January 2027 brown-out happened.
- [ ] Every company claim carries a dated source; Veldmark figures match the ledger.

## Non-goals

- Text analysis, synonyms, autocomplete and hybrid retrieval — [[query-understanding]].
- Learning to rank and paid-organic blending — [[ranking]].
- Geo queries and map clustering — [[map-search]]; percolation and alert fan-out — [[saved-searches-and-alerts]].
- End-to-end publication SLA and moderation gate — [[publication-pipeline]].
- Event contract design and outbox — [[event-driven-listings]]; CQRS in general — [[listing-data-management]].
- Degradation design and SLOs per journey — [[reliability-and-scale]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source was found for the search engines of OLX, Marktplaats, Kleinanzeigen, Idealista or AutoScout24; the engine table may grow when sources appear.
- Vinted's before-and-after figures mix engine, hardware and topology changes; a neutral engine comparison for listing workloads is not public.
- Whether the read-path status recheck should be part of the search contract or of each marketplace's hydration layer.

## Decision log

- **2026-10-19** — Organized the chapter around the "index is a projection" principle rather than an engine survey, because engine choice is the decision readers over-weight.
- **2026-10-19** — Used Vinted's dated series as the main public case and kept leboncoin, Rightmove and Homegate to one line each, because only Vinted documents the evolution in detail.
- **2026-10-19** — Used the Rightmove Wednesday TV-break peak as the documented peak example; the Sunday-evening peak stays a Veldmark property.
- **2026-10-19** — Added local Veldmark details (2.6 engine requests per results page, 6.4M daily counter writes, 610 promoted attribute keys, 15 s index budget, 10 s removal target) to make the worked example concrete.

## Sources

- **Internal**
  - [[meet-veldmark]], scenario ledger — engines, volumes, brown-out, 14 September 2027 decision.
  - [[publication-pipeline]], [[listing-data-management]], [[event-driven-listings]] — neighboring ownership.
- **External**
  - Vinted Engineering, Search Scaling series (2017–2025) — engine history, indexing, facets, freshness.
  - Elastic, Solr and Vespa documentation — aliases, refresh, mapping limits, commits and caches, partial updates.
  - Elastic (2024) and Linux Foundation (2024) — license and governance history.
  - Google Cloud Press Corner (2021) — Rightmove's peak minute.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: timetoread corrected, license acronyms expanded, Vinted facet-count wording and Rightmove/Zillow evidence dated or hedged, American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,943 → 6,905 prose words; lead rewritten to place the chapter as the start of Part IV's discovery read models; "Architecture: Components and Boundaries" renamed "Architecture: The Index as a Projection"; "Choosing an Engine" moved after capacity planning, so engine choice follows the structure it depends on; topic sentences tightened. Spec unchanged apart from this line. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: "projection" → "read model" in the excerpt, KEY POINTS, lead, Architecture heading ("Architecture: The Index as a Rebuildable Read Model") and Figure 2 caption, matching the glossary, [[listing-data-management]] and the Part IV intro; spec Intent updated to match. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 6: kept attempt 1: line from 'Shared indexer framework' to 'Amazon OpenSearch Service' merges with the 'Elasticsearch adapter' line at a junction, so it can read as 'Elasticsearch adapter' also pointing to Amazon OpenSearch. *(AI-mediated session)*
