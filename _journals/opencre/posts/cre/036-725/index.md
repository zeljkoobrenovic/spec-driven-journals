---
id: "CRE-036-725"
title: "Set content HTTP response type"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-036-725
excerpt: "CRE 036-725 · in Technical application security controls › Configuration hardening › HTTP security headers · 15 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [036-725](https://opencre.org/cre/036-725)
>
> **Part of**: [[cre-636-660]] › [[cre-233-748]] › [[cre-636-347]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.4.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v144-http-security-headers) | Verify that every HTTP response contains a Content-Type header. Also specify a safe character set (e.g., UTF-8, ISO-8859-1) if the content types are text/*, /+xml and application/xml. Content must match with the provided Content-Type header. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [3](https://capec.mitre.org/data/definitions/3.html) | Using Leading 'Ghost' Character Sequences to Bypass Input Filters | automatic |
| [4](https://capec.mitre.org/data/definitions/4.html) | Using Alternative IP Address Encodings | automatic |
| [52](https://capec.mitre.org/data/definitions/52.html) | Embedding NULL Bytes | automatic |
| [53](https://capec.mitre.org/data/definitions/53.html) | Postfix, Null Terminate, and Backslash | automatic |
| [64](https://capec.mitre.org/data/definitions/64.html) | Using Slashes and URL Encoding Combined to Bypass Validation Logic | automatic |
| [71](https://capec.mitre.org/data/definitions/71.html) | Using Unicode Encoding to Bypass Validation Logic | automatic |
| [72](https://capec.mitre.org/data/definitions/72.html) | URL Encoding | automatic |
| [78](https://capec.mitre.org/data/definitions/78.html) | Using Escaped Slashes in Alternate Encoding | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [80](https://capec.mitre.org/data/definitions/80.html) | Using UTF-8 Encoding to Bypass Validation Logic | automatic |
| [120](https://capec.mitre.org/data/definitions/120.html) | Double Encoding | automatic |
| [267](https://capec.mitre.org/data/definitions/267.html) | Leverage Alternate Encoding | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [173](https://cwe.mitre.org/data/definitions/173.html) | Improper Handling of Alternate Encoding | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [036-725](https://opencre.org/cre/036-725). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
