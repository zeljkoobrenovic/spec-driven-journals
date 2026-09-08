---
timetoread: "8 min listen"
---

## The Thing Every Team Thinks It Owns

**Ben:** Straight to the sore spot. CI/CD is the one thing every engineering team already does and already has opinions about. Why does an operating model take it away from them?

**Ana:** Because nobody is taking anything away — the record takes over the part teams never wanted: the *how*. Start with what the baseline inventory finds in most organizations: hundreds of workflows, thousands of lines of YAML, and reuse implemented by copy-paste. The record calls that copy-paste as a service. Every copied pipeline is a fork that will never be merged — every improvement becomes N pull requests, every bug becomes immortal, and every security fix rolls out at the speed of the slowest team.

**Ben:** So what does the team keep?

**Ana:** The *what*. A team pipeline becomes a minimal wrapper — the target is under roughly thirty lines — of typed inputs: language, service name, deploy target, secrets at the workflow level. Everything about *how* — testing, linting, container build, scanning, deployment stages — lives in versioned platform templates the team references like any other dependency.

**Ben:** Thirty lines sounds like a slogan, not an engineering number.

**Ana:** It's a measurement of abstraction quality. If a team's workflow fits in thirty lines, the platform is genuinely absorbing the complexity. If the file keeps growing, one of two things is true: the team is routing around the platform, or the platform is missing a capability many teams need. Either way, the record's move is the same — investigate large team-specific logic as a possible missing platform capability. It's a discovery mechanism, not a compliance rule.

## One Template to Break Them All

**Ben:** Here's the practitioner nightmare, though. The day everyone references one template, one merge to that template breaks every pipeline in the company at once. You've built a single point of coordinated breakage.

**Ana:** You have — unless you run the repository like a product, which is why the versioning section is not optional plumbing. Semantic versioning throughout: major for breaking, minor for compatible features, patch for fixes. Specific release tags like `v1.2.3` so teams can pin, floating major tags like `v1` for teams that want compatible updates automatically, and breaking changes documented with migration requirements. Nobody references `main`. The anti-pattern even has a name: pinned to `main`.

**Ben:** And the platform's own code? Platform teams are famously the cobbler's children — CI tooling with no CI.

**Ana:** The record closes that explicitly. Every platform action is validated in its own CI — syntax, required fields, supported types, every input described, composite actions that actually contain steps — and an invalid action cannot be released. A platform that ships a broken action ships an outage to everyone simultaneously, so the platform's actions are tested like the software they are. That's [[four-pillars]] pillar two applied to CI/CD: a real software abstraction with an owned lifecycle.

**Ben:** This is all GitHub Actions language. What happens when we're not a GitHub shop?

**Ana:** The reference stack — GitHub Actions, Buildx, Trivy, Argo Rollouts, Flux, OpenTelemetry — is the worked example, named honestly because the record is grounded in a build-it-end-to-end handbook. The commitments hold at the capability level: reusable tasks in one versioned repository, minimal team wrappers, a scan gate, progressive delivery, pipeline telemetry. Swap any vendor; the shape survives.

## Gates, Not Reports

**Ben:** The scan gate. Security scanners cry wolf for a living. Fail every build on findings and teams will spend their lives triaging — or bypassing.

**Ana:** Which is why the threshold is explicit: HIGH or CRITICAL fails the build, and — this is the part with teeth — the vulnerable image is never pushed to the registry. Not "pushed with a warning," never pushed. The alternative is the advisory scanner: dashboards of known vulnerabilities already running in production. A scan that ships anyway is theater. The gate makes the registry itself a trustworthy boundary, at the cheapest point to stop a bad artifact.

**Ben:** And when the gate accumulates exceptions?

**Ana:** Then the record's own revisit trigger fires — routine bypasses mean the gate has become theater, and the record gets revisited rather than quietly hollowed out. Worth saying what this gate is *not*, too: it's the pipeline's slice of security only. The cluster-side story is [[platform-security]], and admission-time enforcement is [[policy-as-code]].

**Ben:** Next gate: progressive delivery. Canary infrastructure is real complexity. Why is it in the default pipeline and not an advanced option?

**Ana:** Because the alternative is the big-bang deploy — one hundred percent of traffic switched at once, and rollback as a manual redeploy performed under pressure at 2 a.m. The reference build uses Argo Rollouts: blue-green where instant switching is useful, canary where gradual traffic shifting is preferred — chosen per service, not one strategy mandated for all. Deployment analysis is wired to Prometheus success-rate thresholds, unhealthy releases stop or roll back automatically, and the previous stable release is verified recoverable before anyone needs it. Rollback stops being heroics and becomes a property of the platform.

**Ben:** And the pipeline's job ends where?

**Ana:** At a GitOps manifest change. The pipeline commits the new image reference; Flux detects and applies it; Rollouts takes the release from there. The cluster machinery belongs to [[platform-creation]] — the migration checklist verifies the handoff end to end.

## Proving It Worked

**Ben:** Last objection, and it's the one my CFO would raise. Platform teams love this consolidation story. How do we know it actually paid?

**Ana:** Because the record makes the pipeline itself observable — and makes you take the baseline *before* you build. Workflow counts, total YAML line counts, adoption rate, and the delivery numbers: deployment frequency, lead time, change failure rate, mean time to restore, p95 build duration, scan pass rate. Then telemetry flows through an OpenTelemetry Collector — workflow events in, metrics to Prometheus, traces to the tracing backend, visible in Grafana. Every run traceable from trigger through deployment, time in tests, builds, and deploys measured, failures associated with the commits that caused them.

**Ben:** So bottleneck debates end.

**Ana:** Anecdote loses its seat at the table, yes. And the same telemetry produces the platform's proof of value: adoption rate climbing, line-count reduction demonstrated, DORA metrics moving — the evidence [[platform-success]] asks every platform to carry. Not a slide. A dashboard.

**Ben:** And the measurement isn't a team scoreboard?

**Ana:** Explicitly not — the record's contrast table says so. The telemetry exists to find pipeline bottlenecks and prove the platform's value, not to grade teams.

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's one offering, built end to end. The platform-wide observability stack is [[observability-implementation]] — here we instrument only the pipeline. End-to-end security is [[platform-security]]; in-cluster policy is [[policy-as-code]]. Day-one wiring for new services is [[starter-kits]] — this record migrates the existing estate, starting with one real application moved onto the platform pipeline, with documentation and migration guidance so the second migration is cheaper than the first. And the product mechanics it leans on throughout are [[platform-as-a-product]].

**Ben:** The one-sentence test?

**Ana:** A real service deploying through a pinned platform pipeline declared in under thirty lines of team-owned YAML — where a vulnerable image cannot reach the registry, an unhealthy release rolls itself back, and the before-and-after numbers are on a dashboard. If your team's pipeline is growing instead, that's not their problem to solve. It's the capability we haven't built yet.
