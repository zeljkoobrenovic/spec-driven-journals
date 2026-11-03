---
status: accepted
revised: 2026-10-28
---

# Spec: Coding Agents: CLIs, Harnesses and the Developer Loop

## Intent

Open Part XI by showing how the book's mechanisms combine in the domain with the most deployed agents. The chapter explains why coding agents can run with more autonomy than any other agent (cheap workspace reversibility, cheap ground truth, an existing review gate) and what keeps that safe: keeping the verifier and the world out of the agent's reach. It tells the Fixture Purge in full as the domain's defining failure (verifier capture), gives an end-to-end reference design adapted from the author's coding interview designs, and sets out the controls per action class, the documented incidents and the disputed productivity evidence. The reader should leave able to design or review a coding-agent program, and to say which of its controls transfer to other domains and which do not.

## Audience

Architects, principal engineers and engineering leaders who run or fund coding CLIs and headless coding harnesses, and architects in other domains who use coding agents as the template. They know CI, code review and version control; they need the agent-specific failure modes and the control design.

## Success criteria

- [x] Consequence profile of the domain stated with the five consequence properties, plus workspace versus world reversibility as an owned term, tied to dated documented incidents (Replit 2025, Terraform destroy 2026, PocketOS 2026).
- [x] Interactive CLI versus headless harness compared in a table; action, rule and outcome approval distinguished; outcome approval owned.
- [x] Reference design labeled as a design example from `ai-coding-cli` and `ai-coding-harness`, with the book's departures stated (microVM, proxy-held credential, split harness per consistency item 20, security model for the outer harness, auto-merge evidence).
- [x] End-to-end sequence diagram of a Forge run, requirements-per-interaction table and a controls table with tier, enforcement, oversight, evaluation and audit per action class.
- [x] At least three failure scenarios with detection, containment and recovery (verifier capture, injection through repository content, world effect through ambient authority, plus sandbox loss, review flood, silent upgrade).
- [x] Verifier capture defined and evidenced (ImpossibleBench, SWE-Lancer audit, SWE-Bench+, METR 2026), with Ostrell's five-part verifier contract and a short code sketch.
- [x] Productivity evidence presented with its disagreement (Peng 2023, Paradis 2024, METR 2025 and 2026, DORA 2025) and a decision drawn from it.
- [x] Fixture Purge numbers match the ledger (July 2027, 9 PRs over two weeks, 2 merged; protected paths, test-count grader, reviewer checklist); "What Transfers to Other Domains" replaces "Across Domains".

## Non-goals

- Isolation technologies, egress control, permission modes and hooks in depth: [[sandboxes-and-execution-environments]].
- Plan-as-data and the change plan mechanics: [[planning-and-decomposition]]; the run card's interface design: [[agent-interaction-design]].
- Grader construction and suite maintenance: [[building-agent-eval-suites]]; evaluation levels: [[evaluating-agentic-systems]].
- Injection defenses: [[prompt-injection-defense]]; identity and tokens: [[agent-identity-and-least-privilege]].
- Compensation and revert mechanics in general: [[partial-failure-and-compensation]].
- Vendor product comparisons or recommendations.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published production rate of verifier capture exists; the chapter uses benchmark propensities and Ostrell illustration. Revisit if a company publishes one.
- The evidence threshold for auto-merge classes is the author's position; no source defines it.
- The METR February 2026 confidence-interval sign convention was not checked against METR's figure; the chapter quotes only METR's "very weak evidence" judgement.

## Decision log

- **2026-10-28** — Made the Fixture Purge the chapter's spine and added canonical local detail (trigger on 5 July 2027, the 4/4/1 breakdown, the back-order defect, detection on 16 July, the verifier contract, Q3 numbers), appended to the ledger.
- **2026-10-28** — Adopted the split harness of consistency item 20 (inner loop inside the microVM as one leased, heartbeated activity; model calls via the egress proxy to Keelson Gateway; only a run-scoped repository token inside) and stated the departure from the `ai-coding-cli` design.
- **2026-10-28** — Separated workspace from world reversibility so the documented destructive incidents are read as credential and backup failures, not test or review failures.
- **2026-10-28** — Kept model versions out of the prose; the METR June 2026 evaluation was re-verified on metr.org and cited without naming the model.

## Sources

- **Internal**
  - [[sandboxes-and-execution-environments]], [[planning-and-decomposition]], [[agent-interaction-design]], [[evaluating-agentic-systems]], [[building-agent-eval-suites]], [[autonomy-and-consequence]], [[evidence-for-autonomy]].
  - `_research/brief-domains-regulation.md` (Part 7), `brief-tools-execution.md` (7.3–7.5), `brief-reliability-recovery.md` (Parts 9–10), `brief-evaluation-observability.md` (1.2, 1.7), `digest-platform-and-coding.md` (sections 2–4).
  - Interview designs: `ai-coding-cli` (steps `agent-loop`, `context`, `safety`, `verify`, `cloud`); `ai-coding-harness` (steps `sensors`, `review-agents`, `lifecycle`, `drift`, `behaviour`, `scale`).
- **External**
  - Zhong, Raghunathan & Carlini, *ImpossibleBench* (2025); Zhu et al. (2025); Aleithan et al., *SWE-Bench+* (2024); METR (2026-06-26).
  - Peng et al. (2023); Paradis et al. (2024); Becker et al. (METR, 2025); METR (2026-02-24); DORA (2025).
  - Anthropic auto-mode post (2026) and Claude Code docs; OpenAI Codex docs; Ji et al. (2026); Stripe Minions posts (2026); Böckeler (2026).
  - Replit (The Register, 2025), Terraform destroy (Tom's Hardware, 2026), PocketOS (Euronews, NeuralTrust, 2026); NVD CVE records (2025).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: fixed a wrong consistency-ruling reference; corrected the AmPermBench description (81% false negatives over 253 state-changing actions from 128 prompts) and its source title; added METR's interval; dated the six-second approval figure to Q2 2027. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
