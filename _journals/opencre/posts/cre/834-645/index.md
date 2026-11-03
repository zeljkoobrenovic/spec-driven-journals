---
id: "CRE-834-645"
title: "Avoid unauthorized client data collection"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-834-645
excerpt: "CRE 834-645 · in Development processes for security › Supply chain management › Dependency integrity · 13 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, ZAP Rule
---
> **CRE**: [834-645](https://opencre.org/cre/834-645)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]] › [[cre-613-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v102-malicious-code-search) | Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the user's permission for it to operate before collecting any data. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [464](https://capec.mitre.org/data/definitions/464.html) | Evercookie | automatic |
| [467](https://capec.mitre.org/data/definitions/467.html) | Cross Site Identification | automatic |
| [498](https://capec.mitre.org/data/definitions/498.html) | Probe iOS Screenshots | automatic |
| [508](https://capec.mitre.org/data/definitions/508.html) | Shoulder Surfing | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [359](https://cwe.mitre.org/data/definitions/359.html) | Exposure of Private Personal Information to an Unauthorized Actor | curated |

More: [[standard-cwe]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10062](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PiiScanRule.java) | PII Disclosure | automatic |
| [110004](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/Email%20Disclosure.js) | Email address found in WebSocket message | automatic |
| [110005](https://github.com/zaproxy/zap-extensions/blob/main/addOns/websocket/src/main/zapHomeFiles/scripts/templates/websocketpassive/PII%20Disclosure.js) | Personally Identifiable Information via WebSocket | automatic |
| [120000-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/InformationInStorageScanRule.java) | Information Disclosure - Information in Browser localStorage | automatic |
| [120000-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/InformationInStorageScanRule.java) | Information Disclosure - Information in Browser sessionStorage | automatic |
| [120001-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/SensitiveInfoInStorageScanRule.java) | Information Disclosure - Sensitive Information in Browser localStorage | automatic |
| [120001-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/SensitiveInfoInStorageScanRule.java) | Information Disclosure - Sensitive Information in Browser sessionStorage | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [834-645](https://opencre.org/cre/834-645). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
