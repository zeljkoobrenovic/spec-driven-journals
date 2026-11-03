---
id: "CRE-463-820"
title: "Limit size and number of uploaded files"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-463-820
excerpt: "CRE 463-820 · in Technical application security controls › Input and output protection › File handling › File upload · 26 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [463-820](https://opencre.org/cre/463-820)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-621-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Related CREs

- [[cre-623-550]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v121-file-upload) | Verify that a file size quota and maximum number of files per user is enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files. | curated |

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
|  | [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [463-820](https://opencre.org/cre/463-820). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
