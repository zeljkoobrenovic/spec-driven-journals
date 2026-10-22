---
status: accepted
revised: 2026-10-22
---

# Spec: Pricing to Turn: Market-Based Pricing, Signals and Repricing

## Intent

Answer the question: **how should the platform help dealers set and change prices against the market?** The chapter treats the asking price as a dossier-owned decision and pricing software as a producer of signals and proposals. It defines price position against a graded valuation reference, the stand-time signal as a comparison with expected days-to-sell rather than a calendar, and the repricing rule as versioned configuration with guardrails, simulation, approval and absolute target prices. It shows the price change as an event that carries author, reason and reference and fans out to portals, the website, price history, the valuation ledger and outcome measurement. It presents velocity pricing as a documented historical practice that its author replaced in 2023 (consistency-issues item 9), and it measures rules against a control group. After reading, an architect can design the pricing loop, its guardrails and its event, and judge a rule by its outcomes.

Productscape bricks covered: `occm` (Occasion Manager Stock and Pricing: signal generator, pricing advisor, stock list UI, stock store price history). The buying-PWA part of `occm` belongs to [[vehicle-acquisition]].

Owns: **price position**, **stand-time signal**, **repricing rule**.

## Audience

Chief architects, principal engineers and product leaders of dealer-software vendors and dealer groups who build or buy pricing tools, run central pricing desks, or must keep price changes consistent across portals and websites.

## Success criteria

- [ ] Reader can define price position with its reference value type, range and confidence, and explain why a position inside the reference range is not a signal.
- [ ] Reader can explain why age-step (velocity) pricing is historical doctrine, cite what replaced it, and contrast it with per-car targets (CarMax 2026, Pollak 2023).
- [ ] Reader can specify a repricing rule (scope, trigger, target, guardrails, mode, version) and explain why targets are absolute prices, not relative cuts.
- [ ] Reader can list the guardrails: VAT-aware floor, ceiling, step and frequency limits, reference-quality gates including valuation segment status, blast-radius stop, state exclusions, simulation.
- [ ] Reader can design the price-change event and its five consumers, with requirements per interaction.
- [ ] Reader can explain the EU prior-price rule (Directive 98/6/EC Art. 6a; PAngV § 11) and why price history is a legal record.
- [ ] Article includes Axleby worked examples with ledger-consistent numbers (Velto Q1 2027 review, the Octavia floor, the Velto pilot with a control group), a requirements table, trade-off tables, an Across Markets table, three mermaid diagrams, failure handling and Questions to ask.
- [ ] Every company and regulatory claim carries a dated source; inferences and Axleby figures are labeled.

## Non-goals

- Valuation methods, confidence, ledger and drift monitoring ([[valuation-engine]]).
- Market stand-time, market days' supply and sale detection as market measures ([[market-data]]).
- Maximum purchase price and appraisal offers ([[vehicle-acquisition]]).
- Stock item, cost layers, clocks and concurrency model ([[inventory-and-vehicle-dossier]]).
- Channel desired-state sync, adapters and withdrawal sagas ([[listing-syndication]]); advert content ([[merchandising]]).
- Days-to-turn and holding-cost economics ([[dealer-and-data-economics]]); margin-scheme invoicing ([[deals-and-sales-documents]]).
- AI-generated pricing agents ([[ai-in-dealer-workflows]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether a portal's automatic "price reduced" badge counts as the dealer's announcement under Article 6a in each market: not verified; flagged for counsel in the text.
- National transposition texts of Article 6a in the Netherlands and Belgium were not fetched; the chapter cites the directive and the German PAngV only.
- No seller-API documentation of a price label was found for Marktplaats or 2dehands; US marketplace deal labels were not verified (web-search quota exhausted).
- Wards (2019) evidence on ProfitTime is seven years old and describes a product, not its current algorithm.

## Decision log

- **2026-10-22** — Framed velocity pricing as historical, per consistency-issues item 9, and used it as the Velto desk's inherited rule so the Axleby story shows its cost rather than asserting it.
- **2026-10-22** — Kept the asking price owned by the dossier and gave pricing only proposals and signals, consistent with [[inventory-and-vehicle-dossier]] and [[dms-integration]].
- **2026-10-22** — Kept automation within the One Dossier plan: 2027 is proposal mode and a pilot with a control group; automatic in-band repricing and the pricing service on the event backbone come in 2028.
- **2026-10-22** — Tied the Velto Thursday run to the Zombie Golf's 2,300 repricing updates to show price changes as syndication load.

## Sources

- **Internal**
  - [[meet-axleby]], [[valuation-engine]], [[inventory-and-vehicle-dossier]], [[listing-syndication]], [[onboarding-and-configuration]], [[dealer-and-data-economics]].
  - `_research/brief-dealer-workflows-economics.md`, `_research/brief-valuation-market-condition.md`, `_research/brief-syndication-leads.md`, `_research/consistency-issues.md` (item 9), `_research/productscape-digest.md` (brick `occm`).
- **External**
  - CarMax 10-K FY2026 (2026); AutoNation 10-K 2025 (2026); Carvana 10-K 2025 (2026); Cox Automotive used retail sales December 2025 (2026); Auto Trader FY26 results (2026) and help center articles (2023–2026); mobile.de Seller API (n.d., accessed 2026-10).
  - Directive (EU) 2019/2161 inserting Art. 6a into Directive 98/6/EC; PAngV § 11; CMA207 (2025); 16 CFR 233.1; Directive 2006/112/EC.
  - Canadian Auto Dealer (2023) and Wards (2019) on Pollak's velocity and potential-based pricing.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: American spelling fix; consistency and evidence checks, no substantive change. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
