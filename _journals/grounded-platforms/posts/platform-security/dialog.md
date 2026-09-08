---
timetoread: "8 min listen"
---

## One Chain, Not a Shopping List

**Ben:** Blunt version first. Every platform team already runs RBAC, a policy engine, a mesh, some audit logging. Why does an operating model need a record for a Kubernetes hardening checklist?

**Ana:** Because "we have all the pieces" and "the pieces form a chain" are different claims, and the second one is the record. Most platforms have security as a shopping list — RBAC here, Gatekeeper there, mTLS half-enabled — each bought separately, each assumed to work. This record builds it as one chain, in order: human identity, least-privilege authorization, machine identity, admission control, network and transport, and evidence. Each link assumes the previous one fails. Short-lived tokens assume credentials leak. Namespace-scoped RBAC assumes tokens get stolen. Admission policy assumes a compromised pipeline pushes a bad image. The audit trail assumes all of the above and answers *what happened*.

**Ben:** And the tests running through it?

**Ana:** Two. Every control is proven by deliberately trying to violate it — the noncompliant deployment Gatekeeper must reject, the service account that must fail to cross a namespace. And one action must be traceable from login through token to Kubernetes API call. The line I'd put on the wall: a control that has never rejected anything is a hope, not a control.

**Ben:** The record names a very specific stack — Keycloak, Gatekeeper, Istio, cert-manager. Is this a tooling mandate?

**Ana:** No, and the record is explicit: the stack is the worked example, not the mandate. The commitments are at capability level — one OIDC realm with group claims and roughly fifteen-minute tokens, an admission controller that rejects at the door, verified strict mTLS. The reference-stack table exists so nobody has to guess what a passing build looks like; swap any tool that keeps the same properties.

## Identity, and Why Fifteen Minutes

**Ben:** Fifteen-minute tokens. That sounds like a great way to make developers hate the platform — re-authenticating four times an hour.

**Ana:** The token lifetime is fifteen minutes; the login session isn't. OIDC refresh handles renewal invisibly. What the short lifetime buys is that a leaked access token is a small problem instead of a standing credential — the window between theft and uselessness is a coffee break. And because groups ride in the JWT and map to Kubernetes RBAC groups, revoking a person is one change in the identity provider, not an archaeology dig through kubeconfigs.

**Ben:** RBAC next. Every organization claims least privilege. What makes this record's version more than the claim?

**Ana:** Verification. The record doesn't say "developers should be limited to their namespaces" — it says the build isn't done until someone has confirmed developers cannot view or modify system namespaces, and checked every claim with `kubectl auth can-i`. Claims about permissions are read from the manifest; facts about permissions come from asking the API server. And the binary question at the end of the final review: does any human or service account hold unnecessary cluster-admin? The record's anti-pattern is the convenience admin — cluster-admin granted during setup to make things work, never revoked, until the platform's real security posture is whatever the oldest kubeconfig can do.

**Ben:** Why is clawing that back so hard that it justifies day-one discipline?

**Ana:** Because "temporary" cluster-admin becomes the permanent topology. Six months in, nobody knows which automations depend on it, so nobody dares revoke it. Scoping people and pipelines correctly at build time costs minutes. Unwinding it later is an organizational project with a risk register.

## The Robot Problem

**Ben:** Machine identity gets its own link in the chain. Isn't a CI service account just another user?

**Ana:** It should be, and that's the point — in practice it's held to a far lower standard. Humans get MFA, reviews, offboarding. The CI account gets a permanent token pasted into a variable in 2019, and it deploys to production every day. This is where platforms are most exposed. So the record: one service account per application or pipeline, scoped to a single namespace, granted only what the pipeline actually does, short-lived projected tokens instead of permanent credentials, and credentials scrubbed from build logs.

**Ben:** One account per pipeline sounds like bureaucracy. Why not one well-guarded deployment account?

**Ana:** The shared robot is a named anti-pattern. When the shared account leaks, the blast radius is the whole platform — and the audit log says only "the robot did it." Per-pipeline accounts make the blast radius one namespace and make the audit trail name a culprit. And note the verification runs both ways: the account demonstrably can do its permitted deployments, and demonstrably cannot reach other namespaces or perform operations it was never granted. The negative test is the control.

**Ben:** Admission control — but there's a whole separate record called [[policy-as-code]]. Why does Gatekeeper appear twice in this journal?

**Ana:** Different altitude. Here, admission control is one link with a fixed baseline: approved registries, CPU and memory limits, no privileged containers, no root containers where the standard forbids them, required namespace labels with permitted values, PodDisruptionBudgets. Deploy it, then submit a deliberately noncompliant deployment and watch it bounce. The practice of authoring, testing, and evolving policies — the lifecycle — is [[policy-as-code]]. This record installs the lock; that record is the locksmith's trade.

## Encrypted Inside, Evidenced Throughout

**Ben:** Strict mTLS everywhere inside the cluster. The classic pushback: TLS at the edge is where the attackers are — why pay the mesh complexity tax for east-west traffic?

**Ana:** Because the perimeter assumption is the anti-pattern — the record calls it the soft interior. TLS at the edge and plaintext inside means one compromised pod reads the platform's east-west traffic. The chain logic again: network and transport protection assumes a workload is already breached. NetworkPolicies deny unnecessary paths — cross-namespace, host-level — and strict mTLS makes what remains unreadable. And "verified, not configured": the build checks that traffic is actually encrypted and unauthorized paths actually blocked. The external side is the same discipline automated — cert-manager issues and renews through the gateway, and expiry is monitored, because an expired certificate is an outage with a security costume.

**Ben:** The audit section reads like observability. Why is it in a security record and not [[observability-implementation]]?

**Ana:** Because here the audit trail is a security control, not a telemetry feature. The record requires the API audit log to record identity, timestamps, authentication and authorization decisions, secrets access, RBAC modifications, privileged operations, outcomes — plus the identity provider's login and token events — centralized, tamper-protected, retention-managed, alerted. Without that, incident response is archaeology. With it, the questions that matter — what did this credential touch, when, on whose authority — have answers in minutes. Tamper protection is the non-negotiable part: an audit log the attacker can edit is testimony from the defendant. The full telemetry stack is [[observability-implementation]]; this is its security slice.

**Ben:** And then the record makes teams stage a breach. Isn't the drill theater?

**Ana:** It's the opposite — the paper drill is the theater. A runbook that has never been run means the first real credential leak is the first rehearsal. The drill is a full loop: simulate an exposed service-account credential, detect it, revoke or rotate, verify the dead credential no longer works, trace the activity in the audit logs, determine the blast radius, document the timeline, implement preventive measures — and prove the fix in a repeat test. That last step is what converts architecture into capability. And it recurs on a schedule, with permission reviews and policy updates, because the chain drifts as the platform evolves.

## The Close

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** Five fences. It doesn't build the environments, GitOps machinery, or the mesh — [[platform-creation]] builds them; this record hardens them and switches mTLS to strict. It doesn't own platform-level secrets and release hygiene — that's [[groundwork]]. It doesn't carry the policy lifecycle — [[policy-as-code]]. It doesn't build the telemetry stack — [[observability-implementation]] does; this record takes the security slice. And it doesn't own the general operating discipline — incidents, on-call, support — that's [[operating-platforms]], which consumes the drill and evidence layer this record builds. The drill discipline generalizes beyond security in [[resilience-automation]], and the whole chain is pillar four of [[four-pillars]] — operated as a foundation — made concrete on the security axis.

**Ben:** So when does a platform in your organization get to call itself secure?

**Ana:** Not at architecture review. When the validation pass has run — admin, user, and CI identities each tested for what they can and cannot do, policies rejecting real noncompliant deployments, mTLS and TLS verified, one action traced from login to API call — and when the first drill has produced a documented timeline and a re-tested fix.

**Ben:** One sentence.

**Ana:** Every control has rejected a deliberate violation, every action can be traced to an identity — and until both are true, "secure" is a hope, not a property.
