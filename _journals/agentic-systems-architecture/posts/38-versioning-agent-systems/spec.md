---
status: accepted
revised: 2026-10-28
---

# Spec: Versioning Prompts, Models, Tools, Policies and Memory

## Intent

Give the reader one answer to "what is the deployable unit of an agentic system?": an immutable, content-hashed **agent version manifest** that binds the exact model identifier, API version and settings, prompts, tool contracts with description hashes, policy version, retrieval index snapshot and embedding model, memory schema and orchestration build. Show which artifacts change behavior without a deploy (aliases, live tool descriptions, console prompts, provider serving stacks), how the parts stay compatible, how runs in flight and stored memories survive version changes, and what reproducibility can honestly be promised. Use the Alias Drift as the problem and Keelson's September 2027 fixes as the answer.

## Audience

Architects and platform leads who own an agent platform or a production agent and must defend which version produced a given decision, plan model migrations, and stop behavior changing underneath them. They know configuration management and release engineering; they need the agent-specific unit of release and its limits.

## Success criteria

- [ ] Reader can list the artifacts that define an agent's behavior and say which can change without a deploy, and by whom.
- [ ] Reader can define agent version manifest, alias drift and behavior regression, and distinguish authored from ambient change.
- [ ] Reader can write registration checks that reject floating references and unreviewed tool descriptions.
- [ ] Reader can classify a tool-contract change (minor, behavioral, major) and say what each consuming agent must do.
- [ ] Reader can explain, with dated provider evidence, why pinning is necessary but not sufficient, and what the daily canary is for.
- [ ] Reader can choose a migration strategy for memory schemas and keep runs in flight on their starting version.
- [ ] Reader can state which level of reproducibility (re-identify, replay, re-execute) to promise an auditor and why.
- [ ] The Alias Drift numbers match the scenario ledger (96.1% to 89.4%; 4% to 11% rejection over 4 days; no wrong entry posted; alias ban September 2027).

## Non-goals

- The release process (shadow, canary, ramp, rollback, forward fix) — [[staged-rollout-and-rollback]].
- Gate thresholds and promotion criteria — [[evidence-for-autonomy]]; suite and grader versioning — [[building-agent-eval-suites]].
- Gateway design and model selection — [[models-and-the-model-gateway]]; tool design — [[tool-contracts]]; MCP itself — [[tool-ecosystems-and-mcp]].
- Workflow-code versioning in durable engines — [[durable-agent-execution]]; task-state schema — [[task-state-and-checkpoints]]; memory write policies — [[agent-memory]].
- Ownership and the agent lifecycle — [[owning-agentic-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether OpenAI documents alias-versus-snapshot semantics for its current models was not verified; the chapter says so.
- No public postmortem of a customer-side agent incident caused by a provider retirement or alias move was found; the Alias Drift is presented as fiction inferred from documented provider behavior.
- The effect of mixing embedding spaces on agent task success is stated as engineering certainty without a published measurement.
- Whether a given model migration is a "substantial modification" under the EU AI Act is left as a legal judgement.

## Decision log

- **2026-10-28** — Made the exact model identifier part of the manifest, departing from the agentic-platform-foundations design whose `agent_versions` omits it (consistency ruling 9); the coding-CLI design's "every model or harness change" gate is the stance adopted.
- **2026-10-28** — Framed reproducibility as three levels and recommended promising replay, not re-execution, given retirement timelines and documented run-to-run variance.
- **2026-10-28** — Used the October 2027 Answerdesk A1 → A2 promotion as a single-field policy-version diff, to show that autonomy changes are manifest changes, leaving the autonomy review itself to chapter 34.
- **2026-10-28** — Kept the Closewise model migration's rollout for chapter 39; this chapter only puts it on the migration calendar.

## Sources

- **Internal**
  - [[models-and-the-model-gateway]], [[tool-contracts]], [[tool-ecosystems-and-mcp]], [[durable-agent-execution]], [[agent-memory]], [[provenance-and-freshness]], [[policy-enforcement-and-audit]], [[human-oversight-and-bounded-autonomy]], [[evidence-for-autonomy]], [[staged-rollout-and-rollback]].
  - Interview designs (design examples): `agentic-platform-foundations` (step `eval-obs`), `ai-coding-cli` (steps `cloud`, `extensibility`), `ai-coding-harness` (step `scale`), `agentic-finance-platform` (step `decision-record`), `agentic-public-benefits-platform` (steps `naive`, `rules`), `agentic-healthcare-platform` (steps `grounding`, `safety`).
- **External**
  - Anthropic model deprecations and models overview (accessed 2026-10); OpenAI deprecations (accessed 2026-10); Google Gemini models (updated 2026-10-22).
  - Chen, Zaharia and Zou (2023) and Narayanan and Kapoor (2023) on behavior drift; Anthropic's September 2025 postmortem; OpenAI's May 2025 sycophancy postmortem (via Simon Willison).
  - Thinking Machines (2025) and Atil et al. (2024) on nondeterminism.
  - Invariant Labs (2025) on tool poisoning and rug pulls; MCP specification versioning (accessed 2026-10).
  - EU AI Act Annex IV and Article 43; Google SRE Workbook on canarying; Hodgson on feature toggles; Microsoft Durable Functions code constraints; Anthropic on rainbow deployments.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: manifest labels prefixed per ruling 23 (Closewise `cw-2027.09.3`; Answerdesk `ad-2027.09.7` → `ad-2027.10.2`, was `2027.10.1`); eval binding aligned to suite v1 (was v9); added the Alias Drift rejection arithmetic (1,498 proposals, 165 rejected, ~105 extra) that agent-observability points to; OpenAI deprecation quote corrected; Tidemark trust level replaces confidence. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
