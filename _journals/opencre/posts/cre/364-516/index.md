---
id: "CRE-364-516"
title: "AI security assurance & validation"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-364-516
excerpt: "CRE 364-516 · in Development processes for security › Verification · 9 sub-requirements · 2 mappings to 2 standards and tools."
tags: ETSI, MITRE ATLAS
---
> **CRE**: [364-516](https://opencre.org/cre/364-516)
>
> **Part of**: [[cre-616-305]] › [[cre-433-442]]
>
> **Maps to**: [[standard-etsi]], [[standard-mitre-atlas]]

## Where It Sits

---begin mermaid---
graph LR
  n433442["Verification"] --> n364516["AI security assurance & validation"]
  n364516 --> n547824["AI model performance validation"]
  n364516 --> n555083["Testing against backdoor poisoning"]
  n364516 --> n536158["Testing against direct prompt injection"]
  n364516 --> n011322["Testing against evasion"]
  n364516 --> n483253["Testing against indirect prompt injection"]
  n364516 --> n011087["Testing against membership inference"]
  n364516 --> n532102["Testing against model inversion"]
  n364516 --> n663550["Testing against model theft by inference"]
  n364516 --> n043703["Testing against sensitive data extraction by…"]
  style n364516 stroke-width:3px
---end mermaid---

## Contains

- [[cre-547-824]]
- [[cre-555-083]]
- [[cre-536-158]]
- [[cre-011-322]]
- [[cre-483-253]]
- [[cre-011-087]]
- [[cre-532-102]]
- [[cre-663-550]]
- [[cre-043-703]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ETSI

| ID | Section | Link |
| --- | --- | --- |
| [6.2.2](https://www.etsi.org/deliver/etsi_gr/SAI/001_099/005/01.01.01_60/gr_SAI005v010101p.pdf) | Robustness evaluation | curated |

More: [[standard-etsi]]

### MITRE ATLAS

| ID | Section | Link |
| --- | --- | --- |
| [AML.M0008](https://atlas.mitre.org/mitigations/AML.M0008) | Validate AI model | curated |

More: [[standard-mitre-atlas]]

## Source

Generated from the OpenCRE catalogue entry [364-516](https://opencre.org/cre/364-516). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
