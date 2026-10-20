---
status: accepted
revised: 2026-10-20
---

# Spec: One Door for Every Model: The Model Gateway and AI Guard

## Intent

Explain why Uber routes every model request through one internal gateway, and make the reader see the gateway as a policy decision rather than an API adapter. The chapter traces the lineage from the 2023 Michelangelo-based GenAI Gateway to the 2026 Model Gateway, explains AI Guard as an inline security baseline, and shows how per-project identity from Michelangelo made attribution, budgets and security review possible. It ends with a sized, buy-first path for companies that are not Uber.

## Audience

Platform, ML-platform and security leads, staff engineers and CTOs who are deciding whether to mandate a model gateway, what should run inline on it, and whether to build or buy it.

## Success criteria

- [x] Reader can name the four names under which the gateway appears in Uber's record and date each source.
- [x] Reader can explain the 2024 documented design (OpenAI-compatible Go service, PII redaction and un-redaction, security review per use case) and what the 2026 sources add (Anthropic compatibility, SPIRE identity, five guard models, under 100 ms, 100M+ requests a day).
- [x] Reader can explain AI Guard's role and why an inline guard is a baseline nobody can forget, and can tell the podcast-only details ("fine-tuned", security-team ownership) from the documented ones.
- [x] Reader can name the Michelangelo assets the gateway reuses (project registry, serving, governance channel).
- [x] Reader can weigh the single-point-of-failure, latency-stacking and lowest-common-denominator trade-offs.
- [x] Reader can pick a minimum viable version for ≈50, ≈500 and ≈5,000 engineers, buying first.
- [x] At least two mermaid diagrams, one trade-off table, failure modes, record gaps and questions to ask.

## Non-goals

- Spend tiers, manager approval and CostCheck — owned by [[token-spend-governance]].
- The harness wrapper and personas — owned by [[aifx-harness-layer]].
- Tool access and MCP — owned by [[mcp-gateway]].
- Michelangelo's pre-AI history in depth — summarized only; the build-in-house pattern lives in [[build-what-does-not-exist]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- AI Guard's fail-open or fail-closed policy, and whether the RSAC 2026 session text can be fetched to confirm its topics.
- Whether model routing is in production as of October 2026.
- Whether the 2024 "16M queries a month" and 2026 "100M+ requests a day" count the same thing.

## Decision log

- **2026-10-20** — Treated GenAI Gateway, Michelangelo Gateway, AI Gateway and Model Gateway as one lineage, with a table of names and dates, instead of choosing one name silently.
- **2026-10-20** — Made the Michelangelo project registry, not the API shape, the "foundation underneath", because attribution and review depend on it.
- **2026-10-20** — Presented the RSAC AI Guard session as agenda only, because the page could not be fetched in full; labeled the guard-parallelism reading as inference.
- **2026-10-20** — Recommended buying (LiteLLM, Kong, Cloudflare) for most readers; building is justified only on top of an existing ML platform.

## Sources

- **Internal**
  - [[build-what-does-not-exist]] — Michelangelo and the build-in-house pattern.
  - [[token-spend-governance]], [[aifx-harness-layer]], [[mcp-gateway]] — neighbours that build on the gateway.
- **External**
  - The October 2026 Pragmatic Engineer episode and show notes — Uber's own account.
  - Uber Blog: GenAI Gateway (2024), Genie (2024), Michelangelo (2017, 2024), agent identity (2026); Michelangelo open-source launch (2026).
  - AI Engineer World's Fair 2026 talk (Medisetty and Huda) and Port's summary.
  - Thoughtworks Radar (LiteLLM), LiteLLM, Cloudflare and Kong documentation.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: corrected the transcript-date note (Medisetty, not the host, corrected 2013 to 2023), qualified the SPIFFE/SPIRE row and the open-source remark, Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 3 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
