# Research brief: Context, retrieval, memory and state in agentic systems

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief covers what an agent can see (context), how it finds what it cannot hold (retrieval), what it keeps between sessions (memory), and what the system keeps so work can resume, be audited or be rolled back (state). It is vendor-neutral. Anthropic, LangGraph and Google ADK appear most often because their documentation states the relevant distinctions plainly and was fetchable. That is not an endorsement.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date. Undated vendor documentation is marked "n.d., accessed 2026-10". For arXiv papers the date is the v1 submission date, and later revisions are noted where they matter.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, conference summary), not from the originator's own technical text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Source types.** Each source is labelled in the source list as a peer-reviewed paper, preprint, vendor documentation, vendor engineering post, vendor research report, security research blog, standard/spec or press. Vendor research reports (Chroma's "Context Rot", the Mem0 paper) are written by companies that sell a related product. They are useful but are not independent.

**Evidence age matters.** This field moves fast. Several foundational papers tested models that are now retired. *Lost in the Middle* (2023) tested GPT-3.5-Turbo and Claude 1.3. RULER (2024) and the RAG paper (2020) also predate current models. Their *mechanisms* (position sensitivity, distraction, effective context shorter than advertised) have been re-observed in 2025 work on newer models, but their *numbers* describe superseded systems. Do not quote a 2023 percentage as a property of a 2026 model. Sources older than about 18 months (before roughly April 2025) are flagged "**Age:**" in the text.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: API beta headers, tool type strings, feature names, model lists, product rollout regions.

**Research limitation.** The session relied on direct fetches, with very few web searches. As a result:

- OpenAI's own memory announcement and memory FAQ returned HTTP 403. ChatGPT memory is described from press coverage (TechCrunch) and from a security researcher's write-up, not from OpenAI's text.
- OWASP's *Agentic AI – Threats and Mitigations* (Feb 2025) landing page was fetched, but its downloadable PDF, which holds the threat list (including memory poisoning), was not read. Microsoft's failure-mode taxonomy was read only through its announcement blog; the whitepaper's memory-poisoning case study numbers were not verified.
- Letta's current documentation was read only at the overview level. Archival memory, recall memory and sleep-time agents are described from MemGPT's paper and from analyst knowledge.
- Several arXiv abstract pages do not list venues. Where the analyst believes a venue (for example UIST 2023 for Generative Agents) but did not see it, the venue is tagged ASSUMPTION.
- Anthropic's "Compaction at a token threshold" sub-page was not fetched; its behaviour is described from the compaction overview and the context-editing page.
- No production incident report describing memory poisoning *at a real customer* was found. All poisoning evidence is from research settings or researcher proofs of concept.

---

## PART 1: Vocabulary — four kinds of "what the agent knows"

### 1.1 The distinctions the book should hold fixed

The words "memory", "context" and "state" are used loosely across vendors. The book needs fixed terms. The table below is the analyst's synthesis; the sources that follow show that the major frameworks draw the same lines, with different names.

| Term (book usage) | What it is | Lifetime | Who writes it | Typical store | Failure if wrong |
| --- | --- | --- | --- | --- | --- |
| **Conversation history** | The ordered record of messages, tool calls and tool results in one session | One session/thread | The runtime appends; nobody edits | Event log, message table, checkpoint | Lost turns; unreproducible behaviour |
| **Working context** | The tokens actually sent to the model on this call | One model call | The harness assembles it (selection, compaction, retrieval) | Nowhere; it is computed | Distraction, context rot, missing facts |
| **Durable task state** | Structured progress of the task: plan, step, pending approvals, side effects done | Until the task ends (plus audit retention) | The orchestrator, deterministically | Checkpointer / workflow engine / database | Duplicate side effects; cannot resume or roll back |
| **Long-term memory** | Facts, preferences, lessons kept across sessions and tasks | Indefinite, subject to retention policy | Often the model itself, sometimes a background process | Files, KV/JSON store, vector store | Stale or poisoned beliefs that persist |
| **Knowledge corpus** (retrieval source) | Documents the agent searches but does not own | Owned by another system | Content owners | Search index, vector DB, APIs | Wrong, stale or injected evidence |

[ASSUMPTION/JUDGEMENT] The table is a synthesis. The sources below draw the same lines:

- Google's Agent Development Kit separates a **Session** ("a _single, ongoing interaction_ between a user and your agent system"), its **Events** ("the chronological sequence of messages and actions taken by the agent"), **State** ("Data stored within a specific `Session`") and **Memory** ("a store of information that might span _multiple past sessions_ or include external data sources"), served by a separate `MemoryService` that ingests information "often from completed `Session`s" [VERIFIED: https://adk.dev/sessions/, n.d., accessed 2026-10].
- LangGraph separates **checkpointers**, which "persist a thread's graph state as checkpoints" (short-term, thread-scoped), from **stores**, which hold application-defined data for long-term memory shared across threads [VERIFIED: https://docs.langchain.com/oss/python/langgraph/persistence, n.d., accessed 2026-10].
- LangGraph's memory guide states that "LangGraph manages short-term memory as a part of your agent's state", while long-term memories "are scoped to any custom namespace, not just within a single thread ID" [VERIFIED: https://docs.langchain.com/oss/python/langgraph/memory, n.d., accessed 2026-10].
- Anthropic's context-editing feature applies edits server-side "before the prompt reaches Claude", and the client "keeps the full, unmodified history". This separates the conversation history (kept in full by the client) from the working context (edited per call) [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10].
- Letta (MemGPT's successor) says all state, "including messages, reasoning, and tool calls", is stored in a database, and older messages stay retrievable after compaction or eviction [VERIFIED: https://docs.letta.com/guides/agents/memory, n.d., accessed 2026-10].

### 1.2 The key separation: history is not context, and memory is not state

[ASSUMPTION/JUDGEMENT] Two confusions cause most design errors in this area:

1. **Treating the conversation history as the working context.** Appending everything and resending it makes cost grow with each turn and quality fall (Part 2). The working context should be *computed* from history, state, memory and retrieval on each call, and the history kept in full elsewhere for audit and replay.
2. **Treating model-written memory as task state.** A model's note "step 3 done" is a belief, not a fact. Whether a refund was issued, an email sent or a migration applied must be recorded by the deterministic orchestrator from the tool's actual result, in a store the model cannot overwrite. Anthropic's own harness work keeps a feature list in JSON that coding agents may only flip (`passes`) because "models are less likely to inappropriately alter" JSON than Markdown (see 3.3). That is a soft version of this rule; regulated domains (finance operations, healthcare, public benefits) need the hard version.

**Durable vs volatile.** The four-way distinction is durable; it is ordinary systems design (log, cache, transaction state, user profile). Names (Session/Thread, State/Checkpoint, Memory/Store) are framework-specific and volatile.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Give each of the four its own store, owner, retention rule and access control. Make the working context a pure function of them that can be logged per call, so any decision can be reconstructed. Never let the model be the only writer of anything that records a side effect.

---

## PART 2: Long-context limits — why "just put it all in the window" fails

### 2.1 Lost in the Middle (2023)

- Liu et al. measured how model accuracy changes with the *position* of the relevant information in a long input, on multi-document question answering and a synthetic key-value retrieval task [VERIFIED: https://arxiv.org/abs/2307.03172, published 2023-07-06].
- Accuracy was often highest when the relevant document was at the start or end of the context and dropped when it was in the middle (the "U-shape"). The authors conclude that "current language models do not robustly make use of information in long input contexts" [VERIFIED: https://arxiv.org/abs/2307.03172, published 2023-07-06].
- Models tested: MPT-30B-Instruct, LongChat-13B (16K), GPT-3.5-Turbo and its 16K variant, Claude-1.3 and Claude-1.3 (100K); GPT-4 only on a subset because full evaluation would have cost "upwards of $6,000" [VERIFIED: https://arxiv.org/html/2307.03172, published 2023-07-06].
- Context sizes: 10, 20 and 30 retrieved documents. GPT-3.5-Turbo scored 56.1% closed-book (no documents). With 20 documents and the answer-bearing document at position 9, it fell to 53.8%, *below* closed-book. In the 30-document setting the 16K model fell to 50.5% versus 56.0% closed-book [VERIFIED: https://arxiv.org/html/2307.03172, published 2023-07-06].
- Query-aware contextualization (putting the question before and after the documents) made key-value retrieval near-perfect but had minimal effect on multi-document QA [VERIFIED: https://arxiv.org/html/2307.03172, published 2023-07-06].
- Limitations the authors state: greedy decoding only; a temporal mismatch between NaturalQuestions-Open and the 2018 Wikipedia dump; some distractor passages may contain plausible answers; the key-value task is synthetic [VERIFIED: https://arxiv.org/html/2307.03172, published 2023-07-06].
- Published in TACL (2023/2024) [VERIFIED: https://arxiv.org/abs/2307.03172, published 2023-07-06].

**Age:** all tested models are retired. Treat the numbers as historical. The finding that matters for architecture is that *adding retrieved documents can make answers worse than adding none*.

### 2.2 RULER: effective context is shorter than claimed (2024)

- RULER extends needle-in-a-haystack (NIAH) with multiple needle types and counts, multi-hop tracing and aggregation: 13 tasks in total [VERIFIED: https://arxiv.org/abs/2404.06654, published 2024-04-09].
- Of 17 long-context models, all scored near-perfect on vanilla NIAH, but "only half of them can maintain satisfactory performance at the length of 32K", although all claimed 32K or more [VERIFIED: https://arxiv.org/abs/2404.06654, published 2024-04-09].
- Published at COLM 2024 [VERIFIED: https://arxiv.org/abs/2404.06654, published 2024-04-09].

**Age:** 2024 models. The durable lesson is methodological: simple needle tests overstate usable context. ⚠ Advertised context windows have grown since; this brief did not verify any current model's effective length.

### 2.3 NoLiMa: without literal overlap, performance collapses earlier (2025)

- NoLiMa builds needles with minimal lexical overlap with the question, so the model must infer a latent association rather than match words. The authors argue that existing benchmarks let models exploit literal matches [VERIFIED: https://arxiv.org/abs/2502.05167, published 2025-02-07].
- 13 LLMs claiming at least 128K context were tested. At 32K tokens, 11 of 13 fell below half of their short-context (<1K) baseline. GPT-4o fell from 99.3% to 69.7% [VERIFIED: https://arxiv.org/abs/2502.05167, published 2025-02-07].
- Reasoning-enhanced models and chain-of-thought prompting still struggled [VERIFIED: https://arxiv.org/abs/2502.05167, published 2025-02-07].
- Accepted at ICML 2025 [VERIFIED: https://arxiv.org/abs/2502.05167, published 2025-02-07].
- The authors *attribute* the decline to attention having more difficulty retrieving without literal matches; this is an explanation from analysis, not a proven mechanism [VERIFIED: https://arxiv.org/abs/2502.05167, published 2025-02-07].

**Why this matters for agents.** [ASSUMPTION/JUDGEMENT] Agent context is rarely a literal lookup. "Which of the earlier tool results contradicts the customer's claim?" is an associative question. NoLiMa is closer to agent reality than vanilla NIAH.

### 2.4 Chroma "Context Rot" (2025)

- Chroma's technical report (Hong, Troynikov, Huber) tested 18 models from Anthropic (Claude Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5, Haiku 3.5), OpenAI (o3, GPT-4.1 family, GPT-4o, GPT-4 Turbo, GPT-3.5 Turbo), Google (Gemini 2.5 Pro/Flash, 2.0 Flash) and Alibaba (Qwen3 235B/32B/8B) [VERIFIED: https://www.trychroma.com/research/context-rot, published 2025-07-14].
- Findings: performance degrades faster with input length when the needle is less similar to the question; one distractor reduces performance and four reduce it further, with uneven effects by distractor; and, surprisingly, *shuffled* haystacks consistently beat coherent ones across all 18 models [VERIFIED: https://www.trychroma.com/research/context-rot, published 2025-07-14].
- On LongMemEval-style conversational memory (306 prompts), models did much better with focused prompts of about 300 tokens than with full prompts of about 113K tokens [VERIFIED: https://www.trychroma.com/research/context-rot, published 2025-07-14].
- In a repeated-words copying task, performance degraded with length for all models [VERIFIED: https://www.trychroma.com/research/context-rot, published 2025-07-14].
- Limitations the authors state: the tasks are simple, so real tasks with reasoning would likely degrade more; input length is confounded with task difficulty; mechanisms are not explained; needle-haystack similarity was tested on only two topics [VERIFIED: https://www.trychroma.com/research/context-rot, published 2025-07-14].

**Source type note.** This is a vendor research report from a vector-database company whose product benefits from the conclusion "retrieve, don't stuff". The method is published and the finding aligns with independent work (2.1–2.3), but it is not peer-reviewed.

### 2.5 Irrelevant context distracts reasoning

- Shi et al. built GSM-IC (grade-school maths with irrelevant sentences added) and found "performance is dramatically decreased when irrelevant information is included". Self-consistency decoding and an instruction to ignore irrelevant information partly mitigated this [VERIFIED: https://arxiv.org/abs/2302.00093, published 2023-01-31; ICML 2023].

**Age:** 2023 models. The durable point: the harm of extra context is not only cost; it is accuracy.

### 2.6 Long-term conversational memory: LongMemEval

- LongMemEval tests five memory abilities over long chat histories: information extraction, multi-session reasoning, temporal reasoning, knowledge updates and abstention, with 500 curated questions [VERIFIED: https://arxiv.org/abs/2410.10813, published 2024-10-14; ICLR 2025].
- Commercial chat assistants and long-context LLMs showed about a 30% accuracy drop when recalling information across sustained interactions [VERIFIED: https://arxiv.org/abs/2410.10813, published 2024-10-14].
- The authors decompose memory into indexing, retrieval and reading, and propose session decomposition, fact-augmented key expansion and *time-aware query expansion* [VERIFIED: https://arxiv.org/abs/2410.10813, published 2024-10-14].

[ASSUMPTION/JUDGEMENT] "Knowledge updates" and "temporal reasoning" being separate abilities is the evidence base for the book's freshness argument (Part 9). A memory that cannot tell the old address from the new one is worse than no memory.

### 2.7 Long context versus retrieval: the trade-off is cost as well as quality

- Li et al. (Google DeepMind/Michigan) found that, given enough resources, long-context LLMs outperform RAG on average on their benchmarks, while RAG costs much less. Their Self-Route method routes each query to RAG or long context based on the model's self-reflection, substantially cutting cost at comparable performance [VERIFIED: https://arxiv.org/abs/2407.16833, published 2024-07-23; EMNLP 2024 industry track].
- Anthropic advises that for a knowledge base under 200,000 tokens (about 500 pages), you can include the whole knowledge base in the prompt and skip RAG, using prompt caching to reduce cost [VERIFIED: https://www.anthropic.com/news/contextual-retrieval, published 2024-09-19].

### Part 2 synthesis

| Claim | Supported by | Strength |
| --- | --- | --- |
| Usable context is shorter than advertised context | RULER, NoLiMa, Context Rot | Strong; replicated across 2024–25 model generations |
| Position in context matters | Lost in the Middle | Strong for 2023 models; Context Rot found position made *no notable* difference in its needle test |
| Irrelevant or near-miss content hurts more than unrelated padding | GSM-IC, Context Rot (distractors), Lost in the Middle (below closed-book) | Strong |
| Long context can beat RAG on quality when cost is no object | Li et al. 2024 | Moderate; one study, 2024 models |

**Durable vs volatile.** Durable: context is a finite resource with diminishing and sometimes negative returns; relevance and distractor density matter more than length alone. Volatile: every specific threshold (32K, 128K) and percentage.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Budget the working context explicitly per call (a token budget per source: instructions, state summary, retrieved evidence, recent turns). Prefer fewer, higher-precision items over more recall. Evaluate your own agent at the context lengths it actually reaches in production, not at short lengths. Treat "the model has a 1M window" as a capacity limit, not a design.

---

## PART 3: Context engineering — compaction, notes and just-in-time retrieval

### 3.1 Anthropic's framing

- Anthropic's Applied AI team defines context engineering as "the set of strategies for curating and maintaining the optimal set of tokens" during inference, extending prompt engineering to everything that enters the window [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29].
- It states that "Context, therefore, must be treated as a finite resource with diminishing marginal returns" and that LLMs have an "attention budget" which every added token draws down [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29].
- The goal it states: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome" [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29].
- Techniques named: **just-in-time retrieval** (keep lightweight references such as file paths or queries and load data with tools only when needed); **compaction** (summarize a nearly full window and restart with the summary); **structured note-taking** (persist notes outside the window and reload them); **sub-agent architectures** (sub-agents work in clean windows and return condensed summaries); **tool-result clearing**, described as one of the lightest forms of compaction [VERIFIED: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, published 2025-09-29].

### 3.2 The API surface (Anthropic, as of October 2026) ⚠

- **Context editing** is in beta under header `context-management-2025-06-27` ⚠. Strategy `clear_tool_uses_20250919` clears the oldest tool results past a threshold and replaces each with placeholder text; defaults are a trigger of 100,000 input tokens and keeping 3 tool uses; `exclude_tools` protects named tools; `clear_at_least` avoids clearing too little to pay for the cache rewrite [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10].
- `clear_thinking_20251015` manages earlier thinking blocks ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10].
- Tool-result clearing **invalidates cached prompt prefixes** [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10]. This is a direct cost/quality trade-off.
- When combined with the memory tool, Claude receives a warning near the threshold so it can save important information to memory before results are cleared [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10].
- The context-editing page now recommends **server-side compaction** as the primary strategy for long conversations, with context editing for finer control. Client-side SDK compaction (`compaction_control`) is deprecated in TypeScript and Ruby and was removed in the Python SDK v1.0 ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10].
- Compaction "replaces the older turns of a conversation with a summary that Claude writes on the server", justified because "response quality degrades as a conversation grows" [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/compaction, n.d., accessed 2026-10].
- Two server modes exist, both beta: **compaction on demand** (the application decides when; beta header `compact-2026-09-04` and a top-level `compaction` parameter) and **compaction at a token threshold** (the API decides when input tokens reach a trigger). Options include keeping recent turns word for word and compacting in the background. A custom summarization prompt can replace the default "when the default summary drops something a later turn needs" ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/compaction, n.d., accessed 2026-10].
- The context-editing page names the server-side compaction edit `compact_20260112` within `context_management` ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/context-editing, n.d., accessed 2026-10]. The relationship between this edit and the threshold mode was not confirmed (sub-page not fetched).

[ASSUMPTION/JUDGEMENT] OpenAI, Google and the open frameworks offer comparable trimming/summarization features under different names; this brief did not verify them. Write chapters against the *mechanisms* (clear, summarize, offload, isolate), not these names.

### 3.3 Notes and harnesses: compaction is not enough

- Anthropic's harness post states that "compaction isn't sufficient": even Opus 4.5 looping across context windows fell short of building a production-quality web app from a high-level prompt [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].
- Its fix: an **initializer** session that creates an `init.sh`, a `claude-progress.txt` log, a JSON feature list (over 200 items for a claude.ai clone, all initially failing) and an initial git commit; then **coding** sessions that make incremental progress on one feature and leave structured updates [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].
- Coding agents may only change the `passes` field; JSON was chosen because models are "less likely to inappropriately alter" it than Markdown; "It is unacceptable to remove or edit tests" [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].
- Observed failure modes: **one-shotting** (trying to build too much, running out of context mid-implementation); **premature completion** (a later agent sees progress and declares the project done); **inadequate testing** (marking features complete after unit tests or `curl` without end-to-end checks) [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].
- Git commits act as recovery points: later agents can revert bad changes rather than guess what the previous session did [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].
- Anthropic's memory tool documentation turns this into a recommended "multisession software development pattern": initializer session, sessions that open by reading memory files, end-of-session progress updates, and "Mark a feature complete only after end-to-end verification confirms it works" [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].

### 3.4 Isolation by sub-agent and by artifact

- In Anthropic's multi-agent research system, the lead agent saves its plan to memory because "if the context window exceeds 200,000 tokens it will be truncated" [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].
- To avoid a "game of telephone", "Subagents call tools to store their work in external systems" and pass lightweight references back to the coordinator [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].
- Because agents are stateful, errors compound; the team "built systems that can resume from where the agent was when the errors occurred" [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].
- On their BrowseComp evaluation, "token usage by itself explains 80% of the variance" in performance; multi-agent systems "use about 15× more tokens than chats" [VERIFIED: https://www.anthropic.com/engineering/multi-agent-research-system, published 2025-06-13].

### 3.5 A worked product example: Claude Code instruction files and auto memory

- Claude Code loads two memory systems at the start of every session: human-written `CLAUDE.md` instruction files and model-written auto memory. "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead" [VERIFIED: https://code.claude.com/docs/en/memory, n.d., accessed 2026-10].
- Only the first 200 lines or 25KB of the auto-memory index `MEMORY.md` load at session start; detail goes into topic files read on demand [VERIFIED: https://code.claude.com/docs/en/memory, n.d., accessed 2026-10].
- The docs warn that longer instruction files "consume more context and reduce adherence", and that if two instructions contradict each other "Claude may pick one arbitrarily" [VERIFIED: https://code.claude.com/docs/en/memory, n.d., accessed 2026-10].
- The project-root `CLAUDE.md` survives `/compact` because it is re-read from disk; an instruction given only in conversation may disappear after compaction [VERIFIED: https://code.claude.com/docs/en/memory, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] This is the clearest vendor statement of a durable principle: **memory and instructions are advisory inputs to a probabilistic component; enforcement belongs in deterministic code at the tool boundary.**

**Durable vs volatile.** Durable: offload, isolate, summarize, and re-derive context from durable files; compaction is lossy, so anything that must survive goes to a store the harness re-reads. Volatile: header names, strategy identifiers, default thresholds, the 200-line/25KB limits, SDK helper names.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Treat compaction summaries as lossy caches, never as the record. (2) Keep a small, structured, harness-owned progress artefact (plan, step, done-list) outside the model's free-text notes. (3) Pin the instructions that must survive (policy, scope limits) in a re-injected file, and enforce the critical ones in code. (4) Measure the cost of cache invalidation when you clear context; clearing is not free.

---

## PART 4: Retrieval — RAG, hybrid search and its evaluation

### 4.1 Origin and original claims

- Lewis et al. defined retrieval-augmented generation as combining *parametric memory* (a pre-trained seq2seq model) with *non-parametric memory* (a dense vector index of Wikipedia accessed by a neural retriever), and reported state-of-the-art results on three open-domain QA tasks [VERIFIED: https://arxiv.org/abs/2005.11401, published 2020-05-22; NeurIPS 2020].
- The paper names "providing provenance for their decisions and updating their world knowledge" as open research problems that motivate the work; it does not claim to solve them [VERIFIED: https://arxiv.org/abs/2005.11401, published 2020-05-22].

**Age:** 2020; the generator was BART-scale. The durable idea is the separation: knowledge in an index can be updated and cited without retraining.

### 4.2 Lexical, dense and hybrid retrieval

- BEIR (18 datasets, zero-shot) found BM25 "a robust baseline"; dense retrievers often underperformed out of domain, and re-ranking and late-interaction models achieved the best average zero-shot results at "high computational costs" [VERIFIED: https://arxiv.org/abs/2104.08663, published 2021-04-17; NeurIPS 2021 Datasets and Benchmarks].
- Reciprocal Rank Fusion scores each document as the sum over rankers of 1/(k + rank), with k = 60 fixed in a pilot and found "near-optimal, but that the choice was not critical"; RRF beat Condorcet Fuse and the best individual system by about 4–5% on average across TREC experiments [VERIFIED: http://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf, published 2009-07 (SIGIR 2009)].

**Age:** BEIR 2021 and RRF 2009 are old but are the standard references behind "hybrid search". [ASSUMPTION/JUDGEMENT] Embedding models have improved since BEIR; the robustness of BM25 on exact identifiers (SKUs, error codes, policy numbers, case numbers) remains a practical reason to keep a lexical leg in agent retrieval.

### 4.3 Contextual retrieval (Anthropic, 2024)

- Anthropic prepends a short, model-generated, chunk-specific context to each chunk before embedding and BM25 indexing. Measured as top-20 retrieval failure rate (1 − recall@20), averaged across codebases, fiction, arXiv papers and science papers using Gemini Text 004 embeddings: contextual embeddings cut failures by 35% (5.7% → 3.7%); adding contextual BM25 by 49% (→ 2.9%); adding reranking by 67% (→ 1.9%) [VERIFIED: https://www.anthropic.com/news/contextual-retrieval, published 2024-09-19].
- With prompt caching, the one-time contextualization cost was estimated at $1.02 per million document tokens under stated assumptions (800-token chunks, 8K-token documents) ⚠ [VERIFIED: https://www.anthropic.com/news/contextual-retrieval, published 2024-09-19].
- Stated caveats: chunking choices matter; gains vary by embedding model; reranking adds latency and cost; only top-5/10/20 were compared; readers should "run evals" on their own use case [VERIFIED: https://www.anthropic.com/news/contextual-retrieval, published 2024-09-19].

**Source type note.** Vendor engineering post; the datasets are not public. **Age:** 2024-09, over 18 months old; prices and models are superseded.

### 4.4 GraphRAG (Microsoft Research)

- GraphRAG builds an LLM-extracted entity graph, pre-generates summaries for communities of related entities, and answers "global sensemaking" questions (for example "What are the main themes?") by map-reducing over community summaries [VERIFIED: https://arxiv.org/abs/2404.16130, published 2024-04-24].
- Evaluation: head-to-head LLM-judge comparisons on 125 LLM-generated questions over two corpora of about 1M and 1.7M tokens (podcast transcripts; news articles). GraphRAG won on comprehensiveness (72–83%) and diversity (62–82%) against vector RAG; vector RAG gave the most *direct* answers; empowerment results were mixed [VERIFIED: https://arxiv.org/html/2404.16130, published 2024-04-24].
- Indexing the podcast corpus took 281 minutes with gpt-4-turbo; root-level community summaries needed over 97% fewer context tokens than source-text summarization at query time [VERIFIED: https://arxiv.org/html/2404.16130, published 2024-04-24].
- Stated limitations: two corpora only; fabrication rates not measured; claim-based validation agreed with the LLM judge in 78% (comprehensiveness) and 69–70% (diversity) of non-tie comparisons, and was sensitive to how ties were defined [VERIFIED: https://arxiv.org/html/2404.16130, published 2024-04-24].

[ASSUMPTION/JUDGEMENT] GraphRAG answers a different query class from passage RAG. Its evidence is LLM-judged quality, not factual accuracy; do not present it as "more accurate RAG".

### 4.5 Evaluating retrieval and grounded generation

- Ragas proposes reference-free metrics for RAG pipelines covering whether retrieved context is relevant and focused, whether the generator uses it faithfully, and generation quality, "without having to rely on ground truth human annotations" [VERIFIED: https://arxiv.org/abs/2309.15217, published 2023-09-26].
- [ASSUMPTION/JUDGEMENT] Reference-free metrics use an LLM as judge, so they inherit the judge's errors. For agents, evaluate retrieval separately (recall@k / failure rate against a labelled set, as Anthropic did in 4.3) from generation (faithfulness/citation support, Part 5), and from end-task success.

**Durable vs volatile.** Durable: separate retrieval quality from generation quality; combine lexical and semantic signals; measure on your own corpus. Volatile: specific embedding models, rerankers, price per million tokens.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] For agents, retrieval is a *tool*, not a pre-step. Just-in-time retrieval means the agent decides when to search, so retrieval quality must be evaluated on the queries the agent actually issues, which are logged. Keep the retrieval index's permission model aligned with the user's (Part 8, OWASP LLM08).

---

## PART 5: Grounding and citations

### 5.1 Measuring attribution

- Rashkin et al. define AIS (Attributable to Identified Sources), a framework for judging whether generated statements about the world are supported by an identified source, with a two-stage human annotation pipeline validated on conversational QA, summarization and table-to-text [VERIFIED: https://arxiv.org/abs/2112.12870, published 2021-12-23]. [ASSUMPTION/JUDGEMENT] The journal version appeared in *Computational Linguistics* (2023); the abstract page did not show this.
- ALCE benchmarks LLMs that must retrieve evidence and answer with citations, scoring fluency, correctness and citation quality with automatic metrics the authors report correlate strongly with human judgment. On ELI5, the best models lacked complete citation support about half the time [VERIFIED: https://arxiv.org/abs/2305.14627, published 2023-05-24; EMNLP 2023].

**Age:** 2023 models. ⚠ Current models are likely better; no 2026 ALCE-style number was verified.

### 5.2 Citation APIs: valid pointers are not verified support

- Anthropic's Citations feature is GA on the Claude API, AWS, Bedrock, Google Cloud and Microsoft Foundry ⚠. Plain text and PDFs are chunked into sentences; custom content documents are cited by block index without further chunking. Citation types: character ranges (text), page numbers (PDF) and block indices (custom content) [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/citations, n.d., accessed 2026-10].
- Because the API extracts `cited_text` itself, "citations are guaranteed to contain valid pointers to the provided documents"; `cited_text` does not count toward output tokens [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/citations, n.d., accessed 2026-10].
- Citations cannot be combined with structured outputs, because citations interleave citation blocks with text [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/citations, n.d., accessed 2026-10].
- Image citations from PDFs are not supported; scanned PDFs without extractable text are not citable [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/citations, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] The guarantee is that the *pointer* is real (the quoted span exists in the supplied document), not that the span *supports* the claim next to it, and not that the document is true or current. ALCE-style support checking (entailment between claim and cited span) remains the application's job where it matters (legal, healthcare, finance).

### 5.3 When retrieved evidence is wrong

- ClashEval perturbed answers in retrieved content (subtle to blatant) across 1,200+ questions in six domains and six top LLMs including GPT-4o. Models adopted incorrect retrieved content, overriding their own correct prior, more than 60% of the time. The more the content deviated from the truth, the less likely it was adopted; the less confident the model's prior (token probabilities), the more likely adoption [VERIFIED: https://arxiv.org/abs/2404.10198, published 2024-04-16].

**Durable vs volatile.** Durable: grounding shifts trust from the model to the source, so source quality, freshness and integrity become the bottleneck. Volatile: which APIs support citations, chunking rules, compatibility limits.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Show citations to humans in review workflows; store the cited span plus a document version identifier (Part 9) so a citation can be re-checked later; add an entailment or rule check before high-stakes actions; and remember that grounding *amplifies* a poisoned or stale source (ClashEval, PoisonedRAG).

---

## PART 6: Agent memory systems

### 6.1 MemGPT (now Letta)

- MemGPT introduced "virtual context management", modelled on OS memory hierarchies: the system moves information between memory tiers so the LLM can work beyond its fixed window, and uses interrupts to manage control flow. Evaluated on analysing documents larger than the window and on multi-session chat [VERIFIED: https://arxiv.org/abs/2310.08560, published 2023-10-12].
- Letta's current documentation organizes memory into **blocks** that agents edit through memory tools and developers edit through the API; attached blocks are pinned in the system prompt; a block can be shared by multiple agents [VERIFIED: https://docs.letta.com/guides/agents/memory, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] Letta is the company and open-source project founded by MemGPT's authors; MemGPT's in-context "core" memory plus out-of-context "archival" and "recall" stores remain the conceptual model. Not verified this session.

**Age:** MemGPT 2023; product has evolved.

### 6.2 Generative Agents' memory stream

- Park et al. gave 25 simulated agents a memory stream: natural-language records with creation and last-access timestamps, plus reflections [VERIFIED: https://arxiv.org/abs/2304.03442, published 2023-04-07].
- Retrieval scores each memory by **recency** (exponential decay, factor 0.995 per game hour since last access), **importance** (LLM-rated 1–10 at creation) and **relevance** (embedding cosine similarity), min-max normalized and summed with equal weights [VERIFIED: https://arxiv.org/html/2304.03442, published 2023-04-07].
- Reflection triggers when summed importance of recent events exceeds 150 (about two to three times a day); reflections cite the memories that support them and can be reflected on again [VERIFIED: https://arxiv.org/html/2304.03442, published 2023-04-07].
- Ablation (100 raters, TrueSkill believability): full architecture μ = 29.89; no reflection 26.88; no reflection or planning 25.64; no memory 21.21; human crowdworker baseline 22.95 [VERIFIED: https://arxiv.org/html/2304.03442, published 2023-04-07].
- Stated failures: missed relevant memories; embellishment (an agent claimed a candidate would "make an announcement tomorrow", which never happened); world-knowledge bleed (attributing *Wealth of Nations* to a neighbour named Adam Smith). About 1.3% of 453 responses about other agents were hallucinated [VERIFIED: https://arxiv.org/html/2304.03442, published 2023-04-07].
- [ASSUMPTION/JUDGEMENT] Published at UIST 2023.

[ASSUMPTION/JUDGEMENT] The measured outcome is *believability* of simulated behaviour, not task correctness. The retrieval formula is a design pattern, not a validated standard for business agents. The "reflections" mechanism is also where an error becomes a durable belief (Part 10).

### 6.3 Mem0

- Mem0 extracts, consolidates and retrieves salient facts from conversations, with a graph-memory variant. On LOCOMO it reports a 26% relative improvement in LLM-as-a-Judge score over OpenAI's memory, 91% lower p95 latency and more than 90% token-cost savings versus full context; the graph variant is about 2% higher overall [VERIFIED: https://arxiv.org/abs/2504.19413, published 2025-04-28].
- **Source type note.** [ASSUMPTION/JUDGEMENT] The authors are Mem0's founders/staff; this is a vendor paper evaluating its own product against competitors, with an LLM judge. Treat the numbers as self-reported and unreplicated.

### 6.4 Memory types and write timing (LangGraph)

- LangGraph distinguishes **semantic** memory (facts, stored as a single profile JSON document or as a collection of narrow documents), **episodic** memory (past experiences, often used as few-shot examples) and **procedural** memory (rules, typically the prompt, which agents may refine by reflection) [VERIFIED: https://docs.langchain.com/oss/python/langgraph/memory, n.d., accessed 2026-10].
- Writing "in the hot path" gives immediate updates but adds latency and competes with the task; writing "in the background" removes latency but risks other threads missing new context. Profiles get error-prone as they grow; collections give "higher recall downstream" but require update/delete logic [VERIFIED: https://docs.langchain.com/oss/python/langgraph/memory, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] *Procedural* memory that edits the agent's own prompt is the highest-risk memory type: it changes future behaviour for every user. It should go through the same review as a prompt change.

### 6.5 Vendor memory tools

**Anthropic memory tool** ⚠

- Tool type `memory_20250818`; available on Claude 4 and later models; no beta header required for the tool itself. It is **client-side**: Claude requests `view`, `create`, `str_replace`, `insert`, `delete`, `rename` on paths under `/memories`, and the application executes them on storage it controls [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].
- The API automatically adds a system-prompt instruction to "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE" and to "ASSUME INTERRUPTION: Your context window might be reset at any moment" [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].
- Security guidance puts the burden on the application: strip sensitive data before writing ("Claude usually refuses to write sensitive information" is not a guarantee); cap file sizes; "Periodically delete memory files that haven't been accessed in a long time"; validate every path against traversal (including URL-encoded `%2e%2e%2f`) [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].
- Recommended pairing: compaction keeps the active context small; "memory preserves the information that must survive summarization" [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].

**OpenAI ChatGPT memory** ⚠ (secondary sources only)

- On 10 April 2025 OpenAI expanded ChatGPT memory to reference past conversations, beyond explicitly saved memories; it started with Plus and Pro, excluded the UK, EU, Iceland, Liechtenstein, Norway and Switzerland pending "additional external reviews", was on by default for users with memory enabled, and could be turned off; Temporary Chat keeps conversations out of memory [WIDELY REPORTED: https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/, 2025].
- Press summaries report that chat-history memories, unlike saved memories, could not be viewed or deleted selectively [WIDELY REPORTED: https://decrypt.co/314380, 2025]. ⚠ Not verified against OpenAI's text; current availability and controls (October 2026) were not verified.

**Durable vs volatile.** Durable: memory is a write path from a probabilistic component into persistent storage; it needs scoping, size limits, expiry, inspection and deletion. Volatile: tool names and versions, product rollout regions, default-on choices, benchmark leaderboards for memory products.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Prefer client-side/self-hosted memory stores where you need tenancy isolation, retention control and erasure (GDPR-style deletion requests must reach memory, embeddings and backups). Scope memory by tenant and user, never globally by default. Give users and operators a view-and-delete surface. Record who/what wrote each memory item, from which session and source (Part 9), so poisoned items can be traced and purged.

---

## PART 7: The state side — checkpointing and durable execution (LangGraph as reference)

- A LangGraph **checkpoint** is "a snapshot of the graph state saved at each super-step"; a **super-step** is one tick in which all scheduled nodes run, possibly in parallel. Checkpoints are grouped by `thread_id` [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- A `StateSnapshot` records `values`, `next` (nodes to run; empty means finished), `config` (thread, namespace, checkpoint id), `metadata` (source, writes, step), `created_at`, `parent_config` and pending `tasks` with errors and interrupts [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- **Replay** from a prior `checkpoint_id` re-runs later nodes, and "Interrupts and LLM or API calls in those nodes are triggered again" [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- `update_state` **forks**: it writes a new checkpoint and leaves the original untouched [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- **Pending writes**: if one node fails mid-super-step, outputs of siblings that succeeded are stored and not re-run on resume [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- **Durability modes** ⚠: `exit` (persist only at end; a crash loses intermediate state), `async` (persist while the next step runs; small risk of losing the last checkpoint), `sync` (persist before the next step; most durable) [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].
- Implementations: `InMemorySaver` (lost on restart), `SqliteSaver` (development), `PostgresSaver` (production). Checkpoints accumulate, adding latency and storage cost, so pruning/retention is advised; subgraphs have their own checkpoint namespaces [VERIFIED: https://docs.langchain.com/oss/python/langgraph/persistence, n.d., accessed 2026-10].
- Checkpoint state can be encrypted via an `EncryptedSerializer`; the default serializer can fall back to pickle when enabled [VERIFIED: https://docs.langchain.com/oss/python/langgraph/checkpointers, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] The replay note is the architectural crux: **a checkpoint restores the agent's state, not the world's.** Replaying from a checkpoint re-issues side-effecting tool calls unless the tools are idempotent (idempotency keys) or the orchestrator records completed side effects and skips them. Workflow engines (Temporal, Step Functions, Azure Durable Functions) solve this with event-sourced histories; the reliability chapter should connect to that literature. Not verified this session.

[ASSUMPTION/JUDGEMENT] Pickle fallback in checkpoint serialization is a deserialization risk if the checkpoint store can be written by anyone other than the runtime; keep it off or the store tightly controlled.

**Durable vs volatile.** Durable: checkpoint at step boundaries; record pending writes; fork rather than overwrite; choose durability per workflow; retention and encryption for state. Volatile: LangGraph class and mode names.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Use the checkpoint history as the audit trail and the basis for human-in-the-loop approval (state is persisted while waiting). Pick `sync`-equivalent durability for any step that precedes an irreversible action. Keep long-term memory (store) and task state (checkpoints) in separate tables with separate retention; they have different legal and operational lifetimes.

---

## PART 8: Memory poisoning and persistence attacks

### 8.1 Research attacks

| Attack | What is poisoned | Attacker access | Reported result | Source type |
| --- | --- | --- | --- | --- |
| **PoisonedRAG** | RAG knowledge database | Inject texts into corpus | ~90% success with ~5 malicious texts per target question in a DB of millions | Preprint; USENIX Security 2025 |
| **AgentPoison** | Agent long-term memory / RAG KB, with optimized trigger | Inject records + trigger in queries | >80% avg success on 3 agents; <1% benign impact; <0.1% poison rate | Preprint |
| **MINJA** | Agent memory bank | **Queries only** (no direct memory access) | Injection success 95.6–100%; attack success 57–98.9% by agent/model | Preprint |

- PoisonedRAG: an attacker injects a few malicious texts so the LLM gives an attacker-chosen answer to an attacker-chosen question; ~5 texts per target, ~90% success, against databases of millions of texts; evaluated defenses were insufficient [VERIFIED: https://arxiv.org/abs/2402.07867, published 2024-02-12; to appear USENIX Security 2025].
- AgentPoison: backdoor attack on generic and RAG-based agents' memory or knowledge base using an optimized trigger; tested on an autonomous-driving agent, a knowledge-intensive QA agent and EHRAgent (healthcare); >80% average success, <1% benign performance impact, <0.1% poison rate, no fine-tuning needed [VERIFIED: https://arxiv.org/abs/2407.12784, published 2024-07-17].
- MINJA: injects malicious records through ordinary queries, using "bridging steps" and an indication prompt that is progressively shortened so poisoned records are retrieved for later victims' queries [VERIFIED: https://arxiv.org/abs/2503.03704, published 2025-03-05].
- MINJA results: EHRAgent (GPT-4) on MIMIC-III ISR 95.6%, ASR 57.0%; on eICU ISR 98.5%, ASR 90.0%; RAP (GPT-4o) on Webshop ISR 99.3%, ASR 98.9%; QA agent on MMLU ISR 100%, ASR 68.9% [VERIFIED: https://arxiv.org/html/2503.03704, published 2025-03-05].
- MINJA tested only prompt-level detection with GPT-4o: a tailored prompt caught most records on EHRAgent but none on RAP or the QA agent; a general prompt caught 29/90 on the QA agent and produced 34/50 false positives on MIMIC-III [VERIFIED: https://arxiv.org/html/2503.03704, published 2025-03-05].

[ASSUMPTION/JUDGEMENT] MINJA is the most important result for architects: **any agent that writes memory from user interactions and shares that memory across users is attackable by an ordinary user.** Shared memory across tenants or users is a cross-user injection channel.

### 8.2 Researcher proofs of concept on shipped products

- **ChatGPT (SpAIware).** Prompt injection from a malicious website or document made the ChatGPT macOS app store attacker instructions in long-term memory; they persisted into future sessions and continuously exfiltrated user input and responses via image URLs. OpenAI fixed the exfiltration vector in version 1.2024.247, but the author notes "A website or untrusted document can still invoke the memory tool to store arbitrary memories" [VERIFIED: https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/, published 2024-09-20].
- **Gemini.** A prompt injection in an uploaded document planted instructions to save attacker-chosen "memories" when the user next replied with a common word ("yes", "sure"), so the memory write appeared user-initiated ("delayed tool invocation"). Google assessed it as "an abuse-related risk with low likelihood and low impact" [VERIFIED: https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/, published 2025-02-10].

**Age:** both are over 18 months old; product behaviour may have changed. They remain valid illustrations of the persistence mechanism.

### 8.3 Industry guidance

- Microsoft's AI Red Team taxonomy of agentic failure modes (April 2025) includes a memory-poisoning case study showing corrupted memory used as a pivot to exfiltrate data; recommended mitigations include limiting the agent's ability to store memories autonomously, requiring "external authentication or validation for all memory updates", limiting which components access memory, and controlling the structure and format of memory items [VERIFIED: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/, published 2025-04-24].
- Secondary sources describe the case study as an email assistant built with LangChain/LangGraph and GPT-4o [WIDELY REPORTED: https://argonsys.com/microsoft-cloud/library/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/, 2025]. The success-rate figures were not verified.
- OWASP LLM08:2025 (Vector and Embedding Weaknesses) lists unauthorized access and leakage, cross-context leaks in multi-tenant stores, embedding inversion, data poisoning and behaviour alteration; mitigations include permission-aware, partitioned vector stores, source authentication, and "detailed immutable logs of retrieval activities" [VERIFIED: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/, published 2025 (n.d.)].
- OWASP's *Agentic AI – Threats and Mitigations* v1.0 was published 17 February 2025 as the first guide of the Agentic Security Initiative [VERIFIED: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/, published 2025-02-17]. ⚠ Its threat list (which the analyst believes includes memory poisoning as T1) was not read; ASSUMPTION.

**Durable vs volatile.** Durable: memory turns a one-shot injection into a persistent compromise; retrieval turns corpus write access into model control; shared memory is a cross-principal channel. Volatile: specific product fixes and vendor severity assessments.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
1. Treat every memory write as an untrusted write: schema-validate it, record its provenance (session, user, source document, tool), and for high-impact memory types (procedural, shared, cross-user) require a gate (human, policy rule, or a separate classifier) before it becomes readable.
2. Scope memory per principal; never share learned memory across tenants without curation.
3. Make memory inspectable and revocable, with bulk purge by provenance (for example "delete everything derived from document X").
4. Do not rely on prompt-level detection; MINJA shows it is unreliable and noisy.
5. Re-validate memory at read time against authoritative systems when it drives an action.

---

## PART 9: Freshness, staleness and provenance

### 9.1 Evidence that freshness is a distinct failure

- FreshQA tests fast-changing knowledge and false-premise questions; human evaluation with more than 50K judgments found all models, regardless of size, struggled with both. FreshPrompt (adding current search results to the prompt) substantially improved results; the number and order of retrieved evidence items affected correctness [VERIFIED: https://arxiv.org/abs/2310.03214, published 2023-10-05].
- LongMemEval treats "knowledge updates" and "temporal reasoning" as separate memory abilities and proposes time-aware query expansion [VERIFIED: https://arxiv.org/abs/2410.10813, published 2024-10-14].
- Anthropic's memory tool guidance recommends periodic expiry of memory files not accessed for a long time [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool, n.d., accessed 2026-10].

### 9.2 Bitemporal thinking

- Fowler distinguishes **actual (valid) time**, when a fact was true in the world, from **record (transaction) time**, when the system learned it. With both, you can answer "what did we believe on 25 Feb when payroll ran" as well as "what was true on 25 Feb". "We don't change what we thought we knew about Sally's salary on Feb 25. We just append the later knowledge we gained" [VERIFIED: https://martinfowler.com/articles/bitemporal-history.html, published 2021-04-07].

[ASSUMPTION/JUDGEMENT] Applied to agents: every memory item and every retrieved fact used in a decision should carry (a) when it was valid in the world, (b) when the system recorded it, and (c) when the agent read it. Then an auditor can tell whether the agent acted on the best knowledge available at the time (defensible) or on stale knowledge that had already been corrected (a system defect). This matters in finance operations, benefits eligibility and healthcare.

### 9.3 Provenance

- W3C PROV is a family of documents (Working Group Note overview dated 30 April 2013) describing provenance as information about "entities, activities, and people involved in producing a piece of data or thing", with PROV-DM as the conceptual model [VERIFIED: https://www.w3.org/TR/prov-overview/, published 2013-04-30].
- [ASSUMPTION/JUDGEMENT] PROV-DM's core relations (an entity *was generated by* an activity, *was derived from* another entity, *was attributed to* an agent) map directly onto agent records: a memory item was generated by a session, derived from a tool result or document, and attributed to a user or a model. Not verified from PROV-DM text this session.
- Anthropic's citation pointers (Part 5) and Letta's statement that all messages, reasoning and tool calls are stored in a database (Part 1) are partial provenance mechanisms.

**Durable vs volatile.** Durable: valid time vs record time; derivation chains; expiry. These are decades-old data-management ideas. Volatile: none of note; vendor features for memory timestamps vary.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Store `source_id`, `source_version`, `valid_from/valid_to`, `recorded_at`, `written_by` (user/model/process) and `derived_from` with every memory item and every cached retrieval result. Put an explicit time-to-live on facts that change (prices, balances, eligibility, inventory, policy) and re-read them from the system of record before acting. Prefer reading live from authoritative tools over remembering volatile facts at all.

---

## PART 10: How errors and stale information propagate

### 10.1 Mechanisms with evidence

| Mechanism | Evidence | What happens |
| --- | --- | --- |
| **Self-conditioning (snowballing)** | Zhang et al. 2023 | Model over-commits to an early wrong answer and generates further false claims to justify it; GPT-4 recognized 87% and ChatGPT 67% of its own such mistakes when asked separately |
| **Context adoption** | ClashEval 2024 | Wrong retrieved content overrides a correct prior >60% of the time |
| **Distraction** | GSM-IC 2023; Context Rot 2025 | Irrelevant or near-miss items lower accuracy |
| **Lossy summarization** | Anthropic harness post 2025; Claude Code docs | Compaction "doesn't always pass clear instructions to the next agent"; conversation-only instructions can vanish after `/compact` |
| **Hand-off loss** | Anthropic multi-agent post 2025 | "Game of telephone" between agents; mitigated by writing artefacts to external storage and passing references |
| **Compounding in stateful runs** | Anthropic multi-agent post 2025 | Errors compound; restarts are costly; resume from the failure point |
| **Belief persistence** | Generative Agents 2023; SpAIware 2024; MINJA 2025 | Embellished or injected content becomes memory and is retrieved later as if it were fact |
| **False completion** | Anthropic harness post 2025 | A later session reads progress notes and declares the project done |

- Snowballing: "over-commit to early mistakes, leading to more mistakes that it otherwise would not make"; ChatGPT and GPT-4 identified 67% and 87% of their own mistakes when asked separately [VERIFIED: https://arxiv.org/abs/2305.13534, published 2023-05-22].
- Compaction "doesn't always pass clear instructions to the next agent" [VERIFIED: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, published 2025-11-26].

### 10.2 The propagation path

[ASSUMPTION/JUDGEMENT] The typical path in an agent is: a wrong or stale fact enters the working context (bad retrieval, poisoned document, stale memory) → the model commits to it (ClashEval, snowballing) → the commitment is written into a summary, note or memory (compaction, reflection, memory tool) → later sessions or other agents read the note as ground truth (hand-off, false completion) → an action is taken on it. Each arrow is a place for a control:

| Hop | Control |
| --- | --- |
| Source → context | Source allow-lists, freshness checks, retrieval permission filters, provenance tags |
| Context → commitment | Ask for citations; entailment checks; "verify before acting" steps that re-read the system of record |
| Commitment → memory | Memory write gates, schema validation, separate writer process, provenance fields |
| Memory → later reader | Read-time re-validation; TTLs; show the provenance to the reader (model and human) |
| Belief → action | Deterministic preconditions in the tool layer; approvals for irreversible actions; idempotency |

### 10.3 Self-correction is real but limited

- [ASSUMPTION/JUDGEMENT] The snowballing paper's finding that models recognize many of their own errors *when asked separately* supports a separate verification pass in a fresh context (no shared history) rather than asking the same context to check itself. The number is from 2023 models.

**Durable vs volatile.** Durable: errors are amplified by persistence (memory, summaries) and by authority (being retrieved, being cited, being in a progress file). Volatile: the measured rates.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Design so that the *system of record* is always one hop from any action, and model-written artefacts are never the only evidence that a precondition holds. Run verification in a fresh context. Log the working context per call so that a bad action can be traced to the item that caused it.

---

## Key numbers

| Number | What it measured | Source | Date |
| --- | --- | --- | --- |
| 56.1% → 53.8% | GPT-3.5-Turbo multi-doc QA: closed-book vs 20 docs with answer at position 9 (below closed-book) | Liu et al., Lost in the Middle | 2023-07 |
| ~half of 17 models | Share of long-context models still "satisfactory" at 32K on RULER, all claiming ≥32K | Hsieh et al., RULER | 2024-04 |
| 11 of 13 models | Fell below 50% of short-context baseline at 32K on NoLiMa | Modarressi et al., NoLiMa | 2025-02 |
| 99.3% → 69.7% | GPT-4o, NoLiMa, <1K vs 32K tokens | NoLiMa | 2025-02 |
| 18 models | Context Rot test set; shuffled haystacks beat coherent ones for all 18 | Chroma | 2025-07 |
| ~300 vs ~113K tokens | Focused vs full prompts on LongMemEval-style task; focused much better | Chroma | 2025-07 |
| ~30% drop | Accuracy drop of commercial assistants / long-context LLMs on sustained-interaction memory | LongMemEval | 2024-10 |
| 200K tokens | Anthropic threshold below which whole-KB-in-prompt is suggested instead of RAG | Anthropic contextual retrieval | 2024-09 |
| 5.7% → 1.9% | Top-20 retrieval failure rate, baseline vs contextual embeddings + contextual BM25 + rerank (−67%) | Anthropic | 2024-09 |
| k = 60 | RRF constant; near-optimal, not critical | Cormack et al., SIGIR | 2009 |
| 72–83% | GraphRAG LLM-judge win rate on comprehensiveness vs vector RAG (podcast corpus) | Edge et al. | 2024-04 |
| ~50% | ELI5 answers from best models lacking complete citation support | Gao et al., ALCE | 2023-05 |
| >60% | Rate at which LLMs adopt incorrect retrieved content over a correct prior | ClashEval | 2024-04 |
| 29.89 vs 21.21 | Believability (TrueSkill μ), full memory architecture vs no memory | Park et al., Generative Agents | 2023-04 |
| 26% / 91% / >90% | Mem0 self-reported: LLM-judge gain over OpenAI memory / p95 latency cut / token savings vs full context (LOCOMO) | Chhikara et al. (vendor) | 2025-04 |
| ~5 texts, ~90% | PoisonedRAG texts per target question and attack success, DB of millions | Zou et al. | 2024-02 |
| >80%, <0.1% | AgentPoison avg attack success; poison rate | Chen et al. | 2024-07 |
| 95.6–100% / 57–98.9% | MINJA injection success / attack success via queries only | Dong et al. | 2025-03 |
| 80% | Share of performance variance explained by token usage (BrowseComp) | Anthropic multi-agent post | 2025-06 |
| ~15× | Tokens used by multi-agent systems vs chats | Anthropic multi-agent post | 2025-06 |
| 100,000 tokens / 3 | Default trigger / kept tool uses for `clear_tool_uses_20250919` ⚠ | Anthropic docs | accessed 2026-10 |
| 200 lines or 25KB | Portion of Claude Code `MEMORY.md` loaded at session start ⚠ | Claude Code docs | accessed 2026-10 |
| 67% / 87% | Share of own snowballed mistakes ChatGPT / GPT-4 recognized when asked separately | Zhang et al. | 2023-05 |

## Where sources disagree

- **Does position matter?** Lost in the Middle (2023) found a strong U-shape by position. Chroma's Context Rot (2025) found needle position made no notable difference in its needle-question similarity experiment. Likely explanations: different tasks, and newer models trained against the middle-position weakness. [ASSUMPTION/JUDGEMENT] Write "position *can* matter; measure it" rather than "the middle is lost".
- **Long context vs RAG.** Li et al. (2024) found long context beats RAG on average when resources allow; Anthropic suggests skipping RAG under 200K tokens; Context Rot, NoLiMa and RULER show quality decay well below advertised limits. The positions reconcile if the question is cost and corpus size versus quality at a given length, but chapter writers should not present either "RAG is obsolete" or "always retrieve" as settled.
- **Coherent vs shuffled context.** Context Rot found shuffled haystacks *helped* across all models, unexplained. This contradicts the intuition that well-structured context is easier to use. It is one vendor report, not replicated in this brief.
- **Severity of memory injection.** Researchers (SpAIware, Gemini PoC) treat persistent memory injection as a serious vulnerability; Google rated the Gemini case "low likelihood and low impact"; OpenAI fixed exfiltration but, per the researcher, not memory injection itself.
- **Who should write memory.** Anthropic's memory tool and Letta let the model write memory directly (hot path). Microsoft's red team recommends limiting autonomous memory writes and requiring external validation of all updates. LangGraph presents hot-path and background writing as a trade-off.
- **Memory product benchmarks.** Mem0 reports beating OpenAI's memory on LOCOMO; it is a vendor evaluating its own product with an LLM judge. No independent replication was found.

## Open questions / not verifiable

- Current effective context lengths of 2026 frontier models on NoLiMa-style or RULER-style tasks: not verified; no post-2025 benchmark result was fetched ⚠.
- OpenAI's own current documentation of ChatGPT memory (controls, retention, enterprise behaviour as of October 2026): 403; only 2025 press coverage verified.
- The contents of OWASP's Agentic AI Threats and Mitigations PDF and Microsoft's failure-mode whitepaper case-study numbers.
- Whether any production deployment has published measured rates of stale-memory or poisoned-memory incidents. None found.
- Precise mechanics of Anthropic's threshold compaction mode and the relationship between `compact_20260112` and the `compact-2026-09-04` beta ⚠.
- Letta's current archival/recall memory and sleep-time agent features.
- How well LLM-judge metrics (Ragas, GraphRAG's evaluation, Mem0's LOCOMO judge) agree with human judgement in enterprise domains.
- Whether citation-support rates (ALCE) have materially improved on 2026 models.
- Legal treatment of model-written memory under data-protection erasure rights: not researched; consult the governance/security brief.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| Effective context engineering for AI agents | Anthropic Applied AI (Rajasekaran, Dixon, Ryan, Hadfield) | 2025 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | engineering post |
| Effective harnesses for long-running agents | Anthropic (J. Young) | 2025 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | engineering post |
| How we built our multi-agent research system | Anthropic | 2025 | https://www.anthropic.com/engineering/multi-agent-research-system | engineering post |
| Introducing Contextual Retrieval | Anthropic | 2024 | https://www.anthropic.com/news/contextual-retrieval | engineering post |
| Context editing | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/context-editing | docs |
| Compaction overview | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/compaction | docs |
| Memory tool | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | docs |
| Citations | Anthropic | n.d. (accessed 2026-10) | https://platform.claude.com/docs/en/build-with-claude/citations | docs |
| How Claude remembers your project | Anthropic (Claude Code) | n.d. (accessed 2026-10) | https://code.claude.com/docs/en/memory | docs |
| Lost in the Middle: How Language Models Use Long Contexts | Liu et al. | 2023 | https://arxiv.org/abs/2307.03172 | paper (TACL) |
| RULER: What's the Real Context Size of Your Long-Context Language Models? | Hsieh et al. (NVIDIA) | 2024 | https://arxiv.org/abs/2404.06654 | paper (COLM 2024) |
| NoLiMa: Long-Context Evaluation Beyond Literal Matching | Modarressi et al. | 2025 | https://arxiv.org/abs/2502.05167 | paper (ICML 2025) |
| Context Rot: How Increasing Input Tokens Impacts LLM Performance | Hong, Troynikov, Huber (Chroma) | 2025 | https://www.trychroma.com/research/context-rot | vendor research report |
| Large Language Models Can Be Easily Distracted by Irrelevant Context | Shi et al. | 2023 | https://arxiv.org/abs/2302.00093 | paper (ICML 2023) |
| LongMemEval | Wu et al. | 2024 | https://arxiv.org/abs/2410.10813 | paper (ICLR 2025) |
| Retrieval Augmented Generation or Long-Context LLMs? | Li et al. | 2024 | https://arxiv.org/abs/2407.16833 | paper (EMNLP 2024 industry) |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Lewis et al. | 2020 | https://arxiv.org/abs/2005.11401 | paper (NeurIPS 2020) |
| BEIR | Thakur et al. | 2021 | https://arxiv.org/abs/2104.08663 | paper (NeurIPS 2021 D&B) |
| Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods | Cormack, Clarke, Büttcher | 2009 | http://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf | paper (SIGIR 2009) |
| From Local to Global: A Graph RAG Approach to Query-Focused Summarization | Edge et al. (Microsoft) | 2024 | https://arxiv.org/abs/2404.16130 | preprint |
| Ragas: Automated Evaluation of Retrieval Augmented Generation | Es et al. | 2023 | https://arxiv.org/abs/2309.15217 | preprint |
| Measuring Attribution in Natural Language Generation Models (AIS) | Rashkin et al. (Google) | 2021 | https://arxiv.org/abs/2112.12870 | preprint (journal version assumed) |
| Enabling Large Language Models to Generate Text with Citations (ALCE) | Gao et al. | 2023 | https://arxiv.org/abs/2305.14627 | paper (EMNLP 2023) |
| ClashEval | Wu, Wu, Zou | 2024 | https://arxiv.org/abs/2404.10198 | preprint |
| MemGPT: Towards LLMs as Operating Systems | Packer et al. | 2023 | https://arxiv.org/abs/2310.08560 | preprint |
| Letta memory overview | Letta | n.d. (accessed 2026-10) | https://docs.letta.com/guides/agents/memory | docs |
| Generative Agents: Interactive Simulacra of Human Behavior | Park et al. | 2023 | https://arxiv.org/abs/2304.03442 | paper (UIST 2023, assumed) |
| Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | Chhikara et al. | 2025 | https://arxiv.org/abs/2504.19413 | preprint (vendor) |
| LangGraph persistence | LangChain | n.d. (accessed 2026-10) | https://docs.langchain.com/oss/python/langgraph/persistence | docs |
| LangGraph checkpointers | LangChain | n.d. (accessed 2026-10) | https://docs.langchain.com/oss/python/langgraph/checkpointers | docs |
| LangGraph memory | LangChain | n.d. (accessed 2026-10) | https://docs.langchain.com/oss/python/langgraph/memory | docs |
| ADK Sessions, State and Memory | Google | n.d. (accessed 2026-10) | https://adk.dev/sessions/ | docs |
| OpenAI updates ChatGPT to reference your other chats | TechCrunch (M. Zeff) | 2025 | https://techcrunch.com/2025/04/10/openai-updates-chatgpt-to-reference-your-other-chats/ | press |
| ChatGPT memory coverage | Decrypt | 2025 | https://decrypt.co/314380 | press (not fetched; via search summary) |
| PoisonedRAG | Zou et al. | 2024 | https://arxiv.org/abs/2402.07867 | paper (USENIX Security 2025) |
| AgentPoison | Chen et al. | 2024 | https://arxiv.org/abs/2407.12784 | preprint |
| Memory Injection Attacks on LLM Agents via Query-Only Interaction (MINJA) | Dong et al. | 2025 | https://arxiv.org/abs/2503.03704 | preprint |
| Spyware Injection Into Your ChatGPT's Long-Term Memory (SpAIware) | J. Rehberger (Embrace The Red) | 2024 | https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/ | security research blog |
| Hacking Gemini's Memory with Prompt Injection and Delayed Tool Invocation | J. Rehberger (Embrace The Red) | 2025 | https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/ | security research blog |
| New whitepaper outlines the taxonomy of failure modes in AI agents | Microsoft Security | 2025 | https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ | engineering post |
| LLM08:2025 Vector and Embedding Weaknesses | OWASP GenAI Security Project | 2025 | https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/ | standard/guidance |
| Agentic AI – Threats and Mitigations | OWASP Agentic Security Initiative | 2025 | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ | standard/guidance (landing page only) |
| FreshLLMs: Refreshing LLMs with Search Engine Augmentation | Vu et al. (Google) | 2023 | https://arxiv.org/abs/2310.03214 | preprint |
| How Language Model Hallucinations Can Snowball | Zhang et al. | 2023 | https://arxiv.org/abs/2305.13534 | preprint |
| Bitemporal History | M. Fowler | 2021 | https://martinfowler.com/articles/bitemporal-history.html | article |
| PROV-Overview | W3C Provenance WG | 2013 | https://www.w3.org/TR/prov-overview/ | spec (WG Note) |
