---
id: "CRE-783-255"
title: "Store cryptographic keys securely"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-783-255
excerpt: "CRE 783-255 · in Technical application security controls › Secure data storage › Secret storage · 11 mappings to 4 standards and tools."
tags: ASVS, NIST 800-63, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [783-255](https://opencre.org/cre/783-255)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-223-780]]
>
> **Maps to**: [[standard-asvs]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.9.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v210-service-authentication) | Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a Trusted Platform Module (TPM) or Hardware Security Module (HSM), or an OS service that can use this secure storage. | curated |

More: [[standard-asvs]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.7.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | curated |
|  | [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.6 | Cryptographic keys used to protect stored account data are secured. | automatic |
| 3.6.1 | Procedures are defined and implemented to protect cryptographic keys used to protect stored account data against disclosure and misuse that include: () Access to keys is restricted to the fewest number of custodians necessary. () Key-encrypting keys are at least as strong as the data-encrypting keys they protect. () Key-encrypting keys are stored separately from data-encrypting keys. () Keys are stored securely in the fewest possible locations and forms. (CUSTOMIZED APPROACH OBJECTIVE): Processes that protect cryptographic keys used to protect stored account data against disclosure and misuse are defined and implemented. (APPLICABILITY NOTES): This requirement applies to keys used to encrypt stored account data and to key-encrypting keys used to protect data-encrypting keys. The requirement to protect keys used to protect stored account data from disclosure and misuse applies to both data-encrypting keys and keyencrypting keys. Because one key-encrypting key may grant access to many data-encrypting keys, the key-encrypting keys require strong protection measures. | automatic |
| 3.6.1.2 | Secret and private keys used to encrypt/decrypt stored account data are stored in one (or more) of the following forms at all times: () Encrypted with a key-encrypting key that is at least as strong as the data-encrypting key, and that is stored separately from the dataencrypting key. () Within a secure cryptographic device (SCD), such as a hardware security module (HSM) or PTS-approved point-of-interaction device. () As at least two full-length key components or key shares, in accordance with an industry-accepted method. (CUSTOMIZED APPROACH OBJECTIVE): Secret and private keys are stored in a secure form that prevents unauthorized retrieval or access. (APPLICABILITY NOTES): It is not required that public keys be stored in one of these forms. Cryptographic keys stored as part of a key management system (KMS) that employs SCDs are acceptable. A cryptographic key that is split into two parts does not meet this requirement. Secret or private keys stored as key components or key shares must be generated via one of the following: () Using an approved random number generator and within an SCD, OR () According to ISO 19592 or equivalent industry standard for generation of secret key shares. | automatic |
| 3.6.1.4 | Cryptographic keys are stored in the fewest possible locations. (CUSTOMIZED APPROACH OBJECTIVE): Cryptographic keys are retained only where necessary. | automatic |
| 3.7.1 | Key-management policies and procedures are implemented to include generation of strong cryptographic keys used to protect stored account data. (CUSTOMIZED APPROACH OBJECTIVE): Strong cryptographic keys are generated. | automatic |
| 3.7.2 | Key-management policies and procedures are implemented to include secure distribution of cryptographic keys used to protect stored account data. (CUSTOMIZED APPROACH OBJECTIVE): Cryptographic keys are secured during distribution. | automatic |
| 3.7.3 | Key-management policies and procedures are implemented to include secure storage of cryptographic keys used to protect stored account data. (CUSTOMIZED APPROACH OBJECTIVE): Cryptographic keys are secured when stored. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [783-255](https://opencre.org/cre/783-255). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
