---
status: accepted
revised: 2026-08-20
---

# Spec: AI-Augmented Platform Engineering

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the build I hold a platform team to when it brings AI into
platform operations. The record turns the AI-augmented platform engineering
chapter of the *Platform Engineer's Handbook* into an operating commitment:
AI enters the platform as a governed operator, not a clever demo. The
capability starts from a measurable operational problem with a documented
baseline, is grounded in the platform's own data through retrieval, acts
through agents with bounded responsibilities and risk-tiered autonomy, is
fenced by guardrails enforced in code rather than prompts, treats model
failure as a normal operational condition with deterministic fallbacks,
leaves a complete audit trail, and expands its autonomy only when the
evidence supports it. The load-bearing test: after the fact, I can
reconstruct exactly what the agent saw, decided, and did — and I would have
approved it in advance.

## Audience

Platform leads and teams in my organization about to add AI to platform
operations (so they know the bar the build is held to); SRE and operations
leaders deciding how much autonomy an agent gets; peer executives asked to
fund "AI for the platform". First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight names the full chain: problem
      first, grounded in platform data, bounded agents, risk-tiered
      autonomy, guardrails in code, failure as a normal condition, complete
      audit trail, evidence-gated expansion — and the reconstruction test.
- [x] **Use-case discipline survives** — business problem before AI
      capability; high-volume repetitive cognitive work (alert
      deduplication, documentation search, incident triage, anomaly
      correlation, prioritization/routing); no AI on irreversible decisions
      without explicit human approval; one focused use case or runbook
      first; the current workflow documented with a measured baseline
      (time, accuracy, MTTR, false positives) before automation
      (checklist §1–2).
- [x] **Deployment and grounding survive** — managed APIs vs cloud-hosted
      open models vs self-hosted, hybrid approaches, licensing, data
      residency, and serving concerns (routing, versioning, token metering,
      latency); RAG preferred before fine-tuning; grounding corpus of
      documentation, runbooks, incident history, and operational data;
      hybrid semantic + keyword retrieval; chunking along section
      boundaries with overlap (checklist §3–4).
- [x] **Bounded agents and risk tiers survive** — every agent has a
      specific responsibility with defined observe/decide/act/communicate
      boundaries, an orchestrator for multi-agent workflows, and an
      explicit autonomous-vs-supervised designation; actions classified
      from low-risk read-only through approval-required mutations to
      human-decided-and-executed destructive actions (checklist §5–6).
- [x] **Guardrails and safety checks survive** — pre-execution dry-runs,
      policy-engine validation (OPA/Kyverno), reviewer sees every proposed
      command, blast-radius estimate and rollback plan; programmatic
      guardrails: rate limits, environment-scoped permissions, dependency
      checks, cost thresholds, rollback conditions, input sanitization and
      prompt-injection prevention, tenant isolation, output validation
      (checklist §7–8).
- [x] **Failure and thresholds survive** — model failure treated as a
      normal operational condition; defined behavior for outages and
      quota exhaustion; cached responses where safe; never a silent
      failure; deterministic fallback; unresolved cases routed to a human;
      confidence bands for autonomy / confirmation / suppression combined
      with severity, recalibrated from operational results (checklist
      §9–10).
- [x] **Audit and measurement survive** — audit trail of context,
      reasoning, confidence, human decision, action, outcome, and
      model/prompt versions; AI-specific metrics (tokens, latency,
      confidence trends, cost per action, override rate, AI-vs-manual
      MTTR, false positives, satisfaction, GPU utilization, vector-DB
      latency, queue depth); agent-health triggers; business-impact
      measures; the review-before-expanding gate and final readiness check
      (checklist §11–15 + final check).
- [x] **Tools are the worked example, not the mandate** — the reference
      stack (managed/self-hosted models, RAG, OPA/Kyverno, the platform
      observability stack) is named honestly; commitments are stated at
      the capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its AI-augmented platform engineering chapter
      checklist.

## Non-goals

- Not [[resilience-automation]] — automated remediation and chaos
  machinery live there; this record governs the AI layer that proposes and
  gates such actions, not the remediation mechanics themselves.
- Not [[observability-implementation]] — the telemetry pipelines live
  there; this record consumes them as grounding data and adds AI-specific
  metrics on top.
- Not [[policy-as-code]] — the policy-engine machinery lives there; this
  record uses it as one pre-execution check on AI-proposed actions.
- Not [[cost-performance-scalability]] — the platform's cost and capacity
  discipline lives there; this record tracks only the AI capability's own
  cost per action and value case.
- Not an organization-wide AI coding or tooling policy — this record is
  about AI inside platform operations, not AI-assisted software
  development generally.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-20** — Grounded in the AI-Augmented Platform Engineering
  chapter checklist of the *Platform Engineer's Handbook* — read through a
  practitioner-executive lens, as with every record in this journal. Note:
  the source PDF's filename says "Cost, Performance, and Scalability", but
  its title page reads "AI-Augmented Platform Engineering"; the title page
  is authoritative.
- **2026-08-20** — Framed as a governance-of-autonomy record rather than a
  tool-adoption record: the chapter's distinctive claim is that the hard
  part of AI in platform operations is bounding, gating, auditing, and
  measuring it — so the record commits to the control chain and treats
  model choice as a deployment decision, not the headline.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 14 _ Cost, Performance, and Scalability.pdf`
    — the chapter checklist; the file's own title page reads
    "AI-Augmented Platform Engineering" despite the filename. Reproduced,
    adapted, in the Checklist tab (`checklist.md`), including the final
    readiness check.
- **External**
  - *Platform Engineer's Handbook* — the AI-Augmented Platform
    Engineering chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md); no spec-side edits were needed. *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 4 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
