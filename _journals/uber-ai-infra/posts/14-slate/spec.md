---
status: accepted
revised: 2026-10-20
---

# Spec: Slate: Letting Agents Test Their Own Changes End to End

## Intent

Explain how Uber lets coding agents verify a multi-service change end to end without copying the stack: Slate's short-lived, request-isolated environments, the trace-baggage routing that makes them work, and the agent workflow (create, deploy, pin test accounts, A/B main against branch in an agent browser, attach before/after evidence to the PR). Make the book's thesis concrete: the agent layer is small; the propagation and routing estate underneath took years and was built for humans. Translate the pattern for companies without that estate.

## Audience

Platform and developer-experience leads, staff engineers and engineering leaders deciding how background agents should prove their changes work. They know microservices, staging and service meshes; they need the mechanism, its dependencies, its limits and a sized path to a minimum viable version.

## Success criteria

- [x] Reader can explain request isolation (route marked requests to services under test) versus environment cloning, and why Uber chose the former.
- [x] Reader can name the documented mechanism (2022 post): `request-tenancy` baggage, Edge Gateway routing overrides, host-routing-agent, test users, two-day default lifetime, `slate.yaml` isolation, and its stated limits.
- [x] Reader can separate the documented system from the podcast-only agent workflow and the staging-vs-production wording discrepancy.
- [x] Reader understands why main-versus-branch comparison and PR artifacts matter more than the deploy itself, linked to BITS placebo runs.
- [x] Reader gets a sized "If you are not Uber" path (≈50 / ≈500 / ≈5,000) with prerequisites and what not to copy.
- [x] Failure modes include silent fallback to production, propagation gaps, test-data leakage and scenario selection bias.
- [x] Jaeger dates follow the documented record (2015–16, open-sourced 2017), not the episode's "2017–18".

## Non-goals

- The trace-baggage and Edge Gateway history in depth — owned by [[contracts-and-context-propagation]].
- Capture-replay and the combinatorial test set — owned by [[capri]].
- `aifx validate`, visual validation in the inner loop and self-healing CI — owned by [[inner-loop-and-self-healing-ci]].
- How the reviewer consumes the evidence — owned by [[code-review-signals]].
- Minion's architecture and PR share — owned by [[minion]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Does Slate still default to production dependencies (2022) or to staging (Medisetty's wording)?
- How do agents detect silent fallback to production before trusting a "no difference" result?
- What share of Minion PRs carry Slate evidence?
- Has the Jaeger-to-OpenTelemetry baggage migration finished, and are both formats honored?

## Decision log

- **2026-10-20** — Built the chapter on the 2022 SLATE post as the documented core and the episode as the agent layer, rather than leading with the demo, because the mechanism is better evidenced than the agent features.
- **2026-10-20** — Kept Deputy and Cerberus to one short subsection with the guest/host discrepancy stated; there is no public record to expand on.
- **2026-10-20** — Framed self-verification around comparison and artifacts, tying it to BITS placebo runs, instead of treating "the agent deployed it" as the result.
- **2026-10-20** — Chose Lyft staging overrides and Signadot as comparisons (same mechanism, different substrate) over generic preview-environment vendors.

## Sources

- **Internal**
  - [[contracts-and-context-propagation]] — Jaeger baggage, Edge Gateway, mesh routing.
  - [[minion]], [[mcp-gateway]], [[inner-loop-and-self-healing-ci]], [[capri]], [[code-review-signals]] — neighbours this chapter hands off to.
- **External**
  - Srivastava, Srivastava and Rathi, *Simplifying Developer Testing Through SLATE* (Uber, 2022) — the documented mechanism and limits.
  - Uber, *Shifting E2E Testing Left at Uber* (2024) — BITS, OTel baggage, placebo runs.
  - Gud, *Why We Leverage Multi-tenancy in Uber's Microservice Architecture* (Uber, 2020) — the testing-in-production rationale.
  - Orosz and Medisetty, *Uber's AI infra, from the inside* (Pragmatic Engineer, 2026) — the agent workflow.
  - InfoQ on Lyft staging overrides (2022); Signadot docs; Spotify Honk Part 3 (2025).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: stated the staging-vs-production default-dependency discrepancy once and qualified every later mention (trade-off table, Lyft comparison, failure modes, gaps); named the 11% merged-PR source; fixed "two corrections" to one; Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
