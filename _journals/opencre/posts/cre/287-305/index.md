---
id: "CRE-287-305"
title: "Document explicit key/secret management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-287-305
excerpt: "CRE 287-305 · in Development processes for security › Technical system documentation · 10 mappings to 3 standards and tools."
tags: ASVS, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [287-305](https://opencre.org/cre/287-305)
>
> **Part of**: [[cre-616-305]] › [[cre-820-877]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Related CREs

- [[cre-223-780]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.6.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v16-cryptographic-architecture) | Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57. | curated |

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
| 3.5.1.3 | If disk-level or partition-level encryption is used (rather than file-, column-, or field--level database encryption) to render PAN unreadable, it is managed as follows: () Logical access is managed separately and independently of native operating system authentication and access control mechanisms. () Decryption keys are not associated with user accounts. () Authentication factors (passwords, passphrases, or cryptographic keys) that allow access to unencrypted data are stored securely. (CUSTOMIZED APPROACH OBJECTIVE): Disk encryption implementations are configured to require independent authentication and logical access controls for decryption. (APPLICABILITY NOTES): Disk or partition encryption implementations must also meet all other PCI DSS encryption and keymanagement requirements. | automatic |
| 3.7 | Where cryptography is used to protect stored account data, key management processes and procedures covering all aspects of the key lifecycle are defined and implemented. | automatic |
| 3.7.4 | Key management policies and procedures are implemented for cryptographic key changes for keys that have reached the end of their cryptoperiod, as defined by the associated application vendor or key owner, and based on industry best practices and guidelines, including the following: () A defined cryptoperiod for each key type in use. () A process for key changes at the end of the defined cryptoperiod. (CUSTOMIZED APPROACH OBJECTIVE): Cryptographic keys are not used beyond their defined cryptoperiod. | automatic |
| 3.7.6 | Where manual cleartext cryptographic keymanagement operations are performed by personnel, key-management policies and procedures are implemented include managing these operations using split knowledge and dual control. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext secret or private keys cannot be known by anyone. Operations involving cleartext keys cannot be carried out by a single person. (APPLICABILITY NOTES): This control is applicable for manual keymanagement operations or where key management is not controlled by the encryption product. A cryptographic key that is simply split into two parts does not meet this requirement. Secret or private keys stored as key components or key shares must be generated via one of the following: () Using an approved random number generator and within a secure cryptographic device (SCD), such as a hardware security module (HSM) or PTS-approved point-of-interaction device, OR () According to ISO 19592 or equivalent industry standard for generation of secret key shares. | automatic |
| 3.7.7 | Key management policies and procedures are implemented to include the prevention of unauthorized substitution of cryptographic keys. (CUSTOMIZED APPROACH OBJECTIVE): Cryptographic keys cannot be substituted by unauthorized personnel. | automatic |
| 3.7.8 | Key management policies and procedures are implemented to include that cryptographic key custodians formally acknowledge (in writing or electronically) that they understand and accept their key-custodian responsibilities. (CUSTOMIZED APPROACH OBJECTIVE): Key custodians are knowledgeable about their responsibilities in relation to cryptographic operations and can access assistance and guidance when required. | automatic |
| 3.7.9 | Additional requirement for service providers only: Where a service provider shares cryptographic keys with its customers for transmission or storage of account data, guidance on secure transmission, storage and updating of such keys is documented and distributed to the service provider’s customers. (CUSTOMIZED APPROACH OBJECTIVE): Customers are provided with appropriate key management guidance whenever they receive shared cryptographic keys. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [287-305](https://opencre.org/cre/287-305). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
