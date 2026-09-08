---
timetoread: "2 min read"
---

When a platform team in my organization creates a platform, the finished build has one defining property: **the platform exists in Git, not in the clusters**. The test I keep running: if the clusters vanished tonight, could the pipeline rebuild every environment from a tagged commit by morning?

**What changes**

* **Environments become declarative stacks.** A platform sandbox, an application dev, and an application prod — each with its own configuration file, unique cluster name, pinned runtime versions, and a planned network with non-overlapping CIDR ranges checked against VPN and host networks. Non-production runs smaller; security and governance settings stay identical everywhere.
* **Provisioning and runtime configuration split into two repositories.** Infrastructure-as-code builds the clusters; a GitOps controller continuously reconciles everything that runs on them. Application manifests never live in the IaC layer; manual drift is corrected visibly; new team repositories and platform services onboard declaratively, versions pinned.
* **One pipeline promotes every change.** Lint, tests, preview, deploy, validate — plus security scanning on every commit; sandbox from main, production releases from Git tags, validation after every environment, and a manual approval recorded in the CI/CD system before production. Approval gates exist only where they provide real governance value.
* **Service traffic runs through a mesh from day one.** Controlled gateway ingress, declared routing, verified mTLS, isolation policies where needed — with proxy overhead measured honestly and telemetry hooks confirmed for the observability build to come.
* **Misconfiguration dies in the pipeline.** Policy-as-code blocks floating `latest` tags, wildcard chart versions, and unpinned deployments before manifests reach the GitOps repository; the policies themselves are tested for allowed and rejected cases.

**What it costs**

* Two repositories and a reconciler mean more moving parts than one repo and a deploy script — the coordination is the price of matching each kind of change to its own rails.
* The mesh taxes every request; the record requires measuring that overhead rather than assuming it away.
* Pinning everything makes upgrades deliberate work — nothing moves until a human moves a version, which is precisely the point.

**What we are not doing**

* Not mandating the reference stack — Pulumi, Kind, CircleCI, Flux, Istio, and OPA are the worked example; every commitment holds at the level of the capability.
* Not the full security, observability, or policy story — hardening is [[platform-security]], the telemetry build is [[observability-implementation]], and in-cluster admission enforcement is [[policy-as-code]].
* Not CI/CD for application teams — that product is [[cicd-as-a-platform-service]]; this pipeline builds the platform itself.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all seventeen build stages and the definition of done. Grounded in the Platform Creation chapter of the* Platform Engineer's Handbook*.*
