---
id: "CRE-838-636"
title: "Check source code and third party libraries to not contain backdoors"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-838-636
excerpt: "CRE 838-636 · in Development processes for security › Supply chain management › Dependency integrity · 5 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [838-636](https://opencre.org/cre/838-636)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]] › [[cre-613-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.2.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v102-malicious-code-search) | Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, rootkits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [698](https://capec.mitre.org/data/definitions/698.html) | Install Malicious Extension | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [507](https://cwe.mitre.org/data/definitions/507.html) | Trojan Horse | curated |
| [508](https://cwe.mitre.org/data/definitions/508.html) | Non-Replicating Malicious Code | automatic |
| [509](https://cwe.mitre.org/data/definitions/509.html) | Replicating Malicious Code (Virus or Worm) | automatic |

More: [[standard-cwe]]

## Source

Generated from the OpenCRE catalogue entry [838-636](https://opencre.org/cre/838-636). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
