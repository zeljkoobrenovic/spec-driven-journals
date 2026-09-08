---
timetoread: "8 min listen"
---

## The Intern with Root

**Ben:** Blunt version first. Every platform team on earth is bolting an LLM onto their ops stack right now. Why does this need a record — isn't it just "use AI, be careful"?

**Ana:** Because "be careful" is exactly what fails. The record's framing is that AI enters the platform as a governed operator, not a clever demo — and everything in it is the difference between those two. One of its named anti-patterns is the intern with root: one general-purpose agent, broad production access, no risk tiers. Trusted like a senior engineer, verified like neither.

**Ben:** And the governed version is what, in one breath?

**Ana:** Start from a measurable operational problem with a documented baseline. Ground the model in the platform's own data through retrieval. Bound every agent in what it can observe, decide, and do. Tier its autonomy by risk. Enforce guardrails in code, not prompts. Treat model failure as a normal operational condition. Audit everything down to the prompt version. And expand only when the evidence supports it.

**Ben:** That's a lot of machinery before anyone gets to the fun part.

**Ana:** The machinery *is* the part. Wiring up a model takes an afternoon. The record's honest cost statement is that governance is most of the build — and the chapter's whole structure agrees: fifteen steps, and the model selection is one of them.

## Problem First, Baseline Always

**Ben:** Step one, then. Teams usually start with "we got API access, what should we build?"

**Ana:** Which the record names as its first anti-pattern: the demo in search of a problem. Impressive in the all-hands, absent from the MTTR chart. The discipline is the reverse — find high-volume, repetitive cognitive work that already exists: alert deduplication, documentation search, incident triage, event correlation, routing decisions where context would help. Then pick *one* focused use case or runbook for the first implementation.

**Ben:** One? That feels timid for a transformation.

**Ana:** It's not a transformation, deliberately — the big-bang version is another named anti-pattern. One use case, small enough to evaluate. And before you automate anything, you document the current manual workflow: what engineers check first, what they gather, which decisions are rote and which need judgment — and you measure it. Time, accuracy, MTTR, false positives.

**Ben:** Why so much ceremony about the baseline?

**Ana:** Because the baseline is the whole argument. Without a measured before, every claim of AI value is a vibe — the record calls that one the vibe-based victory. Later, the expansion gate asks whether AI-assisted resolution beats manual, whether the cost per action beats the equivalent manual effort. Those questions are unanswerable without the baseline. And one constraint gets set right at use-case selection: no AI on irreversible decisions without explicit human approval. You decide that before the incident review, not during it.

**Ben:** Fine. But why retrieval? The whole appeal of these models is that they already know Kubernetes.

**Ana:** They know Kubernetes in general. They do not know *our* runbooks, our incident history, our naming, our weird legacy namespace. The ungrounded oracle answers fluently, confidently — about somebody else's platform. So the record grounds the model with RAG over authoritative docs, runbooks, incident history, and operational data before fine-tuning is even considered: cheaper, auditable, and it updates at the speed the documentation does. And retrieval is real engineering — semantic search for concepts, keyword search where the exact flag matters, hybrid where both do, chunks split on section boundaries with overlap so context survives.

## Guardrails Are Code

**Ben:** Here's my sharpest objection. You can just tell the model the rules. System prompt: "never delete anything, always ask before restarting a service." Why isn't that enough?

**Ana:** Because a prompt is a request, not a control. The record's phrase is the prompt-shaped guardrail — safety implemented as instructions, with nothing in code to make it true when the model decides otherwise. Or when an attacker does: unsanitized input that steers agent behavior is prompt injection, and no prompt defends against prompts. So the guardrails are programmatic — rate limits, separate permissions for production and non-production, dependency checks before remediation, cost thresholds that trigger approval, input validation, strict tenant isolation, output validation before anything acts.

**Ben:** And before an action actually runs?

**Ana:** Dry-run in staging, validation against security and resource policies — through the same policy engine that gates human changes, which is the whole point of [[policy-as-code]] — an estimated blast radius, and a rollback plan defined before execution. And the reviewer sees every proposed command. An approval click on an action you did not read is not a control.

**Ben:** Which brings us to approvals. If a human has to bless every action, haven't you built a very expensive suggestion box? The point of automation is removing the human.

**Ana:** The point is removing the *toil*, and the record prices autonomy by reversibility. Read-only queries and context gathering — low-risk, run free. That's most of triage, and most of the value. Ticket creation and documentation updates can be autonomous, as a deliberate decision. Restarts, rollbacks, scaling, configuration changes — human approval. And destructive or irreversible actions, plus anything touching backups, security policies, critical infrastructure, database migrations, or money — the human doesn't just approve, the human executes. A wrong query costs seconds; a wrong migration costs the weekend, or the company.

**Ben:** So some automation speed is left on the table.

**Ana:** Deliberately, and the record says so. The tiers can move — but only on evidence, which we'll get to.

## When the Model Fails

**Ben:** The model API goes down at 3 a.m. mid-incident. Now what?

**Ana:** Now nothing dramatic — and that's the design. The record treats model failure as a normal operational condition, not an exception: defined behavior for outages, rate limits, quota exhaustion; cached responses where safe; deterministic fallbacks; unresolved cases routed to a human. The one forbidden behavior is the silent shrug — an unexplained empty response or a quiet timeout. That teaches engineers to distrust the tool at exactly the moment they need it, and trust doesn't come back.

**Ben:** And when the model is up but unsure?

**Ana:** Confidence thresholds, in bands. Above the line, autonomous. A middle range that requires human confirmation. Below it, suppress or escalate rather than generating noise — combined with incident severity when routing, and recalibrated from actual operational results, not set once and forgotten.

## Earning Autonomy

**Ben:** Last push. Audit trails, AI metrics, health checks, business-impact measurement — this reads like you're operating a suspect, not a tool.

**Ana:** You're operating a probabilistic component with production reach — the record just extends the platform's normal discipline to it. Every action logged with the context the model saw, its reasoning, its confidence, whether the human approved, rejected, or modified it, the action, the outcome, and the model and prompt versions — because without those, a regression is uninvestigable. That's the black box without a flight recorder. Then the AI-specific metrics get watched like SLIs: token usage, latency, confidence trends, cost per action, override rate, AI-assisted versus manual MTTR, false positives.

**Ben:** And those numbers actually decide something?

**Ana:** They decide everything. High override rates get investigated. If triage accuracy falls below threshold, autonomous use stops or gets restricted — the record is explicit that this is the system working, not an embarrassment. And expansion runs through a gate: guardrails confirmed, fallbacks tested, overrides reviewed, drift and cost reviewed, and scope grows only when the evidence supports it — one use case, one agent at a time. Autonomy is earned in tiers, and it is revocable.

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's not the remediation machinery — that's [[resilience-automation]]; these tiers gate what that automation may do unattended. It's not the telemetry pipeline — [[observability-implementation]] builds what the AI reads. It's not the policy engine — [[policy-as-code]] built the gate the agent's actions pass through. And it's not an organization-wide AI coding policy — this is AI inside platform operations only.

**Ben:** One-sentence version for the elevator?

**Ana:** After anything the agent did, I can reconstruct exactly what it saw, decided, and executed — and I would have approved it in advance. If either half fails, it doesn't run autonomously in my platform.
