---
id: "CRE-821-832"
title: "Ensure keys and passwords are replaceable"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-821-832
excerpt: "CRE 821-832 · in Technical application security controls › Secure data storage › Secret storage · 5 mappings to 3 standards and tools."
tags: ASVS, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [821-832](https://opencre.org/cre/821-832)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-223-780]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.6.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v16-cryptographic-architecture) | Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data. | curated |

More: [[standard-asvs]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | curated |
|  | [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 2.3.2 | For wireless environments connected to the CDE or transmitting account data, wireless encryption keys are changed as follows: () Whenever personnel with knowledge of the key leave the company or the role for which the knowledge was necessary. () Whenever a key is suspected of or known to be compromised. (CUSTOMIZED APPROACH OBJECTIVE): Knowledge of wireless encryption keys cannot allow unauthorized access to wireless networks. | automatic |
| 3.7.5 | Key management policies procedures are implemented to include the retirement, replacement, or destruction of keys used to protect stored account data, as deemed necessary when: () The key has reached the end of its defined cryptoperiod. () The integrity of the key has been weakened, including when personnel with knowledge of a cleartext key component leaves the company, or the role for which the key component was known. () The key is suspected of or known to be compromised. Retired or replaced keys are not used for encryption operations. (CUSTOMIZED APPROACH OBJECTIVE): Keys are removed from active use when it is suspected or known that the integrity of the key is weakened. (APPLICABILITY NOTES): If retired or replaced cryptographic keys need to be retained, these keys must be securely archived (for example, by using a key-encryption key). | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [821-832](https://opencre.org/cre/821-832). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
