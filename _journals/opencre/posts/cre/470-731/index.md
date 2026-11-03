---
id: "CRE-470-731"
title: "Minimize session life"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-470-731
excerpt: "CRE 470-731 · in Technical application security controls › Session management · 4 sub-requirements · 3 mappings to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [470-731](https://opencre.org/cre/470-731)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n177260["Session management"] --> n470731["Minimize session life"]
  n470731 --> n673736["Enable option to log out from all active session"]
  n470731 --> n065782["Ensure session timeout (soft/hard)"]
  n470731 --> n238346["Terminate all sessions when password is changed"]
  n470731 --> n457165["Terminate session after logout"]
  style n470731 stroke-width:3px
---end mermaid---

## Contains

- [[cre-673-736]]
- [[cre-065-782]]
- [[cre-238-346]]
- [[cre-457-165]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AC-11 DEVICE LOCK](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AC-11) | curated |
|  | [AC-12 SESSION TERMINATION](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AC-12) | curated |
|  | [SC-10 NETWORK DISCONNECT](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-10) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [470-731](https://opencre.org/cre/470-731). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
