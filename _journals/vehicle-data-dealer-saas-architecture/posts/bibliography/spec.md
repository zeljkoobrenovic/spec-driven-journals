---
status: accepted
revised: 2026-10-22
---

# Spec: Bibliography

## Intent

Give readers one register of the public sources the pages cite, findable by topic and by chapter. Each entry states the year the citing chapter gave, what kind of evidence it is and which pages rely on it, so a reader can weigh a claim by the kind and age of the source behind it and move between a source and the argument it supports. Registers, statutes and data licenses carry much of this book's argument, so the register separates official registers and law, court and competition decisions, filings, product and API documentation, standards, research and practitioner and press sources. The page follows the bibliographies of LISTED and BOOKED: stable identifiers, a topic index, per-entry citing chapters and the reading rules stated once. It is generated, not hand-written, so it can be regenerated as other sessions finish the pages.

Productscape bricks covered: none. The Productscape domain model of a Dutch vehicle-data company (VWE), built from public sources, appears once, as the author's working model, and is mapped in [[domain-coverage]].

## Audience

Chief Architects, vehicle-data and dealer-SaaS platform architects, and engineering leaders who want to check a company claim, a register's access terms, a legal date or a practice recommendation against its source. Reviewers and later writing sessions use it to see which sources each chapter rests on.

## Success criteria

- [x] Front matter, then IN THIS SECTION, YOU WILL; KEY POINTS with exactly three bullets; two failure patterns (Provenance Amnesia, License Blindness); `<br>`; an intro covering the October 2026 research, Dutch and German sources, gated and secondary sources, the Productscape model and 2026 company names.
- [x] Every entry was harvested from a `## Sources and Evidence` section of a page in `config.yaml`; nothing is added that no page cites; URLs are copied exactly; pointer lines, the internal research briefs and plan, and cross-links to the companion books are not entries.
- [x] Entries are deduplicated by normalized URL, by CFR section, CELEX number and RFC number, and by explicit equivalences; they carry identifiers R1, R2, … in topic order; new sources append from the next free R-number and are never renumbered (the registry is `_research/bib-tools/ids.json`).
- [x] Each entry has identifier, title, publisher, the chapter's publication year (or "n.d."), one clause on what it supports, an evidence type and a Cited in line of `[[permalink]]` links.
- [x] Ten topic sections that follow the ten parts, each listed in the Topic Index with its identifier range and its part link; data law sits together under Part V; company records of the four case companies sit in the tenth.
- [x] Sources by Chapter lists the identifiers each page cites, in reading order.
- [x] The page ends with the Axleby sentence; the build passes and every `[[…]]` link resolves.

## Non-goals

- Further reading or annotated reading lists.
- Verifying or rewriting the chapters' citations; missing URLs, years or inconsistent metadata are reported to the chapter owners, not fixed here.
- Definitions of terms ([[glossary]]), templates ([[toolkit]]) and the model-to-chapter map ([[domain-coverage]]).

## Modalities

Article only. A reference page is not adapted into other modalities.

## Open questions

- Chapters are still being edited in parallel. Rerun the harvest with `sh _journals/vehicle-data-dealer-saas-architecture/_research/bib-tools/run.sh` whenever a page's sources change, keep `ids.json` so existing identifiers do not shift, and read the script output for UNRESOLVED, SAME TITLE, TITLE VARIANTS and YEAR CONFLICT lines.
- Three entries besides the Productscape model have no URL: Ulrich Homann's MSDN article, Evans's *Domain-Driven Design* and the *Team Topologies* book. Chapter owners may add URLs where they exist.
- Part VIII (journeys) adds almost no sources of its own; its topic holds one entry. If the journey chapters keep reusing sources, the topic may be folded into the parts above in a later edition.

## Decision log

- 2026-10-22: Generated the register by script from the pages' Sources and Evidence sections (`gen.py` → `classify.py` → `fix.py` → `render.py`, adapted from BOOKED), so the Cited in lines and Sources by Chapter come from the actual citations.
- 2026-10-22: Organized topics by the ten parts: a source sits under the part whose chapters cite it most. Legal texts, regulator guidance and judgments cited by [[data-licensing-and-governance]], [[privacy-and-retention]] or [[connected-vehicle-data]] sit together under Part V, so the data law (the GDPR, the Data Act, the DPPA and their guidance) is found in one place; register law that more Part II chapters cite stays under Part II with [[registers-and-official-data]]. Rejected: putting all law under Part VII (privacy is one chapter of five there, and the licensing chapter is where law becomes rules on every fact).
- 2026-10-22: Routed results, filings, corporate announcements and encyclopedia histories of Cox Automotive, CDK Global, Auto Trader and VWE to the tenth topic; their engineering posts and product documentation stay with the part they inform.
- 2026-10-22: Used the evidence types company engineering; company filing, report or announcement; product and API documentation; standard or specification; regulation and official register; court or competition decision; research; book; practitioner and press; encyclopedia; and the author's working model. Practitioner writing and press are one type, as both are secondary.
- 2026-10-22: Split multi-link source lines into one entry per URL with each link's own date or note; merged one document cited under two URLs (GDPR on EUR-Lex and the Publications Office, the Authenticom and Brnovich opinions at two hosts, the RDW open dataset's page, metadata and API, CFR sections at eCFR and Cornell, RFCs at the RFC Editor and Datatracker) into a single entry that keeps both links. Kept the most common metadata wording and, where chapters gave different years, the most specific citation.

## Sources

- Every page's `## Sources and Evidence` section; [[where-vehicle-platforms-go-wrong]] for Provenance Amnesia and License Blindness.
- The BOOKED bibliography tools in `_journals/stays-marketplace-architecture/_research/bib-tools/`.

## Changelog

- **2026-10-22** — Initial spec and bibliography harvested from every page's Sources and Evidence section. Status `accepted`. *(AI-mediated session)*
