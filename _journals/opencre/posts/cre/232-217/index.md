---
id: "CRE-232-217"
title: "Whitelist redirected/forwarded URLs"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-232-217
excerpt: "CRE 232-217 · in Technical application security controls › Input and output protection › Input validation · 16 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [232-217](https://opencre.org/cre/232-217)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-010-308]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.1.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v51-input-validation) | Verify that URL redirects and forwards only allow destinations which appear on an allow list, or show a warning when redirecting to potentially untrusted content. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [178](https://capec.mitre.org/data/definitions/178.html) | Cross-Site Flashing | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [601](https://cwe.mitre.org/data/definitions/601.html) | URL Redirection to Untrusted Site ('Open Redirect') | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/04-Testing_for_Client_Side_URL_Redirect.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10028](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/UserControlledOpenRedirectScanRule.java) | Off-site Redirect | automatic |
| [20019-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ExternalRedirectScanRule.java) | External Redirect | automatic |
| [20019-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ExternalRedirectScanRule.java) | External Redirect | automatic |
| [20019-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ExternalRedirectScanRule.java) | External Redirect | automatic |
| [20019-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ExternalRedirectScanRule.java) | External Redirect | automatic |
| [210002-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Open redirect via window.open | automatic |
| [210002-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Open redirect via Navigation API | automatic |
| [210004-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Route-controlled history.replaceState | automatic |
| [210004-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Route-controlled Navigation API transition | automatic |
| [210005-1](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | Form action manipulated by tainted route or body input | automatic |
| [210005-2](https://github.com/DenisPodgurskii/pentestkit/blob/master/src/ptk/background/iast/modules/modules.json) | formAction manipulated by tainted route or body input | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [232-217](https://opencre.org/cre/232-217). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
