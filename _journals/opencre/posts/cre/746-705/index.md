---
id: "CRE-746-705"
title: "Limit/authorize user's access to functionality"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-746-705
excerpt: "CRE 746-705 · in Technical application security controls › Technical application access control › Strong authorization checking · 27 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [746-705](https://opencre.org/cre/746-705)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-128-128]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V11.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x19-V11-BusLogic.md#v111-business-logic-security) | Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [125](https://capec.mitre.org/data/definitions/125.html) | Flooding | automatic |
| [130](https://capec.mitre.org/data/definitions/130.html) | Excessive Allocation | automatic |
| [147](https://capec.mitre.org/data/definitions/147.html) | XML Ping of the Death | automatic |
| [197](https://capec.mitre.org/data/definitions/197.html) | Exponential Data Expansion | automatic |
| [229](https://capec.mitre.org/data/definitions/229.html) | Serialized Data Parameter Blowup | automatic |
| [230](https://capec.mitre.org/data/definitions/230.html) | Serialized Data with Nested Payloads | automatic |
| [231](https://capec.mitre.org/data/definitions/231.html) | Oversized Serialized Data Payloads | automatic |
| [469](https://capec.mitre.org/data/definitions/469.html) | HTTP DoS | automatic |
| [482](https://capec.mitre.org/data/definitions/482.html) | TCP Flood | automatic |
| [486](https://capec.mitre.org/data/definitions/486.html) | UDP Flood | automatic |
| [487](https://capec.mitre.org/data/definitions/487.html) | ICMP Flood | automatic |
| [488](https://capec.mitre.org/data/definitions/488.html) | HTTP Flood | automatic |
| [489](https://capec.mitre.org/data/definitions/489.html) | SSL Flood | automatic |
| [490](https://capec.mitre.org/data/definitions/490.html) | Amplification | automatic |
| [491](https://capec.mitre.org/data/definitions/491.html) | Quadratic Data Expansion | automatic |
| [493](https://capec.mitre.org/data/definitions/493.html) | SOAP Array Blowup | automatic |
| [494](https://capec.mitre.org/data/definitions/494.html) | TCP Fragmentation | automatic |
| [495](https://capec.mitre.org/data/definitions/495.html) | UDP Fragmentation | automatic |
| [496](https://capec.mitre.org/data/definitions/496.html) | ICMP Fragmentation | automatic |
| [528](https://capec.mitre.org/data/definitions/528.html) | XML Flood | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [770](https://cwe.mitre.org/data/definitions/770.html) | Allocation of Resources Without Limits or Throttling | curated |
| [774](https://cwe.mitre.org/data/definitions/774.html) | Allocation of File Descriptors or Handles Without Limits or Throttling | automatic |
| [789](https://cwe.mitre.org/data/definitions/789.html) | Memory Allocation with Excessive Size Value | automatic |
| [1325](https://cwe.mitre.org/data/definitions/1325.html) | Improperly Controlled Sequential Memory Allocation | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-$$](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/README.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [746-705](https://opencre.org/cre/746-705). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
