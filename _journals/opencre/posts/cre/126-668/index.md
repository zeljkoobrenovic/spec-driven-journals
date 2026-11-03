---
id: "CRE-126-668"
title: "Secure data storage"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-126-668
excerpt: "CRE 126-668 · in Technical application security controls · 5 sub-requirements · 2 mappings to 2 standards and tools."
tags: OWASP Top 10 2021, PCI DSS
---
> **CRE**: [126-668](https://opencre.org/cre/126-668)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-owasp-top-10-2021]], [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n126668["Secure data storage"]
  n126668 --> n538770["Data access control"]
  n126668 --> n400007["Encrypt data at rest"]
  n126668 --> n208830["Manage temporary storage"]
  n126668 --> n223780["Secret storage"]
  n126668 --> n542270["Secure random values"]
  style n126668 stroke-width:3px
---end mermaid---

## Contains

- [[cre-538-770]] — 1 more below
- [[cre-400-007]] — 15 more below
- [[cre-208-830]] — 6 more below
- [[cre-223-780]] — 12 more below
- [[cre-542-270]] — 3 more below

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A04](https://owasp.org/Top10/A04_2021-Insecure_Design/) | Insecure Design | curated |

More: [[standard-owasp-top-10-2021]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 9.4 | Media with cardholder data is securely stored, accessed, distributed, and destroyed. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [126-668](https://opencre.org/cre/126-668). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
