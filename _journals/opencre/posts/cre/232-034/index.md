---
id: "CRE-232-034"
title: "Set '_Host'  prefix for cookie-based session tokens"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-232-034
excerpt: "CRE 232-034 · in Technical application security controls › Session management › Cookie-config · 9 mappings to 5 standards and tools."
tags: ASVS, NIST 800-63, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [232-034](https://opencre.org/cre/232-034)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-110-531]]
>
> **Maps to**: [[standard-asvs]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.4.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v34-cookie-based-session-management) | Verify that cookie-based session tokens use the "__Host-" prefix so cookies are only sent to the host that initially set the cookie. | curated |

More: [[standard-asvs]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 7.1.1 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html#host-prefix) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10058](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/GetForPostScanRule.java) | GET for POST | automatic |
| [10063-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/PermissionsPolicyScanRule.java) | Deprecated Feature Policy Header Set | automatic |
| [50007-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Endpoint Supports Introspection | automatic |
| [50007-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/graphql/src/main/java/org/zaproxy/addon/graphql/ExtensionGraphQl.java) | GraphQL Circular Type Reference | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [232-034](https://opencre.org/cre/232-034). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
