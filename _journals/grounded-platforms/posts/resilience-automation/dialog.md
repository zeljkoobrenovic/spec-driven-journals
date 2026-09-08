---
timetoread: "8 min listen"
---

## Proven, Not Assumed

**Ben:** Blunt version first. Every platform team I know already claims resilience — replicas, multi-AZ, backups running nightly. Why does this need a record?

**Ana:** Because every one of those claims is an assumption until something proves it. That's the whole record in one line: resilience is proven, never assumed. When a platform team in this organization builds the resilience capability, the build closes one loop — define objectives, inject failure deliberately, measure the system against the objectives, remediate what you find, retest after the fix. The two signature lines do most of the work: a backup that has never been restored is a hypothesis, and a failover that has never been run is a hope.

**Ben:** And the evidence that the loop is actually closing? Because "we do chaos engineering" is exactly the kind of claim that goes stale.

**Ana:** Four dates and four results. The platform lead can show me the date and outcome of the last error-budget review, the date and result of the last restore test, the last chaos run, and the last DR drill's measured recovery time against its RTO. That is what "resilient" means here — not an architecture diagram.

## Budgets with Teeth

**Ben:** Start with the SLOs, then. Everybody has SLOs. Most of them are wall art.

**Ana:** The record names that anti-pattern — the decorative SLO. Targets defined, dashboarded, budget burning, and no consequence ever triggered. The chapter's discipline is in the other half: every critical service gets SLIs — availability, error rate, request success, latency — a target over a defined window, a calculated error budget, and a written policy for what happens when the budget nears exhaustion, including deployment-freeze criteria where appropriate. Written before anyone is angry.

**Ben:** There's the fight. A freeze policy means the platform team can stop a product team's release. That's a political weapon, not an engineering practice.

**Ana:** It's only a weapon if it's discretionary. The point of writing the criteria down in advance is that nobody decides anything in the moment — the budget was agreed, the burn rate is measured, the freeze triggers itself. A burn-rate alert interrupting a release conversation is the SLO doing its job. And the targets are tiered by business criticality, which is what keeps it fair. The record calls the failure mode the uniform nine: one ambitious target for everything — meaningless for the payment path, extortionate for the batch job, and evidence that nobody made a decision.

**Ben:** Where do the definitions live? Because I've watched SLO spreadsheets rot.

**Ana:** In version control, as configuration — the reference stack uses OpenSLO for vendor-neutral definitions and Sloth to generate the Prometheus rules, so nobody hand-writes burn-rate math. Grafana shows compliance, budget remaining, burn rate, and remaining allowable downtime. But the commitment is capability-level: definitions in git, rules generated, status visible, alerts on burn. The tools are the worked example, not the mandate.

## The Schrödinger Backup

**Ben:** Backups. Ours run nightly and the jobs are green. What more do you want?

**Ana:** That's the Schrödinger backup — scheduled, green, and never restored. Simultaneously working and broken until the day you need it collapses the wave function. Backup jobs succeed silently for years while producing archives that can't actually rebuild a cluster. So the record puts the weight on the restore side: automated restoration of resources and volumes, validation of application health, logs, and data integrity after every restore, and restore tests on a schedule — weekly, say — in an isolated test cluster, with functional tests against the restored environment.

**Ben:** Weekly restore tests are real engineering time. Who pays for that?

**Ana:** The platform does, and the record is honest that this is recurring cost, not a milestone. But the scheduled restore test is the only evidence the backup capability exists at all. Everything before it is a job that writes to object storage. And note what's covered — not just volumes but the cluster's state itself: CRDs, Secrets, ConfigMaps — all landing in durable storage that replicates cross-region where DR requires it. Plus the RPO connection: backup frequency is tuned to the RPO, recovery automation to the RTO — the objectives drive the automation, never the reverse.

**Ben:** Does the platform team back up everything for everyone?

**Ana:** No — self-service, like everything else in this section of the journal. Teams configure their own backups; resources opt in through labels or configuration. The platform provides the capability, not a ticket queue. Same pattern as [[self-service-infrastructure]].

## Breaking Things on Purpose, Politely

**Ben:** Now the part where you break production during business hours. Deliberately. Sell me that.

**Ana:** The scheduling rule surprises people, but it's the sane one: prefer business hours, when engineers are available to respond. The alternative is midnight chaos — experiments scheduled when nobody's around, which voluntarily reproduces the worst conditions of a real incident. The point of injecting failure is to have people watching when it happens.

**Ben:** Still — "controlled" is doing a lot of work in that sentence.

**Ana:** It's doing all the work, and the record spells it out. Every experiment has a meaningful failure scenario, a scope, a target workload, a duration, an expected steady state established before the run, and abort conditions with safety boundaries. Schedules are predictable and communicated to affected teams. You avoid peak traffic unless peak-load resilience is the explicit objective, and the aggressive stuff runs in dedicated DR drills or low-traffic windows. That's the difference between controlled science and vandalism. On the reference stack it's Chaos Mesh — Kubernetes-native, abortable, and it exports its own metrics so you can compare what the tool claims it injected with the pod churn you actually observed.

**Ben:** And you're watching what, exactly, while it runs?

**Ana:** Everything the objectives are written in: latency percentiles, restart counts, request success rates, connection-pool behavior, SLO burn-rate alerts, recovery-failure alerts — and, where possible, the correlation to business metrics: users impacted, revenue impact. A chaos result should read in business terms, not just kubectl output. Then the loop: review, identify gaps, create remediation work, retest after the fix. Without that last step it's chaos theater — a game day with slides and applause and no backlog.

**Ben:** One objection you haven't touched: our riskiest dependencies are managed. RDS, managed Kafka. That's the provider's problem.

**Ana:** The record calls that the trusted dependency, and it's the anti-pattern I'd bet finds the most gaps. Managed doesn't mean immune — slow queries, connection-limit exhaustion, failovers, cross-region latency all happen to managed services. And when they do, what's actually under test is your retry logic, your backoff, your circuit breakers, your graceful-degradation path. The provider's SLA is a refund policy, not a resilience strategy. So you test the degradation before an outage tests it for you — including the managed database failover procedure itself.

## The Drill Is the Document

**Ben:** Disaster recovery. Every org I've seen has a DR document. Most have never opened it under pressure.

**Ana:** The paper failover — replica promotion documented, DNS failover configured, nothing ever executed. A DR plan whose first rehearsal is the disaster. DR documents age instantly: the promotion command that changed, the DNS record nobody updated, the monitoring that goes dark exactly when the region does — which is why the record explicitly requires monitoring to keep operating during failover. The build itself is what you'd expect: recovery priorities for what must survive catastrophe, an explicit multi-region decision with the replication and standby environments to back it, and documented failover and promotion procedures. But none of that is DR yet.

**Ben:** What makes it DR?

**Ana:** Drills against the numbers. Regular drills that measure actual recovery time and compare it to the stated RTO and RPO, with procedures updated from results. And here's the reframe worth keeping: a drill that misses its target is a successful drill — it found the gap on a Tuesday instead of during the incident.

**Ben:** Alright. Close it out — what is this record explicitly not doing?

**Ana:** It doesn't build the telemetry it rides on — that's [[observability-implementation]]. It doesn't inject load — [[cost-performance-scalability]] does load, autoscaling, and cost; this record injects failure. The conceptual operating discipline — incidents, on-call, support — is [[operating-platforms]]; this is that discipline made self-testing, which is also why it's pillar four of [[four-pillars]] in executable form. And it's not adversarial — attack-shaped testing lives in [[platform-security]].

**Ben:** And the revisit triggers?

**Ana:** Each one is the loop breaking somewhere. A real incident exceeds an RTO the drills claimed we could meet. Restore validation lapses while backup jobs stay green. Budgets burn repeatedly and no freeze ever triggers. Or the chaos schedule stalls because remediation piles up unretested — the record calls that one fix and forget.

**Ben:** So the one-line test, for the exec who reads nothing else?

**Ana:** For every resilience claim your platform makes — show me the date and result of the last time you exercised it. If the answer is "never," you don't have resilience. You have hope with a dashboard.
