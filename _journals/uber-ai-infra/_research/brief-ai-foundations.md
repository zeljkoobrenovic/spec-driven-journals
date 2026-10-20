# Research brief: Uber's AI foundations as documented publicly

Compiled 20 Oct 2026. Every URL below was fetched unless marked **(snippet only)**. Fetched pages were treated as data. Labels used:

- **CONFIRMED**: an Uber primary source (Uber blog, Uber-authored paper, Uber speakers at a talk) states it.
- **PARTLY CONFIRMED**: the mechanism is confirmed, but the podcast's number, date or name is not, or differs.
- **PODCAST-ONLY**: no public source found.

Podcast reference: "Uber's AI infra, from the inside", The Pragmatic Engineer, 14 Oct 2026, Gergely Orosz with Uday Kiran Medisetty (Distinguished Engineer), 1:33:17. [S1]

---

## 0. Headline numbers across sources (read this first)

Uber's own figures move between sources because they are snapshots taken months apart, and some define the metric differently. Always cite the source and date with a number.

| Metric | Value | Source, date |
| --- | --- | --- |
| PRs opened by agents | 11% | Pragmatic Engineer, Mar 2026 [S3]; Background Agents Summit, 7 May 2026 [S16] |
| PRs attributed to local or cloud agents | >70% | AI Engineer World's Fair talk [S13]; Uber blog, 27 Aug 2026 [S2] |
| Agentic coding users | 84% of devs (Mar 2026); 92% use agents monthly | [S3] |
| Engineers using AI tooling monthly | >90% of 5,000+ engineers | AAIF/MCP Dev Summit, 14 May 2026 [S15] |
| AI-related costs | up 6x since 2024 | [S3] |
| Cost per session | down 52% from June peak to August (model held constant) | [S2] |
| Cost per 1,000 model requests | down almost 34% from peak, Feb to Jul | [S2] |
| Token cost "about 50% lower in recent months" | **closest match is [S2]'s 52% cost-per-session drop**; no source states a 50% fleet-wide token reduction | [S1] vs [S2] |

---

## 1. Michelangelo (the ML platform underneath)

**Facts**
- Introduced publicly on 5 Sept 2017 ("Meet Michelangelo", Mike Del Balso and Jeremy Hermann). Six-step workflow: manage data, train, evaluate, deploy, predict, monitor. Feature store of about 10,000 features. P95 serving latency under 5 ms (under 10 ms with Cassandra features). Top models serve >250,000 predictions/s. Built on HDFS, Spark, Samza, Cassandra, MLlib, XGBoost, TensorFlow. [S4]
- "From Predictive to Generative" (2 May 2024; Kai Wang, Joseph Wang, Min Cai) divides history into Michelangelo 1.0 (2016–2019, tabular ML, Palette feature store with 20,000+ features), 2.0 (2019–2023, deep learning; >60% of tier-1 models use DL; Canvas, MA Studio) and Generative AI (2023 on). Scale: ~400 active ML projects, >20K training jobs/month, >5K production models, 10M real-time predictions/s at peak, 5,000+ GPUs. [S5]
- GenAI layer on Michelangelo (2024): Gen AI Gateway, Model Catalog (GPT-4, PaLM, Llama 2), LLM Evaluation Framework, Prompt Engineering Toolkit (versioned templates with code review), Ray-based fine-tuning with Hugging Face, PEFT and DeepSpeed. Ray replaced Spark trainers; Kubernetes replacing Peloton/Mesos; Triton replacing Neuropod. [S5]
- **Open-sourced 20 May 2026** ("Michelangelo is Now Open Source", Michelangelo team). Released: Uniflow (pipeline framework), API server, controller, local sandbox (`ma sandbox create`), CLI; runs on a laptop or an existing Kubernetes cluster. [S6]
- GitHub `michelangelo-ai/michelangelo`: Apache-2.0, README says "currently in beta", breaking changes possible, ~129 stars when fetched, no tagged releases. A separate `michelangelo-ai/enhancements` repo hosts public RFCs (internal ERD first, then public RFC). [S7]
- The agent identity post says agents are **registered through the Michelangelo platform**. [S8]

**Podcast claims**
- Model Gateway "built late 2023 on Michelangelo": **PARTLY CONFIRMED.** Genie (launched Sept 2023) already logged LLM usage through "Michelangelo Gateway" [S11], and [S5] dates Michelangelo's GenAI phase from 2023. The first dedicated public write-up is July 2024 [S9]. No source gives "late 2023" as a build date.

---

## 2. Model Gateway / GenAI Gateway / AI Gateway (and AI Guard)

The same system appears under four names: "GenAI Gateway" (2024 blog), "Michelangelo Gateway" (Genie post), "AI Gateway" (agent identity post), "Model Gateway" (AI Engineer talk and podcast). Treat them as one lineage; say so in the journal.

**Facts (2024)** [S9] "Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway", 11 July 2024, Tse-Chi Wang and Roopansh Bansal.
- Go service; **mirrors the OpenAI HTTP/JSON API**, so OpenAI-style clients reach other vendors. Supports Python, Java, Go clients.
- Vendors: OpenAI, Google Vertex AI (Uber wrote and open-sourced `go-vertex-ai`), and Uber-hosted models (e.g. llama-2-70b-chat-hf).
- **PII redaction**: a redactor swaps PII for numbered placeholders (e.g. `ANONYMIZED_NAME_0`), keeps a mapping, and un-redacts the vendor response before returning it. The post admits redaction costs latency and some quality, with no figures.
- Authn/authz, metrics, audit logs (cost attribution, security audit, quality evaluation), budgeting. Each use case passes an Engineering Security review against the data-handling standard before access.
- Scale then: 60+ LLM use cases, ~30 customer teams, ~16M queries/month, peak 25 QPS.

**Facts (2026)**
- AI Engineer World's Fair talk (Medisetty and Adam Huda): single **OpenAI/Anthropic-compatible** endpoint, SPIRE identity, data anonymizer, AI guard; **>20 PII types redacted, 5 specialized safety/policy models, middleware <100 ms**; **800+ internal projects, >100M model requests/day**. [S13] (Port's summary [S14] repeats these.)
- Agent identity post (21 May 2026): the AI Gateway mediates outbound calls to OpenAI and Anthropic, with **AI Guard** handling prompt injection, jailbreaks and PII redaction. [S8]
- RSAC 2026 session "AI Guard: Securing LLMs, Agents and AI Applications at Uber Scale" (speaker Junyan Guo, Staff SWE): centralized platform intercepting LLM traffic; prompt injection/jailbreak, content safety, PII redaction, terminology/policy checks; lessons on latency and failure coupling; shadow-mode rollout, flagged-rate alerting, parallel rail execution across CPU/GPU models. **(snippet only: the RSAC pages returned 403 or an empty agenda)** [S20]
- Model choice is benchmark-driven and Pareto-efficient on the internal **Uber SWE Benchmark**; subagents default to a cheaper model. [S2]

**Podcast claims**
- OpenAI/Anthropic-compatible API: **CONFIRMED** (OpenAI 2024 [S9]; Anthropic 2026 [S13]).
- All model requests go through it: **CONFIRMED** by [S13]/[S14] ("every model call, internal and external").
- AI Guard as security-team middleware: **CONFIRMED** as a guard layer [S8][S13]; "security team" ownership is not stated publicly.
- ~5 fine-tuned models on every request/response: **PARTLY CONFIRMED.** "5 specialized safety/policy models" [S13]; "fine-tuned" is not stated anywhere public.
- Latency guardrails: **CONFIRMED in spirit** (<100 ms middleware [S13]; RSAC latency hardening [S20]). The podcast summary describes AI Guard as also flagging slow models [S1]; that part is podcast-only.

---

## 3. Spend controls, CostCheck and token-cost reduction

**Facts** [S2] "Running a Software Factory Efficiently at Uber Scale", Uber blog, 27 Aug 2026, Uday Kiran Medisetty. (A search snippet showed 13 Oct 2026; the fetched page says 27 Aug 2026. Use 27 Aug.)
- Cost equation: users × sessions/user × turns/session × requests/turn × tokens/request × price/token.
- **Spend tiers**: one shared tier for all interactive harnesses, separate tiers for managed agents; **manager sign-off to move up a tier**; Slack nudges at 50%, 80%, 100% of expected spend; live cost counter in the harness status line.
- A **"cost check skill"** gives on-demand cost breakdowns and status-line tips. A session-analysis dashboard flags 16 anti-patterns (e.g. simple sessions on Opus, 40 KB MCP payloads, expired caches after breaks, 100K-token prompt initialization). Example dashboard: $4,162.07 over 433 sessions, 95% cache hit rate, $1,213.87 saved.
- Defaults: auto-compaction at 400K tokens even on 1M-context models; reasoning effort Medium; interactive sessions moved from 5-minute to 1-hour prompt-cache TTL (subagents stay at 5 min). Cache read 0.1x, 5-min write 1.25x, 1-h write 2x input price.
- Results (model held constant): cost per 1,000 requests down ~34% from peak (Feb–Jul); **cost per session down 52% from the June peak (to Aug)**; total AI spend roughly stable since April while weekly active agentic users grew 7x and weekly agentic requests 9.4x (Feb–Aug 2026).
- Bloomberg (2 June 2026, Natalie Lung): Uber caps **$1,500 per employee per month per agentic coding tool** (Cursor, Claude Code), spend on one tool not counting against another, after it "blew through its AI budget earlier this year". [S18]
- eeNews Europe (28 May 2026): the 2026 AI budget was reportedly exhausted within months; COO Andrew Macdonald said the link between more tokens and better consumer features is not yet clear. [S19]
- Axios exclusive (27 Aug 2026): Uber cut AI costs while usage rose; >30,000 agent tasks/day; users more than quadrupled; per-task model routing; 400K session cap; terminal cost display; 1-hour cache; CTO cites open-weight models. **(snippet only: 403 on fetch)** [S21]

**Podcast claims**
- Per-user spend tiers with manager approval: **CONFIRMED** [S2].
- CostCheck plugin: **PARTLY CONFIRMED.** [S2] calls it a "cost check skill"; the podcast page calls it a cross-session plugin [S1]. Naming differs.
- ~50% token cost reduction: **PARTLY CONFIRMED.** Nearest public figure is the 52% cost-per-session drop [S2]; the talk cites ">40% fleetwide savings" tied to the MCP/code-mode work [S13][S14]. Code mode cut tokens per SQL query by 55–71% [S2]. No source gives one 50% fleet-wide token number.
- **Contradiction to flag:** Bloomberg's per-tool $1,500 cap (June) vs [S2]'s single shared tier across interactive harnesses (Aug). This is probably a policy change between June and August, but no source says so.

---

## 4. AIFX ("AI Foundations" CLI / harness wrapper)

**Facts**
- Pragmatic Engineer (10 Mar 2026): the AIFX CLI provisions AI clients, discovers MCP servers, runs background tasks and updates tools. [S3]
- AAIF write-up of the MCP Dev Summit NA 2026 talk (14 May 2026): coding agents (Claude Code, Cursor, Minions) add MCP servers through the AIFX CLI. [S15]
- MCP Gateway blog (1 Oct 2026): "Code Mode" routes MCP calls through `aifx`, "Uber's CLI", with `aifx mcp list`, `aifx mcp search`, `aifx mcp call`; output can go to files; now the company default for MCP use in coding agents. [S10]
- "AI Foundations" is a real Uber team name: Will Bond (Staff Engineer, AI Foundations) co-authored uReview [S12]; Nikhil Ramakrishnan's title is "AI Foundations & Developer Experience" [S16]. Reading AIFX as "AI Foundations" plus Uber's "-Fx" framework suffix (as in MCPFx) is an inference; no public source spells it out.
- AI Engineer talk: managed skills ship with persona-based defaults [S13]. That is close to the podcast's "personas" but is described for skills, not for AIFX.

**Podcast claims**
- Wrapper over Claude Code, Codex, OpenCode that carries settings, skills and plugins across harness switches: **PODCAST-ONLY** (public sources show AIFX as a provisioning/MCP CLI, not explicitly a multi-harness wrapper). Claude Code, Codex and Copilot as external tools are confirmed [S3].
- Personas, synced settings, status line: status-line cost counter **CONFIRMED** [S2] (the harness is not named); personas and settings sync are **PODCAST-ONLY** for AIFX.
- `aifx validate` (inner-loop checks before a PR): **PODCAST-ONLY.** Note the podcast page spells it `afx validate` [S1].

---

## 5. MCP Gateway

**Facts** [S10] "Designing MCP Gateway: Uber's MCP Management Platform", Uber blog, 1 Oct 2026, Alok Srivastava, Deepanshu Mehndiratta, Gaurav Gill.
- **800+ MCP servers, 5,000+ tools.**
- Control plane: MCP Registry (discovery, ownership, enablement). Data plane: Proxy Gateway translating MCP to HTTP, gRPC or TChannel and back; one `/<service-name>/mcp` endpoint per virtual server; config refresh without restarts; downstream calls through Muttley (service-mesh sidecar).
- **AutoCrawler**: a cron-triggered Cadence workflow watches the IDL registry, parses Protobuf/Thrift (method names, schemas, doc comments), has an **LLM write agent-friendly tool descriptions**, converts schemas to MCP JSON-RPC 2.0, upserts into the registry. Native MCP servers are built with **MCPFx** and detected by heartbeat metrics. Everything is registered **disabled by default**; owners must review and enable; description edits create a config diff owners approve, with rollback.
- Security: tool-level authorization via Uber's Access Control System (server-level charter policies, tool-level overrides; callers are humans, services or agents); out-of-the-box PII redaction in responses.
- Third-party MCPs (examples: Jira, Google): the gateway relays the user token, enforces authz, rate limits and redaction; a service exchanges the internal token for the third-party token.
- Context efficiency: **Omni MCP** (`discover_server`, `discover_tools`, `get_tool_schema`, `invoke_tool`); **Response Projection** (GraphQL-like field paths trim responses); **Code Mode** through `aifx` CLI.
- [S2]: 1,000+ MCP servers behind the gateway; standard MCP loading cost 50K–70K tokens of schema with 100+ tools; all 1K+ internal MCP tools exposed as CLI commands; 25+ code-mode skills; SaaS schema examples: workspace suite 49 tools (~22K tokens), messaging 34, project tracking 46.
- [S15] (AAIF, 14 May 2026; speakers Meghana Somasundara and Rush Tehrani): ~60,000 agent executions/week, 1,500+ agents active monthly, 10,000+ internal services, LLM turns 10,000+ proto/thrift IDLs into tool descriptions; auth on by default for sensitive data; PII redactor on outputs; code scanning; guardrails block writes to critical services; third-party MCPs gated more strictly. Consumers: Uber Agent Builder (no-code), Uber Agent SDK (YAML), coding agents via AIFX. Roadmap: evals and SLAs in the registry, a tool-search MCP, a Skills Registry with A/B tests of skill versions.
- [S8]: Uber built an internal Agent platform in early 2025 and made its microservices MCP-ready; MCP Gateway is a policy enforcement point (verifies tokens, tool-level access, redaction). [S3]: MCP strategy and gateway built by a temporary "tiger team".

**Podcast claims**
- April 2025 start: **PARTLY CONFIRMED.** "Early 2025" agent platform [S8] and the tiger team [S3] fit; no source gives April 2025.
- Auto-generated MCP servers from the Thrift/Protobuf IDL registry, LLM-optimized descriptions: **CONFIRMED** [S10][S15].
- Vendor tools (Google, Slack) proxied: **CONFIRMED** for Jira and Google [S10]; Slack is implied by "messaging" in [S2] but not named.
- MCPs projected as CLIs: **CONFIRMED** [S2][S10][S13].
- **Count contradiction:** 800+ servers / 5,000+ tools [S10, Oct 2026] vs 1,000+ servers [S2, Aug 2026] vs 1,000+ tools [S13/S14]. Don't merge these.

---

## 6. Agent Skills monorepo

**Facts**
- [S2] (27 Aug 2026): **3,600+ agent skills, 30K+ skill executions/day.**
- [S13] (World's Fair talk): managed skills marketplace, core and domain skills, lint and automated review, persona-based defaults, feedback loops, scheduled maintenance skills (e.g. feature-flag cleanup); **2,500 skills, >20,000 executions/day** (an earlier snapshot).
- [S15]: Skills Registry with output evaluation and A/B testing on the roadmap (May 2026).
- [S2]: 25+ pre-built code-mode skills; next steps include automated skill updates.

**Podcast claims**
- ~30,000 skill executions/day: **CONFIRMED** [S2].
- Monorepo layout: **PODCAST-ONLY** (sources say "marketplace" or "registry", not where skills are stored).
- Evals: **PARTLY CONFIRMED** (lint, automated review, feedback loops [S13]; evaluation and A/B testing planned [S15]).
- Trace-driven improvement: **PARTLY CONFIRMED** (session-trace anti-pattern dashboard [S2]; skill feedback loops [S13]); "skills improved from traces" is not stated.

---

## 7. Context Graph and Cortana

**Facts**
- [S2]: **AI Context Graph of 24M nodes and 80M edges, 86 node types and 117 edge types, from 30+ internal systems.** In one example a graph-grounded query took 38 s and was correct; ungrounded it took 20 m 09 s and was wrong.
- [S13]: shared graph linking code, design docs, data, Jira and incidents; **150 node and edge types, ~40M entries**, replacing lookups across 20–30 systems. **Cortana**: internal assistant in Slack, CLI and web; **300 personas created in the prior month, >20,000 sessions/day**.
- [S8] (agent identity): tokens carry an actor chain (e.g. `[user1, oncall-agent, investigation-agent]`); single-hop, audience-scoped, short-lived; STS P99 <40 ms; based on OAuth 2.0 Token Exchange (RFC 8693); Agent Registry plus SPIRE SVIDs. This is the public mechanism behind "acting with the user's permissions".
- Related earlier work: Neo4j GraphSummit NYC 2025 talk on Uber's config knowledge graph with GraphRAG and MCP (Vignesh Murugesan). **(snippet only)**

**Podcast claims**
- 100+ node types, 130+ edge types: **CONTRADICTED in detail.** [S2] says 86 node / 117 edge types; [S13] says 150 combined. Three different snapshots; none matches the podcast.
- Cortana on Slack/web/CLI: **CONFIRMED** [S13].
- Permission-preserving: **PARTLY CONFIRMED** via the actor-chain identity design [S8] and user-token relay in MCP Gateway [S10]; no source says this of Cortana specifically.

---

## 8. Earlier GenAI developer tools (context for the journal)

| Tool | Source, date | Key facts |
| --- | --- | --- |
| **Genie** (on-call copilot) | Uber blog, 10 Oct 2024; Marcott, Sidorovics, Chothani [S11] | Launched Sept 2023; ~45,000 questions/month in Slack support channels; RAG over Engwiki, internal Stack Overflow, requirement docs; Spark ETL, LangChain chunking, OpenAI embeddings, Sia vector DB, Terrablob; usage logged via Michelangelo Gateway; 154 channels, 70,000+ questions, 48.9% helpfulness, ~13,000 engineering hours saved. |
| **Enhanced Agentic RAG** | Uber blog, 29 May 2025; Chakraborty, Settles, Raghavendra [S17] | Query Optimizer and Source Identifier agents before retrieval, Post-Processor after; vector + BM25 hybrid; 100+ SME golden queries over 40+ policy docs; LLM-as-judge 0–5; **+27% acceptable answers, −60% incorrect advice** (relative); built on **Langfx** (Uber's LangChain-based service in Michelangelo) and LangGraph. |
| **QueryGPT** | Uber blog, 19 Sept 2024; Johnson, Busch, Khune [S22] | Began at Generative AI Hackdays May 2023; 20+ iterations; intent, table and column-prune agents; workspaces; ~1.2M interactive queries/month (36% Operations); ~10 min to ~3 min per query; ~300 DAU in limited release; 78% said it saved time. |
| **uReview** | Uber blog, 12 Aug 2025; Mahajan, Roy Choudhary, Bond [S12] | Prompt chain: generate, filter, validate, dedupe; Standard, Best Practices, AppSec assistants; best setup Claude-4-Sonnet generator + o4-mini-high grader; >90% of ~65,000 weekly diffs; 75% of comments rated useful, >65% addressed (humans' comments 51%); median 4 min; six monorepos; ~1,500 dev-hours/week saved (estimate); Uber uses Phabricator. Note: the post also says "65,000 diffs per month" once (internal inconsistency). |
| **AutoCover** | ICSE 2026 SEIP paper, 15 Apr 2026; Rastenis, Chou, Roy Choudhary, Just; Distinguished Paper [S23] | LangGraph multi-agent pipeline (prepare, generate, execute, validate/repair); CLI, Headless and IDE modes; coverage-delta and mutation gates, multi-run flakiness checks; ~11% of new tests landed; baseline: median 4 min per covered line. Pragmatic: 5,000+ unit tests/month [S3]. |
| **Validator / Lang Effect** | LangChain Interrupt 2025 (Shirhatti, Rastenis), via ZenML summary [S24] | Validator: IDE LangGraph agent mixing LLM best-practice checks with deterministic linting; thousands of daily fix interactions; ~21,000 dev-hours saved (AutoCover); framework named "Lang Effect" here vs "Langfx" in [S17]. Likely the same thing (LangFX); flag the spelling. |
| **FixrLeak** | Uber blog, 1 May 2025; Sridharan, Zhang, Utture [S25] | SonarQube leaks + Tree-sitter AST checks + GenAI (e.g. GPT-4o) fixes favouring try-with-resources; 124 leaks found, 102 eligible, 93 fixed (~91%); build, tests and SonarQube recheck before a one-click-accept PR. |
| **DragonCrawl** | Uber blog, 23 Apr 2024; Zamani, Hira, Marcano [S26] | LLM mobile-test agent on MPNet-base (~110M params); 99%+ stability Nov–Dec 2023; trips completed in 85 of 89 cities; blocked 10 high-priority bugs in first 3 months. |
| **Minion** (background agent) | Background Agents Summit, 7 May 2026 (Nikhil Ramakrishnan) [S16]; AAIF [S15]; Pragmatic [S3] | Lineage container prototype → DevPod → Minion; 11% of merged PRs; ~1,800 code changes/week, used by 95% of engineers [S15]; draft PRs [S13]. |
| **Agent Builder / Agent Studio / Agent SDK** | [S3][S15] | No-code agent creation with thousands of monthly active agents; Agent Studio traces and evaluates multi-agent workflows; YAML-configured SDK for production agents. |

Talks found for 2024–2026: AI Engineer World's Fair 2026 [S13]; MCP Dev Summit NA 2026 [S15]; Background Agents Summit May 2026 [S16]; LangChain Interrupt 2025 [S24]; Pragmatic Summit (Ty Smith, Anshu Chada) [S3]; RSAC 2026 AI Guard [S20]; AI/ML Infra Meetup Nov 2025 on open-sourcing Michelangelo (snippet only). **No Uber QCon/InfoQ talk on this stack was found**; InfoQ covered Genie (Oct 2024) and the GenAI Gateway as news.

---

## 9. Pragmatic Engineer, "How Uber uses AI for development: inside look"

[S3] Gergely Orosz, 10 Mar 2026 (updated 11 Mar); from the Pragmatic Summit talk by Ty Smith (Principal Engineer) and Anshu Chada (Director, Dev Platform). Paywalled after section 4.
- 84% of devs are agentic coding users; 65–72% of IDE code is AI-generated; Claude Code usage 32% (Dec) → 63% (Feb) while Cursor/IntelliJ plateaued.
- 92% use agents monthly; 11% of PRs opened by agents; AI costs up 6x since 2024; ~3,000 people in tech.
- Tools: Michelangelo as base, MCP Gateway (auth, telemetry, logging, registry, sandbox), Uber Agent Builder + Agent Studio, AIFX CLI, Minion, Code Inbox, uReview, Autocover (5,000+ tests/month), Shepherd.
- Built the MCP strategy via a temporary tiger team; parallel background agents create cost pressure.
- It does **not** state a 50% token-cost reduction (the visible part).

---

## 10. General pattern references

- **Model Context Protocol** [S27][S28]: JSON-RPC 2.0; hosts, clients, servers; server features Resources, Prompts, Tools; client features Sampling, Roots, Elicitation. **Current revision is 2026-07-28** (date-based versions; per-request version in `_meta`, `server/discover` RPC; handshake revisions 2025-11-25 and earlier remain for backward compatibility). Security principles: user consent, data privacy, tool descriptions untrusted unless from a trusted server.
- **Anthropic Agent Skills** [S29][S30]: a skill is a folder with `SKILL.md` (YAML `name` ≤64 chars and `description` ≤1024 chars); progressive disclosure: metadata ~100 tokens/skill always loaded, body <5k tokens on trigger, bundled files and scripts loaded as needed. Claude Code skills live in `~/.claude/skills/` or `.claude/skills/`. The format was developed by Anthropic and released as an open standard at agentskills.io, supported by Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot and others.
- **AGENTS.md** [S31]: "a README for agents"; stewarded by the Agentic AI Foundation under the Linux Foundation; 60k+ open-source projects; nearest file in the tree wins, explicit user prompts override; supported by Codex, Jules, Gemini CLI, Cursor, opencode, Copilot coding agent and others.

---

## Gaps and open questions

1. No public source for: AIFX as a multi-harness wrapper with synced settings and personas; `aifx validate`; skills stored in a monorepo; "fine-tuned" AI Guard models; the April 2025 MCP Gateway date; a single "50% token cost" figure.
2. Context-graph type counts disagree three ways (podcast 100+/130+; blog 86/117; talk 150 combined).
3. MCP server/tool counts disagree (800+/5,000+ vs 1,000+ servers vs 1,000+ tools).
4. Agent-PR share: 11% (Mar–May 2026) vs >70% (Aug 2026), with different definitions.
5. Spend policy: per-tool $1,500 cap (Bloomberg, June) vs one shared interactive tier (Uber, Aug).
6. Axios (27 Aug 2026) and RSAC AI Guard pages could not be fetched; facts from them are snippet-level.
7. No Uber blog post yet on AIFX, Cortana, the Context Graph or Minion specifically.

---

## Sources

| ID | Title | URL | Date | Author(s) | Fetched |
| --- | --- | --- | --- | --- | --- |
| S1 | Uber's AI infra, from the inside (podcast page) | https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside | 14 Oct 2026 | Gergely Orosz; guest Uday Kiran Medisetty | yes |
| S2 | Running a Software Factory Efficiently at Uber Scale | https://www.uber.com/us/en/blog/efficient-software-factory/ | 27 Aug 2026 | Uday Kiran Medisetty | yes |
| S3 | How Uber uses AI for development: inside look | https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development | 10 Mar 2026 | Gergely Orosz (talk by Ty Smith, Anshu Chada) | yes (partial, paywall) |
| S4 | Meet Michelangelo: Uber's Machine Learning Platform | https://www.uber.com/blog/michelangelo-machine-learning-platform/ | 5 Sept 2017 | Mike Del Balso, Jeremy Hermann | yes |
| S5 | From Predictive to Generative – How Michelangelo Accelerates Uber's AI Journey | https://www.uber.com/blog/from-predictive-to-generative-ai/ | 2 May 2024 | Kai Wang, Joseph Wang, Min Cai | yes |
| S6 | Michelangelo is Now Open Source | https://michelangelo-ai.org/blog/open-source-launch/ | 20 May 2026 | The Michelangelo Team | yes |
| S7 | michelangelo-ai/michelangelo (GitHub) | https://github.com/michelangelo-ai/michelangelo | n/a | Uber | yes |
| S8 | Solving the Identity Crisis for AI Agents | https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/ | 21 May 2026 | Matt Mathew, Prasad Borole, Meng Huang | yes |
| S9 | Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway | https://www.uber.com/blog/genai-gateway/ | 11 July 2024 | Tse-Chi Wang, Roopansh Bansal | yes |
| S10 | Designing MCP Gateway: Uber's MCP Management Platform | https://www.uber.com/blog/designing-mcp-gateway/ | 1 Oct 2026 | Alok Srivastava, Deepanshu Mehndiratta, Gaurav Gill | yes |
| S11 | Genie: Uber's Gen AI On-Call Copilot | https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/ | 10 Oct 2024 | Nicholas Marcott, Eduards Sidorovics, Paarth Chothani | yes |
| S12 | uReview: Scalable, Trustworthy GenAI for Code Review at Uber | https://www.uber.com/blog/ureview/ | 12 Aug 2025 | Sonal Mahajan, Shauvik Roy Choudhary, Will Bond | yes |
| S13 | Agentic SDLC at Uber: Building Blocks for Uber's Software Factory (AI Engineer World's Fair 2026) | https://ai.engineer/talks/17-YSUHo6Lk-agentic-sdlc-at-uber-building-blocks-ubers | 2026 (exact date not on page) | Uday Kiran Medisetty, Adam Huda | yes |
| S14 | How Uber built an AI software factory for agentic coding (Port newsletter; vendor-published summary of S13) | https://newsletter.port.io/p/how-uber-built-a-software-factory | 24 Aug 2026 | Zohar Einy | yes |
| S15 | How Uber Runs 60,000 AI Agent Tasks Per Week With MCP (AAIF) | https://aaif.io/blog/how-uber-runs-60000-ai-agent-tasks-per-week-with-mcp | 14 May 2026 | Agentic AI Foundation (talk by Meghana Somasundara, Rush Tehrani) | yes |
| S16 | Inside Uber's agent-ready platform behind 11% of merged PRs (Background Agents Summit) | https://background-agents.com/summit/sessions/nikhil-ramakrishnan/ | 7 May 2026 | Nikhil Ramakrishnan | yes |
| S17 | Enhanced Agentic-RAG: What If Chatbots Could Deliver Near-Human Precision? | https://www.uber.com/blog/enhanced-agentic-rag/ | 29 May 2025 | Arnab Chakraborty, Christopher Settles, Adi Raghavendra | yes |
| S18 | Uber Caps Usage of AI Tools Like Claude Code to Manage Costs | https://news.bgov.com/artificial-intelligence/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs-1 | 2 June 2026 | Natalie Lung (Bloomberg) | yes (excerpt) |
| S19 | AI token costs force rethink at Uber and Microsoft | https://www.eenewseurope.com/en/ai-token-costs-uber-microsoft-goldman/ | 28 May 2026 | Brian Tristam Williams | yes |
| S20 | AI Guard: Securing LLMs, Agents and AI Applications at Uber Scale (RSAC 2026) | https://www.rsaconference.com/Library/presentation/USA/2026/AI%20Guard%20Securing%20LLMs%20Agents%20and%20AI%20Applications%20at%20Uber%20Scale | Mar 2026 | Junyan Guo | **no (403; snippet only)** |
| S21 | Exclusive: Uber cuts AI costs even as usage jumps (Axios) | https://axios.com/2026/08/27/ai-uber-spending | 27 Aug 2026 | Axios | **no (403; snippet only)** |
| S22 | QueryGPT – Natural Language to SQL Using Generative AI | https://www.uber.com/blog/query-gpt/ | 19 Sept 2024 | Jeffrey Johnson, Callie Busch, Abhi Khune | yes |
| S23 | Automated Software Test Generation at Industry Scale Using a Multi-Agent Architecture and Workflow Integration (ICSE 2026 SEIP) | https://conf.researchr.org/details/icse-2026/icse-2026-software-engineering-in-practice/58/Automated-Software-Test-Generation-at-Industry-Scale-Using-a-Multi-Agent-Architecture | 15 Apr 2026 | Matas Rastenis, Ben Chou, Shauvik Roy Choudhary, René Just | yes |
| S24 | Building AI Developer Tools Using LangGraph for Large-Scale Software Development (ZenML summary of LangChain Interrupt 2025 talk) | https://www.zenml.io/llmops-database/building-ai-developer-tools-using-langgraph-for-large-scale-software-development | 2025 | ZenML (talk: Sourabh Shirhatti, Matas Rastenis) | yes (secondary) |
| S25 | FixrLeak: Fixing Java Resource Leaks with GenAI | https://www.uber.com/blog/fixrleak-fixing-java-resource-leaks-with-genai/ | 1 May 2025 | Manu Sridharan, Chris Zhang, Akshay Utture | yes |
| S26 | DragonCrawl: Generative AI for High-Quality Mobile Testing | https://www.uber.com/blog/generative-ai-for-high-quality-mobile-testing/ | 23 Apr 2024 | Ali Zamani, Anam Hira, Juan Marcano | yes |
| S27 | MCP Specification (2025-06-18 revision) | https://modelcontextprotocol.io/specification/2025-06-18 | 2025-06-18 | MCP project | yes |
| S28 | MCP Versioning | https://modelcontextprotocol.io/specification/versioning | current rev 2026-07-28 | MCP project | yes |
| S29 | Agent Skills overview (Claude docs) | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | n/a | Anthropic | yes |
| S30 | Agent Skills open standard | https://agentskills.io/ | n/a | agentskills.io (originated by Anthropic) | yes |
| S31 | AGENTS.md | https://agents.md/ | n/a | Agentic AI Foundation / LF Projects | yes |
