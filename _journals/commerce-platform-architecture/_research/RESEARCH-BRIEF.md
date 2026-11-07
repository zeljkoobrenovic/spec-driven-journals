# Research Brief — ORDERED research briefs

You are preparing one verified research brief for **ORDERED: Architecting Commerce Platforms**, a book that teaches readers who are **new to commerce architecture** how commerce systems fit together, why the architectural decisions matter, and how they evolve with scale. It follows the evidence discipline of its sibling books (BOOKED, LISTED, RECONCILED, *Architecting a Vehicle Data and Dealer SaaS Platform*).

ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/commerce-platform-architecture/`

## The book's frame

Read `ROOT/PLAN.md` ("Positioning", "Structure" and the chapter contracts that name your brief) so you know which chapters your brief feeds. The book is **platform-neutral** and **evidence-led**: it covers hosted SaaS platforms (Shopify, BigCommerce/Commerce.com), enterprise suites (SAP Commerce, Salesforce Commerce Cloud, Adobe Commerce), open source (Magento/Mage-OS, WooCommerce, Shopware, PrestaShop), composable vendors (commercetools, Elastic Path, Medusa, Saleor), ERP-centred commerce (Odoo, JTL, PlentyONE, Microsoft Business Central), and the specialist layers around them (OMS, PIM, WMS, shipping, returns, search, payments, EDI, marketplace integration). Geography: Europe-first (Netherlands, Belgium, Germany) with the United States and global practice as the contrast.

The book's running example is fictional; your brief is about **real, public, dated evidence**.

## A private starting point you may read, with rules

The author's private journal *FEDERATED* (`/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/hidden-katapull-group-cto/`) contains seven research briefs in `_research/briefs/` (platforms and ERP landscape, Shopify architecture, Shopify commerce surface and agentic commerce, regulation, two briefs on Katapull's labels, and a Productscape digest) and an appendix of about 250 sources at `posts/08-sources/index.md`. You **may read them to find sources quickly**. Rules:

- Everything you carry over must be **re-verified in this session** by fetching the URL; tag it by what you found, not by the old tag.
- Never copy any line that cites a "supplied brief", "the brief", "productscape" or "Katapull internal"; those rest on a confidential document. Facts about Katapull and its labels are allowed **only** when they come from public pages or press that you fetched.
- Do not reproduce that journal's inferences about Katapull. Your brief is for a platform-neutral book.

## Format to match

Read the first 60 lines of `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/_research/brief-dms-integration.md` and copy its conventions:

- Title `# Research brief: <topic>` and a "Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*" line.
- A "How to read this brief" section with the three tags: **[VERIFIED: url, published YYYY-MM(-DD)]** (you fetched the page in this session and it supports the claim; date = publication date, or "n.d." for undated product pages, with "accessed 2026-11" noted), **[WIDELY REPORTED: url, YYYY]** (reputable secondary source), **[ASSUMPTION/JUDGEMENT]** (industry knowledge or inference; every statement about a proprietary system a company has not described).
- Evidence-age warnings (say when a source is older than about three years and may describe a replaced system), ⚠ volatility flags for anything likely to change (pricing, product names, protocol status), and an honest "Research limitation" paragraph naming what you could not verify.
- Numbered PARTs and sections; tables of contrasts where useful; quote sparingly and accurately.
- **Per section, a short "For newcomers" note**: the two or three terms a reader new to the field must have defined, each in one plain sentence, so writers can lift the definitions.
- **Per section, a short "Architecture implications" note**: what the facts imply for system design and for the four scale stages (Starting / Growing / Omnichannel / Group, defined in `ROOT/_research/scenario-ledger.md`), tagged ASSUMPTION/JUDGEMENT.
- End with: "Key numbers" table (each with source and date), "Open questions / not verifiable", and "Source list" (title, publisher/author, year, URL).

## Research rules

- Prefer primary sources: official product and API documentation (developer portals, changelogs, API version pages), standards (GS1 GTIN/GLN/SSCC, EDIFACT, Peppol BIS, EN 16931, cXML, OpenAPI, Standard Webhooks, PCI DSS, schema.org), regulators and official texts (EUR-Lex via the Publications Office, national tax authorities, FTC, EU Commission pages), investor filings and annual reports (SEC EDGAR, annual reports), company engineering blogs and conference talks, court and competition-authority decisions, peer-reviewed or well-known practitioner publications.
- Medium pages often return 403: fetch the RSS feed instead (`https://medium.com/feed/<publication>`). EUR-Lex blocks fetches; the EU Publications Office serves official texts: `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: application/xhtml+xml` (use curl in Bash). arXiv abstracts fetch reliably. Dutch and German official pages are fine to read; quote them in English translation and say so.
- The web-search quota is shared with other researchers running in parallel; search efficiently, then fetch known URLs directly.
- Never invent proprietary internals (service names, volumes, algorithms) of real companies. If something is only plausible, tag it ASSUMPTION/JUDGEMENT.
- Never put the user's email address or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies. For SEC EDGAR (which requires a contact User-Agent), use `research-bot admin@example.com` or skip EDGAR.
- Record every source with its publication year. Aim for **40–90 tagged claims** and **350–700 lines**. Depth and accuracy beat breadth.

## Deliverable

Write only `ROOT/_research/brief-<your-topic>.md` (the name is given in your task). Do not edit any other file.

## Report back

Under 150 words: file written, line count, the five most important findings for the book's architecture teaching, and the biggest gaps you could not verify.
