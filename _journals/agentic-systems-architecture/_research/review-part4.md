# Review — Part IV (CONTEXT), 2026-10-28

Scope: `part-4-intro`, `14-context-engineering`, `15-retrieval-and-grounding`, `16-agent-memory`, `17-task-state-and-checkpoints`, `18-provenance-and-freshness`. Read against style-guide.md, consistency-issues.md (rulings 1–23) and scenario-ledger.md (including `[editor]` lines).

## Word counts (front matter to "Sources and Evidence", tables without pipes, no code or mermaid)

| Page | Before | After |
| --- | --- | --- |
| part-4-intro | 925 | 925 (not edited) |
| 14-context-engineering | 7,000 | 7,044 |
| 15-retrieval-and-grounding | 6,950 | 6,953 |
| 16-agent-memory | 7,202 | 7,164 |
| 17-task-state-and-checkpoints | 7,029 | 7,042 |
| 18-provenance-and-freshness | 7,412 | 7,277 |

All under 8,000. The intro is 25 words over the 900 guide. I left it unchanged because it is within tolerance and every sentence carries a case.

## Rulings checked across the part

- Ruling 19 (turn vs exchange): this was the main deviation. 14, 15, 16 and 17 used "turn" for a customer message plus reply, and for history units. Fixed (details below).
- Rulings 4, 5, 6, 15, 1: already applied correctly. Ch17 uses intent → execute → receipt, `unknown` → status lookup → repair queue, and "exactly-once *effect*". Ch18 binds approvals to the content hash and voids them on a fact change, and has Bulkhead decide while Toolyard executes. "Harness" is used only in ruling 1's sense or in Anthropic's post title.
- Rulings 20, 21, 22, 23 and the Closewise 380/day `[editor]` line are not referenced in Part IV. No "325/day", no manifest labels and no `sub`/`act` claims appear.
- Ostrell numbers checked against the ledger and match: Half-Posted Accrual (52/37/€2.84M/2 days), game day 4 June 2027, schema v3 → v4, Weekend Fan-out, Alias Drift, Stale Price Book (23 days, 14 quotes, €46,000, 3 later drafts, 2027-05-20/06-01), Stale Preference (640,000/96,000/6.8%/46/11/€290/2,140; migration rows sum to ≈188,000), grounding audit (11.2% → 2.4%, recall 0.71 → 0.90), Second Revisit (57/41, 14,800 → 13,900, 58,000 → 23,600, 11% → 76%, 71% → 94%, 79% → 85%).

## Per chapter

### part-4-intro
- No issues. Numbers match the chapters. Hand-offs to [[part-3]] and [[part-5]] are present. Not edited.

### 14-context-engineering
- **Fold-back date (`[editor]` line 137).** The chapter said the billing specialist agent was folded back "in April 2027", and the May trace review showed 34 tools on every call. The editor ruling dates the fold-back to 2027-06-07, with a typed handoff in place from 2027-04-28. Rewritten: the team *prepared* the fold-back after April's Lost Handoff, and it shipped 7 June ([[coordination-and-handoffs]]). The May findings row now reads "19 tools in production; the fold-back release candidate carried 34 tools, about 11,800 tokens". This also stays consistent with the June resident-core plus tool-search change.
- **Ruling 19.** About 30 replacements: history units, compaction ranges, the per-call budget layout, the worked example and the tables now say *exchange*.
  - Before: "5.2 customer turns … each turn makes 2.8 model calls". After: "5.2 exchanges … 2.8 model calls, that is, 2.8 turns in [[agent-runtime]]'s sense".
  - Before: "turn 19", "turns 1–14", "last 4 turns". After: "exchange 19", "exchanges 1–14", "last 4 exchanges".
  - Before: "append-only within a turn's inner loop, re-assembly at the turn boundary". After: "append-only across the turns inside one exchange, re-assembly at the exchange boundary".
  - The code literal `"turns"` became `"exchanges"`.
- **Evidence wording.** Anthropic's 77,000 → 8,700-token figure belongs to a separate 50+-tool example, not the 58-tool/55,000-token setup. Reworded.

### 15-retrieval-and-grounding
- **Ruling 19.** "every turn" became "every model call"; "a turn that makes a factual claim" became "a reply"; "live chat turn", the "One turn, end to end" heading and the Figure 3 caption became *exchange*; "knowledge turn" became "knowledge answer"; "Pre-retrieval every turn" became "before every model call".
- No number changed. Ownership is clean: grounding, citation and permission-aware retrieval are defined here.

### 16-agent-memory
- **Repetition.** Replaced the five-store table (a third copy, after ch14 and ch17) with one sentence linking to [[context-engineering]].
- **Ruling 19.** Memory provenance cited "turns". These are now *messages*: the field `sourceTurns` became `sourceMessages`. "Confirmation adds a turn" became "adds a question to the conversation"; "ground every turn" became "every exchange".
- **Evidence.** For the OWASP Agentic Top 10 (ASI06, "Memory and Context Poisoning"), the December 2025 publication date is verified, but the resource page does not show the categories. Now labeled "not verified against the primary text".

### 17-task-state-and-checkpoints
- **Store table aligned with agent-memory.**
  - Long-term memory writer. Before: "Model or background process, under a write policy". After: "Gated write path; the model may only propose".
  - Memory lifetime. Before: "Months, with expiry". After: "Per memory class, always finite".
  - Conversation-history lifetime. Before: "One session". After: "Session plus audit retention", as in ch14.
- **Approval wait vs durable-agent-execution ledger (48-working-hour timer).** Before: "waits up to three days for controller approval". After: "can wait days … escalating to the entity's deputy controller after 48 working hours ([[durable-agent-execution]])".
- **Ruling 19** in Across Domains: "Conversation turn state" became "Conversation state"; "within a turn" became "within an exchange"; "Per turn" became "Per exchange".

### 18-provenance-and-freshness
- **Repetition / ownership.** Four Evidence paragraphs re-taught material owned by 15, 16 and 14, and were cut to one sentence each with links:
  - ALCE plus Anthropic Citations
  - MINJA plus PoisonedRAG details
  - the Anthropic harness and multi-agent posts
  - *Moffatt v. Air Canada*

  Their now-uncited source entries were removed: ALCE, MINJA, PoisonedRAG, the harness post and Citations. About 135 words saved.
- **Ledger alignment.**
  - Memory row in the freshness register. Before: "Review after 90 days *(assumption)*". After: Ostrell policy, linked to [[agent-memory]].
  - Tidemark row. Before: "Provenance, confidence and expiry". After: "Provenance, trust level and expiry" (schema v3 replaced model confidence).
- **Recommendation fix.** "require re-read and compare for every action **above tier A3**" was meaningless, because A3 is the highest autonomy. It now reads "every action that changes an external system or makes a commitment and depends on a volatile data class, whatever its tier".
- **Quote fix.** Zhang et al. Before: "over-commit to early mistakes, leading to more mistakes that [they] otherwise would not make". After: the abstract's wording, "over-commits … that it otherwise would not make".

## Sources spot-checked (URL → verdict)

| Ch | URL | Verdict |
| --- | --- | --- |
| 14 | anthropic.com/engineering/advanced-tool-use | Supported (24 Nov 2025); 77K → 8.7K is a separate 50+-tool example. Wording fixed |
| 14 | github.com/open-telemetry/semantic-conventions-genai/…/gen-ai-spans.md | Supported: SHOULD NOT capture by default; external storage with references recommended in production |
| 14 | arxiv.org/abs/2510.09023 (Nasr et al.) | Supported: 12 defenses, >90% for most |
| 14 | adk.dev/sessions/ | Supported: Session, State, Memory (Events mentioned) |
| 15 | platform.claude.com/…/citations | Supported: "guaranteed to contain valid pointers"; incompatible with structured outputs |
| 15 | arxiv.org/pdf/2405.15793 (SWE-agent, Table 3) | Supported: Summarized 18.0, Iterative 12.0, No search 15.7 |
| 15 | anthropic.com/engineering/demystifying-evals-for-ai-agents | Supported (9 Jan 2026): "Unknown" option; calibrate against human experts |
| 16 | genai.owasp.org/…/owasp-top-10-for-agentic-applications-for-2026/ | Date verified (9 Dec 2025); ASI06 title not visible. Claim labeled as unverified |
| 16 | microsoft.com/…/2025/04/24/new-whitepaper-outlines-the-taxonomy-… | Supported: memory-poisoning case; "external authentication or validation for all memory updates" |
| 16 | embracethered.com/…/2025/gemini-memory-persistence-prompt-injection/ | Supported (10 Feb 2025): trigger word; low likelihood and low impact |
| 16 | techcrunch.com/2025/04/10/openai-updates-chatgpt-… | Supported: UK, EU and other countries excluded pending "additional external reviews" |
| 17 | learn.microsoft.com/…/durable-functions-code-constraints | Supported; ms.date 2026-10-12 (the "October 2026 revision" is correct); all four quotes present |
| 17 | temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal | Supported (12 Nov 2025): recorded LLM decisions, no new plan |
| 17 | github.com/temporalio/ai-integrations/…/openai_agents | Supported: quote verbatim; model calls run as activities |
| 18 | arxiv.org/abs/2503.18813 (CaMeL) | Supported: 77% vs 84% |
| 18 | arxiv.org/abs/2305.13534 (Zhang et al.) | 67%/87% supported; quotation wording corrected |
| 18 | sre.google/workbook/data-processing/ | Supported: ch. 13; both freshness formats |

No citation failed outright. Two needed rewording (advanced-tool-use, Zhang) and one was labeled unverified (OWASP ASI06).

## Spec updates

`revised: 2026-10-28` was already set. A Changelog line "Review pass: …" was added to the specs of 14, 15, 16, 17 and 18. Success criteria and Non-goals still match the articles. The intro spec is unchanged.

## Verification

- Build: `[built] agentic-systems-architecture -> docs/agentic-systems-architecture`. The only warnings are missing not-yet-written pages: introduction, where-agentic-systems-go-wrong, part-11-intro, source-coverage, glossary.
- `render_check.py` on part-4 and the five chapters: 15 mermaid diagrams, 0 failed, 0 unresolved cross-links.

## Cross-part issues for the editor

1. **Fixture Purge dates disagree between Part VI and Part XI ledger lines.**
   - `[partial-failure-and-compensation]`: "reviewer flagged it Thu **22 July 2027**; `fix_failing_ci` action class held that evening … hold lifted Mon **2 August 2027** (11 days)".
   - `[domain-coding-agents]`: "Noticed **Fri 16 July** by a Parts reviewer …; trigger paused that day; 19 July: 7 open PRs closed …; Trigger re-enabled **Mon 9 Aug 2027**".
   - Chapters 25 and 41 should be checked. Not in Part IV.
2. **Ledger line `[context-engineering]` still says "After April's Lost Handoff fix Answerdesk had 34 tools"** and "last **4** turns kept verbatim". The chapter now follows the `[editor]` fold-back date (2027-06-07) and ruling 19 ("4 exchanges"). The ledger is append-only, so an `[editor]` line may be wanted. The same applies to the `[caching-and-context-budgets]` wording "this turn's retrieval results" (an exchange) if chapter 37 uses it.
3. **Answerdesk escalation-review line `[agent-interaction-design]`** says Toolyard's "one active credit proposal per ticket" rule. That is consistent with ruling 21's second clause. No action needed; noted only because reviewers grepping "per ticket" may flag it.
