---
id: "CRE-613-286"
title: "Dependency management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-613-286
excerpt: "CRE 613-286 · in Development processes for security › Supply chain management · 3 sub-requirements · 17 mappings to 4 standards and tools."
tags: DevSecOps Maturity Model (DSOMM), NIST SSDF, OWASP Top 10 2021, SAMM
---
> **CRE**: [613-286](https://opencre.org/cre/613-286)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]]
>
> **Maps to**: [[standard-devsecops-maturity-model-dsomm]], [[standard-nist-ssdf]], [[standard-owasp-top-10-2021]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n613285["Supply chain management"] --> n613286["Dependency management"]
  n613286 --> n053751["Force build pipeline to check outdated/insecu…"]
  n613286 --> n863521["Maintain/manage inventory of third party comp…"]
  n613286 --> n715334["Update third party components build- or compi…"]
  style n613286 stroke-width:3px
---end mermaid---

## Contains

- [[cre-053-751]]
- [[cre-863-521]]
- [[cre-715-334]]

## Related CREs

- [[cre-007-274]]
- [[cre-732-148]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [2a44b708-734f-4463-b0cb-86dc46344b2f](https://dsomm.owasp.org/activity-description?uuid=2a44b708-734f-4463-b0cb-86dc46344b2f) | Deployment: Inventory of production components | automatic |
| [6c05c837-8c99-46e2-828b-7c903e27dba4](https://dsomm.owasp.org/activity-description?uuid=6c05c837-8c99-46e2-828b-7c903e27dba4) | Static depth for applications: Static analysis for important server side components | automatic |
| [07fe8c4f-ae33-4409-b1b2-cf64cfccea86](https://dsomm.owasp.org/activity-description?uuid=07fe8c4f-ae33-4409-b1b2-cf64cfccea86) | Static depth for applications: Software Composition Analysis (client side) | automatic |
| [8f2b4d5a-3c1e-4b7a-9d8f-2e6c4a1b5d7f](https://dsomm.owasp.org/activity-description?uuid=8f2b4d5a-3c1e-4b7a-9d8f-2e6c4a1b5d7f) | Consolidation: Artifact-based false positive treatment | automatic |
| [9e3a7c2f-1b4d-4e8a-a5c6-7f2b9d1e3a8c](https://dsomm.owasp.org/activity-description?uuid=9e3a7c2f-1b4d-4e8a-a5c6-7f2b9d1e3a8c) | Consolidation: Global false positive treatment | automatic |
| [13e9757e-58e2-4277-bc0f-eadc674891e6](https://dsomm.owasp.org/activity-description?uuid=13e9757e-58e2-4277-bc0f-eadc674891e6) | Deployment: Inventory of production dependencies | automatic |
| [2858ac12-0179-40d9-9acf-1b839c030473](https://dsomm.owasp.org/activity-description?uuid=2858ac12-0179-40d9-9acf-1b839c030473) | Build: SBOM of components | automatic |
| [83057028-0b77-4d2e-8135-40969768ae88](https://dsomm.owasp.org/activity-description?uuid=83057028-0b77-4d2e-8135-40969768ae88) | Deployment: Inventory of production artifacts | automatic |
| [c922981b-65ed-40f3-a947-96fee9a0125f](https://dsomm.owasp.org/activity-description?uuid=c922981b-65ed-40f3-a947-96fee9a0125f) | Test KPI: Generation of response statistics | automatic |
| [d918cd44-a972-43e9-a974-eff3f4a5dcfe](https://dsomm.owasp.org/activity-description?uuid=d918cd44-a972-43e9-a974-eff3f4a5dcfe) | Static depth for applications: Software Composition Analysis (server side) | automatic |
| [ee68331f-9b1d-4f61-844b-b2ea04753a84](https://dsomm.owasp.org/activity-description?uuid=ee68331f-9b1d-4f61-844b-b2ea04753a84) | Static depth for applications: Static analysis for all self written components | automatic |
| [f2f0f274-c1a0-4501-92fe-7fc4452bc8ad](https://dsomm.owasp.org/activity-description?uuid=f2f0f274-c1a0-4501-92fe-7fc4452bc8ad) | Static depth for applications: Exploit likelihood estimation | automatic |
| [f3c4971e-9f4d-4e59-8ed0-f0bdb6262477](https://dsomm.owasp.org/activity-description?uuid=f3c4971e-9f4d-4e59-8ed0-f0bdb6262477) | Build: Pinning of artifacts | automatic |
| [f4ff841d-3b2a-45d9-853e-5ec7ecbcb054](https://dsomm.owasp.org/activity-description?uuid=f4ff841d-3b2a-45d9-853e-5ec7ecbcb054) | Static depth for applications: Static analysis for all components/libraries | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| RV.1.1 | Gather information from software acquirers, users, and public sources on potential vulnerabilities in the software and third-party components that the software uses, and investigate all credible reports. | curated |

More: [[standard-nist-ssdf]]

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A06](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) | Vulnerable and Outdated Components | curated |

More: [[standard-owasp-top-10-2021]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [I-SB-B](https://owaspsamm.org/model/implementation/secure-build/stream-b) | Software Dependencies | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [613-286](https://opencre.org/cre/613-286). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
