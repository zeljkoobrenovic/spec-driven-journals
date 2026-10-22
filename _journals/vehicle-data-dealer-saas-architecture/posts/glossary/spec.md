---
status: accepted
revised: 2026-10-22
---

# Spec: Glossary

## Intent

Give *Architecting a Vehicle Data and Dealer SaaS Platform* one shared vocabulary. A reader who meets a term in any chapter (an identifier, a register act, a valuation or condition concept, a dealer-workflow object, a tenancy, billing or licensing term, an API, event, operations or leadership device) can find a short definition in one place, see it beside the terms it is most often confused with, decode Dutch, Belgian, German, UK and US register words, and follow a link to the chapter that owns it. The page also serves the writers and AI tools working on the book: the chapters define these terms, and a disagreement between a chapter and this page is a defect to fix in one of them.

Productscape bricks: none directly; the page covers the vocabulary of every brick mapped in [[domain-coverage]].

## Audience

Chief architects, principal engineers, data, integration and platform leads, and product and engineering directors at vehicle-data companies, dealer-software vendors, portals, lessors and dealer groups, reading the book out of order. Most arrive with one term to look up, so the page must work as a lookup first and a read second. Readers from one market also use it to decode another market's register vocabulary.

## Success criteria

- [ ] Every term listed under "Owns" in the book PLAN appears in a row, plus the key terms and acronyms chapters define on first use (VIN, WMI, DMS, CRM, ADF, STAR, SoH, BMS, MPP, GPU, GRR/NRR, RLS, SCIM, RBAC/ReBAC, SLI/SLO, CDC, BOLA, MCP, DPIA, UCPD and others).
- [ ] Terms are grouped by part: Preface (evidence labels and the fifteen failure patterns), Parts I–X, a register-terms table and Axleby names. Each section is a table with the term in bold and a `[[permalink]]` in the Chapter column.
- [ ] Every definition is one or two sentences, follows the owning chapter's own definition (harvested from the chapter text, not invented), expands its acronyms and dates regulatory facts.
- [ ] The contrasts that cause real errors sit in one row or adjacent rows: vehicle / stock item / channel listing / market vehicle; plate / VIN / vehicle key; stand-time / days-to-turn; damage estimate / reconditioning cost; issued / live artifact; controller / processor; source of truth / system of record.
- [ ] The register table gives term → market → English → meaning for NL, BE, DE, UK and US terms (*tenaamstellen*, *vrijwaren*, APK, NAP, BPM, WOK, *Zulassung*, HSN/TSN, V5C, MOT, KADOE, NMVTIS, title brand and others).
- [ ] The Axleby section is clearly labeled fictional and agrees with the scenario ledger and [[meet-axleby]].
- [ ] An alphabetical index lists every row term and alias, generated from the tables so it cannot drift.
- [ ] Opening callouts follow the reference-page format: IN THIS SECTION, YOU WILL; exactly three KEY POINTS; two failure patterns. 250–400 rows.

## Non-goals

- Teaching any concept in depth; the linked chapter does that, with sources and the Axleby worked example.
- Authoritative legal, tax, register or standards definitions; the official source wins.
- Axleby's volumes, prices and incident detail beyond one line; [[meet-axleby]] and the owning chapters hold them.
- Templates ([[toolkit]]), the model-to-chapter map ([[domain-coverage]]) and sources ([[bibliography]]).
- Every term the book mentions: one-off artifacts, narrow vendor features and failure-handling table rows stay in their chapters.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only. A glossary has no argument to summarize or dramatize.

## Open questions

- A few rows paraphrase how a chapter uses a term because the chapter gives no one-sentence definition (for example error budget, version pin, upstream budget broker, match-in, adapter ownership). Recheck them in the next review pass of those chapters.
- [[bibliography]] was not yet written when this page was drafted; its link resolves once it exists.
- Who re-checks the page when chapters are revised? Working assumption: a pass during each review cycle, rerunning the generator.

## Decision log

- 2026-10-22 — Mirrored BOOKED's glossary: grouped by part, evidence labels and failure patterns first, fictional names last so they stay visibly separate, index generated from the tables.
- 2026-10-22 — Added a five-column register-terms table (term, market, English, meaning, chapter), because the book keeps Dutch and German terms in the original and the reader most often needs the gloss.
- 2026-10-22 — Definitions harvested from each chapter's bold first-use definitions and definition tables, then trimmed from 428 to 399 rows by dropping failure-handling cases, single-chapter incidents from the ledger additions and minor mechanisms; slash rows hold contrasted pairs.
- 2026-10-22 — Part X holds the public products and programs the case studies rely on (Fortellis, Bridge ID, MUVVI, Autotrader Connect, MijnVWE and others), described only as their dated sources describe them.

## Sources

Internal: every chapter of the book, harvested for bold first-use definitions and definition tables; the "Owns" lists in the book PLAN; [[where-vehicle-platforms-go-wrong]] for the fifteen patterns; [[introduction]] for the evidence labels; [[meet-axleby]] and the scenario ledger for Axleby names; the structure of BOOKED's glossary.

External: none directly. Definitions follow the regulation, register, standard and company sources cited in the linked chapters.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling in the A–Z index and Kilometra entries (License, kilometers). *(AI-mediated session)*
