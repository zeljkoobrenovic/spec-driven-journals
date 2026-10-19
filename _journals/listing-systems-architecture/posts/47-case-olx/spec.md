---
status: accepted
revised: 2026-10-19
---

# Spec: OLX Group: Regional Platforms, Verticalization and Retreat

## Intent

Use OLX Group's public record, from its 2006 founding and the Naspers roll-up through the 2020 regional mergers, the OLX Autos bet and the 2022–2026 retreat to seven markets, as a tested case of portfolio strategy shaping what a listing platform carries. The page must show, phase by phase, which markets and adjacent businesses the platform carried and what the engineering teams published about the stack while the portfolio changed. It must keep documented fact, the author's interpretation and labeled reference-architecture inference visibly apart, and read eight years of engineering posts by era, since many describe markets OLX no longer owns. After reading, a Chief Architect should have three decision rules: let the portfolio decide what a shared platform is worth; build adjacent inventory and payment businesses so that they can be retired cheaply; and evolve search, ranking and multi-brand configuration in place with an explicit proof sequence.

## Audience

Chief and enterprise architects of marketplace groups, search and ranking leads, and engineering directors deciding which markets and adjacent businesses a shared platform should serve, and how to change a live search stack. They know search engines and ML; they need the evidence trail and the judgement.

## Success criteria

- [ ] A dated timeline section replaces the Veldmark scene; every company fact carries a source and publication year, and secondary sources are marked as widely reported.
- [ ] Each of the four phases states what the platform carried, with Prosus/OLX figures re-verified (FY25, FY26, vertical split, OLX Autos, Avito sale).
- [ ] Engineering evidence is presented by era, with the search evolution (sort → formula → LTR in Solr → Vanilla/VAS LTR → hybrid) and the hybrid-search proof sequence documented with quotes.
- [ ] Inferences about OLX internals appear only in callouts labeled `INFERENCE, NOT DOCUMENTED`; no invented service names, volumes or architectures.
- [ ] An explicit "Where the Public Evidence Stops" section lists the unanswered questions, including code sharing across country brands, La Centrale's integration and the event backbone.
- [ ] A trade-off table and a vertical-differences table; at least two mermaid diagrams.
- [ ] The final section compares the case to the book's patterns and to Veldmark's 2027–2028 decisions, with ledger-consistent facts and links to the owning chapters.
- [ ] Questions to ask (6–10) and grouped Sources and Evidence.

## Non-goals

- Not a company profile or an investment view.
- Does not re-teach ranking design ([[ranking]]), hybrid retrieval ([[query-understanding]]), tenancy models ([[multi-country-platforms]]), consolidation sequencing ([[platform-consolidation]]) or transactional design ([[transactions-and-payments]]); it summarizes and links.
- Does not cover Adevinta's side of the OLX Brasil joint venture ([[case-adevinta]]) or automotive groups in general ([[case-automotive]]).
- Does not describe OLX's moderation, media or recommendation systems in depth; a summary table links to the owning chapters.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Which OLX Europe brands share a code base, and when the real-estate "unified platform" rolled out. Revisit if OLX publishes on it.
- Whether La Centrale's "integration ahead of plan" includes moving onto a shared motors platform.
- Completion of the Uzbekistan, Kazakhstan and Fixly sales (only signing dates confirmed in the FY26 release); status of the OLX Brasil joint venture.
- How OLX.pl and Otomoto divide dealers and listings in Poland — the evidence that would test Veldmark's Polish overlap rule.

## Decision log

- **2026-10-19** — Organized the case as four dated phases plus an engineering-record section, because the teaching value lies in the contrast between portfolio upheaval and steady in-place evolution of the listing stack.
- **2026-10-19** — Treated the early history (2006–2018) as widely reported and kept it short; leaned on Prosus filings for economics, flagging the aEBIT-to-aEBITDA metric change rather than comparing margins as like for like.
- **2026-10-19** — Showed the multi-brand shape only as a labeled inference figure built from documented fragments; refused to name which brands share code.
- **2026-10-19** — Used the Veldmark comparison for Safe Deal, Hearthly Direct, Ranking policy v1, the OpenSearch move and the external assistant channel, plus the Polish overlap as a worked question; no new canonical facts added to the ledger.

## Sources

- **Internal**
  - [[liquidity-and-network-effects]], [[ranking]], [[query-understanding]], [[multi-country-platforms]], [[platform-consolidation]], [[transactions-and-payments]], [[experimentation]], [[ai-in-listing-systems]] — patterns the case tests.
  - [[case-adevinta]] — format model and the OLX Brasil joint-venture partner.
  - [[meet-veldmark]] and the scenario ledger — Veldmark decisions used in the comparison.
  - `_research/brief-olx.md` (primary), `brief-search-discovery.md`, `brief-monetization-economics.md`, `brief-automotive.md`, `brief-platform-data-ml.md`.
- **External**
  - OLX Group FY25 and FY26 releases; Prosus FY25 booklet and FY2026 media release — economics and portfolio (re-verified 19 October 2026).
  - Naspers 2022 Avito disposal; OLX Group releases on OfferUp, Grupo ZAP, Uzbekistan, Kazakhstan, Otodim — portfolio moves (partly re-verified).
  - OLX tech blog 2018–2026 — search, ranking, experimentation, multi-brand, trust and safety, media and recommendations (hybrid search, recommendations, group sequential testing and WOF posts re-verified via the RSS feed).
  - News24/Fin24 2023 and TechCrunch 2021, 2023 — OLX Autos.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 9 load-bearing claims (FY26, Avito, OLX Autos, hybrid search, Otodim, OfferUp); noted the implied FY25 aEBITDA margin, the Schibsted-to-Adevinta JV stake and the unnamed Pay&Ship provider. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
