---
id: "CRE-742-431"
title: "Use approved cryptographic algorithms"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-742-431
excerpt: "CRE 742-431 · in Technical application security controls › Secure data storage › Encrypt data at rest › Encryption algorithms · 29 mappings to 8 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), PCI DSS, ZAP Rule
---
> **CRE**: [742-431](https://opencre.org/cre/742-431)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]] › [[cre-742-432]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V6.2.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x14-V6-Cryptography.md#v62-algorithms) | Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [97](https://capec.mitre.org/data/definitions/97.html) | Cryptanalysis | automatic |
| [459](https://capec.mitre.org/data/definitions/459.html) | Creating a Rogue Certification Authority Certificate | automatic |
| [473](https://capec.mitre.org/data/definitions/473.html) | Signature Spoof | automatic |
| [475](https://capec.mitre.org/data/definitions/475.html) | Signature Spoofing by Improper Validation | automatic |
| [608](https://capec.mitre.org/data/definitions/608.html) | Cryptanalysis of Cellular Encryption | automatic |
| [614](https://capec.mitre.org/data/definitions/614.html) | Rooting SIM Cards | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [327](https://cwe.mitre.org/data/definitions/327.html) | Use of a Broken or Risky Cryptographic Algorithm | curated |
| [325](https://cwe.mitre.org/data/definitions/325.html) | Missing Cryptographic Step | automatic |
| [328](https://cwe.mitre.org/data/definitions/328.html) | Use of Weak Hash | automatic |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |
| [780](https://cwe.mitre.org/data/definitions/780.html) | Use of RSA Algorithm without OAEP | automatic |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | automatic |
| [1240](https://cwe.mitre.org/data/definitions/1240.html) | Use of a Cryptographic Primitive with a Risky Implementation | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | curated |
|  | [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C8](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c8-protect-data-everywhere.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.3.2 | SAD that is stored electronically prior to completion of authorization is encrypted using strong cryptography. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): Whether SAD is permitted to be stored prior to authorization is determined by the organizations that manage compliance programs (for example, payment brands and acquirers). Contact the organizations of interest for any additional criteria. This requirement applies to all storage of SAD, even if no PAN is present in the environment. Refer to Requirement 3.2.1 for an additional requirement that applies if SAD is stored prior to completion of authorization. This requirement does not apply to issuers and companies that support issuing services where there is a legitimate issuing business justification to store SAD). Refer to Requirement 3.3.3 for requirements specifically for issuers. This requirement does not replace how PIN blocks are required to be managed, nor does it mean that a properly encrypted PIN block needs to be encrypted again. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 3.6.1.1 | Additional requirement for service providers only: A documented description of the cryptographic architecture is maintained that includes: () Details of all algorithms, protocols, and keys used for the protection of stored account data, including key strength and expiry date. () Preventing the use of the same cryptographic keys in production and test environments. This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. () Description of the key usage for each key. () Inventory of any hardware security modules (HSMs), key management systems (KMS), and other secure cryptographic devices (SCDs) used for key management, including type and location of devices, as outlined in Requirement 12.3.4. (CUSTOMIZED APPROACH OBJECTIVE): Accurate details of the cryptographic architecture are maintained and available. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. In cloud HSM implementations, responsibility for the cryptographic architecture according to this Requirement will be shared between the cloud provider and the cloud customer. The bullet above (for including, in the cryptographic architecture, that the use of the same cryptographic keys in production and test is prevented) is a best practice until 31 March 2025, after which it will be required as part of Requirement 3.6.1.1 and must be fully considered during a PCI DSS assessment. | automatic |
| 4.2 | PAN is protected with strong cryptography during transmission. | automatic |
| 4.2.1 | Strong cryptography and security protocols are implemented as follows to safeguard PAN during transmission over open, public networks: () Only trusted keys and certificates are accepted. () Certificates used to safeguard PAN during transmission over open, public networks are confirmed as valid and are not expired or revoked. This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. () The protocol in use supports only secure versions or configurations and does not support fallback to, or use of insecure versions, algorithms, key sizes, or implementations. () The encryption strength is appropriate for the encryption methodology in use. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext PAN cannot be read or intercepted from any transmissions over open, public networks. (APPLICABILITY NOTES): There could be occurrences where an entity receives cardholder data unsolicited via an insecure communication channel that was not intended for the purpose of receiving sensitive data. In this situation, the entity can choose to either include the channel in the scope of their CDE and secure it according to PCI DSS or implement measures to prevent the channel from being used for cardholder data. A self-signed certificate may also be acceptable if the certificate is issued by an internal CA within the organization, the certificate’s author is confirmed, and the certificate is verified—for example, via hash or signature—and has not expired. Note that selfsigned certificates where the Distinguished Name (DN) field in the “issued by” and “issued to” field is the same are not acceptable. The bullet above (for confirming that certificates used to safeguard PAN during transmission over open, public networks are valid and are not expired or revoked) is a best practice until 31 March 2025, after which it will be required as part of Requirement 4.2.1 and must be fully considered during a PCI DSS assessment. | automatic |
| 4.2.1.2 | Wireless networks transmitting PAN or connected to the CDE use industry best practices to implement strong cryptography for authentication and transmission. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext PAN cannot be read or intercepted from wireless network transmissions. | automatic |
| 8.3.2 | Strong cryptography is used to render all authentication factors unreadable during transmission and storage on all system components. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext authentication factors cannot be obtained, derived, or reused from the interception of communications or from stored data. | automatic |
| 12.3.3 | Cryptographic cipher suites and protocols in use are documented and reviewed at least once every 12 months, including at least the following: () An up-to-date inventory of all cryptographic cipher suites and protocols in use, including purpose and where used. () Active monitoring of industry trends regarding continued viability of all cryptographic cipher suites and protocols in use. () A documented strategy to respond to anticipated changes in cryptographic vulnerabilities. (CUSTOMIZED APPROACH OBJECTIVE): The entity is able to respond quickly to any vulnerabilities in cryptographic protocols or algorithms, where those vulnerabilities affect protection of cardholder data. (APPLICABILITY NOTES): The requirement applies to all cryptographic suites and protocols used to meet PCI DSS requirements. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100010](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20Hashes.js) | Information Disclosure - Hash | automatic |
| [100021](https://github.com/zaproxy/community-scripts/blob/main/passive/Telerik%20Using%20Poor%20Crypto.js) | Telerik UI for ASP.NET AJAX Cryptographic Weakness (CVE-2017-9248) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [742-431](https://opencre.org/cre/742-431). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
