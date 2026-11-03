# Review — Part I (FOUNDATIONS)

Reviewer pass, 2026-10-28. Chapters: `part-1-intro`, `01-what-makes-a-system-agentic`, `02-when-agents-are-justified`, `03-autonomy-and-consequence`, `04-workflows-loops-and-autonomous-agents`.

## Word counts (front matter to "Sources and Evidence", tables de-piped, mermaid and code excluded)

| Page | Before | After |
| --- | --- | --- |
| part-1-intro | 904 | 872 |
| 01 what-makes-a-system-agentic | 7,191 | 7,041 |
| 02 when-agents-are-justified | 7,046 | 6,833 |
| 03 autonomy-and-consequence | 7,701 | 7,527 |
| 04 workflows-loops-and-autonomous-agents | 7,076 | 6,971 |

## Rulings and Ostrell numbers checked

The following were already correct in all five pages, so nothing changed: harness meaning (1), exactly-once *effect* wording (4), unknown-outcome state (5, ch04), approval bound to the content hash with expiry and invalidation (6, ch03), kill switches that hold work (10), authorization separate from execution (15, ch01 seams table and ch03 component table).

Rulings 20, 22 and 23 and the Closewise 380/day figure do not come up in Part I. The only Closewise volume Part I uses is 1,900 a month (ch04), which is correct.

Ostrell figures I recomputed, all of which match the ledger: Weekend Fan-out (41 h, 1,900 runs, 310M tokens, €8,700); Double Credit (212 customers, €31,400, 30 s); Half-Posted Accrual (37 of 52, €2.84M); Rubber Stamp (4,812, 99.3%, 6 s, 3.1%); Invoice Chaser (5,800/month, 300×5 replay, 93%, 6, 11, 9 calls; the cost table sums to €205,700 ≈ €206k and €37,700 ≈ €38k); Peoplepoint (2,300/month, 0.987⁷ ≈ 91%, 98.4%, 37 vs 207 corrections); Answerdesk stop-reason mix (41.0/20.5/10.6/1.1/0.8/26.0, so ≈57 budget stops a day); A2 credit sizing (1,470/month, €104 mean, €9,000 / 120 hold; agrees with ch19, ch22, ch34 and ch42); Scout budget €90 / 8M tokens / 90 min (stops at €90 after ~25 min, which matches the ledger's cost-chapter line).

## Per chapter

### part-1-intro
- Was 4 words over the 900-word cap. Trimmed three sentences: 904 → 872.
- spec.md listed the Half-Posted Accrual (37 entries, €2.84M) in its Intent and numbers check, but the intro does not use it. Removed it from the spec. Changelog line added.

### 01 what-makes-a-system-agentic
- **Ruling 19:** in the Answerdesk map's Stop row, "Turn, token and time budgets" became "Step, token and time budgets".
- **Repetition:** cut the TheAgentCompany cost-per-success arithmetic ($4.2 / 30.3% ≈ $14). It now gets one clause and a link to [[when-agents-are-justified]], which owns cost per verified outcome.
- **Repetition:** removed *Moffatt v. Air Canada* (it was cited in ch01, ch02 and ch03) and replaced it with a pointer to [[autonomy-and-consequence]], which cites the tribunal's primary decision. The Law360 source was dropped, and the Incidents group now reads "None specific; Ostrell's incidents are fictional".
- **Evidence:** before, METR's results were "sensitive to modeling choices by a factor of 1.5–2". After, the range is qualified as applying to the newest models, about 1.5× for the 50% horizon and 2× for the 80% horizon, from curve-fitting choices. This is what the March 2026 note says.
- **Wording:** in the Peoplepoint leave flow, "the model held the locus at no decision point" became "the task needed the model at no decision point". The flow was built as a loop, so the old wording contradicted itself.
- The spec still matches the article. Changelog line added.

### 02 when-agents-are-justified
- **Ruling 19:** before, "Latency caps the number of model steps a turn can hold". After, "...an exchange (one user message and the reply) can hold". "Sub-second turns" became "Sub-second responses".
- **Ownership:** the restated Anthropic and Mitchell definitions (owned by ch01) and the "Where the sources disagree" definitions paragraph became one sentence each with a link to [[what-makes-a-system-agentic]].
- **Repetition:** the *Moffatt* paragraph is now two sentences, with a link to ch03.
- **Evidence:** in Kapoor et al. (2024), the "simple retry-style baseline" (93.2%, $2.45) is the paper's **warming** baseline, so it is now named as such. The METR 1.5–2× range is qualified as above.
- Normalized the Anthropic "Building effective agents" URL to `/engineering/`.
- The spec still matches the article. Changelog line added.

### 03 autonomy-and-consequence
- **Ruling 21 (credit limits)** was applied in five places. Before: "one per ticket" / "1 credit per ticket" / "one credit and one revisit per ticket". After: "at most one credit per technician visit (business key: visit id + reason code)" and "one pending credit proposal per ticket" (revisits stay one per ticket, per the ledger). The five places are the per-run blast-radius bullet, the limits paragraph, the code comment, the register table row and the A2 sizing bullet.
- **Ruling 19:** the requirements table now says "within the step's budget", "outside the conversational exchange" and "within the exchange for credits" (each was "turn" before).
- **Ownership and repetition:** cut the duration paragraph's METR 4–6× quote and Ord's half-life, with a link to ch02, which owns compounding and the horizon evidence. Dropped those two entries from Sources. The TheAgentCompany renamed-user story is now one clause with a link to ch02.
- **Citation fix:** before, the DataTalks.Club incident said "afterwards, the agent ran no destructive Terraform commands". The Tom's Hardware report says Grigorev **stopped letting the agent run Terraform commands** and reviews plans himself, so it now says that.
- The spec still matches the article (Success criteria refer to ch34's numbers, which agree). Changelog line added.

### 04 workflows-loops-and-autonomous-agents
- **Ruling 19:** Answerdesk's limits said "Per customer turn: ≤ 6 model steps, 4 tool calls, 6 s deadline… the turn continues". They now say "Per exchange (one customer message and Answerdesk's reply)… the exchange continues". The budget table's step and time budgets are now "per exchange and per run" (they were "per turn"). The requirements table now says "exchange deadline". "A turn cap here" became "a step cap here".
- **Evidence:** Cemri et al. (MAST) changed from "NeurIPS 2025 Datasets and Benchmarks" to "preprint". Neither the arXiv page nor the paper text names the venue. The percentages check out against the paper (15.7%, 12.4%, 9.1 + 8.2 + 6.2 = 23.5%). The METR caveat is qualified as above. Anthropic's "99.9th-percentile turn duration" is glossed as Anthropic's measure, so readers do not confuse it with the book's turn.
- The closing hand-off to [[part-2]] / [[agentic-reference-architecture]] is present.
- The spec still matches the article. Changelog line added.

## Sources spot-checked (WebFetch, 2026-10-28)

| URL | Chapter(s) | Verdict |
| --- | --- | --- |
| modelcontextprotocol.io/specification/2026-07-28/server/tools | 01 | **Supported.** "model-controlled"; "SHOULD always be a human in the loop with the ability to deny tool invocations"; servers MUST validate inputs and implement access controls. |
| anthropic.com/research/measuring-agent-autonomy | 01, 03, 04 | **Supported.** Published 2026-02-18; 998,481 calls; 0.8% irreversible; 87% vs 67% human involvement; 99.9th-percentile turn <25 → >45 min; auto-approve ~20% → >40%; caveats as stated. |
| metr.org/time-horizons/ | 01, 02, 04 | **Supported.** Updated 2026-09-08, "no longer actively updated", "Measurements above 16 hrs are unreliable". |
| metr.org/notes/2026-03-20-… | 02 (and the wording in 01, 04) | **Partly.** The ~1.5× (50%) and 2× (80%) range applies to the newest model and to curve-fit choices; other models are affected less. Wording qualified. |
| arxiv.org/html/2412.14161 (TheAgentCompany v3, 2025-09-10) | 01–04 | **Supported.** Gemini 2.5 Pro: 30.3%, 27.2 steps, $4.2, 175 tasks; the renamed-user passage. |
| arxiv.org/html/2406.12045 (τ-bench) | 01, 02, 04 | **Supported.** Retail pass^1 61.2, pass^8 < 25%; airline without policy 33.2 → 10.8. |
| thinkingmachines.ai/…defeating-nondeterminism… | 01 | **Supported.** 1,000 runs at temperature 0, 80 unique completions (Qwen3-235B), 2025-09-10. |
| arxiv.org/html/2407.01502 (AI Agents That Matter) | 02 | **Supported, wording sharpened.** LATS 88.0% at $134.50; warming 93.2% at $2.45; five runs; "almost two orders of magnitude". |
| arxiv.org/abs/2510.11977 (HAL) | 02 | **Supported.** 21,730 rollouts, 9 models, 9 benchmarks; agents searching HuggingFace for the benchmark. |
| fortune.com/2025/05/09/klarna-… | 02 | **Supported.** "too predominant evaluation factor"; "lower quality"; 2025-05-09 (remarks made to Bloomberg). |
| anthropic.com/engineering/claude-code-auto-mode | 03 | **Supported.** 2026-03-25; "users accept 93% of them". |
| tech.yahoo.com/…claude-code-deletes… (Tom's Hardware) | 03 | **Partly.** The facts check out (Grigorev, Terraform destroy, two sites, snapshots, restored in about a day). The aftermath was misstated and is corrected. |
| euronews.com/…2026/04/28/… + neuraltrust.ai/blog/pocketos-railway-agent | 03 | **Supported.** Euronews gives the 30-plus-hour outage. NeuralTrust gives the single Railway API call, the volume-level backups and the broadly scoped token found in an unrelated file. The chapter already credits the detail to the founder's account as relayed. |
| ai.meta.com/blog/practical-ai-agent-security/ | 03 | **Supported.** 2025-10-31; Rule of Two as stated. |
| stripe.dev/blog/minions-… | 04 | **Supported.** 2026-02-09, Alistair Gray; "interleave agent loops and deterministic code"; "at most two rounds of CI"; "over a thousand pull requests merged each week". |
| code.claude.com/docs/en/agent-sdk/subagents | 04 | **Supported.** Default depth 3 and concurrency 20; spend: "No limit" unless `max_budget_usd`. |
| openai.github.io/openai-agents-python/running_agents/ | 04 | **Supported.** `MaxTurnsExceeded`; "Pass `max_turns=None` to disable this turn limit". |
| docs.langchain.com/oss/python/langgraph/checkpointers | 04 | **Supported.** "Nodes after the checkpoint re-execute, including any LLM calls…". |
| arxiv.org/abs/2503.13657 + html (MAST) | 04 | **Numbers supported; venue not verified.** Relabeled as a preprint. |

The Google "Agents" whitepaper (ch01) is already labeled as reported from a secondary summary and not checked against the original. Left as is.

## Verification

- `python3 _wiring/build.py`: `[built] agentic-systems-architecture`. The only warnings are for book pages not yet written (introduction, where-agentic-systems-go-wrong, part-11-intro, source-coverage, glossary).
- `render_check.py part-1 what-makes-a-system-agentic when-agents-are-justified autonomy-and-consequence workflows-loops-and-autonomous-agents`: all OK, 0 mermaid failures, 0 unresolved links.

## Cross-part issues for the editor

1. **Ledger line `[workflows-loops-and-autonomous-agents]` (Answerdesk loop limits)** says "per turn ≤ 6 model steps and ≤ 4 tool calls, 6 s answer deadline". Under ruling 19 this is **per exchange**. Ch04 is now aligned. The ledger line itself was left untouched (append-only); an `[editor]` line may be needed.
2. **Ch35 agent-latency-and-throughput** (Part IX) uses "turn" for an exchange: "Per turn after the redesign: **1.6 Mid-tier calls** on average… about 350 output tokens per turn", "≈ 3.4 turns per second", "steps per turn", "share of turns ending in the deadline fallback". A turn with 1.6 model calls contradicts ruling 19 (one model call per turn). Ch04 cites ch35 for the ≤ 6 s Answerdesk deadline, which ch04 now calls the exchange deadline.
3. ***Moffatt v. Air Canada*** was cited in full in ch01, ch02 and ch03. It is now owned by ch03, which cites the primary decision; ch01 and ch02 only point to it. Later parts (for example domain-customer-operations) should also link rather than retell it.
