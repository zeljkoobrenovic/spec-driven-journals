---
status: accepted
revised: 2026-11-07
---

# Spec: Bibliography: Every Source the Book Cites

## Intent

One register of every public source the pages of ORDERED cite, each listed once with its year, evidence type and citing pages, so a reader can trace any claim back to a dated document by topic or by chapter.

## Audience

Readers checking a figure or a rule, reviewers auditing the evidence, and AI tools using the book as context.

## Success criteria

- Every entry comes from a page's **Sources and Evidence** section; nothing is added as further reading.
- Each entry has a stable R-number, linked title, publisher or author, year (or "n.d." with the access month), one clause on what it supports, an evidence type and "Cited in" links.
- Topics follow the book's eleven parts; a **Sources by Chapter** list maps every citing page to its identifiers.
- R-numbers never change: `_research/bib-tools/ids.json` keeps them; new sources append, removed ones are retired.
- The page is generated, never hand-edited: `sh _journals/commerce-platform-architecture/_research/bib-tools/run.sh`; fixes go in `gen.py` or `fix.py`.

## Non-goals

- No reading list, no ranking of sources, no listing of the research briefs, the plan or links to companion books.

## Modalities

Article only.

## Open questions

None.

## Decision log

- Legal texts cited by the Part VIII chapters sit together under Security, privacy and regulation unless another part cites them in more pages.
- Filings and announcements of the case subjects (Shopify, Amazon, Zalando, commercetools, Shopware) go to Company records and case evidence.

## Sources

The **Sources and Evidence** sections of every page in `config.yaml`.

## Changelog

- 2026-11-07: First version; page generated from 818 sources.
