---
id: "CRE-316-272"
title: "Whitelist CORS resources"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-316-272
excerpt: "CRE 316-272 · in Technical application security controls › Input and output protection › Validate HTTP request headers · 24 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [316-272](https://opencre.org/cre/316-272)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-541-441]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.5.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v145-http-request-header-validation) | Verify that the Cross-Origin Resource Sharing (CORS) Access-Control-Allow-Origin header uses a strict allow list of trusted domains and subdomains to match against and does not support the "null" origin. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [21](https://capec.mitre.org/data/definitions/21.html) | Exploitation of Trusted Identifiers | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [75](https://capec.mitre.org/data/definitions/75.html) | Manipulating Writeable Configuration Files | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [89](https://capec.mitre.org/data/definitions/89.html) | Pharming | automatic |
| [111](https://capec.mitre.org/data/definitions/111.html) | JSON Hijacking (aka JavaScript Hijacking) | automatic |
| [141](https://capec.mitre.org/data/definitions/141.html) | Cache Poisoning | automatic |
| [142](https://capec.mitre.org/data/definitions/142.html) | DNS Cache Poisoning | automatic |
| [160](https://capec.mitre.org/data/definitions/160.html) | Exploit Script-Based APIs | automatic |
| [384](https://capec.mitre.org/data/definitions/384.html) | Application API Message Manipulation via Man-in-the-Middle | automatic |
| [385](https://capec.mitre.org/data/definitions/385.html) | Transaction or Event Tampering via Application API Manipulation | automatic |
| [386](https://capec.mitre.org/data/definitions/386.html) | Application API Navigation Remapping | automatic |
| [387](https://capec.mitre.org/data/definitions/387.html) | Navigation Remapping To Propagate Malicious Content | automatic |
| [388](https://capec.mitre.org/data/definitions/388.html) | Application API Button Hijacking | automatic |
| [510](https://capec.mitre.org/data/definitions/510.html) | SaaS User Request Forgery | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [346](https://cwe.mitre.org/data/definitions/346.html) | Origin Validation Error | curated |
| [925](https://cwe.mitre.org/data/definitions/925.html) | Improper Verification of Intent by Broadcast Receiver | automatic |
| [939](https://cwe.mitre.org/data/definitions/939.html) | Improper Authorization in Handler for Custom URL Scheme | automatic |
| [940](https://cwe.mitre.org/data/definitions/940.html) | Improper Verification of Source of a Communication Channel | automatic |
| [1385](https://cwe.mitre.org/data/definitions/1385.html) | Missing Origin Validation in WebSockets | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-07](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/07-Testing_Cross_Origin_Resource_Sharing.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100025](https://github.com/zaproxy/community-scripts/blob/main/active/Cross%20Site%20WebSocket%20Hijacking.js) | Cross-Site WebSocket Hijacking | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [316-272](https://opencre.org/cre/316-272). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
