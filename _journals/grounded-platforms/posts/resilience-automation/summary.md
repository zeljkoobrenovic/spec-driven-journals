---
timetoread: "2 min read"
---

Resilience is **proven, never assumed**. When a platform team builds the resilience capability, the build closes one loop: define objectives (SLOs with error budgets, RTO/RPO per service), inject failure deliberately, measure the system against the objectives, remediate, and retest. A backup that has never been restored is a hypothesis; a failover that has never been run is a hope. The reference stack — OpenSLO, Sloth, Prometheus, Grafana, CSI snapshots with object storage, Chaos Mesh — is the worked example; the commitment is the loop.

**What changes**

* **SLOs become contracts with consequences.** Critical services get SLIs, targets tiered by business criticality, error budgets over a defined window, and a written policy — including deployment-freeze criteria — for budget exhaustion. Definitions live in version control; alerting rules are generated from them; compliance, budget, and burn rate are on dashboards.
* **Backups are proven by restores.** Automated backups of cluster resources and volumes land in durable, replicated object storage — and restore tests run on a schedule in isolated clusters, validating application health, logs, and data integrity. Teams configure backups self-service; resources opt in via labels.
* **Failure is injected deliberately.** Chaos experiments have scope, target, duration, expected steady state, and abort conditions; they run on communicated schedules in business hours, off peak unless peak resilience is the objective. Pods, networks, resources, and managed cloud dependencies — slow queries, connection exhaustion, failover, degradation paths — are all tested before an outage tests them for us.
* **DR is rehearsed against numbers.** Recovery priorities, replication, standby environments, and failover procedures exist — and regular drills measure actual recovery time against RTO/RPO, updating procedures from the results.
* **Every finding closes the loop.** Gaps become remediation work, and experiments repeat after fixes. The standing evidence: four dates and four results — last error-budget review, last restore test, last chaos run, last DR drill.

**What it costs**

* Scheduled restore tests, chaos runs, and DR drills are recurring engineering time, not a one-off milestone — and remediation from them takes roadmap capacity.
* Error budgets bite: when the budget exhausts, the freeze policy interrupts real releases.
* Testing managed services and multi-region DR carries real infrastructure spend where business impact justifies it.

**What we are not doing**

* Not building the telemetry pipeline — that is [[observability-implementation]]; this record consumes it.
* Not load testing, autoscaling, or cost discipline — [[cost-performance-scalability]] injects load; this record injects failure.
* Not the conceptual operating discipline of incidents and on-call — that is [[operating-platforms]]; nor adversarial testing, which lives in [[platform-security]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all ten sections, including the hands-on Chaos Mesh validation exercise. Grounded in the Resilience Automation chapter of the* Platform Engineer's Handbook*.*
