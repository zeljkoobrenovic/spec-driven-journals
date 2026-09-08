---
status: accepted
revised: 2026-08-20
---

# Spec: Cost, Performance, and Scalability

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the build I hold a platform team to when it takes on cost,
performance, and scalability as a platform capability. The post turns the
"Cost, Performance, and Scalability" chapter checklist of the *Platform
Engineer's Handbook* into a reference-implementation record: SLOs and explicit
trade-offs come before any savings work; cost is made visible and attributable
down to the team that incurs it; optimization runs as a measured loop —
baseline, rightsize, autoscale, buy capacity at the right price, measure —
never as a one-time savings project; and guardrails, anomaly alerts, and CI/CD
cost gates move the cost conversation to before the invoice arrives. The
reference stack (OpenCost, Grafana, HPA/VPA/Goldilocks, Karpenter,
spot/committed capacity, ResourceQuotas/LimitRanges, Kyverno/Gatekeeper, cost
checks in the pipeline) is the worked example; the commitments are stated at
the capability level.

## Audience

Platform leads and teams in my organization building or hardening the cost and
capacity capability of an internal platform (so they know the end-to-end bar);
infrastructure and FinOps-adjacent leaders deciding what "cost is under
control" concretely means; peer executives reading cloud bills. First-person
declarative.

## Success criteria

- [x] **Principle is quotable** — highlight names the three simultaneous
      outcomes (cost visible and attributable, performance defended by SLOs
      and tested autoscaling, consumption bounded by guardrails) and the
      continuous-loop framing, plus the running test: does anyone see the
      cost before the invoice does.
- [x] **Goals and trade-offs survive** — SLOs for availability and
      performance, acceptable latency/throughput/downtime, cost calculated
      per SLO, trade-offs explicit, cost justified by business value, never
      lowest-price-only.
- [x] **Cost observability survives** — cloud-native cost reporting plus
      OpenCost, consistent labels (team, cost center, business unit,
      application) applied to namespaces and deployments, CPU and memory cost
      tracked, Grafana dashboards, allocation to teams, showback/chargeback.
- [x] **Baseline and rightsizing survive** — chosen workload, recorded
      hourly/monthly cost, measurable reduction target, profiled CPU/memory
      usage and peaks, usage-vs-requests comparison; requests reduced with
      headroom, bound-type determined (CPU/memory/I/O/storage), instance
      category matched, automated instance selection considered.
- [x] **Autoscaling survives** — HPA with min/max replicas, utilization
      targets, safe scale-up/down behavior, stabilization windows, custom
      business metrics, load-tested against SLOs; VPA in recommendation mode
      first with an observation window, bounded limits, sidecar exclusions,
      and an explicit HPA+VPA decision.
- [x] **Capacity mix survives** — on-demand for stability, spot for
      fault-tolerant workloads with interruption handling, taints/affinity
      and on-demand fallback, the named spot exclusions, committed-use
      discounts only for the true baseline and never for variable workloads.
- [x] **Governance, anomalies, and CI/CD gates survive** — ResourceQuotas
      and LimitRanges with defaults, minima, maxima, and required requests,
      enforced by policy-as-code; cost baseline with anomaly alerts, tuned
      thresholds, leak and CPU investigations; pre-deploy cost estimates,
      request diffs, approval for major increases, quota checks with clear
      remediation, cost in PR/deploy metadata, post-deploy comparison.
- [x] **Measurement and the worked exercise survive** — post-optimization
      comparison against baseline, SLO/latency/autoscaling verification,
      remaining-waste hunt, repeat; the chapter's 30%-reduction exercise
      reproduced in the checklist as the training loop, with the final
      review.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its "Cost, Performance, and Scalability" chapter
      checklist.

## Non-goals

- Not [[policy-as-code]] — the enforcement machinery (Gatekeeper, Kyverno,
  admission control) lives there; this record only states which cost and
  resource policies that machinery enforces.
- Not [[observability-implementation]] — the telemetry stack is built there;
  this record reuses it to carry cost signals and dashboards.
- Not [[cicd-as-a-platform-service]] — the pipeline as a platform service
  lives there; this record only adds the cost gates and cost metadata that
  run inside it.
- Not [[self-service-onboarding]] — the default quotas a new tenant receives
  at onboarding live there; this record governs how quotas bound ongoing
  consumption.
- Not FinOps organizational design, cloud contract negotiation, or unit-cost
  economics of the platform's own business case — [[platform-success]] and
  [[four-pillars]] carry the economics of the platform itself.

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

- **2026-08-20** — Grounded in the "Cost, Performance, and Scalability"
  chapter checklist of the *Platform Engineer's Handbook* — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-20** — Framed as a continuous optimization loop rather than a
  cost-cutting playbook: the chapter's distinctive move is putting SLOs and
  explicit trade-offs *before* any savings work and closing every round with
  measurement, so the record commits to the loop and rejects the one-time
  savings-project framing.
- **2026-08-20** — Tools named as the reference stack (OpenCost, Grafana,
  HPA/VPA, Karpenter, Kyverno/Gatekeeper), commitments stated at the
  capability level — consistent with the Reference Implementation section's
  tools-are-the-worked-example convention.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 12 _ Cost, Performance, and Scalability.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the 30%-reduction completion exercise and
    the final review.
- **External**
  - *Platform Engineer's Handbook* — the "Cost, Performance, and
    Scalability" chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md): canonical loop phrasing unified across excerpt, highlight, and Figure 1 caption; comic panel 6 caption trimmed to the four stages shown; minor consistency nits. Spec itself unchanged. *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
