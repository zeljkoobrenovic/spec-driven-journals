---
status: accepted
revised: 2026-10-21
---

# Spec: Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics

## Intent

Establish liquidity as the thing a listing marketplace sells and make it measurable. The chapter defines liquidity (the probability of a qualified match within a meaningful time window, per place × category cell), explains cross-side and same-side network effects, asymptotic effects, seeding, winner-take-most dynamics, multi-homing and disintermediation with dated evidence, and builds a liquidity metric tree with counter-metrics. Its distinctive move is to show that liquidity metrics are the source of most non-functional requirements (publication time, alert latency, unpublish propagation, feed reconciliation, peak capacity) and to trace each requirement to the chapter that owns it.

## Audience

Chief architects, data and ML leads, product directors and engineering directors who set targets for a marketplace platform and need to justify them in business terms, or who inherit dashboards built on listing and traffic counts.

## Success criteria

- [x] Defines liquidity, network effect (cross-side, same-side, asymptotic), multi-homing and liquidity metrics precisely; cites Rochet & Tirole, NFX, a16z and Hagiu & Rothman appropriately (paywalled source labeled as summary).
- [x] Shows winner-take-most with dated evidence and names the measurement caveats (Rightmove's two panels), plus documented limits (Autotrader forecourts and stock lever, Hemnet free formats with the cause labeled unknown).
- [x] Documents multi-homing with the Bundeskartellamt 2026 finding and disintermediation as a fraud, observability and monetization problem.
- [x] Presents a liquidity metric tree in a table with definitions and pitfalls, plus counter-metrics (ghost share, duplicate ratio, unsafe contact rate) and a diagram.
- [x] Veldmark worked example: Tradeyard NL vs PT national and cell-level numbers; the Rotterdam bike decomposed at "searchable"; Essen Golf 26-hour ghost; Hearthly 1.7 listings per property; brown-out liquidity cost estimate.
- [x] A metrics-to-requirements table and diagram linking each requirement to its owner chapter.
- [x] Trade-off table, vertical-differences table, failure modes, Chief Architect's view, questions, Sources and Evidence.

## Non-goals

- Marketplace models and endpoints ([[marketplace-taxonomy]]).
- Industry history ([[industry-evolution]]).
- Governed metric implementation and tracking plans ([[data-platform]]); causal measurement and interference ([[experimentation]]).
- Ranking objectives in depth ([[ranking]]); alert fan-out design ([[saved-searches-and-alerts]]); publication pipeline design ([[publication-pipeline]]).
- Monetization KPIs such as ARPA and ARPR ([[monetization-models]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Sunday-evening peak is a Veldmark illustration; the documented public example used is Rightmove's Wednesday 8:48 pm minute (2021).
- The EC Facebook Marketplace decision is cited by subject matter only; the fine and date were not retrieved in this session.
- Andrew Chen's *The Cold Start Problem* would strengthen the seeding section but could not be verified (publisher page blocked, search quota exhausted).

## Decision log

- **2026-10-19** — Defined liquidity as a per-cell probability within a time window, rather than as a ratio of buyers to listings, so the Tradeyard PT example could show the national ratio misleading.
- **2026-10-19** — Organized metrics as a tree with explicit counter-metrics, to tie the chapter to the Ghost Inventory and Seeing Double failure patterns.
- **2026-10-19** — Made "metrics become requirements" a full section with an owner-chapter column, so later chapters can cite their targets back to a liquidity mechanism.
- **2026-10-19** — Estimated the brown-out's liquidity cost (2.3M failed searches, about 40,000 contacts) as a labeled Veldmark estimate rather than adding it to the canonical incident facts.

## Sources

- **Internal**
  - [[marketplace-taxonomy]] — endpoints and success events per model.
  - [[meet-veldmark]], scenario ledger — Tradeyard, Motorvane and Hearthly facts and the recurring examples.
  - Research briefs: monetization-economics, real-estate-portals, automotive, olx, platform-data-ml, search-discovery; productscape digest.
- **External**
  - Rochet & Tirole (2003); NFX Network Effects Bible (2019/2024); a16z 13 metrics (2020); Hagiu & Rothman (2016); Gurley (2012); Parker (2010).
  - Rightmove FY2025, Autotrader FY26, REA FY26, Hemnet (2026), Scout24 FY2025, Zillow 10-K — dominance, limits and consumer subscriptions.
  - OLX Tech (2022, 2026) — contact labels, seller-side checks, causal measurement of packages.
  - Bundeskartellamt (2026) — dealer multi-homing; Meta Newsroom (2016) and EC IP/24/5801 — distribution from an existing network.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: brown-out cost aligned with reliability-and-scale (3.4M failed requests, ~9,800 fewer first contacts); Common Ground timing fixed (three months in April 2027); Hemnet, Rightmove and Facebook claims spot-checked. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,142 → 6,138 words; 1 heading renamed ("Getting Started and Staying Ahead" → "Competing for Liquidity"); winner-take-most paragraphs reordered (mechanism before limits); opening names where the requirements are traced; bike paragraph leads with the six-minute split. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
