# BOOKED — Manuscript Workspace

**BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces**

How architects and engineering leaders design, scale, govern and evolve the systems behind accommodation marketplaces. The book covers both the OTA that sells hotel rooms by rate plan and the hosted-stays marketplace that sells nights in someone's home. It runs from supply connectivity and availability to search, booking, money, trust and the platforms beneath them, and it compares the two marketplace types wherever their architectures differ.

## Layout

- `config.yaml` — reading order, **68 configured pages**, each with a companion `spec.md`. Public permalinks are stable.
  - Preface: 3 pages.
  - Parts I–IX: each opens with an unnumbered part introduction; 47 chapters in folders `01`–`47`.
  - Part X PRACTICE: an introduction and four public case studies, folders `48`–`51`.
  - Reference: domain coverage, toolkit, glossary, bibliography.
- `PLAN.md` — positioning, structure and one contract per chapter. Each contract gives the question, the scope, the Corvane thread, the terms the chapter owns, the Productscape domains it covers, and its research briefs.
- `posts/<folder>/index.md` + `spec.md` — each page and the spec it was written against (spec-driven authoring, see the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — format, voice, evidence discipline (documented fact with date, industry practice, labeled inference, recommendation, illustration), the hotels-vs-homes comparison rule, diagram rules, the sixteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Corvane Group**, the fictional running example (Roomstead, Nookaway, Corvane Connect, Corvane Payments). Pages must agree with it.
  - `RESEARCH-BRIEF.md`, `WRITER-BRIEF.md` and other `*-BRIEF.md` files — instructions given to the AI research, writing, review and illustration sessions.
  - `brief-*.md` — verified research briefs. Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION with publication dates. Topics:
    - Booking.com; Airbnb; Expedia/Vrbo, Agoda and Trip.com
    - supply and connectivity; availability and pricing; search and discovery; booking and reservations
    - payments, finance and tax; trust, safety and regulation
    - platform, data and ML; host, partner, guest and service tooling
  - `productscape-digest.md` — digest of the two Productscape domain models (travel accommodations, hosted stays): the full domain inventory, the overlap matrix and the gaps.
  - `tools/render_check.py` — loads built pages in Playwright and reports mermaid failures and unresolved or cross-journal links.
- `_input/` — private inputs (empty at creation).

## Provenance and neutrality

The book grew out of two generic Productscape marketplace domain models and public research. The models' own notes name Booking.com and Airbnb as inspiration, but the models are not descriptions of either company.

Company-specific statements are cited to public, dated sources. Where companies have not published how their systems work, the book says so and offers clearly labeled reference-architecture inferences instead. Every worked example uses Corvane, a fictional composite.

## Conventions

Same reference format as LISTED (`_journals/listing-systems-architecture`) and RECONCILED (`_journals/finance-systems-architecture`):

- callout blocks: IN THIS CHAPTER / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS / FAILURE PATTERNS;
- a running fictional example;
- tables of contrasts;
- numbered figures;
- `[[permalink]]` cross-links;
- a Sources and Evidence section on every page.

Specific to BOOKED: every chapter in Parts II–VIII has a **"Hotels and Homes: Where the Two Marketplaces Differ"** section.

Diagrams were written as mermaid during the text phase and converted to generated illustrations in the visual pass (21 Oct 2026), as in the sibling books; each page also has two conceptual figures (one for intros and preface pages), an icon and a header image, and the journal has a hero image. Prompts are archived in `_research/diagram-illustrations/figs/`; open figure issues in `_research/figure-issues.md`.
