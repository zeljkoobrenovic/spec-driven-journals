---
status: accepted
revised: 2026-11-07
---

# Spec: Glossary

## Intent

Give *ORDERED: Architecting Commerce Platforms* one shared vocabulary. A reader new to commerce architecture who meets a term in any chapter (a catalog, order, payment, fulfillment, channel, integration, platform, security, privacy or AI term, a law or standard, or a Kestrel & Pine name) finds a short plain-language definition in one place, sees it beside the terms it is most often confused with, and follows a link to the chapter that owns it. The page also serves the writers and AI tools working on the book: a disagreement between a chapter and this page is a defect to fix in one of them.

## Audience

Newcomers to commerce architecture (engineers, product managers, analysts, consultants and leaders who have just joined a retailer, brand, wholesaler, vendor or agency), reading out of order. Most arrive with one term to look up, so the page works as a lookup first and a read second. Engineers moving into commerce benefit most.

## Success criteria

- [ ] Every term listed under "Owns" in the PLAN appears in a row, plus the acronyms chapters expand on first use (SKU, GTIN, PIM, ATP, OMS, WMS, 3PL, PSP, SCA, 3-D Secure, EDI, DESADV/ASN, SSCC, Peppol, POS, GMV, AOV, CDC, DLQ, MCP, ACP, UCP, AP2 and others).
- [ ] Terms are grouped as Preface (evidence labels, take-away tiers, scale stages, sixteen failure patterns), Parts I–XI, a standards-protocols-regulations table with scope, and Kestrel & Pine names; each row links with a valid `[[permalink]]`.
- [ ] Every definition is one or two plain sentences, follows the owning chapter, expands its acronyms and dates regulatory facts.
- [ ] Contrasts that cause real errors sit in one row: product / variant; on hand / committed / reserved; authorization / capture; settlement / payout; controller / processor; monolith / modular monolith; shadow / parallel run.
- [ ] The Kestrel & Pine section is labeled fictional and agrees with the scenario ledger and [[meet-kestrel-and-pine]].
- [ ] An alphabetical index of every term and alias is generated from the tables.
- [ ] Openers follow the reference-page format: IN THIS SECTION, YOU WILL (one sentence) and exactly three KEY POINTS.

## Non-goals

- Teaching any concept in depth; the linked chapter does that, with sources and the worked example.
- Authoritative legal, tax or standards definitions; the official source wins.
- Templates ([[toolkit]]), the model-to-chapter map ([[domain-coverage]]) and sources ([[bibliography]]).
- Every term the book mentions: failure-handling table rows, one-off vendor features and narrow mechanisms stay in their chapters.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only. A glossary has no argument to summarize or dramatize.

## Open questions

- GMV is defined three ways across chapters ("before refunds" in [[build-buy-or-assemble]] and [[commerce-scaling-stages]]; Shopify's "gross merchandise volume ... net of refunds" in [[case-shopify]]); the row says definitions differ. Align the two Part X chapters in their next review.
- SKU is "one sellable variant" in the ledger and [[journey-of-an-order]], but "the merchant's code for that variant" in [[product-information]]; the row carries both.
- Who re-checks the page when chapters are revised? Working assumption: rerun the generator in each review cycle.

## Decision log

- 2026-11-07 — Mirrored the sibling glossaries: grouped by part, evidence labels and failure patterns first, fictional names last, index generated from the tables by `_research/glossary-tools/assemble.py` from `rows.py`.
- 2026-11-07 — Replaced the sibling's market-register table with a "Standards, Protocols and Regulations" table (term, scope, short name, meaning, chapter), because this book's external vocabulary is EU law, national e-invoicing and fiscal rules, US rules and global standards.
- 2026-11-07 — Definitions harvested from each chapter's bold first-use definitions and definition tables, then trimmed by dropping minor mechanisms and failure-handling cases; slash rows hold contrasted terms.
- 2026-11-07 — WHY IT MATTERS callout omitted, following the author's decision to drop it from every page.

## Sources

- Every chapter of the book, via the links in each row; [[introduction]], [[where-commerce-platforms-go-wrong]], [[meet-kestrel-and-pine]].
- External sources are those cited in the owning chapters, collected in [[bibliography]].

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
