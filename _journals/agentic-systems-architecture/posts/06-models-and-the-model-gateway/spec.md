---
status: accepted
revised: 2026-10-28
---

# Spec: Models and the Model Gateway

## Intent

Give the reader a way to decide which model each step of an agent should use and how the system should reach it. The chapter replaces "pick a model for the agent" with **model roles** (planner, worker, classifier, reader, judge, embedder) that set each call's requirements, separates the **model tier** (a catalog label) from the **route** (provider account, exact model, API version, region, endpoint kind, data terms) that a step actually runs on, and defines the **model gateway** as the policy enforcement point for model calls: the only path to any provider, holding credentials, quotas, data-handling eligibility and version pins, and recording the model that served. It makes provider differences, above all data-handling terms, explicit route attributes rather than something an abstraction hides. After reading, an architect can specify a gateway's responsibilities and refusals, a route catalog with data classes, and a failover policy, and defend the multi-provider and self-hosting choices.

## Audience

Architects, platform leads and security or privacy architects who must put several model providers (and perhaps a self-hosted model) behind a shared agent platform, and who will be asked by a risk owner "which provider saw this data, under which terms?" They know API gateways, secrets management and cloud contracts; they need the agent-specific responsibilities and failure modes.

## Success criteria

- [x] Reader can name the model roles and state, per role, the requirements that drive model choice (structured output, latency, data access, independence), with evidence for judge independence (MT-Bench self-enhancement, self-preference preprint) and its age.
- [x] Reader can distinguish tier, route and pin, and knows that the gateway must refuse aliases and record the served model (briefly; depth in [[versioning-agent-systems]]).
- [x] Reader can list what the gateway does and what it must never do (no tool authority, no unrecorded model choice, no prompt editing, no semantic "repair"), with a requirements-per-interaction table.
- [x] Reader can explain which provider differences must stay visible (data terms, schema dialect, refusal and truncation, sampling controls, caching, rate-limit accounting, lifecycle, client–model coupling), each dated and sourced.
- [x] Reader can design data classes and route eligibility, including the hold-when-no-eligible-route rule, with a dated snapshot of three providers' training, retention, ZDR and residency terms and the 2025 preservation-order case.
- [x] Reader can weigh single-provider, multi-provider and self-hosted options, including the evaluation cost of each fallback route.
- [x] Ostrell example: the Quiet Failover (February 2027) and the 19 October 2027 outage handled by the route catalog, with numbers consistent with the ledger and labeled assumptions.
- [x] No model version is named as a recommendation; all prices and terms are dated and marked volatile.

## Non-goals

- Per-step routers, cascades, budgets and cost attribution — [[agent-cost-and-model-routing]].
- Rate-limit ceilings, quota pools and priority admission in depth — [[agent-latency-and-throughput]].
- Prompt caching mechanics and prefix layout — [[caching-and-context-budgets]].
- The agent version manifest, alias drift and migration calendar — [[versioning-agent-systems]].
- Retry ownership across layers — [[retries-idempotency-and-concurrency]]; span design — [[agent-observability]].
- Tool authority and the policy engine in depth — [[tool-contracts]], [[policy-enforcement-and-audit]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published evaluation measures whether a model gateway reduces incidents, data-handling violations or cost; the chapter's case is structural. Replace with documented experience if one appears.
- No public postmortem of a failover-caused data-handling violation was found; the Quiet Failover is fiction built from documented terms.
- Provider data terms (Anthropic Covered Models, OpenAI residency uplift, Google paid/unpaid terms) were read on 2026-10-28 and will change; re-check before publication updates.
- The Epoch AI open-model lag estimate is from November 2024; a newer estimate should replace it.

## Decision log

- **2026-10-28** — Made the **route**, not the tier or the provider, the unit that carries data terms and is pinned and evaluated, because the verified terms attach to account, feature and model (batch and certain models differ from the provider default).
- **2026-10-28** — Separated the API edge from the model gateway and kept prompts out of the gateway, departing from the agentic-platform-foundations naming and the public-benefits design's "prompt templates" in the gateway (consistent with configuration as code in [[versioning-agent-systems]]).
- **2026-10-28** — Adopted "hold when no eligible route" over "fail over to any healthy route", and declared fallbacks per role in the manifest, so Answerdesk's failover to provider B stays consistent with the ceiling and evaluation rule in [[agent-latency-and-throughput]].
- **2026-10-28** — Used the OpenAI 2025 preservation order (via Simon Willison's quotation of the primary texts) as the documented case for "only data never stored is safe from a later obligation to keep it", labeled as one provider and one case.

## Sources

- **Internal**
  - [[agentic-reference-architecture]], [[agent-runtime]], [[agent-cost-and-model-routing]], [[agent-latency-and-throughput]], [[caching-and-context-budgets]], [[versioning-agent-systems]], [[agent-observability]], [[retries-idempotency-and-concurrency]], [[prompt-injection-defense]].
  - `_research/brief-performance-economics-evolution.md` (§1.3, 1.5, 1.7, 2.1–2.4), `_research/brief-tools-execution.md` (§1.1–1.3), `_research/brief-evaluation-observability.md` (§3.1), `_research/consistency-issues.md` (items 3, 9, 15).
- **Interview designs** (design examples): `agentic-platform-foundations`, `agentic-finance-platform`, `agentic-legal-platform`, `agentic-public-benefits-platform`, `agentic-healthcare-platform` (`technologyChoices`), `ai-coding-cli` (step `inference`, `technologyChoices`).
- **External**: Anthropic API and data retention; OpenAI data controls; Gemini API additional terms; Anthropic and OpenAI structured-output docs; Claude Code LLM gateway docs; Anthropic postmortem (2025); Zheng et al. (2023); Panickssery et al. (2024); Geng et al. (2025); Kwon et al. (2023); Cottier et al., Epoch AI (2024); Simon Willison on the 2025 preservation order.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: turn vs exchange wording (ruling 19); corrected the in-catalog price spread (about 100×, verified against the pricing table) and the OpenAI reusable-prompts notice (dated 3 June 2026, shutdown 30 November 2026, exact quote). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
