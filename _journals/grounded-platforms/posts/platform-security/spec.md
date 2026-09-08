---
status: accepted
revised: 2026-08-20
---

# Spec: End-to-End Platform Security

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the security build I hold a platform team to when they
secure a Kubernetes-based internal platform end to end. The post turns the
end-to-end security checklist of the *Platform Engineer's Handbook* into a
reference-implementation record: security is a single chain — human identity
(OIDC via Keycloak, short-lived tokens), least-privilege authorization
(namespace-scoped RBAC), machine identity (per-pipeline service accounts with
projected tokens), admission control (OPA/Gatekeeper), network and transport
protection (NetworkPolicies, strict mTLS, automated TLS), and evidence (audit
logging, alerting, and a rehearsed incident drill). The load-bearing ideas:
every control is validated by deliberately trying to break it; any user action
is traceable from login through token to Kubernetes API call; and no human or
service account holds cluster-admin without a defended reason.

## Audience

Platform leads and engineers in my organization building or hardening a
Kubernetes platform (the bar their build is held to); security and compliance
partners who need to know what the platform enforces by construction; peer
executives assessing whether "the platform is secure" is a claim or a chain of
verified controls. First-person declarative.

## Success criteria

- [x] **Highlight is quotable** — names the six-link chain (human identity →
      authorization → machine identity → admission → network and transport →
      evidence) and the
      two running tests: every control proven by a deliberate violation, every
      action traceable login → token → API call.
- [x] **Identity survives** — dedicated realm, OIDC client for the API
      server, platform-admins/platform-users groups, group-to-RBAC mapping,
      short-lived (~15-minute) tokens, API server OIDC configuration (issuer,
      client ID, username claim, groups claim), login tested, group membership
      confirmed in the issued JWT.
- [x] **Authorization survives** — team namespaces with governance labels
      (team, environment, cost-center), namespace-scoped developer Role and
      RoleBindings to identity groups, admin cluster-level troubleshooting
      permissions, developers confined to their namespaces and out of system
      namespaces, no unnecessary cluster-admin, permissions verified with
      `kubectl auth can-i`.
- [x] **Machine identity survives** — one service account per application or
      pipeline, scoped to a single namespace, least-privilege grants, no
      ClusterRoleBinding to cluster-admin, short-lived projected tokens over
      permanent credentials, credentials kept out of build logs, verified
      positively (can deploy) and negatively (cannot cross namespaces or
      perform unauthorized operations).
- [x] **Admission control survives** — Gatekeeper deployed; approved-registry,
      CPU/memory-limit, no-privileged, no-root, and namespace-label policies
      (with permitted values for team/environment/cost-center), system
      namespace exclusions, PodDisruptionBudget policy, a deliberately
      noncompliant deployment tested and rejected, violations monitored.
- [x] **Network and transport survive** — ingress and egress rules defined,
      NetworkPolicies created, cross-namespace and host-level access
      restricted, Istio strict mTLS verified, cert-manager with a configured
      issuer integrated with the Istio Gateway, Certificate resource and
      Secret, VirtualService configured, external HTTPS confirmed, automatic
      renewal verified and expiry monitored.
- [x] **Validation and evidence survive** — the three-identity validation
      pass (admin, user, CI/CD service account; authorized and unauthorized
      actions; boundaries, RBAC denials, policy rejections, network blocks,
      mTLS, external TLS; the login → token → API call trace) and the audit
      layer (API audit logging with identity, timestamp, authn/authz
      decisions, secrets access, RBAC modifications, privileged operations,
      outcomes; Keycloak login/token events; centralized, tamper-protected,
      retention-managed logs; alerts on security-sensitive changes; identity
      events correlated with cluster activity).
- [x] **The drill survives** — the credential-compromise drill (simulate,
      detect, revoke/rotate, verify dead, trace in audit logs, determine blast
      radius, document timeline, add preventive measures, re-test) and the
      final security review gates, including scheduled permission reviews,
      policy updates, and recurring drills.
- [x] **Tools are the worked example, not the mandate** — a reference-stack
      table names Keycloak, RBAC, Gatekeeper, NetworkPolicies/Istio,
      cert-manager, and audit logging as the reference tools while the
      commitments are stated at capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its End-to-End Kubernetes Platform Security checklist.

## Non-goals

- Not [[policy-as-code]] — Gatekeeper appears here as one link in the
  security chain (admission control with a fixed baseline policy set); the
  full policy-as-code practice — authoring, testing, and lifecycle of
  policies — is that record.
- Not [[platform-creation]] — building the environments, GitOps machinery,
  and the mesh lives there; this record hardens what that record builds
  (strict mTLS is switched on and verified here, the mesh itself is not
  re-argued).
- Not [[groundwork]] — platform-level secrets management and release hygiene
  live there; this record covers cluster identity and runtime credentials.
- Not [[observability-implementation]] — the full telemetry stack is that
  record; this one takes only the security slice: audit logs, security
  alerts, and identity correlation.
- Not [[operating-platforms]] — the general operating discipline (incidents,
  on-call, support); this record contributes the security drill and evidence
  layer that discipline consumes.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-20** — Grounded in the *Platform Engineer's Handbook* chapter
  checklist "End-to-End Kubernetes Platform Security" — read through a
  practitioner-executive lens, as with every record in this journal. (The
  source PDF is filed as "Platform Creation" 03; its title page carries the
  security title, which this record follows.)
- **2026-08-20** — Framed the chapter's nine tool-specific sections as one
  identity-to-evidence chain rather than a list of independent controls: the
  chapter's distinctive move is that each control is validated by a
  deliberate violation and the whole chain is proven by tracing one action
  from login to API call. Rejected a tool-by-tool structure — the record
  commits to capabilities; the PEH stack is the worked example.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 03 _
    Platform Creation.pdf` — the chapter checklist; despite the filename, its
    title page reads "End-to-End Kubernetes Platform Security". Reproduced,
    adapted, in the Checklist tab (`checklist.md`), including the final
    security review.
- **External**
  - *Platform Engineer's Handbook* — the End-to-End Kubernetes Platform
    Security chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md), including a
  spec-side fix: success criterion 1's chain enumeration aligned to the
  six-link framing used by every modality. *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared
  VERA/KAI cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
