---
id: "CRE-614-353"
title: "Store backups securely"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-614-353
excerpt: "CRE 614-353 · in Operating processes for security › Facilities management › Backup · 14 mappings to 4 standards and tools."
tags: ASVS, CWE, PCI DSS, ZAP Rule
---
> **CRE**: [614-353](https://opencre.org/cre/614-353)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]] › [[cre-163-776]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.1.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v81-general-data-protection) | Verify that backups are stored securely to prevent data from being stolen or corrupted. | curated |

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

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 9.4.1.1 | Offline media backups with cardholder data are stored in a secure location. (CUSTOMIZED APPROACH OBJECTIVE): Offline backups cannot be accessed by unauthorized personnel. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [120002-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/JwtInStorageScanRule.java) | Information Disclosure - JWT in Browser localStorage | automatic |
| [120002-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/client/src/main/java/org/zaproxy/addon/client/pscan/JwtInStorageScanRule.java) | Information Disclosure - JWT in Browser sessionStorage | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [614-353](https://opencre.org/cre/614-353). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
