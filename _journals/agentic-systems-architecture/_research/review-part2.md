# Review — Part II (ARCHITECTURE)

Reviewer pass, 2026-10-28. Scope: `part-2-intro`, `05-agentic-reference-architecture`, `06-models-and-the-model-gateway`, `07-agent-runtime`, `08-agents-in-the-enterprise`, `09-agent-interaction-design`. Every changed article got a `revised: 2026-10-28` spec and a Changelog line. Build passes. `render_check.py` on all six permalinks: 0 problems, 14 mermaid blocks, 0 unresolved links.

## Word counts (front matter to "Sources and Evidence", without tables' pipes, code or mermaid)

| Page | Before | After |
| --- | --- | --- |
| part-2-intro | 884 | 893 |
| 05 | 6,625 | 6,626 |
| 06 | 7,051 | 7,070 |
| 07 | 7,269 | ~7,290 |
| 08 | 7,252 | 7,257 |
| 09 | 7,078 | 7,092 |

Every page is under the 8,000 cap, so I made no length cuts.

## Rulings checked across the part

- **19, turn vs exchange.** 07 owns the terms and uses them correctly. 06, 08 and 09 used "turn" where they meant an exchange; I fixed every case (see below).
- **20, Forge split.** 07 follows it: a Runtime workflow, the inner loop runs in the microVM as one leased activity, and model calls leave through the egress proxy. Note: ledger line `[agent-runtime]` still says "Forge's loop runs in Keelson Runtime outside the sandbox". The ledger line is stale; the chapter follows the ruling.
- **21, credit limits.** 09 says "one active credit proposal per ticket", which matches the ruling. No chapter says "one credit per ticket".
- **22, `sub`/`act`.** 08 puts the verified customer as subject and the agent as actor, which matches.
- **4, 5, 6 and 15.** All consistent: exactly-once effect wording, `unknown` leading to lookup and then a repair queue, approvals bound to a content hash with expiry, and Bulkhead deciding while Toolyard executes.
- **1, harness.** 05 and 07 use the one meaning.
- **23 and Closewise 380/day.** Neither appears in Part II.

## Per chapter

### part-2-intro
- **Before:** "In February auditors found **40** ERP entries with no approver on record". **After:** "sampled **40** ERP entries posted by an integration account whose approvals the ERP could not show". The ledger says 40 were sampled: approval evidence for 9 was a chat message and for 2 it was missing.
- **Before:** "In June a correction four seconds late sent a technician to the wrong site, one of 23". **After:** "In May and June … in **23** conversations". The ledger dates the 23 to May–June.

### 05 — hub check against owning chapters
I compared the responsibilities table and the requirements table with chapters 07, 14, 16, 20, 24, 26, 30 and 33 (architecture sections and ledger entries).
- **Idempotency key.** Before: "derived … from the run id and step number". After: "minted … from the agent id, run id and action object id". Source: the 24 ledger entry.
- **Bulkhead decision latency.** Before: "p99 under 10 ms *(assumption)*". After: "p99 ≤ 5 ms from a cached bundle *(assumption)*". Source: 30, PEP table.
- **Bulkhead row.** Added the on-output PEP (30 defines four PEPs).
- **Tidemark row.** "confidence" became "trust level". 16 replaced model-rated confidence with trust levels in schema v3.
- **Link fix.** The independent Toolyard limit enforcement now links to [[autonomy-and-consequence]], which owns it in the ledger, instead of [[evidence-for-autonomy]].
- **Furr quote.** I removed "everything that had been working before continues to work" because it is not on the fetched page. The other two quotes were verified.
- **Agreed without change:** Runtime records and does not execute (07). Context assembler inside Runtime (14). Retrieval through Toolyard tools (15). Gateway rows (06). Toolyard: brokered credentials, `unknown` and revocation (20, 24). Execution environment (21). Task record (17). Logbook (30). Wake (33). Static-stability table (consistent with the 05 ledger entry and 30's fail-closed rules).

### 06
- **Turn vs exchange.** "One Answerdesk turn can include a classifier call, a planner call and a worker call" became "exchange". "Fallback response on 4.8% of turns" became "4.8% of chat exchanges". "Interactive turn" became "interactive exchange".
- **Price spread.** Before: "roughly 40×". After: "roughly 100× per input token". The models overview lists the smallest model from $0.10 and the largest at $10 per input MTok.
- **OpenAI deprecation.** Before: "June 2026 notice … 'Move prompts into app code'". After: "3 June 2026 notice that hosted reusable prompts shut down on 30 November 2026 … 'move reusable prompt content into your application code'" (the exact text).

### 07
- **Idempotency key wording** aligned with 24 (agent id, run id, action object id, covering the version).
- **MCP annotation quote.** Before: the annotations are "hints" and clients "should never make tool use decisions…". Neither phrase is on the 2026-07-28 tools page. After: the verified text, "clients MUST consider tool annotations to be untrusted unless they come from trusted servers".
- **Uncited source removed.** The Thinking Machines entry was listed in Sources but cited nowhere in the body.
- **Answerdesk limits.** 04 gives April 2027 limits (6 model calls per exchange, €1.00 per conversation); 07 gives the November 2027 profile (8 turns per exchange, €1.20 per run). I added a clause stating the November profile widened the April limits, with a link to 04.

### 08
- **Turn vs exchange.** "Before the conversation turn ends" became "before the agent's reply is sent". "Turn-latency budget" became "per-exchange latency budget".
- **Escalations per day.** Before: "about **2,340** a day (7,100 × 0.33)". After: "about **2,300** a day", matching the 13 ledger entry (~2,300/day).
- **Peoplepoint.** Before: "probably not an Annex III use". After: "Ostrell's documented assessment treats Peoplepoint's helpdesk as not high-risk", matching the 30 ledger entry (the Art. 6(3) assessment) and the 29 ledger entry.
- **Entra Agent ID link.** Updated to the page it redirects to, `what-are-agent-identities`. Content and the 2026-06-15 update date were verified.

### 09
- **Turn vs exchange (ruling 19).** Changed in the mode table, "who waits", "where can a gate sit", the requirements table, the trade-off table, the domain table, and "the customer always gets a reply".
- **Escalations and savings.** 2,340 became 2,300 a day. The recomputed savings went from 7,700 min (128 h) to 7,600 min (126 h).
- **Pending-action example.** Before: "Credit of €180 — awaiting approval". After: "€320". After October 2027 a €180 credit is A2 and would not wait for approval.
- **Internal reference removed from published prose.** "(consistency ruling 6: …)" became "because approvals bind to the action's content hash".
- **Moffatt award.** Now reads CA$812.02 in total, of which CA$650.88 was damages, with the rest interest and fees.

## Sources spot-checked

| URL | Chapter | Verdict |
| --- | --- | --- |
| modelcontextprotocol.io/specification/2026-07-28/server/tools | 05, 07 | The revision exists. Tool execution errors are returned with `isError` for self-correction (supported). Annotations are "untrusted unless they come from trusted servers"; the "hints" wording is not on this page, so I fixed the quote in 07. |
| docs.aws.amazon.com/bedrock-agentcore/…/what-is-bedrock-agentcore.html | 05 | Supported. All 13 services named; "together or independently"; Policy intercepts every tool call via Gateway. |
| builder.aws.com/…/static-stability-using-availability-zones | 05 | Furr, 2019. Two quotes verified; the third was not found and is removed. |
| docs.aws.amazon.com/whitepapers/…/control-planes-and-data-planes.html | 05 | Supported (all three quotes). |
| platform.claude.com/…/model-deprecations | 06 | Supported: 60-day notice, and `temperature`/`top_p`/`top_k` removed in API version 2026-10-21 (400 error). |
| platform.claude.com/…/models/overview | 06 | "Every Claude model ID is a pinned snapshot" is supported. The 40× spread was **wrong** (about 100×) and is fixed. |
| platform.claude.com/…/api-and-data-retention | 06 | Supported: no training without permission, Covered Models need 30-day retention, batch 29 days, flagged content up to 2 years. |
| developers.openai.com/api/docs/deprecations | 06 | Date and quote were slightly wrong; fixed. |
| developers.openai.com/api/docs/guides/your-data | 06 | Supported: 1 March 2023, 30 days, ZDR-ineligible features, US/EU/UAE processing, 10% uplift from 5 March 2026. |
| code.claude.com/docs/en/agent-sdk/agent-loop | 07 | Supported: turn definition, "No limit" defaults, overshoot by one response, `readOnlyHint`, queued message stays queued. |
| code.claude.com/docs/en/agent-sdk/subagents | 07 | Supported: depth 3, 20 concurrent, spend "No limit". |
| devblogs.microsoft.com/agent-framework/…-1-0/ | 07 | Supported: 3 April 2026, version 1.0. |
| anthropic.com/research/measuring-agent-autonomy | 07, 09 | Supported: 18 Feb 2026; 5% vs 9% interrupts; 20% vs >40% auto-approve; production and evaluation traffic not distinguished. |
| publications.europa.eu/resource/celex/32026R1744 | 08, 09 | Partly checked: it amends 2024/1689 including Art. 113, published 24 July 2026, in force 27 July. Only metadata was readable; the 2 December 2027 Annex III date rests on the regulation brief's verified quote of amended Art. 113. Kept. |
| learn.microsoft.com/…/agent-id (redirected) | 08 | Supported: delegated access, one-to-one agent user accounts, updated 2026-06-15. Link updated. |
| arxiv.org/abs/2411.07763 | 08 | Supported: 21.3%, 91.2%, 73.0%, 632 tasks. |
| modelcontextprotocol.io/specification/2026-07-28/basic/authorization | 08 | Supported: audience validation; "MUST NOT accept or transit any other tokens". |
| anthropic.com/engineering/claude-code-auto-mode | 09 | Supported: 25 March 2026; "users accept 93%". |
| docs.github.com/…/about-coding-agent | 09 | Supported: 59 minutes, steering by chat, one PR per task. |
| arxiv.org/html/2507.22358 | 09 | Supported: 162 tasks, 30.3% to 51.9%, about 10% help requests, 12 participants, three-way action guards. |
| decisions.civilresolutionbc.ca/…/525448 | 09 | Returned HTTP 403, so not fetched. The MLT Aikins summary confirms 2024 BCCRT 149 and CA$650.88 damages. The CA$812.02 total and the quotes are widely reported; kept. |

## Cross-part issues for the editor

1. **Data classes and route eligibility: 06 (Part II) vs 26 (Part VII).**
   - **06** (ledger `[models-and-the-model-gateway]`) dates data-class routing to March 2027, with classes `legal_privileged` (0 days), `customer_personal`, `finance_confidential` and `source_code` (30 days). Its route table gives `customer_personal` "All EU synchronous routes", including `b-mid-eu` (30-day retention). On 19 October 2027, ~11,400 Answerdesk calls failed over to `b-mid-eu`.
   - **26** says the June 2027 review "produced a routing rule in Keelson Gateway that did not exist before". It also says: "**D1 Internal** … Approved endpoints under zero-retention terms", "**D2 Customer confidential** … Endpoints under zero-retention terms with regional processing", "**D3 Personal** … As D2".
   - **The conflict:** under 26, Answerdesk (D3) could not fail over to a 30-day route, and the rule's origin date and vocabulary also differ. Recommendation: in 26, present D0–DS as the June 2027 refinement of 06's March 2027 classes (a mapping table). Then either relax D1–D3 to "no training, ≤ 30-day retention, EU processing", or state that provider B's synchronous routes moved to zero retention after June. That second option would require changing 06's October outage narrative.
2. **Ledger hygiene (no chapter conflict):**
   - `[agent-runtime]` still says the Forge loop runs outside the sandbox, which contradicts ruling 20.
   - `[partial-failure-and-compensation]` says the Fixture Purge was "flagged Thu 22 July 2027". Chapters 25 and 41 both say Friday 16 July, so the ledger line should be corrected.
3. **Turn wording in 04 (Part I).** It already uses "per exchange" correctly. No change needed; noted only because 07 now cross-references its April 2027 limits.
