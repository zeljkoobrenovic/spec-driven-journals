---
id: "CRE-482-771"
title: "Check boundaries against integer overflow weaknesses"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-482-771
excerpt: "CRE 482-771 · in Technical application security controls › Input and output protection › Memory, String, and Unmanaged Code · 5 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, ZAP Rule
---
> **CRE**: [482-771](https://opencre.org/cre/482-771)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-866-553]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.4.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v54-memory-string-and-unmanaged-code) | Verify that sign, range, and input validation techniques are used to prevent integer overflows. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [92](https://capec.mitre.org/data/definitions/92.html) | Forced Integer Overflow | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [190](https://cwe.mitre.org/data/definitions/190.html) | Integer Overflow or Wraparound | curated |
| [680](https://cwe.mitre.org/data/definitions/680.html) | Integer Overflow to Buffer Overflow | automatic |

More: [[standard-cwe]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [30003](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/IntegerOverflowScanRule.java) | Integer Overflow Error | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [482-771](https://opencre.org/cre/482-771). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
