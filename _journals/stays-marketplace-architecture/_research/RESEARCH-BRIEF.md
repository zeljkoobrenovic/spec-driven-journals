# Research Brief — BOOKED research briefs

You are preparing one verified research brief for **BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces**, a serious architecture book for chief architects, principal engineers and engineering leaders. It follows the format and evidence discipline of its sibling book LISTED.

ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/`

## The book's frame

The book covers two marketplace types and compares them wherever their architectures differ:

- **Travel accommodation marketplace (OTA-style)** — Booking.com, Expedia/Hotels.com, Agoda, Trip.com: hotels and other professionally run properties, room types and rate plans, inventory pushed by channel managers and property-management systems (PMS), connectivity standards (OpenTravel/OTA, HTNG), GDS and bedbanks, merchant versus agency payment models.
- **Hosted stays marketplace (peer-to-peer / short-term rental)** — Airbnb, Vrbo, others: whole homes and rooms run by individual and professional hosts, one-unit calendars, iCal sync, host-set and smart pricing, request-to-book, guest–host trust, damage protection, payouts to individuals, short-term-rental regulation.

## Format to match

Read the first 60 lines of `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/listing-systems-architecture/_research/brief-search-discovery.md` and copy its conventions exactly:

- Title `# Research brief: <topic>` and a "Prepared 21 October 2026 for chapter writers of *BOOKED…*" line.
- A "How to read this brief" section with the three tags: **[VERIFIED: url, published YYYY-MM(-DD)]** (you fetched the page in this session and it supports the claim; date = publication date), **[WIDELY REPORTED: url, YYYY]** (reputable secondary source), **[ASSUMPTION/JUDGEMENT]** (industry knowledge or inference; every statement about a proprietary system a company has not described).
- Evidence-age warnings (say when a source is older than ~3 years and may describe a replaced system), ⚠ volatility flags, and an honest "Research limitation" paragraph naming what you could not verify.
- Numbered PARTs and sections; tables of contrasts where useful; quote sparingly and accurately.
- **Per section, a short "OTA vs hosted stays" note** where the two marketplace types differ.
- End with: "Key numbers" table (each with source and date), "Open questions / not verifiable", and "Source list" (title, publisher/author, year, URL).

## Research rules

- Prefer primary sources: company engineering blogs (Booking.com: `booking.ai`, `medium.com/booking-com-development`, Booking developers docs `developers.booking.com`; Airbnb: `medium.com/airbnb-engineering` and `airbnb.tech`; Expedia Group: `medium.com/expedia-group-tech`, `developers.expediagroup.com`; Agoda: `medium.com/agoda-engineering`; Trip.com tech blog; Vrbo/HomeAway), conference talks (QCon, InfoQ, KDD, RecSys, SIGIR papers on arXiv / ACM), investor filings (10-K, annual reports), public API docs, standards bodies (OpenTravel Alliance, HTNG/HFTP, IETF iCalendar RFC 5545), regulators (EUR-Lex, EU Publications Office, national/city STR rules).
- Medium pages often return 403: fetch the RSS feed instead, e.g. `https://medium.com/feed/airbnb-engineering`, `https://medium.com/feed/booking-com-development`, `https://medium.com/feed/expedia-group-tech`, `https://medium.com/feed/agoda-engineering` (the feed holds only recent posts; for older posts try the article URL, `https://<publication>.medium.com/...`, the arXiv paper, or a talk transcript on InfoQ). EUR-Lex blocks fetches; the EU Publications Office serves official texts: `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: application/xhtml+xml` (use curl in Bash). arXiv abstracts fetch reliably.
- The web-search quota is shared with other researchers running in parallel; search efficiently, then fetch known URLs directly.
- Never invent proprietary internals (service names, volumes, algorithms) of real companies. If something is only plausible, tag it ASSUMPTION/JUDGEMENT.
- Record every source with its publication year. Aim for **40–90 tagged claims** and **400–800 lines**. Depth and accuracy beat breadth.

## Deliverable

Write only `ROOT/_research/brief-<your-topic>.md` (the name is given in your task). Do not edit any other file.

## Report back

Under 150 words: file written, line count, the five most important findings for the book's architecture, and the biggest gaps you could not verify.
