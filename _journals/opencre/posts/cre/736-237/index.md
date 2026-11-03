---
id: "CRE-736-237"
title: "Set metadata/content-Disposition for API responses"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-736-237
excerpt: "CRE 736-237 · in Technical application security controls › Configuration hardening › HTTP security headers · 10 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [736-237](https://opencre.org/cre/736-237)
>
> **Part of**: [[cre-636-660]] › [[cre-233-748]] › [[cre-636-347]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.4.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v144-http-security-headers) | Verify that all API responses contain a Content-Disposition: attachment; filename="api.json" header (or other appropriate filename for the content type). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [73](https://capec.mitre.org/data/definitions/73.html) | User-Controlled Filename | automatic |
| [81](https://capec.mitre.org/data/definitions/81.html) | Web Server Logs Tampering | automatic |
| [85](https://capec.mitre.org/data/definitions/85.html) | AJAX Footprinting | automatic |
| [104](https://capec.mitre.org/data/definitions/104.html) | Cross Zone Scripting | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [116](https://cwe.mitre.org/data/definitions/116.html) | Improper Encoding or Escaping of Output | curated |
| [117](https://cwe.mitre.org/data/definitions/117.html) | Improper Output Neutralization for Logs | automatic |
| [644](https://cwe.mitre.org/data/definitions/644.html) | Improper Neutralization of HTTP Headers for Scripting Syntax | automatic |
| [838](https://cwe.mitre.org/data/definitions/838.html) | Inappropriate Encoding for Output Context | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [736-237](https://opencre.org/cre/736-237). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
