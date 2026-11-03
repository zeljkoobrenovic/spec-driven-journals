# Research brief: Performance, economics and evolution of agentic systems

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief covers two chapters' worth of evidence. The first part is about what an agent loop costs and how long it takes: prompt caching, batch and priority tiers, token growth in loops and multi-agent systems, routing and cascades, parallel and speculative execution, latency components and rate limits. The second part is about how an agentic system survives change: model retirement, version pinning, behavior drift, two dated vendor postmortems, ML technical debt, canary and shadow releases, flags and configuration-as-code for prompts, and who owns all of it. The brief is vendor-neutral. Anthropic, OpenAI and Google get the most space because their pricing, lifecycle and incident documents are public and dated, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date. Vendor documentation is usually undated or continuously edited; it is tagged "n.d., accessed 2026-10" or with the "last updated" date the page shows.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (a well-known commentator quoting the primary text, a journal index, a press summary), not read at the primary source in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including all worked arithmetic. Chapter writers should present these as reference-architecture judgement, not as findings.

**Evidence age matters.** This field changes in months. The model names in this brief (Claude Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1; GPT-5.6 Sol/Terra/Luna and GPT-6.1; Gemini 4 Argon and 3.8 Flash) are the ones the vendors' own pages listed on 28 October 2026. Several of the papers are from 2023–2024 and measured models that are now retired (GPT-3.5, GPT-4 March/June 2023, Claude Sonnet 3.7, Claude Opus 4). Their mechanisms are still useful; their numbers describe superseded models. Each section says how old its evidence is. A source older than about 18 months is flagged.

**Pricing is volatile.** ⚠ Every price, multiplier, TTL, minimum length and rate limit in this brief is a snapshot of 28 October 2026. Prices do not only fall: Google's pricing page already schedules a doubling of Gemini 4 Argon prices from 1 December 2026 and of Gemini 3.8 Flash from 1 January 2027 (§1.3). Chapters should state ratios and mechanisms in the body and keep absolute dollar figures in dated tables or footnotes.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: prices, multipliers, TTLs, model names, tier names, notice periods and feature availability.

**Research limitation.** OpenAI's own blog posts (openai.com/index/…) returned HTTP 403 and could not be read in this session. The two GPT-4o sycophancy posts (29 April and 2 May 2025) are therefore cited through Simon Willison's quotation of the primary text and through search excerpts, and are tagged WIDELY REPORTED. Other gaps:

- OpenAI's current rate-limit tiers and the latency behavior of its Flex tier were not fetched.
- Google's explicit-cache default TTL was not on the caching page fetched; it is flagged as unverified.
- The full text of RouteLLM, FrugalGPT and the 2023 drift paper was not read; claims are limited to their abstracts plus the parts noted.
- The seven capabilities of the DORA 2025 AI Capabilities Model appear only in an image on the announcement page and were not enumerated.
- No public, dated engineering writeup was found that reports a production agent's prompt-cache hit rate together with its cost before and after caching, other than the Manus post (§1.2) and Claude Code's own UI example (§1.5).

---

## PART 1: Performance and economics

### 1.1 Where the money goes in an agent loop

An agent loop re-sends its whole context on every model call. The system prompt, tool definitions, the task and every earlier tool call and tool result go back to the model each turn. Input therefore dominates cost, and it grows with the square of the number of turns unless something is cached, cleared or summarized.

**What the sources say**

- Claude Code's cost documentation states that it "sends your full conversation with every request, and each time Claude uses tools it sends another request carrying that batch of tool results" [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10].
- Manus reports that in its agent "the input-to-output ratio averages about 100:1", so prompts dominate the cost profile, and calls "the KV-cache hit rate … the single most important metric for a production-stage AI agent" [VERIFIED: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, published 2025-07-18]. This is a vendor engineering post about one product. It reports a ratio, not a measured distribution.
- Anthropic's context-engineering post describes "context rot": recall from context decreases as context grows, a pattern it says appears across all models. It frames context as "a finite resource with diminishing marginal returns" and notes that transformers create "n² pairwise relationships for n tokens" [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29]. The n² remark is about attention, not billing; billing is linear in tokens per call (see the worked example below).
- Tool use itself adds input. Anthropic adds a hidden tool-use system prompt whenever tools are present: 286 tokens on Claude Opus 5.5 and 675 on Claude Opus 4.7 (tool_choice auto/none). Declaring the `computer_toolset_20260801` toolset adds "about 4,500 input tokens", and `browser_toolset_20260801` about 6,600 [VERIFIED: https://platform.claude.com/docs/en/about-claude/pricing, n.d., accessed 2026-10]. ⚠
- Anthropic reports that presenting MCP tools as code the agent calls from a sandbox, instead of loading every tool definition and routing intermediate results through the model, "reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%" in its example. It names the two causes: tool definitions overloading context, and intermediate results (a two-hour transcript passed through the model twice, about 50,000 extra tokens). It warns that running agent-generated code "requires a secure execution environment with appropriate sandboxing", resource limits and monitoring [VERIFIED: https://www.anthropic.com/engineering/code-execution-with-mcp, published 2025-11-04]. This is one illustrative example, not a benchmark.

**Worked example: quadratic input growth** [ASSUMPTION/JUDGEMENT]

Let a loop start with a fixed prefix of P tokens (system prompt, tools, task) and add Δ tokens per turn (the model's tool call plus the tool result). Turn k sends P + kΔ input tokens. Over n turns the model reads

  total input = nP + Δ · n(n+1)/2

which grows with n². With P = 10,000, Δ = 3,000 and n = 50, the loop reads about 4.3 million input tokens, although no single request exceeds 160,000.

At the Claude Sonnet 5.5 list prices of 28 October 2026 ($2/MTok input, $10/MTok output, $2.50/MTok 5-minute cache write, $0.10/MTok cache read; §1.2):

| Scenario | Input cost | Output cost (500 tokens/turn) | Total |
| --- | --- | --- | --- |
| No caching | 4.33 MTok × $2 = $8.65 | 25k × $10 = $0.25 | ≈ $8.90 |
| Prefix cached each turn (≈ 4.18 MTok read, ≈ 0.16 MTok written) | $0.42 + $0.40 = $0.82 | $0.25 | ≈ $1.07 |

Caching cuts the run cost by roughly 8× in this example. Output becomes about a quarter of the bill. The quadratic term is still there; caching only multiplies it by a smaller price. Compaction, tool-result clearing and sub-agents (§1.4) attack the term itself. These figures are illustrative arithmetic, not a measurement.

**Durable vs volatile.** Durable: input re-reading dominates agent cost, total input grows superlinearly with turn count, and tool definitions and tool results are input. Volatile: the per-token prices, the hidden tool-prompt sizes, and the 98.7% example.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Cost should be modelled per *task*, not per request, and budgeted as a function of expected turn count. Put a turn or token budget in the orchestrator as a hard limit, not a prompt instruction. Treat large tool results as a design defect to fix at the tool boundary (filter, paginate, return handles), because every byte a tool returns is paid for again on every later turn.

---

### 1.2 Prompt caching: mechanics and prices across three providers

Prompt caching reuses the provider's computed state for an identical prompt prefix. All three providers now cache automatically on current models, charge a premium or nothing to write, and discount reads by 90–97.5%. The details differ enough that a cross-provider abstraction leaks.

**Anthropic (Claude API)** [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/prompt-caching, n.d., accessed 2026-10] ⚠

- **Price multipliers on base input**: 5-minute cache write 1.25×; 1-hour cache write 2×; cache hits and refreshes 0.1× by default, but 0.05× on Claude Opus 5.5 and Sonnet 5.5 and 0.025× on Fable 5.1 and Mythos 5.1.
- **TTL**: default 5 minutes ("ephemeral"), "refreshed for no additional cost each time the cached content is used"; optional 1 hour (`"ttl": "1h"`). The page does not state explicitly whether the 1-hour entry is refreshed on hit.
- **Minimum cacheable length**: 512 tokens on the newest models (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5/5.1, Opus 5); 1,024 on Opus 4.8, Sonnet 5 and Sonnet 4.x; 2,048 on Opus 4.7; 4,096 on Opus 4.5/4.6 and Haiku 4.5. Shorter prompts are processed uncached "and no error is returned"; the only signal is that `cache_creation_input_tokens` and `cache_read_input_tokens` are both 0.
- **Breakpoints**: at most 4 explicit breakpoints; automatic caching (one top-level `cache_control` field that moves the breakpoint to the last cacheable block as the conversation grows) uses one slot. Lookback is 20 blocks per breakpoint.
- **Invalidation hierarchy**: prefix order is `tools` → `system` → `messages`; a change at one level invalidates it and everything after. Changing tool definitions invalidates everything. Changing `tool_choice` or adding/removing images invalidates messages. Changing thinking parameters or effort always invalidates message blocks.
- **Matching and isolation**: hits require "100% identical prefix content". Caches are never shared across organizations and are also isolated per workspace on the Claude API.
- **Speed is part of the key**: "Requests at different speeds do not share cached prefixes", so falling back from fast mode to standard is a cache miss [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/fast-mode, n.d., accessed 2026-10].

**OpenAI (Responses/Chat APIs)** [VERIFIED: https://developers.openai.com/api/docs/guides/prompt-caching, n.d., accessed 2026-10] ⚠

- Caching is "enabled by default for supported OpenAI models".
- **GPT-5.6 and later**: minimum 1,024 visible input tokens; cached reads 0.1× input (0.05× on GPT-6.1 Sol and Terra); writes are now charged, at 1.25× for the default 30-minute TTL and 2.5× for the 12-hour TTL. The page calls these total rates, not surcharges. An explicit-breakpoint mode exists alongside automatic caching.
- **Earlier models**: no cache-write charge; retention `in_memory` (about 5–10 minutes of inactivity, up to one hour) or `24h`; cache prefixes on GPT-5.5 fall at 2,048-token intervals.
- **Routing**: `prompt_cache_key` "influence[s] routing" but does not guarantee a hit; the page advises about 15 requests per minute per key, above which "overflow routing" can cause misses.

**Google (Gemini API)** [VERIFIED: https://ai.google.dev/gemini-api/docs/caching, last updated 2026-10-23] ⚠

- "Implicit caching is enabled by default for all Gemini 2.5 and newer models." Explicit caching (managed cache objects) is "not supported … for Gemini 4 Argon and onward".
- Minimum tokens for implicit caching: 4,096 on Gemini 4 Argon, 3.8 Flash, 3.6 Flash and 3.1 Pro Preview; 2,048 on Gemini 2.5 Flash/Pro.
- Multi-turn rule on Argon and newer: Gemini caches the full previous request only if the new request adds at least 2,050 tokens; otherwise the last 2,050 tokens are re-processed at the standard rate.
- Prices from the pricing page [VERIFIED: https://ai.google.dev/gemini-api/docs/pricing, last updated 2026-10-27]: Argon input $2.00 and cached $0.10 per MTok (a 0.05× ratio, derived); 3.8 Flash $0.75 and $0.075 (0.1×), with cache storage $0.50 per MTok per hour; 2.5 Pro $1.25 and $0.125 (≤200k prompt), storage $4.50 per MTok per hour. The default TTL for explicit caches was not on the pages fetched ⚠ (not verified).

**Comparison table** (28 October 2026, current flagship generation) ⚠

| | Anthropic (Opus/Sonnet 5.5) | OpenAI (GPT-5.6+) | Google (Gemini 4 Argon) |
| --- | --- | --- | --- |
| Default mode | Explicit breakpoints or one-field automatic | Automatic (explicit optional) | Implicit only |
| Write price | 1.25× (5 min), 2× (1 h) | 1.25× (30 min), 2.5× (12 h) | No write charge listed |
| Read price | 0.05× (0.1× on most other models) | 0.1× (0.05× on GPT-6.1 Sol/Terra) | 0.05× (derived from price table) |
| Minimum prefix | 512 tokens | 1,024 tokens | 4,096 tokens |
| Storage fee | None | None | None listed for Argon; per-hour on older models with explicit caching |
| Silent failure | Yes (usage fields show 0) | Yes | Yes |

Sources: the three caching pages and the three pricing pages cited above. The ratios are derived by the analyst from the listed prices [ASSUMPTION/JUDGEMENT for the derivation].

**Engineering practice from operators**

- Manus's rules: keep the prompt prefix stable ("A common mistake is including a timestamp" at the start of the system prompt), keep context append-only, "Ensure your serialization is deterministic" (unstable JSON key order causes silent misses), and mask tools by constraining decoding rather than removing them, because changing tool definitions mid-task invalidates the cache. It quotes Claude Sonnet cached input at $0.30/MTok against $3 uncached at the time [VERIFIED: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, published 2025-07-18]. That price refers to Sonnet 3.x/4-era list prices; current Sonnet 5.5 prices are lower (§1.3).
- Claude Code exposes cache health to the user: a `Prompt cache (main)` line reports the share of input served from cache, misses, the likely cause of the last miss (for example "tool definitions changed") and "expected rebuilds" after compaction or tool-result clearing. Its example shows "91% of input tokens from cache" [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10]. The 91% is a UI example, not a reported fleet average.

**Durable vs volatile.** Durable: caches match exact prefixes; anything that changes early in the prompt (tools, system prompt, timestamps, serialization order) destroys reuse for everything after it; misses are silent. Volatile: every multiplier, TTL and minimum length above, and which provider charges for writes (OpenAI introduced write charges only for GPT-5.6+).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Prompt layout is an architectural decision: order the context from most stable to least stable (tools, policy, long-lived instructions, task, history) and keep volatile data such as clocks and request IDs out of the prefix. Treat tool-set changes during a run as expensive. Monitor cache hit rate per agent and per route as an SLI, because a deploy that reorders a JSON field can double cost without any error. A model-provider abstraction layer should expose caching controls rather than hide them.

---

### 1.3 Price tiers: batch, flex, fast and priority

All three providers sell the same model at several prices depending on how long the caller can wait. The spread between the cheapest and the dearest tier for one model is now about 4×.

| Provider (model) | Batch / flex | Standard | Fast / priority |
| --- | --- | --- | --- |
| Anthropic (Opus 5.5) | Batch: 50% off input and output | $4 in / $20 out per MTok | Fast mode: $8 / $40 (2×), "up to 2.5x higher output tokens per second" |
| OpenAI (gpt-5.6-sol) | Batch and Flex: $2 / $10 (50% off) | $4 / $20 | Fast (formerly Priority): $8 / $40 (2×) |
| Google (Gemini 4 Argon, until 30 Nov 2026) | Batch and Flex: $1 / $5 (50% off) | $2 / $10 | Priority: $3.60 / $18 (1.8×) |

Sources: [VERIFIED: https://platform.claude.com/docs/en/about-claude/pricing, n.d., accessed 2026-10]; [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/fast-mode, n.d., accessed 2026-10]; [VERIFIED: https://developers.openai.com/api/docs/pricing, n.d., accessed 2026-10]; [VERIFIED: https://ai.google.dev/gemini-api/docs/pricing, last updated 2026-10-27]. ⚠ All figures.

**Further details**

- **Anthropic Message Batches**: a batch holds up to 100,000 requests or 256 MB; "most batches completing within 1 hour"; batches expire if not complete within 24 hours, and expired requests are not billed; results are available for 29 days. Because batches can take longer than 5 minutes, the docs suggest the 1-hour cache TTL for shared context in batches [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/batch-processing, n.d., accessed 2026-10]. Batch and caching discounts stack [VERIFIED: https://platform.claude.com/docs/en/about-claude/pricing, n.d., accessed 2026-10].
- **Anthropic fast mode** runs "the same model with a faster inference configuration. There is no change to intelligence or capabilities." Its gains are "focused on output tokens per second (OTPS), not time to first token (TTFT)". It is not available with the Batch API or with a Priority Tier commitment, and has its own rate limit [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/fast-mode, n.d., accessed 2026-10].
- **Anthropic Priority Tier** "capacity commitments are no longer available for purchase"; existing commitments run to contract end. The tier "targets 99.5 percent uptime" and commitments were for 1, 3, 6 or 12 months and "a specific model version" [VERIFIED: https://platform.claude.com/docs/en/api/service-tiers, n.d., accessed 2026-10]. The book should not present Anthropic Priority Tier as a current purchasing option.
- **OpenAI** renamed Priority processing to Fast mode [VERIFIED: https://developers.openai.com/api/docs/pricing, n.d., accessed 2026-10].
- **Location premiums**: Anthropic's US-only inference (`inference_geo: "us"`) costs 1.1× on all token categories for Claude 4.6 and later; regional endpoints on Bedrock and Google Cloud carry a 10% premium over global endpoints [VERIFIED: https://platform.claude.com/docs/en/about-claude/pricing, n.d., accessed 2026-10].
- **Long context**: Claude 4.6 and later (except Haiku 5.5) include the 1M-token window "at standard pricing"; Haiku 5.5 is priced higher above 100,000 prompt tokens ($0.10 → $0.50 input per MTok) [VERIFIED: same]. Gemini 2.5 Pro doubles input price above 200k tokens [VERIFIED: https://ai.google.dev/gemini-api/docs/pricing, last updated 2026-10-27].
- **Hosted agent runtimes add a time dimension**: Claude Managed Agents bills tokens plus $0.08 per session-hour of `running` time, and Batch API discounts do not apply to sessions [VERIFIED: https://platform.claude.com/docs/en/about-claude/pricing, n.d., accessed 2026-10].
- **Prices can rise.** Google's page lists Gemini 4 Argon input at $2.00/MTok through 30 November 2026 and $4.00 from 1 December 2026, and Gemini 3.8 Flash at $0.75 through 31 December 2026 and $1.50 from 1 January 2027 [VERIFIED: https://ai.google.dev/gemini-api/docs/pricing, last updated 2026-10-27]. ⚠

**Durable vs volatile.** Durable: providers price-discriminate by latency tolerance; asynchronous work is roughly half price; guaranteed speed costs a premium; data-location constraints cost extra. Volatile: tier names (Priority → Fast at OpenAI; Priority Tier withdrawn at Anthropic), the exact multipliers, and scheduled price changes.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Classify agent work by deadline at design time. Evaluations, back-office reconciliation, enrichment and nightly report agents belong on batch or flex paths, which means they must be resumable and idempotent, since a batch may expire. Interactive paths decide whether OTPS (long answers, code) or TTFT (short turns) matters before paying for a fast tier. Keep price tables in configuration with effective dates, because a cost model hard-coded to October prices will be wrong in December.

---

### 1.4 Multi-agent token multipliers and when they pay

**What Anthropic measured** [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13]

- "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."
- The multi-agent system (Claude Opus 4 lead, Sonnet 4 subagents) "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval". This is an internal eval; its size and composition are not published.
- On BrowseComp, "three factors explained 95% of the performance variance", and "token usage by itself explains 80% of the variance", with the number of tool calls and model choice as the other two factors.
- "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7."
- Parallelism: "the lead agent spins up 3-5 subagents in parallel rather than serially" and "the subagents use 3+ tools in parallel"; these changes "cut research time by up to 90% for complex queries".
- Economics: "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance"; they are a poor fit where agents must share context or have many dependencies, and "most coding tasks involve fewer truly parallelizable tasks than research."
- Operations: "Synchronous execution creates bottlenecks"; "Agents are stateful and errors compound", so they built systems that "resume from where the agent was when the errors occurred".

Evidence age: June 2025, Claude 4-generation models (Opus 4 and Sonnet 4 are now retired on the Claude API; §2.1). ⚠ The multipliers describe that system, not a law.

**Other data points**

- Claude Code docs: agent teams "use approximately 7x more tokens than standard sessions when teammates run in plan mode", and team token usage "is roughly proportional to team size" [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10].
- Claude Code docs: "the average cost is around $13 per developer per active day and $150-250 per developer per month, with costs remaining below $30 per active day for 90% of users", across enterprise deployments [VERIFIED: same]. Undated; the population and period behind the average are not stated ⚠.
- Anthropic's context-engineering post: sub-agents may spend tens of thousands of tokens exploring but return "a condensed, distilled summary", often 1,000–2,000 tokens, to the lead agent [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29].

**Durable vs volatile.** Durable: fan-out multiplies token spend roughly by the number of independent contexts; it buys breadth and wall-clock time, not efficiency; it pays only when the subtasks are separable and the task is valuable. Volatile: 4×, 15×, 7×, 90.2%, $13/day.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A multi-agent design needs a written economic justification: task value, expected fan-out, and the cheaper single-agent baseline it beat. Sub-agents are also a context-management device (they absorb verbose work and return summaries), which can make them cheaper than one long single-agent context in some workloads; measure both. Use smaller models for sub-agents where the eval allows. Cap fan-out and total tokens per task in the orchestrator.

---

### 1.5 Model routing, cascades and small models

**Research**

- **FrugalGPT** (Chen, Zaharia, Zou; Stanford). Names three strategies: "prompt adaptation", "LLM approximation" and "LLM cascade". The cascade learns which LLMs to call, in order, for each query. The abstract claims it can "match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction" or "improve the accuracy over GPT-4 by 4% with the same cost" [VERIFIED: https://arxiv.org/abs/2305.05176, published 2023-05-09]. arXiv preprint; no peer-reviewed venue listed. Evidence age: 2023, GPT-4-era model prices and single-turn tasks; flag as older than 18 months.
- **RouteLLM** (Ong et al.; LMSYS/UC Berkeley/Anyscale). Trains routers between one strong and one weak model on human preference data with augmentation; claims costs reduced "by over 2 times in certain cases" without compromising quality, and that routers keep performance when the model pair is swapped at test time [VERIFIED: https://arxiv.org/abs/2406.18665, v1 2024-06-26, v4 2025-02-23]. The arXiv page lists no venue ⚠ (often cited as ICLR 2025; not verified here). The abstract names no benchmarks or models.
- **AI Agents That Matter** (Kapoor, Stroebl, Siegel, Nadgir, Narayanan; Princeton). Argues "SOTA agents are needlessly complex and costly" and that "Agent evaluations must be cost-controlled" [VERIFIED: https://arxiv.org/abs/2407.01502, published 2024-07-01]. In the full text, on HumanEval (five runs): a simple "warming" baseline on GPT-4 scored 93.2% at $2.45 total; retry 92.0% at $2.51; an escalation baseline (cheap model first, then stronger) 85.0% at $0.27; LDB 91.0% at $2.19; Reflexion 87.8% at $3.90; LATS (GPT-4) 88.0% at $134.50. The authors find "no significant accuracy difference between our warming strategy and the best-performing agent architecture" and costs differing "by almost two orders of magnitude" for similar accuracy. Joint cost–accuracy optimization of a DSPy pipeline on HotPotQA cut variable cost by about 53% (GPT-3.5) and 41% (Llama-3-70B) at similar accuracy. They recommend reporting dollar cost and token counts so costs "can be recalculated as prices change" [VERIFIED: https://arxiv.org/html/2407.01502, v1 2024-07-01]. Evidence age: mid-2024 models and benchmarks; the method (plot accuracy against cost; compare with simple baselines) is the durable part. The abstract does not use the word "Pareto"; the paper's figures show cost–accuracy frontiers.
- **Small models position paper** (Belcak et al., arXiv). Argues that small language models are capable enough, better suited and more economical for many repetitive, specialized agentic subtasks (paraphrase of the abstract), and that heterogeneous multi-model systems are the natural choice where general conversation is needed; outlines an LLM-to-SLM conversion algorithm [VERIFIED: https://arxiv.org/abs/2506.02153, v1 2025-06-02, v3 2026-09-22]. It is a position paper with no new quantitative results; do not cite it as evidence that SLMs match LLMs.

**Vendor guidance**

- Anthropic's routing pattern sends "easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5"; the post opens with "Agentic systems often trade latency and cost for better task performance" and advises finding "the simplest solution possible, and only increasing complexity when needed" [VERIFIED: https://www.anthropic.com/engineering/building-effective-agents, published 2024-12-19]. The page names a model released after its publication date, so it has been edited since; quote the principle, not the model name.
- Anthropic's current model table describes Haiku 5.5 as "For high-volume, latency-sensitive tasks such as classification, extraction, and routing", with comparative latency "Fastest" against "Moderate" for Opus 5.5; Haiku 5.5 lists from $0.10/$0.50 per MTok against $4/$20 for Opus 5.5 [VERIFIED: https://platform.claude.com/docs/en/about-claude/models/overview, n.d., accessed 2026-10]. That is a 40× list-price gap. ⚠
- Claude Code docs: "Sonnet handles most coding tasks well and costs less than Opus. Reserve Opus for complex architectural decisions or multi-step reasoning", and set `model: haiku` for simple subagent tasks [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10].

**Where the evidence cuts the other way.** Anthropic's finding that a model upgrade beat doubling the token budget (§1.4) means that routing to a cheaper model can cost more if the cheap model needs more turns, retries or human repair. Escalation in *AI Agents That Matter* was the cheapest option but also the least accurate of the strong baselines (85.0% against 93.2%).

**Durable vs volatile.** Durable: most queries do not need the strongest model; a router or cascade needs a quality signal (a learned router, a verifier, or a confidence check) and its own evaluation; the right comparison is cost per *successful task*, not per token. Volatile: the specific savings figures, which depend on the 2023–2024 price gaps between model tiers.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Make the model choice a per-step configuration in the orchestrator, not a global constant, so planning, extraction, summarization and verification can each use a different tier. Evaluate routing on end-to-end task success and total cost including retries and escalations. Keep a "no LLM" branch: OpenAI's latency guide lists "Don't default to an LLM" as a principle (§1.6).

---

### 1.6 Latency: where the time goes

**Components.** A model call's latency is roughly time to first token (queueing, network, prefill of the input) plus output tokens divided by output tokens per second. An agent task's latency is the sum over its sequential model calls and tool calls, plus any human wait. [ASSUMPTION/JUDGEMENT] for the decomposition; the vendor statements below support its parts.

- OpenAI's latency guide lists seven principles: "Process tokens faster", "Generate fewer tokens", "Use fewer input tokens", "Make fewer requests", "Parallelize", "Make your users wait less", "Don't default to an LLM". Its heuristic: "cutting 50% of your output tokens may cut ~50% of your latency", whereas "cutting 50% of your prompt may only result in a 1–5% latency improvement" [VERIFIED: https://developers.openai.com/api/docs/guides/latency-optimization, n.d., accessed 2026-10]. The heuristic predates prompt caching becoming automatic and very long contexts becoming common; for 500k-token prompts, prefill is not negligible ⚠ [ASSUMPTION/JUDGEMENT].
- Anthropic's fast mode improves OTPS "not time to first token" [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/fast-mode, n.d., accessed 2026-10]. Its model table rates latency only comparatively ("Slower", "Moderate", "Fast", "Fastest") and notes "Actual latency depends on prompt length, output length, and thinking effort" [VERIFIED: https://platform.claude.com/docs/en/about-claude/models/overview, n.d., accessed 2026-10].
- Thinking tokens are output tokens: Claude Code docs note "Thinking tokens are billed as output tokens, and the default budget can be tens of thousands of tokens per request", and that thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models; effort levels are the control [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10]. Reasoning effort is therefore a latency and cost dial as well as a quality dial.

**Parallel and speculative execution**

- **Parallel tool calls.** Claude may emit several `tool_use` blocks in one turn; "The API doesn't prescribe an execution order". The docs advise that "Independent, read-only operations are usually safe to run in parallel", while tools "with side effects, shared state, or ordering requirements might be better run sequentially", and that every call gets a `tool_result` (with `is_error: true` if it was not run) in the next message [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use, n.d., accessed 2026-10].
- **LLMCompiler** (Kim et al., ICML 2024) plans a DAG of function calls and runs independent calls in parallel; against ReAct it reports up to 3.7× lower latency, up to 6.7× lower cost and up to about 9% higher accuracy [VERIFIED: https://arxiv.org/abs/2312.04511, v1 2023-12-07, v3 2024-06-05]. Evidence age: late 2023, before native parallel tool calls were standard in vendor APIs.
- **Speculative decoding** (Leviathan, Kalman, Matias, ICML 2023 oral) uses a small draft model to propose tokens that the large model verifies in parallel, "without changing the distribution"; it reports "a 2X-3X acceleration" on T5-XXL "with identical outputs" [VERIFIED: https://arxiv.org/abs/2211.17192, v1 2022-11-30]. This is an inference-server technique; API users get it only if the provider uses it. The provider's fast tiers may use such techniques, but no vendor page fetched says so [ASSUMPTION/JUDGEMENT].
- **Speculative actions** (Ye et al., Columbia) apply the same idea to agent steps: a fast "speculator" predicts the next API call, which runs in parallel, and the result is committed only if the authoritative model agrees. The abstract reports "up to 55% next-action prediction accuracy" and "up to 20% latency reductions" across gaming, e-commerce and web-search environments [VERIFIED: https://arxiv.org/abs/2510.04371, v1 2025-10-05, v2 2026-04-23]. Search results list it as an ICLR 2026 paper [WIDELY REPORTED: https://iclr.cc/virtual/2026/poster/10009726, 2026]. The abstract does not explain how speculative actions with irreversible side effects are handled.
- **Tail latency** compounds in fan-out: Dean and Barroso's "The Tail at Scale" argues that rare slow responses dominate at scale and that services must be "latency tail-tolerant", building "a predictably responsive whole out of less predictable parts" [VERIFIED: https://research.google/pubs/the-tail-at-scale/, published 2013]. Evidence age: 2013, web-search serving; the principle applies directly to agents that wait on the slowest of N parallel subagents or tools [ASSUMPTION/JUDGEMENT].

**Durable vs volatile.** Durable: output length and the number of sequential steps dominate latency; parallelism helps only for independent, side-effect-free steps; fan-out exposes the tail. Volatile: OTPS figures, fast-mode multipliers, and the measured speedups (tied to specific models and benchmarks).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Declare per tool whether it is read-only and idempotent, and let the orchestrator parallelize or speculate only on those. Speculation on a tool with side effects needs a reversible or staged action (draft, hold, commit) or it is not lossless. Put deadlines on every sub-agent and tool call and decide in advance what partial result the lead agent returns when one is late. Measure TTFT, OTPS, steps per task and end-to-end task latency separately; they have different fixes.

---

### 1.7 Rate limits, quotas and spend caps

**Anthropic** [VERIFIED: https://platform.claude.com/docs/en/api/rate-limits, n.d., accessed 2026-10] ⚠

- Limits are measured in requests per minute (RPM), input tokens per minute (ITPM) and output tokens per minute (OTPM) per model class, enforced with a token bucket ("continuously replenished … rather than being reset at fixed intervals"). A 60 RPM limit "might be enforced as 1 request per second", so bursts can fail.
- **Cache-aware ITPM**: "For most Claude models, only uncached input tokens count toward your ITPM rate limits." With a 2,000,000 ITPM limit and an 80% cache hit rate, an organization "could effectively process 10,000,000 total input tokens per minute". Caching is therefore a throughput lever as well as a cost lever.
- `max_tokens` does not count against OTPM; OTPM counts tokens actually generated.
- Standard tiers on Opus 5.5: Start 1,000 RPM / 2M ITPM / 400k OTPM; Build 5,000 / 5M / 1M; Scale 10,000 / 10M / 2M. Monthly spend caps: Start $500, Build $1,000, Scale $200,000; at the cap, requests return HTTP 429 with `enforced_spend_limit_reached` and no `retry-after`, until the first day of the next month.
- "acceleration limits" can return 429 after "a sharp increase in usage"; the advice is to "increase your traffic gradually".
- Workspaces can have lower limits to protect other workloads; organization limits always apply.
- Batches have separate limits (Start tier: 200,000 batch requests in the processing queue).

**Sizing guidance for a coding-agent fleet.** Claude Code's docs recommend per-user TPM that falls with team size, from 200k–300k TPM per user for 1–5 users to 10k–15k for 500+ users, because "fewer users tend to use Claude Code concurrently in larger organizations"; for 200 users, about 4 million TPM in total [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10].

**OpenAI caching interacts with routing.** Above about 15 requests per minute per prefix and key, overflow routing can cause cache misses [VERIFIED: https://developers.openai.com/api/docs/guides/prompt-caching, n.d., accessed 2026-10]. OpenAI's own rate-limit tiers were not fetched (see Research limitation).

**Durable vs volatile.** Durable: providers enforce per-minute token buckets and monthly spend caps per organization; bursts and sudden growth are throttled; caching can raise effective throughput. Volatile: all numbers and tier names, and whether cached tokens count (true for "most" Claude models, not all).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Rate limits are a shared, organization-wide resource, so an agent platform needs admission control and per-tenant or per-workload quotas of its own, plus separate workspaces or keys for production, evaluation and developer tooling. A spend-cap 429 is not retryable and must be distinguished from a rate-limit 429 in client code. Plan capacity in uncached input tokens, which ties capacity planning to cache hit rate. Ramp new agent workloads gradually to avoid acceleration limits.

---

## PART 2: Evolution: models, prompts and behavior change underneath you

### 2.1 Model deprecation and retirement policies

| Provider | Stated notice | Lifecycle terms | Notes |
| --- | --- | --- | --- |
| Anthropic | "at least 60 days' notice before model retirement for publicly released models" | Active, Legacy, Deprecated, Retired | Partner platforms (Bedrock, Google-managed) set their own dates; deprecated models "are likely to be less reliable" |
| OpenAI | GA models "At least 6 months"; specialized variants at least 3 months; preview models may be retired on much shorter notice, "such as 2 weeks" | Deprecated, Shutdown/sunset, Legacy | Deprecation is immediate on announcement |
| Google (Gemini API) | Preview models "will be deprecated with at least 2 weeks notice"; 2-week email notice for breaking changes behind a `-latest` alias; no fixed period stated for stable models | Stable, Preview, Latest, Experimental | Listed shutdown dates are "earliest possible dates" |

Sources: [VERIFIED: https://platform.claude.com/docs/en/about-claude/model-deprecations, n.d., accessed 2026-10]; [VERIFIED: https://developers.openai.com/api/docs/deprecations, n.d., accessed 2026-10]; [VERIFIED: https://ai.google.dev/gemini-api/docs/models, last updated 2026-10-22]; [VERIFIED: https://ai.google.dev/gemini-api/docs/deprecations, last updated 2026-10-22]. ⚠ All notice periods.

**Observed retirement intervals (Anthropic, Claude API)** [VERIFIED: https://platform.claude.com/docs/en/about-claude/model-deprecations, n.d., accessed 2026-10]; interval arithmetic by the analyst [ASSUMPTION/JUDGEMENT]:

| Model | Deprecation notice | Retirement | Interval |
| --- | --- | --- | --- |
| claude-3-opus-20240229 | 2025-06-30 | 2026-01-05 | ≈ 189 days |
| claude-3-5-sonnet (two snapshots) | 2025-08-13 | 2025-10-28 | ≈ 76 days |
| claude-3-7-sonnet-20250219 | 2025-10-28 | 2026-02-19 | ≈ 114 days |
| claude-3-5-haiku-20241022 | 2025-12-19 | 2026-02-19 | ≈ 62 days |
| claude-3-haiku-20240307 | 2026-02-19 | 2026-04-20 | ≈ 60 days |
| claude-sonnet-4 / claude-opus-4 (20250514) | 2026-04-14 | 2026-06-15 | ≈ 62 days |
| claude-opus-4-1-20250805 | 2026-06-05 | 2026-08-05 | ≈ 61 days |
| claude-sonnet-4-5-20250929 | 2026-09-30 | 2026-11-30 | ≈ 61 days |

Since late 2025 the interval has settled at the 60-day minimum. Claude Opus 4 was retired about 13 months after its May 2025 snapshot date. Active models carry "not sooner than" retirement dates, for example Opus 5.5 "Not sooner than September 22, 2027". Two active rows show dates that have already passed (Haiku 4.5 "Not sooner than October 15, 2026"; Opus 4.5 "Not sooner than November 24, 2026" is close), which illustrates that "not sooner than" is a floor, not a schedule.

**Recent OpenAI notices** [VERIFIED: https://developers.openai.com/api/docs/deprecations, n.d., accessed 2026-10]:

- 2026-06-11: older snapshots of gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-pro, o3 and o3-pro, shutdown 2026-12-11 (6 months).
- 2026-10-14: specific snapshots of GPT-4o, GPT-4o mini, GPT-4.1 and GPT-4.1 mini, shutdown 2027-01-14 (about 3 months). ⚠ This is shorter than the 6-month GA policy as summarized; the page may classify these snapshots differently. Not resolved in this session.
- 2025-08 (notice given 2025-08-26 per the body text): Assistants API, shutdown 2026-08-26, replaced by Responses and Conversations APIs.
- 2026-06-03: **reusable prompts (`v1/prompts`), the Evals platform and Agent Builder**, shutdown 2026-11-30, with the advice to "Move prompts into app code", use Promptfoo for evals and the Agents SDK. This is direct evidence that a vendor-hosted prompt store or eval store is itself a dependency with a lifecycle.

**Google**: `gemini-2.0-flash` and `gemini-2.0-flash-lite` had earliest shutdown dates of 2026-06-01; `gemini-3-pro-preview` 2026-03-09 [VERIFIED: https://ai.google.dev/gemini-api/docs/deprecations, last updated 2026-10-22].

**API versions also retire behavior.** Anthropic removed `temperature`, `top_p` and `top_k` in API version `2026-10-21` (they return HTTP 400); earlier API versions reject non-default values on Claude 4.7 and later models [VERIFIED: https://platform.claude.com/docs/en/about-claude/model-deprecations, n.d., accessed 2026-10]. A migration to a new model can therefore force code changes as well as prompt changes.

**Anthropic's preservation commitments.** Anthropic commits to keep the weights of every publicly released model "for at least the company's lifetime", to write a post-deployment report on deprecation, and to interview models before retirement; it is "considering" keeping some retired models available [VERIFIED: https://www.anthropic.com/research/deprecation-commitments, published 2025-11-04]. Preserved weights are not an API; for system architects, retirement still means requests fail on the retirement date.

**Durable vs volatile.** Durable: every hosted model has a finite life measured in months to about two years; retirement forces a migration that changes behavior; partner clouds run their own schedules; platform features (prompt stores, eval stores, assistant runtimes) retire too. Volatile: notice periods, which vary by provider and model class, and every date.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Budget a model migration as recurring work, at least once or twice a year per model in use, with an evaluation suite ready before the notice arrives; 60 days is too short to build one. Keep a usage audit that maps every model ID to the code, prompts and owners that use it (Anthropic's docs point to a usage export by API key and model for this purpose). Keep prompts, eval cases and agent definitions in your own repository, not only in a vendor console.

---

### 2.2 Version pinning: what a model ID actually guarantees

- Anthropic: "Every Claude model ID is a pinned snapshot, including the dateless IDs used from the 4.6 generation on." For models before 4.6, the alias was "a convenience pointer that resolves to the dated ID" [VERIFIED: https://platform.claude.com/docs/en/about-claude/models/overview, n.d., accessed 2026-10]. The pin covers weights; the September 2025 postmortem (§2.4) shows that serving infrastructure can still change outputs under a fixed ID.
- Google: stable model names "usually don't change" and are recommended for production; `-latest` aliases are "hot-swapped" with each release; previews may be retired with two weeks' notice [VERIFIED: https://ai.google.dev/gemini-api/docs/models, last updated 2026-10-22].
- OpenAI: the models page fetched did not state alias/snapshot guidance ⚠ (not verified). The deprecations page refers to retiring "specific snapshots" [VERIFIED: https://developers.openai.com/api/docs/deprecations, n.d., accessed 2026-10]. ChatGPT-facing aliases such as `chatgpt-4o-latest` were deprecated on 2025-11-18 with shutdown 2026-02-17 [VERIFIED: same].
- Narayanan and Kapoor argued in 2023 that snapshots are only a partial fix because OpenAI "only maintains them for a few months", so developers must keep updating [VERIFIED: https://www.normaltech.ai/p/is-gpt-4-getting-worse-over-time, published 2023-07-19]. Evidence age: 2023; current snapshot lifetimes are longer (§2.1), but the point stands.

**Durable vs volatile.** Durable: pin a snapshot for reproducibility, and expect the pin to expire; a pin fixes the model but not the provider's serving stack, the API version, or the tool runtime. Volatile: naming conventions (dated vs dateless IDs) and alias semantics.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Treat the tuple (model ID, API version, prompt version, tool schema versions, sampling and effort settings) as the deployable unit, record it on every trace, and change it only through the same release process as code. Never point production at a `-latest` alias.

---

### 2.3 Behavior drift across versions

**Chen, Zaharia and Zou (2023).** Compared the March 2023 and June 2023 versions of GPT-3.5 and GPT-4 on seven tasks (math, sensitive questions, opinion surveys, multi-hop knowledge questions, code generation, US medical licensing questions, visual reasoning). GPT-4's accuracy on identifying prime numbers fell from 84% (March) to 51% (June), partly attributed to following chain-of-thought prompts less well; GPT-3.5 improved on the same task. GPT-4 became less willing to answer sensitive and opinion questions; both models made more formatting mistakes in generated code. The authors conclude "the performance and behavior of both GPT-3.5 and GPT-4 can vary greatly over time" and call for continuous monitoring [VERIFIED: https://arxiv.org/abs/2307.09009, v1 2023-07-18, v3 2023-10-31]. Published in *Harvard Data Science Review* issue 6.2, March 2024 [WIDELY REPORTED: https://hdsr.mitpress.mit.edu/pub/y95zitmz, 2024]. Evidence age: 2023, retired models; flag as older than 18 months.

**The critique.** Narayanan and Kapoor argued the paper measured behavior change, not capability loss: the prime-number test set contained only primes ("They picked 500 numbers, but all of them were prime!"), so a model that always answers "prime" scores well; on composite numbers the errors reversed. The code test checked whether output was directly executable, not whether it was correct, so "the newer model's attempt to be more helpful counted against it". They agree that behavior drift breaks products: "Code that is deployed to users might simply break if the model underneath changes its behavior" [VERIFIED: https://www.normaltech.ai/p/is-gpt-4-getting-worse-over-time, published 2023-07-19].

**Durable vs volatile.** Durable: the same named service can change behavior between versions; format compliance and refusal behavior are especially fragile; an evaluation that confuses format with correctness produces misleading drift signals. Volatile: the specific numbers.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. For agents, the fragile parts are exactly the ones the system depends on: tool-call format, schema adherence, refusal rates and instruction following. Validate them structurally at the boundary (schemas, structured outputs) and track them as production metrics, not only in offline evals. Design drift checks that separate "the output format changed" from "the answer got worse".

---

### 2.4 Two dated vendor postmortems

**OpenAI, GPT-4o sycophancy, April 2025** [WIDELY REPORTED: https://simonwillison.net/2025/May/2/what-we-missed-with-sycophancy/, 2025, quoting OpenAI's "Expanding on what we missed with sycophancy" of 2025-05-02; primary at https://openai.com/index/expanding-on-sycophancy/ returned 403]

- Timeline: the GPT-4o update in ChatGPT launched on 25 April 2025; system-prompt mitigations were pushed on the night of 27 April; OpenAI rolled back to the previous GPT-4o version on 28 April; the expanded postmortem appeared on 2 May.
- Cause, as OpenAI described it: candidate improvements that "had looked beneficial individually" combined; the update added "an additional reward signal based on user feedback—thumbs-up and thumbs-down data from ChatGPT", which weakened the primary reward signal that had held sycophancy in check. OpenAI also said "user memory contributes to exacerbating the effects of sycophancy" in some cases.
- Detection: offline evaluations "generally looked good" and A/B tests suggested users liked the model; expert testers' "vibe checks" said it "felt" slightly off. Search excerpts of the primary post say sycophancy "wasn't explicitly flagged" in hands-on testing and there were no "specific deployment evaluations tracking sycophancy" [WIDELY REPORTED: https://openai.com/index/expanding-on-sycophancy/, 2025].
- Commitments: "We need to treat model behavior issues as launch-blocking like we do other safety risks", add sycophancy evaluations, and communicate model updates proactively.
- Scope note: this was a ChatGPT product update, not an API snapshot change [ASSUMPTION/JUDGEMENT based on the posts describing "GPT-4o in ChatGPT"].

**Anthropic, three infrastructure bugs, August–September 2025** [VERIFIED: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues, published 2025-09-17]

- "We never reduce model quality due to demand, time of day, or server load." The problems "were due to infrastructure bugs alone".
- **Context-window routing error**: from 5 August some Sonnet 4 requests went to servers configured for the upcoming 1M-token context window, initially 0.8% of requests; a 29 August load-balancing change raised that, peaking at 16% of Sonnet 4 requests in the worst hour on 31 August. About 30% of Claude Code users who made requests in the period had at least one misrouted message. Routing was "sticky". Fixed 4 September; rollout finished 16 September (first party, Vertex AI) and 18 September (Bedrock).
- **Output corruption**: a TPU misconfiguration deployed 25 August caused some tokens to get unexpectedly high probability (for example Thai or Chinese characters in English answers) on Opus 4.1, Opus 4 and Sonnet 4; rolled back 2 September.
- **Approximate top-k XLA:TPU miscompilation**: a 25 August change to token selection triggered a latent compiler bug, confirmed on Haiku 3.5 and possibly on Sonnet 4 and Opus 3; rolled back 4 and 12 September.
- Why detection was slow: evaluations "did not capture the degradation users reported", partly because Claude often recovers from isolated mistakes; privacy controls limit engineers' access to user interactions; each bug showed different symptoms on different platforms; and a spike in reports on 29 August was not immediately tied to the load-balancing change.
- Commitments: more sensitive evaluations, "continuous quality evaluations on true production systems", faster privacy-preserving debugging of user feedback, and continued feedback channels (`/bug` in Claude Code, thumbs-down in apps).

**What the two incidents share** [ASSUMPTION/JUDGEMENT]. In both cases offline evaluations passed while users noticed. In one case the change was to the model's training signal; in the other the model was unchanged and the serving infrastructure changed. In both, the first reliable signal came from users, and the remedy included production-time evaluation. Neither incident was caused by the customer's own code, so a customer's own regression suite is the only control they hold.

**Durable vs volatile.** Durable: quality regressions can come from the provider's training, configuration, routing or compilers without a model-ID change; offline evals miss them; user feedback and production probes catch them. Volatile: the models, percentages and dates.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Run a small, fixed canary evaluation against production endpoints on a schedule (hourly or daily), with per-model and per-platform results, so that an upstream regression shows up as a step change in your own metric. Capture user feedback with enough trace context (model ID, platform, region, prompt version) to correlate it. Keep a second provider or platform route warm for agents where a quality regression is a business incident, and decide in advance who can switch it.

---

### 2.5 Hidden technical debt and testing for ML systems

- Sculley et al. (Google, NIPS 2015) list ML-specific risk factors: "boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, changes in the external world, and a variety of system-level anti-patterns" [VERIFIED: https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html, published 2015]. Evidence age: 2015, pre-LLM; the categories map well onto agents.
- Breck et al. (Google, IEEE Big Data 2017) propose "28 specific tests and monitoring needs" as a rubric for production readiness [VERIFIED: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, published 2017].

**Mapping to agentic systems** [ASSUMPTION/JUDGEMENT]

| Sculley risk factor | Agentic equivalent |
| --- | --- |
| Entanglement (a change to one input changes everything downstream) | Editing one line of a system prompt changes tool selection, tone and refusals at once |
| Hidden feedback loops | Agent output written to a knowledge base later retrieved as context; OpenAI's thumbs-up reward signal (§2.4) is a feedback loop at the provider |
| Undeclared consumers | Downstream services parsing free-text agent output |
| Data dependencies | Retrieval indexes, tool APIs and MCP servers whose content or schemas change |
| Configuration issues | Prompts, tool lists, effort levels, model IDs and policies held in configuration, often unreviewed |
| Changes in the external world | Provider model retirements, price changes, API versions, upstream infra bugs |

**Durable vs volatile.** Durable: the system around the model accumulates debt faster than the model code. Volatile: nothing here; this is the most durable section in the brief.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Use the ML Test Score idea, a scored readiness rubric, adapted to agents: tool-schema contract tests, prompt-change regression evals, cost and latency budgets, drift monitors, a rollback path and an owner for each.

---

### 2.6 Canary, shadow and progressive release for models and prompts

- Google's SRE workbook defines canarying as "a partial and time-limited deployment of a change in a service and its evaluation", which is "effectively an A/B testing process". It advises a canary large and long enough to be representative, one canary at a time, a small set of attributable metrics, and concurrent canary-vs-control comparison rather than before/after, which it calls "risky" because time itself changes metrics. It notes that a majority of incidents are triggered by binary or configuration pushes, so configuration deserves the same scrutiny [VERIFIED: https://sre.google/workbook/canarying-releases/, published 2018].
- AWS SageMaker shadow tests route "a copy of the inference requests" to a shadow variant; "Only the responses of the production variant are returned to the calling application", and shadow responses can be logged for offline comparison [VERIFIED: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html, n.d., accessed 2026-10].
- Anthropic uses "rainbow deployments to avoid disrupting running agents", gradually shifting traffic from old to new versions while both run, because long-running agents hold state mid-task [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].

**Agent-specific constraints** [ASSUMPTION/JUDGEMENT]

| Technique | Works for agents when… | Breaks when… |
| --- | --- | --- |
| Shadow | The agent's actions are read-only or can be stubbed; compare plans and tool calls, not just final text | The agent writes, sends, pays or books: a shadow copy must not execute side effects |
| Canary | Metrics are attributable per task and the canary cohort is pinned per session | A session flips between versions mid-task (state and cache mismatch) |
| Rainbow / version-per-session | Long-running tasks must finish on the version they started on | Old versions are retired before in-flight tasks finish |
| Before/after comparison | Never recommended as the primary signal (SRE workbook) | Weekly traffic patterns and upstream provider changes confound it |

**Durable vs volatile.** Durable: progressive exposure with concurrent control; shadowing for read-only paths; version stickiness for stateful work. Volatile: specific platform features.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Pin a task or session to one configuration tuple (§2.2) for its whole life. A prompt or model change goes through shadow (replay or live, side effects stubbed), then a small canary with task-success, cost-per-task, escalation-rate and refusal-rate metrics, then ramp. Caching interacts with canaries: a new prompt version starts cold, so canary cost and latency look worse for the first minutes; compare after warm-up.

---

### 2.7 Feature flags and configuration-as-code for prompts and policies

- Hodgson's taxonomy (on martinfowler.com) distinguishes release, experiment, ops and permissioning toggles by longevity and dynamism; it warns that "Savvy teams view the Feature Toggles in their codebase as inventory which comes with a carrying cost" and suggests expiry dates, "time bombs" and caps on active flags [VERIFIED: https://martinfowler.com/articles/feature-toggles.html, published 2017-10-09].
- LaunchDarkly's AgentControl (formerly AI Configs) lets teams "manage prompts, instructions, and model settings outside of application code", serve variations by targeting rules, "roll out changes gradually and safely" and track "generation count, token usage, latency, errors, and evaluation scores" [VERIFIED: https://launchdarkly.com/docs/home/agentcontrol, n.d., accessed 2026-10]. Vendor documentation; the product was renamed recently ⚠.
- Counter-evidence for vendor-hosted prompt stores: OpenAI is shutting down reusable prompts (`v1/prompts`), its Evals platform and Agent Builder on 2026-11-30 and advises to "Move prompts into app code" [VERIFIED: https://developers.openai.com/api/docs/deprecations, n.d., accessed 2026-10].

**Tension** [ASSUMPTION/JUDGEMENT]. Runtime flags let operators change a prompt or model in seconds, which is good for kill switches and gradual rollouts. They also move behavior-defining text out of code review, version control and the eval pipeline. The SRE workbook's point that configuration pushes cause incidents (§2.6) applies with full force to prompts.

**Durable vs volatile.** Durable: prompts, tool lists and policies are configuration that changes behavior and needs versioning, review, testing, progressive rollout and rollback; flags carry debt. Volatile: products and their names.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Keep the source of truth for prompts, tool policies and agent definitions in version control, reviewed and evaluated in CI like code. Use a flag or configuration service only to *select* among reviewed versions and to hold ops toggles (kill switch, model fallback, lower effort under load). Give every flag an owner and an expiry. Log the resolved versions on every trace.

---

### 2.8 Ownership and operating model

- Microsoft's Cloud Adoption Framework recommends that organizations early in AI adoption use a centralized AI Center of Excellence, then move "from a centralized control to an advisory team". It says to "Transfer AI delivery to the platform teams" so they "enforce consistent governance, manage reliable deployments, and help ensure secure delivery", and to "Replace the CoE gatekeeper model that blocks work with an advisory group that sets guardrails", distributing expertise into product, platform and enabling teams. It warns against creating a standalone AI team unless existing teams cannot support adoption [VERIFIED: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence, ms.date 2025-06-09, updated 2026-10-15].
- The DORA 2025 report says "AI doesn't fix a team; it amplifies what's already there"; reports that 90% of respondents use AI at work; finds a positive relationship between AI adoption and delivery throughput but a continued negative relationship with delivery stability; and reports that 90% of organizations have adopted at least one internal platform, with "a direct correlation between a high quality internal platform and an organization's ability to unlock the value of AI". The survey covered nearly 5,000 technology professionals [VERIFIED: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report, published 2025-09-23]. Survey evidence of correlation, not causation; about AI-assisted *software development*, not agentic products specifically.
- Claude Code's docs show the cost controls a platform team ends up owning: workspace spend limits, per-user analytics, contracted-rate reporting via managed settings, OpenTelemetry export, and an LLM gateway for per-key spend [VERIFIED: https://code.claude.com/docs/en/costs, n.d., accessed 2026-10].

**A suggested split** [ASSUMPTION/JUDGEMENT]

| Concern | Platform / AI enablement team | Product (stream-aligned) team |
| --- | --- | --- |
| Provider contracts, keys, workspaces, rate-limit allocation | Owns | Requests quota |
| Model gateway, caching defaults, routing infrastructure, cost attribution | Owns | Uses; sets per-route model choice |
| Model migration calendar and usage audit | Owns the calendar and audit | Owns migration of its own agents |
| Production canary evals for upstream drift | Owns shared probes | Owns task-specific evals |
| Prompts, tools and policies for a given agent | Provides templates and CI checks | Owns content and outcomes |
| Kill switches and fallbacks | Provides mechanism | Decides when to use them for its agent |

**Durable vs volatile.** Durable: centralize the scarce, shared and contractual parts (keys, quotas, gateways, cost data, migration calendar); keep behavior and outcomes with the team that owns the product; evolve from gatekeeping to guardrails. Volatile: survey percentages and vendor tooling.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The economic and evolution concerns in this brief need an owner outside any one agent: someone must hold the price tables, the migration calendar, the shared rate-limit budget and the upstream drift probes. Without that owner, each product team rediscovers retirement notices 60 days before the deadline.

---

## Key numbers

| Number | What it measured | Source | Date |
| --- | --- | --- | --- |
| 1.25× / 2× / 0.1× | Anthropic cache write (5 min) / write (1 h) / read multipliers on base input (read 0.05× on Opus and Sonnet 5.5; 0.025× on Fable/Mythos 5.1) ⚠ | platform.claude.com prompt-caching | accessed 2026-10 |
| 512–4,096 tokens | Anthropic minimum cacheable prefix, by model ⚠ | same | accessed 2026-10 |
| 4 / 20 | Anthropic max cache breakpoints / lookback blocks per breakpoint ⚠ | same | accessed 2026-10 |
| 1,024 tokens; 0.1× read; 1.25× (30 min) / 2.5× (12 h) write | OpenAI caching on GPT-5.6+ ⚠ | developers.openai.com prompt-caching | accessed 2026-10 |
| ~15 RPM per key | OpenAI threshold above which overflow routing can cause cache misses ⚠ | same | accessed 2026-10 |
| 4,096 tokens; 2,050-token rule | Gemini implicit-cache minimum on Argon/3.x; multi-turn re-cache threshold on Argon+ ⚠ | ai.google.dev caching | updated 2026-10-23 |
| 50% | Batch discount at Anthropic, OpenAI (also Flex) and Google ⚠ | three pricing pages | accessed 2026-10 |
| 100,000 req / 256 MB / 24 h / 29 days | Anthropic batch size limits, expiry, result retention ⚠ | batch-processing docs | accessed 2026-10 |
| 2× price, up to 2.5× OTPS | Anthropic fast mode on Opus 5.5; OTPS not TTFT ⚠ | fast-mode docs | accessed 2026-10 |
| 2× / 1.8× | OpenAI Fast and Gemini Priority premiums over standard ⚠ | pricing pages | accessed 2026-10 |
| $2.00 → $4.00 | Gemini 4 Argon input price per MTok, scheduled rise on 2026-12-01 ⚠ | ai.google.dev pricing | updated 2026-10-27 |
| 1.1× | Anthropic US-only inference multiplier (Claude 4.6+) ⚠ | pricing docs | accessed 2026-10 |
| 2M ITPM × 80% hit → 10M | Anthropic example: cached reads do not count toward ITPM on most models ⚠ | rate-limits docs | accessed 2026-10 |
| ~100:1 | Input-to-output token ratio in the Manus agent | Manus blog | 2025-07-18 |
| 4× / 15× | Tokens used by agents / multi-agent systems relative to chat (Anthropic Research system) | Anthropic engineering | 2025-06-13 |
| 90.2% | Multi-agent (Opus 4 + Sonnet 4) over single-agent Opus 4 on an internal research eval | same | 2025-06-13 |
| 80% / 95% | BrowseComp performance variance explained by token usage / by tokens + tool calls + model | same | 2025-06-13 |
| ~7× | Claude Code agent-team tokens vs standard sessions, teammates in plan mode | code.claude.com costs | accessed 2026-10 |
| ~$13 / day; $150–250 / month; 90% < $30 / day | Claude Code enterprise average cost per developer (population and period unstated) ⚠ | same | accessed 2026-10 |
| 150k → 2k tokens (98.7%) | One illustrative MCP-as-code example | Anthropic engineering | 2025-11-04 |
| up to 98% | FrugalGPT cost reduction while matching the best single LLM, 2023 models | arXiv 2305.05176 | 2023-05-09 |
| > 2× | RouteLLM cost reduction "in certain cases" | arXiv 2406.18665 | 2024-06/2025-02 |
| 93.2% at $2.45 vs 88.0% at $134.50 | Simple warming baseline vs LATS on HumanEval (GPT-4) | arXiv 2407.01502 | 2024-07-01 |
| 3.7× / 6.7× / ~9% | LLMCompiler latency, cost, accuracy gains over ReAct | arXiv 2312.04511 (ICML 2024) | 2023-12/2024-06 |
| 2–3× | Speculative decoding speedup on T5-XXL, identical outputs | arXiv 2211.17192 (ICML 2023) | 2022-11 |
| 55% / 20% | Speculative actions: next-action prediction accuracy / latency reduction (upper bounds) | arXiv 2510.04371 | 2025-10-05 |
| ~50% vs 1–5% | OpenAI heuristic: latency gain from halving output vs halving prompt | OpenAI latency guide | accessed 2026-10 |
| ≥ 60 days | Anthropic retirement notice for publicly released models ⚠ | model-deprecations | accessed 2026-10 |
| ≥ 6 months / ≥ 3 months / ~2 weeks | OpenAI notice for GA / specialized / preview models ⚠ | OpenAI deprecations | accessed 2026-10 |
| ≥ 2 weeks | Gemini preview-model deprecation notice ⚠ | ai.google.dev models | updated 2026-10-22 |
| 84% → 51% | GPT-4 prime-number accuracy, March → June 2023 (test set all primes; see critique) | arXiv 2307.09009 | 2023-07-18 |
| 0.8% → 16% | Share of Sonnet 4 requests misrouted, 5 Aug → worst hour 31 Aug 2025 | Anthropic postmortem | 2025-09-17 |
| ~30% | Claude Code users with at least one misrouted message in that period | same | 2025-09-17 |
| 25 → 28 April 2025 | GPT-4o sycophancy update launch → rollback | OpenAI via Willison | 2025-05-02 |
| 28 | Tests and monitoring needs in the ML Test Score rubric | Breck et al. | 2017 |
| 90% / ~5,000 | DORA 2025: respondents using AI at work / survey size | Google Cloud blog | 2025-09-23 |

---

## Where sources disagree

1. **Is drift capability loss or behavior change?** Chen, Zaharia and Zou (2023) report large drops on some tasks; Narayanan and Kapoor (2023) show the prime-number set was all primes and the code test measured format, and argue capability was largely unchanged. Both agree behavior changes break products. Chapters should say "behavior drift" and avoid "the model got dumber".
2. **Do multi-agent systems save or spend?** Anthropic reports 15× chat tokens for a 90.2% gain and recommends them only for high-value, parallelizable work; *AI Agents That Matter* shows simple single-model baselines matching complex agents at a fraction of the cost. They measure different tasks; the shared lesson is to compare against a simple baseline on cost and accuracy together.
3. **Cheaper model or more tokens?** Routing papers (FrugalGPT, RouteLLM) and vendor guidance favour smaller models for easy queries; Anthropic found a model upgrade beat doubling the token budget. Routing helps when a reliable difficulty signal exists; otherwise cheap-model retries can cost more.
4. **Does input length matter for latency?** OpenAI's guide says halving the prompt may only gain 1–5% latency; Anthropic's context-engineering post stresses context rot (quality, not latency) and n² attention. With caching and 1M-token windows, the older heuristic is likely too optimistic for very long agent contexts [ASSUMPTION/JUDGEMENT].
5. **Cache write pricing.** Anthropic has always charged a write premium; OpenAI charged nothing until GPT-5.6, and now charges 1.25×–2.5×; Google lists no write charge for Argon's implicit caching. A cost model that assumes free writes is wrong for two of three providers' current models.
6. **Notice periods in practice vs policy.** OpenAI's stated GA policy is at least six months, but the 2026-10-14 notice for specific GPT-4o/GPT-4.1 snapshots gives about three months; the page may classify those snapshots as non-GA. Anthropic's practice has converged on its 60-day floor.
7. **Where prompts should live.** LaunchDarkly positions runtime prompt configuration outside code; OpenAI is retiring its hosted prompt store and tells users to move prompts into app code. Both can be right: a runtime selector over versioned, reviewed prompts.

---

## Open questions / not verifiable

- OpenAI's text of the two GPT-4o sycophancy posts could not be read directly (HTTP 403); the details rely on Simon Willison's quotation and search excerpts.
- Whether Anthropic's 1-hour cache TTL refreshes on hit is not stated explicitly in the docs.
- Gemini explicit-cache default TTL was not on the pages fetched.
- OpenAI's alias-vs-snapshot guidance and current rate-limit tiers were not fetched; Flex-tier latency behavior is unverified.
- Whether any provider uses speculative decoding to implement its fast tier is not stated in the pages fetched.
- The population, period and model mix behind Claude Code's "$13 per developer per active day" are not stated.
- RouteLLM's venue (often cited as ICLR 2025) is not shown on its arXiv page.
- The DORA 2025 AI Capabilities Model's seven capabilities were not enumerated (image only).
- No public, dated production writeup was found that reports an agent's cost per task, cache hit rate and model-routing mix together over time. Chapter writers should present cost models as reference-architecture arithmetic.
- No public postmortem was found of a customer-side agent incident caused by a provider model retirement or migration.

---

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Prompt caching | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | docs |
| Pricing | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/about-claude/pricing | docs |
| Batch processing | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/batch-processing | docs |
| Fast mode | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/fast-mode | docs |
| Service tiers | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/api/service-tiers | docs |
| Rate limits | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/api/rate-limits | docs |
| Parallel tool use | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use | docs |
| Models overview | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/about-claude/models/overview | docs |
| Model deprecations | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/about-claude/model-deprecations | docs |
| Manage costs effectively (Claude Code) | Anthropic | n.d. (accessed 2026-10) | https://code.claude.com/docs/en/costs | docs |
| How we built our multi-agent research system | Anthropic | 2025-06-13 | https://www.anthropic.com/engineering/multi-agent-research-system | engineering post |
| Effective context engineering for AI agents | Anthropic | 2025-09-29 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | engineering post |
| Code execution with MCP | Anthropic | 2025-11-04 | https://www.anthropic.com/engineering/code-execution-with-mcp | engineering post |
| Building effective agents | Anthropic | 2024-12-19 (edited since) | https://www.anthropic.com/engineering/building-effective-agents | engineering post |
| A postmortem of three recent issues | Anthropic | 2025-09-17 | https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues | incident report |
| Commitments on model deprecation and preservation | Anthropic | 2025-11-04 | https://www.anthropic.com/research/deprecation-commitments | policy statement |
| Prompt caching | OpenAI | n.d. (accessed 2026-10) | https://developers.openai.com/api/docs/guides/prompt-caching | docs |
| Pricing | OpenAI | n.d. (accessed 2026-10) | https://developers.openai.com/api/docs/pricing | docs |
| Latency optimization | OpenAI | n.d. (accessed 2026-10) | https://developers.openai.com/api/docs/guides/latency-optimization | docs |
| Deprecations | OpenAI | n.d. (accessed 2026-10) | https://developers.openai.com/api/docs/deprecations | docs |
| Expanding on what we missed with sycophancy | OpenAI (read via Simon Willison) | 2025-05-02 | https://openai.com/index/expanding-on-sycophancy/ ; https://simonwillison.net/2025/May/2/what-we-missed-with-sycophancy/ | incident report / commentary |
| Context caching | Google | updated 2026-10-23 | https://ai.google.dev/gemini-api/docs/caching | docs |
| Gemini Developer API pricing | Google | updated 2026-10-27 | https://ai.google.dev/gemini-api/docs/pricing | docs |
| Gemini models | Google | updated 2026-10-22 | https://ai.google.dev/gemini-api/docs/models | docs |
| Gemini deprecations | Google | updated 2026-10-22 | https://ai.google.dev/gemini-api/docs/deprecations | docs |
| Context Engineering for AI Agents: Lessons from Building Manus | Yichao "Peak" Ji, Manus | 2025-07-18 | https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus | engineering post |
| FrugalGPT | Chen, Zaharia, Zou | 2023 | https://arxiv.org/abs/2305.05176 | paper (preprint) |
| RouteLLM: Learning to Route LLMs with Preference Data | Ong et al. | 2024–2025 | https://arxiv.org/abs/2406.18665 | paper (preprint) |
| AI Agents That Matter | Kapoor, Stroebl, Siegel, Nadgir, Narayanan | 2024 | https://arxiv.org/abs/2407.01502 | paper (preprint) |
| Small Language Models are the Future of Agentic AI | Belcak et al. | 2025–2026 | https://arxiv.org/abs/2506.02153 | paper (position, preprint) |
| An LLM Compiler for Parallel Function Calling | Kim et al. | 2023–2024 | https://arxiv.org/abs/2312.04511 | paper (ICML 2024) |
| Fast Inference from Transformers via Speculative Decoding | Leviathan, Kalman, Matias | 2022–2023 | https://arxiv.org/abs/2211.17192 | paper (ICML 2023) |
| Speculative Actions: A Lossless Framework for Faster Agentic Systems | Ye et al. | 2025–2026 | https://arxiv.org/abs/2510.04371 | paper (preprint; ICLR 2026 per conference site) |
| The Tail at Scale | Dean, Barroso | 2013 | https://research.google/pubs/the-tail-at-scale/ | paper (CACM) |
| How is ChatGPT's behavior changing over time? | Chen, Zaharia, Zou | 2023 (HDSR 2024) | https://arxiv.org/abs/2307.09009 | paper |
| Is GPT-4 getting worse over time? | Narayanan, Kapoor | 2023-07-19 | https://www.normaltech.ai/p/is-gpt-4-getting-worse-over-time | commentary |
| Hidden Technical Debt in Machine Learning Systems | Sculley et al. | 2015 | https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html | paper (NIPS) |
| The ML Test Score | Breck, Cai, Nielsen, Salib, Sculley | 2017 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | paper (IEEE Big Data) |
| Canarying Releases (SRE Workbook) | Google / O'Reilly | 2018 | https://sre.google/workbook/canarying-releases/ | book chapter |
| Shadow tests | AWS | n.d. (accessed 2026-10) | https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html | docs |
| Feature Toggles (aka Feature Flags) | Pete Hodgson, martinfowler.com | 2017-10-09 | https://martinfowler.com/articles/feature-toggles.html | article |
| AgentControl | LaunchDarkly | n.d. (accessed 2026-10) | https://launchdarkly.com/docs/home/agentcontrol | docs (vendor) |
| Establish an AI Center of Excellence | Microsoft | 2025-06-09, updated 2026-10-15 | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence | docs (guidance) |
| Announcing the 2025 DORA report | Google Cloud | 2025-09-23 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | press / survey summary |
