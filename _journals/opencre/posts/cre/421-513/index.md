---
id: "CRE-421-513"
title: "Ignore/at least validate filenames from untrusted origin (against RFD)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-421-513
excerpt: "CRE 421-513 · in Technical application security controls › Input and output protection › File handling › File execution · 2 mappings to 2 standards and tools."
tags: ASVS, CWE
---
> **CRE**: [421-513](https://opencre.org/cre/421-513)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-451-082]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.3.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v123-file-execution) | Verify that the application protects against Reflective File Download (RFD) by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter, the response Content-Type header should be set to text/plain, and the Content-Disposition header should have a fixed filename. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [641](https://cwe.mitre.org/data/definitions/641.html) | Improper Restriction of Names for Files and Other Resources | curated |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [421-513](https://opencre.org/cre/421-513). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
