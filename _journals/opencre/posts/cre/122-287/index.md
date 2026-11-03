---
id: "CRE-122-287"
title: "Ensure cryptographic elements can be upgraded or replaced"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-122-287
excerpt: "CRE 122-287 · in Technical application security controls › Secure data storage › Encrypt data at rest › Encryption algorithms · 13 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [122-287](https://opencre.org/cre/122-287)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]] › [[cre-742-432]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V6.2.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x14-V6-Cryptography.md#v62-algorithms) | Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. ((C8)(https://owasp.org/www-project-proactive-controls/#div-numbering)) | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [192](https://capec.mitre.org/data/definitions/192.html) | Protocol Analysis | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [326](https://cwe.mitre.org/data/definitions/326.html) | Inadequate Encryption Strength | curated |
| [328](https://cwe.mitre.org/data/definitions/328.html) | Use of Weak Hash | automatic |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | curated |
|  | [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C8](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c8-protect-data-everywhere.html) | curated |

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10105-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java) | Weak Authentication Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [122-287](https://opencre.org/cre/122-287). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
