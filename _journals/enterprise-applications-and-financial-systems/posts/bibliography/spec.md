---
status: accepted
revised: 2026-10-18
---

# Spec: Bibliography

## Intent

Give readers one register of the external sources the chapters cite, findable by topic and by chapter. Each entry states what kind of evidence it is and which chapters rely on it, so a reader can weigh a claim by the source behind it and move between a source and the argument it supports. The page models itself on the bibliography of OWNED, the private-techuity journal: stable identifiers, a topic index, per-entry citing chapters, and the reading rules stated once.

## Audience

Chief Architects, finance-systems and integration architects, and finance-transformation leaders who want to check a vendor claim, a regulatory date or a practice recommendation against its source. Reviewers and later writing sessions use it to see which sources each chapter rests on.

## Success criteria

- [ ] Front matter, then IN THIS SECTION, YOU WILL; KEY POINTS with exactly three bullets (sources listed because consulted; evidence types differ; facts, recommendations and the fictional Northmere kept distinct); one FAILURE PATTERN (Vendor Gravity: vendor documentation describes capability, not fit); `<br>`; an intro covering consultation dates (October 2026), partly limited web access, identifiers and evidence types.
- [ ] Every entry was harvested from a chapter's `## Sources and Evidence` section; no source is added that no chapter cites. Pointer lines ("sources in [[…]]") and the book's internal research briefs are not listed as entries.
- [ ] Entries are deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment, `.htm`, `/eng`, locale prefix and percent-encoding ignored) and carry stable identifiers R001, R002, … in topic order; sources added after the first edition take R389 onward and sit under their topic without renumbering.
- [ ] Each entry has identifier, linked title, author or publisher, year or version where the chapter gave one, one clause on what it supports, an evidence type from the fixed list (Vendor documentation, Standard or regulation, Regulator or official, Practitioner, Book, Research, News) and a Cited in line of `[[permalink]]` links.
- [ ] A Topic Index paragraph per topic gives its identifier range and where to start; fourteen topic sections follow, with Payments split into fundamentals and regulation, Adyen, Stripe, and orchestration, and the Part V case studies in their own section (Public case studies: Uber).
- [ ] Sources by Chapter lists the identifiers each chapter cites, in config order.
- [ ] The build passes and every `[[…]]` link resolves.

## Non-goals

- Further reading, annotated reading lists or "To Probe Further" material.
- Verifying or rewriting the chapters' citations; URL problems are reported to the chapter owners, not fixed here.
- Definitions of terms ([[glossary]]) and templates ([[toolkit]]).

## Modalities

Article only. A reference page is not adapted into other modalities.

## Open questions

- Rerun the harvest whenever a chapter or a Part V case study is added, and append its new sources from the next free identifier so existing identifiers do not shift.
- Some cited URLs still look fragile or inconsistent: [[vendor-portfolio-strategy]] still cites the SAP News `?p=140253` short link that other chapters replaced with the canonical URL, [[ai-in-finance]] cites the Stripe Sessions 2025 post under a `/br/` locale path, and a 2016 SAP Help path remains. Chapter owners should confirm them.

## Decision log

- 2026-10-18: Generated the register from the chapters' Sources and Evidence sections by script rather than by hand, so that the Cited in lines and Sources by Chapter come from the actual citations.
- 2026-10-18: Listed each source once, under the topic it serves best, with a Cited in line across topics, instead of repeating entries per topic.
- 2026-10-18: Used compact one-paragraph entries rather than OWNED's heading-per-entry layout because the register holds close to 400 sources.
- 2026-10-18: Kept the chapters' own clause on what each source supports, lightly normalized, so the register never claims more than the citing chapter did.

## Sources

- Every chapter's `## Sources and Evidence` section; the research briefs in `_research/brief-*.md` for context.
- [[where-finance-architecture-goes-wrong]] for the Vendor Gravity pattern.

## Changelog

- 2026-10-18: Update pass, AI-mediated session: harvested chapter 33 ([[incremental-modernization]]), the new Part V case study ([[case-uber-payments]]) and the [[toolkit]]'s new sources section; added R389 (Regulation S-K Item 308, under Accounting, controls and regulation) and a new topic section, Public case studies: Uber (R390–R413), for 413 sources in all. Recomputed every Cited in line and Sources by Chapter from the chapters' current sources, so citations dropped in review passes are gone and chapter 25 now cites R402. Updated URLs fixed in the chapters (canonical SAP News URLs and titles for R125–R127, fisglobal without `:443` for R322, the Workday newsroom release for R337, the Gartner newsroom URL for R359, with the CFOtech report noted). Added source counts per evidence type to the intro table and switched the remaining British spellings to American.
- 2026-10-18: Initial spec and page, AI-mediated session: 388 sources harvested from the 43 pages that cite external sources, deduplicated, typed and indexed by topic and by chapter.
