---
timetoread: "2 min read"
---

When a platform team in my organization builds the cost, performance, and scalability capability, the finished build makes three things true at once: **cost is visible and attributable** to the team that incurs it, **performance is defined by SLOs and defended by tested autoscaling**, and **consumption is bounded by guardrails** that catch expensive mistakes before the invoice does. Optimization runs as a continuous loop — baseline, rightsize, scale, buy capacity at the right price, measure, repeat — never as a one-time savings project.

**What changes**

* **SLOs come before savings.** Availability and performance SLOs are defined first, the cost of meeting each is calculated, and trade-offs are explicit — nothing is chosen only because it is cheapest.
* **Every workload gets a price tag and an owner.** Cloud-native cost reporting plus OpenCost, consistent labels (team, cost center, business unit, application), Grafana dashboards, and showback or chargeback — the team that sees its own number is the team that fixes it.
* **Optimization becomes a measured loop.** Baseline cost recorded and usage profiled before anything is touched; requests rightsized with headroom; HPA load-tested against the SLO with stabilization windows; VPA run in recommendation mode before any recommendation is obeyed; results verified against the baseline and the SLOs, then the loop repeats.
* **Capacity is bought per stability class.** On-demand or committed for the true baseline, spot for fault-tolerant workloads with interruption handling and fallback — never for business-critical single replicas, and no commitments stretched over variable workloads.
* **Cost decisions move into the pipeline.** Quotas and limit ranges enforced by policy-as-code, anomaly alerts on a tuned baseline, and CI/CD gates that estimate cost, diff resource requests, require approval for major increases, and fail quota-breaking deployments with a clear remediation message.

**What it costs**

* SLO definition and per-SLO cost calculation are real up-front work — the discipline forbids skipping straight to the savings.
* Attribution, dashboards, and anomaly tuning are standing platform obligations, not a setup task; the loop has no end date.
* Some savings are deliberately left on the table: headroom stays in rightsized requests, and spot discounts are refused for workloads that cannot tolerate interruption.

**What we are not doing**

* Not the enforcement machinery itself — Gatekeeper and Kyverno live in [[policy-as-code]]; the telemetry stack lives in [[observability-implementation]]; the pipeline lives in [[cicd-as-a-platform-service]].
* Not onboarding-time default quotas — those live in [[self-service-onboarding]]; this record governs how bounds hold over time.
* Not FinOps org design or the platform's own business-case economics — [[four-pillars]] and [[platform-success]] carry those.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full build, including the handbook's worked 30%-reduction exercise. Grounded in the* Platform Engineer's Handbook*, "Cost, Performance, and Scalability" chapter.*
