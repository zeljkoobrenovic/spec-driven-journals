---
id: "CRE-284-521"
title: "Enforce additional authorization and segregation of duties"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-284-521
excerpt: "CRE 284-521 · in Technical application security controls › Technical application access control › Strong authorization checking · 24 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS, ZAP Rule
---
> **CRE**: [284-521](https://opencre.org/cre/284-521)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-128-128]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V4.3.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md#v43-other-access-control-considerations) | Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [1](https://capec.mitre.org/data/definitions/1.html) | Accessing Functionality Not Properly Constrained by ACLs | automatic |
| [17](https://capec.mitre.org/data/definitions/17.html) | Using Malicious Files | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [61](https://capec.mitre.org/data/definitions/61.html) | Session Fixation | automatic |
| [62](https://capec.mitre.org/data/definitions/62.html) | Cross Site Request Forgery | automatic |
| [81](https://capec.mitre.org/data/definitions/81.html) | Web Server Logs Tampering | automatic |
| [122](https://capec.mitre.org/data/definitions/122.html) | Privilege Abuse | automatic |
| [127](https://capec.mitre.org/data/definitions/127.html) | Directory Indexing | automatic |
| [180](https://capec.mitre.org/data/definitions/180.html) | Exploiting Incorrectly Configured Access Control Security Levels | automatic |
| [206](https://capec.mitre.org/data/definitions/206.html) | Signing Malicious Code | automatic |
| [234](https://capec.mitre.org/data/definitions/234.html) | Hijacking a privileged process | automatic |
| [642](https://capec.mitre.org/data/definitions/642.html) | Replace Binaries | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [732](https://cwe.mitre.org/data/definitions/732.html) | Incorrect Permission Assignment for Critical Resource | curated |
| [276](https://cwe.mitre.org/data/definitions/276.html) | Incorrect Default Permissions | automatic |
| [277](https://cwe.mitre.org/data/definitions/277.html) | Insecure Inherited Permissions | automatic |
| [278](https://cwe.mitre.org/data/definitions/278.html) | Insecure Preserved Inherited Permissions | automatic |
| [279](https://cwe.mitre.org/data/definitions/279.html) | Incorrect Execution-Assigned Permissions | automatic |
| [281](https://cwe.mitre.org/data/definitions/281.html) | Improper Preservation of Permissions | automatic |
| [766](https://cwe.mitre.org/data/definitions/766.html) | Critical Data Element Declared Public | automatic |
| [1004](https://cwe.mitre.org/data/definitions/1004.html) | Sensitive Cookie Without 'HttpOnly' Flag | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [REST Assessment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.5.4 | Roles and functions are separated between production and pre-production environments to provide accountability such that only reviewed and approved changes are deployed. (CUSTOMIZED APPROACH OBJECTIVE): Job roles and accountability that differentiate between pre-production and production activities are defined and managed to minimize the risk of unauthorized, unintentional, or inappropriate actions. (APPLICABILITY NOTES): In environments with limited personnel where individuals perform multiple roles or functions, this same goal can be achieved with additional procedural controls that provide accountability. For example, a developer may also be an administrator that uses an administrator-level account with elevated privileges in the development environment and, for their developer role, they use a separate account with user-level access to the production environment. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10010](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieHttpOnlyScanRule.java) | Cookie No HttpOnly Flag | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [284-521](https://opencre.org/cre/284-521). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
