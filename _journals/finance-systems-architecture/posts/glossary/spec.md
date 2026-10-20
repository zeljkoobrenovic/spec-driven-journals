---
status: accepted
revised: 2026-10-18
---

# Spec: Glossary

## Intent

Give RECONCILED one shared vocabulary. A reader who meets a term in any chapter (an accounting term, a vendor object, a payments role, a control or a governance device) can find a plain-language definition in one place, see it next to the terms it is most often confused with, and follow a link to the chapter that owns it. The page also serves the writers and AI tools that work on the book: the chapters are meant to follow these definitions, so a disagreement between a chapter and this page is a defect to fix in one of them.

## Audience

Chief Architects, finance-systems and integration architects, and finance-transformation leaders reading the book out of order, plus finance readers (controllers, CAOs) who need the architecture terms and architects who need the accounting ones. Readers arrive with a single term to look up, so the page must work as a lookup first and a read second.

## Success criteria

- [ ] An alphabetical index lists every term (and common abbreviations and aliases) with a link to the section that defines it; the links work in the rendered page.
- [ ] Terms are grouped into seven sections: Accounting and Finance; Enterprise Architecture; Integration and Data; Platforms and Vendors; Payments; Controls, Resilience and Regulation; Strategy and Governance. Each section is a `| Term | Definition | Chapter |` table.
- [ ] Between 180 and 280 rows, harvested from the chapters' bolded definitions and the PLAN "Owns" lists; every owned term in PLAN appears.
- [ ] Every definition is one or two plain sentences and agrees with the chapter it links to; vendor-specific terms name the vendor, and date-sensitive names and regulatory status are marked as of 2026.
- [ ] The contrasts that cause real errors sit in one row or in adjacent rows: clearing account / suspense account / dead letter; system of record / system of reference / golden copy / derived store; principal / agent / merchant of record; account reconciliation / transaction matching; reconciling item / break; translation / revaluation; event date / posting date.
- [ ] Every Chapter cell is a valid `[[permalink]]` and the build renders it as a titled link; no literal `[[…]]` remains.
- [ ] Opening callouts follow the book's format: IN THIS SECTION, YOU WILL; exactly three KEY POINTS; two failure patterns.

## Non-goals

- Teaching any concept in depth; the linked chapter does that, with the Northmere worked example and sources.
- Authoritative accounting, legal or vendor definitions; the page says the standard, regulator or vendor documentation wins.
- Northmere's cast, brands and systems; [[meet-northmere]] owns them. Northmere appears only where a row needs a concrete anchor.
- Templates and sources; [[toolkit]] and [[bibliography]] own them.
- Every term the book mentions. Narrow vendor objects, report names and one-off Northmere artifacts are left to their chapters to keep the page a usable size.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only. A glossary has no argument to summarize or dramatize.

## Open questions

- Should the index carry every alias, or only the row terms and abbreviations? Currently it carries row terms, abbreviations and a short list of aliases defined inside other rows (for example Interchange, Representment, Dual write).
- When later chapters are revised, who re-checks that this page still agrees with them? A periodic pass during each review cycle is the working assumption.

## Decision log

- 2026-10-18 — Section anchors are explicit `<a id>` tags in the `##` headings, because the post renderer does not generate heading ids; the index links to sections, not rows, following the OWNED glossary.
- 2026-10-18 — Grouped by subject rather than by part, using the seven groups requested; the section intros name the owning chapters so a reader can jump to the full treatment.
- 2026-10-18 — Capped at 260 rows: related terms that are only meaningful as a pair are merged into one row with a slash (for example Dispute / chargeback, Reverse shadow / point of no return), and minor terms are kept as index aliases pointing at the row that defines them.
- 2026-10-18 — Cap raised from 260 to 280 rows to take the FinOps chapter's owned terms; the merge-related-terms rule still applies.
- 2026-10-18 — The alphabetical index is generated from the tables, so it cannot drift from them when rows are added or removed.

## Sources

Internal: every chapter of the book, in particular [[accounting-for-architects]], [[integration-architecture]], [[systems-of-record]], [[payments-fundamentals]], [[payments-to-ledger]], [[controls-and-auditability]], [[architecture-governance]] and [[incremental-modernization]]; the "Owns" lists in the book PLAN; the structure of the OWNED glossary in the private-techuity journal.

External: none directly. Definitions follow the vendor, standard and regulator sources cited in the linked chapters.

## Changelog

- 2026-10-18 — Initial spec and page (260 terms, seven sections, generated alphabetical index), AI-mediated session.
- 2026-10-18 — Added 14 terms owned by [[finops]] (FOCUS, BilledCost / EffectiveCost, ChargeCategory / ChargeClass, cut-off snapshot, commitment discount, cost of revenue / R&D / G&A, intercompany recharge, FinOps, TBM, cloud cost allocation, sub-account register, tag policy / unallocated spend, showback / chargeback, unit cost) to Accounting and Finance, Integration and Data, and Strategy and Governance, with 22 index entries; 274 terms. Row cap raised to 280. AI-mediated session.
