---
status: accepted
revised: 2026-10-20
---

# Spec: AVIV Group: Building a European Real-Estate Platform from Acquisitions

## Intent

Use AVIV Group's public record, from Axel Springer's property-portal acquisitions (2010–2019) to the 2025 carve-out under KKR and CPP Investments and the move to local autonomy, as a tested case of how much of a real-estate portal can be shared across countries. Because AVIV publishes almost no engineering material, the page must be explicit about the limits of the evidence: dated corporate, regulatory and trade-press facts; the author's reading, marked as such; and labeled reference-architecture inferences that never describe AVIV's systems. After reading, a Chief Architect should hold three ideas: AVIV is a portfolio whose record is corporate, not technical; its documented integration moves were commercial and data-driven (valuation, a bundled professional offer, seller-lead routing), not a shared listing platform; and the 2021 integration intent gave way in 2025 to local autonomy with group functions, a "shared core, local edge" shape whose contents are not public.

## Audience

Chief and enterprise architects of marketplace groups with property portals in several countries, and engineering leaders weighing a group platform after acquisitions. They know platforms; they need the evidence trail, the boundary argument and the decision questions.

## Success criteria

- [ ] A dated timeline replaces the Veldmark scene; every company fact carries a source and publication year; the 2015 (not 2023) Immowelt–Immonet combination is stated and corrected once.
- [ ] Inferences about AVIV appear only in callouts or figure captions labeled as inference or reference architecture; no invented service names, volumes or architectures; weak signals (job ads, CVs, aggregators) are named and not used as fact.
- [ ] The 2021 intent and the 2025 reversal are quoted exactly, with the source of the phrase "fully integrated platform" (the interviewer) made clear.
- [ ] The seller funnel (Meilleurs Agents, Ultimmo, private-seller opening, commission share) is documented and drawn.
- [ ] An explicit "Where the Public Evidence Stops" section lists the unanswered questions.
- [ ] A trade-off table and a vertical-differences table; at least two mermaid diagrams.
- [ ] The final section compares the case to the book's patterns and to Veldmark's 2027 decisions with ledger-consistent facts and links to the owning chapters.
- [ ] Questions to ask (6–10) and grouped Sources and Evidence.

## Non-goals

- Not a company profile, valuation or investment view; no judgement on the owners' decisions.
- Does not re-teach tenancy models ([[multi-country-platforms]]), consolidation sequencing ([[platform-consolidation]]), vertical physics ([[vertical-requirements]]), ingestion contracts ([[listing-ingestion]]), duplicate handling ([[entity-resolution]]) or AVM governance ([[ml-platform]]).
- Does not cover Zillow, Rightmove, Idealista or REA ([[case-property-portals]]) or Adevinta's real-estate assets ([[case-adevinta]]).
- Does not describe AVIV's stacks, search, ingestion or valuation models, for which no first-party evidence exists.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What the 2021 "European real estate marketplace" and the abandoned "fully integrated platform" contained, how far it got, and which group functions remain.
- Closing of the Yad2 sale to Apax (signed December 2025; no closing found as of October 2026).
- Current status of immonet as a separate brand, and of Housell, Homeday and the Zumper stake.
- AVIV's founding year as a named entity (2018 per company profiles, seen only as search snippets).
- Whether AVIV uses OpenImmo, or any common format, for French or Belgian ingestion.

## Decision log

- **2026-10-19** — Organized the case as four dated phases (assembly, seller funnel, integration intent, separation), because the evidence documents strategy direction, not systems.
- **2026-10-19** — Used the regulators' decisions (Bundeskartellamt 2015, Autorité de la concurrence 2018) as the main public description of market structure; they are primary sources where AVIV is silent.
- **2026-10-19** — Quoted the 2021 CEO line in full ("…to create a European real estate marketplace") and avoided the word "unified", which no AVIV source uses; attributed "fully integrated platform" to the interviewer.
- **2026-10-19** — Veldmark comparison built on ledger facts only (Supply Contract v1, Valuo commission-share pilot, Keybridge neutrality, Hearthly duplicates); no new canonical facts added to the ledger.

## Sources

- **Internal**
  - [[vertical-requirements]], [[multi-country-platforms]], [[platform-consolidation]], [[listing-ingestion]], [[ml-platform]], [[monetization-models]], [[liquidity-and-network-effects]], [[case-adevinta]], [[case-property-portals]] — patterns and neighbouring cases.
  - [[meet-veldmark]] and the scenario ledger — Hearthly, Valuo, Keybridge and Common Ground facts.
  - `_research/brief-real-estate-portals.md` Part A (and C.4, C.7, Part D) — evidence base.
- **External** (re-verified 19 October 2026 unless noted)
  - Immowelt press release (2015); Bundeskartellamt (2015); Autorité de la concurrence (2018).
  - Axel Springer/KKR/CPP Investments signing release (2024); KKR effective-structure release (2025).
  - Online Marketplaces articles 2021–2025 (McLean, AVIV France hiring, H1 2023, AVIV Germany, Realo, CEO change, Yad2, Mseka interview).
  - MySweetImmo (2022 Ultimmo; 2022 and 2023 Le Tendre interviews); FrenchWeb (2008, 2012, 2019); Tradingsat (2010).
  - OpenImmo e.V. (accessed 2026); AVIV GitHub and Medium feed (accessed 2026, empty).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 12 load-bearing claims; corrected the Bundeskartellamt quote and the 2023 "write the future" quote, added the KKR-control caveat on the Yad2 sale, expanded DPE/DVF, timetoread updated. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,480 → 5,434 prose words; outline unchanged (house case-study shape); opening now names the Hearthly comparison it feeds; point-first openers in the Meilleurs Agents, two-portals, Germany/Belgium and vertical-table paragraphs; duplicate 300-hire mention and meta sentences cut. *(AI-mediated session)*
- **2026-10-20** — Trade-offs heading capitalized as in the 45 chapters. *(AI-mediated session)*
- **2026-10-20** — "The final section" now points to the Veldmark comparison near the end, since two sections follow it. *(AI-mediated session)*
