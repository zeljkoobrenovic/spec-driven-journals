---
timetoread: "2 min read"
---

In my organization, CI/CD is a **service the platform ships, not a craft each team practices**: one versioned platform repository of reusable actions and pipeline templates, consumed by reference; team pipelines shrunk to roughly thirty lines that declare *what* while the platform owns *how*; scanning as a gate, delivery as a progressive rollout with automated rollback, and the pipeline itself instrumented so its value is measured, not asserted. This record is part of the Reference Implementation section — the end-to-end shape I hold a platform team to when it builds this capability.

**What changes**

* **One platform repository, run like a product.** Composite actions, composed workflow templates, tests, and docs in one place — semantically versioned (`v1.2.3` releases, floating `v1` tags), pinned by teams, with breaking changes shipped alongside migration guidance. The platform's own actions have CI; an invalid action cannot be released.
* **Team pipelines become minimal wrappers.** Under roughly thirty lines of typed inputs, defaults, and workflow-level secrets, with controlled escape hatches. Team-specific logic that keeps growing is investigated as a missing platform capability — roadmap input, not local color.
* **The registry becomes a trustworthy boundary.** The reusable container-build action scans every image; HIGH or CRITICAL findings fail the build, and a vulnerable image is never pushed.
* **Every release watches itself.** Canary or blue-green per service, deployment analysis wired to live success-rate thresholds, unhealthy releases stopped or rolled back automatically, the previous stable release verified recoverable. The pipeline ends at a GitOps manifest; the cluster machinery of [[platform-creation]] applies it.
* **The pipeline is measured end to end.** Telemetry from trigger through deployment — stage timings, failures tied to commits, traces in dashboards — against a recorded baseline, so DORA metrics, adoption rate, and pipeline line-count reduction are demonstrable.

**What it costs**

* A baseline inventory before the build — workflow counts, YAML line counts, DORA and scan-pass-rate baselines — because migration claims need before/after evidence.
* Product discipline on the platform side: versioning, migration docs, and a real application migrated end to end as the first release, not an announcement memo.
* A shared template is a single point of coordinated breakage; semantic versioning and pinning are the standing tax that makes it safe.

**What we are not doing**

* Not mandating the reference stack — GitHub Actions, Trivy, Argo Rollouts, Flux, and OpenTelemetry are the worked example; the commitments hold at the capability level.
* Not the platform-wide observability stack ([[observability-implementation]]), the end-to-end security story ([[platform-security]]), or in-cluster policy enforcement ([[policy-as-code]]) — this record carries only the pipeline's own telemetry and gates.
* Not day-one wiring for new services — that lives in [[starter-kits]]; this record builds the service and migrates the existing estate.

*The Article tab carries the rationale, reference stack, and anti-patterns; the Checklist tab carries the full build checklist. Grounded in the "CI/CD as a Platform Service" chapter of the* Platform Engineer's Handbook*.*
