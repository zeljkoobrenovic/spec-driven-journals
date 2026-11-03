---
id: "CRE-402-133"
title: "Do not expose session token in URL"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-402-133
excerpt: "CRE 402-133 · in Technical application security controls › Session management · 8 mappings to 4 standards and tools."
tags: ASVS, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [402-133](https://opencre.org/cre/402-133)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v31-fundamental-session-management-security) | Verify the application never reveals session tokens in URL parameters. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [598](https://cwe.mitre.org/data/definitions/598.html) | Use of HTTP Request With Sensitive Query String | curated |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/04-Testing_for_Exposed_Session_Variables.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [3-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoSessionIdUrlScanRule.java) | Session ID in URL Rewrite | automatic |
| [3-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoSessionIdUrlScanRule.java) | Session ID in URL Rewrite | automatic |
| [3-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoSessionIdUrlScanRule.java) | Referer Exposes Session ID | automatic |
| [10024](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InformationDisclosureInUrlScanRule.java) | Information Disclosure - Sensitive Information in URL | automatic |
| [10025](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InformationDisclosureReferrerScanRule.java) | Information Disclosure - Sensitive Information in HTTP Referrer Header | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [402-133](https://opencre.org/cre/402-133). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
