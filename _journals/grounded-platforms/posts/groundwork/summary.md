---
timetoread: "2 min read"
---

Before a platform team in my organization builds anything for anyone else, it lays its own foundation — **and the foundation is code**. Repositories provisioned by IaC from one configuration file, secrets in a vault and never in source control, onboarding and offboarding as reviewed configuration diffs, conventional signed commits enforced on administrators too, and trunk-based delivery where pushes validate and annotated tags release through an approval gate. The test the build is held to: a second platform engineer can reproduce the entire foundation from the repository alone.

**What changes**

* **The foundation is a product from day zero.** Stakeholders identified, feedback loops short, metrics defined for adoption, reliability, delivery, and satisfaction, golden paths and sensible defaults established, and security, governance, testing, and compliance embedded from the beginning — the platform team is its own first customer.
* **Repositories and membership become configuration.** One file is the source of truth; repositories are created programmatically through preview → review → apply, with visibility set by configuration and delete protection proven against an accidental destroy. Joining, leaving, and role changes are applied-and-verified diffs, and admin access goes through a service account or group, not individuals.
* **Secrets discipline becomes mechanical.** Example files committed, real values gitignored, credentials pushed to the vault by a scripted authenticate–unlock–upsert–sync–lock flow and verified there. A credential is either never in source control or it is leaked; there is no mostly-clean history.
* **Commit and policy discipline is enforced, not requested.** Conventional commit messages validated by distributed hooks, branch protection and merge requirements applied through IaC, and signed commits required on every branch — administrators included — with both rejection and success verified.
* **Validation and release become different events.** Pushes trigger validation; annotated tags trigger the release workflow — tests, configuration validation, an approval gate, then apply — and rollback mechanisms are tested regularly, not documented and trusted. The groundwork ends with a first tagged, verified release.

**What it costs**

* Gates, signing, and vault discipline add friction on day one — accepted deliberately, because whatever is done manually "just this once" in week one becomes the permanent exception.
* Rollback testing recurs; it is standing work, not a one-time setup.
* The reference stack (Pulumi, Bitwarden, GitHub, CircleCI) must be learned even though the commitments are stack-agnostic.

**What we are not doing**

* Not mandating the reference stack — the tools are the worked example; the commitments hold under any stack with the same properties.
* Not building clusters, environments, GitOps, or the mesh yet — that is [[platform-creation]].
* Not yet offering CI/CD or onboarding as products to application teams — those are [[cicd-as-a-platform-service]] and [[self-service-onboarding]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full build sequence, exercises, and completion check. Grounded in the Groundwork chapter of* The Platform Engineer's Handbook*.*
