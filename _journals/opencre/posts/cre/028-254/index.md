---
id: "CRE-028-254"
title: "Secure auto-updates over full stack"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-028-254
excerpt: "CRE 028-254 · in Development processes for security › Deploy/build · 16 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [028-254](https://opencre.org/cre/028-254)
>
> **Part of**: [[cre-616-305]] › [[cre-473-177]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v103-application-integrity) | Verify that if the application has a client or server auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [184](https://capec.mitre.org/data/definitions/184.html) | Software Integrity Attack | automatic |
| [185](https://capec.mitre.org/data/definitions/185.html) | Malicious Software Download | automatic |
| [186](https://capec.mitre.org/data/definitions/186.html) | Malicious Software Update | automatic |
| [187](https://capec.mitre.org/data/definitions/187.html) | Malicious Automated Software Update via Redirection | automatic |
| [533](https://capec.mitre.org/data/definitions/533.html) | Malicious Manual Software Update | automatic |
| [538](https://capec.mitre.org/data/definitions/538.html) | Open-Source Library Manipulation | automatic |
| [657](https://capec.mitre.org/data/definitions/657.html) | Malicious Automated Software Update via Spoofing | automatic |
| [662](https://capec.mitre.org/data/definitions/662.html) | Adversary in the Browser (AiTB) | automatic |
| [691](https://capec.mitre.org/data/definitions/691.html) | Spoof Open-Source Software Metadata | automatic |
| [692](https://capec.mitre.org/data/definitions/692.html) | Spoof Version Control System Commit Metadata | automatic |
| [693](https://capec.mitre.org/data/definitions/693.html) | StarJacking | automatic |
| [695](https://capec.mitre.org/data/definitions/695.html) | Repo Jacking | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [494](https://cwe.mitre.org/data/definitions/494.html) | Download of Code Without Integrity Check | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 5.3.1 | The anti-malware solution(s) is kept current via automatic updates. (CUSTOMIZED APPROACH OBJECTIVE): Anti-malware mechanisms can detect and address the latest malware threats. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [028-254](https://opencre.org/cre/028-254). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
