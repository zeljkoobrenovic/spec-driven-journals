---
id: "CRE-177-260"
title: "Session management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-177-260
excerpt: "CRE 177-260 · in Technical application security controls · 7 sub-requirements · 5 mappings to 2 standards and tools."
tags: NIST 800-53 v5, OWASP Top 10 2021
---
> **CRE**: [177-260](https://opencre.org/cre/177-260)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-nist-800-53-v5]], [[standard-owasp-top-10-2021]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n177260["Session management"]
  n177260 --> n110531["Cookie-config"]
  n177260 --> n402133["Do not expose session token in URL"]
  n177260 --> n470731["Minimize session life"]
  n177260 --> n582541["Re-authenticate before sensitive transactions"]
  n177260 --> n258115["Re-authentication from federation or assertion"]
  n177260 --> n114277["Session integrity"]
  n177260 --> n716526["Session token generation"]
  style n177260 stroke-width:3px
---end mermaid---

## Contains

- [[cre-110-531]] — 5 more below
- [[cre-402-133]]
- [[cre-470-731]] — 4 more below
- [[cre-582-541]]
- [[cre-258-115]] — 3 more below
- [[cre-114-277]] — 2 more below
- [[cre-716-526]] — 4 more below

## Related CREs

- [[cre-270-568]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AC-10 CONCURRENT SESSION CONTROL](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AC-10) | curated |
|  | [IA-11 RE-AUTHENTICATION](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=IA-11) | curated |
|  | [SC-23 SESSION AUTHENTICITY](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-23) | curated |

More: [[standard-nist-800-53-v5]]

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) | Broken Access Controls | curated |
| [A07](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) | Identification and Authentication Failures | curated |

More: [[standard-owasp-top-10-2021]]

## Source

Generated from the OpenCRE catalogue entry [177-260](https://opencre.org/cre/177-260). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
