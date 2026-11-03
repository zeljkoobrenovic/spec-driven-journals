# Review — Part V (TOOLS), 2026-10-28

Scope: `posts/part-5-intro`, `19-tool-contracts`, `20-tool-ecosystems-and-mcp`, `21-sandboxes-and-execution-environments`, `22-side-effects-and-external-actions`.

Word counts are prose and tables from the start of the file to "Sources and Evidence". Mermaid and code fences and table pipes are excluded. Front matter is included, which is the stricter count.

| Page | Before | After |
| --- | --- | --- |
| part-5-intro | 989 (body ≈ 920) | 950 (body ≈ 880) |
| 19 tool-contracts | 6,919 | 6,942 |
| 20 tool-ecosystems-and-mcp | 7,217 | 7,230 |
| 21 sandboxes-and-execution-environments | 8,022 | 7,876 |
| 22 side-effects-and-external-actions | 7,130 | 7,207 |

These counts are not strictly comparable. The "before" column came from the first run of the counting script. During the session the shared scratchpad script was changed (it now drops front matter and punctuation-only tokens), so the "after" column was re-measured with the brief's stricter method. Every chapter is under 8,000 on both methods.

## Rulings checked across the part

| Ruling | Result |
| --- | --- |
| 1 harness | OK |
| 4 exactly-once effect | OK |
| 5 unknown state | OK |
| 6 approval model | OK. Ch22 expiry was fixed (see below). |
| 15 authorization vs execution | Stated in ch20 and ch22. |
| 19 turn vs exchange | Fixed in 19 and 22. |
| 20 Forge split | Ch21 already follows it. |
| 21 credit limits | Fixed in ch22. |
| 22 RFC 8693 | Not used in Part V. |
| 23 manifest label | Ch22 action object now uses `ad-2027.10.2`. |
| Closewise 380/day | Not used. Ch22 uses 1,900 a month, which is consistent. |
| 25 approval expiry 4 h | Applied in ch22. |

## part-5-intro

- "twenty-hour approval wait" → "an overnight approval wait", to match the 4-hour approval expiry (ruling 25).
- Lead paragraph and the questions paragraph trimmed toward the spec's 500–900 words.
- No external citations, so none to spot-check.

## 19 tool-contracts

- Ruling 19: the requirements table said "inside the conversation turn". Changed to "exchange".
- Cross-chapter number conflict with ch22. The Q3 table cell said replies claiming a credit without `issued` were "0 delivered". Ch22 (which owns the Promised Credit) reports **2 premature statements** in the September 2027 500-conversation audit. Before: "0 delivered; the reply check blocked 3 drafts". After: "blocked 3 drafts; September audit found 2 premature statements and no customer told of a credit that did not happen".
- Citation fix: TheAgentCompany does not use the term "self-deception". The paper's §7.3 heading is "Deceiving oneself". Wording corrected.

Sources spot-checked:

| Source | Verdict |
| --- | --- |
| MCP Tools 2026-07-28 | Supported: server MUST validate inputs, etc.; annotations untrusted unless from trusted servers; outputSchema MUST/SHOULD; execution-error quote. |
| Anthropic structured outputs | Supported: no min/max/multipleOf, minLength/maxLength or recursive schemas; refusal, max_tokens and enum-capitalization quotes. |
| OpenAI function-calling guide | Supported: "Offload the burden…", "Combine functions…", strict mode, fewer than 20 functions. |
| arXiv 2412.14161 (TheAgentCompany) | Renaming incident supported (v3 dated 10 Sep 2025). The label "self-deception" was not supported and was fixed. |

## 20 tool-ecosystems-and-mcp

- Factual fix. Before: "four backward-incompatible revisions in twenty months (2025-03-26 to 2026-07-28)". That range is 16 months, and incompatibility was not verified for each revision. After: "four revisions in the twenty months after its first (2024-11-05); the latest, 2026-07-28, removed sessions and the handshake."
- The fold-back is now dated 7 June 2027 (`[editor]` line).

Sources spot-checked:

| Source | Verdict |
| --- | --- |
| MCP 2026-07-28 changelog | Supported: stateless, initialize removed, handles, "a broken response stream loses the in-flight request…", deterministic ordering, deprecations of Roots, Sampling, Logging and DCR. |
| MCP feature lifecycle | Supported: 12-month floor, 90 days for an active security risk. |
| MCP Registry about | Supported: preview, metadata only, GitHub/DNS/HTTP namespace checks, delegated scanning, no private servers, not for direct host consumption. |
| Linux Foundation AAIF | Supported: 9 Dec 2025, MCP a founding project. |
| AWS AgentCore Policy docs | Supported: Cedar, "before allowing tool access". GA 3 March 2026 confirmed via the AWS What's New listing. |
| Anthropic advanced tool use | Supported: 2025-11-24; 58 tools ≈ 55K tokens; 77K → 8.7K; 49→74% and 79.5→88.1%. |

## 21 sandboxes-and-execution-environments

- Length: 8,022 → 7,876. The cuts:
  - shortened the lead;
  - removed the Modal and code-execution lifetime figures;
  - removed the TechCrunch quote of OpenAI's position (trade press, primary not fetched);
  - shortened the convergence paragraph;
  - removed the ai-coding-cli audit-gap aside;
  - tightened the Silent Fallback review paragraph.
- The Modal and TechCrunch source entries were removed because nothing cites them any more.
- The code-execution "30-day container" claim was not verified. It is now worded as "multi-day".
- Typo fixed: ")).," in the browser paragraph.
- Ruling 20 (Forge split) was already followed.

Sources spot-checked:

| Source | Verdict |
| --- | --- |
| arXiv 2604.04978 (Ji et al.) | Supported. The v3 date of 22 Oct 2026 was confirmed, along with 81.0% (CI 73.8–87.4), 70.3%, 31.9%, 128 prompts, 253 actions and 36.8%. |
| Anthropic auto mode (2026-03-25) | Supported: 93% acceptance; 0.4% / 17% / 5.7% with n = 10,000 / 52 / 1,000; "not a drop-in replacement" quote. |
| Codex docs at learn.chatgpt.com/docs/sandboxing | Supported: the quote, the mode names and `auto_review`. |
| NVD CVE-2025-59532 | Supported: Codex CLI treated a model-generated cwd as the writable root. |
| Claude Code sandboxing docs | Every quoted item supported, including the Limitations section: "not a complete isolation boundary", the github.com/domain-fronting warning, docker.sock, "considerably weakens security", computer use "on your actual desktop". |

## 22 side-effects-and-external-actions

- **Approval expiry (ruling 25 / ch29).** Before: "approves after 20 hours, close to the approval's 24-hour expiry (local rule)". After: the €420 request is an R2 card; nobody picks it up within 4 working hours, so it moves to the billing desk queue, where a specialist approves it the next morning. The sequence-diagram participant was renamed TeamLead → Approver. The reply text says "our billing team".
- **A2 sampling.** Before: "one in twenty (5%)". After: "a 10% sample". This follows the ledger human-oversight line on the post-October 2027 A2 promotion.
- **Ruling 21.** Before: "One goodwill credit per visit". After: "At most one service credit per technician visit (business key: visit + reason code); at most one active credit proposal per ticket". The validation step now also checks that there is no other active proposal.
- **Within-part consistency with the ch19 contract.**
  - Identifiers `T-8810233` / `V-5521907` → `TCK-08810233` / `VIS-05521907`.
  - Reason `TECH_NO_SHOW` → `missed_visit`. The model proposes no amount; €180 is the contract policy amount.
  - The €420 case is now `goodwill_other` on the last visit.
- **Ruling 23.** The agent ref is now `answerdesk@ad-2027.10.2`. The credit policy version "2027.10.2", which looked like a manifest label, is now `credits-v12`.
- **Ruling 19.** "Within the conversation turn" → "exchange".
- **Euronews/PocketOS.** The article does not report "one API call", "volume-level backups" or "an over-scoped token found in the repository". It does report that the data was recovered after an outage of more than 30 hours. The claim was rewritten to match, and "irreversible" became "destructive". The source annotation was updated.
- The "## Next" heading was removed so the hand-off paragraph matches the other chapters. "twenty-hour" → "overnight".

Sources spot-checked:

| Source | Verdict |
| --- | --- |
| Euronews 2026-04-28 | Partly supported. Fixed as described above. |
| Tom's Hardware via Yahoo 2026-03-07 | Supported: Terraform destroy wiped DataTalks.Club and AI Shipping Labs infrastructure, the database and snapshots (AWS restored within about a day). |
| Meta Agents Rule of Two | Supported: 2025-10-31; three properties; supervision when all three are needed. |
| Anthropic auto mode | Supported: 93%. |
| MCP Tools 2026-07-28 | Supported: annotations untrusted. |

## Specs

Each of the five specs has `revised: 2026-10-28` and a review-pass Changelog line. No Success criteria or Non-goals needed to change.

## Verify

- The build printed `[built] agentic-systems-architecture`. The missing-post warnings are for introduction, where-agentic-systems-go-wrong, source-coverage and glossary, which are not in this part.
- `render_check.py` passed on all five pages: 0 mermaid failures and 0 unresolved links.

## Cross-part issues for the editor

1. **Ledger line `[agent-runtime]` contradicts ruling 20.** It says "Forge's loop runs in Keelson Runtime outside the sandbox …; only its tool calls execute in the microVM". The ch07 article itself (line ~245) already follows ruling 20 ("the inner coding loop runs *inside* a per-run microVM as one leased, heartbeated activity"). Only the ledger line is stale.
2. **Ledger line `[side-effects-and-external-actions]` is now stale.** It says "Answerdesk A1 credit approvals expire after **24 h** *(local rule)*". Ch22 now follows ch29 and ruling 25: R1/R2 requests expire after 4 working hours to the billing desk queue, and an approval is valid 4 hours. I did not edit the ledger (append-only).
3. **Second-reviewer sampling after the A2 promotion.** The Rubber Stamp canonical example (ledger item 9) says the "5% random sample" from Q3 2027. The `[human-oversight-and-bounded-autonomy]` ledger line says it is **10%** after October 2027. Ch22 now uses 10% for November 2027. Other chapters that say 5% for post-October A2 sampling should be checked.
4. **`[staged-rollout-and-rollback]` ledger line** labels the Closewise candidate `2027.10.2` / `2027.12.1` / `2027.09.3` without the `cw-` prefix that ruling 23 requires. This is Part X and was not edited.
5. **Promised Credit, ch42.** `42-domain-customer-operations/index.md:310` dates it "(May 2027)". Ch22 has April–May 2027 for the period, with discovery in May, so this is consistent. No action needed unless ch42 cites the "0 delivered" figure.
