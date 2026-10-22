# Research Brief — vehicle data and dealer SaaS research briefs

You are preparing one verified research brief for **Architecting a Vehicle Data and Dealer SaaS Platform**, a serious architecture book for chief architects, principal engineers and engineering leaders. It follows the format and evidence discipline of its sibling books LISTED (`_journals/listing-systems-architecture/`), BOOKED (`_journals/stays-marketplace-architecture/`) and RECONCILED (`_journals/finance-systems-architecture/`).

ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/`

## The book's frame

The book is about platforms that combine two businesses around the used (and new) car:

- **Vehicle data services** — turning registers, manufacturer build data, insurer and service records, odometer readings, adverts and transactions into vehicle identity, specification, history, condition, valuation and market insight; sold as reports, APIs, file enrichment and dashboards to dealers, lessors, insurers, software vendors, portals and consumers. Examples: Carfax and AutoCheck (Experian), S&P Global Mobility, J.D. Power, Black Book, Kelley Blue Book, NHTSA vPIC, NMVTIS (US); HPI, Cap HPI, DVLA and DVSA MOT data, Auto Trader UK valuations (UK); DAT, Schwacke/Autovista, KBA (Germany); RDW, NAP, Autotelex, VWE (Netherlands); Jato, Autovista Group (pan-European).
- **Dealer SaaS** — the software in which dealers and dealer groups acquire, appraise, stock, price, merchandise, advertise (syndicate to portals), handle leads, sell, finance, register and trade vehicles, integrated with dealer management systems (DMS) and CRMs. Examples: Cox Automotive (vAuto, Dealertrack, VinSolutions, Autotrader, Manheim), CDK Global, Reynolds and Reynolds, Tekion, DealerSocket, Keyloop, Pinewood, incadea, Motorhub, VWE MijnVWE, Autotrader UK's retailer products, mobile.de and AutoScout24 dealer tools.

The book's geography is **Europe-first (Netherlands, Belgium, Germany, United Kingdom) with the United States as the main contrast**. Every chapter has a section comparing markets, so country-specific facts (registers, access regimes, taxes, valuation providers, DMS ecosystems, lead standards, privacy law) matter.

## Format to match

Read the first 60 lines of `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/listing-systems-architecture/_research/brief-search-discovery.md` and copy its conventions exactly:

- Title `# Research brief: <topic>` and a "Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*" line.
- A "How to read this brief" section with the three tags: **[VERIFIED: url, published YYYY-MM(-DD)]** (you fetched the page in this session and it supports the claim; date = publication date, or "n.d." for undated product pages, with "accessed 2026-10" noted), **[WIDELY REPORTED: url, YYYY]** (reputable secondary source), **[ASSUMPTION/JUDGEMENT]** (industry knowledge or inference; every statement about a proprietary system a company has not described).
- Evidence-age warnings (say when a source is older than ~3 years and may describe a replaced system), ⚠ volatility flags, and an honest "Research limitation" paragraph naming what you could not verify.
- Numbered PARTs and sections; tables of contrasts where useful; quote sparingly and accurately.
- **Per section, a short "Across markets" note** (NL / BE / DE / UK / US) where the countries differ.
- **Per section, a short "Architecture implications" note**: what the facts imply for system design (tagged ASSUMPTION/JUDGEMENT).
- End with: "Key numbers" table (each with source and date), "Open questions / not verifiable", and "Source list" (title, publisher/author, year, URL).

## Research rules

- Prefer primary sources: official product and API documentation (developer portals, OpenAPI specs, feed specifications), standards (ISO 3779/3780/4030, STAR, ADF/XML, schema.org, Standard Webhooks), regulators and official registers (RDW, DVLA, DVSA, KBA, NHTSA, NMVTIS/DOJ, FTC, EUR-Lex texts), investor filings and annual reports, company engineering blogs and conference talks, court and competition-authority decisions.
- Medium pages often return 403: fetch the RSS feed instead (`https://medium.com/feed/<publication>`). EUR-Lex blocks fetches; the EU Publications Office serves official texts: `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: application/xhtml+xml` (use curl in Bash). arXiv abstracts fetch reliably. Dutch and German official pages are fine to read; quote them in English translation and say so.
- The web-search quota is shared with other researchers running in parallel; search efficiently, then fetch known URLs directly.
- Never invent proprietary internals (service names, volumes, algorithms) of real companies. If something is only plausible, tag it ASSUMPTION/JUDGEMENT.
- Record every source with its publication year. Aim for **40–90 tagged claims** and **350–700 lines**. Depth and accuracy beat breadth.

## Deliverable

Write only `ROOT/_research/brief-<your-topic>.md` (the name is given in your task). Do not edit any other file.

## Report back

Under 150 words: file written, line count, the five most important findings for the book's architecture, and the biggest gaps you could not verify.
