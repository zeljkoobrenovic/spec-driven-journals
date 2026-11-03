---
id: "CRE-384-344"
title: "Store and serve user-uploaded files such that they cannot execute/damage server or client"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-384-344
excerpt: "CRE 384-344 · in Technical application security controls › Input and output protection › File handling › File upload · 3 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [384-344](https://opencre.org/cre/384-344)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-621-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Related CREs

- [[cre-760-764]]
- [[cre-760-765]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.12.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v11-secure-software-development-lifecycle) | Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. Implement a suitable Content Security Policy (CSP) to reduce the risk from XSS vectors or other attacks from the uploaded file. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [209](https://capec.mitre.org/data/definitions/209.html) | XSS Using MIME Type Mismatch | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [646](https://cwe.mitre.org/data/definitions/646.html) | Reliance on File Name or Extension of Externally-Supplied File | curated |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [384-344](https://opencre.org/cre/384-344). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
