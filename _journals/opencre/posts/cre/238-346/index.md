---
id: "CRE-238-346"
title: "Terminate all sessions when password is changed"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-238-346
excerpt: "CRE 238-346 · in Technical application security controls › Session management › Minimize session life · 5 mappings to 5 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [238-346](https://opencre.org/cre/238-346)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-470-731]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.3.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v33-session-termination) | Verify that the application gives the option to terminate all other active sessions after a successful password change (including change via password reset/recovery), and that this is effective across the application, federated login (if present), and any relying parties. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [613](https://cwe.mitre.org/data/definitions/613.html) | Insufficient Session Expiration | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-06](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/06-Testing_for_Logout_Functionality.html#testing-for-log-out-user-interface) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.2.5 | Access for terminated users is immediately revoked. (CUSTOMIZED APPROACH OBJECTIVE): The accounts of terminated users cannot be used. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [238-346](https://opencre.org/cre/238-346). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
