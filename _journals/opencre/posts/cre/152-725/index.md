---
id: "CRE-152-725"
title: "Limit access to admin/management functionality"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-152-725
excerpt: "CRE 152-725 · in Technical application security controls › Technical application access control › Minimize permissions · 7 mappings to 5 standards and tools."
tags: CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [152-725](https://opencre.org/cre/152-725)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-123-124]]
>
> **Maps to**: [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [419](https://cwe.mitre.org/data/definitions/419.html) | Unprotected Primary Channel | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Web Service Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHZ-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 7.2.6 | All user access to query repositories of stored cardholder data is restricted as follows: () Via applications or other programmatic methods, with access and allowed actions based on user roles and least privileges. () Only the responsible administrator(s) can directly access or query repositories of stored CHD. (CUSTOMIZED APPROACH OBJECTIVE): Direct unfiltered (ad hoc) query access to cardholder data repositories is prohibited, unless performed by an authorized administrator. (APPLICABILITY NOTES): This requirement applies to controls for user access to query repositories of stored cardholder data. See Requirements 7.2.5 and 7.2.5.1 and 8.6.1 through 8.6.3 for controls for application and system accounts. | automatic |
| 9.2.4 | Access to consoles in sensitive areas is restricted via locking when not in use. (CUSTOMIZED APPROACH OBJECTIVE): Physical consoles within sensitive areas cannot be used by unauthorized personnel. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [152-725](https://opencre.org/cre/152-725). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
