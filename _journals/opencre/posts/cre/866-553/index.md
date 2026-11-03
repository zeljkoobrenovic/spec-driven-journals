---
id: "CRE-866-553"
title: "Memory, String, and Unmanaged Code"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-866-553
excerpt: "CRE 866-553 · in Technical application security controls › Input and output protection · 3 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [866-553](https://opencre.org/cre/866-553)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n503455["Input and output protection"] --> n866553["Memory, String, and Unmanaged Code"]
  n866553 --> n482771["Check boundaries against integer overflow wea…"]
  n866553 --> n824732["Force format strings as constants"]
  n866553 --> n831570["Use memory-safe functions exclusively"]
  style n866553 stroke-width:3px
---end mermaid---

## Contains

- [[cre-482-771]]
- [[cre-824-732]]
- [[cre-831-570]]

## Related CREs

- [[cre-760-764]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-16 Memory Protection](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-16) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [866-553](https://opencre.org/cre/866-553). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
