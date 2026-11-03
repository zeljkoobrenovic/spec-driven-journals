---
id: "CRE-836-068"
title: "Deserialization Prevention"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-836-068
excerpt: "CRE 836-068 · in Technical application security controls › Input and output protection · 4 sub-requirements · 1 mapping to 1 standard and tool."
tags: OWASP Top 10 2021
---
> **CRE**: [836-068](https://opencre.org/cre/836-068)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]]
>
> **Maps to**: [[standard-owasp-top-10-2021]]

## Where It Sits

---begin mermaid---
graph LR
  n503455["Input and output protection"] --> n836068["Deserialization Prevention"]
  n836068 --> n831563["Avoid deserialization logic"]
  n836068 --> n736554["Block serialization of content from untrusted…"]
  n836068 --> n387848["Parse JSON safely"]
  n836068 --> n762616["Secure serialized objects (e.g. integrity che…"]
  style n836068 stroke-width:3px
---end mermaid---

## Contains

- [[cre-831-563]]
- [[cre-736-554]]
- [[cre-387-848]]
- [[cre-762-616]]

## Related CREs

- [[cre-184-284]]
- [[cre-515-021]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A08](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/) | Software and Data Integrity Failures | curated |

More: [[standard-owasp-top-10-2021]]

## Source

Generated from the OpenCRE catalogue entry [836-068](https://opencre.org/cre/836-068). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
