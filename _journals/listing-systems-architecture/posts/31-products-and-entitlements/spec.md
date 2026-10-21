---
status: accepted
revised: 2026-10-21
---

# Spec: Packages, Bumps and Quotas: Products, Pricing and Entitlements

## Intent

Design the commercial core behind a listing marketplace's paid products: product catalog, pricing engine, consumer checkout and professional contracts, entitlement and quota ledger, effect projection onto hot paths, enforcement points, metering, billing and the sold-versus-delivered reconciliation. After reading, the reader should be able to replace scattered package checks (Billing by Guesswork) with four separated concerns joined by events. They should see that an entitlement is an append-only ledger whose effects are projected onto the listing read model. They should also be able to show that every invoice line can be traced to delivery evidence.

## Audience

Principal engineers and architects who own monetization, search or billing integration at a marketplace or a marketplace group. Engineering leaders deciding on build versus buy for billing and entitlements. Readers know event-driven systems and search; they may not know how packages, quotas, feeds and price events interact.

## Success criteria

- [ ] Defines product catalog, pricing engine, entitlement, quota and effect precisely, and states why catalog, price, entitlement and bill stay separate (table of concerns).
- [ ] Specifies the entitlement ledger's entry types with idempotency keys and an entitlement lifecycle diagram.
- [ ] Explains effect projection onto the listing document with concrete `paid.*` fields and the Sunday-peak arithmetic (31,000 queries/s) that rules out live lookups; links to [[ranking]] for how effects are used.
- [ ] Gives an enforcement-point table including fail-open/fail-closed behavior, and a quota-versus-feed policy table.
- [ ] Covers metering, billing, revenue recognition over the display period, credit notes, and the sold-versus-delivered reconciliation with disclosure evidence.
- [ ] Anchors behavior in dated public sources (Rightmove, Autotrader, CarGurus, OLX, Vinted, Adevinta) and billing documentation (Stripe), with the architecture labeled as reference inference.
- [ ] The Veldmark worked example (the Autohaus Ruhrblick overbilling, Tally design, sizing table, price-event and migration plan) agrees with the ledger.
- [ ] Contains trade-off and vertical tables, three mermaid diagrams, an entitlement matrix, a Chief Architect's view, questions and Sources and Evidence.

## Non-goals

- Choosing monetization models and their liquidity costs: [[monetization-models]].
- How paid effects are blended into the result order: [[ranking]].
- The ad stack and sponsored-listing auctions in the ad server: [[advertising-platforms]].
- Payment processing, payouts and buyer protection: [[transactions-and-payments]]; accounting design: RECONCILED's [[designing-financial-ledgers]].
- Feed contracts in general: [[listing-ingestion]]; organization hierarchies: [[sellers-and-accounts]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Keybridge should ever join the shared entitlement ledger, given the neutrality decision; deferred to the 2029 review in the chapter.
- The 400-candidates-per-query figure used for the peak arithmetic is illustrative; [[search-architecture]] or [[ranking]] may fix a canonical value.

## Decision log

- **2026-10-19** — Built the chapter around one dispute (13 cars, €117) that generalizes into a group audit. A concrete billing error makes the "two counters" failure tangible in a way an abstract anti-pattern description does not.
- **2026-10-19** — Chose an append-only ledger with projected effects over a counter service, and showed counters as a trade-off option rather than a strawman.
- **2026-10-19** — Recommended buying invoicing, tax and collection while building catalog, ledger and projector. Stripe's entitlement documentation is used to show both what billing vendors cover (feature switches) and what they do not (quotas, per-listing time-boxed effects, delivery evidence).
- **2026-10-19** — Named the group entitlement service "Tally" and set the migration order Motorvane → Tradeyard → Hearthly, with shadow months, so later chapters can reference it.

## Sources

- **Internal**
  - [[monetization-models]], [[ranking]], [[event-driven-listings]], [[listing-ingestion]], [[meet-veldmark]] and the scenario ledger.
- **External**
  - Rightmove FY2025 RNS (2026), Autotrader FY26 results (2026), CarGurus 10-K FY2025 (2026), Adevinta Annual Report 2023 (2024), Vinted price list (2026), OLX Tech posts (2025, 2026) — product behaviors the core must support.
  - Stripe Entitlements and Idempotent requests documentation (n.d., read 2026-10-19) — the vendor pattern and idempotency principle.
  - Directive (EU) 2019/2161 and Regulation (EU) 2019/1150 — paid-ranking disclosure duties.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: [[toolkit]] link restored for the entitlement matrix, Omnibus and P2B citations verified against the Official Journal and relinked to EUR-Lex. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,231 → 5,243 prose words; outline unchanged; lead now states the chapter's place in Part VI and names [[ranking]] and [[advertising-platforms]] as consumers of its effects; buried points moved to first sentences (effect projection, reconciliation, Ruhrblick replay, real-estate hierarchy); one paragraph split; Figure 3 moved above the property list; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Concepts section now says its subsections cover three of the four concerns and points to the billing interface under Architecture. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 2: kept attempt 2: invented title 'Reference Architecture: Commercial Core Flow'; invented label 'delivery evidence flows back into the ledger'; that arrow points 'Entitlement ledger' → 'Metering and delivery evidence' instead of the reverse; Figure 4: kept attempt 1 (structure correct): words START and END printed beside the dots. *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
