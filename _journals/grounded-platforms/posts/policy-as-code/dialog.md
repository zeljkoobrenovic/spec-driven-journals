---
timetoread: "8 min listen"
---

## Rules That Machines Hold

**Ben:** Blunt version first. We already have security standards, a review board, and a wiki page everyone signed. Why does policy need to become code?

**Ana:** Because a policy that lives in a document and a review meeting is not a guardrail — it's a hope with a signature line. [[four-pillars]] demands guardrails with safe defaults as part of serving a broad developer base; this record is that demand made executable. The record's opening anti-pattern is the compliance PDF: complexity relocated and annotated, never enforced. Policy as code is what makes the standard hold at three in the morning, on the hundredth deployment, for the team that never read the wiki. If no machine holds the rule, there is no rule.

**Ben:** And this is a Reference Implementation record, so there's a concrete stack behind it?

**Ana:** The *Platform Engineer's Handbook* builds it end to end: OPA Gatekeeper for admission control and audit, Rego as the policy language, Conftest for shift-left testing, Prometheus and Grafana for compliance visibility, optionally Backstage to surface it per service. But the stack is the worked example, not the mandate. The commitments are capability-level: one policy source, three gates, a core floor, progressive enforcement, visible compliance.

## Three Gates, One Source

**Ben:** Unpack "three gates." Isn't an admission controller enough? It's the only gate nobody can bypass.

**Ana:** It must exist for exactly that reason — and it's the worst place for a developer to discover a policy. The cost of feedback rises at every stage: a violation caught at the desk costs seconds, in the pull request minutes, at admission a broken deployment and an interrupted afternoon. So the same policies run locally with Conftest and in pre-commit hooks, then as a policy-validation job on every pull request that fails the pipeline on required violations and puts the feedback directly in the PR, and only then at the admission webhook as the backstop. A platform whose developers first meet a policy when the cluster bounces their release has built a tollbooth, not a guardrail. The record calls that the last-gate discovery.

**Ben:** Practitioner objection: I've seen exactly that architecture rot. CI checks one rule set, the cluster enforces a slightly different one, and now I have a green pipeline and a red deployment.

**Ana:** The split brain — it's on the anti-pattern list because it kills trust in both gates at once. That's why "one source" is in the principle, not just "three gates." The same Rego that Gatekeeper evaluates at admission sits in the `policy/` directory that Conftest runs at the desk and in CI. Versioned, reviewed, released like any other platform software. The gates can't drift because there's nothing to drift between.

**Ben:** What's actually in the floor — the policies that always enforce?

**Ana:** The chapter's core set: CPU and memory requests and limits for every container; no containers running as root; no privileged containers; read-only root filesystems where appropriate; dangerous Linux capabilities like SYS_ADMIN blocked; and images restricted to approved registries. Plus one requirement that isn't a rule but a property of every rule: a clear, human-readable violation message.

**Ben:** That last one sounds like politeness, not policy.

**Ana:** It's a user interface. The difference between a guardrail and an obstacle is usually one sentence — the one that tells the developer what to change. "Your container has no memory limit; add one" teaches. A raw policy-engine trace punishes. The record is blunt about it: a policy that cannot explain itself does not get to block a deployment. The source's final validation makes understandable remediation feedback a condition of being done, right next to blocking critical violations.

## Audit Before Enforce

**Ben:** Here's where I push hardest. Every policy rollout I've lived through went the same way: security flips everything to enforce on a Tuesday, half the org's deployments break, and by Friday there's an exemption process with a six-week queue.

**Ana:** The big-bang deny — and the record rejects it structurally, not just tonally. Enforcement is progressive: new policies start in audit mode where appropriate, developers are educated about why each policy exists before it starts blocking them, feedback and exemption requests get reviewed, and policies that create unnecessary friction get fixed rather than defended. Then risk sets the pace. Genuine security exposures — privileged containers, dangerous capabilities — move to enforcement. Lower-risk standards stay monitored until the audit data and the education have done their work.

**Ben:** Doesn't audit mode become the parking lot? A dashboard of violations nobody remediates, forever?

**Ana:** The eternal audit — also named. Audit is a phase with an exit decision, not a destination. Every audit-mode policy carries an implicit decision date: enforce it or retire it. That's one of the record's revisit triggers — audit-mode policies persisting for quarters without a decision means the mechanism has stalled.

**Ben:** And exemptions? Someone always genuinely needs to run privileged.

**Ana:** Exceptions are reviewed instead of becoming permanent workarounds — that's straight from the final validation. System namespaces are excluded explicitly and deliberately; everything else that gets an exemption goes on a review cadence. The permanent exemption is the quiet failure mode: granted once, never revisited, growing until the floor is decorative.

## Watching Compliance

**Ben:** Why does the build include a whole monitoring leg? Enforcement either works or it doesn't.

**Ana:** Because admission control only tells you what was stopped. Continuous audit tells you what's already running in violation — the workloads deployed before the policy existed. So the build enables Gatekeeper auditing, scrapes its metrics into Prometheus, breaks violations down by constraint and by namespace, and puts a dashboard in front of stakeholders: total violations, violations by constraint, by namespace, compliance rate, and remediation progress over time. Compliance you cannot see is compliance you do not have.

**Ben:** A dashboard of violations by namespace sounds like a leaderboard of shame.

**Ana:** It's a remediation instrument, and it's also what makes exceptions governable — an exemption on a dashboard gets reviewed; an exemption buried in a YAML annotation becomes permanent by default. And the visibility goes where developers already look: optionally, Backstage shows each service its violation count, the most recent audit time, policy status, and a service-level compliance scorecard. The revisit trigger on this leg is telling: if the dashboard shows the same violations recurring without remediation, visibility exists but the loop back into enforcement and education is broken.

## The Wider Map

**Ben:** Last structural question. Once you have a working admission controller, the temptation is to shove everything through it — cost rules, account rules, data residency.

**Ana:** The Kubernetes hammer. The cluster is one layer of governance, not the whole map. The build includes an explicit decision about which policies Gatekeeper enforces at the Kubernetes level and which are better handled by AWS, Azure, or GCP governance tools — with an eye on lock-in where portability matters — plus export paths so compliance data reaches audit and security systems that need it. And the least glamorous commitment: named ownership for policy creation, review, and remediation. A rule nobody owns is a rule nobody can change, explain, or safely delete.

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's the policy engine and its lifecycle, nothing more. The end-to-end security build — identity, network, secrets, supply chain — is [[platform-security]]. Pipeline architecture is [[cicd-as-a-platform-service]]; this record just adds the policy gate to it. The metrics and dashboard stack is [[observability-implementation]]; this adds compliance panels on top. The cluster and GitOps baseline these policies protect is [[platform-creation]]. And it's not an OPA mandate — the stack is the reference implementation, the commitments hold whatever engine a team picks.

**Ben:** And the one-line test, for the team that builds it?

**Ana:** Deploy a deliberately non-compliant workload. If it gets in, the gates aren't real. If it gets rejected with a message its author can't act on — the gates are real and the platform just made an enemy. Done is both: blocked at admission, and explained in a sentence a developer can fix before lunch.
