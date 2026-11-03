---
id: "CRE-333-888"
title: "Do not expose data through API URLs"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-333-888
excerpt: "CRE 333-888 · in Technical application security controls › Secure communication › Minimize communication · 10 mappings to 5 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [333-888](https://opencre.org/cre/333-888)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-341-076]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-118-110]]
- [[cre-486-813]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V13.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x21-V13-API.md#v131-generic-web-service-security) | Verify API URLs do not expose sensitive information, such as the API key, session tokens etc. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [598](https://cwe.mitre.org/data/definitions/598.html) | Use of HTTP Request With Sensitive Query String | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Web Service Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

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

Generated from the OpenCRE catalogue entry [333-888](https://opencre.org/cre/333-888). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
