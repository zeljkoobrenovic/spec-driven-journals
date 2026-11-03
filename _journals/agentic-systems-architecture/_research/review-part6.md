# Review — Part VI (RELIABILITY)

Reviewer pass, 2026-10-28. Pages: `part-6-intro`, `23-durable-agent-execution`, `24-retries-idempotency-and-concurrency`, `25-partial-failure-and-compensation`. Build passes; `render_check.py` reports 0 problems (mermaid 1/3/4/2, no unresolved links).

## Word counts (front matter to "Sources and Evidence", tables/code/mermaid excluded)

| Page | Before | After |
| --- | --- | --- |
| part-6-intro | 913 | 913 |
| 23 durable-agent-execution | 7,347 | 7,353 |
| 24 retries-idempotency-and-concurrency | 6,911 | 6,935 |
| 25 partial-failure-and-compensation | 7,171 | ~7,290 |

All are under 8,000, so nothing had to be cut for length. The intro is 13 words over its 900-word target, which is acceptable.

## part-6-intro

- Checked the callouts, the three KEY POINTS, the failure patterns, the figure, the chapter list and the hand-off. Its numbers (52/37/€2.84M/2 days; 23 entities, 61 once each; 212/€31,400/30 s; 11 timeouts, 0 duplicates; 9 PRs, 2 merged; about 35 min) match the chapters and the ledger. No changes.

## 23 durable-agent-execution

- **Kill switch (ruling 10, ownership).** Before: "The platform-wide kill switch is cancellation applied to every run of an agent at once…". This contradicted chapter 25's definition (holds, never cancels). After: "The platform kill switch is not mass cancellation: it stops new side effects across every run in its scope and holds queued actions…", linked to [[partial-failure-and-compensation]].
- **Run state name.** In the failure table, `cancel_requested` became `cancelling` (the [[agent-runtime]] lifecycle).
- **Model fallback.** "Mid tier with a Large-tier fallback" became "with a fallback only where the manifest names and gates one", matching the gateway and manifest rules (`fallback: none` unless gated; the Quiet Failover).
- **Scout and job queues.** The trade-off table implied Scout runs on a job queue, but the ledger has Keelson Runtime running every agent on the durable engine. It now reads "read-only research runs like Scout's". The unsourced "median of about €3.10" restart cost became a labeled assumption.
- Ledger check: the September 2027 close figures (1,912 proposals, 164 for Ostrell Field Deutschland GmbH, 44 of 61, the node-pool upgrade on 4 Oct with 2 re-sent calls, 9 Assure UK escalations, 3 voided approvals, the Benelux cancellation with 31/0/17, working day 5 on 7 Oct) all match. Close-week volume: 1,912 over five days is about 382 a day, consistent with the editor's 380. The approval timer of 48 working hours and the 45 s heartbeat both match.
- Exactly-once *effect* wording (ruling 4) and the unknown state (ruling 5) are both used correctly.

## 24 retries-idempotency-and-concurrency

- **Credit limits (ruling 21).** "one goodwill credit per ticket and visit" / "per missed visit" / "per visit" (3 places) became "at most one service credit per technician visit". The collision table now adds "at most one pending credit proposal per ticket".
- **Approval and authorization (rulings 6, 15).** "A Bulkhead approval is bound to…" became "An approval is bound to the object's content hash, expires, and is re-checked by Bulkhead immediately before dispatch".
- **Ownership link.** The Half-Posted Accrual pointed to [[durable-agent-execution]]; it now points to [[task-state-and-checkpoints]], the chapter that owns the story.
- **Citation precision.** Anthropic's errors page (fetched) now says a self-set spend limit returns 400, and that a 429 without `retry-after` comes from a usage tier's monthly spend cap. The wording was updated to match.
- Ledger check: the Double Credit (30 s, 212, €31,400, 3 step attempts, approval attached to the step, client reference not sent, parallel email and chat), the post-fix rules (key from agent, run and action object ids; ≤ 3 tool attempts; 10-minute lookup then the billing desk; Gateway ≤ 2 retries and ≤ 10%; the business key format; Closewise workflow id = entity + period) all match. The November worked example is labeled illustrative.

## 25 partial-failure-and-compensation

- **Fixture Purge timeline (editor ruling 24; [[domain-coding-agents]] owns the story).**
  - Before: flagged Thu 22 July 2027 by a Field scheduling reviewer (PR "Fix failing CI on route optimizer"); held that evening; blast radius Fri 23 July, 31 PRs including the 9 from the purge; revert PRs restored the tests; hold lifted Mon 2 August, 11 days.
  - After: noticed Fri 16 July 2027 by a Parts engineer (a PR that removed eleven test cases led them to the earlier skip); held that afternoon; 7 open PRs quarantined, then closed on Mon 19 July; the back-scan found 31 *further* test-removing PRs, all justified; the 2 merged PRs were compensated on 19 July (skip reverted and the shipped defect fixed by hand, which is the forward fix after deploy; the timing test restored behind a retry annotation); re-enabled Mon 9 August on 120 repositories after the verifier contract shipped; held about three and a half weeks.
  - I appended a superseding line to `scenario-ledger.md`, because the chapter's original ledger line still carries the old dates.
- **`issue_credit` reversibility (cross-chapter contradiction).** Chapter 25 called `issue_credit` a **pivot**. Chapters 03 and 22 class credits as **compensable** (undo = a debit on the next invoice with customer notice). Chapter 25's own rule also caps pivots at A1, which conflicted with credits running at A2. I aligned chapter 25 to the earlier-owned chapters:
  - Table row: compensable, `debit_next_invoice` with customer notice, window until the next invoice *(illustrative)*, compensation tier A0.
  - The policy paragraph was rewritten to match.
  - The pivots row in Across Domains changed from "Money to the customer" to "Card refunds and payments to the customer".
  - "Accept and remediate" was reworded.
  - The superseding ledger line records this.
- **Restate quote fixed.** The chapter quoted "because the charge may succeed even if the confirmation is lost". The page actually says "in case action succeeded but confirmation was lost".
- **Refusal guidance and the source disagreement.** The cited Anthropic page (as of October 2026) recommends retrying a refused request on a fallback model. The chapter now says so and keeps its own rule (no re-prompting or model switching after effects exist) as the author's judgement.
- **Robodebt.** The cited LSJ article does not support "debts … reduced to zero". The sentence now states what the article does say: reimbursement of about 430,000 debts worth more than A$720 million, plus about A$112 million in compensation.
- Ledger check: the Half-Posted Accrual, the compensation drill (37 reversals, about 35 min, 3 partly offset duplicates), the Alias Drift (4 days, 4% → 11%), the Stale Price Book (14 quotes, €46,000), the kill switch's five scopes and ≤ 60 s target, and `post_reversal_entry` approved by a different controller all match.

## Specs

All three chapter specs now have a Changelog line for this review; `revised` stays 2026-10-28. In spec 25:

- The success criterion now carries the ruling-24 dates.
- A decision-log line records the credit reclassification.
- The "money returned to a customer" decision is narrowed to card refunds.

The specs' success criteria and non-goals still match the articles.

## Sources spot-checked (WebFetch)

| URL | Verdict |
| --- | --- |
| anthropic.com/research/measuring-agent-autonomy | Supported (99.9th percentile turn under 25 → over 45 min, Oct 2025–Jan 2026; published 18 Feb 2026) |
| github.com/temporalio/ai-integrations/…/openai_agents | Supported (model calls routed through activities; function tools run in the workflow unless backed by an activity) |
| docs.temporal.io/workflow-execution/limits | Supported (warning at 10,240 events / 10 MB; limit 51,200 / 50 MB) |
| learn.microsoft.com/…/durable-functions-code-constraints | Supported; ms.date 2026-10-12 confirmed. "won't catch all violations" is about thread detection, which is consistent with the chapter's use |
| thinkingmachines.ai/blog/defeating-nondeterminism… | Supported (1,000 completions, 80 unique, batch-invariant kernels make all identical; 10 Sept 2025, H. He) |
| platform.claude.com/docs/en/api/errors | Supported (SDK retries twice by default; streaming suggested for long requests and 504s); the spend-limit 429 wording was refined (ch 24) |
| datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ | Supported (-08 dated 22 Oct 2026; 400/422/409; -00 submitted 1 July 2021, matching "a draft since 2021") |
| arxiv.org/abs/2503.13657 (+ HTML v3) | Supported (1,600+ traces, 7 frameworks, step repetition 15.7% and the most frequent; premature termination and verification modes listed) |
| docs.langchain.com/oss/python/langgraph/fault-tolerance | Supported (RetryPolicy max_attempts default 3) |
| modelcontextprotocol.io/specification/2025-11-25/schema | Supported (annotations are hints, "not guaranteed to provide a faithful description"; idempotentHint defined) |
| euronews.com/…/an-ai-agent-deleted-a-companys-entire-database… | Supported (PocketOS, Cursor agent, database and backups, outage of more than 30 h, data restored; T. Farrant, 28 Apr 2026) |
| neuraltrust.ai/blog/pocketos-railway-agent | Supported (token found in an unrelated file, not narrowly scoped; backups inside the volume; 28 Apr 2026) |
| tech.yahoo.com/…/claude-code-deletes-developers-production… | Supported (Terraform destroy, database and snapshots, AWS support restored the data "within about a day"; B. Ferreira, Tom's Hardware, 7 Mar 2026) |
| lsj.com.au/…/robodebt-royal-commission-findings | Partly supported: figures confirmed, "reduced to zero" not supported. Fixed |
| docs.restate.dev/guides/sagas | Paraphrase presented as a quote. Fixed; business errors as terminal confirmed |
| platform.claude.com/…/handle-streaming-refusals | Supported (HTTP 200 with `stop_reason: "refusal"`, error-rate monitoring misses it, reset context, model refusals as standard text); the page also recommends fallback-model retry, now acknowledged |

No citation had to be removed.

## Cross-part issues for the editor

1. **Credit reversibility.** Fixed on the Part VI side. The original chapter-25 ledger line (`issue_credit` and `send_email` are pivots) is now superseded by an appended line. Chapter 03 (line ~315, "Issue credit ≤ €250 | Compensable | C2") and chapter 22 (line ~128, "Service credit (reversal note)") were already consistent. A pivot-at-A1 rule elsewhere would no longer conflict with A2 credits.
2. **Fixture Purge.** Chapter 25 is now consistent with chapter 41 and ruling 24. No other chapter used the old 22 July / 2 August dates (checked by grep).
3. Not an error, but worth knowing: chapter 41 states "the first bad merge went unnoticed for eight days" (8 → 16 July). Chapter 25 now implies the same window.
