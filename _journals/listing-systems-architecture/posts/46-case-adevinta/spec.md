---
status: accepted
revised: 2026-10-19
---

# Spec: Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform

## Intent

Use Adevinta's public record, from the 2019 demerger out of Schibsted to the 2025–2026 decentralization and break-up, as a tested case of the centralization pendulum in a multi-country marketplace group. The page must show, layer by layer, what Adevinta shared, when, and what the sharing cost when its capital strategy changed. It must keep documented fact, the author's interpretation and labeled reference-architecture inference visibly apart, and end by testing the book's patterns and Veldmark's Common Ground choices against the case. After reading, a Chief Architect should have three decision rules: share by layer using the 2019 "large investment, uniform technology" test; treat product-platform convergence as a separate investment case; and make separability a design requirement whenever ownership can change.

## Audience

Chief and enterprise architects of marketplace groups, platform-engineering leads and engineering directors deciding what to share across marketplaces after acquisitions, or preparing for a possible divestment. They know platforms and Kubernetes; they need the evidence trail and the judgement, not tutorials.

## Success criteria

- [ ] A dated timeline section replaces the Veldmark scene, and every company fact carries a source and publication year.
- [ ] Each phase states what was shared and at which layer, with quotes from the 2019 and 2023 annual reports and the 2025 strategic report.
- [ ] Inferences about Adevinta internals appear only in callouts labeled `INFERENCE, NOT DOCUMENTED`; no invented service names, volumes or architectures.
- [ ] An explicit "Where the Public Evidence Stops" section lists the unanswered questions, including the fate of the leboncoin–Kleinanzeigen convergence and of SCHIP.
- [ ] A trade-off table compares sharing infrastructure, narrow services, product components, whole product platforms and decentralization.
- [ ] A vertical-differences table covers generalist, automotive and real estate.
- [ ] At least two mermaid diagrams; the final section compares the case to the book's patterns and to Veldmark's 2027 decisions, with ledger-consistent facts and links to the owning chapters.
- [ ] Questions to ask (6–10) and grouped Sources and Evidence.

## Non-goals

- Not a company profile or an investment view; no judgement on whether the owners' decisions were right.
- Does not re-teach tenancy models ([[multi-country-platforms]]), consolidation sequencing ([[platform-consolidation]]), team topologies ([[organizing-marketplace-engineering]]) or payments design ([[transactions-and-payments]]).
- Does not cover eBay Classifieds Group before 2021 ([[case-ebay-classifieds]]) or OLX ([[case-olx]]).
- Does not describe leboncoin's, Kleinanzeigen's or mobile.de's search and ranking engines, for which no public evidence was found.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Did the "unified global platform" for leboncoin and Kleinanzeigen ship in any form? Revisit if Adevinta or either marketplace publishes on it.
- Outcome of the reported mobile.de IPO-or-sale process and the willhaben sale completion date (both volatile as of October 2026; the web-search quota ran out before they could be rechecked).
- Whether the €130–165 million eCG synergy target was reported as achieved.
- Primary documentation of the Schibsted-era "Blocket platform" model.

## Decision log

- **2026-10-19** — Organized the case as five dated phases plus a cross-phase layer map, rather than by capability, because the case's teaching value is the movement of the shared/local line over time.
- **2026-10-19** — Treated the 2023 convergence as unverified in outcome: quoted the decision and the May 2024 progress line, and refused to infer its architecture. Rejected presenting it as a failure, which the record does not show.
- **2026-10-19** — Framed the reversal as capital strategy changing platform economics, labeled as the author's reading; rejected a "centralization was wrong" conclusion.
- **2026-10-19** — Used the Veldmark comparison to raise separability (Veldmark is also private-equity owned), with a hypothetical Hearthly sale built only from ledger facts; no new canonical facts added to the ledger.

## Sources

- **Internal**
  - [[multi-country-platforms]], [[platform-consolidation]], [[organizing-marketplace-engineering]], [[data-platform]], [[experimentation]], [[ml-platform]], [[transactions-and-payments]], [[long-term-evolution]] — patterns the case tests.
  - [[meet-veldmark]] and the scenario ledger — Common Ground decisions used in the comparison.
  - `_research/brief-adevinta.md`, `brief-platform-data-ml.md`, `brief-monetization-economics.md` — evidence base (no eBay Classifieds brief existed when this page was written).
- **External**
  - Adevinta Annual Reports 2019 and 2023; Aurelia UK Feederco Ltd Strategic Reports 2024 and 2025 — strategy, segment revenue, convergence and decentralization quotes (re-verified 19 October 2026).
  - Adevinta press releases 2021–2025 — acquisition, synergies, divestments, Q1 2024 convergence statement (re-verified).
  - Adevinta Tech Blog 2022–2026 and Galo Navarro's 2020 write-ups — platform, data, ML, experimentation and dispute-component evidence.
  - Kleinanzeigen and AVROTROS Radar pages — buyer-protection flows.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 10 load-bearing claims; dated the Kleinanzeigen provider history (OPP 2020–2023, Adyen per 2026 help page) and Marktplaats OPP (2022); aligned the Hearthly-sale worked question with the long-term-evolution stressor and tenancy model; expanded OCR/EU5; American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
