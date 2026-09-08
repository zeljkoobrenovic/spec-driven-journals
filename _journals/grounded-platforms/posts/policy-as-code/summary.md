---
timetoread: "2 min read"
---

When a platform team in my organization implements policy as code, the build I hold them to is **one policy source evaluated at three gates**: at the developer's desk before commit, in the pipeline on every pull request, and at cluster admission as the backstop. Policies are versioned code held by machines, enforcement is progressive rather than indiscriminate, and a policy that cannot explain itself does not get to block a deployment.

**What changes**

* **Three gates, one source.** The same policy code runs locally and in pre-commit hooks, fails the pull-request pipeline on required violations with feedback in the PR itself, and is enforced by a validating admission webhook — so what CI checks and what the cluster enforces can never drift apart.
* **A core security floor.** Resource requests and limits required for all containers; no root, no privileged containers, no dangerous capabilities, read-only root filesystems where appropriate; images from approved registries only — each with a clear, human-readable violation message that names the fix.
* **Progressive enforcement.** New policies start in audit mode where appropriate; developers are told why each policy exists; feedback and exemption requests are reviewed and friction gets fixed. Genuine security risks move to enforcement; lower-risk standards stay monitored until the data supports enforcing them.
* **Visible compliance.** Continuous audit of what is already running, metrics by constraint and by namespace, and a dashboard — total violations, by constraint, by namespace, compliance rate, remediation over time — accessible to stakeholders, optionally surfaced per service in the developer portal.
* **A deliberate governance map.** Kubernetes-level rules enforced in the cluster, provider-level rules left to cloud governance tools, compliance data exported where audit requires it — and named ownership for policy creation, review, and remediation.

**What it costs**

* Policy authoring is engineering work: rules, remediation messages, exemption review, and the enforce-or-retire decision on every audit-mode policy are an owned lifecycle, not a one-time setup.
* Progressive enforcement is slower than a big-bang deny — deliberately: turning everything on at once breaks teams and teaches the organization to route around policy.
* Visibility carries obligations: metrics, dashboards, and a review cadence that keeps exceptions from quietly becoming permanent.

**What we are not doing**

* Not the end-to-end security build — identity, network, secrets, and supply chain live in [[platform-security]].
* Not pipeline architecture or the observability stack — this record adds a policy gate to [[cicd-as-a-platform-service]] and compliance panels to [[observability-implementation]].
* Not mandating OPA — Gatekeeper, Rego, and Conftest are the reference stack; the commitments hold whatever engine a team picks.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full build, from admission controller to compliance dashboard. Grounded in the* Platform Engineer's Handbook*.*
