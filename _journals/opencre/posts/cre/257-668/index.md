---
id: "CRE-257-668"
title: "Configure CSP configuration properly"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-257-668
excerpt: "CRE 257-668 · in Technical application security controls › Configuration hardening › HTTP security headers · 17 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [257-668](https://opencre.org/cre/257-668)
>
> **Part of**: [[cre-636-660]] › [[cre-233-748]] › [[cre-636-347]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-760-765]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.4.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v144-http-security-headers) | Verify that a Content Security Policy (CSP) response header is in place that helps mitigate impact for XSS attacks like HTML, DOM, JSON, and JavaScript injection vulnerabilities. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [103](https://capec.mitre.org/data/definitions/103.html) | Clickjacking | automatic |
| [181](https://capec.mitre.org/data/definitions/181.html) | Flash File Overlay | automatic |
| [222](https://capec.mitre.org/data/definitions/222.html) | iFrame Overlay | automatic |
| [504](https://capec.mitre.org/data/definitions/504.html) | Task Impersonation | automatic |
| [506](https://capec.mitre.org/data/definitions/506.html) | Tapjacking | automatic |
| [587](https://capec.mitre.org/data/definitions/587.html) | Cross Frame Scripting (XFS) | automatic |
| [654](https://capec.mitre.org/data/definitions/654.html) | Credential Prompt Impersonation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [1021](https://cwe.mitre.org/data/definitions/1021.html) | Improper Restriction of Rendered UI Layers or Frames | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting.html) | curated |
|  | [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting.html) | curated |
|  | [WSTG-INPV-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10020-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/AntiClickjackingScanRule.java) | Missing Anti-clickjacking Header | automatic |
| [10020-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/AntiClickjackingScanRule.java) | Multiple X-Frame-Options Header Entries | automatic |
| [10020-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/AntiClickjackingScanRule.java) | X-Frame-Options Defined via META (Non-compliant with Spec) | automatic |
| [10020-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/AntiClickjackingScanRule.java) | X-Frame-Options Setting Malformed | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [257-668](https://opencre.org/cre/257-668). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
