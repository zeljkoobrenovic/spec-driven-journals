---
id: "CRE-128-128"
title: "Strong authorization checking"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-128-128
excerpt: "CRE 128-128 · in Technical application security controls › Technical application access control · 12 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [128-128](https://opencre.org/cre/128-128)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n724770["Technical application access control"] --> n128128["Strong authorization checking"]
  n128128 --> n822100["Constrain functional features based on user s…"]
  n128128 --> n640364["Enforce access control on trusted parts/serve…"]
  n128128 --> n650560["Enforce access control on trusted service layer"]
  n128128 --> n284521["Enforce additional authorization and segregat…"]
  n128128 --> n664080["Enforce model-based authorization both at URI…"]
  n128128 --> n166151["Ensure that secure fail-safe is in place for…"]
  n128128 --> n746705["Limit/authorize user's access to functionality"]
  n128128 --> n615744["Protect against directory browsing/discovery…"]
  n128128 --> n304667["Protect API against unauthorized access/modif…"]
  n128128 --> n801310["Use ABAC/FBAC on data/feature level, even whe…"]
  n128128 --> n060472["Use CSRF protection against authenticated fun…"]
  n128128 --> n201246["Use multifactor authentication on administrat…"]
  style n128128 stroke-width:3px
---end mermaid---

## Contains

- [[cre-822-100]]
- [[cre-640-364]]
- [[cre-650-560]]
- [[cre-284-521]]
- [[cre-664-080]]
- [[cre-166-151]]
- [[cre-746-705]]
- [[cre-615-744]]
- [[cre-304-667]]
- [[cre-801-310]]
- [[cre-060-472]]
- [[cre-201-246]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AC-3 ACCESS ENFORCEMENT](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AC-3) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [128-128](https://opencre.org/cre/128-128). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
