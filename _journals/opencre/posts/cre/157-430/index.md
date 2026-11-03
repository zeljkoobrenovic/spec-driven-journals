---
id: "CRE-157-430"
title: "Protect and clear cached sensitive data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-157-430
excerpt: "CRE 157-430 · in Technical application security controls › Secure data storage › Manage temporary storage · 11 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, ZAP Rule
---
> **CRE**: [157-430](https://opencre.org/cre/157-430)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-208-830]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v81-general-data-protection) | Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [37](https://capec.mitre.org/data/definitions/37.html) | Retrieve Embedded Sensitive Data | automatic |
| [204](https://capec.mitre.org/data/definitions/204.html) | Lifting Sensitive Data Embedded in Cache | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [524](https://cwe.mitre.org/data/definitions/524.html) | Use of Cache Containing Sensitive Information | curated |
| [525](https://cwe.mitre.org/data/definitions/525.html) | Use of Web Browser Cache Containing Sensitive Information | automatic |

More: [[standard-cwe]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10015](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CacheControlScanRule.java) | Re-examine Cache-control Directives | automatic |
| [10049-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/CacheableScanRule.java) | Non-Storable Content | automatic |
| [10049-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/CacheableScanRule.java) | Storable but Non-Cacheable Content | automatic |
| [10049-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/CacheableScanRule.java) | Storable and Cacheable Content | automatic |
| [10050-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/RetrievedFromCacheScanRule.java) | Retrieved from Cache | automatic |
| [10050-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/RetrievedFromCacheScanRule.java) | Retrieved from Cache | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [157-430](https://opencre.org/cre/157-430). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
