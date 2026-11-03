---
id: "CRE-433-122"
title: "Use nonces and initialization vectors only once"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-433-122
excerpt: "CRE 433-122 · in Technical application security controls › Secure data storage › Encrypt data at rest › Encryption algorithms · 13 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [433-122](https://opencre.org/cre/433-122)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]] › [[cre-742-432]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V6.2.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x14-V6-Cryptography.md#v62-algorithms) | Verify that nonces, initialization vectors, and other single use numbers must not be used more than once with a given encryption key. The method of generation must be appropriate for the algorithm being used. | curated |

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

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10105-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java) | Weak Authentication Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [433-122](https://opencre.org/cre/433-122). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
