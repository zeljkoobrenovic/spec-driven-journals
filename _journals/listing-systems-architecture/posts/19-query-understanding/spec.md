---
status: accepted
revised: 2026-10-20
---

# Spec: What Did They Mean? Query Understanding and Autocomplete

## Intent

Show architects that query understanding in a listing marketplace is mostly the compilation of short, ambiguous, multilingual queries into the marketplace's own categories and attribute filters, and that it must be built as a governed layer: shared vocabulary from the taxonomy and attribute service, confidence-based interpretation policy owned by each marketplace, explicit null-result recovery, and evaluation per market. Place autocomplete, dense and hybrid retrieval, and LLM-based natural-language search on top of that structured core, using the dated 2023–2026 public record. The chapter owns query understanding, query categorization and hybrid retrieval, and hands off to [[ranking]].

## Audience

Search and ML leads, principal engineers and chief architects of classifieds, real-estate and automotive marketplaces deciding how far to invest in query understanding, dense retrieval and LLM search, and how to govern it across brands and languages.

## Success criteria

- [ ] Reader can describe the query-understanding pipeline and its ownership split ("one vocabulary, many policies").
- [ ] Reader can explain per-language analysis risks (hyphens, folding, stemming, decompounding, bilingual markets) and why token-parity tests are needed.
- [ ] Reader can explain why meaning belongs in the attribute dictionary rather than synonym files, and why synonyms go at search time.
- [ ] Reader can apply a confidence-to-action policy (filter, boost, suggest) with visible chips, and the "adding a filter never increases results" invariant.
- [ ] Reader can design a null-result recovery ladder and an autocomplete pipeline, using Vinted's 2026 figures.
- [ ] Reader can compare Vinted's and Airbnb's dense-retrieval choices and pick a fusion method (RRF vs normalization).
- [ ] Reader can describe the LLM filter-compiler pattern from coches.net and leboncoin, with its validation step and limits.
- [ ] Company claims are dated and sourced; the Veldmark e-bike example matches the ledger and the bikes split date.

## Non-goals

- Engine, document and index design — [[search-architecture]].
- Ordering of results, learning to rank, paid blending — [[ranking]].
- Category tree design and migrations — [[categories-and-taxonomies]]; attribute dictionary design — [[attribute-schemas]].
- Geo semantics and map queries — [[location-and-geo]], [[map-search]].
- Recommendation candidate generation — [[recommendations]]; ML platform governance — [[ml-platform]].
- Broader AI strategy — [[ai-in-listing-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source documents query categorization or spelling systems at OLX, Marktplaats, Kleinanzeigen or leboncoin; the chapter relies on reference-architecture reasoning there.
- The leboncoin retriever details rest on a press report; the primary Medium post was not verifiable.
- Outcome metrics for LLM search are thin (Rightmove's H1 2026 figures are the only quantitative claim); revisit when more are published.

## Decision log

- **2026-10-19** — Framed query understanding as compilation to filters rather than text relevance, because listing traffic is filter-heavy and the documented LLM cases all compile to filters.
- **2026-10-19** — Made the e-bike variants the worked example (with the speed-pedelec exclusion) to tie the chapter to the 1 November 2027 bikes split owned by the taxonomy and attribute chapters.
- **2026-10-19** — Treated autocomplete inside this chapter, using Vinted's 2026 post as the single detailed case, rather than spreading thin across vendors.
- **2026-10-19** — Kept agentic assistants to one table row and a short section on external assistants as clients; [[ai-in-listing-systems]] owns the broader view.

## Sources

- **Internal**
  - [[search-architecture]] — latency budget, analyzers, search contract.
  - [[attribute-schemas]], [[categories-and-taxonomies]], [[ml-platform]] — dictionary, bikes split, order-tier governance.
- **External**
  - Vinted Engineering (2024, 2025, 2026) — analyzer parity, dense retrieval, autocomplete.
  - Adevinta Tech Blog (2024) — coches.net and leboncoin LLM search.
  - Abdool et al., Airbnb (2026) — IVF vs HNSW, replay evaluation.
  - Rightmove plc results (2026); Scout24 Engineering (2026); HousingWire (2024); OLX Magic talk (2024).
  - Elastic and OpenSearch documentation — synonyms, decompounding, fuzziness, RRF, normalization.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: NL bike figures aligned with the editor line (380k bikes, 214k city bikes), pre-split leaves corrected, Rightmove and Vinted claims tightened to source wording, Scout24 sources made specific, old evidence flagged, HNSW/CLIP expanded, AI-gateway links added. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
