---
id: "CRE-208-830"
title: "Manage temporary storage"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-208-830
excerpt: "CRE 208-830 · in Technical application security controls › Secure data storage · 6 sub-requirements · 1 mapping to 1 standard and tool."
tags: NIST 800-53 v5
---
> **CRE**: [208-830](https://opencre.org/cre/208-830)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]]
>
> **Maps to**: [[standard-nist-800-53-v5]]

## Where It Sits

---begin mermaid---
graph LR
  n126668["Secure data storage"] --> n208830["Manage temporary storage"]
  n208830 --> n046257["Clear authentication data from client storage"]
  n208830 --> n617524["Do not store sensitive data on client (browse…"]
  n208830 --> n846302["Prevent caching of sensitive data in server c…"]
  n208830 --> n157430["Protect and clear cached sensitive data"]
  n208830 --> n473758["Set sufficient anti-caching headers"]
  n208830 --> n715304["Zeroize sensitive information in memory after…"]
  style n208830 stroke-width:3px
---end mermaid---

## Contains

- [[cre-046-257]]
- [[cre-617-524]]
- [[cre-846-302]]
- [[cre-157-430]]
- [[cre-473-758]]
- [[cre-715-304]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-4 Information in Shared System Resources](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-4) | curated |

More: [[standard-nist-800-53-v5]]

## Source

Generated from the OpenCRE catalogue entry [208-830](https://opencre.org/cre/208-830). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
