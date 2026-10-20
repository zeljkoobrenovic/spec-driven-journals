---
status: accepted
revised: 2026-10-20
---

# Spec: Bibliography

## Intent

Give readers one register of the public sources the pages cite, findable by topic and by chapter. Each entry states the year the citing chapter gave, what kind of evidence it is and which pages rely on it, so a reader can weigh a claim by the kind and age of the source behind it and move between a source and the argument it supports. The page follows the bibliography of RECONCILED (`finance-systems-architecture`): stable identifiers, a topic index, per-entry citing chapters and the reading rules stated once.

## Audience

Chief Architects, marketplace platform and search architects, and engineering leaders who want to check a company claim, a regulatory date or a practice recommendation against its source. Reviewers and later writing sessions use it to see which sources each chapter rests on.

## Success criteria

- [ ] Front matter, then IN THIS SECTION, YOU WILL; KEY POINTS with exactly three bullets; one failure pattern (The Platform Mandate); `<br>`; an intro covering the October 2026 research, secondary summaries and 2026 naming.
- [ ] Every entry was harvested from a `## Sources and Evidence` section of a page in `config.yaml`; nothing is added that no page cites; URLs are copied exactly; pointer lines and the internal research briefs are not entries.
- [ ] Entries are deduplicated by normalized URL and carry identifiers R1, R2, … in topic order; new sources append from the next free R-number and are never renumbered (the registry is `_research/bib-tools/ids.json`).
- [ ] Each entry has identifier, title, publisher, the chapter's publication year (or "n.d."), one clause on what it supports, an evidence type and a Cited in line of `[[permalink]]` links.
- [ ] Thirteen topic sections, six of them company sections (Adevinta and Schibsted; OLX and Prosus; eBay Classifieds, Kleinanzeigen and Marktplaats; AVIV and property portals; automotive; other marketplaces), each listed in the Topic Index with its identifier range.
- [ ] Sources by Chapter lists the identifiers each page cites, in reading order.
- [ ] The page ends with the Veldmark sentence; the build passes and every `[[…]]` link resolves.

## Non-goals

- Further reading or annotated reading lists.
- Verifying or rewriting the chapters' citations; missing URLs or years are reported to the chapter owners, not fixed here.
- Definitions of terms ([[glossary]]) and templates ([[toolkit]]).

## Modalities

Article only. A reference page is not adapted into other modalities.

## Open questions

- Rerun the harvest (`gen.py` → `classify.py` → `fix.py` → `render.py` in `_research/bib-tools/`) whenever a page's sources change; keep `ids.json` so existing identifiers do not shift.
- Eight entries have no URL (among them the Prosus FY25 results booklet, the Schibsted Q3 2016 investor presentation, the eBay Classifieds Group archived pages, the two DDD books and Broder 1997), and the OLX duplicate-detection posts in [[media-pipeline]] are cited as known only through search summaries. Chapter owners should add primary URLs where they exist.
- Several company engineering entries carry "n.d." (for example the Airbnb Tech guest-journey post, the Chronon and FIAAS repositories and the AVIV Group pages); the style guide asks for a year on company engineering evidence.

## Decision log

- 2026-10-19: Generated the register by script from the pages' Sources and Evidence sections, so the Cited in lines and Sources by Chapter come from the actual citations.
- 2026-10-19: Split multi-link source lines into one entry per URL, and merged one document cited under two URLs (the DSA, Omnibus and P2B texts; one Adevinta press release; the Base Adresse Nationale) into a single entry that keeps both links.
- 2026-10-19: Put company-specific sources in six company sections and generic engine documentation and research papers, including company-authored papers, under the technical topic they inform.
- 2026-10-19: Kept the most common metadata wording across citing chapters and, where chapters gave different years, the most specific citation.

## Sources

- Every page's `## Sources and Evidence` section; [[where-listing-systems-go-wrong]] for The Platform Mandate.
- The RECONCILED bibliography and its tools in `_journals/finance-systems-architecture/_research/bib-tools/`.

## Changelog

- **2026-10-19** — Initial bibliography harvested from every page's Sources and Evidence section. *(AI-mediated session)*
- **2026-10-20** — Term alignment with the glossary: "projection" → "read model", "copy register" → "consumer registry", "filter compiler" → "query compiler", where they occur on this page. *(AI-mediated session)*
