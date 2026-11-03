---
id: "CRE-473-758"
title: "Set sufficient anti-caching headers"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-473-758
excerpt: "CRE 473-758 · in Technical application security controls › Secure data storage › Manage temporary storage · 7 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [473-758](https://opencre.org/cre/473-758)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-208-830]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-636-347]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v82-client-side-data-protection) | Verify the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [37](https://capec.mitre.org/data/definitions/37.html) | Retrieve Embedded Sensitive Data | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [525](https://cwe.mitre.org/data/definitions/525.html) | Use of Web Browser Cache Containing Sensitive Information | curated |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHN-06](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10015](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CacheControlScanRule.java) | Re-examine Cache-control Directives | automatic |
| [10050-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/RetrievedFromCacheScanRule.java) | Retrieved from Cache | automatic |
| [10050-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/RetrievedFromCacheScanRule.java) | Retrieved from Cache | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [473-758](https://opencre.org/cre/473-758). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
