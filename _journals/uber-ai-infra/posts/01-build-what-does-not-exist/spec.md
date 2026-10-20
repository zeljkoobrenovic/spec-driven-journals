---
status: accepted
revised: 2026-10-20
---

# Spec: Build What the Market Cannot Yet Sell: Uber's Pre-AI Platform Bets

## Intent

Open Part I by explaining why Uber built so much of its own infrastructure between 2014 and 2020, and what those systems left behind for the AI era. The chapter must show that the AI layer's real inheritance is not the systems themselves but the **metadata** they hold (ownership, metrics, configuration and experiment history, design docs, incidents) in schemas Uber controls, and that the **city** is a domain primitive running through every layer. Once they have read it, a reader can name their own domain primitive and check whether their company records the facts an agent will need.

## Audience

Engineering leaders, platform and DevEx leads, staff+ engineers and CTOs deciding what to build, buy or retire before investing in AI developer infrastructure. They know what metrics systems, feature flags and workflow engines are; they do not know Uber's history or system names.

## Success criteria

- [x] Reader can explain the three conditions (pace of architectural change, city-shaped business, a platform organization from 2014) that made Uber build in-house.
- [x] Reader can describe uOwn, M3, Cadence, Morpheus/Flipr/XP, Michelangelo and design-doc/incident tooling with evidence labels and dates, and what record each holds for agents.
- [x] Reader can explain the city as a first-class primitive across metrics, configuration, sharding, region pinning and deployment groups, with the NSDI '26 evidence.
- [x] Reader can describe the build → open-source → buy lifecycle with dated examples, and how the AI era inverts it (buy models and harnesses, build the gateways).
- [x] Reader can map pre-AI systems to the AI-era consumers of their metadata (context graph, Shepherd/Fox, Wisdom, Model Gateway).
- [x] Reader leaves with size-specific guidance (≈50/≈500/≈5,000 engineers) and three things not to copy.
- [x] All podcast-only claims (uOwn, sharding by city, logical deployment groups, switchbacks) are attributed; inferences are labeled.

## Non-goals

- Monorepos, Bazel, SubmitQueue and DOMA ([[monorepos-and-one-build]]).
- DevPods ([[devpods]]).
- IDL registry, Jaeger and baggage, the Edge Gateway, standardized language frameworks ([[contracts-and-context-propagation]]).
- Michelangelo's role in the Model Gateway and AI Guard ([[model-gateway]]).
- The context graph's design ([[context-graph]]) and Capri's mechanism ([[capri]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- How is uOwn populated and kept accurate? No public source; worth revisiting if Uber publishes one.
- Which pre-AI systems feed the context graph directly (the Aug 2026 blog says "30+ systems" without naming them)?
- Does any AI-era agent run on Cadence?

## Decision log

- **2026-10-20** — Framed the chapter around "metadata is the legacy" rather than a tour of systems, because a system tour would duplicate the timeline and the system catalog and give non-Uber readers little to act on.
- **2026-10-20** — Kept Jaeger to one row of the lifecycle table; its mechanism and baggage belong to [[contracts-and-context-propagation]].
- **2026-10-20** — Added H3 (2018) as documented evidence of the city primitive, since the podcast's sharding and deployment-group claims are podcast-only.
- **2026-10-20** — Cited the Aug 2026 blog's context-graph counts (86/117) alongside the podcast's (100+/130+), per the ledger's reconciliation rule.

## Sources

- **Internal**
  - [[the-harness-is-the-easy-part]] — the thesis this chapter makes concrete for Part I.
  - [[context-graph]], [[shepherd-and-fox]], [[wisdom-and-debug-assist]], [[model-gateway]] — consumers of the metadata.
  - `_research/brief-pre-ai-foundations.md`, `_research/fact-ledger.md`.
- **External**
  - Pragmatic Engineer, *Uber's AI infra, from the inside* (Oct 2026) — Medisetty's account.
  - Uber Blog: M3 (2018), Cadence 1.0 (2023), Flipr (2021), XP (2022), Michelangelo (2017, 2024), H3 (2018), Piranha (2020), Edge Gateway (2020), Software Factory (Aug 2026).
  - Bansal et al., *Uber's Failover Architecture*, NSDI '26 — city-to-region pinning.
  - Orosz, *The Platform and Program Split at Uber* (2021); Spotify, *Five Years of Backstage* (2025); DORA platform-engineering capability.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: replaced an over-long, bracket-reconstructed build/buy quote with a paraphrase plus short accurate quotes; aligned Cadence's open-source date (2017) with the timeline. *(AI-mediated session)*
- **2026-10-20** — Added 3 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
