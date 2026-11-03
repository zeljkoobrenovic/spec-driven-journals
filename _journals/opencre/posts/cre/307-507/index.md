---
id: "CRE-307-507"
title: "Allow only trusted sources both build time and runtime; therefore perform integrity checks on all resources and code"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-307-507
excerpt: "CRE 307-507 · in Development processes for security › Deploy/build · 11 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST SSDF, OWASP Cheat Sheets
---
> **CRE**: [307-507](https://opencre.org/cre/307-507)
>
> **Part of**: [[cre-616-305]] › [[cre-473-177]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-ssdf]], [[standard-owasp-cheat-sheets]]

## Related CREs

- [[cre-613-285]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.3.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v103-application-integrity) | Verify that the application employs integrity protections, such as code signing or subresource integrity. The application must not load or execute code from untrusted sources, such as loading includes, modules, plugins, code, or libraries from untrusted sources or the Internet. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [14](https://capec.mitre.org/data/definitions/14.html) | Client-side Injection-induced Buffer Overflow | automatic |
| [39](https://capec.mitre.org/data/definitions/39.html) | Manipulating Opaque Client-based Data Tokens | automatic |
| [74](https://capec.mitre.org/data/definitions/74.html) | Manipulating State | automatic |
| [75](https://capec.mitre.org/data/definitions/75.html) | Manipulating Writeable Configuration Files | automatic |
| [389](https://capec.mitre.org/data/definitions/389.html) | Content Spoofing Via Application API Manipulation | automatic |
| [665](https://capec.mitre.org/data/definitions/665.html) | Exploitation of Thunderbolt Protection Flaws | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [353](https://cwe.mitre.org/data/definitions/353.html) | Missing Support for Integrity Check | curated |

More: [[standard-cwe]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PS.2.1 | Make software integrity verification information available to software acquirers. | curated |

More: [[standard-nist-ssdf]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [307-507](https://opencre.org/cre/307-507). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
