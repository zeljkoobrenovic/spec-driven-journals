---
timetoread: "2 min read"
---

When a platform team in my organization secures a Kubernetes platform, security is built as **one chain, end to end**: central OIDC identity with short-lived tokens, namespace-scoped least-privilege RBAC, per-pipeline machine identities, admission policies that reject noncompliant workloads, deny-by-default networking with strict mTLS and automated TLS, and a tamper-protected audit trail. Two tests run through the build: every control is proven by deliberately trying to violate it, and any action can be traced from login through token to Kubernetes API call.

**What changes**

* **Identity is central and short-lived.** People authenticate through one OIDC realm; groups carry authorization into Kubernetes RBAC; tokens expire in roughly fifteen minutes, so a leaked token is a small problem rather than a standing credential.
* **Least privilege is verified, not declared.** Developers hold namespace-scoped roles and provably cannot touch system namespaces; admins get troubleshooting permissions, not omnipotence; every claim is checked with `kubectl auth can-i`. No human or service account keeps unnecessary cluster-admin.
* **Pipelines become first-class identities.** One narrowly scoped service account per pipeline, short-lived projected tokens instead of permanent credentials, secrets kept out of build logs — and negative tests proving what each account cannot do.
* **Policy runs at admission, encryption runs by default.** Gatekeeper (in the reference build) rejects unapproved registries, missing resource limits, privileged and root containers, and unlabeled namespaces before they run; NetworkPolicies block unnecessary paths; mTLS is strict inside, and cert-manager renews external TLS automatically.
* **Evidence and rehearsal close the chain.** Audit logs record identity, decisions, secrets access, and privileged operations — centralized, tamper-protected, retained, and alerted on — and the build ends with a credential-compromise drill: detect, revoke, trace, size the blast radius, fix, and re-test.

**What it costs**

* Negative testing is real work: every control must reject a deliberate violation before it counts as done — a control that has never rejected anything is a hope, not a control.
* Least privilege at build time means friction: per-pipeline service accounts and scoped roles cost minutes now to avoid an ungovernable cluster-admin topology later.
* The drill, permission reviews, and policy updates recur on a schedule — this is a standing practice, not a launch ceremony.

**What we are not doing**

* Not the full policy-as-code practice — authoring, testing, and policy lifecycle live in [[policy-as-code]]; this record installs admission control as one link.
* Not building the environments or the mesh — [[platform-creation]] builds them; this record hardens them. Platform-level secrets hygiene stays in [[groundwork]].
* Not the full telemetry stack — that is [[observability-implementation]]; this record takes only the security slice of audit, alerting, and correlation.
* Not the general operating discipline — incidents, on-call, and support live in [[operating-platforms]], which consumes the drill and evidence layer this record builds.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the complete build, validation pass, and final security review. Grounded in the* Platform Engineer's Handbook *security chapter checklist.*
