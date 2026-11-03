---
status: accepted
revised: 2026-10-28
---

# Spec: Sandboxes and Execution Environments

## Intent

Show architects where agent-generated actions should run and which boundaries keep them contained. The chapter must say what each isolation technology actually guarantees (seccomp, OS sandboxes such as Seatbelt and bubblewrap, containers, gVisor, microVMs, V8 isolates), set one rule for choosing among them (isolation strength follows autonomy and code provenance), and design the three boundaries of a sandbox together: filesystem, network (egress control) and credentials, plus a single reviewable exit. It must place permission modes, hooks and classifier-gated modes in coding CLIs as policy layered on that boundary, never as the boundary, and catalogue the escape classes every design must plan for, without describing working exploits. After reading, the reader can defend "autonomy up, isolation up" and can audit a sandbox by asking what crosses each boundary.

## Audience

Architects, platform and security engineers, and engineering leaders who run coding agents (local CLIs and headless harnesses), code-execution tools or browser agents, and must decide isolation technology, egress policy, credential placement and CLI configuration for an organization. They know containers, VMs and CI; they need the agent-specific consequences.

## Success criteria

- [ ] Reader can state what each rung of the isolation ladder guarantees and its known limits, with dated sources (runc CVEs, Firecracker NSDI 2020, gVisor non-goals, seccomp documentation).
- [ ] Reader can apply the autonomy-by-isolation matrix and the book ruling that unattended model-written code runs in a microVM or gVisor-class sandbox, and explain why the ai-coding-cli design's container-only cloud sandbox is not adopted.
- [ ] Reader can design filesystem, network and credential boundaries with a proxy-held credential, default-deny egress and one exit, and choose where the harness's inner loop and control plane run.
- [ ] Reader can map vendor permission modes to stable mode classes, explain deny-first precedence, the limits of pattern rules and the fail-open defaults of hooks.
- [ ] Reader can name the escape classes (kernel or runtime bug, misconfiguration, boundary computed from untrusted input, surfaces outside the sandbox, allowlisted destinations, built-in escape hatches, escape through the exit, side channels) with a documented instance and a control for each.
- [ ] Reader can present both measurements of classifier-gated autonomy (vendor 17% vs independent 81% false negatives) and the reason for the gap.
- [ ] Reader can follow Forge's sandbox and the local CLI's Silent Fallback with Ostrell numbers consistent with the ledger; the chapter has requirements, failure-scenario, trade-off and Across Domains tables and three mermaid diagrams.

## Non-goals

- Tool contracts and the tool broker in depth ([[tool-contracts]], [[tool-ecosystems-and-mcp]]); code execution as a tool interface is introduced there.
- Agent identity, token exchange and least privilege in depth ([[agent-identity-and-least-privilege]]).
- Prompt-injection defense architecture ([[prompt-injection-defense]]) and the threat model ([[agent-threat-model]]).
- Side-effecting actions, receipts and idempotency ([[side-effects-and-external-actions]], [[retries-idempotency-and-concurrency]]).
- Approval-gate design and automation-bias evidence ([[human-oversight-and-bounded-autonomy]]); the full coding-agent flow ([[domain-coding-agents]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The isolation technology behind several hosted agent sandboxes is not publicly documented; revisit if vendors publish it.
- No published incident analysis of agent output escaping through CI ("escape through the exit") was found; the row is the author's judgement.
- Classifier-gated modes are changing quickly and only one independent evaluation exists; update the Evidence section when more appear.
- The 84% prompt-reduction figure has no published method.

## Decision log

- **2026-10-28** — Adopted consistency items 1–3: one meaning of "harness"; isolation strength follows autonomy and code provenance (microVM or gVisor for unattended model-written code); credentials brokered and short-lived, local CLI named as ambient authority. Recorded the ai-coding-cli container cloud sandbox as a departure not adopted.
- **2026-10-28** — Added harness placement (whole harness inside, split, loop outside) as an explicit decision; recommended at least a split harness (control plane, budgets and credentials outside), matching Forge's inner loop running inside its sandbox as one leased activity per the agent-runtime ledger entry.
- **2026-10-28** — Framed escapes as classes with documented instances, not techniques, and added "escape through the exit" (agent output running in privileged CI) as the class most platforms miss.
- **2026-10-28** — Added two Ostrell stories: the January 2027 Forge red-team findings and the April 2027 Silent Fallback on 118 Linux workstations, to show the boundary's failure as configuration rather than technology.

## Sources

- **Internal**
  - [[what-makes-a-system-agentic]], [[autonomy-and-consequence]], [[tool-ecosystems-and-mcp]] (Toolyard, egress proxy, Tracker Update), [[planning-and-decomposition]] (Forge change plan), [[prompt-injection-defense]] (June 2027 principle), [[evaluating-agentic-systems]] (graders outside the sandbox), [[side-effects-and-external-actions]] (next page).
  - Design examples: `ai-coding-cli/interview.json` (steps `safety`, `cloud`, `extensibility`; `dataModel[permission_rules]`), `ai-coding-harness/interview.json` (step `sensors`), `agentic-platform-foundations/interview.json` (step `runtime`), `agentic-healthcare-platform/interview.json` (technology choices, step `privacy`).
- **External (key)**
  - Anthropic, Claude Code sandboxing, permissions and hooks documentation (accessed 2026-10); "Beyond permission prompts" (2025-10-20); auto mode post (2026-03-25).
  - OpenAI Codex sandboxing, approvals and hooks documentation (accessed 2026-10).
  - Ji et al., "Measuring the Permission Gate" (arXiv 2604.04978, 2026).
  - Agache et al., Firecracker (NSDI 2020); gVisor security model; Linux seccomp documentation; runc advisories (2024, 2025); NVD CVE-2025-54794, -54795, -59532.
  - Anthropic computer-use documentation; Claude for Chrome (2025-08-25); GitHub Actions secrets documentation.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: trimmed under 8,000 words (lead, hosted-sandbox lifetimes, browser-injection trade-press quote, Silent Fallback review paragraph); removed the Modal and TechCrunch sources no longer cited; fixed a citation typo. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
