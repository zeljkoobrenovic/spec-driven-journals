---
id: "CRE-387-848"
title: "Parse JSON safely"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-387-848
excerpt: "CRE 387-848 · in Technical application security controls › Input and output protection › Deserialization Prevention · 10 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [387-848](https://opencre.org/cre/387-848)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-836-068]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.5.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v55-deserialization-prevention) | Verify that when parsing JSON in browsers or JavaScript-based backends, JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [35](https://capec.mitre.org/data/definitions/35.html) | Leverage Executable Code in Non-Executable Files | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [95](https://cwe.mitre.org/data/definitions/95.html) | Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) | curated |
|  | [XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html) | curated |
|  | [XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/02-Testing_for_JavaScript_Execution.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [210001-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Dynamic code execution via eval | automatic |
| [210001-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Dynamic code execution via Function constructor | automatic |
| [210001-3](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Dynamic code execution via Function.apply | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [387-848](https://opencre.org/cre/387-848). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
