---
id: "CRE-640-364"
title: "Enforce access control on trusted parts/serverside"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-640-364
excerpt: "CRE 640-364 · in Technical application security controls › Technical application access control › Strong authorization checking · 18 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [640-364](https://opencre.org/cre/640-364)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-128-128]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Related CREs

- [[cre-155-155]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.4.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v14-access-control-architecture) | Verify that trusted enforcement points, such as access control gateways, servers, and serverless functions, enforce access controls. Never enforce access controls on the client. | curated |

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
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [640-364](https://opencre.org/cre/640-364). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
