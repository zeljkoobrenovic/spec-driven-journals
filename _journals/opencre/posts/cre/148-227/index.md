---
id: "CRE-148-227"
title: "Endpoint management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-148-227
excerpt: "CRE 148-227 · in Operating processes for security › Facilities management · 3 sub-requirements · 12 mappings to 4 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5
---
> **CRE**: [148-227](https://opencre.org/cre/148-227)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n850376["Facilities management"] --> n148227["Endpoint management"]
  n148227 --> n286500["OS security"]
  n148227 --> n007274["Patching and updating system components"]
  n148227 --> n872574["Virus/malware protection"]
  style n148227 stroke-width:3px
---end mermaid---

## Contains

- [[cre-286-500]]
- [[cre-007-274]]
- [[cre-872-574]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| UEM | Universal Endpoint Management | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [dccf1949-b9a8-4ce8-b992-6a4a7f3a623a](https://dsomm.owasp.org/activity-description?uuid=dccf1949-b9a8-4ce8-b992-6a4a7f3a623a) | Dynamic depth for infrastructure: Test for unauthorized installation | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 6.7 | Remote working | curated |
| 8.1 | User end point devices | curated |
| 8.17 | Clock synchronization | curated |
| 8.19 | Installation of software on operational systems | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [PL-2 System Security and Privacy Plans](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=PL-2) | curated |
|  | [SC-25 Thin Nodes](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-25) | curated |
|  | [SC-45 System Time Synchronization](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-45) | curated |
|  | [SC-49 Hardware-enforced Separation and Policy Enforcement](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-49) | curated |
|  | [SC-51 Hardware-based Protection](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-51) | curated |
|  | [SI-8 Spam Protection](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-8) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [148-227](https://opencre.org/cre/148-227). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
