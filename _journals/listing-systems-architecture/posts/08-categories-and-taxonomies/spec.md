---
status: accepted
revised: 2026-10-19
---

# Spec: Category Trees That Can Change: Designing Marketplace Taxonomies

## Intent

Show that a marketplace category is a schema key, not a label, and give the reader a design for a taxonomy that can change: a canonical classification tree with stable IDs and leaf-only listing, separated from navigation trees, country views, labels and external mappings; a taxonomy service that publishes versioned releases with their migration artifacts; and a runbook for splits, merges, moves and retirements that covers listings, saved searches, URLs, partner codes, models and analytics. The reader should leave able to diagnose the Category Straitjacket in their own platform and to plan a split like Veldmark's bikes migration.

## Audience

Chief architects, principal engineers, search and data leads, and product and engineering directors of classifieds and vertical portals who own or depend on category trees, especially in multi-country groups that inherited several trees.

## Success criteria

- [ ] Reader can list what a category controls and name the owning system for each dependency.
- [ ] Reader can choose between strict tree, polyhierarchy and facets, and explain why classification and navigation are separate layers (Amazon browse nodes vs product types).
- [ ] Reader can compare country trees, a global tree and a canonical tree with country views.
- [ ] Reader can specify a taxonomy release: tree, from→to mapping, attribute diff, effective dates, with eBay and Shopify precedents.
- [ ] Reader can explain why merges are deterministic and splits need reclassification, and describe the Mercari LLM-labeler-plus-kNN pattern accurately.
- [ ] Reader can walk through the seven-step migration runbook and the Veldmark bikes split numbers.
- [ ] Reader can apply change classes and fitness metrics to taxonomy governance.
- [ ] Reader will not treat Google's taxonomy or schema.org as an internal model.

## Non-goals

- Attribute dictionaries, types, units and schema governance — [[attribute-schemas]].
- Feed formats and inbound code mapping mechanics — [[listing-ingestion]].
- Query categorization and search-time category handling — [[query-understanding]].
- SEO landing-page architecture in depth — [[web-and-seo-architecture]].
- Saved-search matching mechanics — [[saved-searches-and-alerts]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- OLX's reported title-based category prediction was not used because only a search summary was available; add it if the primary post can be verified.
- Licence terms for redistributing vehicle taxonomies (Schwacke, CAP HPI, JATO) remain unverified; the chapter only flags the risk.
- Should the toolkit include a "taxonomy release card" derived from the four-artifact table?

## Decision log

- **2026-10-19** — Made the classification / navigation / labels separation the chapter's central structural idea, anchored on Amazon's documented browse-node vs product-type split, rather than leading with tree-shape debates.
- **2026-10-19** — Recommended a canonical tree with country views over a single global tree, because Veldmark's PL and PT markets need local structure and the ledger's four trees make harmonization the realistic path.
- **2026-10-19** — Used the canonical bikes split (live 1 November 2027) as the worked example and added local numbers (19 country leaves, 640,000 and 410,000 listings, 46/50/4% reclassification tiers, 96.8% audit, 1.3 million saved searches, 1,640 canonical leaves in release 2027.10) recorded in the ledger.
- **2026-10-19** — Presented Mercari's method without accuracy claims, because the source publishes none.

## Sources

- **Internal**
  - [[listing-aggregate]] (taxonomy version on the listing), [[attribute-schemas]], [[meet-veldmark]], [[web-and-seo-architecture]], [[saved-searches-and-alerts]].
  - Research briefs: listing data and ingestion (taxonomies, evolution, migration runbook, ML evidence), automotive (vehicle taxonomies, Auto Trader model splits, ESCO), search (SEO landing pages); productscape digest (category as driver of attributes, fees and operating model).
- **External**
  - eBay Listing Metadata Guide and Taxonomy API v1.1.1; Amazon SP-API product types and browse nodes (2026); Shopify product-taxonomy (2026-08); Google product taxonomy (2021-09-21) and Merchant Center help; Google vehicle-listing changelog (2025), redirects (2026) and faceted-navigation guidance; schema.org V30.1; ESCO v1.2.1 (2025); Mercari Engineering (2024, two posts); eBay magical listing (2023); mobiFlip on Kleinanzeigen (2025); Auto Trader developer portal.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
