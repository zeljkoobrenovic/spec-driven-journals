---
id: "CRE-430-636"
title: "Verify TLS certificates and trust chain"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-430-636
excerpt: "CRE 430-636 · in Technical application security controls › Secure communication › TLS · 11 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, PCI DSS
---
> **CRE**: [430-636](https://opencre.org/cre/430-636)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-228-551]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-pci-dss]]

## Related CREs

- [[cre-486-813]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V9.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x17-V9-Communications.md#v92-server-communication-security) | Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [459](https://capec.mitre.org/data/definitions/459.html) | Creating a Rogue Certification Authority Certificate | automatic |
| [475](https://capec.mitre.org/data/definitions/475.html) | Signature Spoofing by Improper Validation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [295](https://cwe.mitre.org/data/definitions/295.html) | Improper Certificate Validation | curated |
| [296](https://cwe.mitre.org/data/definitions/296.html) | Improper Following of a Certificate's Chain of Trust | automatic |
| [297](https://cwe.mitre.org/data/definitions/297.html) | Improper Validation of Certificate with Host Mismatch | automatic |
| [298](https://cwe.mitre.org/data/definitions/298.html) | Improper Validation of Certificate Expiration | automatic |
| [299](https://cwe.mitre.org/data/definitions/299.html) | Improper Check for Certificate Revocation | automatic |
| [370](https://cwe.mitre.org/data/definitions/370.html) | Missing Check for Certificate Revocation after Initial Check | automatic |
| [599](https://cwe.mitre.org/data/definitions/599.html) | Missing Validation of OpenSSL Certificate | automatic |

More: [[standard-cwe]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 4.2.1.1 | An inventory of the entity’s trusted keys and certificates used to protect PAN during transmission is maintained. (CUSTOMIZED APPROACH OBJECTIVE): All keys and certificates used to protect PAN during transmission are identified and confirmed as trusted. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [430-636](https://opencre.org/cre/430-636). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
