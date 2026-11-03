---
id: "CRE-161-451"
title: "Output encoding and injection prevention"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-161-451
excerpt: "CRE 161-451 · in Technical application security controls › Input and output protection · 11 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [161-451](https://opencre.org/cre/161-451)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n503455["Input and output protection"] --> n161451["Output encoding and injection prevention"]
  n161451 --> n064808["Encode output context-specifically"]
  n161451 --> n806367["Encode output near the consuming interpreter"]
  n161451 --> n533516["Encode output while preserving user input for…"]
  n161451 --> n366835["Escape output against XSS"]
  n161451 --> n620101["Force output encoding for specific interprete…"]
  n161451 --> n732873["Lock/precompile queries (parameterization) to…"]
  n161451 --> n607671["Protect against JS or JSON injection attacks"]
  n161451 --> n531558["Protect against LDAP injection"]
  n161451 --> n547283["Protect against LFI / RFI"]
  n161451 --> n857718["Protect against OS command injection attack"]
  n161451 --> n134207["Protect against XML/XPath injection"]
  style n161451 stroke-width:3px
---end mermaid---

## Contains

- [[cre-064-808]]
- [[cre-806-367]]
- [[cre-533-516]]
- [[cre-366-835]]
- [[cre-620-101]]
- [[cre-732-873]]
- [[cre-607-671]]
- [[cre-531-558]]
- [[cre-547-283]]
- [[cre-857-718]]
- [[cre-134-207]]

## Related CREs

- [[cre-760-764]]
- [[cre-760-765]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-15 Information Output Filtering](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-15) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [161-451](https://opencre.org/cre/161-451). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
