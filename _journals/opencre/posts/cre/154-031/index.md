---
id: "CRE-154-031"
title: "Harden application by excluding unwanted functionality"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-154-031
excerpt: "CRE 154-031 · in Development processes for security › Supply chain management · 6 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, PCI DSS
---
> **CRE**: [154-031](https://opencre.org/cre/154-031)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-pci-dss]]

## Related CREs

- [[cre-486-813]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.2.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v102-malicious-code-search) | Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality. | curated |

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

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 2.2.4 | Only necessary services, protocols, daemons, and functions are enabled, and all unnecessary functionality is removed or disabled. (CUSTOMIZED APPROACH OBJECTIVE): System components cannot be compromised by exploiting unnecessary functionality present in the system component. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [154-031](https://opencre.org/cre/154-031). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
