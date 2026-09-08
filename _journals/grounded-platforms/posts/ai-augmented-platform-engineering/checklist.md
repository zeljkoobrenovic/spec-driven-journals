---
timetoread: "8 min read"
---
*The working checklist behind this record — the AI capability build, end to end. The Article tab carries the rationale and anti-patterns.*

## 1. Identify the Right Use Case

- [ ] We start with a real business or operational problem rather than asking what can be built with AI
- [ ] We identify high-volume, repetitive cognitive work
- [ ] We look for opportunities involving alert duplication, documentation search, or incident triage
- [ ] We identify tasks where pattern recognition could improve anomaly detection or event correlation
- [ ] We identify decisions where contextual information could improve prioritization or routing
- [ ] We do not use AI for irreversible decisions without explicit human approval
- [ ] We select one focused use case or runbook for the first implementation

## 2. Define the Current Workflow

- [ ] We document the existing manual process
- [ ] We identify what engineers always check first
- [ ] We identify the logs, metrics, tickets, and documentation normally gathered
- [ ] We separate repetitive decisions from decisions requiring significant human judgment
- [ ] We record the current time and effort required to complete the workflow
- [ ] We establish a baseline for current accuracy, MTTR, false positives, or other relevant metrics

## 3. Select the AI Deployment Approach

- [ ] We evaluate managed APIs for reasoning-heavy or prototype workloads
- [ ] We evaluate cloud-hosted open-source models when greater data control is required
- [ ] We evaluate self-hosted models when local control, air-gapped operation, or high-volume cost efficiency is important
- [ ] We consider a hybrid approach where different workloads use different model types
- [ ] We review current licensing requirements before using or fine-tuning open-source models
- [ ] We verify applicable data residency and compliance requirements
- [ ] We account for model serving, routing, versioning, token metering, and latency monitoring

## 4. Ground the AI with Platform Data

- [ ] We prefer RAG before considering fine-tuning
- [ ] We identify authoritative platform documentation and runbooks
- [ ] We include relevant incident history where appropriate
- [ ] We include operational data such as logs, metrics, traces, or Kubernetes events where required
- [ ] We implement document ingestion and indexing
- [ ] We use semantic/vector retrieval for conceptually related information
- [ ] We include keyword retrieval where exact commands or terminology matter
- [ ] We consider hybrid retrieval combining semantic and keyword search
- [ ] We split documents along meaningful section boundaries rather than arbitrary character limits
- [ ] We preserve enough overlap between chunks to maintain context

## 5. Define Agent Responsibilities

- [ ] Every agent has a specific and clearly bounded responsibility
- [ ] We define what information each agent can observe
- [ ] We define what decisions each agent can make
- [ ] We define what actions each agent can execute
- [ ] We define how agents communicate with one another
- [ ] We establish an orchestrator or coordination mechanism for multi-agent workflows
- [ ] We determine which agents can operate autonomously
- [ ] We determine which agents require supervision

## 6. Classify Actions by Risk

- [ ] We classify read-only queries and context gathering as low-risk where appropriate
- [ ] We determine whether incident-ticket creation or documentation updates can be autonomous
- [ ] We require human approval for actions such as service restarts, deployment rollbacks, scaling, or configuration changes
- [ ] We require humans to decide and execute destructive or irreversible actions
- [ ] We require human control for actions affecting backups, security policies, critical infrastructure, database migrations, or financial commitments

## 7. Add Pre-Execution Safety Checks

- [ ] We dry-run AI-generated operational changes in staging or a sandbox
- [ ] We validate generated actions against security and resource policies
- [ ] We use policy engines such as OPA or Kyverno where applicable
- [ ] We require explicit human approval for high-impact actions
- [ ] We show the reviewer every proposed command or API action
- [ ] We estimate the expected impact and blast radius
- [ ] We define a rollback plan before execution

## 8. Implement Guardrails in Code

- [ ] Guardrails are enforced programmatically rather than relying only on prompts
- [ ] We add rate limits for repeated actions or notifications
- [ ] We apply different permissions for production and non-production environments
- [ ] We check dependencies before performing remediation
- [ ] We add cost thresholds that trigger approval
- [ ] We add rollback conditions for failed or rapidly reverted actions
- [ ] We validate inputs before including them in model prompts
- [ ] We prevent unsanitized input from controlling agent behavior
- [ ] We maintain strict tenant or organizational context isolation
- [ ] We validate generated outputs before acting on them

## 9. Plan for AI Failure

- [ ] We treat model failures as normal operational conditions
- [ ] We define behavior for API outages, rate limits, or quota exhaustion
- [ ] We use cached responses when safe and appropriate
- [ ] We route unresolved failures to a human
- [ ] We never silently fail or return an unexplained empty response
- [ ] We validate response format and guardrail compliance
- [ ] We maintain deterministic fallback behavior
- [ ] We require human confirmation when AI triage cannot determine a reliable result

## 10. Establish Confidence and Approval Thresholds

- [ ] We define confidence thresholds for autonomous actions
- [ ] We define a middle range requiring human confirmation
- [ ] We suppress or escalate low-confidence results rather than creating unnecessary noise
- [ ] We combine confidence with incident severity when routing alerts
- [ ] We recalibrate thresholds using actual operational results

## 11. Build an Audit Trail

- [ ] We log every agent action
- [ ] We record the context supplied to the model
- [ ] We record model or agent reasoning information required by our governance process
- [ ] We record confidence scores
- [ ] We record whether a human approved, rejected, or modified the recommendation
- [ ] We record the action taken
- [ ] We record the final outcome
- [ ] We preserve the model and prompt versions needed to investigate regressions

## 12. Monitor AI-Specific Metrics

- [ ] We track token usage
- [ ] We track inference latency
- [ ] We track confidence-score trends
- [ ] We compare model decisions with known ground truth
- [ ] We track cost per action
- [ ] We track the human override rate
- [ ] We track AI-assisted versus manual MTTR
- [ ] We track false-positive rates
- [ ] We track developer or customer satisfaction
- [ ] We track GPU/CPU utilization when models are hosted locally
- [ ] We track vector database query latency
- [ ] We track agent action queue depth

## 13. Evaluate Agent Health

- [ ] We investigate consistently low confidence scores
- [ ] We investigate high human override rates
- [ ] We stop or restrict autonomous use if triage accuracy falls below acceptable thresholds
- [ ] We investigate when AI-assisted resolution becomes slower than manual resolution
- [ ] We recalibrate when false-positive rates rise
- [ ] We investigate unexpected increases in cost or token consumption
- [ ] We watch for unbounded agent reasoning loops

## 14. Measure Business Impact

- [ ] We measure the reduction in MTTR
- [ ] We measure improvements in incident detection or prevention
- [ ] We measure improvements in developer productivity
- [ ] We measure reductions in alert fatigue
- [ ] We measure triage classification accuracy
- [ ] We measure root-cause hypothesis precision
- [ ] We measure runbook or documentation retrieval effectiveness
- [ ] We measure the time from alert generation to ticket creation
- [ ] We measure human approval and review time
- [ ] We compare AI operating costs against the equivalent manual effort
- [ ] We calculate the value of time saved
- [ ] We confirm that the AI system creates measurable value before expanding its scope

## 15. Review Before Expanding

- [ ] We confirm that guardrails work as intended
- [ ] We confirm that failures reliably fall back to safe behavior
- [ ] We review human overrides and rejected recommendations
- [ ] We review model drift and accuracy trends
- [ ] We review costs and infrastructure utilization
- [ ] We update documentation and runbooks based on feedback
- [ ] We expand autonomous scope only when the evidence supports it
- [ ] We add additional agents or use cases incrementally rather than attempting a complete platform transformation at once

## Final Readiness Check

- [ ] The use case solves a measurable operational problem
- [ ] Agent responsibilities and boundaries are clearly defined
- [ ] Platform knowledge is grounded through reliable data or RAG
- [ ] High-impact actions require appropriate human approval
- [ ] Guardrails are enforced in code
- [ ] Failure and fallback paths are tested
- [ ] Actions and outcomes are fully auditable
- [ ] AI-specific observability is in place
- [ ] Success metrics and thresholds are defined
- [ ] Business value can be measured
- [ ] The first implementation is small enough to evaluate before expanding
