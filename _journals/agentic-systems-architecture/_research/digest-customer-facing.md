# Digest — customer-facing group (support, sales, marketing)

Group: `customer-facing`. Digested 28 Oct 2026 for **Architecting Agentic Systems**.

**Provenance.** All three sources are design exercises from the author's system-design interview project. They are proposed architectures, not descriptions of deployed systems. Every number below is an illustrative assumption from the dataset, not a measurement. In the book, cite them as *design examples from the author's system-design interview project*, with the path and step, for example `system-design-interviews/data/book/agentic-support-platform/interview.json, step action-gate`.

**Source paths** (all under `/Users/zeljkoobrenovic/PycharmProjects/system-design-interviews/data/book/`):

| Short name | interview.json | REVIEW.md |
| --- | --- | --- |
| SUPPORT | `agentic-support-platform/interview.json` | `agentic-support-platform/REVIEW.md` (dated 2026-06-24) |
| SALES | `agentic-sales-platform/interview.json` | `agentic-sales-platform/REVIEW.md` (dated 2026-06-24) |
| MARKETING | `agentic-marketing-platform/interview.json` | `agentic-marketing-platform/REVIEW.md` (dated 2026-06-24) |

Citation convention in this digest: `SUPPORT step:action-gate` means `system-design-interviews/data/book/agentic-support-platform/interview.json`, the entry in `steps[]` whose `id` is `action-gate`. Field paths such as `SUPPORT dataModel.action_proposals` or `SALES capacity["Send volume vs inbox caps"]` point at the top-level keys of the same file.

**Review staleness (important).** All three REVIEW.md files are older than the current JSON. Most of their "highest-impact issues" have since been fixed in the JSON (details in each §10). Do not quote a REVIEW.md complaint as a current defect without checking the JSON. The reviews also refer to a top-level `patterns` key. That key no longer exists: patterns now live as per-step `concepts[]` entries.

---

# 1. SUPPORT — Agentic Support Platform

## 1.1 Summary

The platform runs customer-support agents that answer questions and also take **transactional actions on the customer's account** (refund, cancel, reschedule, address change) while the conversation is live, handing off to a human when needed. Users are customers on chat, voice and messaging channels, plus human support agents who approve risky actions and take escalations. Failure means money moves wrongly (a double refund, an unearned payout), an irreversible account change (closure, a change to a shipped order), account takeover through social engineering, or a customer who is stranded by a bot that deflects but never resolves. The central idea is stated in `SUPPORT description`: "every other vertical gates BEFORE an async action, but support gates INSIDE a live loop under a turn-taking latency budget." An **in-loop action gate** classifies each proposed action by reversibility and risk: auto-execute, human approval, or escalate. Side effects are made safe by provider-scoped idempotency, reconciliation and compensation.

## 1.2 Requirements and capacity (the dataset's illustrative assumptions)

Functional (`SUPPORT requirements.functional`): real-time conversation across chat, voice and messaging; answers grounded in product/policy docs **and** the customer's scoped account/order record; transactional actions within the conversation; a per-turn decision to deflect, act or escalate; human handoff with full context.

Non-functional (`SUPPORT requirements.nonFunctional`), quoted:
- "Real-time: each turn must respond within a latency budget; the gate runs inside the loop, not before it."
- "Transactional side effects use provider-scoped idempotency (effectively-once with reconciliation); reversal is by compensation where possible, manual repair where not."
- "Higher-risk / less-reversible actions require human approval; low-risk reversible ones can auto-execute."
- "Act only with scoped, delegated authority; customer input is untrusted."

Capacity (`SUPPORT capacity`):

| Item | Value | Note (abridged) |
| --- | --- | --- |
| Active load | ~50k concurrent conversations | ~2 active turns/min/conversation gives ~1.7k turns/sec at peak; mostly chat, with a smaller voice tail |
| Action mix | ~15% of turns propose an action | of those: ~70% low-risk auto, ~20% need human approval, ~10% escalate |
| Retrieval fan-out | 1 + 1–2 reads | one KB search plus 1–2 account reads, run in parallel under the turn deadline |
| Turn latency | text p95 < 2.5 s | first token streamed < 800 ms; voice uses partial verbal responses and async action status |
| Provider limits | QPS-capped | commerce/payment systems have stricter QPS than the chat front end, so back-pressure and circuit breakers |
| Audit volume | ~5–10 events/turn | retention 1–7 years by tenant policy |
| Side effects | effectively-once | idempotency keys, reconciliation by lookup or webhook, manual repair queue |

Derived sizing (`SUPPORT step:live-loop`, deep dive "What the capacity numbers imply for sizing each bottleneck"): ~50 approvals/sec at peak are "a staffed queue with its own SLA". Audit runs at ~8.5–17k events/sec, "roughly tens of TB/year", partitioned by tenant and time and "never on the synchronous turn path". Inference has "a smaller/faster fallback model and a queue-depth alarm that triggers shedding before p95 first-token blows."

## 1.3 Evolution path (one failure at a time)

| # | Step id / title | Failure it fixes | New risk it exposes (`recap.newRisk`) |
| --- | --- | --- | --- |
| 1 | `naive` — "A Bot That Answers But Can't Act" | baseline: the bot deflects every real task to a human; the opposite extreme (free live action) is worse | "It can't resolve anything that needs an action, and a naive 'let it act' version would act live with no controls." |
| 2 | `grounding` — "Ground in Policy + the Customer's Account" | generic answers; a reply that is right by policy but wrong for this order | grounded answers must still arrive within a conversational latency budget |
| 3 | `live-loop` — "The Real-Time Loop & Latency Budget" | answers had no time bound; the session did not survive a restart | the agent must now take real account actions safely inside the loop |
| 4 | `action-gate` — "Take Actions Inside the Loop, by Reversibility" | the agent could only talk, or would act without control | live actions can fail mid-flight, so they must be idempotent and reversible |
| 5 | `txn-safety` — "Transactional Safety: Idempotency & Rollback" | a retried or failed action could apply twice | some conversations still need a human, and the handoff must carry context |
| 6 | `escalation` — "Deflect-vs-Escalate & Human Handoff" | the agent either resolved or dead-ended | quality, compliance and reputation must be measured across live conversations |
| 7 | `compliance-eval` — "Compliance, Audit & Evaluation" | only CSAT was measured | "Policy, model, and provider changes can silently shift action correctness, so evals must gate every gate-policy rollout and trigger rollback when correctness drops." |

## 1.4 Final architecture

Nodes (`SUPPORT highLevelArchitecture.nodes`), grouped by the dataset's `types`:

- **Real-Time Loop** (`live-loop`): `ConvAgent` (Conversation Agent, orchestrator: "Drives the real-time turn loop: understand, retrieve, decide deflect/act/escalate"), `Inference` (shared low-latency LLM tier from Foundations), `KB` (Product/Policy KB, the grounding corpus).
- **In-Loop Action Gate** (`action-gate`): `ActionGate` ("Classifies an action by reversibility/risk and decides auto-execute, approve, or escalate — inside the live turn"), `TxnEngine` (refunds, cancels and reschedules with provider-scoped idempotency, reconciliation and compensation), `Agent2` (Human Agent), `Identity` (Identity & Token Broker: "Scoped, delegated authority to act on the customer's behalf").
- **State & Audit** (`ops`): `SessionStore` ("Live conversation state plus a durable log so an action resumes without duplicating a committed side effect"), `Guardrail` (entitlement/policy checks, PII handling, screening of untrusted input), `AuditLog` (append-only).
- Boundary and other nodes: `Customer`, `Channel`, `Gateway` (Support API: authenticates the session and **resolves customer scope** before routing), `Account` (external account/order record), `Payments`, `Escalation` (router), `Observability` (trajectories, latency/CSAT/resolution, deflection and action-correctness eval).

Key links: `gw-conv` "route (customer scope)"; `conv-gate` "classify action risk"; `gate-txn` "auto-execute low-risk"; `gate-agent` "high-risk -> approve"; `agent-id` "authorize action"; `id-acct` "scoped on-behalf-of action"; `txn-session` "idempotent + compensating log"; `esc-agent` "handoff with context".

**Agent-specific vs ordinary machinery.**
- Agent-specific: the conversation agent on the Foundations harness, two-sided grounding with evidence, the reversibility-tiered gate (including a learned risk score that may only *lower* autonomy), untrusted-input partitioning, the action-bound delegated token, the read-only agent after handoff, and action-correctness eval.
- Ordinary distributed systems: the WebSocket/SSE gateway, admission control, a durable session store, idempotency keys, outbox and saga, circuit breakers, queue routing with SLA, hash-chained audit, tiered storage.

The design says plainly that it consumes the harness rather than rebuilding it (`SUPPORT step:live-loop`): "this platform adds the latency budget and in-loop action gate on top of that harness rather than rebuilding the loop."

## 1.5 Reusable patterns

| Pattern (noun phrase) | Where | Note |
| --- | --- | --- |
| Two-sided grounding with evidence versions (policy truth + account truth) | step:grounding | KB version, source doc IDs and account snapshot version are recorded per turn (`dataModel.knowledge_sources`) |
| Scope resolved before the first read | step:grounding | "the Gateway resolves scope before any account read" |
| Freshness by data class | step:grounding deep dive | policy is cached by KB version; account state "re-reads the live record before acting" |
| Deadline-bounded parallel retrieval with an honest fallback reply | step:live-loop flow | the `alt` branch streams an "I'm checking that" fallback and sets `status=timed_out` |
| Channel-specific degradation | step:live-loop deep dive | text streams; "Voice can't hold silence"; async messaging finishes out of band |
| Reversibility-tiered in-loop action gate | step:action-gate | resend receipt → auto; $1,500 refund → approval; close account → escalate |
| Learned risk score that can only lower autonomy | step:action-gate options | "it can lower autonomy but never raise it past policy" |
| Approval bound to action, resource, amount, policy version and approver | step:action-gate | "a customer message can request an action but can never approve a policy bypass" |
| Action-bound delegated token minted after the gate | step:action-gate; `dataModel.delegated_token_grants` | "can't be reused for a different action"; `revocation_state` active/used/expired/revoked |
| Fraud signals as autonomy reducers | step:action-gate deep dive | proofing challenge, lower tier, fraud queue |
| Idempotency is not reversibility | step:txn-safety | three classes: reversible / compensatable / not safely reversible |
| Reconcile before retry; manual-repair queue for unknown outcomes | step:txn-safety flow | `unknown_external_state -> manual_repair` |
| Compensation as a new forward action, never a mutation | step:txn-safety deep dive | "the audit chain shows refund -> compensation, not a rewritten history" |
| Escalation as a first-class outcome | step:escalation | "like abstention in the healthcare vertical" |
| Read-only agent after handoff | step:escalation deep dive | "Identity won't mint a scoped token while a handoff is open" |
| Proposal expiry that never executes silently | step:escalation deep dive | an unapproved proposal "is dropped, not silently executed" |
| Context package by pointer, not by copy | technologyChoices "Human approval, routing, and handoff queue" | "point to transcript, account snapshot, evidence … rather than copying uncontrolled blobs" |
| Hash-chained, correlated audit | step:compliance-eval; `dataModel.audit_record.prev_hash` | correlation IDs chain turn → proposal → approval → transaction → compensation → handoff |
| Risk-tiered QA sampling with incident-triggered quarantine | step:compliance-eval options | default option |
| Autonomy kill switch per action class | step:compliance-eval deep dive "Incident response" | detect → contain → roll back → repair → stay read-only |

## 1.6 Decisions and trade-offs

- **Deflection vs resolution** (step:naive). Both extremes are rejected; the design builds an agent that acts "only on a scoped account, within a latency budget, and behind an in-loop gate."
- **Policy truth vs account truth** (step:grounding). Every turn pays for two-sided retrieval to make replies traceable. When they disagree, "the account state wins."
- **Turn latency vs thoroughness** (step:live-loop). The harness runs under an explicit per-turn budget. The REVIEW (§5) asked for options here: synchronous action in the turn vs streamed reply plus async status vs forced human pause. **No options were added for this step.** It remains the one step whose central trade-off is not branched.
- **Rule auditability vs learned nuance** (step:action-gate). The chosen default is deterministic policy-rule tiers; a learned classifier may be added later, clamped. technologyChoices "Action gate, policy engine…": "Learned risk scores can rank or lower autonomy, but deterministic policy must be the final allow/approve/escalate decision for side effects." Options listed: OPA, Cedar, Drools, OpenFGA, AWS Verified Permissions.
- **Live autonomy vs mid-conversation approval** (step:action-gate). Only "the dangerous tail waits."
- **Provider dedupe vs local outbox vs saga** (step:txn-safety options). Chosen: provider idempotency plus reconciliation lookup. The outbox is a full alternative (the customer sees "action in progress"). The saga is reserved for multi-step resolutions ("Most support actions are single-step — saga is overkill").
- **Full transfer vs lightweight approval** (step:escalation). Chosen: queue-aware routing with full ownership transfer, "because ambiguity about who is acting is more dangerous than the extra weight of a full transfer." Approval without transfer remains an option, with the risk of "approvers rubber-stamping out of context if the package is thin."
- **Resolution rate vs safe abstention** (step:escalation). Escalation is a legitimate outcome, not a failure to minimise.
- **Risk-weighted vs uniform QA** (step:compliance-eval). Chosen: risk-tiered sampling with auto-quarantine.
- technologyChoices "makesIrrelevant" lines worth quoting:
  - "A managed contact-center platform removes most custom channel gateway, recording, presence, and agent-desktop work, but not the in-loop action gate."
  - "Temporal or a managed workflow service removes most hand-rolled retry timer, lease, and compensation bookkeeping, though provider idempotency remains mandatory."
  - Guardrails "must not become the authority source for account actions; the deterministic gate still decides side effects."
  - "Never let the conversation agent call payment or order APIs directly; it should propose actions and let the gate plus transaction engine execute them." (concern "Commerce/payment adapters…")

## 1.7 Failure modes and containment

| Failure | Containment | Source |
| --- | --- | --- |
| Policy says yes, account says no (out of window, already refunded) | account state wins; the agent explains why | step:grounding deep dive |
| Account read times out | "never guess eligibility"; fallback reply; no action on stale or missing data | step:grounding, step:live-loop flow |
| Customer asserts an entitlement or injects instructions | text is data, never authority; Guardrail partitions message from action authority | step:grounding, step:txn-safety |
| Turn backlog under load | admission control sheds or queues and shows a "high volume" state | step:live-loop deep dive |
| Inference queue grows | smaller fallback model; queue-depth alarm triggers shedding | same |
| Provider QPS cap or outage | circuit breaker, per-tenant and per-action rate limits, bounded retry budget, async deferral | same |
| Refund succeeds but the connection drops and the customer retries | provider-scoped idempotency key per attempt | step:txn-safety decisionPrompt |
| Provider timeout with unknown outcome | lookup by key or webhook; then reuse, retry, or manual repair | step:txn-safety flow |
| Compensation itself fails | manual-repair queue (`compensations.manual_repair`) | step:txn-safety options |
| Approver absent past SLA | proposal expires; conversation re-routes; customer always gets a turn back | step:escalation deep dive |
| Agent acts while a human owns the case | no token minted while a handoff is open | same |
| Address change as an account-takeover route | identity proofing (`verification_challenges`) required | step:action-gate matrix |
| Wrong-action spike after a policy or model rollout | lower the tier for affected action kinds and tenants, roll back, clamp the classifier, repair | step:compliance-eval incident deep dive |
| High CSAT hides a wrong refund | action-correctness eval | step:compliance-eval concept |

## 1.8 Domain constraints

- **Domain-specific:** an action happens live on the customer's money and orders; the turn-taking latency budget (p95 < 2.5 s text, first token < 800 ms); voice cannot hold silence; refund abuse and account takeover; agentic checkout with delegated payment authority (a follow-up names a commerce protocol, "ACP"); 1–7 year transcript retention with PII (addresses, payment hints).
- **Broadly applicable:** untrusted user input; delegated rather than impersonated authority; reversibility as a policy attribute; reconciliation of external side effects; a staffed human queue as a capacity constraint; escalation as a valid outcome; correctness over satisfaction metrics; incident-driven reduction of autonomy.
- **Human roles:** the human support agent is both *approver* (one action; the conversation stays automated) and *owner* (after handoff; the agent goes read-only). technologyChoices states the difference: "Approval and handoff are related but not identical."

## 1.9 API and data-model snippets (exact)

Turn response (`SUPPORT api[0]`, `POST /v1/conversations/{id}/turn`):
```
{ "turnId": "...", "reply": "...", "decision": "none|executed|awaiting_approval|escalated", "proposedActionId": "...|null", "riskTier": "low|high", "reversibility": "reversible|compensatable|irreversible", "approvalRequired": false, "escalationReason": "...|null", "eventStreamUrl": "...", "auditEventId": "..." }
```
Approve (`SUPPORT api[1]`): "only an approval mints a scoped action token and executes. The proposed action expires if not decided in time." Request: `{ "decision": "approve|reject", "idempotencyKey": "...", "approverPrincipal": "...", "policyVersion": "...", "reasonCode": "in_policy|over_threshold|fraud_suspected|..." }`.

Escalate request (`SUPPORT api[2]`): `"reasonCode": "low_confidence|policy_conflict|customer_ask|rejected_action|fraud_suspected"` plus `transcriptPointer`, `summary`, `attemptedActions`, `accountSnapshot`, `priority`, `routingSkill`.

Proposal lifecycle (`SUPPORT dataModel.action_proposals.status`):
`enum(proposed,blocked_by_policy,awaiting_approval,approved,executing,executed,rejected,compensating,compensated,escalated)` with `expires_at`.

Attempt states (`SUPPORT dataModel.transaction_attempts.state`): `enum(pending,succeeded,failed,provider_timeout,unknown_external_state,reconciled)`.

Tenant policy (`SUPPORT dataModel.tenant_action_policies`): `auto_limit numeric null`, `reversibility_tier`, `required_proofing enum(none,low,high)`, `approval_rule enum(auto,approve,escalate)`, `version`, `active`.

Reversibility matrix (`SUPPORT step:action-gate`, deep dive "The reversibility / action matrix the gate keys off"), quoted rows:
- "resend_receipt -> reversible, auto, no provider money movement: the cheapest tier."
- "small_refund -> reversible/compensatable, auto only below the tenant auto_limit, provider idempotency required."
- "address_change -> reversible only before the fulfillment cutoff, requires identity proofing (verification_challenges) because it's an account-takeover surface."
- "account_closure -> not safely reversible -> escalate, never auto."

## 1.10 Weaknesses and inconsistencies

Fixed since REVIEW.md (do not cite as defects): the reversibility matrix (REVIEW §4), fraud signals (§6), the incident kill switch (§7), the authority model `tenant_action_policies` / `delegated_token_grants` / `verification_challenges` (§3), capacity sizing notes (§2), and options on steps 5, 6 and 7 (§5). The state writes in the step 3–6 flows were also added: `conversation_turns status=streamed/timed_out`, `write approval_decisions + audit (before token mint)`, `write handoffs`.

Still open, or found in this pass:
1. **Approval cannot fit the turn budget, and nothing models this explicitly.** ~50 approvals/sec at peak against a p95 of 2.5 s per turn means the customer cannot wait inside the turn. The turn response has `decision: awaiting_approval` and the voice note mentions "async action status", but no step shows the conversation turn that resumes after approval arrives. Step 3 has no options (REVIEW §5 is still open). The book must reconcile what "approval mid-conversation" means here: an asynchronous continuation within the session, not a blocking pause inside the turn.
2. **Approver staffing is unquantified.** At ~50 approvals/sec and an assumed 30 s per decision, the peak needs about 1,500 concurrent approvers. The dataset calls approval "a staffed queue with its own SLA" but never sizes it. That is a strong teaching point for the book (human throughput as a capacity constraint) that the source leaves implicit.
3. **Cost per conversation is absent.** There is a "token budget per turn" and a "smaller/faster fallback model", but no tokens per turn, no cost per resolution, and no deflection-economics figure. The book's performance/economics chapter cannot draw a cost model from SUPPORT.
4. **`risk_tier` has two values but the gate has three outcomes.** `risk_tier enum(low,high)` sits alongside `approval_rule enum(auto,approve,escalate)` and `reversibility` with three values. The tier is not the decision; the decision comes from the policy row. A reader can be confused, so the book should present the gate as a function of (kind, amount, reversibility, proofing, fraud signals), with tier as just one input.
5. **"Small refund is reversible/compensatable" is questionable.** Reversing a refund means re-charging the customer ("refund-then-recharge"), which in practice needs customer consent or authorisation. Calling it compensatable understates the effect on the customer. The book should treat money returned to a customer as effectively irreversible from the platform's side.
6. **Graph and flow mismatches.** The step:escalation flow has `ActionGate -> Escalation` ("expire proposal … build package"), but no link from ActionGate to Escalation exists in `highLevelArchitecture.links`. The step:action-gate flow has `Identity -> TxnEngine` "execute with scoped token", while the graph has `id-acct` (Identity → Account), which suggests that Identity performs the action itself.
7. **Enum drift.** `approval_decisions.decision` is `enum(approve,reject,expire)`, while the approve API response status is `executed|rejected|expired`. That is acceptable but inconsistent.
8. **Self-reference to sibling verticals** ("like abstention in the healthcare vertical"; finance/legal "before-the-action gates" in `followUps`). These reference other datasets outside this group; the book must not depend on them silently.

## 1.11 Best uses in the book

- **Foundations:** the "inside the loop vs before the action" axis, as the cleanest statement of the claim that *where* the gate sits is a design dimension.
- **Reference architecture:** the full 17-node final design as the interactive, transactional archetype.
- **Orchestration:** the harness under a latency budget; deflect/act/escalate as the per-turn router.
- **Context/memory/state:** two-sided grounding, evidence versions, freshness by data class, durable turn records for resume.
- **Tools/execution:** propose-then-execute (the agent never calls payment APIs); action-bound tokens; idempotency vs reversibility; reconciliation; compensation as a forward action.
- **Reliability/recovery:** unknown-outcome handling, the manual-repair queue, the saga trade-off, channel degradation.
- **Security/oversight:** customer text as data; fraud signals that only lower autonomy; proofing; the read-only agent after handoff; the approval vs ownership distinction.
- **Evaluation/observability:** action correctness over CSAT; the metric list in the step:compliance-eval deep dive; risk-tiered sampling; quarantine.
- **Performance/economics:** turn latency budgets, first-token targets, fallback models, admission control, audit volume arithmetic. Flag that cost per conversation is missing.
- **Deployment/evolution:** eval-gated policy and model rollout, plus the kill switch per action class.

---

# 2. SALES — Agentic Sales Platform

## 2.1 Summary

The platform runs SDR (sales development) agents: prospect research and enrichment, personalised **email-first** outbound sequences, CRM updates, and handoff of qualified replies to human reps. Users are sales reps and managers (who approve outreach and take handoffs), the tenants' prospects (who receive the mail), and operators. Failure here does not move money. It destroys **sender reputation and deliverability**, and it creates compliance violations (CAN-SPAM, GDPR; TCPA once SMS or phone is enabled): "a burned domain is slow to recover" (`SALES description`), and it "takes weeks to recover, if it recovers at all" (step:naive). The central idea: the agent drafts, and a **deterministic send gate** authorises. Approval is not delivery. Every send is re-checked at send time against a **global identity-resolved suppression list**, and volume is paced by a **reputation-aware per-inbox scheduler** rather than by provider API quota.

## 2.2 Requirements and capacity (the dataset's illustrative assumptions)

Functional (`SALES requirements.functional`): source prospects from intent signals and ICP lists; enrich through a waterfall of providers; personalise email-first outreach grounded in enriched, deduplicated CRM data; update the CRM bidirectionally; "Send only after a gate: suppression, compliance, approval, and reputation-aware rate limiting"; hand qualified replies to a rep.

Non-functional: deliverability is first-class (rotation, warmup, per-inbox caps, bounce/spam monitoring); "Honor every opt-out via a global, identity-resolved suppression list surviving across domains and inboxes"; compliance; tenant isolation; enriched and web text treated as untrusted; auditable.

Capacity (`SALES capacity`):

| Item | Value | Note (abridged) |
| --- | --- | --- |
| Workload | ~2k tenants | ~3 campaigns each, ~500 new prospects/campaign/day, so ~3M prospects/day |
| Enrichment fan-out | ~2.5 calls/miss | ~60% cache hit gives ~1.2M misses/day and ~3M provider calls/day (~35 QPS average, ~100–150 peak) |
| Send volume vs inbox caps | ~40–50/inbox/day | ramp starts at ~10–20/day; ~3M sends/day ÷ ~45 ≈ ~67k warmed inboxes; "the inbox cap, not provider throughput, is the binding constraint" |
| Reputation thresholds | <2% bounce, <0.1% spam | crossing either auto-pauses the domain |
| Suppression | global, sub-10 ms | checked at submit and re-checked at send |
| Audit & events | ~10–20M events/day | ~5–7 events per prospect; long retention |

Note: `SALES capacityDiagram` is qualitative only (Reputation → Suppress → Deliver). It carries no numbers, unlike SUPPORT's.

## 2.3 Evolution path

| # | Step id / title | Failure it fixes | New risk exposed |
| --- | --- | --- | --- |
| 1 | `naive` — "An Agent That Blasts Outreach" | baseline: one domain blasting unverified mail; opt-outs ignored | "Sender reputation collapses, opt-outs are ignored, and there's no approval or compliance." |
| 2 | `enrichment` — "Ground in the CRM + Waterfall Enrichment" | outreach guessed at prospect details; one provider gives poor coverage | "Even perfect personalization must not send to someone who opted out or burn the domain." |
| 3 | `send-gate` — "Suppression, Compliance & Approve-Before-Send" | messages could go to anyone unchecked; late opt-outs raced approval | "Even compliant sends burn reputation if volume and warmup aren't managed." |
| 4 | `deliverability` — "Deliverability as First-Class Infrastructure" | volume capped only by API limits | "Replies need routing to humans, and quality needs measuring." |
| 5 | `handoff` — "Qualified Handoff, Audit & Evaluation" | replies and quality unmanaged; raw replies went straight to reps | points onward to HR (a fairness gate) |

## 2.4 Final architecture

Nodes (`SALES highLevelArchitecture.nodes`) by group:

- **Research & Personalize** (`research`): `Orchestrator` (SDR Orchestrator: "Supervisor: research -> personalize -> sequence -> handoff. Hierarchical multi-agent."), `ResearchAgent` (enriches and drafts), `Enrichment` (waterfall with "per-field gap detection and cost control"), `CRM` (system of record with "field-level permissions and conflict resolution").
- **Send Gate** (`send-gate`): `SendQueue` ("Durable queue of approved sends; the deliverability manager leases work to it only when a warmed inbox has cap"), `SendGate` ("Final pre-send gate: suppression check, compliance, approval, reputation-aware rate limit"), `Suppression` (global identity-resolved opt-out, stateful), `Deliverability` (rotation, warmup, caps, bounce/spam monitoring, SPF/DKIM/DMARC), `Rep`.
- **Delivery & Audit** (`delivery`): `Email` (sending infrastructure), `Guardrail` (CAN-SPAM/GDPR/TCPA, tenant isolation, screening of untrusted enriched/web text), `AuditLog`.
- Also: `Signal`, `Gateway`, `Inference`, `DraftStore` ("immutable approved draft versions; nothing sends until cleared"), `Identity` ("ties approval to a rep"), `Observability`.

Key links: `sendqueue-sendgate` "lease when cap available"; `deliver-sendqueue` "cap / pause decisions"; `email-webhook` "bounce/complaint/unsub -> suppress"; `email-orch` "reply webhook (classify)"; `orch-rep` "qualified handoff"; `id-sendgate` "scoped act-as-rep token"; `id-crm` "scoped CRM write". The naive link `research-email` "blast directly (unsafe)" stays in the graph for step 1 only.

Final-design sentence worth quoting (`SALES finalDesign.description`): "The distinct queues — approval, send/scheduler, provider-retry, and the webhook/event stream — each carry different safety properties."

**Agent-specific vs ordinary.**
- Agent-specific: hierarchical orchestrator over research/draft sub-agents on the harness; personalisation grounded in a resolved profile, not model guesses; enriched text as untrusted (Dual-LLM / CaMeL split); LLM classification of reply intent before handoff; trajectory eval of reply quality.
- Ordinary (the bulk of the design): email deliverability, suppression lookup, idempotent send attempts, webhook dedupe, CRM conflict resolution, durable queues with leases, audit streaming. SALES is the strongest evidence in this group that **most of an agentic platform is not agentic**.

## 2.5 Reusable patterns

| Pattern | Where | Note |
| --- | --- | --- |
| Waterfall enrichment with per-field provenance and cost | step:enrichment; `dataModel.enrichment_results` | `provider`, `confidence`, `cost_cents`, `fetched_at` per field |
| Async enrichment queue with cache and freshness policy | step:enrichment options (recommended) | sized against provider QPS caps |
| Enrichment as provenance-bearing input, never overwriting the system of record | step:enrichment trap | "write only on confidence + freshness thresholds, and resolve conflicts against the CRM's external version" |
| Untrusted retrieved text kept out of the privileged path | step:enrichment concept | "A quarantined/Dual-LLM split keeps content the agent reads out of the privileged path that approves and sends." |
| Immutable approval snapshot | step:send-gate; `dataModel.drafts`, `approvals` | approval binds rep to `draft_version`; body immutable; footer template version snapshotted |
| Approve, enqueue, re-check at send time | step:send-gate options (recommended) | "A late opt-out blocks the queued send — suppression is authoritative at send time." |
| Global identity-resolved suppression with scope | step:send-gate concept; `dataModel.suppression` | block if a platform-scope row exists OR a matching tenant-scope row exists |
| Minimal suppression tombstone surviving data deletion | step:send-gate deep dive | DSR erases enriched PII "but preserves a minimal suppression row (identity_key + reason)" |
| Idempotent approve and send plus callback dedupe by provider event id | step:send-gate deep dive | "A provider timeout after it accepted the message is resolved by the idempotency key on retry, not by re-sending blindly." |
| Reputation-driven rate limiting (distinct from API quota) | step:deliverability | "a fleet can sit well under its API quota and still burn a domain" |
| Lease-on-headroom scheduler | step:deliverability | queued work waits; it is leased only when a warmed inbox has cap |
| Auto-pause and quarantine on threshold, rotate to warm spare | step:deliverability flow | "never blast from a cold replacement" |
| Kill switch that holds, never drops | `api /v1/fleet/pause` | "queued attempts transition to blocked and the durable queue holds (work is paused, not dropped)" |
| Classify before handoff | step:handoff; `api /v1/webhooks/replies` | "replies never route straight to a rep" |
| Route to the system-of-record owner, not the initiator | step:handoff trap | CRM account owner, not campaign owner |
| Delegated act-as-rep token with approved-by claim | step:send-gate concept | "not the rep's own credentials … every send is attributable" |
| Policy-versioned gate decisions | `dataModel.audit_events.policy_version` | replay which compliance ruleset allowed or blocked a send |

## 2.6 Decisions and trade-offs

- **Volume vs sender reputation** (step:naive). The blast baseline is rejected.
- **Freshness vs pipeline resilience** (step:enrichment). Chosen: async enrichment queue over synchronous inline enrichment, "because absorbing provider latency and staying under per-provider QPS caps matters more than perfectly fresh fields at draft time."
- **Provider cost vs completeness** (step:enrichment). Waterfall, first hit wins per field.
- **Approve-time vs send-time checking** (step:send-gate). Chosen: snapshot plus re-check; costs extra states and "slightly higher send latency."
- **API quota vs reputation limits** (step:deliverability). Chosen: a reputation-aware per-inbox scheduler with "Lower peak throughput per inbox (by design)."
- **Automation reach vs human judgment** (step:handoff). Classify every reply first; "the handoff boundary is where automation must yield to a human."
- **Send volume vs measured quality** (step:handoff). Reply quality, qualification accuracy and deliverability are evaluated together.
- technologyChoices highlights:
  - "Do not put sender-reputation caps only at the edge: per-inbox leases still belong in the deliverability scheduler." (API edge)
  - "Airflow-style batch orchestration is useful for refresh/backfill jobs, not for low-latency send gating." (SDR orchestration)
  - "Managed iPaaS connectors speed integration but often hide conflict semantics that matter for safe bidirectional writes." (CRM)
  - "Cold-outreach volume still needs many warmed domains and inboxes regardless of provider; the inbox cap, not provider throughput, is the binding constraint." (Email sending)
  - "A ledger database gives stronger tamper-evidence but is harder to query and operate at high event volume." (Audit; QLDB listed)
  - "Trace IDs should connect enrichment, draft, approval, send attempt, provider callback, reply classification, CRM update, and audit append." (Observability)

## 2.7 Failure modes and containment

| Failure | Containment | Source |
| --- | --- | --- |
| Mass blast burns a domain | gate, warmup, per-inbox caps, rotation | step:naive → step:deliverability |
| Opt-out on domain A, mail sent from domain B | global identity-resolved suppression | step:send-gate decisionPrompt |
| Opt-out between approval and send | send-time re-check | step:send-gate options |
| Reputation drops while work is queued | quarantine drains queued attempts to `blocked` | step:deliverability flow |
| Provider accepted, then timed out; retry double-sends | idempotency key on send attempt | step:send-gate trap |
| Duplicate or out-of-order webhooks | dedupe on provider event id; reconcile by timestamp | `api /v1/webhooks/delivery` |
| Enrichment clobbers a rep's curated CRM field | confidence and freshness thresholds; external-version conflict check | step:enrichment trap; `dataModel.crm_sync` |
| Prompt injection in scraped or enriched text | screened at the guardrail; no tool or send authority | step:enrichment trap |
| Provider outage stalls the pipeline | async enrichment queue | step:enrichment options |
| Out-of-office treated as interest | detect OOO; pause and retry after the return date | step:handoff trap |
| "Take me off your list" written in free text | intent classification leads to global suppression | step:handoff trap |
| Handoff goes to the wrong rep | route to the CRM account owner | step:handoff trap |
| Rapid reputation collapse | manual kill switch per tenant, domain or fleet | `api /v1/fleet/pause` |

## 2.8 Domain constraints

- **Domain-specific:** email deliverability mechanics (warmup, SPF/DKIM/DMARC, bounce <2%, complaints <0.1%); CAN-SPAM footer and physical address; RFC 8058 one-click unsubscribe (probe link); TCPA for deferred channels; CRM as an external system of record that humans also edit; enrichment provider cost and QPS caps.
- **Broadly applicable:** the scarce shared asset (here, reputation) as the binding constraint rather than API quota; approval snapshots with re-check at action time; obligations that outlive data deletion (suppression tombstones); classification before routing to humans; kill switches that pause durably; provenance on every input that drives an external action.
- **Reversibility:** an email cannot be unsent; reputation damage recovers slowly ("weeks"). It is irreversible in the small and slow to repair in aggregate.
- **Latency:** none customer-facing. The only hard latency is suppression lookup ("sub-10ms") at send. Throughput is bounded by inbox caps, not by compute.
- **Human role:** the rep approves drafts and closes deals. "The agent opens and qualifies; a human closes."

## 2.9 API and data-model snippets (exact)

Approve (`SALES api[1]`, `POST /v1/sequences/{id}/approve`): "The approval is idempotent (same key + version is a no-op) and snapshots the exact text approved; it enqueues the send rather than delivering directly, so the gate can re-check suppression and reputation at send time." Request: `{ "decision": "approve|reject", "draftVersion": 3, "idempotencyKey": "..." }` → `{ "status": "approved|rejected", "queuedSends": 4 }`.

Reply webhook (`SALES api[3]`) response: `{ "accepted": true, "classification": "qualified|unsubscribe|out_of_office|other" }`.

Kill switch (`SALES api[4]`): `{ "scope": "tenant|domain|fleet", "target": "...", "action": "pause|resume", "reason": "..." }` → `{ "status": "paused|resumed", "heldAttempts": 0 }`.

Suppression note (`SALES dataModel.suppression.note`): "Composite unique on (scope, tenant_id, identity_key); tenant_id is NULL for platform scope. Gate blocks if a platform-scope row OR a matching tenant-scope row exists."

Send-attempt lifecycle (`SALES step:send-gate` deep dive): "States: awaiting_approval -> approved -> queued -> (blocked | sent) -> delivered | bounced | complained | unsubscribed | failed; plus paused_for_reputation for the whole sequence."

Inbox health (`SALES dataModel.inboxes`): `warmup_state enum(warming,warm,paused,quarantined)`, `daily_cap`, `used_today`, `bounce_rate`, `spam_rate`, `spf_dkim_dmarc jsonb`.

Audit (`SALES dataModel.audit_events`): `actor_type enum(rep,agent,system)`, `action`, `object_type`, `object_id`, `draft_version`, `decision` ("allow/block + reason"), `source_event_id`, `policy_version`. The note says it is "never updated/deleted".

## 2.10 Weaknesses and inconsistencies

Fixed since REVIEW.md: the capacity arithmetic (REVIEW §1: now 1.2M misses → ~3M calls → ~35 QPS), suppression scope keying (§2: `tenant_id`, composite unique), a first-class `audit_events` (§3), the reply path through the orchestrator plus `/v1/webhooks/replies` (§4), the send-attempt state-machine deep dive (§5), Identity links into the gate and CRM, handoff traps, the deliverability control-loop flow, and technologyChoices.

Still open, or found in this pass:
1. **Human approval of every sequence does not scale to the stated volume. This is the sharpest internal inconsistency in the group.** The design requires rep approval before any send (`requirements.functional`: "Send only after a gate: … approval"; `sequences.status` passes through `awaiting_approval`). At ~3M prospects/day across ~2k tenants, that is ~1,500 approvals per tenant per day. There is no risk-tiering, no template-level approval, and no sampling. SUPPORT approves ~20% of actions and MARKETING ~15% of assets, so SALES is the outlier. The book should resolve this with approval at the template or sequence-policy level plus spot checks, and say explicitly that the dataset leaves it open.
2. **Approvals never expire.** `approvals` has no `expires_at`, and nothing invalidates an approval when the compliance ruleset (`policy_version`) or the footer template changes. MARKETING expires approvals on claim-library change; SUPPORT expires proposals by time. The send-time re-check covers suppression and caps, but not drift in the approval's own validity.
3. **"Hierarchical multi-agent" is asserted, not shown.** The orchestrator is called "Hierarchical multi-agent", but only one worker node (`ResearchAgent`) exists. No sub-agent boundaries, context isolation or delegation contracts are modelled.
4. **The cost model covers enrichment but not the LLM.** `enrichment_results.cost_cents` exists, but there is no token cost per prospect or sequence and no per-tenant model budget (MARKETING has one). There is no "cost per conversation" figure.
5. **Reply classification is an LLM decision with compliance consequences, and it is never evaluated as such.** A missed "remove me" is a legal opt-out failure, yet eval mentions only "reply quality and qualification accuracy". The book should add an opt-out recall metric.
6. **TCPA appears in the Guardrail node description and in send-gate step 3** ("compliance (CAN-SPAM address/opt-out, GDPR, TCPA)") even though phone and SMS are deferred and `sequences.channel` is `enum(email)`. This is a minor scope bleed.
7. **The capacity diagram has no numbers**, unlike SUPPORT. The ~67k-inbox figure is striking (about 33 warmed inboxes per tenant) and deserves a sentence in the book on what operating that fleet means.

## 2.11 Best uses in the book

- **Foundations:** the "scarce shared asset" framing, where the constraint is reputation, not compute.
- **Reference architecture:** the async, high-volume outbound archetype with several queues, each with its own safety property.
- **Orchestration:** the supervisor over research and drafting; queues as distinct safety stages.
- **Context/memory/state:** the system of record vs enrichment provenance; CRM conflict resolution; the waterfall as retrieval with a cost.
- **Tools/execution:** approval snapshot with send-time re-check (the cleanest **time-of-check vs time-of-use** example in the group); idempotent sends; webhook dedupe.
- **Reliability/recovery:** the deliverability control loop; quarantine; a kill switch that holds work.
- **Security/oversight:** untrusted enrichment text (Dual-LLM/CaMeL); act-as-rep delegated tokens; suppression tombstones vs DSR.
- **Evaluation/observability:** outcomes over activity ("volume never masks declining outcomes"); deliverability SLOs; trace IDs across the lifecycle.
- **Performance/economics:** inbox-cap arithmetic as the binding constraint; enrichment cache-hit economics.
- **Deployment/evolution:** domain warmup as gradual rollout of a reputation-bearing resource.

---

# 3. MARKETING — Agentic Marketing Platform

## 3.1 Summary

The platform lets marketing agents turn a campaign brief into per-channel assets (ad copy, email, social, landing pages, images), activate them across channels with CDP personalisation, and optimise live through a **bandit loop**. Users are marketers and brand owners (who approve high-risk claims), the audiences who see the assets, and operators. Failure is **public brand and reputation damage**: a prohibited or regulated claim, off-brand content, undisclosed synthetic media. There is also a quieter failure, runaway generation spend and provider rate-limit violations. The dataset places this "between the Developer and Finance verticals" on the irreversibility gradient (`MARKETING description`). The central idea: a **brand/claim gate** combining "deterministic claim/regulatory checks … plus model-judged brand-voice conformance", C2PA provenance on synthetic media, and risk-tiered approval, wrapped around a **policy-constrained bandit** whose every regenerated variant goes back through the gate.

## 3.2 Requirements and capacity (the dataset's illustrative assumptions)

Functional (`MARKETING requirements.functional`): turn a brief into per-channel assets; ground every asset in the brand kit; review for prohibited/regulatory claims and brand voice before launch; activate with personalisation and optimise through a bandit; "Require human approval for high-risk claims before publishing in the brand's name."

Non-functional: "Brand safety: nothing off-brand or making a prohibited claim is published"; C2PA provenance on synthetic media; channel compliance (CAN-SPAM, TCPA, GDPR, template approval); tenant isolation; brief and external text untrusted; auditable.

Capacity (`MARKETING capacity`):

| Item | Value | Note (abridged) |
| --- | --- | --- |
| Tenants & campaigns | 2k tenants, ~5k campaigns/day | ~5 channels × ~8 variants gives ~40 assets/campaign and ~200k assets/day |
| Generation cost | ~200k LLM + ~80k image calls/day | peak ~10 generations/sec; concurrency cap ~500; per-tenant token/image budget |
| Approval queue | ~15% high-risk, so ~30k approvals/day | "minutes-to-hours latency" |
| Channel delivery | provider rate-limited | per-provider token buckets; retry/backoff; dead letter; `publish_attempt` tracks partial failure |
| Performance events | ~50k impressions/sec peak | conversions land "hours-to-days" late within an attribution window |
| Bandit cadence | reallocate every ~15 min | over currently cleared variants only; stale analytics freezes; low traffic gets a fixed split |
| Audit retention | ~1M events/day, 7-year retention | partitioned by tenant and month |

## 3.3 Evolution path

| # | Step id / title | Failure it fixes | New risk exposed |
| --- | --- | --- | --- |
| 1 | `naive` — "An Agent That Generates and Publishes" | baseline: direct publish, no brand check, no disclosure, no sign-off; plus unbounded spend and provider overload | "Off-brand, false-claim, or undisclosed synthetic content can go public with no review." |
| 2 | `grounding` — "Ground in the Brand Kit / DAM" | generic model style; no record of which guidance was used | "Grounding biases toward on-brand but doesn't guarantee no prohibited claim slips through." |
| 3 | `brand-gate` — "Brand & Claim Review + C2PA Provenance" | assets could publish unchecked | "Once live, the platform must optimize without drifting off-brand." |
| 4 | `optimize` — "The Optimization Loop: Bandits Over Variants" | campaigns static after launch | "Personalization and channels carry their own compliance rules and untrusted data." |
| 5 | `compliance` — "Channel Compliance, Personalization & Audit" | channel rules ad hoc; compliance treated as a boolean | "Quality and brand-safety must be measured, not assumed." |
| 6 | `eval` — "Brand-Safety & Performance Evaluation" | only performance measured | points onward to sales and HR |

## 3.4 Final architecture

Nodes (`MARKETING highLevelArchitecture.nodes`) by group:

- **Generation** (`generation`): `Orchestrator` (Campaign Orchestrator; "Submits cleared, approved assets to the delivery workflow rather than calling channels directly, so retries, partial-failure, and publish-attempt state are durable"), `GenAgent` (Content Agent, LLM/image), `BrandKit` (Brand Kit/DAM: voice, style, approved assets, negative-claim library).
- **Brand & Claim Gate** (`brand-gate`): `ClaimGate` ("Deterministic claim/regulatory checks (negative-claim library, required disclosures, blocked phrases) plus model-judged brand-voice conformance with a threshold and evidence"), `Provenance` (C2PA stamping), `AssetStore` (pending assets), `Marketer`, `DeliveryWorkflow` ("Durable publish state machine: holds publish_attempts per provider, enforces generation concurrency, per-tenant spend caps, and per-provider token buckets, and owns retries, backoff, and dead-letter handling").
- **Activation & Optimization** (`optimize`): `Channels`, `Analytics`, `Bandit`, `CDP`.
- Also: `Brief`, `Gateway`, `Inference`, `Guardrail`, `Identity` ("ties approval to a brand owner"), `AuditLog`, `Observability` (brand-safety and claim-violation rates).

Key links: `orch-deliver` "submit publish attempt"; `deliver-guard` "final policy + approval re-check"; `deliver-id` "scoped channel token"; `channels-deliver` "delivery callback (deduped)"; `analytics-bandit`; `bandit-orch` "reallocate / regenerate"; `claim-brand` "check vs negative-claim library". The naive link `gen-channels` "publish directly (no gate)" stays in the graph for step 1.

**Agent-specific vs ordinary.**
- Agent-specific: orchestrator fan-out to content agents; brand-kit retrieval with version citation; the model judge for brand voice; regeneration around winners (the agent writes new arms for the optimiser); brief text as untrusted; brand-safety eval as a release gate.
- Ordinary: the rules engine for prohibited claims; C2PA signing and KMS; the durable publish workflow with token buckets and DLQ; webhook dedupe; streaming analytics with attribution windows; the bandit itself (a classic algorithm, not an LLM); consent and preference management.

## 3.5 Reusable patterns

| Pattern | Where | Note |
| --- | --- | --- |
| Spend admission control (concurrency cap + per-tenant budget) | step:naive; capacity "Generation cost" | the naive design's second, quieter failure |
| Versioned retrieval with citation | step:grounding options (recommended) | "A changed negative-claim library can re-flag pending assets by version diff." |
| Split gate: deterministic rules for the guaranteeable, model judge for the subjective | step:brand-gate | "claims must be enforced as rules while voice genuinely needs judgment" |
| Negative-claim library as a deterministic check | step:brand-gate concept | "It turns brand/legal risk into a deterministic check instead of hoping the model behaves." |
| Risk-tiered human approval | step:brand-gate | regulated/financial/claim-bearing assets go to a brand owner; low-risk "flow under policy" |
| Approval that expires on a policy-corpus change | `api /v1/assets/{assetVersionId}/approve`; `dataModel.approvals.snapshot_claim_lib_version` | "expires if the library changes" |
| Immutable asset versions with supersession | `dataModel.asset_versions.supersedes` | "supersession instead of mutation" |
| Publish attempt as a state machine, not a flag | step:brand-gate deep dive; `dataModel.publish_attempts` | one delivery row per provider; partial failure is recoverable |
| Re-check at activation, immediately before provider submission | step:compliance trap | consent, region policy, template approval, approval validity |
| Content provenance stamp (C2PA) with a canonical copy | step:brand-gate; technologyChoices "Content authenticity" | "storing a canonical copy protects auditability when a channel strips metadata" |
| Policy-constrained optimiser over eligible arms only | step:optimize options (recommended) | arms "materialized from current approvals/claim status at decision time, not cached" |
| Optimisation that fails closed | step:optimize deep dive "Bandit guardrails" | stale analytics or a missing safety feed "freezes allocation at the last safe split" |
| Regenerated output re-enters the gate | step:optimize | "every regenerated variant goes back through the brand/claim gate" |
| Scoped consent (recipient × channel × region × purpose × legal basis) | step:compliance; `dataModel.consent` | "Compliance is not one boolean" |
| DSR tombstone alongside de-identified append-only audit | step:compliance | `suppression_reason = dsr_deletion` |
| Kill switch that also removes optimiser arms | `api /v1/campaigns/{id}/pause` | "remove its arms from bandit allocation" |
| Eval as a release gate with numeric thresholds | step:eval trap | "block a prompt/model/reviewer rollout if shadow eval raises the claim-violation rate above 0.1% or drops the median brand-voice score below 0.8 against the held-out set" |

## 3.6 Decisions and trade-offs

- **Speed to publish vs brand safety** and **variant volume vs spend control** (step:naive). Both baselines are rejected.
- **Versioned retrieval vs prompt stuffing** (step:grounding). Versioned retrieval is chosen despite the infrastructure cost.
- **Deterministic rules vs model judgment** (step:brand-gate). Split gate over a model-only self-check: "A prompt can't guarantee a prohibited claim never appears across thousands of variants."
- **Review friction vs risk tiering** (step:brand-gate). Tiered, "at the cost of a tiering policy that must itself be right."
- **Exploration vs guardrails** (step:optimize). The policy-constrained bandit is chosen over unconstrained bandits and fixed A/B tests.
- **Continuous optimisation vs statistical simplicity** (step:optimize). The bandit is accepted, with logged, reversible decisions and attribution windows.
- **Personalisation reach vs consent scope** (step:compliance). Consent is enforced as versioned structure "so the optimization loop cannot optimize past it."
- **Performance lift vs claim safety** (step:eval). Two-dimensional eval: "the best-performing asset can be the least safe one."
- technologyChoices highlights:
  - "provenance still does not prove the asset is safe or compliant" (Content authenticity).
  - "managed guardrail services reduce classifier operations but can hide exact policy semantics" (Claim gate).
  - "Feature-flag/config systems make allocation changes fast and reversible" (Bandit).
  - "Managed messaging suppression removes some opt-out bookkeeping, but DSR/deletion versus retention/audit reconciliation remains domain logic" (Consent).

## 3.7 Failure modes and containment

| Failure | Containment | Source |
| --- | --- | --- |
| Prohibited claim in one of thousands of variants | deterministic negative-claim rules | step:brand-gate |
| Off-brand voice | thresholded model judge, escalation on low scores | step:brand-gate |
| Undisclosed deepfake or synthetic image | C2PA stamp; canonical manifest copy | step:brand-gate; technologyChoices |
| Claim library updated after approval | approval expires; re-check at activation | `api …/approve`; step:compliance trap |
| One channel publishes, another fails | per-provider `deliveries` under a `publish_attempt`; `partially_delivered` state | step:brand-gate deep dive |
| Retried publish double-publishes | idempotency key on create/approve/publish | `api …/publish` |
| Duplicate or out-of-order callbacks | `webhook_dedupe_key`; append-only events | `api /v1/webhooks/{provider}/delivery` |
| Exhausted retries | dead letter for operator attention | step:brand-gate deep dive |
| Bandit allocates to a paused, revoked or regressed arm | eligibility materialised at decision time | step:optimize trap |
| Bandit overspends or over-targets a segment | budget pacing, frequency caps, audience and fairness caps | step:optimize deep dive |
| Short attribution window overfits | reward = conversions within the window; discount unsettled arms | same |
| Analytics or safety feed stale | freeze at the last safe split | same |
| Cold-start or low-traffic campaign | fixed A/B or rules fallback | same |
| Recipient consented to email, not SMS | consent scoped by channel and purpose | step:compliance trap |
| Provider template revoked | `channel_policy_versions.template_approval` re-checked | step:compliance |
| Model, prompt, reviewer or brand-kit change raises the violation rate | shadow eval as a release gate | step:eval trap |
| Runaway generation spend | concurrency cap ~500; per-tenant token/image budget | capacity; step:naive |

## 3.8 Domain constraints

- **Domain-specific:** brand voice; negative-claim libraries; synthetic-media disclosure (C2PA); ad-platform template approval; attribution windows and delayed conversions; CDP personalisation under GDPR purpose limitation; 7-year audit retention.
- **Broadly applicable:** deterministic rules for what can be guaranteed and judges for what cannot; version-pinned grounding that invalidates downstream approvals; output regenerated by an optimiser must re-enter the gate; fail-closed optimisation; spend admission control; eval as a release gate.
- **Reversibility:** a published asset can be paused or rolled back ("rollback reverts to a prior approved version"), but the public exposure cannot be undone: it is "public reputation damage that can't be quietly retracted" (step:naive tradeoffs).
- **Latency:** none in the turn. Approvals take "minutes-to-hours", reallocation runs every ~15 minutes, conversions arrive over hours to days.
- **Human role:** the brand owner approves high-risk assets (~30k/day across 2k tenants, ~15 per tenant per day, which is plausible) and owns brand liability: "brand liability stays with the company."

## 3.9 API and data-model snippets (exact)

Approve (`MARKETING api[1]`, `POST /v1/assets/{assetVersionId}/approve`): "A brand owner approves a specific immutable asset version; the approval snapshots the claim-library version and expires if the library changes." Request `{ "decision": "approve|revise|reject", "comment": "..." }` → `{ "approvalId": "...", "status": "approved|returned|rejected", "expiresAt": "..." }`.

Publish (`MARKETING api[2]`): "opens a publish_attempt, re-checks policy/approval validity, and fans out per-provider deliveries. Idempotent via Idempotency-Key so a retried publish returns the same attempt rather than double-publishing."

Performance read (`MARKETING api[5]`): `{ "variants": [ { "id": "...", "ctr": 0, "conv": 0, "allocation": 0, "eligible": true } ] }`. The `eligible` flag makes the safety filter visible in the API.

Publish attempt states (`MARKETING dataModel.publish_attempts.state`): `enum(admitted,policy_rechecked,submitting,partially_delivered,delivered,paused,failed,dead_letter)`.

Asset version states (`MARKETING dataModel.asset_versions.status`): `enum(generated,claim_checked,awaiting_approval,approved,live,paused,superseded,rejected)`, with `model_id`, `prompt_hash`, `brand_kit_version`, `claim_lib_version`, `c2pa_manifest`.

Consent (`MARKETING dataModel.consent`): `channel enum(email,sms,push,ads)`, `purpose enum(marketing,transactional,service)`, `legal_basis enum(consent,legitimate_interest,contract)`, `state enum(opted_in,opted_out,suppressed)`, `suppression_reason enum(user_optout,bounce,complaint,dsr_deletion,provider_revoked,null)`.

Bandit decision (`MARKETING dataModel.bandit_decisions`): `eligible_arms jsonb (cleared asset_version_ids)`, `allocation`, `exploration_rate`, `constraints jsonb (frequency/audience caps)`. The note reads: "Auditable, reversible budget reallocation over only cleared/approved arms."

## 3.10 Weaknesses and inconsistencies

Fixed since REVIEW.md: the publish lifecycle is now a first-class node and entity (REVIEW §1: `DeliveryWorkflow`, `publish_attempts`, `/publish`); compliance semantics (§2: `purpose`, `legal_basis`, `channel_policy_versions`, `suppression_reason`, the DSR note); bandit guardrails (§3); queue and admission control are visible (§4); claim-gate wording is normalised in the node and final design (§5); a concrete eval threshold (P3); the second naive failure (spend) is mentioned.

Still open, or found in this pass:
1. **Step 5's flow contradicts the architecture and the publish API.** The step:compliance sequence has `Orchestrator -> Guardrail` "final check", then `Guardrail -> Identity` "request scoped channel token", then `Channels -> AuditLog` "delivery webhook". But the graph and `api[2]` route the final re-check through `DeliveryWorkflow -> Guardrail` (`deliver-guard`) and `DeliveryWorkflow -> Identity` (`deliver-id`), and callbacks go to `DeliveryWorkflow` (`channels-deliver`). Two different owners of the final pre-submit check appear. The book should name one: the delivery workflow.
2. **Provenance is stamped before review.** Link `gen-prov` (GenAgent → Provenance) signs media at generation time, before the claim check and approval. The C2PA technology note says to sign "asset-version ID, and claim-library version", which are not final until review. The signing point needs to be stated: after approval, or re-signed at approval.
3. **The `audit_record` model is the thinnest in the group.** It has only `event_id, campaign_id, kind, payload`: no actor, no policy version, no hash chain, no tenant_id, despite 7-year retention and "brand liability stays with the company". Compare `SUPPORT audit_record` (hash-chained, correlation IDs) and `SALES audit_events` (actor, decision, policy_version).
4. **Email/SMS is sent without the deliverability machinery SALES calls the binding constraint.** MARKETING activates email and SMS and handles bounces and complaints as consent `suppression_reason`, but has no warmup, inbox caps or reputation thresholds. For marketing (opt-in) mail the constraint is weaker than for cold outbound, but the dataset never says so. This is a cross-source contradiction to address.
5. **Consent has no identity resolution or platform scope.** It is keyed by `subject_hash` per tenant only, so it cannot represent SALES's "platform-scope" suppression (a platform-wide abuse block across tenants).
6. **Regeneration latency vs the bandit cadence.** The bandit runs every ~15 min, but high-risk regenerated variants wait "minutes-to-hours" for approval. The dataset does not say whether high-risk regenerations are allowed in the loop at all, or how the loop behaves when the eligible arm set shrinks. That is implied by "allocates only among arms with current cleared claim status" but not discussed.
7. **The "Developer and Finance verticals" on the gradient** reference datasets outside this group.

## 3.11 Best uses in the book

- **Foundations:** the irreversibility gradient (brand damage sits between developer and finance), and the claim that "polish isn't brand-safety."
- **Reference architecture:** the generate → gate → publish → measure → regenerate closed loop.
- **Orchestration:** fan-out generation; an optimiser that feeds back into an agent and so must re-enter the gate.
- **Context/memory/state:** versioned grounding corpora whose version pins invalidate approvals; immutable asset versions.
- **Tools/execution:** publish attempt as a state machine; partial multi-provider failure; token buckets.
- **Reliability/recovery:** DLQ, pause and rollback; a fail-closed optimiser.
- **Security/oversight:** the split gate (rules vs judge); C2PA provenance; brief text as untrusted; scoped consent and DSR.
- **Evaluation/observability:** two-dimensional eval; a release gate with numbers (0.1% violation rate, 0.8 voice score).
- **Performance/economics:** the clearest spend model in the group (~200k LLM + ~80k image calls/day, concurrency cap ~500, per-tenant budgets).
- **Deployment/evolution:** shadow eval that gates prompt, model and reviewer rollouts.

---

# 4. Cross-source synthesis

## 4.1 Patterns that recur (each source's name for them)

| Book pattern name (proposed) | SUPPORT | SALES | MARKETING |
| --- | --- | --- | --- |
| **Deterministic gate before the external side effect** | "In-Loop Action Gate" (reversibility-tiered) | "Send Gate" (suppression, compliance, approval, reputation) | "Brand & Claim Reviewer" / "Brand & Claim Gate" |
| **Bounded autonomy** (agent free, gate fences) | concept "Bounded autonomy (agent + deterministic gate)" at step:action-gate | same concept at step:send-gate | same concept at step:brand-gate, step:optimize |
| **Model may only lower autonomy** | "learned risk score can only lower autonomy" | (implicit: the gate is deterministic) | model judge escalates on low voice score; it never overrides the rules |
| **Approval bound to an exact version / snapshot** | approval bound to action id + resource + amount + policy version + approver | approval binds rep to immutable `draft_version` | approval binds brand owner to `asset_version_id` + `snapshot_claim_lib_version` |
| **Re-check at time of use** | account re-read "before acting"; token minted only after gate | "re-check suppression + caps at send time" | "Re-check consent, region policy, template approval, and approval validity at activation time" |
| **Delegated, scoped, attributable authority** | action-bound on-behalf-of token (`delegated_token_grants`) | "scoped act-as-rep token" with act/approved-by claim | "scoped channel token"; approval tied to brand owner |
| **Idempotent side effect + callback dedupe** | provider-scoped idempotency key per attempt; reconcile by lookup | idempotency key on approve/send; dedupe on provider event id | Idempotency-Key on create/approve/publish; `webhook_dedupe_key` |
| **Attempt lifecycle as a state machine** | `action_proposals` + `transaction_attempts` | send-attempt lifecycle | `publish_attempts` + `deliveries` |
| **Untrusted content partitioned from authority** | customer messages | enriched/scraped web text | brief text and scraped content |
| **Versioned grounding corpus with evidence** | KB version + account snapshot version | per-field enrichment provenance | brand-kit + claim-library version on every asset |
| **Kill switch / emergency pause** | lower autonomy per action class; agent read-only | `/v1/fleet/pause` (tenant/domain/fleet; holds work) | `/v1/campaigns/{id}/pause` (removes bandit arms) |
| **Append-only audit with policy version** | hash-chained `audit_record` | `audit_events` | `audit_record` (thin) |
| **Human handoff after classification** | deflect-vs-escalate router with context package | reply classification before rep handoff | (none: humans approve, they don't take conversations) |
| **Outcome eval over activity/satisfaction metrics** | action correctness over CSAT | reply quality over send volume | claim-violation rate alongside CTR/lift |
| **Harness reuse from Foundations** | turn loop on the harness | SDR orchestrator on the harness | campaign orchestrator on the harness |

All three use the same concept labels inherited from a shared catalogue: "Human-in-the-loop approval (gate)", "Delegation not impersonation (OAuth token exchange, act claim)", "Prompt-injection defense (CaMeL / Dual-LLM / Plan-then-Execute)", "LLM-as-judge / trajectory evaluation", "Memory: short-term vs long-term". The book can adopt one vocabulary from these.

## 4.2 Where the sources disagree

1. **Approval semantics (three incompatible models).**
   - SUPPORT: approval is per *action*, ~20% of proposed actions, expires by **time** (`expires_at`, SLA). A missed approval leads to expiry and re-route, never execution. Decision values: approve/reject/expire.
   - SALES: approval is per *draft version* of every sequence, **no expiry**, no tiering. Values: approve/reject.
   - MARKETING: approval is per *asset version*, ~15% risk-tiered, expires on **policy-corpus change** (claim library). Values: approve/revise/reject.
   - The book needs one approval model: bound to an immutable object version + policy version + approver; expiring on time **or** on policy change; risk-tiered; with explicit expired/revise outcomes.
2. **Suppression and consent models.** SALES has `suppression` (identity-resolved, tenant or platform scope, reason/provenance, no purpose). MARKETING has `consent` (per tenant `subject_hash`, channel × region × purpose × legal basis, no platform scope, no identity resolution). SUPPORT has none: customer consent is folded into `verification_challenges` (proofing). A unified model needs scope (tenant/platform), resolved identity, channel, purpose, legal basis, reason and provenance, and a DSR tombstone. Both SALES and MARKETING tombstone on DSR, but name it differently ("minimal suppression row" vs `suppression_reason = dsr_deletion`).
3. **Where the final check lives.** SUPPORT: the ActionGate, then Identity mints the token, then TxnEngine executes. SALES: SendGate leased from SendQueue. MARKETING: DeliveryWorkflow → Guardrail in the graph, but Orchestrator → Guardrail in the step 5 flow (an internal contradiction). The book should present "the executor re-checks immediately before the external call" as one rule, owned by the component that holds the attempt state.
4. **Audit depth.** SUPPORT is hash-chained with correlation IDs and retention classes; SALES has actor, decision and policy_version but no hash; MARKETING has kind and payload only. The book should take SUPPORT's schema as canonical and note the others as weaker variants.
5. **Reversibility vocabulary.** SUPPORT has an explicit three-class attribute (reversible / compensatable / irreversible) per action. SALES and MARKETING place the whole vertical on a gradient ("reputation tier") without per-action classes, although MARKETING does pause and roll back. The book can generalise SUPPORT's per-action attribute to all three: an email send is irreversible; a published asset is pausable but its exposure is irreversible.
6. **Deliverability.** SALES says inbox reputation is the binding constraint for email; MARKETING sends email/SMS with only consent-based suppression. They contradict each other unless the book separates cold outbound (reputation-bound) from opt-in marketing (consent-bound).
7. **Multi-agent claims.** SALES says "Hierarchical multi-agent" with one worker; MARKETING says "fans out per-channel asset generation to content agents"; SUPPORT is single-agent. None models sub-agent context boundaries. Do not cite any of them as evidence for a multi-agent design.
8. **"Gate" naming of the human step.** SUPPORT calls a human-approval step mid-conversation part of the gate; SALES and MARKETING treat approval as a precondition checked *by* the gate. That is a small difference, but the book should define the gate as the deterministic decision point and approval as one of its inputs.

## 4.3 Strongest domain contrasts

| Dimension | SUPPORT | SALES | MARKETING |
| --- | --- | --- | --- |
| Consequence of failure | money moved, account changed or taken over, for one customer | sender reputation burned (fleet-wide, slow recovery); legal violation per message | public brand damage, regulated-claim liability; spend overrun |
| Blast radius | one customer per error, but errors repeat at ~255 actions/sec | one bad domain affects every tenant mailing from it | one asset can be seen by millions of impressions |
| Reversibility | per action: receipt (reversible) … closure (irreversible) | email: irreversible; reputation: recovers over weeks | pausable and rollback-able, but exposure is irreversible |
| Where the gate sits | **inside** a live turn | before an async send, re-checked at send time | before publish, re-checked at activation, and again for every regenerated variant |
| Latency | hard: p95 < 2.5 s text, first token < 800 ms | none customer-facing; suppression lookup < 10 ms | none; approvals minutes to hours; bandit every 15 min |
| Volume | ~1.7k turns/sec; ~50k concurrent | ~3M prospects/day; ~10–20M events/day | ~200k assets/day; ~50k impressions/sec |
| Binding constraint | turn latency and human approver throughput | warmed-inbox caps (~67k inboxes) | generation spend and provider QPS; approval queue |
| Required human control | approve ~20% of actions *while the customer waits*; own escalated cases | approve every sequence (as written); close deals | approve ~15% of assets (high-risk); own brand liability |
| Data sensitivity | highest: authenticated account, payment hints, addresses, PII transcripts (1–7 yr) | prospect PII from third-party enrichment; consent basis often "legitimate_interest/unknown" | CDP profiles for personalisation; consent by purpose; 7-yr audit |
| Untrusted input source | the customer (adversarial: fraud, social engineering) | the open web via enrichment | the brief and scraped competitive content |
| Optimisation loop | none (eval feeds gate policy) | none (eval only) | yes: a bandit drives regeneration, so the gate must be in the loop |
| Cost data available | token budget per turn, fallback model (no $) | `cost_cents` per enrichment field (no LLM cost) | call counts, concurrency cap, per-tenant budget (no $) |

## 4.4 Gaps across all three (for the book to fill or flag)

- **Cost per conversation / per outcome is never quantified in money.** MARKETING has the best call-volume model; SUPPORT has only "token budget per turn"; SALES costs only enrichment. The performance/economics chapter will have to build its own illustrative cost model and say so.
- **Human approver capacity is never sized.** SUPPORT's ~50/sec peak and SALES's every-sequence approval both imply staffing figures that the datasets do not compute.
- **Eval of the LLM-made routing decisions** (SUPPORT deflect-vs-escalate confidence, SALES reply-intent classification) is mentioned (missed-escalation rate in SUPPORT) but not designed: no labelled sets, no recall targets for compliance-critical intents such as opt-out.
- **Model routing and fallback** appear only in SUPPORT (a smaller, faster fallback model). None discusses model choice per step or per tenant beyond technologyChoices prose.
- **Multi-turn memory across conversations** (the returning customer, the prospect contacted again) is absent. All three ground in an external system of record instead. That is a defensible choice, and worth stating in the context/memory chapter.

## 4.5 Recommended use of the group in the book

- Use **SUPPORT** as the primary worked example for *where the gate sits* (inside the loop), *reversibility classes*, *idempotency ≠ reversibility*, *reconciliation of unknown outcomes*, *approval vs ownership handoff*, and the *autonomy kill switch*.
- Use **SALES** as the primary worked example for *time-of-check vs time-of-use* (approval snapshot plus send-time re-check), *a shared scarce resource as the binding constraint*, *queues with distinct safety properties*, and *obligations that outlive deleted data*. Also use it to show how much of an "agentic" platform is ordinary distributed-systems machinery.
- Use **MARKETING** as the primary worked example for *closed optimisation loops that must re-enter the gate*, the *split gate (rules for the guaranteeable, judge for the subjective)*, *version-pinned grounding that expires approvals*, *fail-closed optimisation*, *spend admission control*, and *eval as a release gate with numbers*.
- Reconcile before citing: the approval model (§4.2.1), the consent/suppression model (§4.2.2), the owner of the final re-check (§4.2.3), and the audit schema (§4.2.4).
