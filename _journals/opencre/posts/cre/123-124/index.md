---
id: "CRE-123-124"
title: "Minimize permissions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-123-124
excerpt: "CRE 123-124 · in Technical application security controls › Technical application access control · 6 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [123-124](https://opencre.org/cre/123-124)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n724770["Technical application access control"] --> n123124["Minimize permissions"]
  n123124 --> n817808["Deny new users by default"]
  n123124 --> n368633["Enforce least privilege"]
  n123124 --> n540566["Let application request minimal permissions"]
  n123124 --> n152725["Limit access to admin/management functionality"]
  n123124 --> n524603["Limit modification of access controls to spec…"]
  n123124 --> n330281["Use least privilege OS accounts for system (c…"]
  style n123124 stroke-width:3px
---end mermaid---

## Contains

- [[cre-817-808]]
- [[cre-368-633]]
- [[cre-540-566]]
- [[cre-152-725]]
- [[cre-524-603]]
- [[cre-330-281]]

## Related CREs

- [[cre-586-842]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AC-6 LEAST PRIVILEGE](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AC-6) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [123-124](https://opencre.org/cre/123-124). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
