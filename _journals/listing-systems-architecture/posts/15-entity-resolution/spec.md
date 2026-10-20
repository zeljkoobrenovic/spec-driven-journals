---
status: accepted
revised: 2026-10-20
---

# Spec: One Property, Five Listings: Duplicates and Entity Resolution

## Intent

Give architects a precise way to think about duplicate listings and entity resolution. The chapter separates abusive duplicates (enforcement) from legitimate ones (clustering for presentation), defines the real-world entity per vertical, lays out the matching pipeline (blocking, pairwise scoring, clustering, an entity registry with stable IDs and lineage), and treats merge policies, especially the representative-listing rule, as governed product and ranking decisions. After reading, the reader can design or review an ER capability and say who owns each decision.

## Audience

Chief and principal architects, search and data leads, and product directors of classifieds, real-estate and automotive marketplaces who face duplicate complaints from buyers or agencies, or who are building a property or vehicle registry.

## Success criteria

- [ ] Reader can name the five duplicate kinds and the right action and owner for each.
- [ ] Reader can explain why the property (or vehicle) must be a separate entity from the listing, and why goods mostly have no such entity.
- [ ] Reader can describe blocking, pairwise scoring, clustering and the entity registry, including the chaining risk and stable-ID requirement.
- [ ] Reader can choose merge policies per audience (search, listing page, alerts, valuation, metrics, leads) and knows the count/facet inconsistency of field collapsing.
- [ ] Reader can explain why the representative rule is a ranking parameter with transparency obligations.
- [ ] Worked example: the Lyon apartment resolved with numbers consistent with the ledger (68 m², €389,000, DPE D, three agencies, Valuo €372,000–€401,000, 1.7 listings per property).
- [ ] Includes a trade-off table, a vertical-differences table, two mermaid diagrams, Chief Architect's view, questions to ask, dated sources.
- [ ] Every company claim is dated and sourced; inferences labeled.

## Non-goals

- Feed mechanics and partner reconciliation ([[listing-ingestion]]).
- Address, VIN and attribute normalization ([[normalization-and-enrichment]]).
- Perceptual hashing as a media capability ([[media-pipeline]]).
- Fraud investigation and enforcement after a stolen-listing match ([[fraud-prevention]]).
- Index design for collapsed results ([[search-architecture]]) and ranking algorithms ([[ranking]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No current primary source describes a classifieds operator's production ER system; the OLX design is from 2019. Replace if a newer public account appears.
- Whether to give the Hearthly property registry a canonical name in the ledger for later chapters (valuation, map search).
- Treatment of VIN as personal data differs by country; [[marketplace-regulation]] may want to own that note.

## Decision log

- **2026-10-19** — Organized the chapter around five duplicate kinds and two action families (enforce vs cluster) rather than around algorithms, because the policy split is where real systems go wrong.
- **2026-10-19** — Made the entity registry, not the search index, the system of record for cluster IDs; rejected a query-time-only collapse design as the recommended approach.
- **2026-10-19** — Used the Keybridge neutrality decision as a constraint on matcher inputs, to show that ER inputs are a governance question.
- **2026-10-19** — Kept the Lyon numbers (thresholds, precision 98.6%, recall 91%, dispute volumes) local and illustrative rather than adding them to the ledger.

## Sources

- **Internal**
  - [[meet-veldmark]], scenario ledger — Hearthly duplicates, Lyon apartment, Keybridge decision, Barcelona ring.
  - [[listing-aggregate]], [[media-pipeline]], [[location-and-geo]], [[fraud-prevention]], [[publication-pipeline]] — neighboring contracts.
  - Research briefs: listing data and ingestion (Part 10), real-estate portals (C.8, Part D), search (Part 13), trust and safety (3.4).
- **External**
  - Grigorev, *Fighting fraud: finding duplicates at scale*, PyCon DE 2019 — the public classifieds dedup design.
  - Online Marketplaces, Idealista duplicate-control tool, 2021-04-11.
  - Zillow 10-K FY2025 — property-first database.
  - Elastic collapse documentation; PDQ release (2019) and docs; Splink; SimHash (2007); OS Open UPRN; BAN; RNB.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: aligned the Barcelona-ring detection with fraud-prevention (flags fired but went to separate queues), expanded UPRN and GTIN. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 11 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
