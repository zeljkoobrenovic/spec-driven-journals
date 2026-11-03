---
id: "CRE-582-541"
title: "Re-authenticate before sensitive transactions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-582-541
excerpt: "CRE 582-541 · in Technical application security controls › Session management · 14 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [582-541](https://opencre.org/cre/582-541)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.7.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v37-defenses-against-session-management-exploits) | Verify the application ensures a full, valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [12](https://capec.mitre.org/data/definitions/12.html) | Choosing Message Identifier | automatic |
| [36](https://capec.mitre.org/data/definitions/36.html) | Using Unpublished Interfaces or Functionality | automatic |
| [62](https://capec.mitre.org/data/definitions/62.html) | Cross Site Request Forgery | automatic |
| [166](https://capec.mitre.org/data/definitions/166.html) | Force the System to Reset Values | automatic |
| [216](https://capec.mitre.org/data/definitions/216.html) | Communication Channel Manipulation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [306](https://cwe.mitre.org/data/definitions/306.html) | Missing Authentication for Critical Function | curated |
| [288](https://cwe.mitre.org/data/definitions/288.html) | Authentication Bypass Using an Alternate Path or Channel | automatic |
| [322](https://cwe.mitre.org/data/definitions/322.html) | Key Exchange without Entity Authentication | automatic |
| [425](https://cwe.mitre.org/data/definitions/425.html) | Direct Request ('Forced Browsing') | automatic |
| [1299](https://cwe.mitre.org/data/definitions/1299.html) | Missing Protection Mechanism for Alternate Hardware Interface | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | curated |
|  | [Transaction Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [582-541](https://opencre.org/cre/582-541). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
