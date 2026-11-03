---
id: "CRE-824-732"
title: "Force format strings as constants"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-824-732
excerpt: "CRE 824-732 · in Technical application security controls › Input and output protection › Memory, String, and Unmanaged Code · 5 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, ZAP Rule
---
> **CRE**: [824-732](https://opencre.org/cre/824-732)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-866-553]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.4.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v54-memory-string-and-unmanaged-code) | Verify that format strings do not take potentially hostile input, and are constant. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [67](https://capec.mitre.org/data/definitions/67.html) | String Format Overflow in syslog() | automatic |
| [135](https://capec.mitre.org/data/definitions/135.html) | Format String Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [134](https://cwe.mitre.org/data/definitions/134.html) | Use of Externally-Controlled Format String | curated |

More: [[standard-cwe]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [30002](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/FormatStringScanRule.java) | Format String Error | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [824-732](https://opencre.org/cre/824-732). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
