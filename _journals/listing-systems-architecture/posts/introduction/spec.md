---
status: accepted
revised: 2026-10-20
---

# Spec: Introduction: Architecture for Liquidity

## Intent

Open **LISTED** by telling the reader what the book is for, whom it serves, what it argues and how to find the chapter that answers the decision already on their desk. Frame the problem with a scene a Chief Architect recognizes (a general manager asks why a smaller competitor turns its listings into more contacts, and every team's own report is green), show that it is an architecture question, and state the book's central argument, a listing marketplace is a liquidity machine, in the same words [[long-term-evolution]] uses, without repeating that chapter's part-by-part synthesis. Explain the five kinds of statement and why company-specific claims carry publication dates.

## Audience

Chief and enterprise architects of marketplace groups, principal and staff engineers, search, data and ML leads, platform-engineering leads, product and engineering directors of classifieds, real-estate, automotive, jobs and recommerce marketplaces, and technology leaders integrating acquisitions (the PLAN positioning). Assumes architecture literacy; assumes no marketplace, search, regulatory or vertical vocabulary.

## Success criteria

- [x] Front matter per style guide (date 2026-10-19, permalink `introduction`); opens with IN THIS BOOK, YOU WILL / WHY THE BUSINESS CARES / WHY ARCHITECTS SHOULD CARE and exactly three KEY POINTS, followed by `<br>`.
- [x] Opening scene poses a liquidity question that turns out to be an architecture question; the Chief Architect's group-scale vantage point is stated.
- [x] Central argument stated consistently with [[long-term-evolution]] ("a liquidity machine… judged by how reliably it turns fresh, trustworthy supply into matches with demand"), with one diagram, and the synthesis left to that chapter.
- [x] Five evidence labels in a table (documented fact with publication year, industry practice, reference-architecture inference, recommendation, illustration) and a dated example of why company claims carry dates.
- [x] Sources described: the two Productscape domain models (generic, not company descriptions), the public record of named companies, standards and research; an explicit "no internal material" statement.
- [x] Structure table and one short paragraph per part (I–IX); a "Start With the Decision in Front of You" routing table of 12–15 rows using only valid permalinks.
- [x] Veldmark in one paragraph linking [[meet-veldmark]]; the failure-patterns guide [[where-listing-systems-go-wrong]] introduced; toolkit and glossary pointers; living-journal and AI-mediated authoring note.
- [x] Closes by handing off to [[where-listing-systems-go-wrong]]; 3,000–4,500 words of prose.

## Non-goals

- The fifteen failure patterns themselves ([[where-listing-systems-go-wrong]]).
- Veldmark's full description, cast, systems and worked examples ([[meet-veldmark]]).
- The part-by-part synthesis, the four cross-cutting ideas, stressor analysis and fitness functions ([[long-term-evolution]]).
- Part-level reading guidance ([[part-1]] to [[part-9]] introductions).
- Definitions of marketplace terms in depth (owning chapters and the [[glossary]]); the industry timeline ([[industry-evolution]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The Part VIII and Part IX introductions did not exist when this page was written; their paragraphs here follow PLAN and `config.yaml`. Re-check them against the intros once written.
- Should the page carry a short "words you need now" glossary teaser as RECONCILED's does? Cut for length in the first version; the glossary is linked instead.

## Decision log

- **2026-10-19** — Modeled on RECONCILED's introduction (scene, audience, why it exists, evidence table, structure table, routing table, fictional-company paragraph, living-journal note), with its reconciliation framing replaced by the liquidity-machine argument.
- **2026-10-19** — Stated the argument with a simplified machine diagram only; the part-by-guarantee-by-metric table stays in [[long-term-evolution]] so the synthesis keeps its payoff.
- **2026-10-19** — Used Adevinta's 2023 "unified global platform" and 2025 "decentralised, standalone operating model" statements as the dated example of why company claims carry publication years, because the book already sources both.
- **2026-10-19** — Routing table starts the payments row at [[marketplace-taxonomy]] and the single-platform row at [[vertical-requirements]], and says why, to model the book's business-model-first stance.

## Sources

- **Internal**
  - `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, `_research/productscape-digest.md`.
  - [[long-term-evolution]] (argument wording), [[part-1]]–[[part-7]] introductions, [[meet-veldmark]], [[where-listing-systems-go-wrong]], [[toolkit]].
  - RECONCILED's introduction (`_journals/finance-systems-architecture/posts/introduction/index.md`) as the structural model.
- **External**
  - Adevinta Annual Report 2023 (2024) and Strategic Report 2025 (2026), as cited in the article.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Part VIII paragraph aligned with the written part intro (one owning team per capability; problems of change, not design); argument checked against long-term-evolution; American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Book retitled to *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*; permalinks unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 3,873 → 3,852 words; outline unchanged; six paragraph openers rewritten to state their point (central claim, liquidity lens, gap, statement kinds, routing warning); spec unchanged. *(AI-mediated session)*
