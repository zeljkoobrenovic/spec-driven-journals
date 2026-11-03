# Research brief: Tools, protocols and execution boundaries

Prepared 28 October 2026 for chapter writers of *Architecting Agentic Systems*. The brief covers how a model's proposed actions become real effects: tool and function calling, structured outputs and constrained decoding, tool design, the Model Context Protocol (MCP), tool-count limits and tool search, code execution as tool use, sandboxing and isolation technology, network egress control, permission models for CLI agents, and browser and computer-use agents. For each mechanism it records **what it actually guarantees** and **its known escapes or limits**. It is vendor-neutral. Anthropic, OpenAI and the MCP project get the most space because they publish dated, detailed documentation, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (28 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date; undated product documentation is marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, trade coverage, third-party summary), not fetched from the originator's own technical documentation in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that its owner has not described falls here. Chapter writers should re-verify these or present them explicitly as reference-architecture judgement.

**Evidence age matters.** This field moves faster than any other the book covers. MCP shipped four incompatible revisions in 20 months (2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28), and the July 2026 revision removed the session and handshake that most 2025 tutorials describe. Vendor documentation pages are living documents: model names, tool version strings (`tool_search_tool_regex_20251119`, `computer_toolset_20260801`) and limits will change. Sources older than about 18 months (SWE-agent, CodeAct, OSWorld, OpenAI's 2024 structured-outputs launch, Firecracker 2020) are cited for durable findings, and each one is marked where it may describe a superseded model or API.

**Research limitation.** Several things could not be verified in this session:

- OpenAI's August 2024 Structured Outputs launch post returned HTTP 403; its numbers are carried as WIDELY REPORTED.
- E2B's documentation site did not state its isolation technology; the Firecracker claim rests on E2B's own open-source runtime README (fetched), not on product documentation.
- Daytona's documentation did not name its isolation technology.
- The NVD web pages did not render; CVE details come from the NVD JSON API (`services.nvd.nist.gov`), which was fetched.
- OpenAI's December 2025 Atlas prompt-injection post was not fetched; it is carried from trade press.
- No independent benchmark of tool-search accuracy across vendors was found; vendor numbers are vendor-measured.
- Full-text limitations sections of several arXiv papers (CodeAct, RAG-MCP, Let Me Speak Freely) were not read; only abstracts were.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as protocol revisions, tool version strings, model names, product limits and default settings.

---

## PART 1: The tool-call contract and structured outputs

### 1.1 What a tool call is, architecturally

| Layer | Who owns it | What it guarantees | What it does not guarantee |
| --- | --- | --- | --- |
| Tool definition (name, description, JSON Schema) | Application developer | The model sees the contract | That the model reads it as intended |
| Tool call (model output) | Model, optionally under constrained decoding | With strict mode: name is valid, arguments parse and match the schema | That the arguments are correct, safe, authorised or what the user wanted |
| Execution | Application or tool server | Whatever the executor enforces | Anything the executor does not check |
| Tool result | Tool server | Whatever the server returns | That it is free of injected instructions |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the sources below. The central architectural point for the book: **the model only ever proposes; execution is ordinary code that must enforce its own authorisation, validation and limits.** Every vendor and spec source fetched for this brief places enforcement outside the model.

- The MCP specification describes tools as "**model-controlled**", meaning "the language model can discover and invoke tools automatically", but says "there **SHOULD** always be a human in the loop with the ability to deny tool invocations" and that clients should show confirmation prompts and make tool invocations visible [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].
- The same spec puts the burden on servers: "Servers **MUST**: Validate all tool inputs; Implement proper access controls; Rate limit tool invocations; Sanitize tool outputs." Clients SHOULD show tool inputs to the user before calling the server "to avoid malicious or accidental data exfiltration", validate results before passing them to the LLM, implement timeouts and log tool usage for audit [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].
- MCP distinguishes **protocol errors** (unknown tool, malformed request) from **tool execution errors** returned with `isError: true`, which "contain actionable feedback that language models can use to self-correct". Clients SHOULD pass execution errors to the model [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28]. The 2025-11-25 revision had already clarified that input-validation errors belong in the second class "to enable model self-correction" [VERIFIED: https://modelcontextprotocol.io/specification/2025-11-25/changelog, published 2025-11-25].
- OWASP's LLM Top 10 (2025 edition) names the failure this layer must prevent: **Excessive Agency**, with three root causes (excessive functionality, excessive permissions, excessive autonomy). Its mitigations include preferring narrow purpose-built tools over open-ended ones such as general shell access, least-privilege access scoped to the individual user, human approval for high-impact actions, and enforcing authorisation in downstream systems "rather than relying on the LLM" [VERIFIED: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/, n.d., accessed 2026-10].

**Durable vs volatile.** Durable: the propose/execute split; validation and authorisation in the executor; the distinction between errors a model can fix and errors it cannot. Volatile: field names (`isError`, `tool_use`, `tool_result`), and every vendor's message shapes.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat every tool call as an untrusted request from a semi-trusted client. The tool broker (or MCP server) is the policy enforcement point, not the prompt. Return model-fixable errors as data so the loop can recover, and keep authorisation failures as hard stops that the model cannot argue past.

### 1.2 Structured outputs and strict tool use: what constrained decoding guarantees

Constrained (grammar-constrained) decoding masks tokens during sampling so that the output can only follow a grammar compiled from a JSON Schema.

- Anthropic: setting `strict: true` "guarantees Claude's tool inputs match your JSON Schema by constraining the model's token sampling to schema-valid outputs (a technique called grammar-constrained sampling)". Guarantees listed: tool `input` follows the `input_schema`, and tool `name` is always valid [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use, n.d., accessed 2026-10].
- Anthropic's structured outputs are GA; beta headers are no longer required except for the deprecated `output_format` parameter ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/structured-outputs, n.d., accessed 2026-10].
- **Documented escapes from the guarantee** (Anthropic): a refusal (`stop_reason: "refusal"`) "might not match your schema"; a `max_tokens` stop "might be incomplete and not match your schema"; and "Claude might return a value that differs from your schema only in capitalization" for enums, with no error and no special stop reason [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/structured-outputs, n.d., accessed 2026-10].
- **Unsupported schema features** (Anthropic): recursive schemas, complex types in enums, external `$ref`, numeric constraints (`minimum`, `maximum`, `multipleOf`), string length constraints, array constraints beyond `minItems` of 0 or 1, and `additionalProperties` other than `false`. Unsupported features return a 400 ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/structured-outputs, n.d., accessed 2026-10].
- **Complexity limits** (Anthropic): 20 strict tools per request, 24 optional parameters, 16 union-typed parameters, internal grammar-size limits and a 180-second compilation timeout; the first use of a schema adds compilation latency, and compiled grammars are cached for 24 hours from last use ⚠ [VERIFIED: https://platform.claude.com/docs/en/build-with-claude/structured-outputs, n.d., accessed 2026-10].
- **Data-handling consequence**: compiled schemas are cached separately from message content, so "PHI must not be included in JSON schema definitions" (property names, enum values, const values, patterns) [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use, n.d., accessed 2026-10].
- OpenAI: Structured Outputs "ensures the model will always generate responses that adhere to your supplied JSON Schema"; JSON mode guarantees only valid JSON. Refusals carry a separate `refusal` field and may not follow the schema; truncation at `max_output_tokens` yields an incomplete response [VERIFIED: https://developers.openai.com/api/docs/guides/structured-outputs, n.d., accessed 2026-10].
- OpenAI schema limits: "up to 5000 object properties total, with up to 10 levels of nesting"; total length of names and enum/const values "cannot exceed 120,000 characters"; up to 1,000 enum values in total; unsupported composition keywords include `allOf`, `not`, `dependentRequired`, `dependentSchemas`, `if`/`then`/`else` ⚠ [VERIFIED: https://developers.openai.com/api/docs/guides/structured-outputs, n.d., accessed 2026-10].
- OpenAI function-calling strict mode requires `additionalProperties: false` on every object and every property listed in `required` (optional fields are expressed by allowing `null`). With fine-tuned models, strict mode is disabled when the model makes several function calls in one turn ⚠ [VERIFIED: https://developers.openai.com/api/docs/guides/function-calling, n.d., accessed 2026-10].
- OpenAI also offers **custom tools with free-text input constrained by a context-free grammar** (Lark or regex syntax), with the warning that overly complex grammars can be rejected ⚠ [VERIFIED: https://developers.openai.com/api/docs/guides/function-calling, n.d., accessed 2026-10].
- At launch (August 2024) OpenAI reported that on its internal evals of complex JSON-schema following, gpt-4o-2024-08-06 with Structured Outputs scored 100%, against under 40% for gpt-4-0613. *Evidence age: 26 months, superseded models; vendor eval, not independently reproduced* [WIDELY REPORTED: https://openai.com/index/introducing-structured-outputs-in-the-api/, 2024].
- MCP explicitly separates tool *output* schemas from model-side constrained decoding: "`structuredContent` is server-produced result data and is unrelated to LLM 'structured outputs' (schema-constrained model generation)". If a tool declares an `outputSchema`, servers MUST conform and clients SHOULD validate [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].

**What strict mode guarantees, in one line.** [ASSUMPTION/JUDGEMENT] It guarantees *syntactic* conformance to a *subset* of JSON Schema on the happy path. It does not guarantee semantic correctness (a well-typed `amount: 10000` instead of `100`), authorisation, idempotency, or conformance when the model refuses or is truncated. Numeric ranges and string lengths, which often carry business rules, are among the unsupported keywords on at least one major vendor, so they must be re-checked in the executor.

**Durable vs volatile.** Durable: constrained decoding moves parse failures out of the loop but leaves semantic validation in place; refusal and truncation remain escape paths. Volatile: every limit number, the supported-keyword list, parameter names (`strict`, `output_config.format`, `output_format`), caching windows.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Use strict schemas at every boundary where a tool call becomes a side effect, then validate again server-side against the *full* schema (ranges, formats, cross-field rules) and against policy. Handle `refusal` and `max_tokens` stop reasons as first-class outcomes in the loop. Keep sensitive data out of schemas.

### 1.3 Does constraining format hurt the model? Research evidence

| Study | Type | What was measured | Finding | Limitations |
| --- | --- | --- | --- | --- |
| Tam et al., *Let Me Speak Freely?* (2024) | arXiv preprint, not shown as peer-reviewed | Reasoning and domain-knowledge tasks with outputs restricted to JSON/XML vs free form | "a significant decline in LLMs reasoning abilities under format restrictions"; stricter constraints, larger drops | Only abstract read here; models are 2024-era |
| Geng et al., *JSONSchemaBench* (2025) | arXiv preprint (Microsoft/EPFL authors) | 10K real-world JSON schemas; six engines (Guidance, Outlines, llama.cpp, XGrammar, OpenAI, Gemini); efficiency, coverage, quality | Constrained frameworks beat unconstrained on three reasoning tasks (Guidance: GSM8K 80.1% → 83.8%); coverage varies widely; closed APIs accept fewer schemas | Quality test uses a small open model (Llama-3.1-8B); not comparable across open/closed engines |

- Tam et al. findings as stated in the abstract [VERIFIED: https://arxiv.org/abs/2408.02442, published 2024-08-05, revised 2024-10-14].
- JSONSchemaBench: Guidance reached 0.41 empirical coverage on the "GitHub Hard" set, against 0.13 for unconstrained generation and 0.03 for Outlines; OpenAI reached 0.09 on that set; closed engines had compliance near 1.00 *where they accepted a schema*, reflecting "a conservative strategy of supporting fewer features"; XGrammar had under-constrained failures in 38 test-suite categories. The paper's headline: constrained decoding can speed generation by about 50% and "improves downstream task performance by up to 4%" [VERIFIED: https://arxiv.org/html/2501.10868v3, published 2025-01-18, revised 2025-02-27].

**Durable vs volatile.** Durable: engines differ in which JSON Schema features they actually enforce, and "under-constrained" engines silently accept invalid output. Volatile: every number; both studies predate 2026 models.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A defensible pattern is "reason free, then emit structured": let the model think in text (or extended thinking) and constrain only the final action or record. Test the specific engine against the schemas you use; do not assume full JSON Schema support.

---

## PART 2: Tool design for agents

### 2.1 Anthropic, "Writing effective tools for agents" (September 2025)

Vendor engineering post. It frames tools as "a contract between deterministic software and non-deterministic agents" and recommends an evaluation-driven loop: prototype, evaluate, analyse transcripts, refine [VERIFIED: https://www.anthropic.com/engineering/writing-tools-for-agents, published 2025-09-11].

| Principle (as stated) | Example given | Architectural reading [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- |
| "More tools don't always lead to better outcomes"; consolidate | a `search_logs` tool instead of `read_logs` | Tools should map to tasks, not to API endpoints |
| Namespace related tools | prefixes by service or resource; prefix vs suffix should be tested | Namespacing is also how tool search groups tools (Part 2.3) |
| Return meaningful context | human-readable names over opaque IDs; a `response_format` (concise/detailed) parameter | Shape outputs for the model's next decision |
| Token efficiency | pagination, filtering, truncation with sensible defaults; Claude Code restricts tool responses to 25,000 tokens by default | Bound every result; budget context like memory |
| Actionable errors | error messages that tell the agent what to change | Same as MCP's tool-execution-error class |
| Prompt-engineer descriptions | write for a new hire; `user_id` not `user` | Descriptions are part of the interface contract |

- Reported effects: Claude Sonnet 3.5 reached state-of-the-art on SWE-bench Verified "after precise refinements to tool descriptions"; Claude-optimised Slack and Asana MCP servers outperformed human-written ones on held-out tests (charts, no exact figures in text); a search tool's description fixed a habit of appending "2025" to queries [VERIFIED: https://www.anthropic.com/engineering/writing-tools-for-agents, published 2025-09-11]. *These are vendor-internal evaluations without published numbers for most claims.*

### 2.2 SWE-agent: the agent-computer interface (2024)

- Yang et al. argue that LM agents are "a new category of end users" that need purpose-built interfaces (an **agent-computer interface**, ACI), as humans benefit from IDEs. SWE-agent reached 12.5% pass@1 on SWE-bench and 87.7% on HumanEvalFix, state of the art at the time [VERIFIED: https://arxiv.org/abs/2405.15793, published 2024-05-06, revised 2024-11-11]. Venue: the arXiv page names none; the paper is widely cited as NeurIPS 2024 [ASSUMPTION/JUDGEMENT — not verified this session].
- **Ablations on SWE-bench Lite** (GPT-4 Turbo, full configuration 18.0% resolved) [VERIFIED: https://arxiv.org/html/2405.15793v3, published 2024-11-11]:

| Interface choice | Variant | % resolved |
| --- | --- | --- |
| Editing | edit command with linting guardrail (rejects syntactically broken edits) | 18.0 |
| | edit without linting | 15.0 |
| | no edit command | 10.3 |
| Search | summarised results | 18.0 |
| | iterative (grep-like paging) | 12.0 |
| | no search tools | 15.7 |
| File viewer | 100-line window | 18.0 |
| | 30-line window | 14.3 |
| | full file | 12.7 |
| History | last 5 observations collapsed | 18.0 |
| | full history | 15.0 |

- Stated limitations: the ACI was designed around one model (GPT-4 Turbo) and may not transfer; other open models performed poorly; per-instance cost was capped at $4; the design was chosen by qualitative analysis of a small hand-picked set [VERIFIED: https://arxiv.org/html/2405.15793v3, published 2024-11-11].
- *Evidence age: 29 months; absolute numbers are far below 2026 models.* The durable finding is relative: interface design changed resolution rate by up to about 7.7 points with the model held fixed.

**Durable vs volatile.** Durable: guardrails inside a tool (a linter that rejects broken edits) beat instructions; bounded, summarised observations beat raw dumps; showing *more* (whole file, full history) can hurt. Volatile: the specific window sizes and percentages.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Tool design is an architecture concern, not prompt polish: the tool layer is where you put validation that rejects bad actions before they take effect, and where you bound observation size. Budget for evaluation of tool interfaces the way you budget for API design reviews.

### 2.3 Tool count limits, tool search and deferred loading

| Source | Claim | Measured how |
| --- | --- | --- |
| Anthropic docs | Tool selection "degrades once you exceed 30–50 available tools"; a five-server setup (GitHub, Slack, Sentry, Grafana, Splunk) consumes ~55K tokens of definitions | Vendor statement |
| Anthropic engineering | Tool definitions seen consuming 134K tokens before optimisation; tool search cut an example from ~77K to ~8.7K tokens (85%) | Worked example |
| Anthropic engineering | MCP evals with large tool libraries: Opus 4 49% → 74%, Opus 4.5 79.5% → 88.1% with tool search | Internal evals |
| OpenAI docs | "Aim for fewer than 20 functions available at the start of a turn" (soft guideline) | Vendor guidance |
| Gan & Sun, RAG-MCP (2025) | Retrieval of tools before prompting cut prompt tokens by over 50% and raised tool-selection accuracy from 13.62% to 43.13% | arXiv preprint, MCP stress test |

- Anthropic tool search sources [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool, n.d., accessed 2026-10]; [VERIFIED: https://www.anthropic.com/engineering/advanced-tool-use, published 2025-11-24].
- OpenAI guidance [VERIFIED: https://developers.openai.com/api/docs/guides/function-calling, n.d., accessed 2026-10]. RAG-MCP [VERIFIED: https://arxiv.org/abs/2505.03275, published 2025-05-06].
- **How Anthropic's tool search works**: all definitions are still sent; tools marked `defer_loading: true` stay out of the context until a regex or BM25 search returns `tool_reference` blocks (5 by default), which the API expands into full definitions. Deferred tools are excluded from the cached prefix "so prompt caching is preserved". Limits: 10,000 deferred tools per request; regex patterns up to 200 characters; BM25 queries up to 500 characters. Recommended when there are 10+ tools, >10K tokens of definitions, or 200+ tools aggregated from MCP servers; keep the 3–5 most-used tools non-deferred ⚠ [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool, n.d., accessed 2026-10].
- Custom tool search (e.g. embeddings) is supported by returning `tool_reference` blocks from your own tool [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool, n.d., accessed 2026-10].
- OpenAI offers equivalent `tool_search` with `defer_loading: true` and namespaces, "supported on `gpt-5.4` and later", and an `allowed_tools` option in `tool_choice` that restricts calls to a subset "which helps preserve prompt caching" ⚠ [VERIFIED: https://developers.openai.com/api/docs/guides/function-calling, n.d., accessed 2026-10].
- MCP 2026-07-28 now says servers SHOULD return `tools/list` in deterministic order "to enable client-side caching and improve LLM prompt cache hit rates", and adds `ttlMs`/`cacheScope` to list results [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].

**Durable vs volatile.** Durable: tool definitions are context and cost; selection accuracy falls as the menu grows; just-in-time loading is the fix. Volatile: thresholds (20, 30–50), version strings, model support lists, every accuracy number (all vendor-internal).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat the tool catalogue as a governed registry with names, namespaces and descriptions written for retrieval. Expose a small resident core and defer the rest. Tool search is a *relevance* mechanism, not a *permission* mechanism: a tool that is merely deferred is still callable once found, so authorisation must be decided by which tools are sent at all.

---

## PART 3: Model Context Protocol (MCP)

### 3.1 Version, status and governance (as of 28 October 2026)

- **Current version: 2026-07-28.** MCP versions are dates marking "the last date backwards incompatible changes were made"; revisions are Draft, Current or Final ⚠ [VERIFIED: https://modelcontextprotocol.io/specification/versioning, n.d., accessed 2026-10].
- Trade coverage describes 2026-07-28 as the largest revision since launch, with a release candidate locked on 21 May 2026 [WIDELY REPORTED: https://releases.sh/modelcontextprotocol/mcp-specification.md, 2026].
- **Revision history** relevant to architects:

| Revision | Notable changes |
| --- | --- |
| 2025-03-26 | Streamable HTTP introduced; HTTP+SSE deprecated (per 2026 changelog) |
| 2025-06-18 | Removed JSON-RPC batching; structured tool output; MCP servers classified as OAuth resource servers; RFC 8707 resource indicators required; elicitation; resource links; `MCP-Protocol-Version` header |
| 2025-11-25 | OpenID Connect discovery; incremental scope consent; tool-name guidance; URL-mode elicitation; tool calling inside sampling; Client ID Metadata Documents (CIMD); experimental tasks; JSON Schema 2020-12 as default dialect; formal governance |
| 2026-07-28 | Stateless: no sessions, no `initialize` handshake; `server/discover`; `subscriptions/listen`; Multi Round-Trip Requests replace server-initiated requests; tasks moved to an extension; Roots, Sampling and Logging deprecated; Dynamic Client Registration deprecated in favour of CIMD; SSE resumability removed |

Sources: [VERIFIED: https://modelcontextprotocol.io/specification/2025-06-18/changelog, published 2025-06-18]; [VERIFIED: https://modelcontextprotocol.io/specification/2025-11-25/changelog, published 2025-11-25]; [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].

- **Foundation status.** The Linux Foundation announced the **Agentic AI Foundation (AAIF)** on 9 December 2025 with three founding projects: Anthropic's MCP, Block's goose and OpenAI's AGENTS.md. Platinum members listed: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI [VERIFIED: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation, published 2025-12-09]. AAIF is described as a directed fund of the Linux Foundation [WIDELY REPORTED: https://sdtimes.com/ai/linux-foundation-forms-agentic-ai-foundation-to-be-new-home-for-mcp-goose-and-agents-md/, 2025].
- **Technical governance stays with the project.** MCP is established as "Model Context Protocol a Series of LF Projects, LLC", Apache-2.0 for code and specifications. Technical governance is hierarchical: Lead Maintainers (BDFL, final authority; currently David Soria Parra and Den Delimarsky), Core Maintainers, Maintainers; membership "is for individuals, not companies"; spec changes go through Specification Enhancement Proposals (SEPs) ⚠ [VERIFIED: https://modelcontextprotocol.io/community/governance, n.d., accessed 2026-10].
- **Deprecation policy** (adopted via SEP-2596 in the 2026-07-28 cycle): features move Active → Deprecated → Removed with a minimum twelve-month window; expedited removal to no less than ninety days is allowed only for an active security risk with a published advisory or in-the-wild exploitation [VERIFIED: https://modelcontextprotocol.io/community/feature-lifecycle, n.d., accessed 2026-10].
- A reported MCPA certification programme under AAIF (September 2026) appeared only in secondary search summaries ⚠ [ASSUMPTION/JUDGEMENT — not verified; do not cite without checking].

**Durable vs volatile.** Durable: MCP is now vendor-neutral, foundation-hosted, with a published deprecation policy. Volatile: everything in the revision table; names of maintainers; foundation programmes.

### 3.2 Transports and the stateless redesign

- Two standard transports: **stdio** (newline-delimited JSON-RPC over a client-launched subprocess) and **Streamable HTTP** (each message an HTTP POST to one endpoint, replies as JSON or a request-scoped SSE stream). Custom transports must preserve JSON-RPC, the message patterns and per-request metadata [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports, published 2026-07-28].
- In 2026-07-28, "servers do not initiate JSON-RPC requests and clients do not send JSON-RPC responses"; every request carries protocol version and client capabilities in `_meta` [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports, published 2026-07-28].
- Sessions and `Mcp-Session-Id` are removed; `tools/list` "**MUST NOT** vary per-connection" but **MAY** vary by the authorisation on the request, "for example, returning only the tools the caller's granted scopes permit" [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].
- Servers needing cross-call state mint **explicit handles** passed as ordinary tool arguments. The spec's guidance: "a handle is a name, not a capability" — validate the caller's authorisation against the handle on every call; use opaque, high-entropy, expiring handles; state the retention policy in the creating tool's description [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].
- SSE resumability is gone: "A broken response stream loses the in-flight request; clients **MUST** re-issue it as a new request with a new request ID" [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].
- Streamable HTTP local-server safety: servers **MUST** validate the `Origin` header to prevent DNS rebinding, and when local **SHOULD** bind to 127.0.0.1 rather than 0.0.0.0 [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http, published 2026-07-28].
- Observability: the revision documents W3C trace-context propagation (`traceparent`, `tracestate`, `baggage`) in `_meta` [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].
- Long-running work moved to an official **tasks extension** (`io.modelcontextprotocol/tasks`) with polling via `tasks/get` [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].

**Durable vs volatile.** Durable: stateless request handling, explicit state handles with per-call authorisation, retries as new requests. Volatile: method names, header names, the extension mechanism.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The 2026 redesign aligns MCP with ordinary horizontally scaled HTTP services: any replica can serve any request, and gateways can route on mirrored headers (`Mcp-Method`, `Mcp-Name`, `Mcp-Param-*`). Because a broken stream loses the request, **non-idempotent tools need idempotency keys** at the server; the protocol no longer provides redelivery. Anything that relied on session state must be redesigned as handles bound server-side to the authenticated user.

### 3.3 Authorization (OAuth 2.1-based)

- Authorisation is **OPTIONAL**. HTTP transports SHOULD conform; stdio implementations "**SHOULD NOT** follow this specification, and instead retrieve credentials from the environment" [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization, published 2026-07-28].
- Based on the **OAuth 2.1 IETF draft** (draft-ietf-oauth-v2-1-13), RFC 6750, RFC 8414, RFC 7591, RFC 8707, RFC 9728, RFC 9207, the CIMD draft and OpenID Connect Discovery. *OAuth 2.1 is still an Internet-Draft, not an RFC* ⚠ [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization, published 2026-07-28].
- Key MUSTs: the MCP server is an OAuth resource server and MUST publish RFC 9728 Protected Resource Metadata; clients MUST use PKCE and send the RFC 8707 `resource` parameter (the server's canonical URI) in authorisation and token requests "regardless of whether authorization servers support it"; servers MUST validate that tokens were issued for them as audience; "MCP servers **MUST NOT** accept or transit any other tokens"; tokens MUST NOT be in query strings [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization, published 2026-07-28].
- New in 2026-07-28: clients MUST validate a present `iss` (RFC 9207) before redeeming a code, mitigating **mix-up attacks**; credentials are bound to the issuing authorisation server; Dynamic Client Registration is deprecated in favour of Client ID Metadata Documents [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/changelog, published 2026-07-28].
- Least privilege is designed in: servers SHOULD send the needed `scope` in `WWW-Authenticate`, return 403 `insufficient_scope` at runtime, and clients SHOULD do **step-up authorisation** with the union of old and new scopes, with retry limits [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization, published 2026-07-28].
- What the spec does not cover: the authorisation server's implementation is "beyond the scope of this specification"; additional mechanisms live in a separate `ext-auth` extensions repository [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization, published 2026-07-28].

**What it guarantees / does not.** [ASSUMPTION/JUDGEMENT] The spec guarantees, if implemented, that an MCP server receives a token minted for it, from a discovered authorisation server, with scopes the user consented to. It does not express *which tool calls* a user approved, does not carry the identity of the agent separately from the user, and gives local stdio servers whatever credentials sit in their environment.

**Durable vs volatile.** Durable: audience-bound tokens, no passthrough, incremental scopes. Volatile: CIMD vs DCR, the `iss` SHOULD/MUST level (the spec says a future revision is "expected to upgrade" it to MUST).

### 3.4 Elicitation and Multi Round-Trip Requests

- Elicitation has two modes: **form** (structured data through the client, flat primitive-only schemas) and **URL** (out-of-band navigation for interactions "that must *not* pass through the MCP client") [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation, published 2026-07-28].
- Servers **MUST NOT** use form mode for "passwords, API keys, access tokens, or payment credentials" and MUST use URL mode for them; clients MUST show which server is asking, allow decline/cancel, show the full URL, not pre-fetch it, and not open it without explicit consent, using a browser context the client and LLM cannot inspect [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation, published 2026-07-28].
- URL-mode third-party OAuth: third-party credentials "MUST NOT transit through the MCP client"; the server stores them bound to the user; servers MUST verify that the user completing the flow is the one who started it (the spec walks through an account-takeover phishing scenario) [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation, published 2026-07-28].
- In 2026-07-28, elicitation, sampling and roots requests are delivered via **MRTR**: the server returns `resultType: "input_required"` with `inputRequests`; the client retries the original request with `inputResponses` (and opaque `requestState`) under a new JSON-RPC id [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Elicitation is a protocol-level home for human-in-the-loop *inside* a tool call, and URL mode is the pattern for keeping secrets out of the model context entirely. MRTR makes a paused tool call a stateless retry, which fits durable-execution engines better than a held-open request.

### 3.5 Tool annotations: hints, not controls

- `ToolAnnotations` fields and defaults: `readOnlyHint` (default false), `destructiveHint` (default true, meaningful only if not read-only), `idempotentHint` (default false), `openWorldHint` (default true) [VERIFIED: https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/schema/2026-07-28/schema.ts, published 2026-07-28].
- The schema states: "all properties in `ToolAnnotations` are **hints**. They are not guaranteed to provide a faithful description of tool behavior … Clients should never make tool use decisions based on `ToolAnnotations` received from untrusted servers." The tools page repeats that clients "**MUST** consider tool annotations to be untrusted unless they come from trusted servers" [VERIFIED: https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/schema/2026-07-28/schema.ts, published 2026-07-28]; [VERIFIED: https://modelcontextprotocol.io/specification/2026-07-28/server/tools, published 2026-07-28].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Defaults are conservative (destructive, non-idempotent, open-world) so that a missing annotation errs safe. Annotations are useful for UX (which calls to confirm) only after the server itself is trusted through an allowlist or registry curation; they cannot replace an enforcing permission layer.

### 3.6 Security best practices, real CVEs and tool poisoning

The MCP project's own security page names these attack classes and mitigations [VERIFIED: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices, n.d., accessed 2026-10]:

| Attack | Mechanism | Required / recommended mitigation |
| --- | --- | --- |
| Confused deputy | MCP proxy with a static client ID to a third-party API + dynamic client registration + consent cookie | Proxies MUST implement per-client consent before the third-party flow; exact redirect-URI match; single-use `state` |
| Token passthrough | Server forwards client tokens issued for something else | "MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server" |
| SSRF | Malicious server supplies internal URLs (e.g. `169.254.169.254`) in OAuth metadata | HTTPS only, block private ranges, validate redirects, use an egress proxy (Stripe Smokescreen named), beware DNS-rebinding TOCTOU |
| State-handle hijacking | Guessed or leaked handle reused by another principal | Never treat handle possession as authentication; bind handles to the verified user |
| Local server compromise | Malicious startup command or package; DNS rebinding to localhost | One-click installs MUST show the exact command and get consent; SHOULD sandbox local servers; prefer stdio |
| Authorization URL injection | `javascript:` or shell-metacharacter URLs | Allow only http(s); MUST NOT open URLs via a shell |
| stdio proxy escalation | XSS steals proxy token; proxy spawns arbitrary commands | Sandbox spawned servers; CSP; least-privilege proxy |
| Scope inflation | Broad tokens granted up front | Minimal initial scopes, step-up elevation, no wildcard scopes |

Two of these were real, scored vulnerabilities before the guidance hardened:

- **CVE-2025-49596** (MCP Inspector < 0.14.1): remote code execution "due to lack of authentication between the Inspector client and proxy, allowing unauthenticated requests to launch MCP commands over stdio"; CVSS 4.0 9.4 [VERIFIED: https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-49596, published 2025-06-13].
- **CVE-2025-6514** (`mcp-remote`): OS command injection "when connecting to untrusted MCP servers due to crafted input from the authorization_endpoint response URL"; CVSS 3.1 9.6 [VERIFIED: https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-6514, published 2025-07-09].

Tool metadata and tool results are also attack surfaces:

- **Tool poisoning** (Invariant Labs): instructions hidden in a tool description that the user does not see but the model does. In their demo, a poisoned `add` tool made Cursor read `~/.cursor/mcp.json` and `~/.ssh/id_rsa` and send them out through a parameter; the confirmation dialog did not show full arguments. Variants: **rug pull** (description changes after approval) and **shadowing** (one server's description changes how the agent uses another server's trusted tool). Mitigations proposed: show full descriptions, pin and hash tool definitions, cross-server dataflow controls [VERIFIED: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks, published 2025-04-01].
- **GitHub MCP exfiltration** (Invariant Labs): a malicious issue in a public repository led an agent (Claude Desktop, Claude 4 Opus, official GitHub MCP server) to pull private-repository data into a public pull request. The authors state it is "not a flaw in the GitHub MCP server code itself" but "a fundamental architectural issue" for the agent system; mitigations: per-session least privilege (e.g. one repository per session) and monitoring [VERIFIED: https://invariantlabs.ai/blog/mcp-github-vulnerability, published 2025-05-26].

**Durable vs volatile.** Durable: confused deputy, SSRF, passthrough and supply-chain risks are classic web-security problems that MCP inherits; tool descriptions are executable-in-effect input to the model. Volatile: specific CVEs, product names.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Put an MCP gateway between agents and servers that (a) allowlists servers and pins tool-definition hashes, (b) strips or reviews descriptions before they reach the model, (c) enforces per-session scope (which repos, which tenants), and (d) fronts all outbound fetches with an SSRF-safe egress proxy. Treat local MCP servers as arbitrary code execution with the user's privileges, because that is what they are.

### 3.7 The MCP Registry

- The official registry is "currently in **preview**. Breaking changes or data resets may occur before general availability" ⚠ [VERIFIED: https://modelcontextprotocol.io/registry/about, n.d., accessed 2026-10].
- It stores **metadata only** (`server.json`: name, package location, run instructions), pointing to code in npm, PyPI, Docker Hub and similar; namespaces (reverse-DNS, e.g. `io.github.user/server`) are verified via GitHub, DNS or HTTP challenges [VERIFIED: https://modelcontextprotocol.io/registry/about, n.d., accessed 2026-10].
- It **delegates security scanning** to package registries and downstream aggregators, and it "is not intended to be directly consumed by host applications"; private servers are unsupported, and organisations are advised to run their own registry implementing the published OpenAPI spec [VERIFIED: https://modelcontextprotocol.io/registry/about, n.d., accessed 2026-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Namespace verification proves *who published*, not *that the server is safe*. Enterprises need a curated internal registry (or aggregator) as the allowlist that the MCP gateway enforces.

---

## PART 4: Code execution as tool use

### 4.1 CodeAct (2024)

- Wang et al. propose **executable Python code as a unified action space** run by an interpreter over multiple turns. Across 17 LLMs on API-Bank and a newly curated benchmark, CodeAct achieved "up to 20% higher success rate" than JSON- or text-based actions. They release CodeActInstruct (~7K multi-turn trajectories) and CodeActAgent fine-tuned from Llama 2 and Mistral. Accepted at ICML 2024 [VERIFIED: https://arxiv.org/abs/2402.01030, published 2024-02-01, revised 2024-06-07].
- *Evidence age: 32 months; models are 2023–24 generation; abstract only read here.* The abstract states no limitations; the obvious one is that executing model-written code requires a sandbox [ASSUMPTION/JUDGEMENT].

### 4.2 Code execution with MCP, Code Mode and programmatic tool calling (2025–26)

| Approach | Publisher, date | Mechanism | Reported effect | Stated cost |
| --- | --- | --- | --- | --- |
| Code execution with MCP | Anthropic engineering, 2025-11-04 | Present MCP servers as code APIs (files); agent loads what it needs and processes data in the sandbox | Example workflow ~150,000 → ~2,000 tokens (98.7%) | Needs a secure sandbox, resource limits, monitoring: "operational overhead and security considerations that direct tool calls avoid" |
| Code Mode | Cloudflare, 2025-09-26 | Convert MCP tools to a TypeScript API; run generated code in V8 isolates; no general internet; reach MCP servers only through bindings; supervisor holds API keys | No quantitative results published | — |
| Programmatic tool calling | Anthropic docs (GA) | Claude writes code in the code-execution container that calls your tools; intermediate results do not enter the context | On BrowseComp and DeepSearchQA: +11% average performance with 24% fewer input tokens; earlier post: 43,588 → 27,297 tokens (37%) on complex research tasks | `allowed_callers` "is not a hard API-level block"; strict tools unsupported |

Sources: [VERIFIED: https://www.anthropic.com/engineering/code-execution-with-mcp, published 2025-11-04]; [VERIFIED: https://blog.cloudflare.com/code-mode/, published 2025-09-26]; [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling, n.d., accessed 2026-10]; [VERIFIED: https://www.anthropic.com/engineering/advanced-tool-use, published 2025-11-24].

- Anthropic also lists privacy as a benefit: intermediate data can stay in the execution environment, and the client can tokenise PII before the model sees it [VERIFIED: https://www.anthropic.com/engineering/code-execution-with-mcp, published 2025-11-04].
- Programmatic tool calling docs warn: tool results "are returned as strings" and "can contain any content, including code snippets or executable commands", so validate external results for code-injection risk; "Do not rely on `allowed_callers` as a security boundary" ⚠ [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling, n.d., accessed 2026-10].

### 4.3 What a hosted code-execution sandbox provides (one vendor example)

- Anthropic's server-side code execution tool: container with 5 GiB RAM, 5 GiB disk, 1 CPU; internet access "Completely disabled"; "Full isolation from host system and other containers"; containers expire 30 days after creation and are checkpointed after ~5 minutes idle; not ZDR-eligible; 1,550 free container-hours per organisation per month, then $0.05 per container-hour ⚠ [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool, n.d., accessed 2026-10]. The isolation technology is not named [ASSUMPTION/JUDGEMENT].

**Durable vs volatile.** Durable: code as an action space composes tools, keeps bulk data out of the context and trades a protocol boundary for an execution boundary. Volatile: token-reduction figures (single worked examples), product limits and pricing.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Code mode moves the security boundary from "which tool calls are allowed" to "what the sandbox can reach". The safe shape, visible in both the Cloudflare and Anthropic designs, is: no ambient network, capabilities passed in as bindings or proxied tool calls, credentials held by a supervisor outside the sandbox, and per-call policy at the binding. Without that, a code-executing agent is a remote shell with the union of its tools' permissions.

---

## PART 5: Sandboxing and isolation technology

### 5.1 The isolation ladder

| Mechanism | Boundary | What it guarantees | Known escapes / limits | Typical agent use |
| --- | --- | --- | --- | --- |
| seccomp-bpf | Syscall filter on a process | Reduces exposed kernel surface | "System call filtering isn't a sandbox"; must be combined with other hardening | Building block inside other sandboxes (Codex on Linux) |
| OS app sandbox (Seatbelt on macOS; bubblewrap/namespaces on Linux) | Per-process filesystem and network policy | File and network access limited to policy | Shared host kernel; policy errors (writable `$PATH`, sockets) widen access; weaker modes inside containers | Local CLI agents (Claude Code, Codex) |
| Containers (runc + namespaces + cgroups) | Shared kernel, namespaced view | Process, mount, network isolation from other containers | Kernel and runtime bugs: CVE-2024-21626, three runc CVEs in Nov 2025 | Dev containers, CI, many hosted sandboxes |
| gVisor | User-space kernel (Sentry) intercepts syscalls | Untrusted code does not talk to the host kernel directly | No protection against hardware side channels; DoS left to cgroups; Sentry bugs possible; performance cost on syscall-heavy work | Modal Sandboxes (default runtime) |
| MicroVM (Firecracker on KVM) | Hardware virtualisation, minimal VMM | Separate guest kernel per workload | Hypervisor/VMM bugs; side channels require host mitigations [ASSUMPTION/JUDGEMENT] | AWS Lambda/Fargate; E2B |
| V8 isolates | Language-runtime isolation | No ambient OS access; capabilities only via bindings | JS engine bugs [ASSUMPTION/JUDGEMENT]; only for JS/TS code | Cloudflare Code Mode |

[ASSUMPTION/JUDGEMENT] The ordering is by strength of the boundary against a hostile workload; every row's "guarantee" column is taken from the sources in 5.2–5.6, and the agent-use column from vendor documentation cited there.

### 5.2 Firecracker microVMs

- Agache et al. (AWS), NSDI 2020: Firecracker is a minimal Virtual Machine Monitor on KVM that "offers memory overhead of less than 5MB per container, boots to application code in less than 125ms, and allows creation of up to 150 MicroVMs per second per host"; deployed in AWS Lambda and Fargate, supporting "millions of production workloads, and trillions of requests per month". It deliberately omits BIOS, PCI, legacy devices and VM migration, and was built to avoid choosing between "virtualization with strong security and high overhead, and container technologies with weaker security and minimal overhead" [VERIFIED: https://www.usenix.org/system/files/nsdi20-paper-agache.pdf, published 2020-02]. Peer-reviewed. *Evidence age: 6.5 years; performance figures are for 2019-era hardware.*
- E2B's open-source runtime describes its sandboxes as "Firecracker microVMs that resume from a snapshot", with lazily served memory pages (`userfaultfd`) and copy-on-write root filesystems [VERIFIED: https://github.com/e2b-dev/infra, n.d., accessed 2026-10]. E2B product docs describe a sandbox as "a fast, secure Linux VM created on demand" [VERIFIED: https://docs.e2b.dev/, n.d., accessed 2026-10].

### 5.3 gVisor

- The Sentry intercepts the application's system calls and implements the system API itself; its own host calls are "explicitly enumerated and controlled"; the Gofer mediates filesystem access [VERIFIED: https://gvisor.dev/docs/architecture_guide/security/, n.d., accessed 2026-10].
- Explicit non-goals: "gVisor does not provide protection against hardware side channels"; resource exhaustion relies on host cgroups; "A sandbox is not a substitute for a secure architecture" [VERIFIED: https://gvisor.dev/docs/architecture_guide/security/, n.d., accessed 2026-10].
- Modal Sandboxes run on gVisor by default ("strong isolation and is suitable for most workloads") or on a VM runtime "with its own Linux kernel"; default maximum lifetime 5 minutes, configurable to 24 hours ⚠ [VERIFIED: https://modal.com/docs/guide/sandboxes, n.d., accessed 2026-10].

### 5.4 Containers and their escapes

- **CVE-2024-21626** ("Leaky Vessels"), runc 1.0.0-rc93 to 1.1.11: an internal file-descriptor leak let a container process get a working directory in the host mount namespace, enabling escape; triggerable by a malicious image or via `runc exec`; CVSS 3.1 8.6; fixed in 1.1.12 [VERIFIED: https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv, published 2024-01-31].
- **November 2025 runc CVEs** (CVE-2025-31133, CVE-2025-52565, CVE-2025-52881): three high-severity escapes via procfs write redirection and mount races; all require custom mount configurations, "so they are mainly a risk when running untrusted images or Dockerfiles that use `RUN --mount`". Mitigations named: user namespaces without host root mapped, non-root, rootless containers; the advisory found "neither AppArmor nor SELinux fully protects" against CVE-2025-52881. Fixed in runc 1.2.8, 1.3.3, 1.4.0-rc.3 [VERIFIED: https://www.openwall.com/lists/oss-security/2025/11/05/3, published 2025-11-05].

### 5.5 seccomp and Linux security modules

- The kernel documentation: "System call filtering isn't a sandbox. It provides a clearly defined mechanism for minimizing the exposed kernel surface. It is meant to be a tool for sandbox developers to use", and dynamic filters "could be construed, incorrectly, as a more complete sandboxing solution" [VERIFIED: https://docs.kernel.org/userspace-api/seccomp_filter.html, n.d., accessed 2026-10].

### 5.6 Hosted agent sandboxes: what the documentation does and does not state

| Provider | Stated isolation | Network control (stated) | Gaps in public docs |
| --- | --- | --- | --- |
| E2B | Firecracker microVMs (runtime README) | Not found in product docs this session | Network policy ⚠ |
| Modal | gVisor or VM runtime | Not on the fetched page | — |
| Daytona | "dedicated kernel, filesystem, network stack" (technology unnamed); "under 90ms from code to execution" | Tiers 1–2 restricted, not overridable; tiers 3–4 open by default with per-sandbox CIDR (max 10) or domain (max 100) allowlists, block-all, or an upstream proxy | Isolation technology; whether 90 ms is typical or best case |

Sources: [VERIFIED: https://github.com/e2b-dev/infra, n.d., accessed 2026-10]; [VERIFIED: https://modal.com/docs/guide/sandboxes, n.d., accessed 2026-10]; [VERIFIED: https://www.daytona.io/docs/en/, n.d., accessed 2026-10]; [VERIFIED: https://www.daytona.io/docs/en/network-limits/, n.d., accessed 2026-10]. Daytona's doc explicitly warns to "Pair it with a domain allow list so clients that ignore `HTTP_PROXY` cannot bypass the proxy" ⚠.

**Durable vs volatile.** Durable: the isolation ladder and its trade-offs (density and start-up vs kernel-sharing risk); seccomp is a component, not a sandbox; containers have a recurring escape history. Volatile: vendor runtimes, limits and tiering.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Match boundary strength to the hostility of the code: agent-generated code influenced by untrusted input (web pages, tickets, repositories) is hostile code and belongs behind a separate kernel (microVM or gVisor) when multi-tenant. A shared-kernel container is acceptable for a single trusted tenant with no secrets in reach. Keep runtimes patched as a standing operational task, because escape CVEs recur.

---

## PART 6: Network egress control

- **Why it is the second half of every sandbox.** Anthropic: "Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys", and without filesystem isolation a compromised agent could escape and gain network access [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20].
- **Hostname allowlists through a proxy have a documented bypass.** Claude Code's proxy decides "from the client-supplied hostname without inspecting TLS", so code inside the sandbox "can potentially use domain fronting or similar techniques to reach hosts outside the allowlist"; "Allowing broad domains such as `github.com` can create paths for data exfiltration"; stronger guarantees need a custom TLS-terminating proxy with its CA installed in the sandbox ⚠ [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- Other proxy limits stated there: tools that ignore proxy variables (plain `ssh`, most database drivers) cannot connect; non-TCP traffic (UDP, QUIC, ICMP) cannot leave; an allowlisted domain without a port allows every port [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- **Credential injection at the proxy.** Claude Code on the web keeps git credentials and signing keys outside the sandbox; a custom git proxy authenticates a scoped credential, checks the request (e.g. pushes only to the configured branch) and attaches the real token [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20]. Cloudflare Code Mode follows the same pattern: the supervisor holds API keys and code reaches services only through bindings [VERIFIED: https://blog.cloudflare.com/code-mode/, published 2025-09-26].
- **SSRF-safe egress** for server-side agents: the MCP guidance recommends blocking private and link-local ranges (including cloud metadata), validating each redirect hop, pinning DNS between check and use, and routing through an egress proxy such as Stripe's Smokescreen; "Avoid implementing IP validation manually" because of encoding tricks [VERIFIED: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices, n.d., accessed 2026-10].
- **Default-deny is now common for local coding agents.** Codex CLI: "Defaults include no network access and write permissions limited to the active workspace"; web search defaults to an OpenAI-maintained cache "to reduce exposure to prompt injection from arbitrary live content" ⚠ [VERIFIED: https://learn.chatgpt.com/docs/agent-approvals-security, n.d., accessed 2026-10]. Anthropic's hosted code execution has no internet [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool, n.d., accessed 2026-10]. Claude Code's sandbox starts with an empty `allowedDomains` but is itself off by default ⚠ [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].

**Durable vs volatile.** Durable: egress is the exfiltration channel of the "lethal trifecta" (Part 9); hostname-only filtering is bypassable; secrets belong in a proxy, not in the sandbox. Volatile: product defaults and settings names.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Design egress as a first-class component: default-deny, an allowlist of narrow hostnames (not whole developer platforms), a TLS-terminating proxy where content inspection matters, credential injection at the proxy, and egress logs as audit evidence. A write-capable allowlisted destination (a code host, a paste site, a ticketing system) is an exfiltration path even with a perfect allowlist.

---

## PART 7: Permission models for CLI agents

### 7.1 Claude Code: rules, modes and precedence

- Rules are evaluated "deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order"; "An allow rule can't carve an exception out of a deny rule" [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].
- Modes: `default` (Manual; prompt on first use), `acceptEdits`, `plan` (read-only exploration), `auto` (a background classifier checks actions), `dontAsk` (auto-deny anything that would prompt), `bypassPermissions` (skip prompts; "Only use this mode in isolated environments like containers or VMs") ⚠ [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].
- Managed settings sit at the top of precedence; "If a tool is denied at any level, no other level can allow it"; administrators can disable bypass and auto modes [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].
- **Documented limits of pattern rules**: "Bash permission patterns that try to constrain command arguments are fragile" — `Bash(curl http://github.com/ *)` misses option reordering, other protocols, redirects and variables; a deny rule "doesn't match the same program by path or inside `sh -c`"; "using WebFetch alone doesn't prevent network access. If Bash is allowed, Claude can still use `curl`"; Read/Edit deny rules do not apply to "a Python or Node script that opens files itself" — for that, enable the OS sandbox [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].
- Permissions and sandboxing are "complementary security layers … sandbox restrictions still apply even if a prompt injection bypasses Claude's decision-making" [VERIFIED: https://code.claude.com/docs/en/permissions, n.d., accessed 2026-10].

### 7.2 Claude Code sandbox: scope and escape hatches

- Built on Seatbelt (macOS) and bubblewrap (Linux/WSL2) via the open-source `@anthropic-ai/sandbox-runtime`; native Windows runs unsandboxed; **off by default**; if the sandbox cannot start, Claude Code by default runs commands unsandboxed unless `failIfUnavailable` is set ⚠ [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- Scope: "The sandbox covers shell commands only. Claude's file tools, MCP servers, and hooks run outside it." Reads are broad by default, including `~/.ssh` and `~/.aws/credentials`, unless denied [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- Escape hatch: after a sandboxed failure Claude "may retry the command with the `dangerouslyDisableSandbox` parameter"; approval depends on the mode (no prompt in `bypassPermissions`, classifier in auto); disable with `allowUnsandboxedCommands: false` [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- Listed security limitations: domain fronting (Part 6); Unix sockets (e.g. `/var/run/docker.sock` "effectively grants access to the host system"); writable `$PATH` or shell rc files; `enableWeakerNestedSandbox` inside Docker "considerably weakens security"; `allowAppleEvents` "removes code-execution isolation"; `allowNestedUserNamespaces` turns off a boundary [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- Effect claimed: sandboxing "safely reduces permission prompts by 84%" in internal usage; measurement method not described [VERIFIED: https://www.anthropic.com/engineering/claude-code-sandboxing, published 2025-10-20].

### 7.3 Classifier-gated autonomy: Claude Code auto mode and an independent stress test

- Anthropic (March 2026): a two-stage transcript classifier (Sonnet 4.6) reviews actions before execution. It sees user messages and tool calls but not assistant text or tool results ("reasoning-blind by design"); a separate probe screens tool results for prompt injection; allow rules and in-project file edits skip the classifier [VERIFIED: https://www.anthropic.com/engineering/claude-code-auto-mode, published 2026-03-25].
- Anthropic's numbers: full-pipeline false-positive rate 0.4% on 10,000 real internal tool calls; false-negative rate 17% on 52 real "overeager" actions ("the honest number") and 5.7% on 1,000 synthetic exfiltration attempts. Motivation: users accept "93%" of manual permission prompts. Stated limit: auto mode "is not a drop-in replacement for careful human review on high-stakes infrastructure" [VERIFIED: https://www.anthropic.com/engineering/claude-code-auto-mode, published 2026-03-25].
- Independent stress test (Ji et al., arXiv preprint): on AmPermBench (128 deliberately ambiguous DevOps prompts, 253 state-changing actions checked against oracle ground truth), end-to-end false-negative rate 81.0% (95% CI 73.8–87.4%); 36.8% of state-changing actions were in-project file edits outside the classifier's scope; on the 160 actions the classifier did see, FNR 70.3% and FPR 31.9%. The authors frame it as a "coverage boundary" (dangerous effects reachable through file edits) and say results describe "scope-escalation coverage under this stress-test workload", not a production error rate [VERIFIED: https://arxiv.org/abs/2604.04978, published 2026-04-04, revised 2026-10-22].

### 7.4 OpenAI Codex CLI: sandbox modes and approval policies

- Sandbox modes: `read-only`, `workspace-write` (default low-friction mode), `danger-full-access` (no sandbox). Approval policies: `on-request` and `never`; "Codex and ChatGPT Work no longer support `untrusted` as a selectable approval policy" ⚠. An `approvals_reviewer` can be `user` or `auto_review` (a reviewer agent) [VERIFIED: https://learn.chatgpt.com/docs/sandboxing, n.d., accessed 2026-10].
- OS mechanisms: macOS Seatbelt (`sandbox-exec` with a profile); Linux "bwrap plus seccomp by default"; native Windows sandbox; inside Docker the sandbox may not work, in which case run `danger-full-access` *inside a container that provides the isolation* [VERIFIED: https://learn.chatgpt.com/docs/agent-approvals-security, n.d., accessed 2026-10].
- Protected paths inside writable roots are read-only: `.git` (including a resolved gitdir), `.agents`, `.codex`, `.aws` [VERIFIED: https://learn.chatgpt.com/docs/agent-approvals-security, n.d., accessed 2026-10].
- Codex docs separate the two controls: "The sandbox defines technical boundaries. The approval policy decides when the agent must stop and ask before crossing them" [VERIFIED: https://learn.chatgpt.com/docs/sandboxing, n.d., accessed 2026-10].

### 7.5 Vulnerabilities in the permission layer itself

| CVE | Product | Flaw | Precondition | Fixed |
| --- | --- | --- | --- | --- |
| CVE-2025-54794 | Claude Code | Path validation used prefix matching instead of canonical comparison, allowing access outside the working directory | A same-prefix directory and untrusted content in context | 0.2.111 |
| CVE-2025-54795 | Claude Code | Command-parsing error let an untrusted command bypass the confirmation prompt | Untrusted content in context | 1.0.20 |
| CVE-2025-59532 | Codex CLI | Sandbox treated a **model-generated cwd** as the writable root, allowing writes and commands outside the session folder (network restriction unaffected) | — | 0.39.0 |

Sources: [VERIFIED: https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-54794, published 2025-08-05]; [VERIFIED: https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-54795, published 2025-08-05]; [VERIFIED: https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-59532, published 2025-09-22]. CVSS (NVD): 54794 v3.1 9.1 / v4.0 7.7; 54795 v3.1 9.8 / v4.0 8.7; 59532 v4.0 8.6.

**Durable vs volatile.** Durable: permission rules govern *the agent's tools*; OS sandboxes govern *processes*; classifiers govern *intent* probabilistically; none is complete alone. The three CVEs share a lesson — boundaries must be computed from trusted inputs (canonical paths, the session's start directory), never from model output. Volatile: mode names, defaults, classifier figures.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Layer three controls and know what each catches: (1) deterministic deny rules and managed policy for known-bad actions; (2) an OS or VM boundary for everything a rule cannot see (scripts, subprocesses); (3) human or classifier review for ambiguous, high-blast-radius actions. Prompt fatigue (93% approval) means manual approval alone is weak evidence of oversight. Measure your classifier on *your* workload: the 17% vs 81% gap shows the error rate depends on the task mix and on which actions are in scope at all.

---

## PART 8: Browser and computer-use agents

- **Capability gap (2024 baseline).** OSWorld: 369 real computer tasks; humans complete over 72.36%, best model 12.24% at publication [VERIFIED: https://arxiv.org/abs/2404.07972, published 2024-04-11]. *Evidence age: 30 months; 2026 models score far higher, but no current figure was verified for this brief* ⚠.
- **Anthropic computer use**: current tool is `computer_toolset_20260801` (17 member tools), GA on the Claude API ⚠. Recommended precautions: a dedicated VM or container with minimal privileges; no access to sensitive data such as logins; an allowlist of domains; human confirmation for consequential actions such as "accepting cookies, completing financial transactions, or agreeing to terms of service". Classifiers scan screenshots for prompt injection and steer the model to check with the user, but "the precautions listed earlier remain important even with these classifiers in place" [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool, n.d., accessed 2026-10].
- Stated limitations include latency, coordinate hallucination, tool-selection mistakes, scrolling and spreadsheet reliability, and vulnerability to "instructions embedded in webpages or images"; "Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight". The toolset definition alone adds about 4,500 input tokens per request [VERIFIED: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool, n.d., accessed 2026-10].
- Claude Code notes that computer use "runs on your actual desktop rather than in an isolated environment", gated by per-app prompts [VERIFIED: https://code.claude.com/docs/en/sandboxing, n.d., accessed 2026-10].
- **Browser agent red-teaming (Claude for Chrome, August 2025)**: 123 test cases across 29 attack scenarios; prompt-injection attack success 23.6% without mitigations, 11.2% with them (autonomous mode); a browser-specific challenge set fell from 35.7% to 0%. Mitigations: site-level permissions, confirmation before publishing, purchasing or sharing personal data, blocked site categories (e.g. financial services), system-prompt hardening, classifiers in development [VERIFIED: https://claude.com/blog/claude-for-chrome, published 2025-08-25]. *Vendor-run evaluation; 11.2% residual success is the figure to carry.*
- OpenAI (December 2025, Atlas): "Prompt injection, much like scams and social engineering on the web, is unlikely to ever be fully 'solved'"; it built an RL-trained automated attacker and shipped an adversarially trained model; a spokesperson declined to share measured reduction [WIDELY REPORTED: https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/, 2025].

**Durable vs volatile.** Durable: a browser agent reads attacker-controlled content by design and acts with the user's sessions; residual injection success is non-zero after vendor mitigations; consequential actions need confirmation outside the model. Volatile: tool versions, success rates, product names.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Run browser and desktop agents in disposable VMs with a separate, low-privilege browser profile (no saved passwords, no payment methods), with site allowlists, and with a deterministic confirmation step for irreversible actions (payments, sends, account changes) enforced by the harness rather than requested by the model. Prefer an API tool over computer use whenever one exists: an API has a schema, scopes and audit logs; a screen has none.

---

## PART 9: Cross-cutting — prompt injection constrains tool architecture

- **The lethal trifecta** (Willison): an agent with (1) access to private data, (2) exposure to untrusted content and (3) the ability to communicate externally can be tricked into exfiltration; guardrails claiming to catch "95% of attacks" are inadequate because "in web application security 95% is very much a failing grade"; "The only way to stay safe there is to avoid that lethal trifecta combination entirely" [VERIFIED: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/, published 2025-06-16]. Practitioner blog, widely cited.
- **Design patterns** (Beurer-Kellner et al., 14 authors across industry and academia): six patterns — Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute, Context-Minimization — organised around the principle that once an agent has ingested untrusted input "it must be constrained so that it is impossible for that input to trigger any consequential actions" [VERIFIED: https://arxiv.org/html/2506.08837v3, published 2025-06-10, revised 2025-06-27]. arXiv preprint.
- **CaMeL** (Debenedetti et al., Google DeepMind and ETH authors): extracts control and data flow from the trusted user query so "the untrusted data retrieved by the LLM can never impact the program flow", and attaches capabilities to data to enforce policies at tool calls; on AgentDojo it solves 77% of tasks "with provable security" against 84% for an undefended system [VERIFIED: https://arxiv.org/abs/2503.18813, published 2025-03-24, revised 2025-06-24]. arXiv preprint; benchmark-scale evaluation, not a production deployment.

**Durable vs volatile.** Durable: capability separation between components that read untrusted data and components that hold tools; dataflow policy at the tool boundary; a measurable utility cost (≈7 points in CaMeL). Volatile: specific frameworks and benchmark numbers.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Every tool should be classified on the three trifecta axes (reads private data / ingests untrusted content / can send outward), and the orchestrator should refuse to place all three in one context without an approval gate or a dataflow policy. Plan-then-execute and code-then-execute fit naturally with Part 4: the plan or program is fixed from trusted input, then run in a sandbox whose bindings enforce what data can flow where.

---

## Key numbers

| Number | What it measured | Source and date |
| --- | --- | --- |
| 2026-07-28 | Current MCP protocol revision | MCP versioning page, accessed 2026-10 |
| 12 months / 90 days | MCP minimum deprecation window / expedited-removal floor | MCP feature lifecycle policy, 2026 |
| 2025-12-09 | AAIF formation (MCP, goose, AGENTS.md) | Linux Foundation press release |
| 20 / 24 / 16 | Anthropic strict tools per request / optional params / union-typed params | Anthropic structured-outputs docs, accessed 2026-10 |
| 180 s; 24 h | Anthropic grammar compilation timeout; compiled-grammar cache | Same |
| 5,000 props; 10 levels | OpenAI structured-output schema size and nesting limits | OpenAI structured-outputs guide, accessed 2026-10 |
| 100% vs <40% | OpenAI internal complex-schema eval, gpt-4o-2024-08-06 strict vs gpt-4-0613 | OpenAI launch post, 2024 (widely reported) |
| 80.1% → 83.8% | GSM8K, Llama-3.1-8B, unconstrained vs Guidance constrained | JSONSchemaBench, 2025 |
| 0.09 | OpenAI empirical coverage on JSONSchemaBench "GitHub Hard" schemas | JSONSchemaBench, 2025 |
| 18.0% vs 10.3% | SWE-bench Lite resolved, SWE-agent with vs without edit command (GPT-4 Turbo) | SWE-agent v3, 2024-11 |
| 25,000 tokens | Claude Code default tool-response cap | Anthropic "Writing effective tools", 2025-09 |
| 30–50 tools | Point at which Claude tool-selection accuracy degrades (vendor statement) | Anthropic tool search docs, accessed 2026-10 |
| <20 functions | OpenAI soft guideline for tools at start of a turn | OpenAI function-calling guide, accessed 2026-10 |
| ~55K tokens | Definitions for 58 tools across five MCP servers | Anthropic advanced tool use, 2025-11-24 |
| 49% → 74%; 79.5% → 88.1% | Internal MCP eval accuracy with tool search, Opus 4; Opus 4.5 | Same |
| 10,000 | Maximum deferred tools per Anthropic request | Tool search docs, accessed 2026-10 |
| 13.62% → 43.13% | Tool selection accuracy, baseline vs RAG-MCP | RAG-MCP preprint, 2025-05 |
| ~150K → ~2K tokens (98.7%) | One worked workflow, direct MCP tools vs code execution | Anthropic, 2025-11-04 |
| +11%, −24% tokens | BrowseComp/DeepSearchQA average with programmatic tool calling | Anthropic PTC docs, accessed 2026-10 |
| up to 20% | Success-rate gain of CodeAct over JSON/text actions, 17 LLMs | CodeAct, ICML 2024 |
| <5 MB; <125 ms; 150/s | Firecracker memory overhead, boot time, microVM creation rate per host | NSDI 2020 |
| 84% | Reduction in Claude Code permission prompts with sandboxing (internal usage, method not stated) | Anthropic, 2025-10-20 |
| 93% | Share of manual permission prompts users accept | Anthropic auto mode post, 2026-03-25 |
| 0.4% / 17% / 5.7% | Auto mode FPR on real traffic / FNR on 52 real overeager actions / FNR on synthetic exfiltration | Same |
| 81.0% (CI 73.8–87.4) | Auto mode end-to-end FNR on AmPermBench stress test | Ji et al., arXiv 2026-04 (v3 2026-10) |
| 23.6% → 11.2% | Prompt-injection attack success on Claude for Chrome, 123 cases, without vs with mitigations | Anthropic, 2025-08-25 |
| 72.36% vs 12.24% | OSWorld success, humans vs best model at publication | OSWorld, 2024-04 |
| 77% vs 84% | AgentDojo tasks solved, CaMeL vs undefended | CaMeL, 2025 |
| 9.4 / 9.6 | CVSS of MCP Inspector RCE / mcp-remote command injection | NVD, 2025 |

## Where sources disagree

- **Does constraining output format hurt reasoning?** Tam et al. report "a significant decline" in reasoning under format restrictions; JSONSchemaBench reports constrained decoding *improves* three reasoning tasks by up to about 4 points. They measure different things (prompted format instructions across tasks vs grammar-constrained decoding with token healing on one small model). [ASSUMPTION/JUDGEMENT] Both support "reason freely, constrain the final action".
- **How reliable is classifier-gated autonomy?** Anthropic reports a 17% false-negative rate on real overeager actions and 0.4% false positives; an independent stress test reports 81% end-to-end FNR and 31.9% FPR on in-scope actions. The authors attribute the gap to workload and to file edits outside the classifier's scope, not to contradiction. Chapter writers should present both and the reason for the gap.
- **How strong is a "sandbox"?** Vendors use the word for very different boundaries: Seatbelt/bubblewrap process policies (Claude Code, Codex), gVisor (Modal), Firecracker microVMs (E2B), unnamed container isolation (Anthropic code execution, Daytona). Claude Code's own docs say its sandbox "is not a complete isolation boundary". [ASSUMPTION/JUDGEMENT] The book should never use "sandboxed" without naming the boundary.
- **Default posture differs.** Codex CLI defaults to an OS sandbox with no network; Claude Code's sandbox is off by default and falls back to unsandboxed if it cannot start, unless configured otherwise. Both change over time ⚠.
- **Human-in-the-loop expectations.** The MCP spec says there SHOULD always be a human able to deny tool invocations; vendors are actively building modes that remove routine prompts (auto mode, `auto_review`), citing prompt fatigue (93% approval). [ASSUMPTION/JUDGEMENT] The reconciliation is risk-tiered approval, not universal prompting.
- **Tool count guidance.** OpenAI suggests fewer than 20 tools at turn start; Anthropic says degradation sets in at 30–50 and recommends tool search from 10 tools. These are vendor heuristics for different models, not measured thresholds.
- **Which side holds the security boundary for code mode.** Anthropic presents code execution with MCP as a context-efficiency win with sandbox costs; Cloudflare presents isolates plus bindings as also a credential-safety win. Both agree the sandbox design, not the model, decides safety.

## Open questions / not verifiable

- No independent, cross-vendor benchmark of tool-search or deferred-loading accuracy was found; all accuracy gains in Part 2.3 are vendor-internal except RAG-MCP.
- The isolation technology behind Anthropic's hosted code execution, Daytona sandboxes and OpenAI's hosted Codex/Work containers is not publicly documented in the pages fetched.
- How widely the MCP 2026-07-28 stateless revision has been adopted by SDKs, gateways and major hosts is unknown; adoption figures circulating in press were not verified.
- Whether the MCP Registry has left preview, and any AAIF certification programme, could not be verified ⚠.
- E2B's network-egress model (reported elsewhere as an nftables firewall with SNI/Host-based allow/deny) is unverified.
- OpenAI's December 2025 Atlas post and any measured injection-rate reduction were not fetched; OpenAI declined to share numbers per press.
- Current (2026) OSWorld or computer-use success rates were not verified.
- The 84% prompt-reduction figure for Claude Code sandboxing has no published methodology.
- Whether SWE-agent was published at NeurIPS 2024 was not confirmed from the arXiv page.

## Source list

| Title | Author / publisher | Year | URL | Type |
| --- | --- | --- | --- | --- |
| MCP Specification 2026-07-28: Key Changes | MCP project (AAIF / LF Projects) | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/changelog | spec |
| MCP Versioning | MCP project | 2026 | https://modelcontextprotocol.io/specification/versioning | spec |
| MCP Tools (2026-07-28) | MCP project | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/server/tools | spec |
| MCP schema.ts (2026-07-28) | MCP project | 2026 | https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/schema/2026-07-28/schema.ts | spec |
| MCP Authorization (2026-07-28) | MCP project | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization | spec |
| MCP Elicitation (2026-07-28) | MCP project | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation | spec |
| MCP Transports (2026-07-28) | MCP project | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports | spec |
| MCP Streamable HTTP (2026-07-28) | MCP project | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http | spec |
| MCP Key Changes 2025-11-25 | MCP project | 2025 | https://modelcontextprotocol.io/specification/2025-11-25/changelog | spec |
| MCP Key Changes 2025-06-18 | MCP project | 2025 | https://modelcontextprotocol.io/specification/2025-06-18/changelog | spec |
| MCP Security Best Practices | MCP project | 2026 | https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices | docs |
| MCP Governance and Stewardship | MCP project | n.d. | https://modelcontextprotocol.io/community/governance | docs |
| MCP Feature Lifecycle and Deprecation Policy | MCP project | 2026 | https://modelcontextprotocol.io/community/feature-lifecycle | docs |
| The MCP Registry | MCP project | n.d. | https://modelcontextprotocol.io/registry/about | docs |
| Linux Foundation announces the formation of the Agentic AI Foundation | Linux Foundation | 2025 | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | press |
| Linux Foundation forms Agentic AI Foundation | SD Times | 2025 | https://sdtimes.com/ai/linux-foundation-forms-agentic-ai-foundation-to-be-new-home-for-mcp-goose-and-agents-md/ | press |
| MCP specification releases | releases.sh | 2026 | https://releases.sh/modelcontextprotocol/mcp-specification.md | press |
| JSON Schema Specification | JSON Schema project | n.d. | https://json-schema.org/specification | spec |
| Strict tool use | Anthropic | n.d. | https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use | docs |
| Structured outputs | Anthropic | n.d. | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | docs |
| Tool search tool | Anthropic | n.d. | https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool | docs |
| Programmatic tool calling | Anthropic | n.d. | https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling | docs |
| Code execution tool | Anthropic | n.d. | https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool | docs |
| Computer use tool | Anthropic | n.d. | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool | docs |
| Writing effective tools for AI agents | Anthropic (K. Aizawa) | 2025 | https://www.anthropic.com/engineering/writing-tools-for-agents | engineering post |
| Introducing advanced tool use | Anthropic | 2025 | https://www.anthropic.com/engineering/advanced-tool-use | engineering post |
| Code execution with MCP | Anthropic (A. Jones, C. Kelly) | 2025 | https://www.anthropic.com/engineering/code-execution-with-mcp | engineering post |
| Making Claude Code more secure and autonomous (sandboxing) | Anthropic (D. Dworken, O. Weller-Davies) | 2025 | https://www.anthropic.com/engineering/claude-code-sandboxing | engineering post |
| Claude Code auto mode | Anthropic (J. Hughes) | 2026 | https://www.anthropic.com/engineering/claude-code-auto-mode | engineering post |
| Claude Code: Sandboxing | Anthropic | n.d. | https://code.claude.com/docs/en/sandboxing | docs |
| Claude Code: Configure permissions | Anthropic | n.d. | https://code.claude.com/docs/en/permissions | docs |
| Piloting Claude for Chrome | Anthropic | 2025 | https://claude.com/blog/claude-for-chrome | engineering post |
| Function calling guide | OpenAI | n.d. | https://developers.openai.com/api/docs/guides/function-calling | docs |
| Structured Outputs guide | OpenAI | n.d. | https://developers.openai.com/api/docs/guides/structured-outputs | docs |
| Introducing Structured Outputs in the API | OpenAI | 2024 | https://openai.com/index/introducing-structured-outputs-in-the-api/ | engineering post (not fetched, 403) |
| Codex: Sandbox | OpenAI | n.d. | https://learn.chatgpt.com/docs/sandboxing | docs |
| Codex: Agent approvals and security | OpenAI | n.d. | https://learn.chatgpt.com/docs/agent-approvals-security | docs |
| OpenAI says AI browsers may always be vulnerable to prompt injection attacks | TechCrunch | 2025 | https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/ | press |
| Code Mode: the better way to use MCP | Cloudflare (K. Varda, S. Pai) | 2025 | https://blog.cloudflare.com/code-mode/ | engineering post |
| Let Me Speak Freely? Format restrictions and LLM performance | Tam et al. | 2024 | https://arxiv.org/abs/2408.02442 | paper (preprint) |
| JSONSchemaBench | Geng et al. | 2025 | https://arxiv.org/abs/2501.10868 | paper (preprint) |
| SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | Yang et al. | 2024 | https://arxiv.org/abs/2405.15793 | paper |
| Executable Code Actions Elicit Better LLM Agents (CodeAct) | Wang et al. | 2024 | https://arxiv.org/abs/2402.01030 | paper (ICML 2024) |
| RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection | Gan, Sun | 2025 | https://arxiv.org/abs/2505.03275 | paper (preprint) |
| OSWorld | Xie et al. | 2024 | https://arxiv.org/abs/2404.07972 | paper |
| Defeating Prompt Injections by Design (CaMeL) | Debenedetti et al. | 2025 | https://arxiv.org/abs/2503.18813 | paper (preprint) |
| Design Patterns for Securing LLM Agents against Prompt Injections | Beurer-Kellner et al. | 2025 | https://arxiv.org/abs/2506.08837 | paper (preprint) |
| Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode | Ji et al. | 2026 | https://arxiv.org/abs/2604.04978 | paper (preprint) |
| Firecracker: Lightweight Virtualization for Serverless Applications | Agache et al. (AWS) | 2020 | https://www.usenix.org/system/files/nsdi20-paper-agache.pdf | paper (NSDI 2020) |
| gVisor Security Model | gVisor project (Google) | n.d. | https://gvisor.dev/docs/architecture_guide/security/ | docs |
| Seccomp BPF | Linux kernel documentation | n.d. | https://docs.kernel.org/userspace-api/seccomp_filter.html | docs |
| runc advisory GHSA-xr7r-f8xq-vfvv (CVE-2024-21626) | Open Container Initiative | 2024 | https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv | incident report |
| runc container breakouts (CVE-2025-31133, -52565, -52881) | A. Sarai, oss-security | 2025 | https://www.openwall.com/lists/oss-security/2025/11/05/3 | incident report |
| E2B Runtime README | E2B | n.d. | https://github.com/e2b-dev/infra | docs |
| E2B documentation | E2B | n.d. | https://docs.e2b.dev/ | docs |
| Modal Sandboxes | Modal | n.d. | https://modal.com/docs/guide/sandboxes | docs |
| Daytona documentation | Daytona | n.d. | https://www.daytona.io/docs/en/ | docs |
| Daytona network limits | Daytona | n.d. | https://www.daytona.io/docs/en/network-limits/ | docs |
| CVE-2025-54794, CVE-2025-54795 (Claude Code) | NVD | 2025 | https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-54794 | incident report |
| CVE-2025-59532 (Codex CLI) | NVD | 2025 | https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-59532 | incident report |
| CVE-2025-49596 (MCP Inspector) | NVD | 2025 | https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-49596 | incident report |
| CVE-2025-6514 (mcp-remote) | NVD | 2025 | https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-6514 | incident report |
| MCP Security Notification: Tool Poisoning Attacks | Invariant Labs | 2025 | https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks | incident report |
| GitHub MCP Exploited: Accessing private repositories via MCP | Invariant Labs | 2025 | https://invariantlabs.ai/blog/mcp-github-vulnerability | incident report |
| The lethal trifecta for AI agents | Simon Willison | 2025 | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | engineering post |
| LLM06:2025 Excessive Agency | OWASP GenAI Security Project | 2024 | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | standard |
