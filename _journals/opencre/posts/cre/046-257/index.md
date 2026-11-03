---
id: "CRE-046-257"
title: "Clear authentication data from client storage"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-046-257
excerpt: "CRE 046-257 · in Technical application security controls › Secure data storage › Manage temporary storage · 15 mappings to 5 standards and tools."
tags: ASVS, CWE, OWASP Web Security Testing Guide (WSTG), PCI DSS, ZAP Rule
---
> **CRE**: [046-257](https://opencre.org/cre/046-257)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-208-830]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.2.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v82-client-side-data-protection) | Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [922](https://cwe.mitre.org/data/definitions/922.html) | Insecure Storage of Sensitive Information | curated |
| [312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | automatic |
| [313](https://cwe.mitre.org/data/definitions/313.html) | Cleartext Storage in a File or on Disk | automatic |
| [314](https://cwe.mitre.org/data/definitions/314.html) | Cleartext Storage in the Registry | automatic |
| [315](https://cwe.mitre.org/data/definitions/315.html) | Cleartext Storage of Sensitive Information in a Cookie | automatic |
| [316](https://cwe.mitre.org/data/definitions/316.html) | Cleartext Storage of Sensitive Information in Memory | automatic |
| [317](https://cwe.mitre.org/data/definitions/317.html) | Cleartext Storage of Sensitive Information in GUI | automatic |
| [318](https://cwe.mitre.org/data/definitions/318.html) | Cleartext Storage of Sensitive Information in Executable | automatic |
| [526](https://cwe.mitre.org/data/definitions/526.html) | Cleartext Storage of Sensitive Information in an Environment Variable | automatic |
| [921](https://cwe.mitre.org/data/definitions/921.html) | Storage of Sensitive Data in a Mechanism without Access Control | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CLNT-12](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client_Side_Testing/12-Testing_Browser_Storage.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.3 | Sensitive authentication data (SAD) is not stored after authorization. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [120002-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/JwtInStorageScanRule.java) | Information Disclosure - JWT in Browser localStorage | automatic |
| [120002-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/JwtInStorageScanRule.java) | Information Disclosure - JWT in Browser sessionStorage | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [046-257](https://opencre.org/cre/046-257). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
