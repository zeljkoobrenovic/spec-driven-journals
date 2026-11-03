# Digest — high-stakes-and-research

Group: `high-stakes-and-research`
Sources (all under `/Users/zeljkoobrenovic/PycharmProjects/system-design-interviews/data/book/`):

- `agentic-healthcare-platform/` — `interview.json`, `REVIEW.md` (dated 2026-06-25), `LINKEDIN.md`
- `agentic-public-benefits-platform/` — `interview.json`, `REVIEW.md` (dated 2026-06-24), `LINKEDIN.md`
- `agentic-research-platform/` — `interview.json`, `REVIEW.md` (dated 2026-06-24), `LINKEDIN.md`

Digested 2026-10-28. Each `interview.json` was read in full (description, highLevelArchitecture, requirements, capacity, api, dataModel, technologyChoices, every step with options/deepDives/flows/tradeoffs, finalDesign, satisfies, interviewScript, levelVariants, followUps). `toProbeFurther` link lists were not digested.

**Provenance rule (applies to everything below).** These are interview design exercises from the author's system-design interview project: proposed architectures, not deployed systems. Nothing here is evidence of production behaviour. Cite as, for example, *design example from the author's system-design interview project, `system-design-interviews/data/book/agentic-healthcare-platform/interview.json`, step 4 (`safety`)*. All numbers are the datasets' illustrative assumptions.

**Freshness warning about the REVIEW.md files.** All three REVIEW.md files predate the current JSON. Most of their "highest-impact issues" have since been fixed in the JSON (details in each section 10). Do not quote a REVIEW.md gap as a current gap without checking the JSON. Treat the REVIEW.md files as a record of which parts were hard to get right, which is useful in itself.

**Coverage gap for the brief.** The brief asks for "multi-agent research decomposition". None of the three sources contains it. The research platform has a single bounded `HypoAgent` node inside a deterministic DAG; a grep of all three JSON files finds no "multi-agent", "subagent", "planner" or "orchestrator-worker". The book must source multi-agent decomposition elsewhere (other digest groups, or external references). What these sources do offer is the opposite lesson: in high-stakes domains the designs deliberately *avoid* agent autonomy and decomposition, and confine the model to one or two bounded nodes.

---

## Source 1 — Agentic Healthcare Platform

Path: `system-design-interviews/data/book/agentic-healthcare-platform/interview.json`

### 1.1 Summary

A platform for clinical decision-support agents: differentials, dosing, guideline lookup and chart summarization. The users are licensed clinicians; the patient is the affected party whose PHI must stay scoped to their care team. If it fails, a person can suffer irreversible bodily harm. The dataset places this at "the top of the irreversibility gradient, above Legal" (interviewScript, phase 1). The central idea is **recommend, never act, and abstain rather than guess**. A deterministic pipeline (retrieve → reason → calibrate → abstain-or-recommend → clinician sign-off) confines the LLM to one bounded reasoning node. A confidence calibrator and a deterministic safety layer stand between the model and the clinician, and neither can be overridden by the model. A licensed clinician authorizes every action; "Nothing acts on a patient autonomously" (top-level `description`). It runs on the agent harness from `agentic-platform-foundations` (step 1 `naive`, concept "Agent harness (from Foundations)").

### 1.2 Requirements and capacity (dataset's illustrative assumptions)

Functional (`requirements.functional`): answer decision-support queries; ground every recommendation in guidelines and the patient record; run deterministic safety checks (contraindications, interactions, allergies, dose limits); abstain when grounding or confidence is insufficient; require a licensed clinician to authorize every recommendation; "Scope behavior by clinical task and risk tier: dosing, differential, chart summary, and guideline lookup don't share one confidence threshold or one approval path."

Non-functional: safety dominates and the safe default is to abstain; PHI is scoped to the care team (HIPAA / BAA / no-train); hard rules the model cannot override; a documented safety case with SaMD/FDA framing; everything auditable.

Capacity (`capacity`):

| Item | Value | Note |
| --- | --- | --- |
| Active clinicians | ~20k DAU | daytime concentration |
| Decision-support queries | ~500k/day | ~25 per clinician per day |
| Peak interactive QPS | ~30–60 QPS | diurnal peak 5–8x average |
| EHR retrieval fanout | ~5–15 calls/query | FHIR/HL7 reads dominate latency, hit EHR rate limits |
| Guideline index latency | p95 < 150 ms | hybrid retrieval, cached hot |
| Interactive p95 latency | < 6 s end-to-end | longer tasks go async with a worklist entry |
| Inference budget | ~4–8k tokens/query | bounded context: chart facts + cited spans |
| Sign-off queue depth | target < 30 min p95 age | "flooding the queue is an operational failure (alert fatigue)" |
| EHR write rate limit | per-tenant, retried | failed write → explicit `ehr_write_failed` |
| Backpressure | queue + admission control | shed non-urgent work "rather than degrading safety" |
| Default on uncertainty | abstain | |
| Autonomy | recommend-only | |
| Safety override | deterministic | |

Note that the last three "capacity" rows are safety invariants rather than capacity figures. That pattern recurs in all three sources.

### 1.3 Evolution path (one failure at a time)

1. **`naive` — An agent that answers clinical questions.** Failure exposed: a confident wrong dose or differential reaches the bedside with no grounding, no safety checks, no refusal and no clinician. "the most dangerous baseline in the whole series."
2. **`grounding` — Ground in guidelines + the patient record.** Fixes generic-knowledge answers. The grounding is two-sided: a versioned guideline or formulary *and* this patient's chart. The guideline/formulary versions and the patient snapshot timestamp are captured, and "A stale or incomplete snapshot ... is itself a reason to abstain." The snapshot is also the input to a freshness re-check at sign-off.
3. **`calibration` — Calibration & abstention.** Fixes "the agent always produced an answer." The calibrator combines three separate signals: grounding sufficiency, a calibrated uncertainty score (the raw score mapped to observed correctness, plus contradiction checks and an out-of-distribution flag), and a risk-tier threshold per task. "Abstaining ... is a successful outcome here, not a failure."
4. **`safety` — The deterministic safety layer.** Fixes the case where a confident, grounded recommendation still violates a hard rule. Each check returns `pass|block|warn|missing_data`; the layer fails closed; rule versions are recorded per case; rule content has a clinical/pharmacy ownership and release workflow with an expedited path that still passes review.
5. **`gate` — Clinician sign-off (recommend, never act).** Fixes "a recommendation could be treated as an action." It adds a case state machine, a triaged worklist, soft claims, a `case_version` optimistic-concurrency check (409 on stale), sign-off idempotency, expiry, and an explicit `ehr_write_failed` state.
6. **`privacy` — PHI scoping, confidentiality & the safety case.** Fixes the absence of isolation and defensibility. Retrieval is identity-scoped; notes and records are untrusted and partitioned from EHR write authority; audit is kept in two layers (PHI access versus recommendation); break-glass, minimum-necessary access and retention tiers get a deep dive.
7. **`eval` — Workflows & safety evaluation.** Fixes "only accuracy was measured." It adds harm-weighted evaluation (confident-wrong rate, abstention precision/recall, calibration drift), slicing per specialty and task, staged rollout, incident review, and metrics on the human gate itself.

### 1.4 Final architecture

Nodes (`highLevelArchitecture.nodes`), grouped by the dataset's `types`:

- **Pipeline group**: `Pipeline` (deterministic DAG orchestrator), `ReasonAgent` ("LLM in a bounded node: drafts a grounded recommendation with an explicit confidence and citations"), `Guidelines` (versioned guideline/formulary/interaction index).
- **Calibration, Safety & Sign-off group**: `Calibrator`, `SafetyLayer`, `AbstainGate`, `Worklist`, `Clinician`.
- **PHI & Audit group**: `PHIScope` (identity-scoped retrieval), `Guardrail` (HIPAA scoping, tenant isolation, untrusted-text screening), `AuditLog`.
- Others: `Request`, `Gateway` (auth, care-team scope), `Inference` (shared serving under BAA/no-train), `EHR` (grounding *and* action surface), `RecStore` (case state machine source of truth), `Identity` ("binds the decision to a licensed clinician principal"), `Observability`, `Patient`.

Key links: `pipe-reason`, `reason-guide`, `reason-phi` → `phi-ehr` (read path goes only through PHIScope); `pipe-cal` → `cal-gate` ("insufficient -> abstain"); `pipe-safety` → `safety-ehr`; `gate-rec` → `rec-worklist` → `worklist-clin`; `clin-id` → `id-ehr` ("write signed-off order/note"). **The write path to the EHR runs only through Identity after a clinician acts**; there is no link from the agent or pipeline to an EHR write.

Agent-specific vs ordinary machinery: only `ReasonAgent` + `Inference` are agentic. `Calibrator` is ML-adjacent (it is a calibration model). Everything else is ordinary distributed-systems machinery: workflow engine, state machine, optimistic concurrency, idempotent writes, WORM audit, IAM/policy.

### 1.5 Reusable patterns

| Pattern (noun phrase) | Where |
| --- | --- |
| Two-sided grounding (domain corpus + subject record) | step 2 `grounding` |
| Evidence bundle with version pins and snapshot timestamp | step 2; `dataModel.evidence_bundle` |
| Stale-data-as-abstention trigger | step 2, step 4 |
| Three-signal calibrator (sufficiency + calibrated score + risk-tier threshold) | step 3 `calibration` |
| Abstention as a first-class successful output | step 3 |
| Risk-tiered thresholds per task type | step 3; API `taskType`/`riskTier` |
| Deterministic safety floor with fail-closed `missing_data` | step 4 `safety` |
| Versioned rule content with owner review and expedited path | step 4 |
| Recommend-only gate bound to a human principal | step 5 `gate` |
| Review worklist as a state machine | step 5 |
| Soft claim + optimistic version check at sign-off | step 5 deepDive "Concurrent review & sign-off idempotency" |
| Idempotent human decision (sign-off key) | step 5; API `/signoff` |
| Revalidate-before-write against current snapshot | step 5 deepDive "EHR write contracts" |
| Unknown-outcome reconciliation by read-back | step 5 deepDive |
| Explicit write-failure state (`ehr_write_failed`) | step 5 |
| Two-layer audit (access audit vs decision audit) | step 6 `privacy` |
| Minimum-necessary retrieval by task type | step 6 deepDive |
| Break-glass as a named, alertable workflow | step 6 deepDive |
| Retention tiers separating raw traces from the safety case | step 6 deepDive |
| Untrusted record text partitioned from write authority | step 6 |
| Harm-weighted, sliced, continuous evaluation | step 7 `eval` |
| Measuring the human gate (rubber-stamp signal) | step 7 deepDive |
| Admission control that sheds work rather than safety | capacity "Backpressure"; step 5 concept |

### 1.6 Design decisions and trade-offs

- **Calibration** (step 3 options): "Risk-tiered thresholds + calibrated evaluator (default)" vs "Single global threshold on the model self-score". Rejected because "A model self-score is poorly calibrated and gameable" and "One threshold over-abstains on low-risk lookups and under-abstains on high-risk dosing — the worst of both." Cost of the chosen option: per-task ground-truth sets, calibration curves, and "Threshold sprawl needs governance".
- **Safety on missing data** (step 4 options): "Fail closed on missing/stale facts (default)" vs "Fail open when facts are missing". Key line: "A blank allergy list never reads as 'no allergies'; absence of data is not evidence of safety." Cost: more abstentions and clinician load.
- **Gate** (step 5 options): "Recommend-only: clinician authorizes every action (default)" vs "Direct EHR write for 'low-risk' actions". Rejected because "'Low-risk' is itself a clinical judgment that can be wrong" and it "Moves responsibility and the regulatory line onto the platform."
- **Worklist coverage vs alert fatigue** (step 5 tradeoffs): routing everything to humans "quietly destroys the value of the gate itself"; triage plus abstention surfacing keep review meaningful.
- **technologyChoices** highlights:
  - Guideline index: "Hybrid keyword plus vector retrieval is safer than pure vector search for clinical lookups because exact drug names ... matter"; "The corpus registry is the source of truth; search indexes should be derived views."
  - Model serving: managed inference "is only acceptable for PHI under a signed BAA with no-train and no-retention controls that the safety case can cite"; "Tool isolation and prompt-injection defenses still live in the application harness, regardless of where the model runs."
  - Orchestration: Temporal/Camunda/Step Functions make the DAG "explicit, retryable, and observable without giving the model autonomous control of the loop"; "A lighter queue plus application state machine can be enough at this QPS."
  - Store: relational, because "reviewers need consistent joins and optimistic version checks"; "A stream is useful for audit ... but the source-of-truth state machine still needs transactional idempotency."
  - Safety rules: Drools/OPA + licensed drug data (RxNorm, First Databank); "makesIrrelevant: ... removes prompt-based contraindication checks."
  - Audit: "Append-only Postgres + hash chain", WORM; "a mutable analytics table alone does not" make the safety case defensible.
  - Eval: "LLM-as-judge can triage trajectories, but clinician adjudication remains the ground truth."

### 1.7 Failure modes and containment

| Failure mode | Containment |
| --- | --- |
| Confident wrong answer | calibrator + abstention (step 3) |
| Guideline-correct but wrong for this patient | two-sided grounding + safety layer (steps 2, 4) |
| Missing allergy list read as "none" | `missing_data` fails closed (step 4) |
| Chart changed between draft and sign-off | snapshot timestamp + revalidate before write, If-Match (steps 2, 5) |
| Two clinicians race; stale revision signed | `case_version` check, 409 `stale_version` (step 5) |
| Double-click / timeout retry / lost EHR response | sign-off `idempotencyKey`, correlation id, read-back reconcile (step 5) |
| EHR write fails | explicit `ehr_write_failed`, retryable (step 5) |
| Case lingers unreviewed | `expired` state, escalation (step 5) |
| Alert fatigue, rubber-stamping | triage, queue-age p95 target, rubber-stamp metric (steps 5, 7) |
| Cross-patient PHI leak | PHIScope identity scoping, fresh care-team check (step 6) |
| Unauthorized access hidden behind "no recommendation" | separate PHI-access audit (step 6) |
| Injected note steers a write | notes untrusted, partitioned from write authority (step 6) |
| Rule regression or urgent new interaction | versioned rules, owner review, rollback, expedited path (step 4) |
| Model or threshold drift | drift detection, staged rollout, incident review (step 7) |
| Overload | admission control sheds non-urgent work, not safety (capacity) |

### 1.8 Domain constraints

Domain-specific: HIPAA/BAA, PHI, SaMD/FDA framing, licensed drug-interaction data, FHIR/HL7 EHR integration, care-team membership, break-glass access, licensed clinician as the regulatory and liability holder.

Broadly applicable: irreversibility drives the gate's position; abstain-over-guess; deterministic floors for never-events; human throughput as a capacity limit; measuring the human gate; separate access audit from decision audit; minimum-necessary context per task (also a cost and latency lever); idempotent human decisions; revalidating before acting on a stale snapshot.

Latency and volume: interactive (< 6 s p95), moderate volume (~500k/day). Human review capacity, not compute, is the binding constraint.

### 1.9 API and data-model snippets (exact)

`POST /v1/recommendations` request (`api[0].request`):

```json
{ "idempotencyKey": "...", "tenantId": "...", "clinicianId": "...", "patientId": "...", "encounterId": "...", "careTeamId": "...", "taskType": "dosing|differential|guideline_lookup|chart_summary", "riskTier": "low|moderate|high", "urgency": "routine|urgent", "query": "...", "consent": { "breakGlass": false } }
```

Response: `{ "caseId": "...", "status": "awaiting_signoff|abstained|blocked_by_safety", "abstainReason": "...|null" }`

`POST /v1/recommendations/{id}/signoff` request (`api[3].request`):

```json
{ "idempotencyKey": "...", "caseVersion": 3, "decision": "authorize|modify|reject|request_evidence", "action": { "type": "order|note|message|chart_summary", "payload": {...} }, "modification": "...|null", "rejectReason": "...|null", "attestation": true }
```

Response includes `"status": "authorized|modified|rejected|awaiting_evidence|ehr_write_failed|stale_version"` and `"ehrWrite": { "status": "succeeded|failed|pending", ... }`.

Case status enum (`dataModel.recommendation_case.status`): `enum(drafted,blocked_by_safety,abstained,awaiting_signoff,modified_by_clinician,authorized,rejected,expired,ehr_write_failed)`.

Safety-check result (`dataModel.safety_checks`): `kind enum(contraindication,interaction,allergy,dose)`, `result enum(pass,block,warn,missing_data)`, plus `rule_version`.

Calibration record (`dataModel.calibration_result`): `grounding_sufficient bool`, `calibrated_score numeric`, `threshold_used numeric`, `ood_flag bool`.

Audit (`dataModel.audit_record`): `category enum(phi_access,recommendation)`, note "PHI-access events are recorded even when no recommendation is authorized."

`case_transition` note: "Append-only state-machine history: one row per state change, with the actor, case version reviewed, and idempotency/correlation keys that distinguish a double-click from a retried request from a lost EHR response."

### 1.10 Weaknesses and inconsistencies

REVIEW.md (`agentic-healthcare-platform/REVIEW.md`, 2026-06-25) issues, checked against the current JSON:

- P1 transition history and sign-off idempotency: **fixed** (`case_transition`, `case_assignment`, `/claim` endpoint, sign-off `idempotencyKey`, deepDive "Concurrent review & sign-off idempotency").
- P1 EHR write contracts: **fixed** (step 5 deepDive "EHR write contracts at the failure boundary"; the technologyChoices FHIR row).
- P2 PHI policy (break-glass, minimum-necessary, revocation, retention): **fixed** (step 6 deepDive "Operational PHI policy").
- P2 option titles null: **still true in the data**. Options carry `name` but `title: null`. Whether this matters depends on which field the renderer reads; for the book it does not.
- P3 isolated `Identity` node in the privacy view: **fixed** (the view now includes link `id-phi`).
- P3 human-gate metric in eval: **fixed** (step 7 deepDive, last point).
- Rule ownership workflow (step 4 suggestion): **fixed** (step 4, third paragraph).

Remaining issues I noticed:

- **Two `case` status vocabularies.** `recommendation_case.status` uses `modified_by_clinician`, while the sign-off response returns `modified`, `awaiting_evidence` and `stale_version`. `awaiting_evidence` is not in the case enum, and `stale_version` is a response code rather than a state. The `RecStore` node description also says `modified`.
- **Calibrator is "deterministic" but contains a learned mapping.** The `Calibrator` node says "Deterministic check of grounding sufficiency and calibrated confidence", yet step 3 says the score is "the raw model score mapped onto observed correctness". The *decision rule* is deterministic, but the score depends on a fitted calibration model that drifts (step 3 says so). The book should say that the threshold rule is deterministic and the calibration curve is a versioned model artifact.
- **Order of calibration and safety.** The step order is calibrate then safety, and the `Pipeline` description lists "retrieve -> reason -> calibrate -> abstain-or-recommend -> clinician sign-off" without naming safety. The final design runs safety after calibration. Both orders can work, but the pipeline string omits the safety node.
- **Duplicate concept entries** in step 1 ("Agent harness (runtime scaffold)" and "Agent harness (from Foundations)") say the same thing.
- **No injection containment mechanism named** beyond "partitioned from EHR write authority". The concept cites CaMeL / Dual-LLM / Plan-then-Execute, but the architecture does not show which one is used. The research platform's structured-IR boundary is the concrete version of this.
- Accuracy claims are flagged "VERIFY BEFORE PUBLISHING" (step 6 deepDive): the dataset itself says any accuracy figure is dated.

### 1.11 Best uses in the book

- **Foundations / autonomy spectrum**: the "recommend, never act" end of the spectrum; the irreversibility gradient (Finance < Legal < Healthcare).
- **Reference architecture**: a bounded LLM node inside a deterministic DAG, with deterministic services around it.
- **Context/memory/state**: two-sided grounding, evidence bundles with version pins, minimum-necessary context by task, snapshot freshness.
- **Reliability/recovery**: idempotent human decisions, the unknown-outcome write, revalidate-before-write, explicit failure states.
- **Security/oversight**: the strongest human-oversight chapter material. It covers abstention, the review worklist as a state machine, alert fatigue, rubber-stamp metrics, break-glass, two-layer audit, and the safety case.
- **Evaluation/observability**: harm-weighted evaluation, abstention precision/recall, the confident-wrong rate, clinician adjudication over LLM-as-judge, and measuring the gate.
- **Performance/economics**: human review capacity as the throughput ceiling; admission control that sheds work rather than safety.

---

## Source 2 — Agentic Public Benefits Platform

Path: `system-design-interviews/data/book/agentic-public-benefits-platform/interview.json`

### 2.1 Summary

A government benefits / eligibility platform covering intake, evidence gathering, eligibility determination and renewals. The users are applicants (claimants), caseworkers (accountable public servants) and independent appeals reviewers. If it fails, a citizen's rights are affected: a wrongful or opaque denial is a due-process failure under administrative law, and systematic inconsistency is "itself an injustice" (step 6). The central idea is a new gate dimension, **contestability**: "the gate produces a contestable decision by construction" (step 4). The model extracts evidence and drafts explanations; a deterministic rule engine on effective-dated, jurisdiction-tagged rule packages decides; a caseworker decides every adverse outcome; the record is built for appeal, not only for compliance; and a fairness monitor watches matched cohorts at population scale.

### 2.2 Requirements and capacity (dataset's illustrative assumptions)

Functional: intake and evidence extraction; determination under "the correct statute/rules for the applicant's date and jurisdiction"; plain-language explanation; route every adverse determination to an accountable caseworker; an appeal path to an independent reviewer.

Non-functional: contestability / due process; "A deterministic rule engine produces the determination; the model assists and explains but cannot override it"; "Adverse decisions are decided by an accountable human, never finalized by the agent"; consistency and fairness at population scale; PII privacy and a legible record.

Capacity (`capacity`):

| Item | Value | Note |
| --- | --- | --- |
| Applications | ~20k/day (5–10x at open enrollment) | surges must be queue-levelled |
| Evidence per application | ~5–15 pages | pay stubs, IDs, official records |
| Adverse rate | ~25% adverse-pending | sets the human backlog |
| Caseworker throughput | ~40 decisions/worker/day | bounds drain rate |
| Appeal rate | ~5% of denials | "the appeal window starts at notice delivery, not at decision" |
| Re-determination load | bulk on rule change | batch re-determination of open cases |
| Adverse decisions | human-decided | |
| Determination | deterministic | |
| Failure behavior | fail-safe, never auto-deny | "the case holds in evidence_needed / adverse_pending rather than defaulting to a denial" |

Derived (not in the dataset; my arithmetic, label it as such if used): 20k/day × 25% = ~5k adverse-pending/day; at 40/worker/day that needs ~125 caseworker-days per day in steady state and 5–10x that at enrollment peaks. This is why the queue is a due-process component.

### 2.3 Evolution path

1. **`naive` — An agent that decides eligibility.** Failure: an opaque model-made denial. "the applicant cannot see the rule version that decided their case, correct the evidence that was used, identify an accountable decision-maker, or appeal from a complete record."
2. **`grounding` — Ground in effective-dated, jurisdiction-tagged rules.** Fixes stale or wrong-jurisdiction rules. "A rule package is legally governed data, not just indexed text": it carries source authority and approval provenance. Applications are untrusted input.
3. **`rules` — A deterministic rule engine (the model doesn't decide).** Fixes model-made outcomes. The LLM is confined to extract-and-explain nodes. Rule packages are pinned per determination, tested against golden cases, legally reviewed and rolled back when needed; surges are absorbed by admission control and bounded batch re-determination.
4. **`gate` — Caseworker decides, decision is contestable.** Fixes the opaque, final adverse decision. Adds an adverse-review queue (priority, SLA aging, retry, deadline escalation) and the caseworker actions `approve|deny|override_to_eligible|request_more_evidence`; an override is flagged for supervisor review and feeds rule-correction signals.
5. **`audit-appeal` — Audit-for-appeal & the appeal path.** Fixes "Records served compliance, not the applicant." Adds a NoticeService (language and accessibility, appeal clock started on delivery), a materialized appeal packet, and an independent reviewer with an explicit `upheld|reversed|remanded` outcome.
6. **`fairness` — Bias-at-scale.** Fixes "Fairness was assumed from individual correctness." Adds matched-cohort analysis, caseworker outlier detection, a remediation escalation ladder, and protected attributes held in a separate analytics partition that never touches the determination path.
7. **`compliance-eval` — Due-process compliance & evaluation.** Fixes "Only accuracy was measured." Adds golden determinations, reviewer replay tests, readability and accessibility checks, time-based obligation checks, and adversarial document-injection tests.

### 2.4 Final architecture

Groups (`types`):

- **Determination Pipeline**: `Pipeline` ("Deterministic DAG: gather evidence -> apply rules -> explain -> caseworker decision"), `IntakeAgent` ("extracts evidence and drafts a plain-language explanation. It does not decide."), `RuleEngine` ("The model cannot override it."), `RuleIndex`.
- **Decision & Due Process**: `DecisionGate` ("the agent never finalizes an adverse decision"), `ReviewQueue`, `Caseworker`, `DecisionStore`, `AppealPath`, `NoticeService`.
- **Fairness & Audit**: `FairnessMonitor`, `Guardrail`, `AuditLog`.
- Others: `Applicant`, `Reviewer`, `Application`, `Gateway`, `Inference`, `CaseRecord`, `Identity` ("binds an adverse decision to an accountable caseworker"), `Observability`.

Key links: `pipe-intake`/`intake-infer` (the LLM path) are separate from `pipe-rules` → `rules-index` ("current rule for date/jurisdiction"). `pipe-gate` → `gate-queue` → `queue-cw` → `cw-id` → `id-decision`. `pipe-notice` → `notice-appl` and `notice-decision` ("record delivery, start appeal clock"). `decision-appeal` → `appeal-reviewer`. `gate-fair` → `fair-obs`.

Agent-specific: only `IntakeAgent` + `Inference`, and the model has **two jobs**: extraction (input side) and explanation (output side). Everything else is rules engines, workflow, queues, notices, identity and analytics.

### 2.5 Reusable patterns

| Pattern | Where |
| --- | --- |
| Model assists, engine decides | step 3 `rules` (concept name) |
| Effective-dated, jurisdiction-tagged rule packages pinned per decision | steps 2–3; `determinations.rule_package_id` |
| Rule package as governed data (source authority, approval provenance) | step 2 |
| Golden-case regression on every rule or model change | step 3 deepDive; step 7 |
| Bounded batch re-determination on rule change | step 3 deepDive; capacity |
| Asymmetric gate (favourable auto-finalizes, adverse goes to a human) | step 4 flow (`eligible` vs `adverse outcome`) |
| Fail-safe hold, never auto-deny | capacity "Failure behavior" |
| Deadline-aware review queue with SLA aging and escalation | step 4; `ReviewQueue` |
| Human override with recorded rationale and supervisor flag | step 4; `/decide` |
| Override as a rule-correction signal | step 4 deepDive |
| Contestable decision (rules + evidence + plain reasons) | step 4 concept |
| Audit-for-appeal record (legible to the affected person) | step 5 concept |
| Materialized appeal packet | step 5 option (chosen) |
| Notice service that owns the due-process clock | step 5 |
| Independent reviewer (not the original decider) | step 5; `/v1/appeals/{id}/decide` |
| Two-axis lifecycle (workflow status vs outcome) | `dataModel.determinations` note |
| Evidence items with provenance, confidence and human correction | `dataModel.evidence_items` |
| Matched-cohort fairness monitoring | step 6 |
| Protected attributes partitioned off the decision path | step 6 deepDive |
| Remediation escalation ladder with thresholds defined up front | step 6 deepDive |
| Reviewer-replay test (can someone re-decide from the record alone?) | step 7 |
| Adversarial document-injection test | step 7 |

### 2.6 Design decisions and trade-offs

- **Rule representation** (step 3 options): policy-as-code vs DMN decision tables vs a custom rules service. **Chosen: policy-as-code**, "because testability against golden cases and versioned, reviewable changes outweigh the legibility edge of decision tables, accepting that rule changes require an engineering deploy." Note the tension with the technologyChoices row: "DMN decision tables are legible to policy and legal reviewers and map cleanly to statute ... Policy-as-code ... needs a stronger approval workflow so legal meaning does not hide in application code." In a contestability-first domain, choosing the *less legible* option is a debatable decision and a good discussion point for the book.
- **Review model** (step 4): "Queued adverse-pending review with SLA" vs "Synchronous blocking review". Chosen: the queue, because synchronous review "Collapses under surge" and "fails silently by delay".
- **Appeal record** (step 5): "Materialized appeal packet" vs "Event-log replay". Chosen: materialized, because "a frozen, self-contained record the reviewer can open immediately is worth paying write cost". The replay option's risk is named: "Replay logic must be versioned so an old case reconstructs under the rules it actually used."
- **Fairness** (step 6): "Matched-cohort analysis" vs "Aggregate-rate dashboards" ("Confounds composition with bias").
- **technologyChoices** highlights: document intake with OCR "create[s] another provenance boundary to audit"; the rule corpus uses "A relational package registry ... search indexes should remain derived views"; a model gateway "centralizes model choice, prompt templates, redaction, caching, and token budgets while keeping the model outside the decision boundary"; WORM audit "increases the cost of correcting mistakes, so redaction and retention classes must be designed up front"; fairness analytics: "a dashboard should surface review, not declare legality"; delegated act claims "remove shared service accounts from the adverse-decision path."

### 2.7 Failure modes and containment

| Failure mode | Containment |
| --- | --- |
| Opaque model denial | rule engine decides; caseworker owns adverse outcomes (steps 3–4) |
| Wrong rule version or jurisdiction | effective-dated, jurisdiction-tagged, pinned packages (step 2) |
| Rule change silently alters past decisions | package pinned per determination (step 3 deepDive) |
| Bad rule release | golden-case tests, legal review, rollback (step 3) |
| Surge at open enrollment | admission control + adverse-review queue (steps 3–4) |
| "Human in the loop" becomes failure-by-delay | SLA aging, deadline escalation, backlog metrics (step 4) |
| Delayed lookup, extraction or assignment defaults to denial | fail-safe hold in `evidence_needed`/`adverse_pending` (capacity) |
| Duplicate case on retry | idempotency key on `POST /v1/determinations` and `/evidence` |
| Missed appeal window | clock starts at notice delivery; tracked per case (step 5) |
| Applicant cannot understand the notice | language and accessibility handling; readability checks (steps 5, 7) |
| Reviewer not independent | the reviewer must not be the original decider (step 5) |
| Injected document alters a determination | text partitioned from rule engine; injection tests (steps 5, 7) |
| Systematic disparity | matched cohorts, outlier detection, remediation ladder (step 6) |
| Protected attributes leak into a decision | separate analytics partition (step 6) |

### 2.8 Domain constraints

Domain-specific: administrative due process (notice, explanation, right to appeal), statutory appeal deadlines, effective-dated statute, jurisdiction, caseworkers as accountable public servants, protected attributes, multilingual and accessible notices.

Broadly applicable: separate the decision engine from the language model; pin the policy version per decision; give the human an explicit override with a rationale; build records for the *affected party*, not only the auditor; treat human backlog as a correctness concern; asymmetric gating by outcome direction; population-level monitoring as distinct from per-case correctness.

Reversibility: an adverse decision is reversible on appeal but costly to the person, and time matters (deadlines). It is the "contestability" axis rather than the "irreversibility" axis. Volume is high and bursty; latency is days, not seconds.

### 2.9 API and data-model snippets (exact)

`POST /v1/determinations/{id}/decide` request: `{ "decision": "approve|deny|override_to_eligible|request_more_evidence", "rationale": "...", "supervisorEscalation": "... (optional)" }`

`POST /v1/appeals/{id}/decide` description: "An independent reviewer disposes of an appeal from the record; the reviewer must not be the original decider." Request: `{ "outcome": "upheld|reversed|remanded", "rationale": "..." }`

`POST /v1/determinations/{id}/notice` description: "Deliver the legible notice to the applicant in their language/format and start the statutory appeal-deadline clock." Request: `{ "channel": "...", "language": "...", "accessibility": { ... } }`

Two-axis model (`dataModel.determinations`):

- `status`: `enum(submitted,evidence_needed,determination_ready,adverse_pending,finalized,noticed,appealed,reviewer_decided) -- workflow state`
- `outcome`: `enum(eligible,denied,upheld,reversed,remanded) null -- eligibility/review result`
- `rule_package_id`: `varchar (pinned version)`; `rules_applied`: `jsonb (trace with versions)`

`evidence_items`: `source enum(applicant_doc,official_record,attestation)`, `extracted_value jsonb`, `confidence float`, `human_correction jsonb null`, `retention_class varchar`.

`explanations`: `reason_text`, `language`, `rule_refs jsonb`, `evidence_refs jsonb`. The explanation is tied by reference to rules and evidence, so it is not free text.

### 2.10 Weaknesses and inconsistencies

REVIEW.md (`agentic-public-benefits-platform/REVIEW.md`, 2026-06-24) issues, checked against the current JSON:

- P1 lifecycle vocabulary: **largely fixed**. There are now two axes and the API uses `approve|deny|override_to_eligible|request_more_evidence`.
- P1 queue invisible: **fixed** (`ReviewQueue` node and links `gate-queue`, `queue-cw`).
- P2 notice/evidence loop: **fixed** (`NoticeService` node; `/evidence` and `/notice` endpoints).
- P2 protected-attribute governance: **fixed** (step 6 deepDive "Protected-attribute governance").
- P3 more option sets: **fixed** (steps 4, 5, 6 now have options).
- The time-based-obligation eval (step 7 suggestion): **fixed**.
- Still open from the review: retention and deletion only hinted at by `retention_class`; no multi-agency or multi-jurisdiction tenancy.

Remaining issues I noticed:

- **`approve` is ambiguous.** On an `adverse_pending` case, "approve / deny accept the engine result". It is unclear whether `approve` means "approve the adverse result" (deny the benefit) or "approve eligibility". Both `approve` and `deny` are described as accepting the engine result, so on an adverse case they should mean the same thing. The book should rename this to something like `confirm_adverse | override_to_eligible | request_more_evidence`.
- **`GET /v1/determinations/{id}` status list is incomplete**: `adverse_pending|finalized|noticed|appealed|reviewer_decided` omits `submitted`, `evidence_needed` and `determination_ready`, which are in the data-model enum.
- **`remanded` has no defined next state.** A remand should re-open the case (back to `determination_ready` or `adverse_pending`), but no transition is given.
- **The human decision is not idempotent or version-checked.** `/decide` and `/appeal` carry no idempotency key and no case version, and `status_history` records only `from/to/actor/at`. Compare the healthcare `case_transition` (version, idempotency key, correlation id) and the healthcare 409 `stale_version`. Two caseworkers could finalize the same adverse case; the dataset is silent on this.
- **No access audit layer.** `audit_record.kind` is `enum(evidence,rule,explanation,decision,notice,appeal)`. There is no PII-access category, unlike healthcare's two-layer audit, although step 5 says "PII is scoped and access is logged."
- **The favourable path has no human.** The step 4 flow finalizes `eligible` directly. This is a deliberate asymmetric gate, but the dataset never states the risk: an erroneous *approval* (fraud, over-payment) has no human check. Healthcare, by contrast, sends every recommendation to a human. The book should make the asymmetry explicit.
- **Policy-as-code chosen in a legibility-first domain** (see 2.6). The step 3 option and the technologyChoices row pull in different directions.
- **Explanation drafted by an LLM is not grounded by a validator.** The explanation carries `rule_refs` and `evidence_refs`, but nothing checks that the LLM's plain-language text matches the rule trace. The eval measures "explanation quality", but there is no runtime check. This is a gap against the research platform's claim-level citation spans.
- **Extraction confidence is stored but unused.** `evidence_items.confidence` exists, but no step says what happens when it is low (contrast with the healthcare calibrator). A low-confidence extraction should route to `evidence_needed` or caseworker review.

### 2.11 Best uses in the book

- **Foundations**: the contestability axis as a third gate dimension, alongside irreversibility (healthcare) and physical actuation (research).
- **Reference architecture**: the clearest "model assists, engine decides" split; the LLM on both the input side (extraction) and the output side (explanation).
- **Security/oversight**: due process as architecture; explainability-for-appeal; independent review; the override as a signal; fairness at scale; protected-attribute partitioning; injection tests.
- **Orchestration / reliability**: the adverse-review queue with SLA and deadline escalation; fail-safe holds; batch re-determination.
- **Context/memory/state**: two-axis lifecycle; pinned rule packages; evidence with provenance and human corrections.
- **Evaluation/observability**: contestability eval, reviewer replay, time-based obligation SLOs, golden determinations.
- **Deployment/evolution**: rule-package release with golden tests and rollback; batch re-determination as the cost of a rule change.

---

## Source 3 — Agentic Research Platform

Path: `system-design-interviews/data/book/agentic-research-platform/interview.json`

### 3.1 Summary

A platform for scientific-research agents covering literature review, hypothesis generation, experimental design, and running experiments through lab automation. The users are principal researchers and biosafety officers. Failure takes two forms (step 1): **physical** irreversibility (reagents consumed, equipment damaged, biosafety/dual-use hazards) and **scientific** irreversibility (claims without provenance cannot be reproduced). The central idea is a **wet-lab boundary**: "The agent proposes; a human authorizes anything physical" (top-level `description`). The model drafts a structured protocol IR with citation spans; a deterministic validator screens it (fail-closed, versioned); a human signs a scoped, expirable authorization object bound to the protocol's content hash; and an **execution controller** that is "the only component allowed to submit lab jobs" turns the authorization into exactly-once physical actuation. Provenance is captured at write time, from claim span to run artifact.

### 3.2 Requirements and capacity (dataset's illustrative assumptions)

Functional: review literature and prior data; generate hypotheses and protocols with citations; validate deterministically before any physical action; human authorization for any experiment that "consumes reagents, drives a lab robot, or has biosafety implications"; run authorized protocols and capture results.

Non-functional: reproducibility is first-class; a deterministic validator the model cannot override; no physical run without human authorization (dry-run vs wet-lab tiering); "Physical actuation is exactly-once: a retry after an ambiguous timeout must never double-run an experiment"; dual-use hazards blocked before authorization; a complete lab-notebook audit.

Capacity (`capacity`):

| Item | Value | Note |
| --- | --- | --- |
| Literature corpus | ~80M docs, +50k/day | retraction and quality signals |
| Retrieval QPS | ~500 q/s peak | cacheable per corpus version |
| Protocol proposals | ~2k/day | LLM-heavy design passes |
| Validations | ~50/sec peak | "throughput is rarely the limit here" |
| Dry-run simulations | ~1.5k/day | "Free for the agent" |
| Authorized wet-lab runs | ~50–150/day | "the real throughput ceiling" |
| Lab robot concurrency | ~10–40 instrument slots | "runs queue against reservations, not CPU" |
| Run duration | minutes → days | drives durable execution, leases, callbacks |
| Result data / run | ~10MB–50GB | object storage |
| Audit events / run | ~50–200 events | |
| Retention | years (regulatory) | storage grows monotonically |

The funnel (2k proposals → 1.5k dry-runs → 50–150 wet-lab runs on 10–40 slots) is a strong figure for the economics chapter: the scarce resource is physical, then human, and only then compute.

### 3.3 Evolution path

1. **`naive` — An agent that runs experiments autonomously.** Failure: unsupervised actuation, plus unreproducible claims. The naive view has a direct `hypo-robot` link ("actuate directly (naive)").
2. **`grounding` — Ground in primary literature + prior data.** Fixes claims from model memory. Ingestion captures "citation spans (the exact passage supporting a claim), versioned corpora, and freshness/retraction/quality signals"; "Every claim carries a citation from the start." Papers and datasets are untrusted.
3. **`validation` — Deterministic protocol validation.** Fixes a protocol going straight to the lab. The validator consumes a "structured protocol IR (typed steps, reagents, quantities, instruments), not the model's free-text prose", so "an injected instruction in a paper can't smuggle past prose parsing." Rules are versioned, fail closed, and risk-tiered.
4. **`gate` — Human authorization for any physical run.** Fixes autonomous actuation. A durable approval workflow produces an authorization object (signer chain, scope, expiry, revocation) bound to the version/hash; dry-runs are free.
5. **`execution` (4a, `parent: gate`) — Durable lab execution.** Fixes the gap where "'Authorized' is not 'safely executed exactly once'". The execution controller adds reservations, an idempotency key, a short-lived run token, a lease and checkpoints, signed callbacks, abort, and reconcile-on-timeout; "The robot rejects any job lacking a valid token."
6. **`reproducibility` — Reproducibility & provenance.** Fixes "Results had no traceable origin." Lineage is captured at write time: claim → span + corpus snapshot; datum → run, artifact checksum, protocol version, conditions, analysis-code version.
7. **`biosafety` — Dual-use & biosafety screening.** This is "the adversarial hardening pass over the validation introduced in Step 3". It separates hard-blocked (un-overridable) from needs-biosafety (routed to an officer); untrusted text never reaches the safety decision.
8. **`eval` — Workflows & scientific-reliability evaluation.** Fixes "Only output plausibility was assessed." Adds replication-weighted evaluation and concrete metrics plus operational alert signals.

### 3.4 Final architecture

Groups (`types`):

- **Research Pipeline**: `Pipeline` ("Deterministic DAG: retrieve -> hypothesize -> design protocol -> validate -> authorize -> run"), `HypoAgent` (bounded LLM node), `LitIndex`.
- **Validation & Authorization**: `ProtocolCheck` (deterministic; "dual-use/biosafety rules the model cannot override"), `ExperimentGate` ("dry-run vs wet-lab tier"), `Researcher`, `Safety` (biosafety officer).
- **Durable Lab Execution**: `ExecCtrl`, `Simulator` ("never actuates the physical world"), `LabRobot` ("Rejects any job lacking a valid authorization/run token").
- **Reproducibility & Audit**: `Provenance`, `DataStore`, `AuditLog` ("Audit / Lab Notebook").
- Others: `Goal` (research console), `Gateway` (lab/tenant scope), `Inference`, `Guardrail`, `Identity` ("binds a wet-lab authorization to a researcher / biosafety principal"), `Observability`.

Key links: `gate-exec` ("authorization object (scoped, signed)"), `exec-id` ("mint run token"), `exec-robot` ("submit run (idempotency key + token)"), `robot-exec` (callback), `exec-sim` ("dry-run (no authorization needed)"), `exec-data` ("write immutable run record"), `check-gate` ("blocked -> stop"). The naive `hypo-robot` link is excluded from the final view.

Agent-specific: only `HypoAgent` + `Inference`. The capability boundary (structured IR in, run token out) is enforced by non-agent components: the validator, the token broker, the execution controller, and the robot's own token check. This is **defence in depth at the actuator**: even if every upstream check failed, the robot refuses untokened jobs.

### 3.5 Reusable patterns

| Pattern | Where |
| --- | --- |
| Claim-level citation spans pinned to a corpus snapshot | step 2; `claim_provenance` |
| Versioned, content-addressed corpus with retraction flags | step 2 option (chosen) |
| Structured IR as the injection boundary (validate typed fields, never prose) | step 3; step 6 |
| Fail-closed policy evaluation on policy-service outage | step 3 concept "policy versioning & fail-closed" |
| Risk-tiered escalation to a specialist approver | step 3 option; step 6 |
| Hard block vs needs-review as distinct outcomes | step 6 |
| Dry-run vs wet-lab capability tiers ("free" vs gated) | step 4 |
| Authorization object (not a flag): version-hash, signer chain, scope, expiry, revocation | step 4 concept |
| Approval bound to content hash | API `/authorize` (`versionId`, `contentHash`) |
| Durable approval decoupled from execution | step 4 option (chosen) |
| Two-tier state machine (readiness vs run) | step 4 concept; `protocols` / `run_attempts` |
| Single actuation broker ("only component allowed") | step 4a `execution` |
| Short-lived scoped run token minted per run | step 4a; `exec-id` |
| Actuator-side token check (defence in depth) | `LabRobot` node |
| Idempotency key for physical actuation | step 4a concept |
| Run lease with reconcile-on-timeout ("query before retry") | step 4a flow |
| `unknown` as an escalation state, never a retry | API `/reconcile` |
| Signed, sequence-numbered callbacks with replay protection | API `/callbacks` |
| Revocation semantics per lifecycle phase | API `/authorizations/{id}/revoke` |
| Scarce-resource reservation separate from submission | step 4a option (chosen); `instrument_reservations` |
| Write-time lineage (not post-hoc reconstruction) | step 5 option (chosen) |
| Artifacts by reference with checksum and `derived_from` lineage | `run_artifacts` |
| Replication-weighted evaluation | step 7 option (chosen) |

### 3.6 Design decisions and trade-offs

- **Corpus** (step 2): "Versioned corpus snapshots + retrieval (chosen, hybrid)" vs "Retrieval-only RAG over a live index" ("Not reproducible — the index moves under you") vs "Frozen curated corpus only" ("Stale fast"). Accepted cost: "pinning can hide newer evidence unless freshness is surfaced."
- **Validation** (step 3): "Deterministic rule engine over a structured IR (chosen, hybrid)" vs "Model-as-judge safety review" ("can be wrong or prompt-injected via the very paper text it reviews") vs "Pure deterministic rule engine (no tiering)" ("Either too strict ... or too loose").
- **Authorization** (step 4): "Durable approval workflow (chosen)" vs "Synchronous approval inside the API request" ("Wet-lab runs take minutes to days") vs "Out-of-band ticket / e-signature only" ("Authorization scope isn't bound to the exact protocol version/hash"). Tradeoff line: "an approval that cannot name exactly what it approved cannot safely gate physical execution."
- **Execution** (step 4a): "Durable workflow engine + reservation service (chosen)" vs "Plain queue + reservation" ("At-least-once queue delivery fights exactly-once actuation") vs "Direct robot API from the pipeline" ("an ambiguous timeout becomes a blind retry that double-actuates"). Named as "the highest-blast-radius bug in the system."
- **Provenance** (step 5): "Lineage captured at write time (chosen)" vs "Post-hoc lineage extraction" ("Lossy ... the gaps surface exactly when you need to reproduce a result").
- **Eval** (step 7): "Replication-weighted evaluation (chosen)" vs "Output plausibility scoring" ("Plausibility is not truth; rewards confident fabrication") vs "Citation precision only" ("A well-cited claim can still fail to replicate").
- **technologyChoices** highlights: the token broker "removes the need to pass user credentials or long-lived API keys into instrument adapters"; provider guardrails "do not replace the structured protocol IR or the fail-closed validator"; Temporal/Cadence fit "multi-day physical runs because leases, timers, callbacks, retries, and replay are core concepts", while managed step engines "may constrain history size, maximum duration"; "Conditional writes plus unique idempotency keys remove the need for best-effort duplicate detection"; lab adapters (SiLA 2, OPC UA, Opentrons) versus vendor SDKs, which "fragment idempotency, abort, calibration, and replay-protection semantics"; a "narrow adapter boundary prevents the hypothesis agent, notebook UI, or generic workflow steps from ever submitting physical lab commands directly."

### 3.7 Failure modes and containment

| Failure mode | Containment |
| --- | --- |
| Agent actuates the lab directly | execution controller is the only submitter; robot rejects untokened jobs (step 4a) |
| Injected paper steers a hazardous protocol | structured IR + deterministic screening of the IR only (steps 3, 6) |
| Policy service down | fail closed: "validation returns blocked, run never schedules" (step 3) |
| Approval does not match what runs | authorization bound to `versionId` + `contentHash` (step 4) |
| Submission timeout after the robot accepted | query status by idempotency key before any retry (step 4a flow) |
| Missing callback, expired lease | `/reconcile`; `unknown` escalates, is never retried |
| Duplicate or replayed callbacks | signature + sequence number, last-writer-by-sequence (API) |
| Crash mid-run | durable checkpointed saga resumes, does not resubmit (step 4a) |
| Revocation mid-flight | phase-specific effect: never starts / slot released / run aborted |
| Instrument contention | reservations against 10–40 slots |
| Claim cites a later-retracted paper | `claim_provenance.retracted`; corpus snapshot pinned |
| Finding cannot be reproduced | write-time lineage incl. conditions, calibration, analysis-code version |
| Plausible fabrication rewarded | replication-weighted eval |

### 3.8 Domain constraints

Domain-specific: biosafety levels and dual-use research, the biosafety officer role, reagents and instruments, lab automation protocols (SiLA 2, OPC UA), regulatory retention of lab notebooks, replication as the ground truth.

Broadly applicable: tiering capabilities by side-effect class (simulate freely, actuate under authorization); content-hash-bound approvals; a single actuation broker with short-lived tokens; idempotency and reconciliation for any irreversible side effect with ambiguous outcomes; long-running human approvals as durable objects; write-time provenance; structured IR as an injection boundary.

Latency: minutes to days per run, so asynchronous by default. Volume: high on reads (500 q/s retrieval), very low on the irreversible side (50–150 runs/day). Data sensitivity: moderate (tenant/lab data governance, not PHI), but the *hazard* sensitivity is the highest of the three sources (dual-use).

### 3.9 API and data-model snippets (exact)

`POST /v1/protocols` response:

```json
{ "protocolId": "...", "versionId": "...", "contentHash": "...", "riskTier": "low|elevated|restricted", "status": "awaiting_authorization|needs_biosafety|blocked", "validation": { "outcome": "...", "policyVersion": "...", "matchedRules": [], "blockedReason": null } }
```

`POST /v1/protocols/{id}/authorize` request:

```json
{ "versionId": "...", "contentHash": "...", "decision": "authorize|reject|request_changes", "scope": { "instruments": [], "reagentLimits": {} }, "expiresAt": "...", "idempotencyKey": "..." }
```

`POST /v1/runs/{id}/reconcile` description: "Resolve an ambiguous run (expired lease, missing callback, unknown state) by querying the robot for the idempotency key's status instead of resubmitting. Returns the reconciled state; 'unknown' stays unknown and is escalated, never blindly retried." Response: `"reconciledStatus": "running|succeeded|failed|never_submitted|unknown"`, `"action": "resumed|resubmitted|escalated|none"`.

`POST /v1/authorizations/{id}/revoke` response: `"effect": "blocked_before_schedule|reservation_released|run_aborted|already_terminal"`.

`POST /v1/runs/{id}/callbacks` request: `{ "runId": "...", "sequence": 7, "event": "running|partial|succeeded|failed", "resultRef": "...|null", "signature": "..." }`.

Concept example (step 4, "authorization object & approval scope"): "Authorization #7 covers version-hash abc on instrument PCR-2, ≤50mL, expiring in 24h."

Concept example (step 3, "structured protocol IR"): "The validator reads `reagent: BSL-3 agent, volume: 50mL` from the IR, not from a sentence in the draft."

`claim_provenance` fields: `source_id`, `citation_span jsonb (exact passage: section/offset/quote)`, `corpus_snapshot`, `retracted bool`; note "Written at claim time, not extracted post-hoc."

`run_attempts` fields include `idempotency_key varchar unique`, `lease_expires_at`, `status enum(submitted,running,succeeded,failed,aborted,unknown)`, `conditions jsonb`, `instrument_calibration_ref`.

`authorizations.state`: `enum(active,consumed,expired,revoked) — an authorized object's own lifecycle, distinct from any run it spawns`.

### 3.10 Weaknesses and inconsistencies

REVIEW.md (`agentic-research-platform/REVIEW.md`, 2026-06-24) issues, checked against the current JSON:

- P1 execution lifecycle APIs: **fixed** (`/v1/runs`, `/callbacks`, `/abort`, `/reconcile`, `/authorizations/{id}/revoke`).
- P1 protocol vs run state conflation: **fixed** (`protocols.readiness`, derived `latest_run_status`, `run_attempts.status`, `authorizations.state`).
- P2 provenance schema: **fixed** (`claim_provenance`, `datum_provenance`, `run_artifacts`, `findings.analysis_code_version`).
- P2 options for grounding, execution and provenance: **fixed**.
- P3 richer API sequences: partly fixed (`/v1/runs` now has a sequence; callbacks, reconcile and revoke do not).
- The review mentions `GET /v1/runs/{id}`; it is **no longer in the API**, so there is no read endpoint for run status.
- Still open: multi-lab governance (per-lab instruments, policies, approvers, inventories, retention) is thin, with only `labId`. Reservation conflicts and reagent inventory are not modelled. The policy-service-down path is not shown in the step 6 flow, although step 3 states it.

Remaining issues I noticed:

- **Is authorization single-use or multi-use?** `authorizations.state` includes `consumed`, which implies one authorization → one run. But the step 4 concept "two-tier state machine" says "Version-hash abc is authorized once but has three run_attempts: a dry-run, a failed wet-lab run, and a successful replication." So it is unclear whether a failed wet-lab run consumes the authorization and a replication needs a new one. The book must pick one: a per-run authorization with reagent limits is the safer default.
- **Dry-runs and authorization contradict each other.** The gate says "dry-run analysis and simulation are free" and `exec-sim` says "no authorization needed", yet `POST /v1/runs` requires `authorizationId`. The `/v1/protocols` response statuses (`awaiting_authorization|needs_biosafety|blocked`) have no "ready for dry-run" value. The step 4 concept example also counts a dry-run among an authorization's run attempts.
- **Where the biosafety officer is routed.** The architecture link is `ExperimentGate → Safety` (`gate-safety`), but the step 6 sequence routes `ProtocolCheck → Safety` directly. The question is which component owns the routing.
- **Overlap between step 3 and step 6.** Dual-use screening is introduced in step 3 and "hardened" in step 6, with the same mechanism described twice. For the book, present it once (structured IR + deterministic screening) and give the adversarial framing a separate treatment.
- **No abstention mechanism.** Step 7 says the eval "watches the rate of blocked/abstained hazardous proposals", but nothing in the design can abstain on weak grounding: there is no calibrator, no grounding-sufficiency check, and no "insufficient evidence" status. Compare healthcare. An unsupported hypothesis is only caught by evaluation after the fact or by the human.
- **"Free" dry-runs are not free.** Capacity says they are "bounded by simulation/analysis backend compute"; the REVIEW also flags missing cost controls for simulation. "Free" means *free of human authorization*, not of cost; the book should say so.
- **Not multi-agent** (see the coverage gap at the top). Literature review, hypothesis generation and protocol drafting all happen in one `HypoAgent` node. Any multi-agent research decomposition in the book (planner, parallel literature searchers, critic, and so on) is *not* supported by this source.
- **`LabRobot → DataStore` (`robot-data`) bypasses the controller**, although the step 4a text says the controller writes "an immutable run record before results enter the data store." The robot writing results directly alongside the controller's record is an ordering ambiguity.
- No Status/option `title` fields (same renderer note as the other two).

### 3.11 Best uses in the book

- **Tools/execution**: the best source in the series for **side-effect execution**. It covers the single actuation broker, scoped short-lived tokens, idempotency keys, leases, reconcile-on-timeout, `unknown` as a state, signed callbacks, abort, and revocation by phase.
- **Reliability/recovery**: the ambiguous-timeout sequence ("query before retrying") is a canonical figure.
- **Security/oversight**: structured IR as the prompt-injection boundary; fail-closed policy; authorization objects bound to content hashes; actuator-side enforcement.
- **Context/memory/state**: versioned corpus snapshots, citation spans, retraction flags; the two-tier state machine.
- **Grounding and citation**: claim-level provenance written at generation time (the strongest grounding material in the group).
- **Evaluation**: replication-weighted evaluation versus plausibility versus citation precision.
- **Performance/economics**: the proposal → dry-run → wet-lab funnel; the scarce resource is instruments and humans, not tokens.
- **Orchestration**: durable workflows for multi-day human-and-physical processes (Temporal/Cadence versus managed step engines and their limits).

---

## Cross-source synthesis

### Recurring patterns and each source's name for them

| Pattern | Healthcare | Public benefits | Research |
| --- | --- | --- | --- |
| Model confined to bounded node(s) in an authored DAG | "Decision-Support Pipeline ... Deterministic DAG"; `ReasonAgent` "bounded node" | "Determination Pipeline ... Deterministic DAG"; `IntakeAgent` | "Research Pipeline ... Deterministic DAG"; `HypoAgent` |
| Deterministic floor the model cannot override | "Deterministic Safety Layer" | "Deterministic Rule Engine" (it *decides*) | "Protocol Validator" + "Dual-Use & Biosafety Screening" |
| Fail closed | `missing_data` → abstain/review | "fail-safe, never auto-deny" (hold) | "policy versioning & fail-closed" (block) |
| Human gate | "Sign-off & Abstain Gate"; "recommend, never act" | "Determination Gate"; caseworker decides adverse | "Experiment Authorization Gate"; "wet-lab boundary" |
| Human decision bound to an identity principal | `Identity` "binds the decision to a licensed clinician principal" | "binds an adverse decision to an accountable caseworker" | "binds a wet-lab authorization to a researcher / biosafety principal" |
| Specialist escalation tier | (risk tier, supervisor reassign) | supervisor review of `override_to_eligible` | biosafety officer for `needs_biosafety` |
| Versioned policy/rule content pinned per case | `safety_checks.rule_version` | `rule_package_id (pinned version)` | `validation_results.policy_version` |
| Versioned grounding corpus | `guideline_version`, `formulary_version` | effective-dated, jurisdiction-tagged rule index | `corpus_snapshot` |
| Reproducible decision record | "safety case"; evidence bundle | "audit-for-appeal"; appeal packet | "lab notebook"; provenance store |
| Explicit state machine with append-only history | `case_transition` | `status_history` | `run_attempts` + `authorizations.state` |
| Human-review queue as a capacity object | Worklist; "< 30 min p95 age" | ReviewQueue; SLA aging, deadline escalation | (authorization queue, not sized) |
| Untrusted input partitioned from authority | notes "partitioned from EHR write authority" | application text "partitioned from the rule engine" | structured IR; untrusted text "out of the tool-authority path" |
| Idempotency on side effects | sign-off key; EHR write correlation id | determination and evidence keys | run idempotency key; authorization key |
| Domain-weighted eval over accuracy | "harm-avoidance eval" | "contestability eval" | "reproducibility eval" |
| LLM-as-judge demoted to auxiliary | "clinician adjudication ... is the source of truth" | "scoped to explanation-quality ... not to deciding whether disparate impact exists" | "Output plausibility scoring" rejected |
| WORM / tamper-evident audit | "Append-only Postgres + hash chain"; WORM | "MinIO Object Lock", "immudb"; WORM | "immudb", "QLDB"; object lock |
| Built on the Foundations substrate | yes | yes | yes |

The recurring skeleton, which is the strongest reusable result for the reference-architecture chapter, is: **bounded LLM node → deterministic floor (versioned, fail-closed) → human gate bound to a principal → durable state machine → reproducible record → domain-weighted eval.** All three sources say this skeleton sits on `agentic-platform-foundations`.

### Where the sources disagree or are incompatible

1. **What the deterministic component does.** In healthcare, the safety layer *vetoes* a model proposal. In benefits, the rule engine *makes* the decision and the model never proposes an outcome. In research, the validator *screens* a model-authored artifact (the IR). These are three different roles (veto, decide, screen) that share the name "deterministic layer the model cannot override". The book needs a taxonomy: **decide / veto / screen**.
2. **What "fail closed" means.** Healthcare fails closed to *abstain or human review* (`missing_data`). Benefits fails closed to a *hold* and explicitly never to denial: here "closed" must not mean the adverse outcome, because the adverse outcome is the harm. Research fails closed to *block*. The safe direction depends on which outcome is harmful, and in benefits "deny" is the unsafe default. This contrast deserves its own section in the reliability chapter.
3. **Gate coverage.** In healthcare every recommendation goes to a human. Benefits gates only *adverse* outcomes (favourable outcomes auto-finalize). Research gates only *physical* actions (dry-runs are free). There are three gating predicates: all outputs, outcome direction, and side-effect class.
4. **Human-decision semantics.** Healthcare: `authorize|modify|reject|request_evidence` with attestation, `caseVersion`, and an idempotency key. Benefits: `approve|deny|override_to_eligible|request_more_evidence` with a rationale, **no version check and no idempotency**. Research: `authorize|reject|request_changes` with scope, expiry and an idempotency key bound to `contentHash`, **no version counter, but hash binding gives the same guarantee**. Only healthcare and research protect against stale or duplicate human decisions; benefits should be brought in line.
5. **What is bound by the approval.** Healthcare binds the "exact EHR action being signed for" plus `caseVersion`. Research binds the protocol `contentHash` plus scope and expiry. Benefits binds only the determination id. The research form (content-addressed, scoped, expiring object) is the strongest and should be the book's canonical "authorization object".
6. **Abstention.** Only healthcare has a calibrated abstention path. Benefits stores extraction `confidence` but never acts on it. Research mentions "abstained" proposals in its eval without having a mechanism. The book should make "grounding-sufficiency check + abstain" part of the general pattern, not a healthcare speciality.
7. **Audit layering.** Healthcare separates access audit from decision audit; the other two do not, although benefits handles PII and says access "is logged".
8. **Lifecycle modelling.** Healthcare uses one status enum plus a transition table. Benefits uses two orthogonal axes (status vs outcome). Research uses two separate state machines (readiness vs run) plus a third (authorization state). These all apply the same principle (do not overload one enum) in different ways. Recommend: **workflow state, outcome, and side-effect attempts are separate records.**
9. **Rule representation legibility.** Benefits chooses policy-as-code over DMN despite its own legibility argument. Healthcare and research choose engines (Drools/OPA/Cedar) without the legibility debate. Contestability argues for legible rules; the book should present this as an open trade-off.
10. **Is the authorization reusable?** Research contradicts itself (`consumed` vs one authorization with many runs). Healthcare binds one sign-off to one EHR write. Benefits has no reuse question.
11. **Ownership of the "deterministic" label.** The healthcare calibrator is called deterministic but depends on a fitted calibration curve. The book should separate deterministic *decision rules* from versioned *learned artifacts* they consume.

### Strongest contrasts between domains

| Dimension | Healthcare | Public benefits | Research |
| --- | --- | --- | --- |
| Consequence of failure | bodily harm to a person | loss of a citizen's rights or benefits; systemic injustice | physical hazard (biosafety, reagents, equipment) + irreproducible science |
| Reversibility | irreversible | reversible by appeal, but time-bound and costly to the person | physical: irreversible; scientific: correctable only if provenance exists |
| Gate axis (dataset's own framing) | top of the irreversibility gradient | contestability / due process | wet-lab (physical) boundary |
| Required human control | every recommendation | every adverse outcome | every physical run; biosafety officer for elevated tiers |
| What the model may do | draft a recommendation with confidence and citations | extract evidence; write explanations; never decide | review literature, hypothesize, draft the IR; simulate freely |
| Who else must understand the record | clinicians, regulators (safety case) | the affected applicant + independent reviewer | other scientists (reproduction) |
| Data sensitivity | PHI (HIPAA/BAA, no-train, break-glass) | PII + protected attributes (partitioned) | lab/tenant data; dual-use hazard info |
| Latency | interactive, < 6 s p95 | days (queue, SLA, statutory deadlines) | minutes → days per run |
| Volume | ~500k queries/day, 30–60 QPS peak | ~20k applications/day, 5–10x surge | ~2k proposals/day → 50–150 wet-lab runs/day |
| Binding constraint | clinician review capacity (alert fatigue) | caseworker throughput vs deadlines | instrument slots + human authorization |
| Eval ground truth | clinician adjudication | reviewer replay, golden determinations | replication on re-run |
| Population-level concern | per-specialty drift | matched-cohort fairness | replication rate |

Three takeaways for the book:

- **Required human control follows the harmful outcome, not the domain's "importance".** Healthcare gates everything because every output can harm. Benefits gates only the adverse direction. Research gates only the physical side effect. This gives the oversight chapter a usable rule: *gate on the predicate that identifies harm.*
- **Who has to understand the record differs.** It is the regulator in healthcare, the affected person in benefits, and a peer scientist in research. The same provenance machinery serves three readers, so explainability is reader-specific.
- **Fail-closed depends on the domain.** Closing to "deny" is safe in research (block the run) but unsafe in benefits (wrongful denial). Healthcare closes to "ask a human".

### Book-chapter map (summary)

| Chapter / topic | Best source and step |
| --- | --- |
| Foundations: autonomy spectrum, irreversibility | healthcare step 1, `interviewScript`; research step 1 (two irreversibilities) |
| Reference architecture: bounded node + deterministic services | all three `highLevelArchitecture`; benefits step 3 ("model assists, engine decides") |
| Orchestration: workflow vs agent, durable long-running approvals | research steps 4–4a; healthcare technologyChoices (orchestration) |
| Context/memory/state: grounding, snapshots, state machines | healthcare step 2; benefits step 2; research step 2 + data model |
| Tools/execution: side-effect broker, idempotency, reconcile | research step 4a + API; healthcare step 5 deepDive "EHR write contracts" |
| Reliability/recovery: fail-closed variants, unknown outcomes | healthcare step 4; benefits capacity "Failure behavior"; research `/reconcile` |
| Security/oversight: gates, abstention, appeal, injection boundary | healthcare steps 3, 5, 6; benefits steps 4–6; research steps 3, 6 |
| Explainability and appeal | benefits steps 4–5, API `/notice`, `/appeal`, `/appeals/{id}/decide` |
| Grounding and citation | research step 2 + `claim_provenance`; healthcare `evidence_bundle` |
| Evaluation/observability | healthcare step 7; benefits step 7; research step 7 |
| Performance/economics | research capacity funnel; healthcare inference budget + human queue |
| Deployment/evolution: rule and model release | benefits step 3 deepDive; healthcare step 4 (rule release), step 7 (staged rollout) |
| Multi-agent decomposition | **not covered by this group**; source elsewhere |
