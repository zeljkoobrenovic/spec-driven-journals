---
id: "CRE-503-455"
title: "Input and output protection"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-503-455
excerpt: "CRE 503-455 · in Technical application security controls · 10 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [503-455](https://opencre.org/cre/503-455)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n503455["Input and output protection"]
  n503455 --> n118110["API/web services"]
  n503455 --> n836068["Deserialization Prevention"]
  n503455 --> n130550["File handling"]
  n503455 --> n010308["Input validation"]
  n503455 --> n866553["Memory, String, and Unmanaged Code"]
  n503455 --> n161451["Output encoding and injection prevention"]
  n503455 --> n308515["Prevent security disclosure"]
  n503455 --> n764507["Restrict XML parsing (against XXE)"]
  n503455 --> n764765["Sanitization and sandboxing"]
  n503455 --> n541441["Validate HTTP request headers"]
  style n503455 stroke-width:3px
---end mermaid---

## Contains

- [[cre-118-110]] — 11 more below
- [[cre-836-068]] — 4 more below
- [[cre-130-550]] — 19 more below
- [[cre-010-308]] — 8 more below
- [[cre-866-553]] — 3 more below
- [[cre-161-451]] — 11 more below
- [[cre-308-515]] — 2 more below
- [[cre-764-507]]
- [[cre-764-765]] — 9 more below
- [[cre-541-441]] — 4 more below

## Related CREs

- [[cre-782-234]]
- [[cre-048-612]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-10 INFORMATION INPUT VALIDATION](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-10) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [503-455](https://opencre.org/cre/503-455). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
