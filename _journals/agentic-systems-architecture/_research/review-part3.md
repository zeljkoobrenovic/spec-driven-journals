# Review — Part III (ORCHESTRATION)

Reviewer pass, 2026-10-28. I read the style guide, consistency rulings 1–23, the full scenario ledger (with every addition and `[editor]` line), all five Part III pages (index.md and spec.md), and the Lost Handoff, router and Scout passages in other parts' chapters (01, 04, 05, 09, 14, 17, 19, 20, 35, 36, 40, 42, meet-ostrell, part-4-intro).

Word counts cover prose and tables from the front matter to "Sources and Evidence", without mermaid, code or table pipes.

| Page | Before | After |
| --- | --- | --- |
| part-3 intro | 904 | 904 |
| planning-and-decomposition | 7,018 | 7,023 |
| routing-and-delegation | 7,121 | 7,140 |
| single-and-multi-agent-designs | 7,064 | 7,090 |
| coordination-and-handoffs | 6,918 | 6,989 |

Every page is under the 8,000-word cap, so I made no length cuts. Ownership is clean. Each chapter retells another chapter's incident (the Weekend Fan-out, the Lost Handoff, the fold-back) in one or two sentences and links to the owner. Ch12's fold-back paragraph is short and defers to ch13.

## part-3 (intro)

- No changes needed. Its numbers agree with the ledger and the chapters: 1,900 runs, €8,700 and 41 h; 17 worker runs and about €57; 1 in 40; 3 credits; about 25,000 handoffs; 0.81 vs 0.64; 64 of 143; recall 71% → 97%.
- Its format matches the part-intro rules. It hands off to [[part-4]], then lists the chapters and ends with "Begin with [[planning-and-decomposition]]".

## 10 planning-and-decomposition

**Issues and fixes**
- A quote from Anthropic's long-running-harness post did not match the source.
  - Before: models were "less likely to inappropriately alter" it.
  - After: "the model is less likely to inappropriately change or overwrite JSON files".
- No number changed. The Scout re-run matches the ledger: plan v1 → v3, 17 worker runs, about 2.0M tokens, about €57, 52 min, 13 markets plus 1 abstention. The approval thresholds (€25, 8 sub-questions, 3 replans, 20%) also match.
- MAST "incorrect or missing verification ≈ 17%" is correct (8.2% + 9.1%).

**Citations spot-checked**
- arxiv.org/abs/2512.08296 (Kim et al.) → supported. It is v3 of 8 Apr 2026, with 260 configurations, six benchmarks, +80.8% and −70.0%.
- research.google/blog/towards-a-science-of-scaling-agent-systems… → supported. The post is from 28 Jan 2026, with 180 configurations, 17.2× vs 4.4×, and 39–70% on sequential tasks.
- arxiv.org/html/2409.13373 (Valmeekam 2024) → supported. Every number checks: 97.8%, 62.6%, 52.8%, 23.6%, 27%, $42.12 per 100, Fast Downward 0.265 s.
- code.claude.com/docs/en/common-workflows → supported. The plan-mode quote is exact.
- anthropic.com/engineering/effective-harnesses-for-long-running-agents → partly supported. The post is from 26 Nov 2025 and mentions 200+ features, one-shotting and premature victory. The quote wording was wrong and is fixed.
- arxiv.org/html/2503.13657 (MAST) → supported. The per-mode percentages match.
- Interview designs (local JSON) → supported. These quotes were found: "a known pipeline with LLM calls", "bounded nodes", "smuggle past prose", the public-benefits "Deterministic DAG: gather evidence -> apply rules -> explain -> caseworker decision" and "Scale fidelity to blast radius".

## 11 routing-and-delegation

**Issues and fixes**
- Ruling 19 (turn vs exchange), three places:
  - "every Answerdesk turn made a Large-tier planning call and a Mid-tier answer call" became "every Answerdesk exchange (one customer message and the reply) …". Two model calls cannot be one turn.
  - "turns marked complex" became "exchanges marked complex".
  - "inside a turn latency budget" became "inside a per-exchange latency budget".
- Ruling 22: the RFC 8693 sentence now names `sub` as the principal served, next to the nested `act`.
- The Cognition 2026 quote "not knowing when to escalate" is not on the page. It is now a paraphrase: a weaker primary model did not know when to escalate.
- Banned word "unlock" appeared twice and became "grants".
- No numbers changed. The router figures match the ledger: 11 routes, v2 shipped on 2027-09-20, and the stages handle 9%, 79%, 12% and 1.9% (about 135 a day) of traffic. The audit used 2,400 conversations: 91.2% top-1 accuracy, 71% `service_incident` recall, and confidence of at least 0.9 on 94% of conversations and on 83% of misroutes. The v2 results were 93.8% top-1, recall of 97% and 99%, and a bounce rate falling from 6.4% to 3.1%. Re-routes are capped at 2.

**Citations spot-checked**
- code.claude.com/docs/en/agent-sdk/subagents → supported. The defaults are depth 3, 20 concurrent subagents and no spend limit. The page says "The only content you pass from parent to subagent is the Agent tool's prompt string" and that instructions "only steer".
- anthropic.com/engineering/a-postmortem-of-three-recent-issues → supported. The post is from 17 Sep 2025: 16% of Sonnet 4 requests in the worst hour, sticky routing, about 30% of Claude Code users affected, and the evaluations did not catch it.
- arxiv.org/html/2407.01502 (Kapoor) → supported. Escalation cost $0.27 at 85.0%, against warming with GPT-4 at $2.45 and 93.2%.
- platform.claude.com/…/tool-search-tool → supported. It states "degrades once you exceed 30–50 available tools".
- cognition.com/blog/multi-agents-working → supported once the quote is fixed. The post is dated 22 Apr 2026.
- Interview designs → supported. These quotes were found: "can lower autonomy but never raise", "mint a scoped token while a handoff", "never auto-authorized", "poorly calibrated and gameable".

## 12 single-and-multi-agent-designs

**Issues and fixes**
- The writer's ⚠ verification markers came out in three places once the SDK page confirmed the claims.
  - The output-scanning sentence now says what the scan does: it neutralizes imitated control tags and turn markers and removes no text.
- MAST mode names were wrong.
  - Before: "incorrect, missing or premature verification".
  - After: "premature termination, no or incomplete verification, incorrect verification". The 23.5% figure is correct.
- Scout workers did not match the ledger's threat model. The ledger says that since July 2027 a worker uses web or internal sources, never both. "Read-only web and internal search" became "web or internal sources, never both in one worker since July 2027", linked to [[agent-threat-model]].
- Ruling 19 (turn vs exchange): "no fan-out on the live turn" became "inside a live exchange", and "Supervisor tokens every turn" became "on every exchange".
- An opening sentence had a double space and a dangling "It"; I joined it to the sentence before.
- The Sources group headings were bold text. They are now `###`, matching the other chapters.
- No numbers changed. The Scout suite matches the ledger: 160 tasks, scores 0.64 → 0.81 at 2.4× tokens and 31 → 16 min, and 0.80 vs 0.78 at 2.9× tokens. The cost table's arithmetic checks out: 3.9M tokens for €21.20.

**Citations spot-checked**
- code.claude.com/docs/en/agent-sdk/subagents → supported. It confirms `parent_tool_use_id`, the output scan (Claude Code v2.1.210+), the default caps and "set the limits as well".
- anthropic.com/engineering/eval-awareness-browsecomp → supported. The post is from 6 Mar 2026: 0.87% multi-agent vs 0.24% single-agent.
- docs.langchain.com/oss/python/langchain/multi-agent → supported. Subagents: 5 calls and about 9K tokens. Handoffs: 7+ calls and 14K+ tokens.
- github.com/microsoft/autogen and github.com/langchain-ai/langgraph-supervisor-py → supported. Both are archived; langgraph-supervisor was archived on 20 Sep 2026. The claim "both archived by October 2026" holds.
- Google blog, Kim v3, MAST → supported, including the Dealroom "39–70%" attributed to the earlier version.
- Interview design ai-coding-cli → supported. The quotes "Impossible by construction … conflicts surface at merge, visibly" and "context isolation first" were found.

## 13 coordination-and-handoffs

**Issues and fixes**
- The ADK quote did not match the page.
  - Before: "parallel peers can't see each other's work".
  - After: an agent "cannot see what its peer agents are doing".
- The Anthropic harness quote was missing a word.
  - Before: "doesn't always pass clear instructions".
  - After: "doesn't always pass perfectly clear instructions".
- The Cognition 2026 claim "children … fail to surface discoveries" overstated the page. It now reads "often assume shared state they lack, and agents do not communicate with one another by default".
- The Linux Foundation release from 9 Apr 2026 claims "active production deployments" but names no customers. The chapter now says so before calling the release non-operator evidence.
- A2A 1.0 writes its task states with a `TASK_STATE_` prefix. The chapter now notes the prefix.
- Ruling 22: the RFC 8693 sentence now names `sub` next to `act`.
- Ruling 19 (turn vs exchange): the requirements table's "inside the turn budget" became "inside the exchange's latency budget".
- Banned word "unlocks" became "permits".
- Cross-part reconciliation with ch09, inside my part only. Ch13 said that since June 2027 escalations "use `escalation_handoff.v2`", rendered by the desktop as the escalation package. Ch09 says that in August 2027 the package was still a model-written paragraph, with 38% re-asks, and that package v2 shipped on 2027-11-08. The ledger holds both facts. Ch13 now says the v2 payload has been in the task record since June, but the desktop showed a model-written paragraph until November. It names August's review as the cost of that gap.
- No numbers changed. The Lost Handoff matches the ledger: about 640 a day, 2,000 handoffs audited, and the 52 / 37 / 11 / 9 / 4 / 3 / 6 / 23 / 6 breakdown. The fix shipped on 2027-04-28, then about 25,000 handoffs, 2.1% refused and +0.4 s. The fold-back is dated 2027-06-07, escalations run at about 2,300 a day, and the A2A pilot ran at about 1,800 tasks a week with a 24 h `INPUT_REQUIRED` cancellation.

**Citations spot-checked**
- github.com/a2aproject/A2A/releases → supported: v1.0.0 on 12 Mar 2026 and v1.0.1 on 28 May 2026.
- aaif.io/blog/a2a-joins-aaif → supported. It was posted on 17 Aug 2026, after mid-2026, and confirms A2A as a hosted AAIF project.
- linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations… → supported (9 Apr 2026, 150+ organizations, Azure AI Foundry, Copilot Studio, Bedrock AgentCore). The production-use wording is now qualified.
- a2a-protocol.org/latest/specification/ (1.0.0) → supported. All quoted phrases were found in the spec text: signature verification, `/.well-known/agent-card.json`, "cannot accept further messages", "SHOULD NOT be used to deliver task outputs", "MUST NOT be considered a reliable delivery mechanism…", "success is not guaranteed", the opacity sentence, and "In-band credential exchange can allow credentials to be passed across chains of multiple A2A agents".
- adk.dev/workflows/collaboration/ → partly supported. It is Google ADK documentation and confirms the task, single_turn and chat modes. The quote is fixed.
- github.com/langchain-ai/langgraph-supervisor-py → supported. It is archived, and its handoff passes the full message history.
- Interview designs → supported. These quotes were found: "Approval and handoff are related", "rather than copying uncontrolled", "not the campaign owner", "a queue, not a callback" and `stale_version`. The public-benefits `/decide` endpoint has no idempotency key or case version, which confirms the gap the chapter names.

## Rulings checked across the part

- **Ruling 1 (harness):** used only for the deterministic harness or Forge.
- **Ruling 4 (exactly-once):** no claims of "exactly-once" or "same transaction".
- **Ruling 5 (unknown outcome):** the `unknown` state is used correctly in ch13.
- **Ruling 6 (approval model):** ch10 states hash binding, expiry and voiding.
- **Ruling 15 (authorization vs execution):** Bulkhead decides and Toolyard executes, throughout.
- **Ruling 21 (credit limits):** no "one credit per ticket" wording appears.
- **Ruling 23 (manifest labels):** no manifest labels appear.
- **Ruling 20 (Forge split):** not discussed in this part.
- **Closewise close-week volume:** only "about 1,900 a month" appears, and no daily figure, so the `[editor]` ruling of 380 a day is not contradicted.
- **Banned words:** none remain. "Robust" appears only inside a paper title.

## Verification

- `python3 _wiring/build.py`: agentic-systems-architecture built. The run ended with a traceback on `docs/opencre`, another journal's parallel build, which does not affect this journal. The only agentic warnings are posts not yet written.
- `render_check.py part-3 planning-and-decomposition routing-and-delegation single-and-multi-agent-designs coordination-and-handoffs`: no failed mermaid diagrams and no unresolved cross-links. 0 pages with problems.
- I updated specs 10–13 with a Changelog line (revised is already 2026-10-28). The intro spec is unchanged. Success criteria and Non-goals still match the articles.

## Cross-part issues for the editor

1. **Escalation handoff vs escalation package (ch09 ↔ ch13; the ledger holds both).**
   - Ch13 originally said: "Since June 2027 those escalations use `escalation_handoff.v2`: the same code-filled identifiers and commitments … The support desktop renders it as the escalation package ([[agent-interaction-design]])."
   - Ch09 says: "The escalation 'package' at the time [August 2027] was a model-written paragraph pasted into the ticket, plus a link to the transcript … identifiers and open commitments were sometimes missing". Package v2 shipped on 2027-11-08.
   - I fixed ch13 to fit ch09. The editor may want one `[editor]` ledger line saying the June payload was not rendered to staff until November.
2. **Fixture Purge dates in the ledger (not Part III, noted in passing).**
   - The `[partial-failure-and-compensation]` addition says: "reviewer flagged it Thu **22 July 2027** … hold lifted Mon **2 August 2027**".
   - The `[domain-coding-agents]` addition says: "Noticed **Fri 16 July** by a Parts reviewer … trigger paused that day … re-enabled **Mon 9 Aug 2027**".
   - The chapters in Parts VI and XI should be checked against each other.
3. **Ledger wording on "turn".** The ledger's `[agent-cost-and-model-routing]` line says "Large-tier planning call every turn" and "classifier-marked complex turns", which ruling 19 would call exchanges. Ch11 now says "exchange". Ch36 (agent-cost-and-model-routing) may still say "turn".
