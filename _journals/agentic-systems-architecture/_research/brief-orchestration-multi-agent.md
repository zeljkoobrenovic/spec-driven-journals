# Research brief: Orchestration, planning and multi-agent coordination

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief is vendor-neutral. Anthropic, Cognition, OpenAI, Google, Microsoft and LangChain get the most space because they have published dated, first-hand material about how they coordinate agents, not because the book endorses their products.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date (for arXiv papers, the v1 submission date, with later revisions noted), not the fetch date. Undated documentation is marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, conference listing, aggregator summary), not from the primary document.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that its owner has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Source types are not equal.** The brief distinguishes peer-reviewed papers (ICLR, ICML, NeurIPS, ACL), arXiv preprints without a venue, vendor engineering posts (first-hand but unreviewed, usually with internal evals that cannot be reproduced), vendor documentation (describes what a product does today, not whether it works), and vendor marketing. A vendor engineering post that reports "90.2% better" on an internal eval is evidence of what that team observed, not a general law.

**Evidence age matters.** This field moves fast. Most planning papers cited here (ReWOO, Tree of Thoughts, HuggingGPT, LLMCompiler, multi-agent debate) were run on GPT-3.5/GPT-4-era models in 2023. Their *architectural* ideas still hold; their *numbers* describe models that are now two or more generations old and should not be quoted in the present tense as the expected gain from the technique. Any source older than about 18 months (before roughly April 2025) is flagged "evidence age" in its section.

**Research limitation.** The session relied on a shared web-search quota, so most evidence comes from direct fetches of known primary URLs. Specifically:

- Several WebFetch results returned only part of long pages (the A2A specification, the MAST HTML paper, the LLMCompiler HTML paper). Claims taken from the unread parts are not made.
- The MAST paper's category-level percentages (e.g. "system design issues 44.2%") were not visible in the fetched text and are not used; only per-mode percentages from the paper's HTML are reported.
- The "17.2× error amplification" and "39–70% degradation" figures from Google's scaling paper were verified on Google's research blog, not in the arXiv abstract, and the blog's numbers (180 configurations, four benchmarks, R² = 0.513) differ from the arXiv v3 abstract (260 configurations, six benchmarks, R² = 0.373). See "Where sources disagree".
- Cognition's follow-up post (April 2026) was fetched; its internal numbers (bug-catch rate, usage growth) are vendor-reported and unverifiable.
- No production incident report specifically attributing an outage or harm to multi-agent coordination was found in this session.
- Framework versions were checked against PyPI on 28 October 2026; framework *behaviour* was checked against current documentation, not by running code.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: SDK names and versions, default settings, project governance, spec versions and feature availability.

---

## PART 1: Vocabulary — what "orchestration" and "multi-agent" mean in this book

### 1.1 Workflows, agents and the patterns between them

| Term | Definition used in this brief | Who controls the next step |
| --- | --- | --- |
| Workflow | LLM calls and tools composed along code paths fixed at design time | Application code |
| Agent (single loop) | One model in a loop that picks its own tool calls until it stops | The model, inside a budget |
| Planner–executor | A model writes a plan up front; executors (code, tools or cheaper models) carry it out; a model may replan | The plan, then the model at replan points |
| Orchestrator–workers (manager pattern) | A lead model delegates sub-tasks to worker agents through tool calls and synthesises their results | The lead model |
| Handoff (decentralised pattern) | One agent transfers control of the conversation to another, which then owns it | Whichever agent currently holds control |
| Debate / voting | Several model instances answer the same question; answers are aggregated or argued over | Aggregation rule |
| Agent-to-agent protocol | Network protocol between independently owned agents that do not share memory or tools | Each agent's owner |

- Anthropic separates **workflows** ("systems where LLMs and tools are orchestrated through predefined code paths") from **agents** (systems where LLMs dynamically direct their own processes and tool usage) [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19].
- The same post names five composable workflow patterns: prompt chaining, routing, parallelization (sectioning or voting), orchestrator-workers, and evaluator-optimizer [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19].
- Its advice: "Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short." It also suggests "developers start by using LLM APIs directly", warning that frameworks add abstraction layers that hide prompts and responses [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19].
- The page now carries a note that much of the tooling it describes has changed since publication [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19]. Evidence age: 22 months; the pattern taxonomy is durable, the tooling advice is not.
- OpenAI's practical guide names two "broadly applicable" multi-agent categories: **Manager (agents as tools)**, where "a central 'manager' agent coordinates multiple specialized agents via tool calls", and **Decentralized (agents handing off to agents)**, where "multiple agents operate as peers, handing off tasks to one another based on their specializations". In graph terms, "in the manager pattern, edges represent tool calls whereas in the decentralized pattern, edges represent handoffs that transfer execution between agents" [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, published 2025-04 (PDF creation date 2025-04-07)].

**Durable vs volatile.** Durable: the split between code-controlled and model-controlled flow, and between "call another agent as a tool and get a result back" and "transfer control to another agent". Volatile: the names (subagent, handoff, swarm, crew, Magentic) and which framework calls what.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The book should treat "who owns the next step" as the first orchestration decision, before any choice of framework. A manager pattern keeps one accountable decision-maker per task; a handoff pattern moves accountability with the conversation, so the system needs a record of who held control when each action ran.

### 1.2 What the vendors themselves recommend first: one agent

- OpenAI: "Our general recommendation is to maximize a single agent's capabilities first. More agents can provide intuitive separation of concepts, but can introduce additional complexity and overhead, so often a single agent with tools is sufficient." [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, published 2025-04]
- OpenAI's splitting criteria are **complex logic** (prompts with many if-then-else branches) and **tool overload**, where "the issue isn't solely the number of tools, but their similarity or overlap. Some implementations successfully manage more than 15 well-defined, distinct tools while others struggle with fewer than 10 overlapping tools." It recommends splitting only if better tool names, parameters and descriptions do not help [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, published 2025-04].
- LangChain's current multi-agent documentation says multi-agent designs suit cases where one agent has too many tools and chooses poorly, where tasks need long specialised prompts, or where steps must unlock in sequence, and notes that a single agent with good tools and prompts can often do the job [VERIFIED: https://docs.langchain.com/oss/python/langchain/multi-agent, n.d., accessed 2026-10].
- Anthropic: add multi-step agentic systems "only when simpler solutions fall short" [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19].

**Durable vs volatile.** Durable: "one agent first, split on evidence". Volatile: the 10–15 tool thresholds, which depend on model capability and will move.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A design review should ask for the evidence that a single agent failed (tool-selection errors, instruction-following failures, context overflow) before approving a multi-agent design. "Separation of concerns" alone is an organisational argument, not a performance one.

---

## PART 2: Planning and task decomposition

### 2.1 Plan-then-execute: the family

| Technique | Year / venue | Core idea | Headline result (as measured) | Evidence age |
| --- | --- | --- | --- | --- |
| Plan-and-Solve prompting | 2023, ACL 2023 | Prompt the model to devise a plan, then execute it, inside one generation | Outperforms Zero-shot-CoT on ten datasets with GPT-3 | 41 months |
| ReWOO | 2023, arXiv preprint | Planner writes the full tool plan with variable placeholders; worker executes; solver answers | 5× token efficiency and +4% accuracy on HotpotQA | 41 months |
| HuggingGPT | 2023, arXiv (v4 Dec 2023) | LLM as controller: plan → select model → execute → summarise | No numeric result in abstract | 43 months |
| Tree of Thoughts | 2023, NeurIPS 2023 | Search over intermediate "thoughts" with self-evaluation and backtracking | Game of 24: 4% (GPT-4 CoT) → 74% | 41 months |
| LLMCompiler | 2023, ICML 2024 | Planner emits a task DAG; dispatcher runs ready tasks in parallel; joiner decides to answer or replan | Up to 3.7× latency, 6.7× cost, ~9% accuracy vs ReAct | 34 months |
| LangChain "plan-and-execute" | 2024 engineering post | Planner LLM + executor(s) + replan step | Claims speed, cost, quality; no measurements | 32 months |

Details and sources:

- **Plan-and-Solve (PS) prompting** asks the model to first devise a plan that splits the task into subtasks, then carry them out; PS+ adds instructions to reduce calculation errors. On ten datasets with GPT-3 it "consistently outperforms Zero-shot-CoT across all datasets by a large margin" and is comparable to 8-shot CoT on math [VERIFIED: https://arxiv.org/abs/2305.04091, published 2023-05-06; ACL 2023]. Note that this is planning *inside one prompt*, not an architectural planner–executor split.
- **ReWOO** (Reasoning WithOut Observation) decouples reasoning from tool observations: the plan is written once, with placeholders, so the model is not re-prompted with the whole history after every tool call. The abstract reports "5x token efficiency and 4% accuracy improvement on HotpotQA", measured across six public NLP benchmarks and one curated dataset against interleaved reason-and-act systems; it also studied robustness under tool failure and offloaded reasoning from 175B GPT-3.5 into a 7B LLaMA via instruction fine-tuning [VERIFIED: https://arxiv.org/abs/2305.18323, published 2023-05-23; arXiv preprint, no venue stated].
- **HuggingGPT** uses ChatGPT as a controller in four stages: task planning, model selection (from Hugging Face model descriptions), task execution, and response generation. The abstract claims "impressive results" without figures [VERIFIED: https://arxiv.org/abs/2303.17580, published 2023-03-30, revised 2023-12-03]. [ASSUMPTION/JUDGEMENT] It is widely cited as a NeurIPS 2023 paper; the arXiv page fetched does not state the venue, so chapter writers should check before citing it as peer-reviewed.
- **Tree of Thoughts (ToT)** generalises chain-of-thought into search over intermediate steps with self-evaluation, lookahead and backtracking. On Game of 24, "GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%"; the other tasks were Creative Writing and Mini Crosswords [VERIFIED: https://arxiv.org/abs/2305.10601, published 2023-05-17; NeurIPS 2023 camera-ready per arXiv v2 comment]. [ASSUMPTION/JUDGEMENT] ToT multiplies model calls per problem; its cost per solved problem was not verified in this session.
- **LLMCompiler** has three components: a *Function Calling Planner* (LLM) that produces a dependency graph with placeholder variables, a *Task Fetching Unit* that substitutes real outputs and dispatches tasks once dependencies are met, and an *Executor* that runs them concurrently. The fetching unit needs no LLM [VERIFIED: https://arxiv.org/html/2312.04511, published 2023-12-07, revised 2024-06-05; ICML 2024].
- **LLMCompiler per-benchmark results** vs ReAct (or tuned baselines) [VERIFIED: https://arxiv.org/html/2312.04511, published 2023-12-07]:

| Benchmark | Model | Latency speedup | Cost reduction | Accuracy (baseline → LLMCompiler) |
| --- | --- | --- | --- | --- |
| HotpotQA | GPT-3.5 | 1.80× (vs tuned ReAct) | 3.37× | 61.52 → 62.00 |
| Movie Recommendation | GPT-3.5 | 3.74× (vs tuned ReAct) | 6.73× | 68.60 → 77.13 |
| ParallelQA | GPT-4-turbo | 2.15× | 4.65× | 89.09 → 89.38 |
| ParallelQA | LLaMA-2 70B | 2.27× | n/a | 59.59 → 68.14 |
| Game of 24 | GPT-4 | 2.89× (vs Tree of Thoughts) | n/a | 74.00 → 75.33 |
| WebShop | GPT-4 | slower than ReAct; ~101.7× faster than LATS | n/a | 35.2 → 55.6 success |

- **LLMCompiler limitations stated in the paper**: planner and final-answer overhead cannot be parallelised (about 1.88 s and 1.62 s on Movie Recommendation); stragglers slow the join (the slowest search averaged about twice mean task latency); 64% of ParallelQA failures came from the executor and 8% from the planner; on WebShop the planner made it slower than ReAct [VERIFIED: https://arxiv.org/html/2312.04511, published 2023-12-07].
- **LangChain's plan-and-execute** post describes a planner that writes a multi-step plan, executors that invoke tools per step, and a re-invocation to respond or replan. Claimed benefits: speed (the big model is not consulted after every action), cost (sub-tasks can use smaller models) and quality (forcing the planner to reason through all steps). It describes ReWOO as sequential execution with variable substitution, and LLMCompiler as a streamed DAG with a task-fetching unit and joiner, citing "3.6x speedup" [VERIFIED: https://www.langchain.com/blog/planning-agents, published 2024-02-13]. These benefits are claimed, not measured in the post.

**What was actually measured.** [ASSUMPTION/JUDGEMENT] Every planning number above comes from short, closed-world benchmarks (multi-hop QA, puzzles, a simulated shop) with 2023-era models. None measures long-horizon enterprise tasks, side-effecting tools, or plan validity when the world changes between planning and execution. The gains from explicit planning have likely shrunk as models gained native long reasoning and parallel tool calling; no 2025–26 head-to-head was found in this session.

**Durable vs volatile.** Durable: separating the *decision* (plan) from *execution*; representing a plan as a dependency graph so independent steps run in parallel; placeholders instead of re-reading history; a replan/joiner checkpoint. Volatile: the accuracy deltas, which are specific to GPT-3.5/GPT-4 and benchmarks now mostly saturated.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- A plan written as data (a DAG of typed steps) is an architectural asset: it can be validated against policy, shown to a human for approval *before* any side effect, persisted for resume, and diffed on replan. A plan that lives only inside a model's reasoning tokens offers none of this.
- The dispatcher in LLMCompiler is ordinary code. Put scheduling, retries, concurrency limits and idempotency there, not in prompts.
- Plan-then-execute trades adaptivity for cost and latency. Where tool results routinely invalidate the plan, the replan rate becomes the metric to watch.

### 2.2 Routing

- Routing "classifies an input and directs it to a specialized followup task" [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19].
- LangChain's documentation lists a **router** pattern (a routing step classifies input, sends it to specialised agents, and synthesises results), rated strong for parallelisation and stateless across turns [VERIFIED: https://docs.langchain.com/oss/python/langchain/multi-agent, n.d., accessed 2026-10].
- Google ADK lists **agent routing** — router functions that select between agents at runtime for fallback, A/B testing and auto-routing — as *experimental* ⚠ [VERIFIED: https://adk.dev/workflows/, n.d., accessed 2026-10].

**Durable vs volatile.** Durable: routing is a classifier problem with measurable precision/recall and a fallback class. Volatile: whether it is called a router, triage agent or coordinator.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A router is the cheapest form of multi-agent and the easiest to evaluate (labelled inputs, confusion matrix). It should be the default before peer handoffs. Keep an explicit "none of the above / human" route.

---

## PART 3: Delegation and handoffs in current frameworks (status as of 28 October 2026)

### 3.1 Framework status table ⚠

| Framework | Latest PyPI version (date) | Multi-agent primitives | Status note |
| --- | --- | --- | --- |
| OpenAI Agents SDK (`openai-agents`) | 0.24.0 (2026-10-15) | Handoffs (tool-represented), agents-as-tools | Still pre-1.0 versioning |
| Claude Agent SDK (`claude-agent-sdk`, Python) | 0.2.174 (2026-10-24) | Subagents via Agent tool, forks, background agents, depth/concurrency/spend caps, Workflow tool (TS) | Bundles Claude Code |
| LangGraph (`langgraph`) | 1.2.18 (2026-10-26) | Graphs, `Command` handoffs; docs patterns: subagents, handoffs, skills, router, custom | `langgraph-supervisor` archived; last release 0.0.31 (2025-11-19) |
| `langgraph-swarm` | 0.1.0 (2025-12-04) | Peer handoffs with active-agent memory | No release in ~11 months |
| Google ADK (`google-adk`) | 2.13.0 (2026-10-23) | sub_agents with modes (chat/task/single_turn), template workflows (sequential/parallel/loop), graph/dynamic/collaborative workflows (2.0+) | Routing experimental |
| Microsoft Agent Framework (`agent-framework`) | 1.23.0 Python (2026-10-22); .NET 1.26.0 (2026-10-23) | Sequential, concurrent, handoff, group chat, Magentic orchestrations | GA 1.0 on 2026-04-03; successor to AutoGen + Semantic Kernel |
| AutoGen (`autogen-agentchat`) | 0.7.5 (2025-09-30) | Group chat, Magentic-One | Archived; not maintained by Microsoft |
| CrewAI (`crewai`) | 1.15.32 (2026-10-27) | Crews (sequential / hierarchical process), Flows (event-driven, persisted state) | Active |
| A2A Python SDK (`a2a-sdk`) | 1.3.0 (2026-10-27) | Protocol client/server | See Part 6 |

Versions and dates: [VERIFIED: https://pypi.org/pypi/<package>/json for each package, n.d., accessed 2026-10-28]. Microsoft .NET release: [VERIFIED: https://github.com/microsoft/agent-framework/releases, published 2026-10-23].

### 3.2 OpenAI Agents SDK: handoffs and agents-as-tools

- "Handoffs are represented as tools to the LLM"; the default tool name is `transfer_to_<agent_name>` [VERIFIED: https://openai.github.io/openai-agents-python/handoffs/, n.d., accessed 2026-10].
- `handoff()` options include `on_handoff` (callback when invoked), `input_type` (schema for model-generated metadata such as a reason or priority), `input_filter` (changes what the next agent sees), `is_enabled` (runtime enable/disable) and `nest_handoff_history` [VERIFIED: same URL].
- **By default the receiving agent sees the full conversation history.** An `input_filter` can rewrite it; built-in filters such as `remove_all_tools` remove structured tool items but not tool content already copied into messages [VERIFIED: same URL].
- `is_enabled` is evaluated before the model returns arguments, so the docs place argument-based authorization at the start of `on_handoff`; raising an exception there stops the transfer [VERIFIED: same URL].
- Nested handoff history (summarising earlier history into a `<CONVERSATION HISTORY>` segment) is an **opt-in beta** ⚠, and the docs warn that nesting "does not redact sensitive data" [VERIFIED: same URL].
- Handoff input filters are not supported with server-managed conversations (`conversation_id`, `previous_response_id`) ⚠ [VERIFIED: same URL].
- The docs distinguish a handoff (transfers control of the conversation) from `Agent.as_tool()` (structured input to a specialist without transferring the conversation) [VERIFIED: same URL].
- OpenAI's guide describes handoffs as "a one way transfer", in which execution starts on the new agent "while also transferring the latest conversation state"; the pattern "is optimal when you don't need a single agent maintaining central control or synthesis" [VERIFIED: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, published 2025-04].

### 3.3 Claude Agent SDK subagents

- Subagents are "separate agent instances that your main agent can spawn to handle focused subtasks", defined programmatically (`agents` option with `AgentDefinition`), as markdown files in `.claude/agents/`, or via a built-in `general-purpose` subagent [VERIFIED: https://code.claude.com/docs/en/agent-sdk/subagents, n.d., accessed 2026-10].
- **Context isolation**: each subagent "runs in its own conversation, which starts fresh unless the subagent is a fork"; intermediate tool calls stay inside it and "only its final message returns to the parent". "The only content you pass from parent to subagent is the Agent tool's prompt string" [VERIFIED: same URL].
- A non-fork subagent receives its own system prompt, the Agent tool's prompt, project CLAUDE.md (unless `omitClaudeMd`), and tool definitions; it does not receive the parent's history, tool results or system prompt [VERIFIED: same URL].
- `AgentDefinition` fields include `tools`/`disallowedTools` (tool restriction), `model` override, `maxTurns`, `background`, `effort` and `permissionMode` ⚠ [VERIFIED: same URL].
- **Growth caps** ⚠: subagents can spawn subagents, "so one prompt can grow into a tree of agents". Defaults: spawn depth 3 layers (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`), 20 concurrent subagents (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`), and no default spend limit (`max_budget_usd`); at the spend cap it refuses new spawns, stops background subagents and ends the query with `error_max_budget_usd`. These apply to TypeScript SDK v0.3.219 / Python SDK v0.2.127 and later [VERIFIED: same URL].
- The docs say Claude Opus 5 "delegates to subagents more readily than earlier models", so the limits "matter most" on Opus 5 queries, and prompt instructions "only steer Claude, so set the limits as well" ⚠ [VERIFIED: same URL].
- Before the parent reads a subagent's final message, Claude Code (v2.1.210+) scans it for instruction-shaped patterns (control-tag imitation, permission-configuration mentions, turn markers) and neutralises or marks them without removing text ⚠ [VERIFIED: same URL].
- For runs coordinating "dozens to hundreds of agents", the docs point to a `Workflow` tool that "moves the orchestration into a script the runtime executes outside the conversation context" (TypeScript SDK v0.3.149+) ⚠ [VERIFIED: same URL].

### 3.4 LangGraph / LangChain

- The `langgraph-supervisor` README now says the team recommends implementing the supervisor pattern directly with tools for most use cases "since it gives more control over context engineering"; the repository is archived and read-only ⚠ [VERIFIED: https://github.com/langchain-ai/langgraph-supervisor-py, n.d., accessed 2026-10].
- Its handoff tools pass the full message history plus a confirming tool message by default; `output_mode` chooses `full_history` or `last_message` for what a worker contributes back; `create_forward_message_tool` sends a worker's last message straight to output "to save supervisor tokens and avoid paraphrasing" [VERIFIED: same URL].
- `langgraph-swarm` implements peers that "dynamically hand off control to one another based on their specializations", remembers the last active agent, and needs a checkpointer for multi-turn use or it loses the active agent and history [VERIFIED: https://github.com/langchain-ai/langgraph-swarm-py, n.d., accessed 2026-10].
- LangChain's documentation compares patterns by model calls and tokens on its own example tasks: one-shot request — subagents 4 calls, handoffs 3, skills 3, router 3; repeat request (turn 2 / total) — subagents 4/8, handoffs 2/5, skills 2/5, router 3/6; three-domain task — subagents 5 calls ~9K tokens, handoffs 7+ calls ~14K+ tokens, skills 3 calls ~15K tokens, router 5 calls ~9K tokens. It says stateful patterns (handoffs, skills) save about 40–50% of calls on repeat requests, while stateless patterns (subagents, router) parallelise and use fewest tokens on multi-domain work [VERIFIED: https://docs.langchain.com/oss/python/langchain/multi-agent, n.d., accessed 2026-10]. These are illustrative counts on vendor examples, not a benchmark.

### 3.5 Google ADK

- ADK 2.0+ adds graph-based workflows (agents and deterministic nodes with branching), dynamic workflows (programmatic composition) and collaborative workflows (a coordinator over sub-agents); template workflows (sequential, loop, parallel) predate 2.0 ⚠ [VERIFIED: https://adk.dev/workflows/, n.d., accessed 2026-10].
- In collaborative workflows a parent declares `sub_agents` and ADK generates a delegation tool per sub-agent. Sub-agent **modes**: `chat` (free-form user interaction, explicit `transfer_to_agent` back), `task` (may ask clarifying questions, returns when it calls `finish_task`), `single_turn` (no user interaction, returns automatically, can run in parallel) [VERIFIED: https://adk.dev/workflows/collaboration/, n.d., accessed 2026-10].
- `task` and `single_turn` agents run in their own session branch and see only their own events; "parallel peers can't see each other's work"; only `single_turn` agents can run in parallel; `task` agents must be leaves; in Python v2.0.0 `task` mode is disabled in graph workflows ⚠ [VERIFIED: same URL].

### 3.6 Microsoft: AutoGen → Agent Framework

- AutoGen's README: "Project archived and no longer maintained"; "Microsoft is not providing bug fixes, security fixes, new features, or support for this project"; new users should start with Microsoft Agent Framework [VERIFIED: https://github.com/microsoft/autogen, n.d., accessed 2026-10]. (The README also contains an older line saying contributions are limited to bug fixes and security patches "as AutoGen is in maintenance mode"; the archived/no-security-fixes wording is the stronger, later statement.)
- Microsoft Agent Framework reached **version 1.0 for .NET and Python on 3 April 2026**. Stable: single-agent abstraction, middleware hooks, memory and context providers, graph-based workflows, multi-agent orchestration (sequential, concurrent, handoff, group chat, Magentic-One), declarative YAML agents, MCP support. Preview ⚠: DevUI, Foundry hosted agents and tools, AG-UI/CopilotKit/ChatKit adapters, Skills, GitHub Copilot SDK and Claude Code SDK integration, Agent Harness. "A2A 1.0 support coming soon" at GA [VERIFIED: https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/, published 2026-04-03].
- The framework was created to combine Semantic Kernel's enterprise foundations with AutoGen's orchestration, with migration assistants for both [VERIFIED: same URL]. A release candidate preceded GA in February 2026 [WIDELY REPORTED: https://devblogs.microsoft.com/agent-framework/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/, 2026].
- Agent Framework orchestrations: Sequential, Concurrent, Handoff, Group Chat and Magentic ("a manager agent dynamically coordinates specialized agents"); orchestrations support human-in-the-loop through approval-required tools that pause the workflow [VERIFIED: https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview, published 2026-02-12, updated 2026-08-25].

### 3.7 CrewAI

- `Process` is an enumeration with two values: **sequential** (tasks in order, outputs as context via the `context` parameter) and **hierarchical** (requires `manager_llm` or `manager_agent`; the manager plans, delegates, reviews outputs and decides completion; tasks are not pre-assigned) [VERIFIED: https://docs.crewai.com/en/concepts/processes, n.d., accessed 2026-10].
- **Flows** are event-driven workflows (`@start`, `@listen`, `@router`) that orchestrate Crews, agents and plain Python, with state (dict or Pydantic), `@persist` to SQLite by default, resume or fork from saved state, and `@human_feedback` (CrewAI 1.8.0+) [VERIFIED: https://docs.crewai.com/en/concepts/flows, n.d., accessed 2026-10].

**Durable vs volatile (Part 3).** Durable: two delegation semantics — *call and return* (subagent, agent-as-tool, ADK `task`/`single_turn`) versus *transfer of control* (handoff, swarm, ADK `chat`) — and the question of what context crosses the boundary (full history by default in OpenAI and LangGraph handoffs; only a prompt string for Claude subagents and ADK task branches). Volatile: every class name, default, version number and beta flag in this part. The consolidation trend (AutoGen archived, LangGraph supervisor library archived in favour of "do it with tools", CrewAI adding Flows, ADK 2.0 adding graphs) is itself the most durable signal: frameworks are converging on *deterministic graph outside, model-driven delegation inside*.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Default context transfer is a security and cost decision hidden in a framework default. Full-history handoffs leak everything the previous agent saw (including untrusted tool output) into the next agent's context; prompt-only delegation loses context the sub-agent may need (Cognition's complaint, Part 4). Make the boundary explicit and reviewed.
- Because spawning is model-driven, bounds must be enforced by the runtime (depth, concurrency, spend, turns), not by prompt. The Claude SDK's defaults (depth 3, 20 concurrent, no spend cap) show a vendor choosing permissive defaults; production deployments should set their own.
- Framework churn is high (an archived Microsoft framework in ~2 years; an archived LangGraph helper library). Keep orchestration semantics in your own thin layer or in durable workflow state, so a framework swap does not change behaviour.

---

## PART 4: When multi-agent helps — first-hand engineering evidence

### 4.1 Anthropic: "How we built our multi-agent research system" (June 2025)

Vendor engineering post; internal evals; not reproducible. Evidence age: 16 months, on Claude Opus 4 / Sonnet 4.

- **Architecture**: orchestrator-worker. A LeadResearcher plans, saves the plan to Memory (because context beyond 200,000 tokens gets truncated), spawns subagents that search iteratively with interleaved thinking, synthesises results and decides whether to continue; a CitationAgent then attaches citations [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].
- **Headline result**: a multi-agent system with Claude Opus 4 as lead and Claude Sonnet 4 subagents "outperformed single-agent Claude Opus 4 by 90.2%" on Anthropic's internal research eval [VERIFIED: same URL].
- **What explains performance**: on BrowseComp, token usage alone explained 80% of the variance; token usage, number of tool calls and model choice together explained 95% [VERIFIED: same URL]. "Multi-agent systems work mainly because they help spend enough tokens to solve the problem." [VERIFIED: same URL]
- **Token cost**: agents use about **4×** the tokens of chat interactions; multi-agent systems about **15×** chat [VERIFIED: same URL].
- **Latency**: parallelism (lead spins up 3–5 subagents in parallel; subagents use 3+ tools in parallel) cut research time "by up to 90%" for complex queries [VERIFIED: same URL].
- **Tool descriptions**: a tool-testing agent that rewrote tool descriptions cut subsequent task completion time by 40% [VERIFIED: same URL].
- **Scaling rules embedded in prompts**: simple fact-finding, 1 agent with 3–10 tool calls; direct comparisons, 2–4 subagents with 10–15 calls each; complex research, more than 10 subagents [VERIFIED: same URL].
- **When it helps**: breadth-first queries, heavy parallelisation, information exceeding one context window, many complex tools. **When it hurts**: tasks needing shared context or many inter-agent dependencies — "most coding tasks" — and tasks whose value does not justify the token cost [VERIFIED: same URL].
- **Observed failures**: spawning 50 subagents for simple queries, endless searching for nonexistent sources, duplicated work from vague task descriptions, continuing after results were sufficient [VERIFIED: same URL].
- "LLM agents are not yet great at coordinating and delegating to other agents in real time." [VERIFIED: same URL]
- **Evaluation**: started with about 20 queries from real usage; an LLM judge (single call, 0.0–1.0 scores plus pass/fail) scored factual accuracy, citation accuracy, completeness, source quality and tool efficiency; human testers still caught issues automation missed, such as preferring SEO content farms over authoritative sources [VERIFIED: same URL].
- **Deployment**: rainbow deployments shift traffic gradually between versions so long-running in-flight agents are not disrupted [VERIFIED: same URL].
- Anthropic's later context-engineering guidance says sub-agents may use "tens of thousands of tokens or more" exploring but return "often 1,000-2,000 tokens", and that sub-agents fit complex research and parallel exploration while compaction fits long back-and-forth and structured note-taking fits milestone-driven iterative work [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09 (date not shown in fetched text; ⚠ confirm exact day)].

**What was measured, and limits.** [ASSUMPTION/JUDGEMENT] The 90.2% figure is a relative improvement on an internal research eval, comparing a system that spent far more tokens to one that spent fewer, so it does not isolate the value of *multiple agents* from the value of *more compute*. Anthropic's own variance analysis (80% explained by tokens) points the same way. The eval set started at about 20 queries. Treat it as strong evidence that parallel breadth search with isolated contexts works for research, not as evidence for multi-agent designs in general.

### 4.2 Cognition: "Don't Build Multi-Agents" (June 2025) and the April 2026 follow-up

- Walden Yan's two principles, verbatim: "Share context, and share full agent traces, not just individual messages" and "Actions carry implicit decisions, and conflicting decisions carry bad results" [VERIFIED: https://cognition.com/blog/dont-build-multi-agents, published 2025-06-12].
- The Flappy Bird example: a task split into "background with pipes" and "bird" sub-tasks produced a Super Mario-style background and a mismatched bird, leaving the final agent to reconcile incompatible outputs [VERIFIED: same URL].
- Recommended instead: a single-threaded linear agent (simplest, keeps context continuous, may overflow on very large tasks), and for long tasks a separate model that compresses history into key details, events and decisions — hard to get right; Cognition fine-tuned a smaller model for it [VERIFIED: same URL].
- It describes Claude Code's subagents (at the time) as deliberately limited — not run in parallel with the main agent, usually answering well-defined questions rather than writing code — with value in keeping investigative work out of the main history [VERIFIED: same URL]. ⚠ Claude Code subagents now run in the background and in parallel by default (Part 3.3), so this description is outdated.
- The post appeared one day before Anthropic's research-system post; the two are often read as opposing positions [WIDELY REPORTED: https://news.smol.ai/frozen-issues/25-06-13-cognition-vs-anthropic.html, 2025].
- **Follow-up, "Multi-Agents: What's Actually Working" (Walden Yan, 22 April 2026).** What works now: clean-context review loops (a reviewer that does not see the coder's context tends to do better), a "smart friend" escalation to a stronger model (works when both are strong), manager-and-child delegation in Devin, and read-only search subagents. What still does not: parallel-writer swarms ("conflicting implicit decisions"), smart-friend with a weaker primary model (SWE-1.5 + Sonnet 4.5 fell short), weaker models not knowing when to escalate, children not surfacing discoveries to siblings and assuming shared state they lack; unstructured agent networks are "mostly a distraction" [VERIFIED: https://cognition.com/blog/multi-agents-working, published 2026-04-22].
- Vendor-reported numbers in the follow-up: Devin Review catches an average of 2 bugs per PR, about 58% severe; Devin usage in the largest enterprise segment grew about 8× in six months [VERIFIED: same URL]. Unverifiable and marketing-adjacent; do not use as evidence about multi-agent design.

**Durable vs volatile.** Durable: *read-many, write-one*. Parallel agents are safe for gathering (search, review, analysis) and dangerous for writing to shared artefacts, because each write embodies unstated decisions. Volatile: which models are strong enough to delegate or to know when to escalate.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Give exactly one agent write authority over a given artefact at a time; parallel agents return findings, not edits. This maps onto single-writer principles in distributed systems.
- An independent reviewer with a clean context is one of the few multi-agent patterns both camps endorse. It is also a natural oversight control.
- When delegating, pass the decisions already taken (style, interfaces, constraints) explicitly; "share context" is a contract design problem, not a prompt-length problem.

### 4.3 Anthropic and Cognition compared

| Question | Anthropic (2025-06) | Cognition (2025-06) | Cognition (2026-04) |
| --- | --- | --- | --- |
| Domain | Open-ended web research | Coding agents | Coding agents |
| Parallel subagents? | Yes, 3–5 at a time, up to >10 | No | Yes for read-only search and review; no for parallel writers |
| Why it works / fails | Spends more tokens in parallel, isolated contexts | Lost context, conflicting implicit decisions | Same; plus weak escalation and sibling communication |
| Cost stated | ~15× chat tokens | Not quantified | Not quantified |
| Agreement | "Most coding tasks" are a poor fit | Coding is a poor fit for splitting | Manager–child works when children are scoped |

[ASSUMPTION/JUDGEMENT] The two positions are more compatible than the headlines: both say multi-agent pays when sub-tasks are independent and read-mostly, and fails when sub-tasks share decisions.

---

## PART 5: Systematic evidence — failures, scaling and debate

### 5.1 MAST: "Why Do Multi-Agent LLM Systems Fail?" (Cemri et al.)

- 13 authors (UC Berkeley Sky lab and collaborators, including Matei Zaharia, Joseph Gonzalez, Ion Stoica); arXiv v1 17 March 2025, v3 26 October 2025 [VERIFIED: https://arxiv.org/abs/2503.13657, published 2025-03-17]. Accepted to the NeurIPS 2025 Datasets and Benchmarks Track [WIDELY REPORTED: https://neurips.cc/virtual/2025/poster/121528, 2025].
- **What was measured**: 1,600+ annotated traces (1,642 in the HTML text) from **7 frameworks** — MetaGPT, ChatDev, HyperAgent, AppWorld, AG2 (MathChat), Magentic-One, OpenManus — using GPT-4o, GPT-4, GPT-4o-mini, Claude 3.7 Sonnet, Qwen2.5-Coder-32B and CodeLlama-7B. The taxonomy was derived (Grounded Theory) from 150 traces; human inter-annotator agreement κ = 0.88 [VERIFIED: https://arxiv.org/abs/2503.13657 and https://arxiv.org/html/2503.13657, published 2025-03-17].
- **Taxonomy**: 14 failure modes in 3 categories — system design (specification) issues, inter-agent misalignment, task verification [VERIFIED: same URLs].
- **Per-mode prevalence** (share of failures) [VERIFIED: https://arxiv.org/html/2503.13657, published 2025-03-17]:

| Category | Failure mode (paraphrased) | Prevalence |
| --- | --- | --- |
| System design | Repeats completed steps | 15.7% |
| System design | Does not recognise task completion | 12.4% |
| System design | Disobeys task requirements | 11.8% |
| System design | Loses conversation context | 2.8% |
| System design | Disobeys assigned role | 1.5% |
| Inter-agent misalignment | Reasoning–action mismatch | 13.2% |
| Inter-agent misalignment | Drifts off task | 7.4% |
| Inter-agent misalignment | Proceeds on assumptions instead of asking | 6.8% |
| Inter-agent misalignment | Unexpected conversation reset | 2.2% |
| Inter-agent misalignment | Ignores other agents' input | 1.9% |
| Inter-agent misalignment | Withholds needed information | 0.85% |
| Task verification | Incorrect verification | 9.1% |
| Task verification | No or incomplete verification | 8.2% |
| Task verification | Premature termination | 6.2% |

- **LLM-as-judge annotator**: OpenAI o1 few-shot reached accuracy 0.94 and κ 0.77 against humans (zero-shot κ 0.58); out-of-domain κ 0.79 [VERIFIED: https://arxiv.org/html/2503.13657].
- **Interventions**: on ChatDev, improved role specification / workflow changes gave **+9.4%** task success, and adding a high-level task-objective verification step gave **+15.6%** on ProgramDev; the authors say interventions gave inconsistent results and task completion stayed low [VERIFIED: https://arxiv.org/html/2503.13657]. (The fetched text describes the +9.4% change inconsistently; cite it cautiously.)
- **Stated limitations**: not exhaustive; some failures stem from base-model limits; modes correlate up to 0.63; closed systems excluded; ProgramDev tasks relatively simple [VERIFIED: https://arxiv.org/html/2503.13657].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Roughly a quarter of failures (the three verification modes, ~23.5%) and the largest single modes (repeating steps, not recognising completion) are things deterministic code can catch: step-level idempotency keys, explicit completion criteria checked by code, and an independent verifier stage. MAST is evidence that multi-agent failure is mostly a *specification and control* problem, which is architecture's territory.

### 5.2 Google/MIT: "Towards a Science of Scaling Agent Systems"

- arXiv preprint, Yubin Kim and 18 co-authors; v1 9 December 2025, v3 8 April 2026; no venue listed [VERIFIED: https://arxiv.org/abs/2512.08296, published 2025-12-09].
- **arXiv v3 abstract**: 260 configurations, six agentic benchmarks, five architectures (one single-agent, four multi-agent), three LLM families; relative change vs single-agent ranges from "+80.8% on decomposable financial reasoning" to "-70.0% on sequential planning"; coordination yields diminishing returns once single-agent baselines are strong ("capability saturation"); tool-heavy tasks incur multi-agent overhead; architectures without centralised verification propagate more errors; a predictive model reaches cross-validated R² = 0.373 (0.413 with a task-grounded capability metric) and picks the best architecture for 87% of held-out configurations [VERIFIED: https://arxiv.org/abs/2512.08296, v3 2026-04-08].
- **Google Research blog** (28 January 2026, describing an earlier version): 180 configurations, three model families (GPT, Gemini, Claude), four benchmarks (Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench); centralised coordination improved Finance-Agent by **80.9%**; every multi-agent variant degraded PlanCraft by **39–70%**; independent multi-agent systems amplified errors **17.2×**, centralised systems contained amplification to **4.4×**; predictive model R² = 0.513, best architecture for 87% of unseen configurations [VERIFIED: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/, published 2026-01-28].
- Architectures defined: single-agent; independent (parallel, no communication, results combined at end); centralised (orchestrator delegates and synthesises); decentralised (peer-to-peer consensus); hybrid [VERIFIED: same blog URL].
- Practitioner takeaways from the blog: "more agents" "often hits a ceiling"; match architecture to task structure; coordination overhead rises disproportionately with tool count; a centralised orchestrator acts as a validation step that limits error propagation [VERIFIED: same blog URL].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] This is the best controlled evidence found for the book's frame: decomposability of the task, not the number of agents, predicts benefit; sequential tasks get worse; an orchestrator that *validates* is what contains error amplification. Chapter writers should cite the arXiv v3 numbers as current and the blog's 17.2×/4.4× as the earlier version's result.

### 5.3 Multi-agent debate: evidence and critiques

| Paper | Venue / status | Setting | Finding |
| --- | --- | --- | --- |
| Du et al., "Improving Factuality and Reasoning… through Multiagent Debate" | arXiv 2023-05 (venue not shown on arXiv page) | 3 agents, 2 rounds, gpt-3.5-turbo-0301, 100 problems per task | Debate beat single agent and reflection on all six tasks |
| Huang et al., "LLMs Cannot Self-Correct Reasoning Yet" | ICLR 2024 | Intrinsic self-correction on reasoning | Models struggle to self-correct without external feedback; sometimes worse |
| Smit et al., "Should we be going MAD?" | arXiv 2023-11, rev. 2024-07 | Several debate protocols vs other prompting | Debate does not reliably beat self-consistency / ensembling; very hyperparameter-sensitive |
| Wang et al., "Rethinking the Bounds of LLM Reasoning" | arXiv 2024-02 | Discussion vs single agent across reasoning tasks | A single agent "with strong prompts can achieve almost the same performance"; discussion wins only with no demonstrations |
| Choi, Zhu, Li, "Debate or Vote" | NeurIPS 2025 Spotlight | Seven NLP benchmarks + theory | "Majority Voting alone accounts for most of the performance gains typically attributed to MAD"; debate is a martingale |

- **Du et al.** used mostly 3 agents and 2 rounds; gains flattened beyond about 4 rounds. Accuracy (single → reflection → debate): arithmetic 67.0 → 72.1 → 81.8; GSM8K 77.0 → 75.0 → 85.0; biographies 66.0 → 68.3 → 73.8; MMLU 63.9 → 57.7 → 71.1; chess move validity 29.3 → 38.8 → 45.2. Limitations stated: higher cost (multiple instances and rounds), long debates where models attend to recent messages, convergence on confidently wrong answers, small samples, one model family [VERIFIED: https://arxiv.org/html/2305.14325, published 2023-05-23]. Evidence age: 41 months, GPT-3.5.
- **Huang et al.** examine "intrinsic self-correction" and find LLMs "struggle to self-correct their responses without external feedback", with performance sometimes degrading [VERIFIED: https://arxiv.org/abs/2310.01798, published 2023-10-03; ICLR 2024]. [ASSUMPTION/JUDGEMENT] The paper is widely cited as also showing that debate's gains shrink against self-consistency with an equal number of responses; the fetched abstract does not state this, so do not attribute it without reading the body.
- **Smit et al.**: MAD systems "do not reliably outperform other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths"; with tuning, some (e.g. Multi-Persona) do better, and adjusting agreement levels can surpass non-debate protocols — i.e. debate is more sensitive to hyperparameters [VERIFIED: https://arxiv.org/abs/2311.17371, published 2023-11-29; arXiv preprint].
- **Wang et al.**: "a single-agent LLM with strong prompts can achieve almost the same performance" as the best multi-agent discussion; discussion beats a single agent "only when there is no demonstration in the prompt" [VERIFIED: https://arxiv.org/abs/2402.18272, published 2024-02-28; arXiv page shows no venue].
- **Choi, Zhu, Li**: decompose debate into voting plus inter-agent debate; voting explains most of the gain; they prove debate induces a martingale over belief trajectories, so "debate alone does not improve expected correctness"; biasing updates toward correction can help; "simple ensembling methods remain strong and more reliable alternatives in many practical settings" [VERIFIED: https://arxiv.org/abs/2508.17536, published 2025-08-24, rev. 2025-10-23; NeurIPS 2025 Spotlight].

**Durable vs volatile.** Durable: sampling several independent answers and aggregating them (voting, self-consistency) is a reliable, cheap-to-reason-about technique; argument between copies of one model adds cost without a reliable expected gain. Volatile: all accuracy numbers (2023 models, saturated benchmarks).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Where a design proposes "agents that debate", start with N independent samples and a deterministic aggregator (vote, or a verifier with external ground truth such as tests or a database). Self-critique without external feedback should not be counted as a control in a risk assessment.

---

## PART 6: Agent2Agent (A2A) protocol

### 6.1 Version and governance ⚠

| Date | Event | Source |
| --- | --- | --- |
| 2025-04 | Google launches A2A | AAIF post (below) |
| 2025-06-23 | Linux Foundation launches the A2A project at Open Source Summit North America; >100 supporting companies; vendor-neutral governance | LF press release |
| 2025-07-30 | v0.3.0: Agent Card well-known URI changed, `signatures` added to AgentCard | GitHub releases |
| 2026-03-12 | v1.0.0, first stable spec, many breaking changes | GitHub releases |
| 2026-04-09 | LF one-year release: >150 organisations; integrations in Azure AI Foundry, Copilot Studio, Amazon Bedrock AgentCore Runtime | LF press release |
| 2026-05-28 | v1.0.1 bug-fix release | GitHub releases |
| 2026-08-17 | A2A becomes a hosted project of the Agentic AI Foundation (AAIF) at the Linux Foundation | AAIF blog |
| 2026-10 | Spec site lists 1.0.0 as latest released spec version; Python SDK `a2a-sdk` 1.3.0 | spec site; PyPI |

- LF launch: A2A, created by Google and introduced in April, gets "a new home" at the Linux Foundation; more than 100 companies support it; SAP, ServiceNow and Cisco's Outshift describe themselves as founding contributors/partners/members; governance is "neutral, nonprofit, open-governance" [VERIFIED: https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents, published 2025-06-23].
- One-year release: version 1.0 is "the project's first stable specification", adding multi-protocol support, multi-tenancy and updated security flows; more than 150 supporting organisations, up from more than 50 in April 2025; Microsoft integrated A2A into Azure AI Foundry and Copilot Studio; AWS added support through Amazon Bedrock AgentCore Runtime [VERIFIED: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year, published 2026-04-09].
- Releases: v1.0.0 on 12 March 2026; v1.0.1 on 28 May 2026 [VERIFIED: https://github.com/a2aproject/A2A/releases, published 2026-03-12 / 2026-05-28].
- AAIF: A2A joins as a hosted project with over 150 backing organisations and its own Technical Steering Committee; AAIF projects listed: AGENTS.md, goose, MCP, agentgateway, A2A [VERIFIED: https://aaif.io/blog/a2a-joins-aaif, published 2026-08-17]. On 22 October 2026 AAIF announced four more projects (Agent Skills, Open Responses, OpenEnv, OpenSandbox), bringing it to 10 [WIDELY REPORTED: https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects, 2026].
- The spec site shows "Latest Released Version" 1.0.0 [VERIFIED: https://a2a-protocol.org/latest/specification/, n.d., accessed 2026-10]. [ASSUMPTION/JUDGEMENT] The SDK version (1.3.0) is independent of the spec version; do not conflate them.

### 6.2 What v1.0 specifies

- **Agent Card**: JSON metadata (identity, skills, endpoint, auth requirements) published at `/.well-known/agent-card.json` (IANA-registered); servers should use HTTPS; cards may be signed with JSON Web Signatures and clients should verify signatures when present; an authenticated extended card is available via `GetExtendedAgentCard` [VERIFIED: https://a2a-protocol.org/latest/specification/, n.d., accessed 2026-10].
- **Task lifecycle**: states SUBMITTED, WORKING, INPUT_REQUIRED, AUTH_REQUIRED, COMPLETED, FAILED, CANCELED, REJECTED; the last four are terminal; results belong in Artifacts rather than Messages; `contextId` groups tasks into a session [VERIFIED: same URL].
- **Bindings**: JSON-RPC, gRPC and HTTP+JSON/REST, plus custom bindings; streaming via Server-Sent Events; push notifications as server-initiated HTTP POSTs to a client webhook [VERIFIED: same URL].
- **Security**: security schemes cover API key, HTTP auth, OAuth 2.0, OpenID Connect and mutual TLS; authorization models are agent-defined; servers must check authorization on every operation and scope results to the caller [VERIFIED: same URL].
- **v1.0 breaking changes** include: OAuth implicit and password flows removed, device code and PKCE added; `v1` segment removed from HTTP URL bindings; ProtoJSON enum format; `FilePart`/`DataPart` flattened into `Part`; native multi-tenancy via a scope field; `tasks/list` with filtering and pagination [VERIFIED: https://github.com/a2aproject/A2A/releases, published 2026-03-12].
- **Opacity**: A2A describes agents as "potentially opaque AI agent systems" that collaborate "without needing access to each other's internal state, memory, or tools"; Opaque Execution is a guiding principle [VERIFIED: https://a2a-protocol.org/latest/specification/].
- **Relation to MCP** (spec Appendix B): complementary — MCP connects models and agents to tools and data; A2A lets independent agents discover each other, manage shared tasks and exchange results as peers; an A2A server may use MCP internally [VERIFIED: same URL].
- Microsoft Agent Framework at GA (April 2026) listed "A2A 1.0 support coming soon" [VERIFIED: https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/, published 2026-04-03]. ⚠ Current status not verified.

**Durable vs volatile.** Durable: discovery by published capability document, an explicit task state machine with input-required and auth-required states, long-running tasks with streaming and push, opacity between organisations, per-operation authorization. Volatile: field names, bindings, version number, foundation membership.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Use A2A at *organisational or trust boundaries* (another team's or vendor's agent you cannot inspect), not between components of your own system, where an in-process call or a durable workflow gives you shared tracing and transactional control.
- Opacity cuts both ways: the caller cannot see the callee's tools or reasoning, so accountability must be contractual (the Agent Card, signed; the task record; the Artifacts) and the caller must treat returned Artifacts as untrusted input.
- `INPUT_REQUIRED` and `AUTH_REQUIRED` are natural hooks for human approval and step-up authorization; design the oversight flow around them rather than in prompts.

---

## PART 7: Coordination costs — tokens, latency, shared state, accountability

### 7.1 Cost and latency

| Source | Measured | Number |
| --- | --- | --- |
| Anthropic research system | Tokens vs chat | Agents ~4×, multi-agent ~15× |
| Anthropic research system | Variance in BrowseComp performance | 80% explained by tokens; 95% with tool calls + model |
| Anthropic research system | Research time with parallelism | Up to 90% less |
| LLMCompiler | Latency / cost vs ReAct | Up to 3.7× faster / 6.7× cheaper (parallelisable tasks); slower on WebShop |
| ReWOO | Tokens on HotpotQA | 5× fewer |
| LangChain docs (example tasks) | Model calls per pattern | Stateful patterns ~40–50% fewer calls on repeat requests |
| Google scaling (blog) | Error amplification | 17.2× independent vs 4.4× centralised |

Sources as in the sections above.

- [ASSUMPTION/JUDGEMENT] Parallelism buys wall-clock time, not cost: the multi-agent research system is faster *and* about 15× more token-expensive than chat. Latency gains are capped by the serial planner and synthesis steps (LLMCompiler's 1.88 s + 1.62 s non-parallelisable overhead) and by stragglers.

### 7.2 Shared state and context transfer

| Mechanism | Example | Risk |
| --- | --- | --- |
| Full history handed over | OpenAI Agents SDK handoff default; LangGraph handoff tools default | Cost growth; untrusted content and sensitive data propagate; no redaction in nested history (beta) |
| Prompt-only delegation, summary back | Claude Agent SDK subagent; ADK task/single_turn branches | Lost decisions (Cognition); summary may drop evidence |
| Shared mutable state | ADK session state, CrewAI Flow state, LangGraph state | Races between parallel writers; implicit coupling |
| External memory / plan store | Anthropic LeadResearcher saving plan to Memory | Staleness; needs schema and ownership |

[VERIFIED for mechanisms: sources in Part 3 and 4.1.] [ASSUMPTION/JUDGEMENT for the risk column.]

### 7.3 Accountability

- [ASSUMPTION/JUDGEMENT] In a manager pattern, one agent (and its owning team) answers for the final output; in a handoff pattern, control moves and so does responsibility, so the trace must record which agent, with which tools and permissions, took each action. Claude SDK subagent messages carry `parent_tool_use_id` and (TypeScript) `agent_id` [VERIFIED: https://code.claude.com/docs/en/agent-sdk/subagents, n.d., accessed 2026-10], an example of the lineage metadata the book should require of any orchestration layer.
- [ASSUMPTION/JUDGEMENT] Across organisations (A2A), accountability is a contract: signed Agent Cards, task IDs and Artifacts are the evidence trail; neither side can audit the other's internals.

**Durable vs volatile (Part 7).** Durable: multi-agent multiplies tokens, adds serial coordination steps, and moves accountability unless lineage is recorded. Volatile: the multipliers themselves, which depend on model price and context size.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Budget per task tree (tokens, money, wall-clock, depth, fan-out), enforced by the runtime; one writer per artefact; explicit context contracts at each delegation boundary; lineage IDs on every action; a verifier stage between workers and any side effect.

---

## Key numbers

| Number | What it measured | Source | Date |
| --- | --- | --- | --- |
| +90.2% | Multi-agent (Opus 4 lead + Sonnet 4 subagents) vs single-agent Opus 4, internal research eval | Anthropic engineering post | 2025-06-13 |
| 80% / 95% | Share of BrowseComp performance variance explained by tokens / by tokens + tool calls + model | Anthropic | 2025-06-13 |
| ~4× / ~15× | Tokens used by agents / multi-agent systems relative to chat | Anthropic | 2025-06-13 |
| up to 90% | Reduction in research time for complex queries from parallelism | Anthropic | 2025-06-13 |
| 40% | Task completion time reduction after an agent rewrote tool descriptions | Anthropic | 2025-06-13 |
| 1,000–2,000 tokens | Typical size of a sub-agent's condensed return | Anthropic context-engineering post | 2025-09 |
| 14 modes / 3 categories | MAST failure taxonomy over 1,600+ traces, 7 frameworks | Cemri et al. (NeurIPS 2025 D&B) | 2025-03 (v3 2025-10) |
| κ = 0.88 | Human inter-annotator agreement for MAST | Cemri et al. | 2025-03 |
| 15.7% / 13.2% / 12.4% | Largest MAST modes: step repetition / reasoning–action mismatch / unaware of termination | Cemri et al. | 2025-03 |
| +9.4% / +15.6% | ChatDev task success from role/workflow fix / added objective verification (ProgramDev) | Cemri et al. | 2025-03 |
| +80.8% to −70.0% | Range of relative change vs single agent across 260 configurations, six benchmarks | Kim et al., arXiv v3 | 2026-04-08 |
| 17.2× / 4.4× | Error amplification, independent vs centralised multi-agent (180-config version) | Google Research blog | 2026-01-28 |
| 39–70% | Degradation of all multi-agent variants on PlanCraft (sequential planning) | Google Research blog | 2026-01-28 |
| 87% | Held-out configurations where predictive model chose best architecture | Kim et al. / Google blog | 2025-12 / 2026-01 |
| 5× / +4% | ReWOO token efficiency / accuracy on HotpotQA | Xu et al. (preprint) | 2023-05 |
| 3.7× / 6.7× / ~9% | LLMCompiler max latency speedup / cost saving / accuracy vs ReAct | Kim et al. (ICML 2024) | 2023-12 |
| 4% → 74% | Game of 24, GPT-4 CoT vs Tree of Thoughts | Yao et al. (NeurIPS 2023) | 2023-05 |
| 77.0 → 85.0 | GSM8K, single agent vs 3-agent 2-round debate, gpt-3.5 | Du et al. | 2023-05 |
| >15 vs <10 | Distinct tools some agents handle vs overlapping tools others fail on | OpenAI practical guide | 2025-04 |
| 3 / 20 / none | Claude Agent SDK default subagent depth / concurrency / spend cap | Claude Agent SDK docs | accessed 2026-10 |
| 1.0.0 (2026-03-12) | A2A first stable spec; 1.0.1 patch 2026-05-28 | A2A GitHub | 2026 |
| >150 | Organisations supporting A2A | LF press release; AAIF | 2026-04-09; 2026-08-17 |
| 2026-04-03 | Microsoft Agent Framework 1.0 GA (.NET and Python) | Microsoft DevBlogs | 2026-04-03 |

## Where sources disagree

- **Should you build multi-agent systems at all?** Anthropic (2025-06) reports large gains for research; Cognition (2025-06) says don't, for coding. Cognition (2026-04) now endorses manager–child delegation, clean-context review and read-only search, but still rejects parallel writers. Both agree that tasks with shared decisions (most coding) split badly. The disagreement is mostly about domain.
- **Why multi-agent helps.** Anthropic attributes most of the gain to spending more tokens (80% of variance). Google's scaling study attributes gains to task decomposability and the presence of a validating orchestrator. These are compatible but imply different designs: "more compute in parallel" versus "structure that matches the task".
- **Google scaling paper numbers.** The blog (2026-01) reports 180 configurations, four benchmarks, R² = 0.513 and +80.9% on Finance-Agent; arXiv v3 (2026-04) reports 260 configurations, six benchmarks, R² = 0.373 and +80.8%. The 17.2×/4.4× error-amplification figures were verified only on the blog.
- **Multi-agent debate.** Du et al. (2023) report debate beating single agents on every task; Smit et al., Wang et al. and Choi et al. find the gain mostly disappears against equal-budget self-consistency/voting or strong single-agent prompts. Choi et al. give a theoretical reason (martingale).
- **Context transfer default.** OpenAI and LangGraph handoffs pass full history by default; Claude subagents and ADK task branches pass only a prompt and return a summary. Cognition argues for full traces; Anthropic's context-engineering guidance argues for condensed 1,000–2,000-token returns. Neither is universally right; it depends on whether the sub-task depends on prior decisions.
- **AutoGen status.** The README contains both a "maintenance mode … bug fixes, security patches" line and an "archived … not providing bug fixes, security fixes" line; secondary sources date maintenance mode to October 2025. Treat AutoGen as unmaintained.
- **A2A 1.0 date.** Secondary blogs give March or April 2026; GitHub shows v1.0.0 on 2026-03-12, and the LF press release announcing it is dated 2026-04-09.

## Open questions / not verifiable

- No independent, reproducible benchmark of the Anthropic research system; the internal eval set (initially ~20 queries) is not public.
- Whether 2023 planning gains (ReWOO, ToT, LLMCompiler) persist with 2026 reasoning models that plan internally and call tools in parallel; no recent head-to-head found.
- Cost-per-solved-task for Tree of Thoughts was not verified.
- HuggingGPT's venue (widely cited as NeurIPS 2023) and Du et al.'s venue (widely cited as ICML 2024) were not confirmed on the arXiv pages fetched.
- MAST category-level percentages and the AG2 intervention numbers were not in the fetched text.
- Microsoft Agent Framework's current A2A 1.0 support status after GA was not checked.
- Exact publication date of Anthropic's context-engineering post (September 2025) was not shown in the fetched text.
- No public incident report attributing a production failure specifically to multi-agent coordination was found.
- Production adoption claims for A2A ("enterprise production use") come from the Linux Foundation's press release, not from operators.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Building effective agents | Erik S., Barry Zhang / Anthropic | 2024 | https://www.anthropic.com/engineering/building-effective-agents | engineering post |
| How we built our multi-agent research system | Anthropic | 2025 | https://www.anthropic.com/engineering/multi-agent-research-system | engineering post |
| Effective context engineering for AI agents | Anthropic | 2025 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | engineering post |
| Don't Build Multi-Agents | Walden Yan / Cognition | 2025 | https://cognition.com/blog/dont-build-multi-agents | engineering post |
| Multi-Agents: What's Actually Working | Walden Yan / Cognition | 2026 | https://cognition.com/blog/multi-agents-working | engineering post |
| A practical guide to building agents | OpenAI | 2025 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | vendor guide |
| Handoffs — OpenAI Agents SDK | OpenAI | n.d. | https://openai.github.io/openai-agents-python/handoffs/ | docs |
| Subagents in the SDK | Anthropic | n.d. | https://code.claude.com/docs/en/agent-sdk/subagents | docs |
| Multi-agent (LangChain docs) | LangChain | n.d. | https://docs.langchain.com/oss/python/langchain/multi-agent | docs |
| langgraph-supervisor-py README | LangChain | n.d. | https://github.com/langchain-ai/langgraph-supervisor-py | docs |
| langgraph-swarm-py README | LangChain | n.d. | https://github.com/langchain-ai/langgraph-swarm-py | docs |
| Planning Agents | LangChain | 2024 | https://www.langchain.com/blog/planning-agents | engineering post |
| ADK workflows | Google | n.d. | https://adk.dev/workflows/ | docs |
| ADK collaborative workflows | Google | n.d. | https://adk.dev/workflows/collaboration/ | docs |
| Microsoft Agent Framework Version 1.0 | Shawn Henry / Microsoft | 2026 | https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/ | press / engineering post |
| Workflow orchestrations in Agent Framework | Microsoft Learn | 2026 | https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview | docs |
| microsoft/agent-framework releases | Microsoft | 2026 | https://github.com/microsoft/agent-framework/releases | docs |
| microsoft/autogen README | Microsoft | n.d. | https://github.com/microsoft/autogen | docs |
| Migrate SK and AutoGen projects to Agent Framework RC | Microsoft | 2026 | https://devblogs.microsoft.com/agent-framework/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/ | engineering post (not fetched) |
| CrewAI Processes | CrewAI | n.d. | https://docs.crewai.com/en/concepts/processes | docs |
| CrewAI Flows | CrewAI | n.d. | https://docs.crewai.com/en/concepts/flows | docs |
| PyPI JSON metadata (openai-agents, claude-agent-sdk, langgraph, langgraph-supervisor, langgraph-swarm, google-adk, agent-framework, autogen-agentchat, crewai, a2a-sdk) | PyPI | 2026 | https://pypi.org/pypi/<package>/json | docs |
| Plan-and-Solve Prompting | Wang et al. | 2023 | https://arxiv.org/abs/2305.04091 | paper (ACL 2023) |
| ReWOO | Xu et al. | 2023 | https://arxiv.org/abs/2305.18323 | paper (preprint) |
| HuggingGPT | Shen et al. | 2023 | https://arxiv.org/abs/2303.17580 | paper (preprint; venue unconfirmed) |
| Tree of Thoughts | Yao et al. | 2023 | https://arxiv.org/abs/2305.10601 | paper (NeurIPS 2023) |
| An LLM Compiler for Parallel Function Calling | Kim et al. | 2023 | https://arxiv.org/abs/2312.04511 | paper (ICML 2024) |
| Why Do Multi-Agent LLM Systems Fail? | Cemri et al. | 2025 | https://arxiv.org/abs/2503.13657 | paper (NeurIPS 2025 D&B) |
| Towards a Science of Scaling Agent Systems | Kim et al. (Google, MIT) | 2025 | https://arxiv.org/abs/2512.08296 | paper (preprint) |
| Towards a science of scaling agent systems (blog) | Yubin Kim, Xin Liu / Google Research | 2026 | https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ | engineering post |
| Improving Factuality and Reasoning through Multiagent Debate | Du et al. | 2023 | https://arxiv.org/abs/2305.14325 | paper (preprint; venue unconfirmed) |
| Large Language Models Cannot Self-Correct Reasoning Yet | Huang et al. | 2023 | https://arxiv.org/abs/2310.01798 | paper (ICLR 2024) |
| Should we be going MAD? | Smit et al. | 2023 | https://arxiv.org/abs/2311.17371 | paper (preprint) |
| Rethinking the Bounds of LLM Reasoning | Wang et al. | 2024 | https://arxiv.org/abs/2402.18272 | paper (preprint) |
| Debate or Vote | Choi, Zhu, Li | 2025 | https://arxiv.org/abs/2508.17536 | paper (NeurIPS 2025) |
| A2A Protocol Specification | A2A Project / Linux Foundation | 2026 | https://a2a-protocol.org/latest/specification/ | spec |
| A2A releases | A2A Project | 2025–26 | https://github.com/a2aproject/A2A/releases | spec |
| Linux Foundation launches the Agent2Agent Protocol Project | Linux Foundation | 2025 | https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents | press |
| A2A protocol surpasses 150 organizations | Linux Foundation | 2026 | https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year | press |
| A2A joins AAIF | Agentic AI Foundation | 2026 | https://aaif.io/blog/a2a-joins-aaif | press |
| AAIF announces four new projects | Agentic AI Foundation | 2026 | https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects | press (not fetched) |
| NeurIPS 2025 poster: Why Do Multi-Agent LLM Systems Fail? | NeurIPS | 2025 | https://neurips.cc/virtual/2025/poster/121528 | conference listing (not fetched) |
| Cognition vs Anthropic (AINews issue) | smol.ai | 2025 | https://news.smol.ai/frozen-issues/25-06-13-cognition-vs-anthropic.html | press (not fetched) |
