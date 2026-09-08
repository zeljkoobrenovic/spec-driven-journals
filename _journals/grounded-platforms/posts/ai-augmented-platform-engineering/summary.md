---
timetoread: "2 min read"
---

When my platform teams bring AI into platform operations, it enters as a **governed operator, not a clever demo**: the capability starts from a measurable operational problem with a documented baseline, is grounded in our own platform data, acts through bounded agents with risk-tiered autonomy, is fenced by guardrails enforced in code, and expands only when the evidence supports it. The test I keep running: can I reconstruct, after the fact, exactly what the agent saw, decided, and did — and would I have approved it in advance?

**What changes**

* **Problem first, baseline always.** The first AI build targets one focused use case of high-volume, repetitive cognitive work — alert deduplication, documentation search, incident triage — with the current manual workflow documented and measured (time, accuracy, MTTR, false positives) before anything is automated. No AI on irreversible decisions without explicit human approval.
* **Grounded, not guessing.** Deployment (managed API, cloud-hosted, or self-hosted model) is matched to data control, latency, and cost; the model is grounded through RAG over our runbooks, incident history, and telemetry — hybrid semantic and keyword retrieval — before fine-tuning is even considered.
* **Bounded agents, tiered autonomy.** Every agent has explicit observe/decide/act/communicate boundaries and an autonomous-or-supervised designation. Read-only work runs free; restarts, rollbacks, scaling, and config changes need human approval; destructive and irreversible actions are decided *and executed* by humans.
* **Guardrails in code, failure as normal.** Dry-runs, policy-engine validation (the same gates as human changes), blast-radius estimates, rate limits, cost thresholds, input sanitization, tenant isolation, and output validation live in code — prompts advise, code enforces. Model outages get deterministic fallbacks and a route to a human; never a silent failure.
* **Audited and evidence-gated.** Every action is logged with context, reasoning, confidence, the human decision, the outcome, and model/prompt versions; AI metrics (cost per action, override rate, AI-vs-manual MTTR) are watched like SLIs; autonomy expands — or is revoked — based on measured results against the baseline.

**What it costs**

* Governance is most of the build: risk tiers, guardrail code, audit trails, and AI-specific observability take longer than wiring up the model itself.
* Human approval stays in the loop for every mutating action, and humans keep executing the destructive tier — some theoretical automation speed is deliberately left on the table.
* The evidence gate cuts both ways: an AI capability that cannot beat its manual baseline gets restricted or stopped, whatever was announced.

**What we are not doing**

* Not the remediation machinery itself — that is [[resilience-automation]]; nor the telemetry pipelines ([[observability-implementation]]) or policy engine ([[policy-as-code]]) this capability builds on.
* Not an organization-wide AI coding or tooling policy — this record covers AI inside platform operations only.
* Not a one-shot AI transformation of platform operations — scope grows one evaluated use case at a time.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all fifteen build steps and the final readiness check. Grounded in the* Platform Engineer's Handbook*.*
