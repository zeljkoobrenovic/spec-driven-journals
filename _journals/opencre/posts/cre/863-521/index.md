---
id: "CRE-863-521"
title: "Maintain/manage inventory of third party components"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-863-521
excerpt: "CRE 863-521 · in Development processes for security › Supply chain management › Dependency management · 8 mappings to 5 standards and tools."
tags: ASVS, NIST SSDF, OWASP Cheat Sheets, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [863-521](https://opencre.org/cre/863-521)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]] › [[cre-613-286]]
>
> **Maps to**: [[standard-asvs]], [[standard-nist-ssdf]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.2.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v142-dependency) | Verify that a Software Bill of Materials (SBOM) is maintained of all third party libraries in use. | curated |

More: [[standard-asvs]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PS.3.2 | Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials (SBOM)). | curated |

More: [[standard-nist-ssdf]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |
|  | [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C2](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c2-leverage-security-frameworks-libraries.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.3.2 | An inventory of bespoke and custom software, and third-party software components incorporated into bespoke and custom software is maintained to facilitate vulnerability and patch management. (CUSTOMIZED APPROACH OBJECTIVE): Known vulnerabilities in third-party software components cannot be exploited in bespoke and custom software. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 12.5.1 | An inventory of system components that are in scope for PCI DSS, including a description of function/use, is maintained and kept current. (CUSTOMIZED APPROACH OBJECTIVE): All system components in scope for PCI DSS are identified and known. | automatic |
| 12.8.1 | A list of all third-party service providers (TPSPs) with which account data is shared or that could affect the security of account data is maintained, including a description for each of the services provided. (CUSTOMIZED APPROACH OBJECTIVE): Records are maintained of TPSPs and the services provided. (APPLICABILITY NOTES): The use of a PCI DSS compliant TPSP does not make an entity PCI DSS compliant, nor does it remove the entity’s responsibility for its own PCI DSS compliance. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [863-521](https://opencre.org/cre/863-521). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
