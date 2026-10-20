# LISTED — Manuscript Workspace

**LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms**

How architects and engineering leaders design, scale, govern and evolve the systems behind classifieds and listing marketplaces — listings, ingestion, search, trust, monetization and the multi-country platforms beneath them.

## Layout

- `config.yaml` — reading order: Preface (3 pages), Parts I–VIII (each with an unnumbered part introduction; 45 chapters, folders `01`–`45`), Part IX PRACTICE (introduction and six public case studies, folders `46`–`51`) and Reference (toolkit, glossary, bibliography): **66 configured pages**, each with a companion `spec.md`. Public permalinks are unprefixed and stable.
- `PLAN.md` — positioning, structure and one contract per chapter (question, scope, Veldmark thread, terms each chapter owns, research briefs).
- `posts/<folder>/index.md` + `spec.md` — each page and the spec it was written against (spec-driven authoring, see the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — format, voice, evidence discipline (documented fact with date, industry practice, labeled inference, recommendation, illustration), diagram rules, the fifteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Veldmark Group**, the fictional running example. Pages must agree with it.
  - `WRITER-BRIEF.md` and the other `*-BRIEF.md` files — instructions given to AI writing, review and illustration sessions.
  - `brief-*.md` — verified research briefs on Adevinta, OLX, eBay Classifieds Group, AVIV and property portals, automotive and other verticals, search and discovery, trust and safety and regulation, platform/data/ML, monetization, and listing data and ingestion. Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION with publication dates.
  - `productscape-digest.md` — digest of the two Productscape domain models (general listings and real estate) the book started from.
- `_input/` — private inputs (empty at creation).

## Provenance and neutrality

The book grew out of two generic Productscape marketplace domain models and public research. Company-specific statements are cited to public, dated sources; where companies have not published how their systems work, the book says so and offers clearly labeled reference-architecture inferences instead. Every worked example uses Veldmark, a fictional composite.

## Conventions

Same reference format as RECONCILED (`_journals/finance-systems-architecture`) and OWNED (`_journals/private-techuity`): callout blocks (IN THIS CHAPTER / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS / FAILURE PATTERNS), a running fictional example, tables of contrasts, mermaid figures, `[[permalink]]` cross-links, and a Sources and Evidence section per page.
