---
status: accepted
revised: 2026-10-20
---

# Spec: Attributes Without Chaos: Schemas, Dictionaries and Validation

## Intent

Give architects a design for listing attributes that stays coherent across categories, countries and verticals: a governed attribute dictionary (meaning), versioned category schemas (binding) and listing values with provenance (value), stored in a hybrid model and compiled into the forms, validators, search mappings and feed mappings every other system uses. The reader should leave able to recognize the Attribute Junkyard, explain why it forms, and plan both its cleanup and the governance that keeps it from regrowing.

## Audience

Chief and principal architects, search and data leads, and engineering directors of multi-vertical listing marketplaces who own, or depend on, attribute data. They know databases, JSON Schema and event schemas; they need the marketplace-specific design: dictionaries, requiredness, compatibility rules, reference data, regulatory attributes and stewardship.

## Success criteria

- [ ] Reader can distinguish attribute definition, attribute dictionary, category schema, reference data and attribute value, and say who owns each.
- [ ] Reader can list the fields of a dictionary entry and explain why purposes, scope and sensitivity matter.
- [ ] Reader can classify a schema change by its compatibility effect on producers and readers and apply the matching rollout rule (recommended first, effective date, enforce on create and revise).
- [ ] Reader can compare wide tables, EAV, validated documents and typed vertical models and justify a hybrid.
- [ ] Reader can describe a schema service that compiles artifacts rather than serving request-time lookups, and why every write path uses one validator.
- [ ] Reader can name the regulatory attributes for French real estate (DPE) and German new-car advertising (Pkw-EnVKV) and their modeling consequences.
- [ ] Reader can follow Veldmark's cleanup numbers (3,900 keys → 1,240 canonical attributes, 990 retired, 600 country extensions) and its governance targets.
- [ ] Every company claim is dated and sourced; inferences and recommendations are labeled.

## Non-goals

- The category tree, taxonomy versioning and category migrations — [[categories-and-taxonomies]].
- The normalization and enrichment pipeline, attribute provenance mechanics and LLM extraction design — [[normalization-and-enrichment]] and [[ai-in-listing-systems]].
- Feed contracts, error reporting to partners and ingestion channels — [[listing-ingestion]].
- Search index design, faceting performance and ranking — [[search-architecture]] and [[ranking]].
- The listing aggregate's lifecycle and invariants — [[listing-aggregate]].
- Event contract design — [[event-driven-listings]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Etsy's 31% to 91% coverage figure rests on a secondary summary; replace with the primary post if it becomes accessible.
- Whether EU EPBD recast obligations (Directive (EU) 2024/1275) add harmonized EPC attributes for Hearthly Spain should be verified on EUR-Lex before a later revision cites them.
- Licensing terms for redistributing vehicle reference data (Schwacke, DAT, JATO) are not public; the chapter gives only the design rule.

## Decision log

- **2026-10-19** — Organized the chapter around three layers (definition, binding, value) rather than around storage technologies, because storage choice matters less than the dictionary and readers usually start from the wrong end.
- **2026-10-19** — Used event-schema compatibility (Confluent's backward/forward vocabulary) as the frame for schema evolution, applied separately to producers and readers; rejected a simple "breaking/non-breaking" list as too coarse for enumeration changes.
- **2026-10-19** — Made the compiled-artifacts architecture the recommendation and explicitly rejected a request-time schema lookup service on the write path.
- **2026-10-19** — Chose the frame-size key sprawl and the bikes split as the main Veldmark thread, with the Essen Golf decode conflict and the Lyon DPE fields as vertical counterpoints.

## Sources

- **Internal**
  - [[categories-and-taxonomies]], [[normalization-and-enrichment]], [[listing-ingestion]], [[search-architecture]], [[media-pipeline]] — neighbouring chapters and hand-off.
  - `_research/brief-listing-data-ingestion.md` (Parts 3, 4, 8, 11), `brief-real-estate-portals.md` (C.1, C.4, C.7), `brief-automotive.md` (A.2, A.3, A.7), `brief-search-discovery.md` (2.2, 2.7), `scenario-ledger.md`.
- **External**
  - eBay Taxonomy API specification and PBSE playbook — the public attribute-dictionary model and the product/instance split.
  - Amazon SP-API Product Type Definitions — JSON Schema contracts with a custom vocabulary.
  - Vinted Engineering, faceted search (2023) — facets on the index; brand curation.
  - Autotrader Connect and mobile.de Seller-API documentation — vehicle taxonomies, reference data, breaking-change policy, validation rules.
  - Confluent schema-evolution docs; PostgreSQL JSON docs; Elastic nested docs; NHTSA vPIC.
  - Service-Public.fr (DPE), Pkw-EnVKV, RESO Data Dictionary, OpenImmo, Rightmove RTDF v1.4.1, ESCO.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: acronyms expanded on first use (DMS, NHTSA), reading time corrected; frame-size baseline (23%) confirmed against the editor's ledger line; DPE, Vinted and ESCO figures re-verified. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
