---
status: accepted
revised: 2026-10-21
---

# Spec: Bibliography

## Intent

Give readers one register of the public sources the pages cite, findable by topic and by chapter. Each entry states the year the citing chapter gave, what kind of evidence it is and which pages rely on it, so a reader can weigh a claim by the kind and age of the source behind it and move between a source and the argument it supports. The page follows the bibliography of LISTED (`listing-systems-architecture`): stable identifiers, a topic index, per-entry citing chapters and the reading rules stated once. It is generated, not hand-written, so it can be regenerated as the remaining pages are finished.

Productscape domains covered: none. The Productscape models appear once, as the author's working model, and are mapped in [[domain-coverage]].

## Audience

Chief Architects, OTA and hosted-stays platform architects, and engineering leaders who want to check a company claim, a regulatory date or a practice recommendation against its source. Reviewers and later writing sessions use it to see which sources each chapter rests on.

## Success criteria

- [x] Front matter, then IN THIS SECTION, YOU WILL; KEY POINTS with exactly three bullets; one failure pattern (The Hotel-Shaped Home); `<br>`; an intro covering the October 2026 research, login-gated and secondary sources, and 2026 naming.
- [x] Every entry was harvested from a `## Sources and Evidence` section of a page in `config.yaml`; nothing is added that no page cites; URLs are copied exactly; pointer lines, the internal research briefs and plan, and cross-links to LISTED and RECONCILED are not entries.
- [x] Entries are deduplicated by normalized URL and carry identifiers R1, R2, … in topic order; new sources append from the next free R-number and are never renumbered (the registry is `_research/bib-tools/ids.json`).
- [x] Each entry has identifier, title, publisher, the chapter's publication year (or "n.d."), one clause on what it supports, an evidence type and a Cited in line of `[[permalink]]` links.
- [x] Ten topic sections that follow the ten parts, each listed in the Topic Index with its identifier range and its part link; company filings, results and histories of the case companies sit in the tenth.
- [x] Sources by Chapter lists the identifiers each page cites, in reading order.
- [x] The page ends with the Corvane sentence; the build passes and every `[[…]]` link resolves.

## Non-goals

- Further reading or annotated reading lists.
- Verifying or rewriting the chapters' citations; missing URLs or years are reported to the chapter owners, not fixed here.
- Definitions of terms ([[glossary]]), templates ([[toolkit]]) and the model-to-chapter map ([[domain-coverage]]).

## Modalities

Article only. A reference page is not adapted into other modalities.

## Open questions

- Part I and the Reference pages are still being finished. Rerun the harvest with `sh _journals/stays-marketplace-architecture/_research/bib-tools/run.sh` whenever a page's sources change, keep `ids.json` so existing identifiers do not shift, and read the script output for unresolved aliases and year conflicts.
- Six entries have no URL: the Productscape models, the two DDD books, the Expedia Booking Notification API requirements and the SiteMinder pmsXchange reference (both seen only as search excerpts), and European Commission press release IP/24/2561, which [[marketplace-intelligence]] cites through the research brief. Chapter owners should add primary URLs where they exist.
- About 135 entries carry "n.d.", mostly living partner documentation and help-center pages, where the access date is the useful date. Three company engineering entries carry "n.d." (an AWS case study, Airbnb's research-publications page and the X-Pipe README); the style guide asks for a year on company engineering evidence.

## Decision log

- 2026-10-21: Generated the register by script from the pages' Sources and Evidence sections (`gen.py` → `classify.py` → `fix.py` → `render.py`, adapted from LISTED), so the Cited in lines and Sources by Chapter come from the actual citations.
- 2026-10-21: Organized topics by the ten parts: a source sits under the part whose chapters cite it most; legal texts used by [[stays-regulation]] sit together under Part VII; filings, results and company histories of Booking Holdings, Airbnb, Expedia Group and Trip.com Group sit under the tenth topic with the sources only the case studies use.
- 2026-10-21: Split multi-link source lines into one entry per URL with each link's own date or note, and merged one document cited under two URLs (the Digital Markets Act on EUR-Lex and the Publications Office; Airbnb's Q2 2026 shareholder letter as PDF, SEC exhibit and investor page; two Booking.com and Expedia documentation paths; one Airbnb post on Medium and airbnb.tech) into a single entry that keeps both links.
- 2026-10-21: Kept the most common metadata wording across citing chapters and, where chapters gave different years, the most specific citation.

## Sources

- Every page's `## Sources and Evidence` section; [[where-stay-platforms-go-wrong]] for The Hotel-Shaped Home.
- The LISTED bibliography and its tools in `_journals/listing-systems-architecture/_research/bib-tools/`.

## Changelog

- **2026-10-21** — Initial spec and bibliography harvested from every page's Sources and Evidence section. *(AI-mediated session)*
