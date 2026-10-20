---
status: accepted
revised: 2026-10-20
---

# Spec: Sunday Evening Peaks: Reliability, Performance and Cost

## Intent

Show that reliability in a listing marketplace is a question of predictable peaks, shared capacity and deliberate sacrifice, not of exotic failures. Using the canonical Sunday-evening brown-out at Tradeyard NL, the chapter should leave the reader able to define journey-level SLOs for the journeys that create liquidity, plan capacity for evening and campaign peaks, design degradation ladders, choose a regional ambition, manage automated traffic and compute unit costs (per thousand searches, per live listing, per contact). It closes Part VII and hands off to the leadership part.

## Audience

Chief architects, platform and SRE leads, search platform leads and engineering directors of multi-brand marketplace groups. They know SLOs, caching and Kubernetes; they need the marketplace-specific translation: which journeys, which peaks, what to give up first, and how cost relates to liquidity.

## Success criteria

- [x] Reader can list the liquidity journeys and define a good event, measurement point and objective for each, including "listing gone" and deliberate safety holds.
- [x] Reader can explain error budgets with a peak-window refinement and a policy that changes behavior.
- [x] Reader can run the capacity model (peak × campaign factor × failure headroom × share not cached or shed) on Veldmark numbers.
- [x] Reader can design a degradation ladder whose order is bots, optional features, freshness, then search itself, and explain why safety scanning is never degraded.
- [x] Reader can compare regional options and justify multi-zone plus read-only standby for a country-scoped group, citing Vinted (2026) and the AWS October 2025 event.
- [x] Reader can describe bot and scraper controls from policy to legal, citing RFC 9309 and crawler verification.
- [x] Reader can compute and interpret cost per thousand queries and per live listing per brand, and name the platform-level FinOps levers documented by Adevinta.
- [x] Ledger brown-out facts are used exactly; the Sunday peak is labeled a Veldmark illustration with Rightmove's documented peak as the public example.

## Non-goals

- Index design, aliases and reindex mechanics ([[search-architecture]]).
- Event backbone and outbox ([[event-driven-listings]]); tenancy model ([[multi-country-platforms]]).
- AI crawler licensing and agent access ([[ai-in-listing-systems]]); crawl budget and SEO status codes ([[web-and-seo-architecture]]).
- Fraud detection and scam patterns ([[fraud-prevention]]); messaging safety ([[messaging-and-leads]]).
- Organizational design of on-call and platform teams ([[organizing-marketplace-engineering]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No classifieds operator published journey SLOs or degradation ladders; both are labeled recommendations. Replace with documented examples if they appear.
- OLX's 2021 load-shedding post could not be retrieved; only its existence is cited.
- Cost per contact is described but not computed for Veldmark; a later chapter or the toolkit may define it precisely.

## Decision log

- **2026-10-19** — Organized reliability around liquidity journeys rather than components, so that the chapter connects to the book's central idea.
- **2026-10-19** — Placed degradation as a product decision made in advance, with a fixed order of sacrifice, rather than an operational runbook topic.
- **2026-10-19** — Recommended multi-zone plus read-only standby over active-active for country-scoped groups; active-active needs a business case.
- **2026-10-19** — Added Veldmark unit-cost baseline (search cost per brand, platform run cost) as canonical ledger facts so later chapters can reuse them.

## Sources

- **Internal**
  - [[search-architecture]], [[web-and-seo-architecture]], [[saved-searches-and-alerts]], [[messaging-and-leads]], [[multi-country-platforms]], [[platform-consolidation]].
  - `_research/brief-platform-data-ml.md` (Parts 4–6) and `_research/brief-search-discovery.md` (Part 2) — evidence and labeled inferences.
- **External**
  - Google SRE Workbook (2018) and SRE book (2016) chapters on SLOs and cascading failures.
  - Vinted Engineering (2021, 2023, 2026); Adevinta Tech Blog (2023, 2024); Rightmove press release (2021); AWS post-event summary (2025); Imperva (2025); Cloudflare (2025); RFC 9309; Google crawler verification; FinOps Foundation; Directive 96/9/EC.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: hand-off now goes to [[part-8]] (plus [[platform-consolidation]]), [[part-7]] linked, Cloudflare AI-crawler claim and unretrieved OLX post hedged, American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 5 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Retitled "Sunday Evening Peaks" to match the ledger's Sunday-evening peak; permalink unchanged. *(AI-mediated session)*
