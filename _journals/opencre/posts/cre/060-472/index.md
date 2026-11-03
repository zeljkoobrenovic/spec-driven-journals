---
id: "CRE-060-472"
title: "Use CSRF protection against authenticated functionality, add anti-automation controls for unauthenticated functionality"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-060-472
excerpt: "CRE 060-472 · in Technical application security controls › Technical application access control › Strong authorization checking · 22 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [060-472](https://opencre.org/cre/060-472)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-128-128]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-028-727]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V4.2.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md#v42-operation-level-access-control) | Verify that the application or framework enforces a strong anti-CSRF mechanism to protect authenticated functionality, and effective anti-automation or anti-CSRF protects unauthenticated functionality. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [62](https://capec.mitre.org/data/definitions/62.html) | Cross Site Request Forgery | automatic |
| [111](https://capec.mitre.org/data/definitions/111.html) | JSON Hijacking (aka JavaScript Hijacking) | automatic |
| [462](https://capec.mitre.org/data/definitions/462.html) | Cross-Domain Search Timing | automatic |
| [467](https://capec.mitre.org/data/definitions/467.html) | Cross Site Identification | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [352](https://cwe.mitre.org/data/definitions/352.html) | Cross-Site Request Forgery (CSRF) | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Authorization Testing Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html) | curated |
|  | [Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Insecure Direct Object Reference Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-05](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10202](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CsrfCountermeasuresScanRule.java) | Absence of Anti-CSRF Tokens | automatic |
| [20012](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/CsrfTokenScanRule.java) | Anti-CSRF Tokens Check | automatic |
| [40103](https://github.com/zaproxy/zap-extensions/blob/main/addOns/foxhound/src/main/java/org/zaproxy/zap/extension/foxhound/ExtensionFoxhound.java) | Cross Site Request Forgery | automatic |
| [90005-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Site Header is Missing | automatic |
| [90005-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Mode Header is Missing | automatic |
| [90005-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Dest Header is Missing | automatic |
| [90005-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-User Header is Missing | automatic |
| [90005-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Site Header Has an Invalid Value | automatic |
| [90005-6](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Mode Header Has an Invalid Value | automatic |
| [90005-7](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-Dest Header Has an Invalid Value | automatic |
| [90005-8](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/FetchMetadataRequestHeadersScanRule.java) | Sec-Fetch-User Header Has an Invalid Value | automatic |
| [100005](https://github.com/zaproxy/community-scripts/blob/main/passive/detect_samesite_protection.js) | SameSite Cookie Attribute Protection Used | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [060-472](https://opencre.org/cre/060-472). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
