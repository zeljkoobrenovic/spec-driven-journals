---
status: accepted
revised: 2026-08-20
---

# Spec: Resilience Automation

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the resilience capability I hold platform teams to when
they build it end to end. The post turns the Resilience Automation chapter
checklist of the *Platform Engineer's Handbook* into a reference-implementation
record: resilience is proven, never assumed. The build closes one loop —
define objectives (SLOs with error budgets, RTO/RPO per service), inject
failure deliberately (chaos experiments, managed-service degradation, workload
kills), measure the system against the objectives, remediate what the
measurement exposes, and retest. Backups exist only when restores are
exercised; DR exists only when failover is rehearsed against its targets. The
reference stack (OpenSLO, Sloth, Prometheus, Grafana, CSI snapshots + object
storage, Chaos Mesh) is the worked example; the commitments are stated at the
level of the capability.

## Audience

Platform leads and engineers in my organization building or reviewing the
resilience capability of an internal platform; SRE and infrastructure leaders
deciding what "resilient" must mean before it is claimed; peer executives
reading the Reference Implementation section as the concrete companion to the
operating model. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — resilience is proven, not assumed; the
      highlight names the loop (objectives → controlled failure → measurement
      → remediation → retest) and the two signature lines: a backup that has
      never been restored is a hypothesis; a failover that has never been run
      is a hope.
- [x] **SLO discipline survives** — critical services identified; SLIs
      (availability, error rate, request success rate, latency); targets
      tiered by business criticality over a defined window (rolling 30 days);
      error budgets with an exhaustion policy and deployment-freeze criteria;
      definitions version-controlled (OpenSLO), Prometheus rules generated
      (Sloth), status published in Grafana (compliance, budget remaining,
      burn rate, remaining allowable downtime) with violation and burn-rate
      alerts.
- [x] **Backup and restore survives** — automated backups of CRDs, Secrets,
      ConfigMaps, and persistent volumes; CSI snapshots; durable object
      storage with retention and cross-region replication where DR requires
      it; scheduled plus on-demand; automated restore of resources and
      volumes with health, log, and data-integrity validation; regular
      restore tests in isolated clusters with functional and performance
      tests; self-service opt-in via labels or configuration.
- [x] **Recovery objectives survive** — RTO and RPO defined per important
      service, tiered by business impact; backup frequency tuned to RPO and
      recovery automation tuned to RTO, not the other way around.
- [x] **Chaos discipline survives** — experiments designed (scenario, scope,
      target, duration, schedule, expected steady state, abort conditions and
      safety boundaries); controlled injection of pod, network, CPU, memory,
      and dependency failures via Chaos Mesh; schedules predictable,
      communicated, in business hours, off peak unless peak-load resilience
      is the objective; full monitoring during experiments (metrics,
      dashboards, logs, latency percentiles, restarts, success rates,
      connection pools, burn-rate and recovery-failure alerts) with
      business-impact correlation; review → remediate → retest.
- [x] **Managed services and workloads are both tested** — slow queries,
      connection-limit exhaustion, database failover, cross-region latency,
      graceful degradation, retry/backoff, circuit breakers on the managed
      side; single/multiple/sustained pod kills, ReplicaSet replacement,
      recovery time, and SLO compliance during failure on the Kubernetes side.
- [x] **DR survives** — recovery priorities; the multi-region decision;
      primary and standby regions; database, object-storage, and cache
      replication; standby cluster; DNS health checks; documented failover
      and replica-promotion procedures; monitoring that operates during
      failover; regular drills measured against RTO/RPO with procedures
      updated from results. The hands-on Chaos Mesh validation exercise
      (checklist §9) is reproduced in the Checklist tab.
- [x] **The continuous loop survives** — resilience testing as an ongoing
      engineering practice: error-budget reviews, scheduled restores, chaos
      runs, and DR drills; failure modes documented; weaknesses remediated
      and experiments repeated after fixes (checklist §10).
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its Resilience Automation chapter checklist.

## Non-goals

- Not [[observability-implementation]] — that record builds the telemetry
  pipeline; this record consumes it. SLO dashboards and burn-rate alerts
  assume the metrics, logs, and dashboards already exist.
- Not [[cost-performance-scalability]] — load testing, autoscaling, and cost
  discipline live there. That record injects load; this one injects failure.
- Not [[operating-platforms]] — the conceptual operating discipline (incident
  ownership, on-call, support) lives there; this record is its automated,
  self-testing counterpart on the reference stack.
- Not [[platform-security]] — failure injection here is operational, not
  adversarial; attack-shaped testing and cluster hardening live there.

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

- **2026-08-20** — Grounded in the Resilience Automation chapter checklist of
  the *Platform Engineer's Handbook* — read through a practitioner-executive
  lens, as with every record in this journal. Part of the Reference
  Implementation section: the how-it-concretely-looks companion to the
  Platform Engineering records.
- **2026-08-20** — Framed around one closed loop (objectives → controlled
  failure → measurement → remediation → retest) rather than as four separate
  practices (SLOs, backups, chaos, DR); the chapter's distinctive claim is
  that each practice is only real when the loop closes on it. Tools named
  honestly as the reference stack; commitments stated at capability level.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 13 _ Cost, Performance, and Scalability.pdf`
    — the chapter checklist; note the file's own title page reads
    "Resilience Automation" despite the filename. Reproduced, adapted, in
    the Checklist tab (`checklist.md`), including the hands-on Chaos Mesh
    validation exercise.
- **External**
  - *Platform Engineer's Handbook* — the Resilience Automation chapter
    checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md); spec itself unchanged (the granularity note required no criteria edit). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 4 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
