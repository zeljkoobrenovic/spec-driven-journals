---
status: accepted
revised: 2026-10-21
---

# Spec: Field Kit: Templates for the Marketplace Architect

## Intent

Give the reader a set of practical, copyable templates for the records a Chief Architect of a marketplace group uses to keep many listing marketplaces coherent, fast and changeable. Each template is derived from the chapter that teaches it, keeps that chapter's terminology and fields, and is filled in once with a short Veldmark example that agrees with the chapter and the scenario ledger. The page should let a reader start from the design or decision on their desk, copy one record, and know which fields carry ownership, removal behavior and dates, and which mistakes make the record useless. It also delivers the publication-pipeline SLA card that [[publication-pipeline]] promises "in the toolkit".

## Audience

Chief and enterprise architects of marketplace groups, principal engineers, search, data, trust-and-safety and monetization leads, and platform-engineering leads who need working forms for capability, vertical, modeling, supply, discovery, trust, monetization, event, consolidation and governance decisions. Product and commercial leaders use Tools 1, 2, 9 and 11 as discussion documents.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; three KEY POINTS; three failure patterns with exact names; `<br>`; an intro on how to use the templates; a table of contents (Tool | Use it when | Chapter).
- [x] Contains the twelve templates in the PLAN contract, each as a `## Tool N` section with purpose, a one-paragraph "use it when", a copyable table or fill-in block, a short Veldmark example, three common mistakes and a closing Learn more `[[link]]` to the owning chapter.
- [x] Every template's fields trace to the owning chapter: heat-map dimensions and verdicts ([[business-capabilities]]); fourteen dimensions and four layers ([[vertical-requirements]]); publication state plus enforcement overlay ([[listing-aggregate]]); dictionary entry fields and requiredness rules ([[attribute-schemas]]); eleven contract clauses, field ownership and mass-change guard ([[listing-ingestion]]); coverage, clock, removal and stage budget ([[publication-pipeline]]); field groups, promotion rule, budgets and rebuild drill ([[search-architecture]]); policy record, ladder and propagation ([[trust-and-safety-architecture]]); ledger entries, effects and enforcement points ([[products-and-entitlements]]); envelope, catalog, topics and compatibility rules ([[event-driven-listings]]); decision-rights and advice process ([[organizing-marketplace-engineering]]).
- [x] Veldmark examples use ledger figures and dates (search run cost €11.8M; Motorvane profile; bike reserved 14:02 and sold 18:10; `bike.battery_capacity_wh` required from 1 March 2028; Supply Contract v1 hybrid; Tradeyard SLA card; Tradeyard BE index; `POL-FRAUD-PAYLINK` v3; Pro 150 and the €212,000 credits; `ListingSold` version 9; Hearthly.es and Keybridge; 14 September 2027 search decision).
- [x] One mermaid diagram shows how the records reference each other; cross-links use only valid permalinks.
- [x] Short Sources and Evidence section with dated sources and the closing fictional-Veldmark sentence.

## Non-goals

- Re-teaching the reasoning behind each template; each tool summarizes and links to its chapter.
- The tenant register and configuration hierarchy ([[multi-country-platforms]]), the qualified-contact definition and metrics catalog ([[data-platform]]) and journey SLOs ([[reliability-and-scale]]), which are linked, not reproduced.
- Definitions of terms ([[glossary]]) and the source list by topic ([[bibliography]]).
- Downloadable file formats (spreadsheets, document templates).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[platform-consolidation]] was not yet written when this page was drafted. Tool 11's fields come from its PLAN contract (integration options, sequence, synergy case, brand migration, regulatory conditions, people) and its Veldmark example uses only decisions already recorded in other chapters and the ledger. Reconcile the card with the chapter once it exists, including any synergy figures it introduces.
- Chapters disagree on two bike details: [[listing-aggregate]] has the Safe Deal reservation at 16:32 and the sale at version 5, while the ledger's editor line has 14:02 and [[event-driven-listings]] has version 9. The toolkit follows the editor line and the owning chapter for events; the editor should align [[listing-aggregate]].
- Should a tenant register entry ([[multi-country-platforms]]) or a consumer registry row ([[listing-data-management]]) become a thirteenth tool?

## Decision log

- **2026-10-19** — Chose the twelve templates in the PLAN contract and no others: a grep of the chapters for "toolkit" found only one explicit promise (the SLA card in [[publication-pipeline]]), already in the list.
- **2026-10-19** — Ordered tools by the book's parts (understand, model, supply, discover, trust, money, platform, lead) rather than by stage, so a reader can move between a tool and its chapter in reading order; the ADR is last because every other tool feeds it.
- **2026-10-19** — Wrote templates as tables where fields need guidance and as fenced blocks where the record is a literal artifact (share-layer row, feed contract, SLA card, policy card, consolidation card, ADR), so they can be copied as they are.
- **2026-10-19** — Used `bike.battery_capacity_wh` rather than the chapter's frame-size entry for Tool 4, because it shows the recommended-then-required runway; frame size appears in the common mistakes.

## Sources

- **Internal**
  - [[business-capabilities]], [[vertical-requirements]] — heat map, verdicts, profiles, share layers, stage gates.
  - [[listing-aggregate]], [[attribute-schemas]] — lifecycle states, overlay, derived visibility, dictionary entry, requiredness.
  - [[listing-ingestion]], [[publication-pipeline]], [[search-architecture]] — feed contract, SLA card, index design and search decision.
  - [[trust-and-safety-architecture]], [[products-and-entitlements]], [[event-driven-listings]] — policy record and ladder, Tally ledger and effects, Listing event contract v1.
  - [[organizing-marketplace-engineering]], [[multi-country-platforms]], [[identity-and-verification]], [[case-aviv]] — governance, tenancy model, Hearthly.es decisions.
- **External**
  - Michael Nygard, *Documenting Architecture Decisions* (2011); Andrew Harmel-Law, *Scaling the Practice of Architecture, Conversationally* (2021).
  - eBay Taxonomy API and Amazon SP-API product type definitions; RFC 9457; Confluent schema compatibility documentation.
  - UK CMA Adevinta/eBay Classifieds decision (2021); Adevinta Kleinanzeigen rebrand release (2023); Regulation (EU) 2022/2065.
  - The RECONCILED toolkit — page format and tool structure.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Tool 11 rebuilt against the written platform-consolidation chapter (six integration options, staged and gated sequence, synergy ledger with dated evidence, 3% traffic rule, Keybridge federated under group controls); bike version 9 and 14:02 reservation confirmed. *(AI-mediated session)*
- **2026-10-20** — Tool 10 purpose now says a listing event specification defines one event in the listing event contract, linking event-driven-listings. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 4,852 → 4,864 words; lead now names the toolkit as the records Parts I–VIII ask for, linking the first and last owning chapters; teaser opener cut from How the Records Connect; Tool 11 purpose sentence split; no headings changed. *(AI-mediated session)*
- **2026-10-20** — Replaced 1 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
