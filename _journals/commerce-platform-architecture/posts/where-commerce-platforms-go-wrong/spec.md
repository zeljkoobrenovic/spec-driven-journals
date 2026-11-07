---
status: accepted
revised: 2026-11-07
---

# Spec: Out of Stock, Out of Sync: Sixteen Ways Commerce Platforms Go Wrong

## Intent

Give the book its shared vocabulary of failure before any chapter uses it. The page names the sixteen failure patterns the style guide fixes (names, warning signs and families exactly as listed), and for each gives a characteristic quote, what it looks like, why it happens, what it costs, a Kestrel & Pine illustration from the ledger's incidents (or a labeled illustrative scene), one dated public example where a brief supports it, the remedy direction and the chapters that address it. It then shows where each pattern typically appears across the four scale stages, how the patterns chain, and how to use them in design reviews, vendor demos, due diligence and a newcomer's first week, and hands off to the merchant page. After reading, a newcomer can name the pattern behind an incident in one sentence and find the chapter that fixes it.

## Audience

Readers new to commerce architecture, especially those who will sit in design reviews, vendor demos or due diligence within weeks of joining: the engineer, product manager, analyst or leader who needs a name for what is going wrong before they can argue about a fix. Every term is explained where it first appears; the page is also a first tour of the vocabulary (system of record, available-to-promise, idempotency key, reverse fulfillment order, disposition, tenant).

## Success criteria

- [x] The sixteen pattern names, warning signs and families match the style guide table exactly, in the same order.
- [x] Each pattern section has: an italic quote, what it looks like, why it happens, what it costs, a Kestrel & Pine illustration (labeled fictional, or labeled illustrative scene where the ledger has no incident), a dated public example where a brief supports it, a remedy direction, and "Where this book helps" with `[[permalink]]` links.
- [x] Every Kestrel & Pine number matches the ledger (1,340 units, €96,000, 37 items, 600 variants, 11 tickets, 212 returns, €19,400, €179 for nine days, 410 orders, €8,200, €52,000, €14,200, two days, 34 integrations, 13 and 5 without owner, 41 apps, €240,000).
- [x] Every public example carries a publisher and a date and comes from a brief's VERIFIED or WIDELY REPORTED entries; dated sources older than about three years are marked.
- [x] A "Where the Patterns Strike" table (pattern × scale stage), a "How the Patterns Reinforce Each Other" section with one mermaid diagram, a "Using the Patterns" section, a hand-off to [[meet-kestrel-and-pine]], and Sources and Evidence.
- [x] No "Across Scale Stages" section and no take-away tiers (this is a preface page).
- [x] A reader new to the field can define every term the page uses from the page alone.
- [x] Length 7,000–9,000 words.

## Non-goals

- Teaching any remedy in depth; every pattern links to the chapters that own it.
- Introducing Kestrel & Pine as a company (the next page does that); the page uses the incidents only as illustrations.
- A taxonomy of security threats; the Card-Testing Night is a trust failure handled by [[commerce-security]], not one of the sixteen.
- Ranking the patterns by frequency; no survey supports it, and the stage table is labeled as the author's judgement.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Some public examples (Shopify Scripts' end date, the Visa agentic-transactions release, the bol Offers API v10 switch-off) rest on brief entries tagged VERIFIED or WIDELY REPORTED with search-snippet provenance; a reviewer should spot-check the three URLs before print.
- One Size Fits None has no ledger incident; the page uses the three-storefronts-in-one-tenant situation and the deferred 2029 review as a labeled illustrative scene. If [[multi-tenancy-and-isolation]] adds a canonical scene, this page should reuse it.
- The chapter-to-pattern links were drawn from the chapters written so far and the PLAN contracts; when the remaining chapters land, their "Failure patterns this chapter addresses" blocks should be checked against this page's "Where this book helps" lists.

## Decision log

- **2026-11-07** — Organized the page as table, then one section per pattern, then strike table, chains, use and hand-off, following the sibling book's "Fifteen Ways Vehicle Platforms Go Wrong" page, because readers of both books should recognize the shape.
- **2026-11-07** — Used Kestrel & Pine's ten incidents (plus the ledger's chapter additions: the stacking bug, the inventory counts, the declined pitches, the OMS cut-over) rather than inventing new scenes, so that every illustration also appears in a chapter with the same numbers; only One Size Fits None gets a labeled illustrative scene.
- **2026-11-07** — Chose one dated public example per pattern over several, and preferred vendor documentation and regulators' own dates over trade-press incident stories, because the former can be re-verified and the latter age quickly; where the public record is thin (The Familiar Stranger, Schrödinger's Order) the example is a vendor model rather than an incident.
- **2026-11-07** — Drew the chains diagram with twelve of the sixteen patterns rather than all, keeping under the fourteen-node rule and leaving the three governance-only patterns (One Size Fits None, The Long Fuse, The Familiar Stranger) to the prose.

## Sources

- **Internal**
  - `_research/style-guide.md` — the sixteen patterns, warning signs and families; page format; valid permalinks.
  - `_research/scenario-ledger.md` — the ten incidents and the chapter additions used as illustrations.
  - `PLAN.md` — the Preface contract and the chapter contracts that decide "Where this book helps".
  - All research briefs, lightly; chiefly `brief-inventory-fulfillment-returns`, `brief-checkout-payments-tax`, `brief-integration-and-data`, `brief-marketplaces-channels-pos`, `brief-platform-engineering-scale`, `brief-platform-landscape`, `brief-cases-amazon-zalando`, `brief-commerce-business-models`, `brief-security-privacy-regulation`, `brief-b2b-edi-erp`, `brief-catalog-pricing-search`, `brief-ai-agentic-commerce`, `brief-shopify`.
  - The existing chapters' "Failure patterns this chapter addresses" blocks.
- **External**
  - Shopify, commercetools, Stripe, Mollie, Adobe, bol, Amazon and Zalando documentation and announcements — stock states, order statuses, webhooks, refunds, version calendars, lifecycle policies.
  - Zalando Engineering (2023, 2025), Twilio Segment (2018), InfoQ on Prime Video (2023), MACH Alliance (2026) — the giants' own accounts.
  - MPR News (2011) and Retail Dive (2013) — the Target and Finish Line replatforming cases.
  - Directive (EU) 2019/2161, GDPR, Directive (EU) 2019/882, FPS Finance Belgium, German BMF, PCI SSC — the regulatory dates.
  - DeHoratius and Raman (2008); NRF (2025); Gorgias (2023); Sansec (2024); Visa (2026); Google and the ACP repository (2026) — the figures and the agent protocols.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: February 2027 pitches aligned with ruling 13a; trimmed toward 6,500 words. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 1 mermaid diagram as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-11-07** — Added one illustration per failure pattern (16 figures, article-illustrator); existing figures renumbered 17–18. *(AI-mediated session)*
