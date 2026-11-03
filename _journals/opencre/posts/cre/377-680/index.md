---
id: "CRE-377-680"
title: "Reject non-whitelisted content types"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-377-680
excerpt: "CRE 377-680 · in Technical application security controls › Input and output protection › API/web services · 6 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [377-680](https://opencre.org/cre/377-680)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-118-110]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V13.1.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x21-V13-API.md#v131-generic-web-service-security) | Verify that requests containing unexpected or missing content types are rejected with appropriate headers (HTTP response status 406 Unacceptable or 415 Unsupported Media Type). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [1](https://capec.mitre.org/data/definitions/1.html) | Accessing Functionality Not Properly Constrained by ACLs | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [434](https://cwe.mitre.org/data/definitions/434.html) | Unrestricted Upload of File with Dangerous Type | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Web Service Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100022](https://github.com/zaproxy/community-scripts/blob/main/passive/Upload%20form%20discovery.js) | Upload Form Discovered | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [377-680](https://opencre.org/cre/377-680). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
