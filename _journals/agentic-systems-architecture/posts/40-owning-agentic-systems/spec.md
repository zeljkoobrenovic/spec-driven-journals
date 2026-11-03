---
status: accepted
revised: 2026-10-28
---

# Spec: Ownership, Operations and Evolving the Architecture

## Intent

Close Parts I–X by answering who owns an agent, who operates it, and how the architecture should adapt as models, prices, providers and regulation change. Define the **agent owner** (one named person), separate it from the **risk owner** per action class and the **platform owner**, and show how the **agent registry** becomes an enforced lifecycle (proposal → pilot → production ↔ restricted → deprecated → retired) rather than a catalog. Define **architecture review** for agents through the envelope rule: changes inside an approved envelope pass automated conformance; changes that move it are reviewed. Then synthesize the book's durable-versus-volatile judgements into one "durable core" and a test for telling a workaround for model weakness from a seam that bounds the model. The Close-Day Queue poses the ownership question; the Keelson 2.0 roadmap for 2028 is the worked answer.

## Audience

Chief architects, heads of agent platforms and engineering directors who must set up or repair the operating model around several production agents: on-call, incident authority, review, cost and risk governance, retirement and model-generation change. They know SRE and platform-team practice; they need the agent-specific splits and the reasons behind them.

## Success criteria

- [ ] Reader can name the three owner roles for an agent, what each owns and does not own, and why the agent owner is a person.
- [ ] Reader can state the hold/promote asymmetry and design who may hold, demote, defer, promote, register, raise budgets and retire, with latency and records (requirements table).
- [ ] Reader can run an agent incident: hold first, scope from evidence, repair as a risk-owner decision, restore by evidence; and knows when a regulatory branch (AI Act Art. 73, Art. 26) applies.
- [ ] Reader can draw the lifecycle state machine, say what each state permits at call time, and list the six retirement checks.
- [ ] Reader can classify a change as inside or outside an agent's envelope and use the review checklist that maps to the book's chapters.
- [ ] Reader can apply the cause test (weakness vs variation, external effects, accountability) to sort durable from volatile parts, and the three framework tests (seam, portability, quarter).
- [ ] Ostrell facts match the ledger (Close-Day Queue numbers, platform team 14 → 19, €5,000/month delegation, billing specialist fold-back 2027-06-07, Scout 0.64 → 0.81 at 2.4× tokens); the 2028 roadmap is appended to the ledger.
- [ ] Across Domains table, trade-off table, failure-scenario table and four mermaid diagrams present.

## Non-goals

- Kill-switch and quarantine mechanics — [[partial-failure-and-compensation]].
- Promotion criteria, demotion triggers and shadow mode — [[evidence-for-autonomy]].
- Manifest contents and migration calendar details — [[versioning-agent-systems]]; release mechanics — [[staged-rollout-and-rollback]].
- Cost metrics and budget hierarchy — [[agent-cost-and-model-routing]]; tracing design — [[agent-observability]].
- Domain-specific end-to-end designs — [[part-11]] and its chapters.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study follows an enterprise agent architecture across several model generations; the durable-core table is judgement. Revisit if such evidence appears.
- Whether an organization building agents for its own use is an AI Act "provider" for Article 73 is a legal question; the chapter flags it rather than answering it.
- ISO/IEC 42001 could not be fetched (HTTP 403) and is not cited; consider adding it if a primary source becomes reachable.

## Decision log

- **2026-10-28** — Used the Close-Day Queue (already canonical) as the scene, because its two-hour containment is an ownership failure, not a component failure.
- **2026-10-28** — Defined the "envelope" as the unit of architecture review, so review effort follows changes in authority and reach, not every release.
- **2026-10-28** — Framed durability with one cause test ("weakness, or variation, external effects, accountability?") to synthesize the per-chapter durable/volatile judgements without repeating them.
- **2026-10-28** — Defined the Keelson 2.0 roadmap (approved 2027-12-14) as mostly operating-model work, with capability re-baselining and a portability drill as the two technical items; appended it to the ledger.

## Sources

- Internal: [[agentic-reference-architecture]], [[autonomy-and-consequence]], [[evidence-for-autonomy]], [[versioning-agent-systems]], [[staged-rollout-and-rollback]], [[partial-failure-and-compensation]], [[agent-observability]], [[agent-cost-and-model-routing]], [[single-and-multi-agent-designs]], [[routing-and-delegation]], [[prompt-injection-defense]].
- Interview designs: `agentic-support-platform` (step `compliance-eval`, incident response), `agentic-platform-foundations` (`technologyChoices`, step `eval-obs`), `ai-coding-harness` (step `scale`), `agentic-sales-platform` (`api[4]`), `agentic-public-benefits-platform` (step `naive`).
- External: Google SRE book "Managing Incidents" (2016); Bainbridge (1983); Microsoft Cloud Adoption Framework AI CoE (2025, updated 2026); DORA 2025; Team Topologies key concepts; METR time horizons (2025–2026) and Becker et al. (2025); Anthropic "Building effective agents" (2024) and "Measuring AI agent autonomy in practice" (2026); OpenAI and Anthropic deprecation pages; AI Act Arts. 26, 73 and the Digital Omnibus (2026/1744); NIST AI RMF.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: exactly-once effect wording aligned with ruling 4; OpenAI deprecation quote and METR sensitivity claim corrected against the sources. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
