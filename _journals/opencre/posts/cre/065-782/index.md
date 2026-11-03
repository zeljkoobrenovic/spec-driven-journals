---
id: "CRE-065-782"
title: "Ensure session timeout (soft/hard)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-065-782
excerpt: "CRE 065-782 · in Technical application security controls › Session management › Minimize session life · 7 mappings to 7 standards and tools."
tags: ASVS, CWE, NIST 800-63, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [065-782](https://opencre.org/cre/065-782)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-470-731]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.3.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v33-session-termination) | If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [613](https://cwe.mitre.org/data/definitions/613.html) | Insufficient Session Expiration | curated |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 7.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C6](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c6-implement-digital-identity.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-07](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/07-Testing_Session_Timeout.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.2.8 | If a user session has been idle for more than 15 minutes, the user is required to re-authenticate to re-activate the terminal or session. (CUSTOMIZED APPROACH OBJECTIVE): A user session cannot be used except by the authorized user. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). This requirement is not meant to prevent legitimate activities from being performed while the console/PC is unattended. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [065-782](https://opencre.org/cre/065-782). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
