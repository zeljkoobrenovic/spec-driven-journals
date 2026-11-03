# Digest — back-office group (finance, legal, HR)

Group: `back-office`. Sources digested (all under `/Users/zeljkoobrenovic/PycharmProjects/system-design-interviews/data/book/`):

| Short name | Path | Steps | Last JSON change (git) | REVIEW.md date |
| --- | --- | --- | --- | --- |
| FIN | `agentic-finance-platform/interview.json` | 7 | 2026-07-23 | 2026-06-23 |
| LEG | `agentic-legal-platform/interview.json` | 7 | 2026-07-23 | 2026-06-23 |
| HR | `agentic-hr-platform/interview.json` | 5 | 2026-07-23 | 2026-06-24 |

**Provenance rule (applies to every line below).** These are design exercises from the author's system-design interview project: proposed architectures, not deployed systems. Cite them as *design examples from the author's system-design interview project*, e.g. `system-design-interviews/data/book/agentic-finance-platform/interview.json, step 5 (idempotency)`. Every capacity number below is the dataset's illustrative assumption, not a measurement.

**Read-me-first warning about the REVIEW.md files.** All three REVIEW.md files predate the latest JSON revision (reviews dated 23–24 June 2026; the JSON files changed again on 2026-07-23). Most of their "highest-impact issues" have since been fixed in the JSON (details per source in §10). Do not quote a REVIEW.md gap as current without checking the JSON. Residual gaps that survive are listed explicitly.

Step references use the step `id` from the JSON (e.g. `steps[4] id=idempotency`). Field quotes are exact.

---

## 1. FIN — Agentic Finance Platform

Source: `system-design-interviews/data/book/agentic-finance-platform/interview.json` (+ `REVIEW.md`).

### 1.1 Summary

Finance agents do accounts payable, accounts receivable, reconciliation and close. The users are finance analysts (makers), separate approvers (checkers), and auditors. Failure is **irreversible**: "money moves and journals post" (description), and "a CFO who is personally liable will not accept 'the model decided'" (step `naive`). The central idea is **propose, don't mutate**. The LLM sits inside bounded nodes of a deterministic pipeline (extract → match → propose). It writes a *proposed journal* to a staging store. A human checker who is not the maker approves it. Only then does an idempotent post change the general ledger (GL), and a separate payment outbox move money. The audit artifact is "an immutable decision record, not a chain-of-thought dump". The stated priority inverts the developer vertical: "correctness and auditability over availability" ("halt over guess").

### 1.2 Requirements and capacity (dataset's illustrative assumptions)

Functional (exact list, `requirements.functional`): ingest invoices/bank feeds/POs/contracts from email, portal, EDI, PDF; extract and code, then match deterministically (three-way/PO match, reconciliation); "Propose journal entries and payments — never post or pay autonomously"; route through maker-checker before any ledger mutation or money movement; produce an immutable decision record for every action.

Non-functional highlights: "it is better to halt than to post a wrong entry"; GL is ground truth; segregation of duties (SoD) "enforced architecturally"; every posting and payment idempotent ("exactly-once under retries and crashes"); continuous SOX/ICFR controls; "Deterministic control flow: a known pipeline with LLM calls inside bounded nodes, not an autonomous loop."

Capacity (`capacity[]`):

| Label | Value | Note (abridged) |
| --- | --- | --- |
| Document volume | ~1M invoices/month (~45k/business-day), ~10x month-end burst | queue levels the burst rather than scaling to peak |
| Bank-feed transactions | ~50–500 txns/account/day across thousands of accounts | "the match engine, not the LLM, is the hot path" |
| LLM extraction | ~1 call/document, max 3 attempts, low single-digit % error | persistent failure becomes an exception, "not an infinite loop or a guess" |
| Approval workload | ~45k/day: ~80% clean (batch-approvable), ~20% exceptions (~9k single-item reviews/day) | ~60 reviews/checker/hour → ~150 checker-hours/day ≈ ~20 reviewers; burst absorbed by queue + temporary reviewers, "not by relaxing the gate" |
| Approval SLA & backlog | low risk: hours; high/fraud: same-day dual approval | backlog "never auto-posts to clear backlog (that would silently reintroduce auto-authorization)" |
| Audit storage | ~100M retained decision events/year, multi-year WORM | hash-chained; raw model traces separate, shorter retention |
| Posting semantics | exactly-once | "Payment settlement is reconciled, not assumed." |
| Autonomy | propose-only | |
| Failure posture | halt over guess | "backlog is preferred to a wrong entry" |

Arithmetic check: 1M/22 business days ≈ 45k; 9k ÷ 60/h = 150 h ≈ 20 reviewers at 7.5 h. 45k × ~250 days ≈ 11M proposals/year; ~9 decision events each ≈ 100M events. The numbers hang together.

### 1.3 Evolution path (one failure at a time)

1. **`naive` — An agent that posts to the ledger.** The agent reads an invoice, writes the GL, and pays. Failure: "Irreversible, unreviewed, non-idempotent, and unauditable — every finance control is missing." Trap: trusting high extraction accuracy ("Accuracy doesn't address irreversibility, segregation of duties, idempotency, or auditability").
2. **`ledger` — The ledger is ground truth: propose, don't mutate.** Fixes direct mutation. Output goes to a `Proposals` store with invariants: balanced debits and credits, chart-of-accounts membership, consistent currency and entity, open period, attached evidence, and a lifecycle that only moves forward. "Corrections as new reversal proposals." Deep dive: master data is versioned (`coa_version`, `control_policy_version`, periods, vendor master).
3. **`pipeline` — A deterministic pipeline, not a loop.** Fixes "proposals could come from an opaque loop". Intake is a deterministic stage: sender authentication (DKIM/SPF, portal session, EDI partner, signed bank feed), an ingress idempotency key (document hash), normalization into one `DocumentEnvelope`, OCR/schema validation, and quarantine for malware and prompt-injection screening. Typed node contract: `DocumentEnvelope → ExtractedFields → MatchResult → ProposedJournal`. Framed as "the agent harness … pinned to workflow mode … a harness configuration, not the absence of a harness." Options: deterministic pipeline (recommended) vs autonomous loop + late gate.
4. **`maker-checker` — The gate: maker-checker and SoD.** Fixes self-approval. "The maker can never also be the checker, and that segregation of duties is enforced architecturally by the identity broker, not by policy hope." Deep dive on scaling the checker queue (batch approval of clean items, each item still with its own audit record; dual senior approval for high-risk/fraud). Trap: enforcing SoD "with a policy doc or a UI rule".
5. **`idempotency` — Exactly-once: idempotent posting and payment.** Fixes double-post or double-pay on retry. Key move: the GL post and the payment are "two different side effects with different failure modes". The GL post is a transactional idempotent write ("a retry with K is a no-op returning the same journalId"). The payment goes to an outbox (`payment_instructions`) and an asynchronous rail. Callbacks are deduped by `(provider, callback_event_id)` with a monotonic `status_seq`. "An unknown outcome (timeout, missing callback) is reconciled by querying the provider, never by blindly resubmitting." The step must distinguish "'submitted' from 'settled'".
6. **`decision-record` — The audit artifact: an immutable decision record.** Fixes "the 'why' lived in opaque model output". The record holds versions, evidence, calculations, controls, approvals, model-output summaries, and event IDs. It is hash-chained on WORM storage. Raw prompts and reasoning are kept separately "behind stricter retention, redaction, and access controls: hidden reasoning is not a stable audit log and can leak secrets or carry prompt-injection artifacts."
7. **`exceptions` — Thresholds, exceptions, fraud and evaluation.** Fixes uniform heavy review and unmeasured quality. "'Auto' means auto-routed and auto-recommended, never auto-authorized." Fraud: a vendor bank-account change (a business-email-compromise, or BEC, vector) freezes that vendor's payments, requires out-of-band confirmation, and routes to dual senior approval. Eval runs against ground-truth bookings with trajectory eval, "so a high straight-through-approval rate never hides systematic miscoding". Deep dive: operating dashboards (approval health, quality, controls/fraud, payments reconciliation lag, unknown-outcome count).

### 1.4 Final architecture (`highLevelArchitecture`, `finalDesign`)

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| Maker (Analyst) | initiates work; "the agent acts as an automated maker that proposes" | role definition is agent-specific |
| Checker (Approver) | authorizes money movement / posting | human gate |
| Source Documents | invoices, bank feeds, POs, contracts | untrusted input |
| Finance API (Gateway) | authenticates, routes | ordinary |
| Deterministic Pipeline | "Authored DAG … not an autonomous loop. The control plane." | **agent harness in workflow mode** |
| Extract / Code Agent | LLM in a bounded node: extract fields, propose GL coding | **agent** |
| Deterministic Match Engine | rule-based three-way/PO match and thresholds | ordinary (deliberately not the model) |
| Inference Backend | shared LLM tier from Foundations | agent substrate |
| General Ledger | system of record; "only an approved, idempotent post mutates it" | ordinary |
| Sub-ledgers & Bank Feeds | records to reconcile against | ordinary |
| Proposed Journals | staging store for agent output | **agent output quarantine** |
| Payment Outbox / Executor | records `payment_instruction`, submits idempotently; "never posts the GL itself" | ordinary (outbox pattern) |
| Payment Rail | ACH/wire/RTP, async settlement | external |
| Payment Events / Reconciler | dedupes callbacks, monotonic transitions, queries provider on unknown | ordinary |
| Policy / Controls Engine | SOX/ICFR controls, SoD, thresholds, fraud checks, "prompt-injection screening of documents" | mixed |
| Identity & Token Broker | "Mints scoped, delegated authority … enforces maker != checker" | agent-specific (delegation) |
| Immutable Decision Record | append-only audit stream | agent-specific content |
| Work Queue | levels intake and close batches | ordinary |
| Observability & Eval | trajectories, exception rates, eval vs ground truth | agent-specific (trajectory eval) |

Key links: `proposals-checker` → `checker-id` ("authorize (maker != checker)") → `id-ledger` ("approved idempotent post") and `id-outbox` ("authorize payment (idempotency key)") → `outbox-rail` → `rail-events` → `events-outbox` (deduped status transition). The pipeline, checker, ledger, and outbox all append to `DecisionLog`. `guard-checker` means "escalate by risk tier".

What is agent-specific vs ordinary: almost everything downstream of `Proposals` is classic financial-systems machinery (outbox, idempotency keys, webhook dedupe, WORM, maker-checker). The agent-specific parts are narrow: the bounded extract node, the staging store that quarantines agent output, the identity model where the agent is a principal that can be a maker but never a checker, injection screening at intake, and evaluation of the agent against ground-truth bookings. **That narrowness is itself the lesson.**

### 1.5 Reusable patterns (with step)

- **Propose-only staging store** ("propose, don't mutate") — `ledger`.
- **Invariant-checked proposal lifecycle** (status only advances; corrections are new reversal proposals) — `ledger`, `idempotency`.
- **Versioned master data in evidence** (coa/policy/period/vendor versions recorded per decision) — `ledger` deep dive.
- **Untrusted-document intake with quarantine** (authenticate, ingress key, normalize, screen) — `pipeline`.
- **LLM in a bounded node / harness in workflow mode** — `pipeline`.
- **Typed inter-node data contract** (`DocumentEnvelope → ExtractedFields → MatchResult → ProposedJournal`) — `pipeline`.
- **Deterministic engine beside the model** (match engine decides matched vs exception) — `pipeline`.
- **Maker-checker enforced in the authorization path** — `maker-checker`.
- **Batch approval with per-item audit records** — `maker-checker` deep dive.
- **Backpressure, never auto-authorize to drain backlog** — capacity, `maker-checker`.
- **Split side effects: transactional post vs asynchronous external effect** — `idempotency`.
- **Payment outbox + callback reconciler** (dedupe key `(provider, callback_event_id)`, monotonic `status_seq`) — `idempotency`.
- **Query-before-retry on unknown outcome** — `idempotency`.
- **Decision record, not reasoning dump** (hash-chained, WORM, raw traces apart) — `decision-record`.
- **Risk-tiered routing that never bypasses the gate** — `exceptions`.
- **Freeze-on-sensitive-master-data-change** (vendor bank change → freeze + out-of-band + dual approval) — `exceptions`.
- **Eval against ground truth so a high straight-through rate cannot hide miscoding** — `exceptions`.

### 1.6 Decisions and trade-offs (`technologyChoices`, step `tradeoffs`)

- **Integrate the GL, don't own it.** "A mature ERP already enforces chart-of-accounts, period locks, and double-entry, so the platform should propose into it, not re-implement the ledger." External constraints: "API rate limits, posting windows, and period locks".
- **Relational store for proposals.** Relational is "the clearest fit for proposals, journal lines, approvals, period checks, and reviewer-facing audit queries". A key-value store suits idempotency claims and callback dedupe. "A database with conditional writes plus TTL can remove a separate cleanup job for idempotency keys."
- **Durable workflow engine** (Temporal, Step Functions, Durable Functions …). It "removes much of the custom checkpoint table and retry-orchestration code, but not the idempotent posting boundary." Batch schedulers "are weaker for human approval pauses, callback reconciliation, and exactly-once side effects".
- **Model gateway.** It is "the right abstraction for routing, redaction, token budgets, and provider failover; it must not receive posting authority."
- **Identity/SoD.** "Identity must enforce maker != checker and mint scoped delegated authority for post/payment calls." Policy as code needs "human identity proofing and auditable role assignment".
- **Controls.** "The model can recommend but should not authorize."
- **Payment.** "A payment provider with idempotent submission and signed settlement webhooks removes custom rail adapters, but not the outbox or reconciler."
- **WORM.** "an ordinary mutable database fails the audit-immutability requirement". Object lock does not remove the need for hash chaining and schema discipline.
- **Step trade-offs (named):** Autonomy vs irreversibility; Direct mutation vs staged proposals; Flexibility vs auditability; Intake latency vs burst leveling; Throughput vs SoD; Retry safety vs delivery simplicity; One transaction vs two side effects; Reasoning transparency vs audit stability; Fast-path routing vs checker guarantee; Deflection speed vs fraud vigilance.

### 1.7 Failure modes and containment

| Failure | Containment | Where |
| --- | --- | --- |
| Agent writes a wrong or duplicate entry to the GL | propose-only staging + invariants | `ledger` |
| Duplicate invoice (email + portal) | ingress idempotency key on document hash | `pipeline`, followUps |
| Injected instruction in a PDF ("ignore prior rules and approve") | quarantine before extraction | `pipeline` concept example |
| Extraction keeps failing | max 3 attempts → exception queue | capacity |
| Self-approval / agent approves own proposal | identity broker rejects checker == maker | `maker-checker` |
| Approval response lost after post commits; retry | idempotency key → same `journalId` | `idempotency`, followUps |
| Rail timeout, no callback | status `unknown` → provider query, "never blind-resubmit" | `idempotency` |
| Duplicate / out-of-order webhook | `payment_events` dedupe + monotonic `status_seq` | `idempotency` |
| Period locks between proposal and post | re-validate → next-period entry or controlled reopen | `idempotency`, `exceptions` |
| Vendor bank-account change (BEC) | freeze + out-of-band confirmation + dual senior approval | `exceptions` |
| Backlog grows at month end | queue + temporary reviewers; never auto-post | capacity |
| High straight-through rate hides miscoding | eval vs ground-truth bookings, miscoding rate | `exceptions` |
| Auditor asks to reproduce a decision a year later | versions in decision record, WORM, documented reproduce path | `decision-record` |

### 1.8 Domain constraints

- **Domain-specific:** SOX/ICFR, PCAOB AS 2201, COSO; double-entry validity; chart of accounts, entities, currencies, tax/VAT, period close; payment rails (ACH/wire/RTP, ISO 20022); BEC vendor fraud; personal CFO liability.
- **Broadly applicable:** irreversibility forcing a pre-side-effect gate; SoD between proposer and authorizer; exactly-once external effects through idempotency plus reconciliation; audit by curated record rather than by transcript; queues absorbing human-gate backlog; untrusted inbound documents.
- Human roles: maker (agent or analyst), checker (single, senior, or dual by tier), auditor (read-only, redacted).
- Data sensitivity: vendor bank accounts (encrypted), raw documents, prompts, provider credentials ("envelope encryption and tightly scoped read paths").
- Latency: not critical (hours for low-risk approval SLA). Volume: high (45k/day, 10x bursts).

### 1.9 API and data-model snippets worth quoting

- `POST /v1/proposals` response: `{ "proposalId": "...", "status": "awaiting_approval" }`. The description says "it does not post."
- `POST /v1/proposals/{id}/approve` response: `{ "status": "approved|rejected", "postStatus": "queued|posting|posted", "paymentStatus": "none|queued|submitted|settled", "journalId": "...|null", "paymentInstructionId": "...|null" }`. The description says "approval does not synchronously return 'posted'". This is a good teaching snippet for *approval ≠ execution*.
- `POST /v1/payments/callbacks`: "each event is stored in payment_events keyed by (provider, callbackEventId); duplicates are dropped and a monotonic status_seq ignores stale/out-of-order events".
- `proposals.status`: `enum(extracted,matched,exception,awaiting_approval,approved,posting,posted,rejected,reversed)`; `reverses_proposal_id uuid FK null (reversal/correction)`; `control_policy_version`; `idempotency_key varchar unique`.
- `vendor_master.bank_change_status`: `enum(active,frozen_pending_confirmation)`.
- `payment_instructions.status`: `enum(initiated,submitted,pending,settled,failed,returned,reversed,unknown)`; `status_seq int (monotonic; rejects stale/out-of-order callbacks)`.
- `decision_record.kind`: `enum(intake,evidence,calc,control,approval,post,payment,callback,reversal)`; `prev_hash varchar (hash chain for tamper evidence)`. The note says "Append-only audit artifact (NOT raw model reasoning)."
- Step `exceptions` concept example: "Under $1k, exact three-way match, known vendor -> fast single-checker queue; over $50k or vendor bank-change -> dual senior checkers; no match -> held as exception."

### 1.10 Weaknesses and inconsistencies

REVIEW.md items (2026-06-23) and their status in the current JSON:

| REVIEW.md issue | Status now |
| --- | --- |
| Approval workload math missing | **Fixed**: capacity "Approval workload" + `maker-checker` deep dive |
| Payment outbox/reconciler not first-class | **Mostly fixed**: `PaymentOutbox`, `PaymentEvents` nodes, step 5 view and sequence |
| Interview script says "Auto-execute vs escalate" | **Fixed**: now "Auto-route/auto-recommend vs escalate thresholds (never auto-authorize)" |
| Accounting master data not modeled | **Mostly fixed**: `accounting_periods`, `vendor_master`, `entity_id`, `currency`, `coa_version`, `control_policy_version` (but no `tax_code` field) |
| `last_callback_event_id` insufficient | **Fixed**: `payment_events` table |
| Time-sensitive "default to Claude" wording | **Fixed**: now "a managed frontier-model provider or the shared model gateway" |

Residual issues I found:

- **Stale link in step 4 view.** `maker-checker` still uses `ledger-rail` ("Ledger → PaymentRail: release approved payment"). This contradicts step 5's rule that payment goes through the outbox and is "not a direct ledger-to-rail call". The step-4 prose ("post to the GL or release the payment") reinforces the shortcut.
- **Identity broker as executor.** The links `id-ledger` and `id-outbox` make the identity broker the component that posts and enqueues side effects, and the approve API says "the broker accepts the approval and enqueues the side effects". This conflates the authorization decision with side-effect execution. The book should separate a policy decision point / token minter from an executor / tool broker. (The same shortcut appears in LEG and HR — see §4.)
- **Who writes proposals is ambiguous.** Both `extract-proposals` (ExtractAgent → Proposals) and `pipe-proposals` (Pipeline → Proposals) exist. The final design uses only `pipe-proposals`. `extract-sub` gives the LLM node direct read access to sub-ledgers.
- **SoD scope is underspecified.** `proposals.maker` is "agent or analyst". The rule is maker ≠ checker. Nothing says whether the *analyst who initiated the agent's task* (or the agent's operator) may be the checker. A trade-off line mentions "the proposing agent (or its operator)", but the identity rule does not encode it.
- **Batch approval tension.** "One checker decision over a reviewed batch" is efficient, but it risks the rubber-stamp review that HR explicitly warns against ("a *meaningful* human review … is not the same as a rubber-stamp approval click", HR step `naive`). The dataset gives no batch-size limit and no sampling rule.
- **Enum drift.** `payment_events.normalized_transition` lacks `reversed`/`unknown`, which exist in `payment_instructions.status`. The step text's lifecycle omits `reversed`/`unknown` too.
- **Duplicated concept.** "Agent harness … in workflow mode" is defined twice in step `pipeline` (once with `definition`, once with `description`).
- **Capacity diagram shows invariants, not capacity.** `capacityDiagram` is `Correct → Audit → Idem` (the same defect REVIEW flagged for HR, which was fixed there and not here).
- **No compensation story for a settled wrong payment** beyond a reversal proposal. Clawback or recall of a settled payment is out of scope, and the book should say so.

### 1.11 Best uses in the book

- **Foundations:** the propose/mutate split; "agent as maker, never checker"; why accuracy does not justify autonomy.
- **Reference architecture:** a canonical "gated side-effect" back office (staging store → gate → executor → system of record → reconciler → decision record).
- **Orchestration:** the workflow-vs-agent selection rule; harness in workflow mode; typed node contracts.
- **Tools/execution:** idempotent post, payment outbox, query-before-retry, two side effects with two mechanisms.
- **Reliability/recovery:** unknown outcomes, monotonic state, period-lock revalidation, reversal as compensation.
- **Security/oversight:** SoD in identity, injection quarantine at intake, BEC freeze, the model gateway with no posting authority.
- **Evaluation/observability:** ground-truth eval, approval-queue SLOs, reconciliation lag as a safety signal.
- **Performance/economics:** human-checker capacity as the binding constraint; queue absorbs bursts instead of relaxing the gate.

---

## 2. LEG — Agentic Legal Platform

Source: `system-design-interviews/data/book/agentic-legal-platform/interview.json` (+ `REVIEW.md`).

### 2.1 Summary

Legal agents do contract review and redlining, due diligence at scale (tabular extraction across thousands of documents), and cited research memos. The users are supervising attorneys at a firm, the firm's clients (whose matter documents are processed), and, implicitly, courts. Failure means malpractice and lost privilege. The irreversible action is "a finalized or filed work product". The central idea is a **two-stage gate** on a deterministic pipeline (retrieve → draft → verify → attorney review). First comes a **machine citation-verification gate** that checks every citation for *existence, currency, relevance*: "a real-but-overruled citation is worse than a fabricated one". Then comes a **mandatory licensed-attorney gate**: "nothing auto-files". Confidentiality (zero data retention, no-train, ethical walls) "constrains retrieval from the very first read", and every finding carries span-level provenance.

### 2.2 Requirements and capacity (dataset's illustrative assumptions)

Functional: playbook contract review with redlines and rationale; due diligence at scale (tabular extraction); grounded cited memos; "Verify every citation before any draft is surfaced to an attorney"; attorney approval before finalize/file.

Non-functional: hallucination is first-class; every finding traceable to a source span; "zero-data-retention, no-train, tenant segregation, ethical walls, SOC 2"; grounding over Westlaw/Practical Law/KeyCite and matter documents, "not the open web"; deterministic control flow.

| Label | Value | Note (abridged) |
| --- | --- | --- |
| Interactive memos | ~2k matters/day, ~8 cites/memo | p95 first-draft latency < 90 s; ~16k citation verifications/day on the interactive path |
| Diligence batches | ~50 batches/day × 1k–10k docs | ~30 pages × ~700 tokens/page; a 10k-doc batch ≈ 200M input tokens; SLA in hours; resumable |
| Citation verification | every cite, every draft | 1–2 KeyCite/Westlaw calls per cite; "the dominant external bottleneck — cached per (citation, version), batched, and circuit-broken" |
| Peak concurrency | per-matter cap + global token budget | stops one diligence batch starving interactive memos; DLQ on repeated failure |
| Autonomy | draft-only | "a licensed attorney finalizes — nothing auto-files" |

Check: 10k × 30 × 700 = 210M tokens ("~200M" is consistent).

### 2.3 Evolution path

1. **`naive` — An agent that drafts from its own knowledge.** The failure is hallucinated or overruled citations, with no grounding, no provenance, no review, and client data sent to a model that may train on it. Trap: "Trusting a fluent draft because its citations look real."
2. **`grounding` — Ground in authoritative law, not model memory.** Fixes drafting from memory. Two source tracks (deep dive). The authoritative-law track is shared, publisher-versioned, and refreshed on a freshness SLA; its failure mode is **staleness**. The client-matter track (DMS) is tenant- and matter-scoped behind ethical walls; its failure mode is **leakage**. The access policy sits **on the retrieval path**: "a walled document is never retrieved, not merely never shown."
3. **`pipeline` — Deterministic retrieve → draft → verify pipeline.** Fixes the "opaque research loop" that "can skip or defer verification". The DraftStore holds one artifact through statuses (unverified intermediate → `awaiting_review` → finalized) "so a draft in flight is never mistaken for one ready for an attorney". The pipeline runs on the Foundations harness, which is "distinct from the eval harness".
4. **`citation-gate` — Verify every citation.** Fixes "citations were trusted as drafted". Existence and currency are deterministic lookups. Relevance is "model-assisted with a threshold", and "an uncertain middle band [is] a flag, not a pass". A flag sends the draft back through a **correction loop**; each attempt writes evidence (`citation_verifications` row). Repeated failure lands in a human exception queue. Provider handling: cache per (citation, source version) within `freshness_sla`, "force a refresh before finalization", "a stale_served status is never allowed to gate an approval"; 3 attempts with backoff behind a circuit breaker; on outage the draft is held in `verifying`, then `verification_blocked`. Attorney override "never rewrites the machine decision to a pass".
5. **`attorney` — Attorney-in-the-loop.** Fixes "a verified draft could be treated as finished". Review is a workflow (assign, annotate, request changes, approve, reject, second review for high-risk work). Approval is bound to a licensed attorney principal and requires "a license/jurisdiction source (a bar-status check or firm-admin attestation)". Professional responsibility (UPL, ABA Model Rule 5.3) stays with the attorney.
6. **`confidentiality` — Confidentiality and audit-defensible provenance.** ZDR/no-train, tenant segregation, ethical walls; matter documents "partitioned from other tenants and from tool authority"; every sentence traced to a source span and version. Deep dive: **retention differs by artifact, and legal hold overrides it**.
7. **`workflows-eval` — Workflows at scale and evaluation.** Fixes "one task, unmeasured quality". Redlines tie to a version-pinned playbook rule. Diligence batches are resumable per document with a DLQ for poison documents and adjudication of low-confidence cells. **Eval is a release gate**: offline attorney-adjudicated set → shadow eval → production monitoring. A candidate model/retriever/verifier/prompt/corpus version ships only if citation-error and unsupported-finding rates hold at or below baseline. Canary plus holdout, with pinned prior versions for rollback.

### 2.4 Final architecture

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| Supervising Attorney | must review and approve before finalize/file | human gate |
| Matter Documents | contracts, diligence sets, requests — "untrusted, tenant- and matter-scoped" | untrusted input |
| Legal API | authenticates the matter, enforces tenant isolation | ordinary |
| Research / Draft Pipeline | deterministic DAG | **harness in workflow mode** |
| Draft Agent | LLM drafts grounded in retrieved sources with citations | **agent** |
| Inference Backend | shared tier "under no-train terms" | substrate |
| Authoritative Source Index | Westlaw/Practical Law/KeyCite/statutes | retrieval (RAG) |
| Document Mgmt System | iManage/NetDocuments, preserves ACLs and ethical walls | external system of record |
| Citation Verifier | existence, currency, relevance | **agent-specific verifier** |
| Draft Work Product | draft lifecycle by status; never auto-filed | **agent output quarantine** |
| Provenance Store | finding/sentence → source span | agent-specific (grounding evidence) |
| Confidentiality & Policy | tenant isolation, ethical walls, ZDR/no-train, document screening | mixed |
| Identity & Token Broker | scoped delegated matter access; "ties approval to a licensed attorney principal" | delegation |
| Audit Record | sources + versions, citations verified, approval, event IDs | agent-specific content |
| Work Queue | levels intake, carries diligence batches | ordinary |
| Observability & Eval | trajectories, citation-error and hallucination rates | agent-specific |

Key links: `verify-auth` ("existence + currency (KeyCite)"), `verify-draft` ("flagged cite -> correction loop", dashed), `guard-dms` ("ethical-wall access control"), `attorney-id` ("approve (licensed)") → `id-draftstore` ("finalize approved work product").

Agent-specific vs ordinary: the verifier, the correction loop, provenance spans, and eval-as-release-gate are agent-specific. The two-track corpus, caching with freshness, circuit breakers, and resumable batches are ordinary distributed-systems machinery applied to an external authority provider.

### 2.5 Reusable patterns

- **Verify-before-surface gate** (machine check before a human invests trust) — `citation-gate`.
- **Existence / currency / relevance** as a three-axis check on any cited claim — `citation-gate`.
- **Deterministic checks plus scored judgment with an uncertain band that escalates** — `citation-gate` deep dive.
- **Bounded correction loop with evidence per attempt, then a human exception queue** — `citation-gate`.
- **Override is a separate audited decision, never a rewrite of the machine verdict** — `citation-gate`, `attorney`.
- **Access policy on the retrieval path (not at output)** — `grounding`.
- **Two-track corpus with different failure modes** (staleness vs leakage) — `grounding` deep dive.
- **Version-pinned sources for stable spans** — `grounding`, `citation-gate`.
- **Freshness-bounded cache that cannot gate an approval when stale** — `citation-gate` deep dive.
- **Degrade to block/escalate, never skip the check** ("the degraded mode is to block or escalate the draft, not to skip verification", technologyChoices) — `citation-gate`.
- **Split job state and review state** — data model `drafts`.
- **Professional-identity binding** (approver must be a licensed principal; license source required) — `attorney`.
- **Span-level provenance map** — `confidentiality`.
- **Retention matrix by artifact, legal hold overrides deletion** — `confidentiality` deep dive.
- **Provider-call ledger** (`provider_calls`: cache state, status, retries, cost) — `citation-gate`.
- **Resumable batch with per-item checkpoint and poison DLQ** — `workflows-eval`.
- **Per-matter fairness of scheduling** (interactive vs batch) — capacity, `workflows-eval`.
- **Eval as release gate with canary, holdout, pinned rollback** — `workflows-eval`.

### 2.6 Decisions and trade-offs

- **Provider stays the source of truth.** "the platform's index is a scoped, version-pinned retrieval cache, not a substitute for KeyCite or publisher metadata." A managed vector search "does not remove the citation-verification gate".
- **Stale cache is a correctness bug.** "stale good-law status is a correctness bug, not just a latency issue."
- **Workflow engine.** Temporal-like engines suit "long-running correction loops and attorney callbacks". A database-backed state machine "usually grows custom retry, timer, and compensation machinery".
- **Relational store for drafts/citations/review events** "because the invariants are cross-row and audit-facing".
- **Scheduler fairness.** It "must allocate by matter, tenant, and token budget, not only by global worker availability."
- **Provenance vs audit split.** "Provenance is queryable state … Audit is append-only evidence". Analytics stores "must not become the only copy of legally required audit evidence."
- **Identity.** "Relationship-based authorization helps model ethical walls and matter teams." Token brokers keep provider credentials "out of prompts, logs, and worker environments".
- **Eval.** "A promotion gate should fail a model or prompt release on legal-quality regressions, not merely display a dashboard."
- **Retention.** "the harder choice is where redaction, legal hold, tenant deletion, and immutable audit retention are allowed to conflict."
- **Step trade-offs (named):** Fluency vs verifiability; Source breadth vs authority; Retrieval convenience vs ethical walls; Research flexibility vs mandatory verification; Draft velocity vs citation certainty; Deterministic checks vs judged relevance; Automation vs professional responsibility; Model improvement vs zero retention; Provenance overhead vs defensibility; Fluency signals vs citation-error eval; Batch scale vs traceability.

### 2.7 Failure modes and containment

| Failure | Containment | Where |
| --- | --- | --- |
| Fabricated citation | existence check | `citation-gate` |
| Real but overruled citation | currency check via KeyCite; refresh before finalization | `citation-gate` |
| Real, current, but off-point citation | scored relevance; uncertain band flags | `citation-gate` |
| Correction loop spins | attempt counter → human exception queue / DLQ | `citation-gate` |
| Authority provider outage / rate limit | cache, batch, backoff, circuit breaker → hold in `verifying` → `verification_blocked` | `citation-gate` |
| Publisher update changes a finalized cite | pin source version used for verification | `citation-gate` |
| Walled document influences a draft | access check on retrieval path | `grounding` |
| Cross-tenant leakage via model provider | ZDR/no-train terms, tenant segregation | `confidentiality` |
| Injection in opposing-party text | matter docs untrusted, partitioned from tool authority | `confidentiality` |
| Unlicensed or agent principal finalizes | identity rejects non-licensed approver | `attorney` |
| Large diligence batch starves memos | per-matter concurrency cap, priority for interactive work | capacity |
| Poison document in a batch | per-document retry budget → DLQ, batch continues | `workflows-eval` |
| Model/verifier upgrade regresses quality | eval release gate, canary, holdout, rollback | `workflows-eval` |
| Deletion request vs legal hold | hold suspends TTL/deletion; immutable audit survives | `confidentiality` |

### 2.8 Domain constraints

- **Domain-specific:** privilege and ABA Model Rules 1.1 / 1.6 / 5.3, ABA Formal Opinion 512, unauthorized practice of law; citators (KeyCite, Shepard's); ethical walls; jurisdictions; court filing.
- **Broadly applicable:** verifying cited claims against an authoritative source; currency vs existence (stale-but-real is worse than missing); access control at retrieval time; external-authority rate limits; retention differing by artifact; eval as a release gate; interactive vs batch fairness.
- Human roles: supervising attorney (approver, overrider), second reviewer for high-risk work, firm admin (license attestation).
- Data sensitivity: highest of the three for confidentiality (privileged client data, opposing parties); a no-train contractual posture is required.
- Latency: interactive p95 < 90 s for a first draft; diligence in hours. Volume: token-heavy batches (200M tokens per batch).

### 2.9 API and data-model snippets

- `POST /v1/drafts` request: `{ "matterId": "...", "task": "contract_review|diligence|memo", "jurisdiction": "...", "sourceCorpus": ["westlaw","dms"], "playbookId": "...", "outputSchemaId": "...", "reviewAssignee": "...", "idempotencyKey": "...", "docs": [ ] }` → `{ "draftId": "...", "status": "queued" }`.
- `GET /v1/drafts/{id}` response: `{ "jobStatus": "verifying", "reviewStatus": null, "attempt": 1, "citations": { "passed": 6, "flagged": 1, "correcting": 1 }, "batch": { "docsDone": 4200, "docsTotal": 10000, "dlq": 3 } }`. This is a good example of a split lifecycle visible to the caller.
- `POST /v1/drafts/{id}/review` request: `{ "decision": "approve|request_changes|reject|override_cite", "citeId": "... (override only)", "notes": "..." }`.
- `drafts.job_status`: `enum(queued,drafting,verifying,correcting,verification_blocked,awaiting_review,human_exception)`; `drafts.review_status`: `enum(unassigned,assigned,changes_requested,approved,finalized,rejected) null`.
- `citations.blocking_reason`: `enum(missing,overruled,questioned,off_point,low_confidence) null`; `citations.decision`: `enum(machine_pass,machine_flagged,attorney_overridden)`.
- `citation_verifications.relevance_score`: `float (0–1, model-assisted)`; `verifier_version`; `attempt`.
- `provider_calls.cache_state`: `enum(hit,fresh_miss,stale_served,refreshed)`; `status`: `enum(ok,timeout,rate_limited,circuit_open,error)`; `cost`: "metered units / tokens, against per-matter budget".
- `matters.retention_policy`: `enum(zdr,retain_30d,retain_per_engagement)`; `ethical_wall_group`.
- `source_corpora.track`: `enum(authoritative_law,client_matter)`; `freshness_sla interval`.

### 2.10 Weaknesses and inconsistencies

REVIEW.md (2026-06-23) status in the current JSON:

| REVIEW.md issue | Status now |
| --- | --- |
| Lifecycle split across API and data model | **Fixed**: `job_status` + `review_status` split, `verification_blocked`, `human_exception` |
| Parent workflow entities missing | **Fixed**: `playbooks`, `playbook_rules`, `extraction_schemas`, `diligence_batches`, `diligence_documents`, `source_corpora` |
| Provider operations not operationalized | **Fixed**: `provider_calls`, freshness rule, 3 retries, circuit breaker, per-matter budget |
| Eval lacks release-gate semantics | **Fixed**: three-layer eval, gate, canary/holdout/rollback |
| DraftStore semantics unclear | **Fixed**: lifecycle-by-status sentence in step `pipeline` |
| Retention/legal-hold nuance | **Fixed**: deep dive in `confidentiality` |

Residual issues I found:

- **The irreversible action is never modeled.** The description says "finalized or filed work product", but there is no filing connector, no court e-filing outbox, no DMS write-back, and no idempotency on the finalize step. "Finalize" is only a `review_status` value. Compared with FIN's outbox, the legal side effect on the system of record is missing. The book should state that *filing* is the external side effect and needs the same outbox/idempotency treatment.
- **Review endpoint has no idempotency key.** `POST /v1/drafts/{id}/review` lacks one, while FIN's approve endpoint and HR's decide endpoint both have one.
- **Override semantics contradict the schema.** Step `citation-gate` says an override "never rewrites the machine decision to a pass — the citation stays machine-flagged, and the override is a separate, audited attorney-overridden decision". But `citations.decision` is one enum holding `machine_pass | machine_flagged | attorney_overridden`, so writing `attorney_overridden` *does* overwrite `machine_flagged`. The evidence survives only in `citation_verifications` and `review_events`.
- **"Deterministic citation verifier" is a misnomer.** The node description says "Deterministic check", but relevance is model-assisted (the dataset admits the gate gets "a probabilistic component into the gate itself"). Call it a *verifier with deterministic and judged axes*.
- **`approved` vs `finalized` undefined.** Both appear in `review_status` and in the review response. The difference (second review? filing pending?) is never stated.
- **Second review is prose only.** There is no field or state for it (HR has `second_review bool`).
- **No SoD between requester and approver.** The attorney who requested the draft can approve it. That is defensible (supervising-attorney responsibility), but it is a deliberate contrast with FIN's maker ≠ checker and should be named as such.
- **Provenance is one span per finding.** `provenance.finding_id` is the PK, so a finding supported by several sources cannot be represented.
- **Audit tamper evidence is weaker than FIN's.** `audit_events` is "append-only, immutable" with no hash chain. WORM appears only in technologyChoices.
- **Capacity diagram shows invariants** (`Ground → Cite → Prov`), not load.
- **Time-sensitive claim.** "A dated Stanford study reported material hallucination even on grounded legal tools" is correctly hedged in the dataset; keep the hedge.
- **Duplicated concept.** "Agent harness" is defined twice in step `pipeline`.
- **"Memory: short-term vs long-term" label** is attached to grounding in step `grounding`. Grounding over a corpus is retrieval, not agent memory, so the book should not reuse this label.

### 2.11 Best uses in the book

- **Foundations:** "fluency is not correctness"; verify-before-surface; why stale-but-real beats missing as a hazard.
- **Context/memory/state:** two-track corpus, version pinning, freshness SLA, access control on retrieval, the split between provenance and audit.
- **Orchestration:** correction loop with attempt budget; split job/review lifecycle.
- **Reliability/recovery:** external-authority rate limits, circuit breaker that blocks rather than bypasses, resumable batches, DLQ.
- **Security/oversight:** ethical walls, ZDR/no-train, licensed-principal binding, audited override.
- **Evaluation/observability:** eval as release gate (offline → shadow → production, canary + holdout + rollback), task-specific metrics.
- **Performance/economics:** per-matter budgets, provider cost per call, interactive vs batch priority, token math for a diligence batch.
- **Deployment/evolution:** pinned model/verifier/corpus versions for rollback.

---

## 3. HR — Agentic HR Platform

Source: `system-design-interviews/data/book/agentic-hr-platform/interview.json` (+ `REVIEW.md`).

### 3.1 Summary

HR agents do candidate screening and recruiting, the employee helpdesk and policy Q&A, and onboarding/offboarding against the HRIS/ATS (Workday, SuccessFactors, ADP). The users are recruiters and hiring managers (deciders), employees and candidates (data subjects and askers), and compliance auditors. The highest-stakes action is a hiring decision: "legally consequential and hard to reverse". The central ideas are: **agents recommend, humans decide every adverse outcome**, with adverse-impact (four-fifths-rule) monitoring built in; **PII-scoped retrieval**, where "an employee's query can only reach their own record", enforced by scoped tokens rather than prompts; **effective-dated, jurisdiction-tagged policy grounding**; and **durable idempotent HRIS workflows with compensation**. Compliance is named as a source-backed requirement: NYC Local Law 144 (annual bias audit, public posting, candidate notice, "enforced since July 5, 2023") and the EU AI Act (Regulation 2024/1689), where Annex III employment uses are high-risk with staged Article 113 dates.

### 3.2 Requirements and capacity (dataset's illustrative assumptions)

Functional: screen on job-related skills and surface recommendations; answer policy/benefits questions grounded in the policy in force; orchestrate onboarding/offboarding against the HRIS; "Route every adverse hiring outcome to a human decision-maker"; monitor adverse impact.

Non-functional: "score on job-related features only; exclude prohibited signals and proxies; no emotion/biometric inference"; "adverse decisions are never automated"; PII privacy with data residency; effective-dated grounding; LL144 and EU AI Act compliance.

| Label | Value | Note (abridged) |
| --- | --- | --- |
| Candidate screenings | ~5k/day steady, ~25k/day burst (~5x) | queue levels the burst; LLM ~1 call/candidate, "not the hot path" |
| Helpdesk / policy QPS | ~20 QPS steady, ~150 QPS at open enrollment (~7x) | cache hot answers per (jurisdiction, effective-date) |
| Onboarding/offboarding | ~500 workflows/day, ~5–20 HRIS writes each | HRIS throttles ~2–10 writes/sec/tenant → idempotent workflow queue |
| Human review load | ~30% of screenings reach a human (~1.5k/day), ~24h decision SLA | ~50 decisions/reviewer/day ≈ ~30 reviewers |
| Policy corpus | ~50k chunks; daily-to-weekly updates | single managed vector index with metadata filters; superseded versions retained |
| Audit retention | ~3–7 yrs; adverse-impact snapshots per audit cycle | compliance drives retention and legal hold |
| Adverse-impact batch | nightly; min cohort ~30–50 | small cohorts get a low-confidence caveat, not a hard flag |
| Latency / SLA | policy answer p95 ~2–3 s; review queue < 24 h; HRIS ops minutes–hours; adverse-impact freshness ~24 h | "The human review queue, not the LLM, is the binding SLA" |

Check: 5k × 30% = 1.5k; 1.5k ÷ 50 = 30 reviewers. Consistent internally, but see the "who reaches a human" contradiction in §3.10.

### 3.3 Evolution path (5 steps)

1. **`naive` — An agent that screens and rejects.** The agent auto-rejects low scores and answers any question against any data it can reach. Failures: "Automated adverse decisions, possible disparate impact, no fairness audit, and PII leakage." It plants two distinctions for later: *recommendation vs decision*, and "*meaningful* human review (sees feature evidence, records a rationale, can override) is not the same as a rubber-stamp approval click." Trap: auto-reject.
2. **`grounding` — Effective-dated, jurisdiction-tagged policy.** Fixes stale or wrong-jurisdiction answers. The corpus has a lifecycle (ingestion, approval, effective date, supersession, cache/index invalidation). Options: **metadata-filtered shared index (recommended)**, where "filter correctness is now load-bearing"; segmented indexes; single global corpus (rejected). The flow ends with an abstain → open HR case.
3. **`privacy` — PII-scoped retrieval and identity.** Fixes "retrieval could reach any record". Options: **token-scoped service boundary (recommended)**, where "the token simply can't fetch another record"; retrieval-filter enforcement ("A filter bug is a silent cross-record leak"); prompt-only (rejected). Resumes are partitioned from HRIS write authority. The refusal path logs "denied cross-scope attempt".
4. **`hiring-gate` — Humans decide, adverse impact monitored.** Fixes "the agent could decide outcomes and bias went unmeasured". "Operationally the gate is a queue, not a callback": each item carries the versioned rubric, feature evidence, assignment, and SLA. The reviewer records a rationale and may override or recuse. A breached SLA, recusal, or flag escalates to a second reviewer. An adverse decision emits the AEDT candidate notice and can be appealed. Protected attributes live in a separate store that scoring never sees. Options: **pre-decision review queue (recommended)**; thresholded escalation ("must guarantee every *adverse* outcome still routes to a human"); post-hoc review (rejected: "auditing, not a human deciding").
5. **`service-eval` — Service delivery, compliance and evaluation.** Fixes ad hoc service and compliance. The helpdesk deflects and escalates. Onboarding/offboarding becomes a **durable workflow of idempotent HRIS tasks with reconciliation**, tracking reversible vs irreversible tasks (options: workflow queue recommended vs synchronous writes). Compliance evidence is **dated audit runs**, not "a searchable firehose". Eval covers quality (deflection, accuracy) and fairness. Deep dive: "What the market retreated from" — emotion/biometric inference.

### 3.4 Final architecture

| Node | Responsibility | Agent-specific? |
| --- | --- | --- |
| Recruiter / Hiring Mgr | "reviews and decides every adverse outcome" | human gate |
| Employee / Candidate | asker; PII owner | data subject |
| HR Request / HR API | auth, resolves identity scope | ordinary |
| HR Orchestrator | routes screening/helpdesk/onboarding; "deterministic where decisions matter" | **harness** |
| Screening Agent | LLM scores on job-related skills only | **agent** |
| Inference Backend | shared tier | substrate |
| Policy KB | effective-dated, jurisdiction-tagged corpus | retrieval |
| ATS / HRIS | candidate/employee records, "the action surface" | external system of record |
| Adverse-Impact Monitor | selection rates, four-fifths rule | agent-governance (fairness) |
| Hiring Review Gate | "agents recommend, humans decide" | **human gate** |
| PII-Scoped Retrieval | identity-scoped retrieval | agent-specific enforcement point |
| Recommendation Store | pending recommendations | **agent output quarantine** |
| Workflow Engine / HRIS Task Queue / Workflow State | durable idempotent provisioning with reconciliation | ordinary |
| Policy & Privacy (Guardrail) | prohibited-signal exclusion, residency, tenant isolation, untrusted-text screening | mixed |
| Identity & Token Broker | delegated access; binds decisions to a human; enforces PII scope | delegation |
| Audit Record | features used, recommendations, decisions, metrics | agent-specific content |
| Observability & Eval | trajectories, selection-rate dashboards, fairness eval | agent-specific |

Key links: `screen-gate` ("recommendation (skills only)"), `gate-recruiter` ("human decides"), `recruiter-id` → `id-hris` ("write decision / provision"), `id-pii` ("bind scope to principal"), `pii-hris` ("fetch only the requester's record"), `queue-hris` ("throttled write (keyed)"), `hris-wfe` ("callback / reconcile"). Baseline-only links kept in the graph: `screen-hris` ("auto-reject (unsafe baseline)"), `orch-hris` ("synchronous write (baseline)").

### 3.5 Reusable patterns

- **Recommendation vs decision** as separate typed artifacts — `naive`, `hiring-gate`.
- **Meaningful-review contract** (evidence shown, rationale required, override and recusal possible) — `naive`, `hiring-gate`.
- **Gate as a queue with assignment, SLA, escalation, second review, appeal** — `hiring-gate`.
- **Feature allowlist per versioned rubric** (the agent may use only listed job-related features) — data model `job_rubrics`, `hiring-gate`.
- **Feature evidence as provenance** (which snippet supported which feature) — `feature_evidence`.
- **Protected-attribute audit separation** (measure fairness on data the scorer cannot see) — `hiring-gate`.
- **Outcome-distribution monitor** (four-fifths rule, rolling window, small-cohort low-confidence) — `hiring-gate`.
- **Effective-dated, jurisdiction-tagged corpus with supersession and invalidation** — `grounding`.
- **Metadata-filtered shared index where the filter is a correctness boundary** — `grounding`.
- **Abstain → human case** (`/v1/policy-cases`) — `grounding`.
- **Token-scoped data boundary for PII** (scope cannot be widened by the prompt) — `privacy`.
- **Logged denial of cross-scope attempts** — `privacy`.
- **Durable workflow of idempotent tasks with reconciliation against the system of record** (callback, timeout, duplicate, manual edit) — `service-eval`.
- **Reversible/irreversible task flag driving compensation vs manual attention** — `service-eval`, `/v1/workflows/{id}/cancel`.
- **Dated compliance evidence packets** (audit runs per regime, WORM, publication approval, legal hold) — `service-eval`.
- **Auth-derived principal** ("The deciding principal is taken from the auth token (not the body)") — API.

### 3.6 Decisions and trade-offs

- **Shared metadata-filtered index over segmentation.** "Strong metadata filtering makes per-jurisdiction physical index sprawl unnecessary." The cost: "filter enforcement must be treated as a hard correctness requirement."
- **Token-scoped PII boundary over row filters or prompts.** It "makes prompt-level 'only read the requester's record' instructions irrelevant as a security control."
- **Pre-decision queue over thresholded or post-hoc review.** It is the "cleanest audit story for LL144 / EU AI Act".
- **Review store separate from HRIS.** "A first-class review store keeps the HRIS from becoming the pending-decision queue."
- **Durable workflow engine over cron or synchronous calls.** HRIS APIs "throttle, page, duplicate callbacks, and allow manual edits". "A reconciliation adapter lets the HRIS remain the system of record instead of copying employee state into the agent platform."
- **Backpressure shapes differ.** Screening needs "fanout and retry", while HRIS tasks need "leases and idempotent delivery".
- **Fairness analytics as a governed boundary.** "A separate protected-attribute analytics boundary removes the temptation to expose demographic fields to the screening agent."
- **WORM evidence packets** "remove the need to prove compliance from mutable operational database snapshots."
- **Step trade-offs (named):** Screening speed vs legal exposure; Shared index vs physical isolation; Static corpus vs policy lifecycle; Enforcement strength vs infrastructure cost; Candidate latency vs human decision guarantee; Queue liveness vs review rigor; Immediacy vs reliability under rate limits; Generic logging vs dated compliance evidence.

### 3.7 Failure modes and containment

| Failure | Containment | Where |
| --- | --- | --- |
| Automated adverse decision | recommend-only; human decides every adverse outcome | `hiring-gate` |
| Proxy discrimination | feature allowlist, prohibited-signal exclusion, four-fifths monitor | `hiring-gate` |
| Protected attributes leak into scoring | separate access-controlled store, never joined | `hiring-gate` |
| Small cohort produces a spurious flag | min cohort 30–50, `low_confidence` | capacity, `selection_metrics` |
| Rubber-stamp review | rationale required, evidence shown, override and recusal possible | `naive`, `hiring-gate` |
| Review queue stalls | SLA + escalation to second reviewer | `hiring-gate` |
| Conflict of interest | recusal → reassign | `hiring-gate` |
| Stale policy after midnight change | effective dating + invalidation (asked as a drill; answer only partly given) | `grounding`, followUps |
| Wrong-jurisdiction answer | jurisdiction filter; filter correctness is load-bearing | `grounding` |
| No in-force policy / low confidence | abstain → HR case | `grounding`, `/v1/policy-cases` |
| Cross-employee PII access / injected request for another record | token cannot widen scope; refusal logged | `privacy` |
| Injected resume alters records | inputs partitioned from HRIS write authority | `privacy` |
| HRIS write times out after succeeding | idempotency key + reconciliation read | `service-eval`, followUps |
| Duplicate webhook / manual HRIS edit | `workflow_reconciliation_events` | `service-eval` |
| Cancelled onboarding half done | compensate reversible tasks, flag irreversible ones manual | `/v1/workflows/{id}/cancel` |
| Regulator asks for evidence | dated `audit_runs` packets | `service-eval` |

### 3.8 Domain constraints

- **Domain-specific:** NYC LL144 (AEDT bias audit, public posting, candidate notice), EU AI Act Annex III high-risk employment uses, 29 CFR 1607.4 (four-fifths rule), EEO data, jurisdiction-specific leave and benefits, emotion/biometric inference restrictions.
- **Broadly applicable:** separating recommendation from decision; making human review meaningful rather than ceremonial; measuring outcome distributions on data the agent cannot see; enforcing identity-scoped retrieval below the prompt; effective dating of knowledge; reconciliation against an external system of record that humans also edit; compliance evidence as dated packets.
- Human roles: recruiter/hiring manager (decider), second reviewer/supervisor (escalation), HR case owner (abstain path), candidate (notice, appeal).
- Data sensitivity: very high and personal (pay, benefits, demographics); residency per record; legal basis for protected attributes.
- Latency: interactive helpdesk p95 2–3 s (the only tight-latency path in this group); hiring within 24 h. Volume: moderate, bursty.

### 3.9 API and data-model snippets

- `POST /v1/screenings` response: `{ "screeningId": "...", "recommendation": "advance|reject", "reviewState": "awaiting_assignment", "status": "awaiting_human_decision" }`. The description says it returns "a recommendation for human review — never a decision", and "the tenant is derived from the auth token, not the body".
- `POST /v1/screenings/{id}/decide` request: `{ "decision": "advance|reject|override", "rationale": "...", "recused": false, "decisionIdempotencyKey": "..." }` → `{ "status": "recorded", "decidedBy": "<auth-principal>", "auditCorrelationId": "...", "noticeSentAt": "...|null", "appealStatus": "none" }`.
- `POST /v1/policy-answers` request `{ "question": "..." }` "(identity & jurisdiction resolved from the auth token, not the body)"; the response carries `citations: [ { "policyId", "version", "effectiveDate": "2026-01-01", "jurisdiction": "US-CA" } ]`, `confidence`, and `escalatedTo`.
- `POST /v1/workflows/{id}/cancel` response: `{ "workflowId": "...", "state": "cancelled|needs_attention", "compensated": [ "taskId" ], "manual": [ "taskId" ] }`. This is the cleanest compensation snippet in the group.
- `job_rubrics.feature_allowlist`: `jsonb (job-related features only)`; `feature_evidence.feature`: `varchar (must be in feature_allowlist)`.
- `protected_attribute_audit_data`: note "kept ONLY for fairness auditing, never exposed to scoring features"; fields `source` (`self-declared, EEO form, inferred`), `legal_basis` (`consent / regulatory`), `retention_expires_at`.
- `workflow_tasks.reversible`: `bool (compensation possible?)`; `state`: `enum(queued,sent,confirmed,failed,reconciling,compensated)`.
- `workflow_reconciliation_events.kind`: `enum(callback,timeout,duplicate,manual_edit,exception)`; `resolution`: `enum(matched,retried,compensated,escalated)`.
- `audit_runs.regime`: `enum(ll144,eu_ai_act,internal)`; `artifact_uri` "(WORM/object-lock evidence packet)"; `legal_hold bool`.
- Four-fifths concept example: "If group A is selected at 50% and group B at 30%, the ratio 0.6 < 0.8 is flagged."

### 3.10 Weaknesses and inconsistencies

REVIEW.md (2026-06-24) status in the current JSON:

| REVIEW.md issue | Status now |
| --- | --- |
| Durable workflow not first-class | **Fixed**: `WorkflowEngine`, `WorkflowQueue`, `WorkflowStore` nodes; `workflow_runs`/`tasks`/`reconciliation_events`; step 5 sequence |
| Review-queue contract thin | **Fixed**: `review_assignments`, `review_state`, SLA, escalation, `decisionIdempotencyKey`, notice/appeal, `/v1/reviews/{id}/escalate` |
| Tenant/residency/retention metadata uneven | **Fixed**: tenant/residency/locale/legal_basis added across tables |
| Non-hiring sequence flows missing | **Fixed**: flows in `grounding`, `privacy`, `service-eval` |
| Capacity diagram is a constraint diagram | **Fixed** (HR only), but its label `Reviewers ~30/day ~24h SLA` is wrong: it is ~30 reviewers, not 30/day |
| Step 5 overloaded (split suggested) | **Not done**: still 5 steps; compliance, helpdesk, onboarding, and eval share one step |

Residual issues I found:

- **Who reaches a human? (the main contradiction).** The requirements say humans decide "every adverse hiring outcome". The chosen option says the design "routes every recommendation through a pre-decision review queue". The hiring-gate sequence has an `advance` branch where the human "confirms". Yet capacity says "~30% of screenings reach a human (~1.5k/day)". These cannot all hold. Either ~70% of outcomes (advances? clear rejects?) apply without a human, which is the *thresholded escalation* option the step rejected, or the reviewer math is off by ~3x (5k/day ÷ 50 ≈ 100 reviewers, 500 at burst). The book must pick one semantic. FIN resolves the same tension explicitly ("auto-routed, never auto-authorized" plus batch approval).
- **Hiring decision write bypasses the workflow machinery.** The `hiring-gate` sequence has `Recruiter → HRIS: apply decision (idempotent)`, a direct, synchronous write by a human actor. The architecture instead has `Identity → HRIS` (`id-hris`), and onboarding writes go through the throttled `WorkflowQueue`. Decision writes to the ATS do not, despite the stated 2–10 writes/sec/tenant throttle.
- **Identity broker as executor** again (`id-hris` "write decision / provision").
- **PII scope used for non-PII policy retrieval.** The policy-answer flows route `Identity → PIIScope → PolicyKB`. Policy documents are tenant/jurisdiction-scoped, not personal data, so the component conflates *subject scoping* (PII) with *applicability scoping* (jurisdiction, effective date).
- **Abstain path goes to the wrong gate.** In the `grounding` sequence, the abstain branch is `Inference → DecisionGate: abstain -> open HR case`. `DecisionGate` is the *hiring* review gate. The API has a separate `/v1/policy-cases`, but the architecture has no case-management node.
- **"Inferred" protected attributes.** `protected_attribute_audit_data.source` allows `inferred`. Inferring demographics is itself a sensitive processing activity (and sits awkwardly next to "no emotion/biometric inference"). The dataset does not discuss it.
- **Compensation gaps.** `hris_operations.state` lacks `compensated`, which `workflow_tasks.state` has. `appeal_status` can be `reversed`, but there is no compensating workflow for a reversed rejection (re-open the candidate, retract the notice). There is no appeal API.
- **No intake quarantine for resumes.** Resumes are "treated as untrusted input" and partitioned from write authority, but there is no screening stage like FIN's quarantine or LEG's "document screening".
- **Audit tamper evidence.** `audit_record` is append-only with no hash chain; WORM applies only to `audit_runs` packets.
- **Control flow is less deterministic than FIN/LEG.** The orchestrator is "deterministic where decisions matter", and the helpdesk path is a free LLM answer. The "Workflow vs agent" concept is attached to step `naive`, not developed.
- **Time-sensitive regulation.** The LL144 enforcement date and EU AI Act Article 113 staging are dated facts. Re-verify them before the book cites them, and label them as of the dataset's date.
- **Duplicated concept / mislabeled memory.** "Agent harness" is defined twice in step `naive`. "Memory: short-term vs long-term" is attached to policy grounding (same mislabel as LEG).
- **SoD absent.** Nothing prevents the recruiter who owns the requisition from being the sole decider. Recusal is self-declared (`recused bool` in the request body).

### 3.11 Best uses in the book

- **Foundations:** recommendation vs decision; meaningful vs rubber-stamp review; "the human queue, not the LLM, is the binding SLA".
- **Context/memory/state:** effective-dated, jurisdiction-tagged corpus with supersession; the filter as a correctness boundary; the midnight-policy-change drill.
- **Tools/execution:** durable idempotent HRIS workflow, reconciliation with manual edits, a reversible flag driving compensation vs manual handling, the cancel API.
- **Reliability/recovery:** compensation semantics; "reconciling" as an honest eventual-consistency state.
- **Security/oversight:** token-scoped PII boundary vs filter vs prompt (three-option comparison); protected-attribute separation; auth-derived principals; logged denials.
- **Evaluation/observability:** fairness monitoring (four-fifths rule, cohort thresholds) as a distinct eval family next to quality; dated compliance packets.
- **Performance/economics:** reviewer staffing math; open-enrollment caching per (jurisdiction, effective-date).

---

## 4. Cross-source synthesis

### 4.1 Recurring patterns and each source's name for them

| Pattern (book name proposal) | FIN | LEG | HR |
| --- | --- | --- | --- |
| **Staging store for agent output** (agent output is a pending artifact, never the system of record) | `Proposals` "Proposed Journals" ("propose, don't mutate") | `DraftStore` "Draft Work Product" (draft-only) | `ReviewStore` "Recommendation Store" (recommend-only) |
| **Human approval gate before the consequential effect** | maker-checker / "The Gate" | attorney-in-the-loop / "The Gate, Part Two" | "Hiring Review Gate" / humans decide |
| **Machine gate before the human gate** | deterministic controls + match engine + fraud checks | citation verifier (existence/currency/relevance) | prohibited-signal exclusion + feature allowlist (weak; no blocking verifier) |
| **Identity binds the approver** | broker enforces maker ≠ checker | broker requires a licensed attorney principal | broker binds decision to a human principal from the auth token |
| **Delegation, not impersonation** | "scoped, delegated authority for postings/payments" | "scoped, delegated matter access" | "scoped, delegated token (act claim, row filter)" |
| **Deterministic control flow with LLM in bounded nodes** | "Deterministic Pipeline … not an autonomous loop" | "Deterministic DAG: retrieve -> draft -> verify -> attorney review" | "deterministic where decisions matter" (weakest) |
| **Untrusted-input partition** (documents can't reach authority) | intake quarantine + injection screening | matter docs "partitioned from other tenants and from tool authority" | resumes "partitioned from HRIS write authority" |
| **Idempotent side effect + reconciliation with the external system** | idempotent GL post + payment outbox + callback reconciler | (missing for filing) | durable workflow of idempotent HRIS tasks + reconciliation events |
| **Compensation** | reversal proposal ("a correction is a new … proposal, never an edit") | none modeled (override, request_changes only before finalize) | compensate reversible tasks; irreversible → manual |
| **Audit artifact** | "Immutable Decision Record" (hash-chained, WORM) | "Audit Record" + separate Provenance Store | "Audit Record" + dated `audit_runs` packets |
| **Raw reasoning kept apart from audit** | explicit, stricter retention | "Keep raw model traces in a separate, access-controlled store under the same ZDR/no-train terms" | "Keep raw inputs and model traces access-controlled and residency-aware" |
| **Versioned rules/knowledge in evidence** | `coa_version`, `control_policy_version` | `verifier_version`, pinned `source_version`, playbook `version` | `rubric_version`, policy `version` + effective dates |
| **Risk-tiered routing that never bypasses the gate** | "auto-routed and auto-recommended, never auto-authorized" | second review for high-risk work | priority + second review + escalation |
| **Queue as backpressure for the human gate** | "it never auto-posts to clear backlog" | per-matter caps; interactive before batch | SLA + escalation; queue sized to reviewer throughput |
| **Domain eval against expert ground truth** | ground-truth bookings, miscoding rate | attorney ground truth, citation-error rate, release gate | answer accuracy + selection-rate fairness |
| **Harness in workflow mode** | "Agent harness in workflow mode" | "Agent harness (runtime scaffold)" | "Agent harness (runtime scaffold)" |

Shared concept tags appear verbatim in all three ("Bounded autonomy (agent + deterministic gate)", "Human-in-the-loop approval (gate)", "Delegation not impersonation (OAuth token exchange, act claim)", "Workflow vs agent (deterministic pipeline vs probabilistic loop)", "Prompt-injection defense (CaMeL / Dual-LLM / Plan-then-Execute)", "LLM-as-judge / trajectory evaluation", "Queue-based load leveling; admission control"). They come from a common pattern catalogue in Agentic Platform Foundations, so the book can treat them as one vocabulary.

### 4.2 Where the sources disagree (must reconcile)

1. **What "the gate" guarantees.**
   - FIN: *every* mutation needs a distinct human checker; thresholds only route.
   - LEG: every finalize needs a licensed attorney, and the machine gate can be **overridden** by the human.
   - HR: humans decide every *adverse* outcome, which leaves room for non-adverse outcomes to apply automatically; its own capacity number (30% reach a human) suggests exactly that.
   - Book proposal: name three gate semantics explicitly — *all-effects gate* (FIN), *finalize gate with overridable machine pre-check* (LEG), *adverse-outcome gate* (HR) — and state what each lets through.
2. **SoD.** FIN enforces maker ≠ checker in identity. LEG and HR have no SoD; the requester or requisition owner can approve. LEG's absence is defensible by professional responsibility; HR's is a gap (self-declared recusal only).
3. **Batch vs meaningful review.** FIN allows one decision over a batch of clean items. HR insists review is "meaningful", not a "rubber-stamp approval click". The book needs a rule: batch approval is acceptable only with per-item records, bounded batch size, sampling, and only for items the machine gate classed clean.
4. **Override semantics.** LEG allows an audited human override of a machine flag. FIN has no override of the deterministic controls (only escalation). HR's `override` means the human overriding the agent's *recommendation*, which is a different thing under the same word. Use distinct terms: *override a machine control* vs *disagree with a recommendation*.
5. **Who executes the side effect.** All three draw the identity broker as the executor (`id-ledger`/`id-outbox`, `id-draftstore`, `id-hris`). FIN's own outbox and HR's workflow engine show the better shape: identity authorizes and mints a scoped token; a separate executor/outbox performs the side effect idempotently. The book should fix this uniformly.
6. **Idempotency coverage.** FIN keys intake, proposal, post, payment, and callbacks. HR keys screening, decision, workflow start, and each HRIS operation. LEG keys draft creation only; review/finalize is unkeyed and filing is unmodeled.
7. **Audit strength.** FIN: hash chain + WORM for every event. LEG: append-only, no chain. HR: append-only stream + WORM only for periodic packets. Pick one baseline (hash-chained append-only + WORM) and treat the periodic packet (HR) as an additional derived artifact.
8. **Determinism claims.** FIN calls the match engine deterministic, and it is. LEG calls the verifier deterministic while one axis is model-judged. HR's orchestrator is only "deterministic where decisions matter". Use "deterministic control flow" for the DAG and say plainly which *checks* are probabilistic.
9. **"Memory" label.** LEG and HR tag corpus grounding as "Memory: short-term vs long-term". Grounding over an authoritative corpus is retrieval with provenance; the book should keep memory (agent-written, expiring state) separate.
10. **Lifecycle shapes.** FIN uses one `status` enum for proposals plus a separate payment state machine. LEG splits `job_status` and `review_status`. HR splits `review_state` and `status`. The LEG split (pipeline lifecycle vs human decision lifecycle) is the cleanest general model; FIN's single enum mixes them (`exception`, `awaiting_approval`, `posting`).

### 4.3 Sharpest domain contrasts

| Dimension | FIN | LEG | HR |
| --- | --- | --- | --- |
| Consequence of failure | money lost / misstated books; personal CFO liability; SOX | malpractice, privilege breach, court sanction | discrimination liability, regulatory enforcement, harm to candidates |
| Reversibility | settled payment effectively irreversible; GL corrected only by reversal entries | filed work product irreversible; drafts freely revisable | rejection "hard to reverse" (appeal exists); onboarding tasks mixed reversible/irreversible |
| What the agent produces | proposed journal / payment instruction | draft memo / redline / diligence cell | recommendation / policy answer / workflow tasks |
| Required human control | distinct checker for every effect; dual for high-risk | licensed attorney for every finalize; second review for high-risk | human for every adverse outcome; second reviewer on flag/SLA/recusal |
| Machine pre-gate | strong, deterministic (match, controls, fraud) | strong, mixed (deterministic + judged relevance) | weak (allowlist + exclusion; fairness measured after the fact, in aggregate) |
| Correctness reference | ledger and bank feeds (ground truth exists) | authoritative law (exists but changes: currency) | policy in force (exists, effective-dated); for hiring, **no ground truth**, only distributional fairness |
| Data sensitivity | financial and banking data; fraud target | privileged, multi-party, ethical walls; strictest contractual no-train | personal and demographic data; residency; legal basis per attribute |
| Latency | hours (approval SLA) | < 90 s p95 interactive draft; hours for batches | 2–3 s p95 helpdesk; 24 h hiring decision |
| Volume | ~45k items/day, 10x month-end | ~2k memos + ~50 batches (up to 10k docs) / day; token-heavy | ~5k screenings/day (25k burst), 150 QPS peak helpdesk |
| Binding bottleneck | checker capacity | external citator rate limits | reviewer queue (24 h SLA) and HRIS write throttle |
| Characteristic attack | BEC vendor bank change; injected invoice | injected opposing-party text; cross-matter leakage | proxy features; prompt-injected cross-record PII request |

Three contrasts the book should foreground:

- **Ground truth exists (FIN) → exists but decays (LEG) → is distributional only (HR).** This explains why FIN can verify per item, LEG must verify per item *and* for currency, and HR can only monitor in aggregate (four-fifths) and must put a human on each adverse outcome.
- **The machine gate weakens as the human gate's meaning strengthens.** FIN has the strongest automated controls and the most mechanical human role (checker, batch-approvable). HR has the weakest automated pre-check and insists on the most deliberative human role (rationale, recusal, appeal).
- **The side effect lands on someone else's system of record in all three** (ERP/GL and rails, DMS/court, HRIS/ATS), and all three say "integrate, don't own". Only FIN and HR model the integration as idempotent execution plus reconciliation; LEG leaves the final side effect implicit.

### 4.4 Candidate book-level abstractions distilled from this group

1. **Staging store + gate + executor + reconciler + decision record.** This is the common back-office spine. The agent writes to staging; gates (machine, then human) authorize; an executor performs an idempotent side effect on the external system of record; a reconciler resolves unknown or async outcomes; every step appends to the decision record.
2. **Authorize ≠ execute.** Identity/PDP mints scoped authority; a separate executor holds the idempotency key and talks to the external system.
3. **Two side-effect mechanisms**: a transactional write (one idempotent call) vs an asynchronous external effect (outbox + callbacks + query-before-retry).
4. **Compensation is domain-shaped.** FIN uses reversal entries (append, never edit). HR compensates reversible tasks and routes irreversible ones to humans. LEG has nothing after filing, so the gate must sit before it.
5. **Decision record ≠ reasoning trace.** Curated, versioned, hash-chained evidence vs access-controlled, shorter-retention raw traces.
6. **Meaningful review contract.** Evidence shown, rationale recorded, override possible, SLA and escalation, separation of duties where the domain demands it.
7. **Gate capacity is a design input.** Every source sizes the human queue (20, unstated, and 30 reviewers). Backlog policy is "hold, escalate, add capacity — never auto-authorize".
8. **Scope enforcement below the prompt.** Tokens and retrieval-path policy (ethical walls, PII scope), never prompt instructions.

---

## 5. Quick index of exact source locations for likely chapter citations

- Propose-only: `agentic-finance-platform/interview.json`, step 2 (`ledger`).
- Workflow-vs-agent selection rule: FIN step 3 (`pipeline`); LEG step 3 (`pipeline`).
- Maker ≠ checker in identity: FIN step 4 (`maker-checker`), trap and sequence.
- Checker capacity math: FIN `capacity[3]`, step 4 deep dive.
- Two side effects / payment outbox / query-before-retry: FIN step 5 (`idempotency`), `api[1]`, `api[2]`, `dataModel` `payment_instructions`, `payment_events`.
- Decision record vs reasoning: FIN step 6 (`decision-record`).
- "Auto-routed, never auto-authorized": FIN step 7 (`exceptions`).
- Existence / currency / relevance: LEG step 4 (`citation-gate`).
- Override never rewrites machine decision: LEG step 4 description (contrast with `dataModel` `citations.decision`).
- Access on the retrieval path / two corpus tracks: LEG step 2 (`grounding`).
- Retention matrix + legal hold: LEG step 6 (`confidentiality`) deep dive.
- Eval as release gate: LEG step 7 (`workflows-eval`) deep dive.
- Recommendation vs decision; meaningful review: HR step 1 (`naive`).
- Token-scoped PII boundary (three options): HR step 3 (`privacy`).
- Review queue with SLA/recusal/appeal; protected-attribute separation; four-fifths: HR step 4 (`hiring-gate`).
- Durable HRIS workflow + compensation: HR step 5 (`service-eval`), `api` `/v1/workflows/{id}/cancel`, `dataModel` `workflow_tasks`, `workflow_reconciliation_events`.
- Dated compliance evidence packets: HR step 5 traps, `dataModel` `audit_runs`.
