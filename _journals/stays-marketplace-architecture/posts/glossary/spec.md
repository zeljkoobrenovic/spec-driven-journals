---
status: accepted
revised: 2026-10-21
---

# Spec: Glossary

## Intent

Give *BOOKED* one shared vocabulary. A reader who meets a term in any chapter (a marketplace type, a supply or connectivity term, an ARI or pricing concept, a booking, payment, tax, trust or regulatory term, a platform or leadership device) can find a plain-language definition in one place, see it beside the terms it is most often confused with, learn where the word means something different on the hotel side and the homes side, and follow a link to the chapter that owns it. The page also serves the writers and AI tools working on the book: the chapters follow these definitions, so a disagreement between a chapter and this page is a defect to fix in one of them.

Productscape domains: none directly; the page covers the vocabulary of every domain mapped in [[domain-coverage]].

## Audience

Chief architects, principal engineers, search, pricing, payments, data and ML leads, and product and engineering directors of OTAs, hosted-stays and vacation-rental marketplaces, channel managers and PMS vendors, reading the book out of order. Most arrive with one term to look up, so the page must work as a lookup first and a read second. Readers from one side of the industry (hotels or homes) also use it to decode the other side's words.

## Success criteria

- [ ] Every term listed under "Owns" in the book PLAN appears in a row, plus the key terms and acronyms the chapters define on first use (ARI, PMS, CRS, GDS, OTA, LOS, ADR, RevPAR, VCC, SCA, MIT, MoR, STR, DSA, DMA, P2B, DAC7, ViDA, iCal, HTNG, OpenTravel and others).
- [ ] Terms are grouped by part: evidence labels and the sixteen failure patterns; Parts I–IX (with the few generic Part X terms under Part IX); Corvane names. Each section is a `| Term | Definition | Chapter |` table with the term in bold.
- [ ] Every definition is one or two plain sentences, agrees with the owning chapter, expands its acronyms, dates regulatory facts (as of 2026), and says how the term differs between the accommodation marketplace and hosted stays where that difference matters.
- [ ] The contrasts that cause real errors sit in one row or adjacent rows: property / unit / listing; inventory / availability; rate plan / product; offer / reservation; agency / merchant / facilitated payments and merchant of record; overbooking / oversell / double booking; gross / net / stayed reservations; trust decision / enforcement action.
- [ ] The Corvane section is clearly labeled fictional, and every name in it agrees with the scenario ledger and with [[meet-corvane]]'s table of group platforms.
- [ ] Every Chapter cell is a valid `[[permalink]]` of this book.
- [ ] An alphabetical index at the end lists every row term and abbreviation (abbreviations with their expansion, so ADR the rate and ADR the decision record are distinct), generated from the tables so it cannot drift.
- [ ] Opening callouts follow the book's reference-page format: IN THIS SECTION, YOU WILL; exactly three KEY POINTS; two failure patterns.

## Non-goals

- Teaching any concept in depth; the linked chapter does that, with sources and the Corvane worked example.
- Authoritative legal, tax, standards or vendor definitions; the regulation, standard or vendor documentation wins.
- Corvane's cast, volumes and incidents; [[meet-corvane]] owns them. Corvane appears only in the evidence-label row and the Corvane-names section.
- Templates ([[toolkit]]), the model-to-chapter map ([[domain-coverage]]) and sources ([[bibliography]]).
- Every term the book mentions: one-off Corvane artifacts and narrow vendor features stay in their chapters.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only. A glossary has no argument to summarize or dramatize.

## Open questions

- [[introduction]] now exists; [[bibliography]] was not yet written when this page was drafted, and its link resolves once it exists.
- About 25 rows paraphrase how a chapter uses a term because the chapter gives no one-sentence definition (for example open book, load shedding, geocoding, disruption registry, merchandising slots). Recheck them in the next review pass of those chapters.
- Who re-checks the page when chapters are revised? Working assumption: a pass during each review cycle, rerunning the generator.

## Decision log

- 2026-10-21 — Grouped by part rather than by subject, following LISTED's glossary, with evidence labels and failure patterns first because every chapter uses them, and Corvane names last so fictional terms stay visibly separate.
- 2026-10-21 — Rows harvested chapter by chapter from bold first-use definitions and the PLAN's Owns lists, then de-duplicated so each term has one home: the chapter that owns it per PLAN, else the one that defines it most fully.
- 2026-10-21 — The page runs longer than LISTED's (about 557 rows against about 400) because the book has nine content parts and 47 chapters; slash rows hold contrasted pairs to keep the count down.
- 2026-10-21 — Alphabetical index generated by a script with a small alias map; section anchors are `<a id>` tags in the headings because the renderer does not generate heading ids.

## Sources

Internal: every chapter of the book (Parts I–IX, the Part X case studies and introductions), harvested for bold first-use definitions; the "Owns" lists in the book PLAN; [[where-stay-platforms-go-wrong]] for the sixteen patterns; [[meet-corvane]] and the scenario ledger for Corvane names; the structure of LISTED's glossary.

External: none directly. Definitions follow the regulation, standard and company sources cited in the linked chapters.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: renamed Visibility Plus to Front Row, fixed two chapter links (occupancy-based pricing, physical and sellable inventory), dropped two duplicate agency/merchant rows, American spelling in row files; regenerated with assemble.py. *(AI-mediated session)*
