---
id: "CRE-480-071"
title: "Prevent Click jacking through X-Frame-Options or CSP"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-480-071
excerpt: "CRE 480-071 · in Technical application security controls › Configuration hardening › HTTP security headers · 15 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [480-071](https://opencre.org/cre/480-071)
>
> **Part of**: [[cre-636-660]] › [[cre-233-748]] › [[cre-636-347]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.4.7](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v144-http-security-headers) | Verify that the content of a web application cannot be embedded in a third-party site by default and that embedding of the exact resources is only allowed where necessary by using suitable Content-Security-Policy: frame-ancestors and X-Frame-Options response headers. | curated |

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
|  | [WSTG-CLNT-09](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/09-Testing_for_Clickjacking.html) | curated |

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

Generated from the OpenCRE catalogue entry [480-071](https://opencre.org/cre/480-071). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
