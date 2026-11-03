---
id: "CRE-473-177"
title: "Deploy/build"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-473-177
excerpt: "CRE 473-177 · in Development processes for security · 9 sub-requirements · 16 mappings to 4 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), NIST 800-53 v5, SAMM
---
> **CRE**: [473-177](https://opencre.org/cre/473-177)
>
> **Part of**: [[cre-616-305]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-nist-800-53-v5]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n616305["Development processes for security"] --> n473177["Deploy/build"]
  n473177 --> n307507["Allow only trusted sources both build time an…"]
  n473177 --> n263184["Automate secure build and deployment, especia…"]
  n473177 --> n171222["Check binary integrity before deployment"]
  n473177 --> n208355["Ensure repeatability of deployment"]
  n473177 --> n028254["Secure auto-updates over full stack"]
  n473177 --> n461680["Securely archive builds and build information"]
  n473177 --> n253452["Securely automate build and deployment in pip…"]
  n473177 --> n347352["Set and confirm integrity of security deploym…"]
  n473177 --> n314131["Use features in compile and build tools for e…"]
  style n473177 stroke-width:3px
---end mermaid---

## Contains

- [[cre-307-507]]
- [[cre-263-184]]
- [[cre-171-222]]
- [[cre-208-355]]
- [[cre-028-254]]
- [[cre-461-680]]
- [[cre-253-452]]
- [[cre-347-352]]
- [[cre-314-131]]

## Related CREs

- [[cre-233-748]]
- [[cre-053-751]]
- [[cre-862-452]]
- [[cre-223-780]]
- [[cre-715-334]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| AIS-06 | Automated Secure Application Deployment | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0cb2626b-fb0d-4a0f-9688-57f787310d97](https://dsomm.owasp.org/activity-description?uuid=0cb2626b-fb0d-4a0f-9688-57f787310d97) | Deployment: Blue/Green Deployment | automatic |
| [9f107927-61e9-4574-85ad-3f2b4bca8665](https://dsomm.owasp.org/activity-description?uuid=9f107927-61e9-4574-85ad-3f2b4bca8665) | Build: Signing of code | automatic |
| [67e1a9aa-9fbf-4ec5-a2de-400f01960c51](https://dsomm.owasp.org/activity-description?uuid=67e1a9aa-9fbf-4ec5-a2de-400f01960c51) | Deployment: Automated deployment process | automatic |
| [85d52588-f542-4225-a338-20dc22a5508d](https://dsomm.owasp.org/activity-description?uuid=85d52588-f542-4225-a338-20dc22a5508d) | Deployment: Rolling update on deployment | automatic |
| [066084c6-1135-4635-9cc5-9e75c7c5459f](https://dsomm.owasp.org/activity-description?uuid=066084c6-1135-4635-9cc5-9e75c7c5459f) | Development and Source Control: Version control | automatic |
| [74938a3f-1269-49b9-9d0f-c43a79a1985a](https://dsomm.owasp.org/activity-description?uuid=74938a3f-1269-49b9-9d0f-c43a79a1985a) | Deployment: Defined deployment process | automatic |
| [598897a2-358e-441f-984c-e12ec4f6110a](https://dsomm.owasp.org/activity-description?uuid=598897a2-358e-441f-984c-e12ec4f6110a) | Test Intensity: Regular automated tests | automatic |
| [5786959d-0c6f-46a6-8e1c-a32ff1a50222](https://dsomm.owasp.org/activity-description?uuid=5786959d-0c6f-46a6-8e1c-a32ff1a50222) | Build: Signing of artifacts | automatic |
| [a340f46b-6360-4cb8-847b-a0d3483d09d3](https://dsomm.owasp.org/activity-description?uuid=a340f46b-6360-4cb8-847b-a0d3483d09d3) | Build: Building and testing of artifacts in virtual environments | automatic |
| [a854b48d-83bd-4f8d-8621-a0bdd470837f](https://dsomm.owasp.org/activity-description?uuid=a854b48d-83bd-4f8d-8621-a0bdd470837f) | Deployment: Same artifact for environments | automatic |
| [a511799b-045e-4b96-9843-7d63d8c1e2ad](https://dsomm.owasp.org/activity-description?uuid=a511799b-045e-4b96-9843-7d63d8c1e2ad) | Deployment: Usage of feature toggles | automatic |
| [f6f7737f-25a9-4317-8de2-09bf59f29b5b](https://dsomm.owasp.org/activity-description?uuid=f6f7737f-25a9-4317-8de2-09bf59f29b5b) | Build: Defined build process | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-34 Non-modifiable Executable Programs](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-34) | curated |

More: [[standard-nist-800-53-v5]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [I-SB-A](https://owaspsamm.org/model/implementation/secure-build/stream-a) | Build Process | curated |
| [I-SD-A](https://owaspsamm.org/model/implementation/secure-deployment/stream-a) | Deployment Process | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [473-177](https://opencre.org/cre/473-177). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
