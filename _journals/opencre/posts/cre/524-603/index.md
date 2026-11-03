---
id: "CRE-524-603"
title: "Limit modification of access controls to specifically authorized actors/users"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-524-603
excerpt: "CRE 524-603 · in Technical application security controls › Technical application access control › Minimize permissions · 7 mappings to 5 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), PCI DSS
---
> **CRE**: [524-603](https://opencre.org/cre/524-603)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-123-124]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V4.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md#v41-general-access-control-design) | Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [639](https://cwe.mitre.org/data/definitions/639.html) | Authorization Bypass Through User-Controlled Key | curated |
| [566](https://cwe.mitre.org/data/definitions/566.html) | Authorization Bypass Through User-Controlled SQL Primary Key | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html) | curated |
|  | [Authorization Testing Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHZ-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 5.3.5 | Anti-malware mechanisms cannot be disabled or altered by users, unless specifically documented, and authorized by management on a case-by-case basis for a limited time period. (CUSTOMIZED APPROACH OBJECTIVE): Anti-malware mechanisms cannot be modified by unauthorized personnel. (APPLICABILITY NOTES): Anti-malware solutions may be temporarily disabled only if there is a legitimate technical need, as authorized by management on a case-by-case basis. If anti-malware protection needs to be disabled for a specific purpose, it must be formally authorized. Additional security measures may also need to be implemented for the period during which anti-malware protection is not active. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [524-603](https://opencre.org/cre/524-603). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
