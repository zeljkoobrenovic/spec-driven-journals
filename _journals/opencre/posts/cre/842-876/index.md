---
id: "CRE-842-876"
title: "Logging and error handling"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-842-876
excerpt: "CRE 842-876 · in Technical application security controls · 5 sub-requirements · 11 mappings to 3 standards and tools."
tags: DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5
---
> **CRE**: [842-876](https://opencre.org/cre/842-876)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n842876["Logging and error handling"]
  n842876 --> n513183["Error handling"]
  n842876 --> n141555["Fail securely"]
  n842876 --> n843841["Log discretely"]
  n842876 --> n148420["Log integrity"]
  n842876 --> n402706["Log relevant"]
  style n842876 stroke-width:3px
---end mermaid---

## Contains

- [[cre-513-183]] — 3 more below
- [[cre-141-555]]
- [[cre-843-841]] — 2 more below
- [[cre-148-420]] — 8 more below
- [[cre-402-706]] — 5 more below

## Related CREs

- [[cre-725-682]]
- [[cre-668-364]]
- [[cre-058-083]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [b4193d32-3948-47e2-a326-3748c48019a1](https://dsomm.owasp.org/activity-description?uuid=b4193d32-3948-47e2-a326-3748c48019a1) | Process: Definition of a change management process | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.15 | Logging | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AU-1 Policy and Procedures](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-1) | curated |
|  | [AU-4 Audit Log Storage Capacity](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-4) | curated |
|  | [AU-5 Response to Audit Logging Process Failures](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-5) | curated |
|  | [AU-6 Audit Record Review, Analysis, and Reporting](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-6) | curated |
|  | [AU-7 Audit Record Reduction and Report Generation](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-7) | curated |
|  | [AU-11 Audit Record Retention](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-11) | curated |
|  | [AU-12 Audit Record Generation](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-12) | curated |
|  | [AU-16 Cross-organizational Audit Logging](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-16) | curated |
|  | [SI-11 Error Handling](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-11) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [842-876](https://opencre.org/cre/842-876). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
