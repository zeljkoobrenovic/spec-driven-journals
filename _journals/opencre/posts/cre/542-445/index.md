---
id: "CRE-542-445"
title: "Sanitize untrusted HTML input"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-542-445
excerpt: "CRE 542-445 · in Technical application security controls › Input and output protection › Sanitization and sandboxing · 15 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [542-445](https://opencre.org/cre/542-445)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-764-765]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v52-sanitization-and-sandboxing) | Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature. ((C5)(https://owasp.org/www-project-proactive-controls/#div-numbering)) | curated |

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
|  | [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) | curated |
|  | [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) | curated |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C5](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c5-validate-all-inputs.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/03-Testing_for_HTML_Injection.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [542-445](https://opencre.org/cre/542-445). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
