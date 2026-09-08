---
timetoread: "8 min listen"
---

## The Loop, Not the Stack

**Ben:** Blunt version first. Every team I know already has Prometheus and Grafana running somewhere. Why does observability need a reference-implementation record — isn't this a solved problem you install?

**Ana:** That's exactly the confusion the record exists to kill. Installing the stack is not the capability. The bar in this record is a closed loop: a deployment degrades user experience, telemetry catches it, an actionable alert reaches the team that can fix it, remediation follows — and MTTD and MTTR measurably drop. Plenty of organizations have Prometheus and Grafana and can't run that loop once. They have the retrofit: observability wired in after the first bad incident, forever partial.

**Ben:** So what makes it a *platform* capability rather than something each team does well on its own?

**Ana:** Correlation. Any team can install an agent; no team alone can make its telemetry line up with everyone else's. The value lives in the joins — the trace ID connecting a customer-facing error to a pod eviction three layers down. Joins need shared conventions, shared identifiers, a shared pipeline. That's platform work by definition. The record's three-signal framing makes it concrete: metrics tell you *what* happened, logs tell you *how*, traces tell you *why* — and common identifiers stitch them into one investigation. Three excellent silos that can't be joined answer three local questions and fail the one that matters.

**Ben:** Which is?

**Ana:** What is happening to users right now, and why. That's the single-pane-of-glass strategy — one deliberate answer to that question, instead of a graveyard of disconnected dashboards each once useful to someone.

## Vendor Neutrality and the Split

**Ben:** The record leans hard on OpenTelemetry. Isn't standardizing on one instrumentation framework just a different vendor lock-in?

**Ana:** It's the opposite move, and it's the chapter's quiet masterstroke: separate what must be stable from what may churn. Instrumentation, semantic conventions, and the OTLP wire format are forever; the backend behind the collector is a procurement decision. Backends *will* churn — pricing changes, scale changes, the build-versus-buy answer changes as you mature. The record treats that as a standing decision: assess maturity, service count, budget, compliance, data residency — and revisit. You can only revisit cheaply if your services aren't tattooed with a vendor's SDK. The vendor tattoo is on the anti-pattern list because the migration bill gets priced in engineer-years.

**Ben:** Fine, but here's the practitioner objection to the responsibility split. If the platform team owns observability, teams will throw instrumentation over the wall. If teams own it, you get fifteen stacks. Pick your failure.

**Ana:** The record refuses both. Platform owns the pipeline — collectors built for batching, buffering, retries, high availability; storage with retention, backups, and a scaling plan; dashboards as a service. Development teams own instrumenting their own code. What connects them is an explicit observability contract — non-functional requirements, stated — plus starter kits, reusable SDK configurations, and self-service, so honoring the contract is cheaper than evading it.

**Ben:** A contract nobody enforces is a wish.

**Ana:** Which is why enforcement lives in CI/CD, not in a policy document. Pipelines fail when required metrics endpoints are missing, when structured logs aren't emitted, when trace spans are absent. Telemetry gets verified in staging before promotion. Uninstrumented code does not reach production — the record calls the alternative the optional endpoint: the service whose missing `/metrics` you discover during the incident. A standard that isn't machine-checked is a suggestion, and suggestions lose to deadlines.

**Ben:** And the collectors themselves, the metrics database — who watches the watcher?

**Ana:** The record names that anti-pattern too — the unwatched watcher. The observability stack is operated like production: service discovery, retention policies, backups, scaling, and metrics that reveal degradation *before* complete failure. Plus deliberate transport choices — pull for metrics, push for traces, hybrid for logs — and ingestion that doesn't load down the workloads it's watching.

## Personas, Alerts, and the Pager

**Ben:** The persona list feels expansive — executives, QA, security, compliance, external customers. Isn't observability for the people on call?

**Ana:** That's the narrowest reading, and the chapter rejects it. Eight consumers, each with a named view: customers get service health, executives get business KPIs, developers get debugging depth, QA gets release validation, DevOps and SRE get incident diagnostics, security gets forensics, compliance gets immutable audit trails. And the delivery mechanism matters: dashboards are code — templated, version-controlled, annotated with deployment and incident markers, edit-restricted. Security observability rides the same pipeline: policy violations, RBAC denials, vulnerabilities as metrics — sanitized aggregates broadly, sensitive detail restricted, security events joinable to traces.

**Ben:** Let's do alerting, because this is where every observability effort I've seen dies. More telemetry means more alerts means everyone ignores the pager.

**Ana:** The record's test is one sentence: every alert must answer *what action should I take?* If there's no action, it's a dashboard, not an alert. Alert on user-impacting symptoms, not internal causes; attach severity and a runbook; use fast-burn alerts for outages and slow-burn for gradual degradation; group related alerts, route by business impact, silence during maintenance. And prune — alerts that repeatedly fire without producing action get removed or redesigned, because each one trains responders to ignore the pager, and that training is expensive to undo. The pager firehose isn't an alerting problem, it's a discipline problem.

## SLOs as Code, and What This Isn't

**Ben:** SLOs, then. Most SLOs I've met live in a slide deck from two reorgs ago.

**Ana:** The wiki SLO — an opinion wearing an SLO's clothes. The record's version is a control system: SLIs that reflect actual user experience, SLOs with error budgets displayed in real time, and error-budget health allowed to govern deployment velocity — a governor no release-review meeting can match. And the definitions live in Git: code-reviewed, rollback-capable, deployed through GitOps, synchronized with recording rules, dashboards, and alerts, consistent across environments with thresholds allowed to differ. Two details I'd flag for any executive: SLOs are defined for internal platform services too — the platform holds itself to the bar it sets for tenants — and deployments are validated against SLOs before promotion.

**Ben:** And the pipeline measuring itself — build times, flakiness — isn't that scope creep into the CI/CD record?

**Ana:** It's the seam, deliberately kept thin. This record takes only what closes the loop: deployment metadata published as telemetry, deployments auto-correlated with what follows, and pipeline performance — build duration, test time, deployment frequency, flakiness — measured so the platform team finds its own bottlenecks instead of hearing about them. The full CI/CD service is [[cicd-as-a-platform-service]].

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's the telemetry build, not the operating discipline — incidents, on-call, and support live in [[operating-platforms]], running on what this record builds. Hardening the platform is [[platform-security]]; here security is only a telemetry consumer. Cost visibility and optimization are [[cost-performance-scalability]]. And the stack itself — OpenTelemetry, Prometheus, Grafana, Flux — is the handbook's worked example, not a mandate: swap any tool, keep every property.

**Ben:** So the acceptance test, in one line?

**Ana:** Break something quietly and start a stopwatch. If the deployment that hurt users finds its own way — through telemetry, correlation, and one actionable page — to the team that can fix it, the capability exists. If a human has to notice first, you own a stack, not observability.
