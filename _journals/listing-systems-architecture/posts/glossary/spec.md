---
status: accepted
revised: 2026-10-19
---

# Spec: Glossary

## Intent

Give *LISTED* one shared vocabulary. A reader who meets a term in any chapter (a marketplace model, a listing-model concept, a feed or search term, a trust or regulatory obligation, a monetization or platform device) can find a plain-language definition in one place, see it beside the terms it is most often confused with, and follow a link to the chapter that owns it. The page also serves the writers and AI tools that work on the book: the chapters follow these definitions, so a disagreement between a chapter and this page is a defect to fix in one of them.

## Audience

Chief architects, principal engineers, search, data and ML leads, and product and engineering directors of listing marketplaces, reading the book out of order. Most arrive with one term to look up, so the page must work as a lookup first and a read second. Readers from one vertical (real estate, automotive, general classifieds) also use it to decode another vertical's terms.

## Success criteria

- [ ] Every term listed under "Owns" in the book PLAN appears in a row, plus the important terms the chapters define in bold on first use.
- [ ] Terms are grouped by part: evidence labels and failure patterns; Parts I–VIII; Veldmark names. Each section is a `| Term | Definition | Chapter |` table with the term in bold.
- [ ] Every definition is one to three plain sentences, agrees with the owning chapter's definition, expands its acronyms, and dates regulatory or vendor facts (as of 2026).
- [ ] The contrasts that cause real errors sit in one row or adjacent rows: listing / underlying entity; publication state / enforcement overlay; full snapshot / delta feed; normalization / enrichment; duplicate detection / entity resolution; contact / conversation / lead; entitlement / quota / effect; system of record / read model; domain event / change event.
- [ ] Every Chapter cell is a valid `[[permalink]]` from the style guide; no cross-journal links except the allowed RECONCILED payments link.
- [ ] An alphabetical index at the end lists every row term, abbreviation and common alias with a link to its section, generated from the tables so it cannot drift.
- [ ] Opening callouts follow the book's format: IN THIS SECTION, YOU WILL; exactly three KEY POINTS; two failure patterns.

## Non-goals

- Teaching any concept in depth; the linked chapter does that, with sources and the Veldmark worked example.
- Authoritative legal, standards or vendor definitions; the regulation, standard or vendor documentation wins.
- Veldmark's cast, volumes and systems in detail; [[meet-veldmark]] owns them. Veldmark appears only in rows that need a concrete anchor and in the short Veldmark-names section.
- Templates ([[toolkit]]) and sources ([[bibliography]]).
- Every term the book mentions: narrow one-chapter devices, single vendor features and one-off Veldmark artifacts stay in their chapters to keep the page usable.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only. A glossary has no argument to summarize or dramatize.

## Open questions

- Rows owned by chapters that were not yet written when this page was drafted ([[industry-evolution]], [[transactions-and-payments]], [[platform-consolidation]], [[modernization-and-migration]], [[long-term-evolution]]) follow the PLAN contracts and standard usage; they were rechecked against the published chapters in the 19 Oct 2026 review pass.
- Should the index carry every alias, or only row terms and abbreviations? It currently carries row terms, abbreviations and a curated list of aliases defined inside rows (for example CQRS, Rendition, Platform tax).
- Who re-checks the page when chapters are revised? Working assumption: a pass during each review cycle.

## Decision log

- 2026-10-19 — Grouped by part rather than by subject, following the book PLAN, with evidence labels and failure patterns first because every chapter uses them, and Veldmark names last so fictional terms stay visibly separate.
- 2026-10-19 — Alphabetical index placed at the end (as requested for this book), generated from the tables by a script with an explicit alias map; section anchors are `<a id>` tags in the headings because the renderer does not generate heading ids.
- 2026-10-19 — First draft of about 480 rows trimmed to about 400: minor single-chapter devices were dropped and related terms merged into slash rows, keeping every PLAN-owned term. The page runs longer than a typical reference page because the book has eight content parts.

## Sources

Internal: every published chapter of the book, harvested for bold first-use definitions, in particular [[marketplace-taxonomy]], [[liquidity-and-network-effects]], [[bounded-contexts]], [[listing-aggregate]], [[attribute-schemas]], [[listing-ingestion]], [[publication-pipeline]], [[search-architecture]], [[ranking]], [[trust-and-safety-architecture]], [[marketplace-regulation]], [[messaging-and-leads]], [[products-and-entitlements]], [[event-driven-listings]], [[listing-data-management]], [[data-platform]], [[experimentation]], [[ml-platform]], [[multi-country-platforms]], [[reliability-and-scale]], [[organizing-marketplace-engineering]] and [[ai-in-listing-systems]]; the "Owns" lists in the book PLAN; the scenario ledger for Veldmark names; the structure of RECONCILED's glossary.

External: none directly. Definitions follow the regulation, standard and company sources cited in the linked chapters.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: rows written from contracts rechecked against industry-evolution, transactions-and-payments, platform-consolidation, modernization-and-migration and long-term-evolution (14 rows corrected, carve-out/TSA and dispute/chargeback rows added, index updated); eight countries; timetoread corrected. *(AI-mediated session)*
