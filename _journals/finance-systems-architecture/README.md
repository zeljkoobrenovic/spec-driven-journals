# RECONCILED — Manuscript Workspace

**RECONCILED: Enterprise Architecture for Financial Systems**

How a Chief Architect designs, integrates, governs and evolves the finance technology of a multinational enterprise — ERP, payments, close, consolidation and the custom platforms between them — as one coherent system.

## Layout

- `config.yaml` — reading order: Preface (3 pages), four parts each with an unnumbered part introduction (44 chapters, including the FinOps chapter `45-finops` added 2026-10-18 and read after ch. 39), Part V PRACTICE with its introduction and one public case study (chapter 44, Uber's payments platform, added 2026-10-18 at the author's request), and Reference (toolkit, glossary, bibliography): **56 configured pages**, each with a companion `spec.md`. Folders are numbered `01`–`45`; `45-finops` sits between 39 and 40 in reading order (config order rules); public permalinks are unprefixed and stable.
- `PLAN.md` — book positioning, structure and one contract per chapter (question, scope, Northmere thread, terms each chapter owns, research briefs).
- `posts/<folder>/index.md` + `spec.md` — each page and the spec it was written against (spec-driven authoring, see the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — format, voice, evidence discipline, diagram rules, the fourteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Northmere Group**, the fictional running example. Chapters must agree with it.
  - `WRITER-BRIEF.md` — the instructions given to AI writing sessions.
  - `brief-*.md` — verified research briefs (SAP, Workday, Oracle, BlackLine and OneStream, payments with Adyen and Stripe, accounting/controls/regulation, EA methods/integration/ledgers, satellite platforms and AI). Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION.
  - `productscape-digest.md` — generalized digest of the Productscape domain model this book started from.
  - `REVIEWER-BRIEF.md`, `review-*.md` — the editorial review pass instructions and per-part review logs.
  - `consistency-issues.md` — cross-chapter consistency decisions (canonical resolutions; editor lines in the scenario ledger win over chapter lines).
  - `bib-tools/` — scripts used to harvest the bibliography from chapters' Sources and Evidence sections; new sources append from the next free R-number, never renumber.
- `_input/` — private inputs (empty at creation).

## Provenance and neutrality

The book grew out of a Productscape model of one multi-brand group's enterprise-application and financial-systems landscape. It is deliberately **not** about that company: the material was generalized into concepts, patterns and practices, and every worked example uses Northmere, a fictional composite. Vendor capabilities are cited to official documentation; architectural recommendations are the author's judgement and are worded as such.

## Conventions

Same reference format as the OWNED book (`_journals/private-techuity`): callout blocks (IN THIS CHAPTER / WHY FINANCE CARES / WHY ARCHITECTS SHOULD CARE / KEY POINTS / FAILURE PATTERNS), a running fictional example, tables of contrasts, figures (generated illustrations; the original mermaid diagrams were replaced on 20 October 2026), `[[permalink]]` cross-links, and a Sources and Evidence section per chapter.
