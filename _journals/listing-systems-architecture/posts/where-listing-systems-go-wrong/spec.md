---
status: accepted
revised: 2026-10-20
---

# Spec: Unlisted: Fifteen Ways Listing Systems Go Wrong

## Intent

Give readers a shared vocabulary of fifteen named failure patterns that recur in classifieds and listing marketplaces before they enter Part I, so that every later chapter can point back to them in its FAILURE PATTERNS callout. Each pattern is explained by mechanism (incentives, ownership gaps, missing contracts, the wrong metric), not by blame, priced in liquidity, trust, speed and money, grounded in a documented public example where one exists, and connected to the chapters whose designs prevent or repair it. The page closes by showing how the patterns reinforce each other and with a pattern-to-chapter matrix, so readers look for the upstream cause before funding a downstream fix and can find every chapter that helps with one pattern.

## Audience

Chief and enterprise architects of marketplace groups, principal engineers, search, data and trust-and-safety leads, and product and engineering directors of classifieds, real-estate, automotive and jobs portals. Also usable by general managers and monetization leads as a shared language with architects. Assumes architectural experience; defines marketplace terms (category taxonomy, attribute dictionary, entity resolution, feed contract, entitlement, trust and safety) on first use.

## Success criteria

- [ ] Uses the fifteen pattern names from the style guide exactly, in style-guide order, each as a `###` heading so callout links and anchors match.
- [ ] Opens with IN THIS SECTION and exactly three KEY POINTS; no failure-pattern callout.
- [ ] A summary table of all fifteen patterns and their warning signs precedes the pattern sections.
- [ ] Each pattern has a fictional quote attributed to a role, what it looks like (warning signs), why it happens, what it costs, a Veldmark illustration labeled fictional, a short remedy direction, and "Where this book helps:" with valid cross-links that match the chapters' own FAILURE PATTERNS callouts.
- [ ] Public examples are dated and sourced (Zillow Offers 2021 for The Unwatched Model; leboncoin 2015 and Which? 2024 for Moderation as an Afterthought; UK Finance 2026 for The Scam Inbox; Adevinta 2019–2025 for the portfolio patterns; Mercari 2024, eBay, OLX, Kleinanzeigen and others); where no public failure is documented, the page says so.
- [ ] Veldmark figures match the scenario ledger (bike timeline and digest, 41,000 downstream ghosts a week, 1.7 listings per property, 8 March 2027 truncated feeds, 17 January 2027 brown-out, boost archaeology, 146-model inventory, €212,000 overbilling, qualified-contact replay).
- [ ] Two mermaid diagrams (patterns along the pipeline; reinforcing chains), a diagnostic table of first indicators, and a closing pattern-to-chapter matrix covering all 51 chapters.
- [ ] Hands off to [[meet-veldmark]].

## Non-goals

- Detailed remedies: these belong to the linked chapters (feed contracts in [[listing-ingestion]], paid-organic blending in [[ranking]], the entitlement ledger in [[products-and-entitlements]], model governance in [[ml-platform]]).
- Prevalence statistics for patterns where none is published (for example ghost-listing rates).
- An introduction to Veldmark (owned by [[meet-veldmark]]) or a reading guide (owned by [[introduction]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now. One illustration per pattern, as in the RECONCILED opening guide, is a candidate for a later pass.

## Open questions

- The article runs to about 9,600 words of prose because each of the fifteen patterns carries a public example; a later edit could move some public examples to the linked chapters if length becomes a problem.
- The matrix marks unwritten chapters (industry-evolution, transactions-and-payments, multi-country-platforms, Part VIII and the Part IX cases other than Adevinta) from the plan; revise it when their callouts exist.
- The Platform Mandate illustration presents the shared search platform's geo query compiler as the alternative to a list-only API; it is a framing of the map-search chapter's decision, not a new ledger fact.

## Decision log

- **2026-10-19** — Kept the RECONCILED anatomy (quote, signs, mechanism, cost, illustration, remedy, chapters) but replaced its control/audit cost dimensions with liquidity, trust, speed and cost, because the book's thesis is that architecture should be judged by liquidity.
- **2026-10-19** — Attributed quotes to roles rather than to cast members, so the patterns read as industry behavior rather than as Veldmark history.
- **2026-10-19** — Built the closing matrix with chapters as rows and pattern codes as columns (● main concern from the chapter's callout or the plan, ○ treated in passing), because fifteen patterns by fifty-one chapters reads best down columns.
- **2026-10-19** — Named Vanity Liquidity and the contract failures (Feed Roulette, The Category Straitjacket) as root patterns, to motivate Parts I–III before discovery and AI.

## Sources

- **Internal**
  - `_research/style-guide.md` — pattern names and warning signs.
  - `_research/scenario-ledger.md` — Veldmark facts, including the additions by chapter.
  - FAILURE PATTERNS callouts of the published chapters in `posts/`; `PLAN.md` for chapters not yet written.
  - Research briefs: adevinta, ebay-classifieds, olx, listing-data-ingestion, platform-data-ml, search-discovery, trust-safety-regulation, monetization-economics, real-estate-portals, automotive.
- **External**
  - Zillow Form 8-K and shareholder letter (2021); Adevinta annual reports 2019 and 2023, strategic report 2025, acquisition release 2021, tech blog 2024; Navarro (2020).
  - Mercari Engineering (2024); eBay Taxonomy API, PBSE playbook and promoted-listings post (2020); mobile.de Seller API; Berlin Tech Blog (2019); OLX Tech Blog (2022, 2025, 2026); OLX Group (2026).
  - Omnibus Directive 2019/2161; P2B Regulation page (European Commission); RFC 9457; Google Search Central and Merchant Center; Bundeskartellamt (2026).
  - UK Finance Annual Fraud Report (2026); Which? (2024); Clubic (2015); Online Marketplaces (2021); Rightmove (2026) and Autotrader (2026) results.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: pattern-to-chapter matrix regenerated from every chapter's FAILURE PATTERNS callout (14 rows changed; ● now means named in the callout only), "Where this book helps" lines extended for Ghost Inventory, the portfolio patterns, Vanity Liquidity and The Unwatched Model; timetoread corrected. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 10,466 → 10,499 prose words; opening now ties the page to the introduction's liquidity argument and states that every chapter's callout points back here; "First indicators for each pattern" promoted to its own H2 section; three small cuts. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 2: kept attempt 1: Portfolio arrow runs behind 'The Duplicate Echo' and Moderation arrow runs behind 'Measurement and control' and 'Paid-Rank Drift', so both read as wrong links; Figure 4: kept attempt 4: label 'new facts go into free keys' missing on Category Straitjacket to Attribute Junkyard arrow; Index-as-Database to Ghost Inventory line runs through The Category Straitjacket box. *(AI-mediated session)*
