---
status: accepted
revised: 2026-10-21
---

# Spec: System of Record and Read Models: Listing Data Management

## Intent

Give architects a working discipline for the copies an event-driven marketplace creates. The chapter establishes **one system of record per listing fact**, treats every other store as a registered copy (replica, read model, cache, archive, evidence store, analytical or external copy) with an owner, a staleness budget, a rebuild path and a retention rule, and turns GDPR erasure into a **workflow with receipts** from every copy owner. After reading, the reader can audit where listing data lives, state the consistency promise for each read path, set retention by data class, and design erasure propagation that can be proven.

## Audience

Chief and principal architects, data and platform leads, and privacy engineers in multi-brand marketplace groups. They know databases, CQRS and Kafka; they need the marketplace-specific rules (sold pages, private sellers, T&S evidence, transaction records, valuation history) and a copy register they can adopt.

## Success criteria

- [ ] Reader can define the listing system of record and distinguish the seven kinds of copy and their governing rules.
- [ ] Reader can state read-your-writes, monotonic reads, bounded staleness and removal priority as staleness budgets, and name an implementation for each.
- [ ] Reader can choose a partitioning scheme (country first versus global hash) and a region strategy, using Vinted's documented evidence.
- [ ] Reader can build a retention schedule by data class and explain why legal obligations (DSA, tax records) conflict with storage limitation.
- [ ] Reader can design erasure propagation: intake, scope, fan-out events, per-copy outcomes, external copies, ledger, backups and crypto-shredding.
- [ ] The Veldmark example (Femke's seven copies, September 2027) is consistent with the ledger and the previous chapter.
- [ ] Includes a trade-off table, a vertical-differences table, failure modes, a Chief Architect's view and design-review questions.

## Non-goals

- The event contract, outbox, replay mechanics — [[event-driven-listings]].
- Search index internals and reindexing — [[search-architecture]].
- The legal analysis of DSA, DAC7 and GDPR obligations — [[marketplace-regulation]].
- Tracking plans and data products — [[data-platform]]; model-side anonymization — [[ml-platform]].
- Disaster recovery and multi-region failover — [[reliability-and-scale]]; SEO handling of sold pages — [[web-and-seo-architecture]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No marketplace has published a full copy inventory or erasure workflow; revisit if one does.
- The Veldmark retention periods (13 months for listing content, 24 months for T&S evidence) are illustrative; [[marketplace-regulation]] and [[trust-and-safety-architecture]] may refine them.
- Re-identification risk of anonymized property price history needs a firmer treatment in [[ml-platform]] or [[case-property-portals]].

## Decision log

- **2026-10-19** — Organized the chapter around one erasure request (Femke, Sept 2027) because erasure exposes every copy at once, rather than around a performance problem.
- **2026-10-19** — Classified copies into seven kinds with different governing rules instead of a single "read model" concept, because archives, evidence stores and external copies cannot be rebuilt.
- **2026-10-19** — Recommended country-first partitioning and single-writer regions for classifieds, presenting Vinted's cross-border catalog as the documented counter-case.
- **2026-10-19** — Treated crypto-shredding as a narrow tool for mandated immutability, not a default erasure strategy.

## Sources

- **Internal**
  - [[event-driven-listings]] — the event stream that creates the copies.
  - [[listing-aggregate]], [[search-architecture]], [[marketplace-regulation]], [[data-platform]].
  - `_research/brief-platform-data-ml.md` Parts 2–4 and 8; `_research/brief-trust-safety-regulation.md` §5.1, §5.10; `_research/productscape-digest.md` §5; `_research/scenario-ledger.md`.
- **External**
  - Vinted Engineering (2023, 2024, 2026) — single writer, projections, read models, Vitess sharding.
  - Adevinta Tech Blog (2024, 2025) — data contracts, personal-data split, compacted topics.
  - GDPR Arts. 5, 12, 17, 19 — storage limitation, deadlines, erasure, notification.
  - Ondernemersplein — Dutch seven-year record retention.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: aligned Femke's media copy with the media-pipeline ledger (six photos, GPS in originals), corrected the Vinted multi-writer quote and Vitess shard wording, hedged the Vinted cross-border claim, verified DSA Arts. 20(1) and 30(5) against the Official Journal text. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,169 → 5,167 words; lead now names the chapters that depend on this one; 1 heading renamed ("Data contracts for read models" → "The copy register as a data contract"); 7 teaser or generic first sentences replaced with their point; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: "copy register" → the **consumer registry** of [[publication-pipeline]], which this chapter extends with source, staleness budget, rebuild path, retention and erasure handler (heading "The consumer registry as a data contract", Figure 2, body); "Serving the promises" → "Implementing the consistency guarantees"; "Architecture: Where Listing Data Lives" → "Architecture: One System of Record, Registered Read Models". *(AI-mediated session)*
- **2026-10-20** — Term alignment with the glossary: "projection" → "read model", "copy register" → "consumer registry", "filter compiler" → "query compiler", where they occur on this page. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
