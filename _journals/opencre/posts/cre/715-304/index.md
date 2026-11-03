---
id: "CRE-715-304"
title: "Zeroize sensitive information in memory after use"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-715-304
excerpt: "CRE 715-304 · in Technical application security controls › Secure data storage › Manage temporary storage · 9 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [715-304](https://opencre.org/cre/715-304)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-208-830]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.3.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v83-sensitive-private-data) | Verify that sensitive information contained in memory is overwritten as soon as it is no longer required to mitigate memory dumping attacks, using zeroes or random data. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [37](https://capec.mitre.org/data/definitions/37.html) | Retrieve Embedded Sensitive Data | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [226](https://cwe.mitre.org/data/definitions/226.html) | Sensitive Information in Resource Not Removed Before Reuse | curated |
| [244](https://cwe.mitre.org/data/definitions/244.html) | Improper Clearing of Heap Memory Before Release ('Heap Inspection') | automatic |
| [1239](https://cwe.mitre.org/data/definitions/1239.html) | Improper Zeroization of Hardware Register | automatic |
| [1272](https://cwe.mitre.org/data/definitions/1272.html) | Sensitive Information Uncleared Before Debug/Power State Transition | automatic |
| [1301](https://cwe.mitre.org/data/definitions/1301.html) | Insufficient or Incomplete Data Removal within Hardware Component | automatic |
| [1330](https://cwe.mitre.org/data/definitions/1330.html) | Remanent Data Readable after Memory Erase | automatic |
| [1342](https://cwe.mitre.org/data/definitions/1342.html) | Information Exposure through Microarchitectural State after Transient Execution | automatic |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [715-304](https://opencre.org/cre/715-304). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
