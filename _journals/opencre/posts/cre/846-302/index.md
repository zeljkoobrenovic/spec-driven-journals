---
id: "CRE-846-302"
title: "Prevent caching of sensitive data in server components"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-846-302
excerpt: "CRE 846-302 · in Technical application security controls › Secure data storage › Manage temporary storage · 12 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, PCI DSS, ZAP Rule
---
> **CRE**: [846-302](https://opencre.org/cre/846-302)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-208-830]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v81-general-data-protection) | Verify the application protects sensitive data from being cached in server components such as load balancers and application caches. | curated |

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

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.4.4 | System components that store cardholder data are not directly accessible from untrusted networks. (CUSTOMIZED APPROACH OBJECTIVE): Stored cardholder data cannot be accessed from untrusted networks. (APPLICABILITY NOTES): This requirement is not intended to apply to storage of account data in volatile memory but does apply where memory is being treated as persistent storage (for example, RAM disk). Account data can only be stored in volatile memory during the time necessary to support the associated business process (for example, until completion of the related payment card transaction). | automatic |

More: [[standard-pci-dss]]

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

Generated from the OpenCRE catalogue entry [846-302](https://opencre.org/cre/846-302). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
