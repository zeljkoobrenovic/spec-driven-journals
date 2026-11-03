# Review — Part IX (ECONOMICS), 2026-10-28

Scope: `part-9-intro`, `35-agent-latency-and-throughput`, `36-agent-cost-and-model-routing`, `37-caching-and-context-budgets`; `14-context-engineering` read only for reconciliation. Build passes; `render_check.py` reports 0 problems for all four pages (mermaid 1/3/4/2, no failures, no unresolved links).

## Word counts (front matter to "Sources and Evidence", tables de-piped, code and mermaid excluded)

| Page | Before | After |
| --- | --- | --- |
| part-9-intro | 1,016 | 898 |
| 35 | 7,685 | 7,749 |
| 36 | 7,017 | 7,036 |
| 37 | 6,997 | 7,034 |

## Answerdesk figures reconciled across 14, 35, 36, 37

| Figure | Source of truth | Status |
| --- | --- | --- |
| 24,000-token per-call cap; evidence ≤ 6,000; compaction trigger 16,000 | ledger + 14 | 37 agreed on the totals, but its slot table did not (see 37 below). Fixed. |
| 14 always-loaded tools ≈ 3,000 tokens | ledger + 14 | 37 said **~5,400** → now **≈ 3,000**. 37's L1 ~3,100 → **1,800**, L2–L3 ~2,000 → **400 + 600**, matching 14. |
| ≈ 14,000 input tokens per call | 14 (13,900 mean, July 2027) | 35 uses 14,000 (rounded). OK. |
| Cache-read share 11% (May) → 76% (July) | ledger | 14, 37, intro agree. 35 uses **78%** at the Monday peak (ledger 35 line). Kept (the ceiling of 3.4/s depends on it) and labeled in 35 as the peak rate, above July's 76% monthly average. |
| Input spend per conversation down "about two thirds" | ledger | 14, 36, 37 agree; 37's arithmetic 1.05 → 0.34. OK. |
| Model spend €120 / 1,000; agent-side €0.39 per resolved; €5.50 per escalation; profile B €50, −€57, ~€148,000/yr | ledger | Recomputed in 36: all consistent (B: €70 − 2.4 × €5.50 ≈ €57; × 2,600 ≈ €147,700). |
| Chat budget ≤ 2 s / ≤ 6 s / ≤ 30 s; 9.6 s → 1.8 s; 11.8 s → 5.6 s | ledger | 35 and intro agree. |
| 2.1/s peak; 3.4/s ceiling; 1.2/s at 40% | ledger | Recomputed (1.6 × 14,000 × 0.22 ≈ 4,900; 1,000,000 ÷ 294,000 ≈ 3.4). Now in exchanges per second. |
| Weekend Fan-out €90 cap after ~25 min | ledger | 36 agrees (€8,700 ÷ 41 h ≈ €212/h). |

## Per chapter

### part-9-intro
- Ruling 19: "3.4 turns per second", "prices the same turn", "rebuilt Answerdesk turn", "each turn uses up" → exchange(s).
- Trimmed to 898 words (part-intro range 500–900): shortened the three-chapter summary, the "by the end" list, the chapter blurbs and the figure caption; dropped the 1,900-run detail (kept in 36). Spec success criterion updated.

### 35 Latency and Throughput
- **Ruling 19 (main fix, also raised by the coordinator):** the chapter defined "agent turn" as "one cycle from user input to agent response" and used "turn" for exchange about 85 times. Now: an **exchange** (one user message and reply) is made of **turns** (one model call plus its proposed tool calls), both owned by [[agent-runtime]]. Budgets, the requirements table ("exchanges per second"), the code sketch (`run_exchange`, `Exchange`, `ExchangeBudget`), the worked example ("1.6 Mid-tier calls per exchange", "2.1 chat exchanges per second", "3.4 exchanges per second"), failure and trade-off tables and questions all use exchange. Real loop turns kept ("possible extra turns"); "in one turn" for parallel tool calls → "in one response".
- Close-Day Queue containment aligned to the ledger (owning-agentic-systems line): "cutting the Sounding run's concurrency and asking Group Finance to pause" → "stopping the Sounding canary run and asking Group Finance to defer the reclassification, which the controller's office agreed to shortly before 11:30", plus a link to [[owning-agentic-systems]].
- 78% vs 76% cache figure explained (see table above).
- Citation fixes: the workspace-limit quote "to protect other workloads" is not on the page → now quotes "other Workspaces from potential overuse" and "Organization-wide limits always apply". The thinking claim "effort levels, not an off switch, are the control" → "on several current models thinking cannot be turned off, so effort levels are the control (as of October 2026)". Speculative Actions "listed for ICLR 2026" → not on arXiv; now "preprint, 2025, revised 2026" in the text and in Sources.

### 36 Cost, Model Selection and Routing
- Removed the three ⚠ markers in the price-dimension table after re-checking every price (below); header now "as of October 2026", access dates 2026-10-28. Batch row made exact: batch 50% at all three providers, flex at the same price at two (OpenAI, Google); fast/priority 1.8–2×.
- OpenTelemetry: "moved to a new repository in May 2026" not stated on the repository → now "are maintained in a separate GenAI repository".
- Weekend Fan-out replay: "would have terminated on Saturday morning" conflicted with 41 hours ending Monday morning (the run must have started Saturday afternoon) → "within half an hour of starting, on the Saturday".
- Ruling 19: "Each Answerdesk turn ran a Large-tier planning call" → exchange (also the profile A table row, figure 4 label, profile B's "exchanges the classifier marks complex", "11% of exchanges", Across Domains "Per exchange", "In an interactive exchange", "Customer-facing exchanges", the support-platform source note). The loop-arithmetic "turns" are real turns and stay.
- Numbers recomputed; no changes needed. Oversight "about 7 approvals per 1,000 conversations" fits Q3 approvals (~5,060 R1–R3 over ~650,000 conversations ≈ 7.8; ~1,600 proposals/month ≈ 7.4).

### 37 Caching and Context Budgets
- **Budget table contradicted chapter 14** (owner of the segment table): L0 14 tools ~5,400 vs 3,000; L1 3,100 vs 1,800; L2–L3 2,000 vs 1,000. Its rows also summed to 33,000 against a "≤ 24,000" total with no explanation. Replaced with a compact table matching 14 (L0–L3 ≈ 5,800; history trigger 16,000; evidence ≤ 6,000; tool results ≤ 2,500 per result; 24,000 hard limit) and one sentence that the ceilings exceed the total on purpose, linking [[context-engineering]] for the full table. Removed the duplicate "[[context-engineering]] explains how the slots are filled" sentence.
- Repetition: the quadratic-input arithmetic (identical P = 10,000, Δ = 3,000, n = 50 example as in 36) reduced to one clause linking [[agent-cost-and-model-routing]]; the Gemini price-rise paragraph reduced to a clause with the same link.
- Citation fixes: OpenAI `allowed_tools` quote "helps preserve prompt caching" is not on the page → now quotes "so you can maximize savings from prompt caching". Gemini increase "a doubling of input prices for two current models" → "doublings for several current models from 1 December 2026 and 1 January 2027" (input and output, at least Gemini 4 Argon, 3.8 Flash, 3.6 Flash and several TTS/robotics models).
- Removed the ⚠ in the provider snapshot table (every cell re-checked, below); header "as of October 2026".
- Ruling 19: the volatile tail holds "this call's" retrieval (figure 1 and layout table); requirements table "Answerdesk chat exchange", "email exchange"; trade-off table "Interactive exchanges". American spelling: "labelled" → "labeled".

## Sources spot-checked (WebFetch, 2026-10-28)

| URL | Claim | Verdict |
| --- | --- | --- |
| platform.claude.com/docs/en/about-claude/pricing | $0.10–$10 input across current models; cache read 0.1× (0.05×, 0.025× on some); writes 1.25× / 2×; batch 50%; residency premium | Supported |
| platform.claude.com/docs/en/build-with-claude/fast-mode | Same model, faster inference config; OTPS not TTFT; speeds don't share caches; price | Supported; fast price is 2× standard (Opus 5.5 $8 vs $4; Opus 5 $10 vs $5) |
| developers.openai.com/api/docs/pricing | Batch/flex 50%; priority ~2× | Supported; note priority was renamed "Fast" on 30 July 2026, 2× standard |
| ai.google.dev/gemini-api/docs/pricing (updated 2026-10-27) | Batch/flex 50%; priority 1.8×; scheduled doublings 1 Dec 2026 / 1 Jan 2027; cache read 5–10% | Supported (37's "two models, input only" was too narrow; fixed) |
| ai.google.dev/gemini-api/docs/caching (updated 2026-10-23) | Implicit by default; 4,096 min on newest; no explicit caching on Gemini 4 Argon onward | Supported |
| developers.openai.com/api/docs/guides/prompt-caching | Automatic; explicit breakpoints on newest; writes 1.25× (30 min) / 2.5× (12 h); reads 0.1× (0.05×); 1,024 min; no cross-org sharing; key routing and ~15 RPM | Supported |
| developers.openai.com/api/docs/guides/function-calling | `allowed_tools` "helps preserve prompt caching" | Wording not on page; requoted |
| developers.openai.com/api/docs/guides/latency-optimization | 50% output ≈ 50% latency; 50% prompt ≈ 1–5% | Supported verbatim |
| platform.claude.com/docs/en/build-with-claude/prompt-caching | 4 breakpoints / automatic; 512–4,096 min; identical prefix; "no error is returned"; org and workspace isolation; tools→system→messages; TTL order; free refresh | Supported |
| platform.claude.com/docs/en/api/rate-limits | Token bucket; 60 RPM as 1/s; cache-aware ITPM and the 2M/80%/10M example; `enforced_spend_limit_reached` without retry-after; acceleration limits; workspace limits | Supported, except the "to protect other workloads" quote (requoted) |
| platform.claude.com/docs/en/build-with-claude/batch-processing | "most batches completing within 1 hour"; 24 h expiry; expired not billed; 1-hour TTL tip | Supported verbatim |
| platform.claude.com/docs/en/build-with-claude/context-editing | Clearing invalidates cache; `clear_at_least` | Supported |
| code.claude.com/docs/en/costs | Full conversation every request; thinking billed as output, tens of thousands; agent teams ~7× in plan mode; "expected rebuild"; per-user TPM table | Supported; "effort not an off switch" reworded to match |
| code.claude.com/docs/en/agent-sdk/subagents | Depth 3, 20 concurrent, no default spend limit, `max_budget_usd` behavior, "only steers Claude, so set the limits as well" | Supported |
| modelcontextprotocol.io/specification/2026-07-28/changelog | Deterministic `tools/list` order SHOULD | Supported verbatim (minor change 3) |
| github.com/open-telemetry/semantic-conventions-genai (+ gen-ai-metrics.md) | Development status; operation duration, TTFT, time per output token metrics | Supported; "moved in May 2026" not stated (removed in 36) |
| arxiv.org/abs/2502.03771 (vCache) | ICLR 2026; 12.5× hits, 26× lower error; "unexpected error rates" | Supported |
| arxiv.org/abs/2506.14852 (plan caching) | 50.31% cost, 27.28% latency; NeurIPS 2025 | Supported (comments field lists NeurIPS 2025) |
| arxiv.org/abs/2510.04371 (Speculative Actions) | 55% / 20%; "listed for ICLR 2026" | Numbers supported; venue not stated → removed |
| arxiv.org/abs/2510.11977 (HAL) | 21,730 rollouts, 9 models, 9 benchmarks; reasoning effort reduced accuracy in most runs | Supported |
| arxiv.org/abs/2502.07776 (prompt-cache audit) | Global cache sharing at seven providers including OpenAI | Supported |

Every dated price keeps an "as of October 2026" label.

## Rulings check

Ruling 19 applied throughout Part IX (see above). Rulings 4, 5 (unknown outcome via receipt lookup, never re-ask the model), 6 (hash-bound approvals, not re-taught here), 10 (budget exhaustion holds, never drops queued actions), 15 (Bulkhead decides, Toolyard executes) and 21 (one active credit proposal) are stated correctly or not touched. No manifest labels, Forge split, RFC 8693 claims or Closewise daily volumes appear in Part IX. Format: three KEY POINTS, 2–3 named failure patterns, "Across Domains" heading, Questions to ask, hand-offs (35 → 36 → 37 → [[part-10]], with [[versioning-agent-systems]] named as its first chapter, added in this pass; intro → [[agent-latency-and-throughput]]), grouped Sources and the closing disclaimer are all present. No banned words remain.

## Cross-part issues for the editor

1. **Chapter 14 vs 36, input spend per conversation.** 14 (table "Before and after"): "Input spend per conversation at an assumed €2 per million uncached tokens | ≈ €0.39 | ≈ €0.13". 36 (ledger-canonical): "Model spend | €120" per 1,000 conversations, i.e. **€0.12 per conversation in total**, output and Large-tier calls included, for Q3 2027 after the July layout. 14's assumed input-only figure (€0.13) is higher than 36's total. Suggest lowering 14's assumed price to about €0.80 per million uncached tokens (giving ≈ €0.16 → €0.05), or dropping the euro row and keeping the token-equivalents row. 14's €0.39 also reads like 36's €0.39 agent-side cost per *resolved* conversation, a different metric.
2. **Chapter 14 segment table vs 35's ceiling arithmetic.** No conflict, but 35 uses 14,000 input tokens per call and a 78% hit rate, while 14 reports 13,900 and 76% (July). 35 now says why (peak vs monthly average). If the editor prefers one number, changing 35 to 76% would move the ledger's 3.4/s ceiling to ≈ 3.1/s.
3. **Ledger wording for ruling 19.** The `[agent-latency-and-throughput]` ledger line still says "tool-calling chat turns", "≈ 2.1 chat turns/s", "ceiling ≈ 3.4 turns/s"; `[agent-cost-and-model-routing]` says "Large-tier planning call every turn"; `[workflows-loops-and-autonomous-agents]` says "per turn ≤ 6 model steps … 6 s answer deadline" (also an exchange). The chapters now say exchange; the ledger is append-only, so an `[editor]` line may be wanted.
4. **Chapter 06** still has two ⚠ markers in its October 2026 snapshot tables (lines 157 and 176); outside this part.
