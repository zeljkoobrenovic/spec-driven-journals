---
id: "CRE-314-131"
title: "Use features in compile and build tools for executable security"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-314-131
excerpt: "CRE 314-131 · in Development processes for security › Deploy/build · 20 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, NIST SSDF, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [314-131](https://opencre.org/cre/314-131)
>
> **Part of**: [[cre-616-305]] › [[cre-473-177]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-ssdf]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v141-build-and-deploy) | Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [8](https://capec.mitre.org/data/definitions/8.html) | Buffer Overflow in an API Call | automatic |
| [9](https://capec.mitre.org/data/definitions/9.html) | Buffer Overflow in Local Command-Line Utilities | automatic |
| [10](https://capec.mitre.org/data/definitions/10.html) | Buffer Overflow via Environment Variables | automatic |
| [14](https://capec.mitre.org/data/definitions/14.html) | Client-side Injection-induced Buffer Overflow | automatic |
| [24](https://capec.mitre.org/data/definitions/24.html) | Filter Failure through Buffer Overflow | automatic |
| [42](https://capec.mitre.org/data/definitions/42.html) | MIME Conversion | automatic |
| [44](https://capec.mitre.org/data/definitions/44.html) | Overflow Binary Resource File | automatic |
| [45](https://capec.mitre.org/data/definitions/45.html) | Buffer Overflow via Symbolic Links | automatic |
| [46](https://capec.mitre.org/data/definitions/46.html) | Overflow Variables and Tags | automatic |
| [47](https://capec.mitre.org/data/definitions/47.html) | Buffer Overflow via Parameter Expansion | automatic |
| [67](https://capec.mitre.org/data/definitions/67.html) | String Format Overflow in syslog() | automatic |
| [92](https://capec.mitre.org/data/definitions/92.html) | Forced Integer Overflow | automatic |
| [100](https://capec.mitre.org/data/definitions/100.html) | Overflow Buffers | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [120](https://cwe.mitre.org/data/definitions/120.html) | Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') | curated |
| [785](https://cwe.mitre.org/data/definitions/785.html) | Use of Path Manipulation Function without Maximum-sized Buffer | automatic |

More: [[standard-cwe]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PW.6.1 | Use compiler, interpreter, and build tools that offer features to improve executable security. | curated |
| PW.6.2 | Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved configurations. | curated |

More: [[standard-nist-ssdf]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [30001](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/BufferOverflowScanRule.java) | Buffer Overflow | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [314-131](https://opencre.org/cre/314-131). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
