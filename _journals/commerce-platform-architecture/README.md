# ORDERED — Manuscript Workspace

**ORDERED: Architecting Commerce Platforms**

How commerce systems fit together, why the architectural decisions behind them matter, and how those decisions evolve as a business grows. Written for readers new to commerce architecture, platform-neutral, following one order from discovery to delivery and back through a fictional omnichannel brand.

## Layout

- `config.yaml` — reading order, **67 configured pages**, each with a companion `spec.md`. Public permalinks are stable.
  - Preface: 3 pages.
  - Parts I–X: each opens with an unnumbered part introduction; 45 chapters in folders `01`–`45`.
  - Part XI PRACTICE: an introduction and four public case studies, folders `46`–`49`.
  - Reference: domain coverage, toolkit, glossary, bibliography.
- `PLAN.md` — positioning, structure, the teaching discipline and one contract per chapter.
- `posts/<folder>/index.md` + `spec.md` — each page and the spec it was written against (spec-driven authoring, see the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — audience and voice (newcomers), format, evidence discipline, the three take-away tiers, the "Across Scale Stages" rule, diagram rules, the sixteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Kestrel & Pine**, the fictional running example. Pages must agree with it.
  - `RESEARCH-BRIEF.md`, `WRITER-BRIEF.md`, `REVIEWER-BRIEF.md` and other `*-BRIEF.md` files — instructions given to the AI research, writing, review and illustration sessions.
  - `brief-*.md` — verified research briefs. Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION with publication dates.
  - `productscape-digest.md` — digest of the Productscape domain models used as research maps.
  - `consistency-issues.md` — numbered cross-chapter rulings.
  - `tools/render_check.py` — loads built pages in Playwright and reports mermaid failures and unresolved or cross-journal links.
  - `bib-tools/`, `glossary-tools/` — generators for the bibliography and the glossary.
- `_input/` — private inputs (empty at creation).

## Provenance and neutrality

The book generalizes the public, commerce-architecture parts of the author's private journal *FEDERATED* into a platform-neutral treatment. Company-specific statements are documented facts with a source and a publication date; everything else is labeled as industry practice, inference, recommendation, illustration or assumption. Kestrel & Pine is fictional and is not a disguised version of any real company.
