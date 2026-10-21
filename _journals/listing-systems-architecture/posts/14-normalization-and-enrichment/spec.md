---
status: accepted
revised: 2026-10-21
---

# Spec: From Raw Supply to Usable Listings: Normalization and Enrichment

## Intent

Show architects how a marketplace turns accepted but heterogeneous records into consistent, enriched listings without losing track of what is true. The chapter owns **normalization** (converting a stated value into the canonical form the dictionary defines, without changing its meaning), **enrichment** (adding facts nobody stated, from registries, models and platform computations) and **attribute provenance** (who said or derived each value, by which process and version, with what confidence). It argues three things: keep the original next to the canonical value; let precedence between seller, feed, registry and model be a per-attribute policy that never silently overwrites asserted values; and run enrichment as a versioned, replayable pipeline that writes back to the system of record, with release gates and an explicit re-processing budget. After reading it, a Chief Architect should know which enrichers to share across brands and which to keep in the verticals, and what the real cost drivers are.

## Audience

Chief architects, principal engineers, data and ML leads and listing-data owners in classifieds, real-estate and automotive marketplaces. They know data pipelines and ML basics; they need the marketplace-specific design of normalization, enrichment and provenance and the public evidence behind it.

## Success criteria

- [ ] Reader can distinguish normalization from enrichment (comparison table) and explain why canonical and original values are both stored.
- [ ] Reader can list the normalization steps a multi-country listing platform needs (encoding, text, numbers and locale, units, enumerations, entities, dates, prices, addresses, contact data) and their rules.
- [ ] Reader can define attribute provenance, name the seven source classes and apply a precedence policy, including "verify, do not derive, legally mandated disclosures".
- [ ] Reader can draw the write-back enrichment loop (Figure 2) and state the five rules that make it replayable, including which steps block publication.
- [ ] Reader can describe the release process for a new enricher version (shadow run, gate, prioritized backfill, churn monitoring, value-level rollback; Figure 3).
- [ ] Reader can trace the Essen Golf value by value, including the 31 decoded attributes and the power-variant conflict, consistent with [[attribute-schemas]].
- [ ] Reader can estimate enrichment cost and explain why re-processing, evaluation and review dominate per-call model cost.
- [ ] Every company claim carries a dated source; Etsy's figures are labeled as reported via a third-party summary.

## Non-goals

- Channels, feed contracts and reconciliation: owned by [[listing-ingestion]].
- The attribute dictionary, category schemas and their compatibility rules: owned by [[attribute-schemas]]; category migrations: [[categories-and-taxonomies]].
- Geocoding providers, geo indexes and location precision: owned by [[location-and-geo]]. Image processing and perceptual hashing: [[media-pipeline]].
- Duplicate detection and canonical entities: owned by [[entity-resolution]].
- Model training, serving, the AVM and model governance in depth: owned by [[ml-platform]]. The AI listing assistant as a product: [[ai-in-listing-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Etsy's primary post blocked automated access; the 31%→91% coverage figure rests on a third-party summary and should be checked in a browser before print.
- No European marketplace has published its VIN-decoding supplier relationships or license terms; the chapter names none for Veldmark and none for real companies.
- Whether the ADEME DPE dataset can be matched reliably to listings by certificate number was not verified; the chapter presents the check as a Veldmark design, not as the documented practice of any real portal.
- Cost figures are illustrative and must not be read as provider prices.

## Decision log

- **2026-10-19** — Separated normalization (meaning-preserving) from enrichment (meaning-adding) as the chapter's first concept, because the two need different provenance, tests and overwrite rules.
- **2026-10-19** — Reused the Essen Golf and its power-variant conflict from [[attribute-schemas]] as the main worked example, and showed it value by value, to make provenance concrete without contradicting the ledger (31 decoded attributes, €22,800 estimate, "good price").
- **2026-10-19** — Added a Tradeyard NL bike-extraction pilot (June–September 2027) to connect enrichment to the ledger's 1 November 2027 bikes split, and a Lyon example to state the rule that legal disclosures are verified, not derived.
- **2026-10-19** — Framed cost around re-processing, evaluation and human review rather than per-call price, following the Mercari evidence; all prices labeled illustrative.

## Sources

- **Internal**
  - `_research/brief-listing-data-ingestion.md` Parts 3, 7, 8 and 11 — units, addresses, ML and LLM extraction evidence, quality dimensions.
  - `_research/brief-automotive.md` Part A.7 — VIN decoding, vehicle taxonomies, price rating.
  - `_research/brief-platform-data-ml.md` Parts 10 and 11 — Adevinta OCR, category prediction, GenAI listing creation.
  - `_research/scenario-ledger.md` — Golf, Lyon apartment, bikes split, ML-platform additions (Valuo trains on DVF; image inference cost).
  - [[listing-aggregate]], [[attribute-schemas]], [[listing-ingestion]] — provenance inside the aggregate; dictionary precedence; record arrival.
- **External**
  - Mercari Engineering (2023, 2024) — LLM extraction, dynamic attributes, re-categorization cost.
  - Adevinta (2023) — OCR service at scale.
  - NHTSA vPIC; DGFiP DVF; ADEME DPE open data; Base Adresse Nationale — registries and reference data.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: expanded DMS, VIN and OCR on first use, clarified the 31-attribute count, American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,458 → 5,477 prose words; 1 heading renamed; opening ties the chapter to Part III's supply chain; model-evidence pattern moved ahead of its examples; spec's figure references corrected to Figures 2 and 3 after the illustrator renumbering. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 2: kept attempt 1: the 'ApplyEnrichment with provenance' line into 'Listing service' has no arrowhead (direction not shown). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
