---
id: "CRE-831-570"
title: "Use memory-safe functions exclusively"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-831-570
excerpt: "CRE 831-570 · in Technical application security controls › Input and output protection › Memory, String, and Unmanaged Code · 18 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [831-570](https://opencre.org/cre/831-570)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-866-553]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.4.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v54-memory-string-and-unmanaged-code) | Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows. | curated |

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

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-13](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/13-Testing_for_Buffer_Overflow.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [30001](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/BufferOverflowScanRule.java) | Buffer Overflow | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [831-570](https://opencre.org/cre/831-570). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
