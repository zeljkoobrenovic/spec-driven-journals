---
id: "CRE-848-711"
title: "Enforce input validation on a trusted service layer"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-848-711
excerpt: "CRE 848-711 · in Technical application security controls › Input and output protection › Input validation · 20 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls
---
> **CRE**: [848-711](https://opencre.org/cre/848-711)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-010-308]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]]

## Related CREs

- [[cre-155-155]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.5.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v15-input-and-output-architecture) | Verify that input validation is enforced on a trusted service layer. ((C5)(https://owasp.org/www-project-proactive-controls/#div-numbering)) | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [21](https://capec.mitre.org/data/definitions/21.html) | Exploitation of Trusted Identifiers | automatic |
| [31](https://capec.mitre.org/data/definitions/31.html) | Accessing/Intercepting/Modifying HTTP Cookies | automatic |
| [162](https://capec.mitre.org/data/definitions/162.html) | Manipulating Hidden Fields | automatic |
| [202](https://capec.mitre.org/data/definitions/202.html) | Create Malicious Client | automatic |
| [207](https://capec.mitre.org/data/definitions/207.html) | Removing Important Client Functionality | automatic |
| [208](https://capec.mitre.org/data/definitions/208.html) | Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements | automatic |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |
| [384](https://capec.mitre.org/data/definitions/384.html) | Application API Message Manipulation via Man-in-the-Middle | automatic |
| [385](https://capec.mitre.org/data/definitions/385.html) | Transaction or Event Tampering via Application API Manipulation | automatic |
| [386](https://capec.mitre.org/data/definitions/386.html) | Application API Navigation Remapping | automatic |
| [387](https://capec.mitre.org/data/definitions/387.html) | Navigation Remapping To Propagate Malicious Content | automatic |
| [388](https://capec.mitre.org/data/definitions/388.html) | Application API Button Hijacking | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [602](https://cwe.mitre.org/data/definitions/602.html) | Client-Side Enforcement of Server-Side Security | curated |
| [565](https://cwe.mitre.org/data/definitions/565.html) | Reliance on Cookies without Validation and Integrity Checking | automatic |
| [603](https://cwe.mitre.org/data/definitions/603.html) | Use of Client-Side Authentication | automatic |
| [784](https://cwe.mitre.org/data/definitions/784.html) | Reliance on Cookies without Validation and Integrity Checking in a Security Decision | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C5](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c5-validate-all-inputs.html) | curated |

More: [[standard-owasp-proactive-controls]]

## Source

Generated from the OpenCRE catalogue entry [848-711](https://opencre.org/cre/848-711). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
