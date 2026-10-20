---
status: accepted
revised: 2026-10-20
---

# Spec: Bibliography

## Intent

List every source the chapters cite, once, grouped by the kind of evidence it is, so a reader can check a claim at its origin and see how much of the book rests on Uber's own account versus independent sources. Each entry gives the linked title, author or publisher, year, one line on what the book uses it for, and the chapters that cite it.

## Audience

Readers who want to verify a claim or read further on one system, and reviewers checking that a chapter's sources are dated and correctly labeled.

## Success criteria

- [x] Every link in every chapter's "Sources and Evidence" section appears exactly once, with regional Uber URL variants and duplicate talk pages merged.
- [x] Groups: the source episode; Uber's engineering record (blog, papers, talks and write-ups, open source); The Pragmatic Engineer; press; industry and research; standards and documentation.
- [x] Each entry has title (linked), author or publisher, year, a one-line use, and `[[links]]` to the citing chapters, computed from the chapters rather than typed by hand.
- [x] Uber blog posts in publication order; "current" marks living documentation.
- [x] Covers all 24 chapters, including [[introduction]] and [[the-retrofit-playbook]], which were written in parallel with this page.
- [x] Opens with `IN THIS PAGE, YOU WILL:` and a lead; no KEY POINTS, no BUILT ON.

## Non-goals

- Evaluating sources beyond what the chapters already say about them.
- Further reading the chapters do not cite.
- Listing body-only links exhaustively; the three found are included and marked.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Re-run the generator after review passes that change chapters' source lists.
- Several Uber blog posts give no author on the page as cited (QueryGPT, FixrLeak, Enhanced Agentic RAG, Shifting E2E Testing Left); add authors if a reviewer confirms them.

## Decision log

- **2026-10-20** — Citing chapters are computed by a script that reads every chapter's "Sources and Evidence" section and normalizes URLs (regional `uber.com/xx/yy/blog/` paths, `www.`, trailing slashes); titles, authors, years and notes are curated by hand. The script and its curated entries live in the session scratchpad (`build_bib.py`, `assemble_bib.py`), not in the repository.
- **2026-10-20** — Third-party write-ups of Uber talks (AAIF, Port, the DX recap, a recap of an OpenJDK talk, Sonar/Gitar) are grouped with Uber's talks, because they report what Uber engineers said, but each is labeled as secondary.
- **2026-10-20** — Industry news on other companies (InfoQ on Lyft, Twitter Diffy, Spotify) is under "Industry and research"; "Press" is reserved for reporting about Uber and the workspace vendor market.
- **2026-10-20** — The episode entry says "cited in every chapter" rather than listing two dozen links.

## Sources

- **Internal**
  - Every chapter's "Sources and Evidence" section; [[introduction]] for the evidence labels.
- **External**
  - The sources listed on the page.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Hero image and icon generated. *(AI-mediated session)*
