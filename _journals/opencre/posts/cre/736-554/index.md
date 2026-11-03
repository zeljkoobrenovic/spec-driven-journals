---
id: "CRE-736-554"
title: "Block serialization of content from untrusted clients"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-736-554
excerpt: "CRE 736-554 · in Technical application security controls › Input and output protection › Deserialization Prevention · 7 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS, ZAP Rule
---
> **CRE**: [736-554](https://opencre.org/cre/736-554)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-836-068]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.5.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v15-input-and-output-architecture) | Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [586](https://capec.mitre.org/data/definitions/586.html) | Object Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [502](https://cwe.mitre.org/data/definitions/502.html) | Deserialization of Untrusted Data | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.4.3 | Anti-spoofing measures are implemented to detect and block forged source IP addresses from entering the trusted network. (CUSTOMIZED APPROACH OBJECTIVE): Packets with forged IP source addresses cannot enter a trusted network. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [90002](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/JsoScanRule.java) | Java Serialization Object | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [736-554](https://opencre.org/cre/736-554). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
