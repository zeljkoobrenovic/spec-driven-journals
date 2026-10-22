# Architecting a Vehicle Data and Dealer SaaS Platform — Manuscript Workspace

How architects and engineering leaders design, integrate, operate and evolve platforms that turn registers, build data, history records and market data into vehicle identity, history and value, and put that data to work in the daily workflows of dealers, dealer groups, traders and lessors. The book covers both halves of such a platform — vehicle data services and dealer SaaS — and compares markets (Netherlands and Belgium, Germany, the United Kingdom, the United States) wherever registers, regulation and ecosystems change the design.

## Layout

- `config.yaml` — reading order, **70 configured pages**, each with a companion `spec.md`. Public permalinks are stable.
  - Preface: 3 pages.
  - Parts I–IX: each opens with an unnumbered part introduction; 49 chapters in folders `01`–`49`. Part VIII (JOURNEYS) holds four end-to-end scenarios.
  - Part X PRACTICE: an introduction and four public case studies, folders `50`–`53`.
  - Reference: domain coverage, toolkit, glossary, bibliography.
- `PLAN.md` — positioning, structure and one contract per chapter: the question, the scope, the Axleby thread, the terms the chapter owns, the Productscape bricks it covers, and its research briefs.
- `posts/<folder>/index.md` + `spec.md` — each page and the spec it was written against (spec-driven authoring, see the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — format, voice, evidence discipline (documented fact with date, industry practice, labeled inference, recommendation, illustration, labeled assumption), the "Across Markets" rule, diagram rules, the fifteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Axleby Group**, the fictional running example (Axleby Data, Lotwise, Showroomly, Axleby Trade, Odolo). Pages must agree with it.
  - `RESEARCH-BRIEF.md`, `WRITER-BRIEF.md`, `REVIEWER-BRIEF.md` — instructions given to the AI research, writing and review sessions.
  - `brief-*.md` — verified research briefs. Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION with publication dates.
  - `productscape-digest.md` — digest of the Productscape domain model: brick inventory, personas, data assets, stressors, vocabulary and gaps.
  - `tools/render_check.py` — loads built pages in Playwright and reports mermaid failures and unresolved or cross-journal links.
- `_input/` — private inputs (empty at creation).

## Provenance and neutrality

The book grew out of a Productscape domain model of one real Dutch vehicle-data company (VWE Automotive), built from public sources, and out of public research. The model served as a research map; the book is not a description of that company. VWE appears only in its own public case study, built from public, dated sources.

Company-specific statements are cited to public, dated sources. Where companies have not published how their systems work, the book says so and offers clearly labeled reference-architecture inferences instead. Illustrative volumes, latency targets and costs are labeled as assumptions. Every worked example uses Axleby, a fictional composite.

## Conventions

Same reference format as BOOKED, LISTED and RECONCILED:

- callout blocks: IN THIS CHAPTER / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS / FAILURE PATTERNS;
- a running fictional example;
- tables of contrasts and requirement tables;
- numbered figures;
- `[[permalink]]` cross-links;
- a Sources and Evidence section on every page.

Specific to this book: every chapter in Parts II–VII has an **"Across Markets: What Changes by Country"** section, and Part VIII walks four end-to-end journeys with their failure cases and recovery.

Diagrams are written as mermaid during the text phase; a later visual pass can convert them into generated illustrations, as in the sibling books.
