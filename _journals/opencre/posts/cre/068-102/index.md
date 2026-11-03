---
id: "CRE-068-102"
title: "Describe high-level system architecture and perform threat modeling on it every critical change and regularly"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-068-102
excerpt: "CRE 068-102 · in Development processes for security › Architecture/design processes · 23 mappings to 8 standards and tools."
tags: ASVS, DevSecOps Maturity Model (DSOMM), NIST 800-53 v5, NIST SSDF, OWASP Cheat Sheets, OWASP Proactive Controls, PCI DSS, SAMM
---
> **CRE**: [068-102](https://opencre.org/cre/068-102)
>
> **Part of**: [[cre-616-305]] › [[cre-326-704]]
>
> **Maps to**: [[standard-asvs]], [[standard-devsecops-maturity-model-dsomm]], [[standard-nist-800-53-v5]], [[standard-nist-ssdf]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]], [[standard-samm]]

## Related CREs

- [[cre-307-242]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.1.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v11-secure-software-development-lifecycle) | Verify definition and security analysis of the application's high-level architecture and all connected remote services. | curated |

More: [[standard-asvs]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0a929c3e-ab9a-4206-8761-adf84b74622e](https://dsomm.owasp.org/activity-description?uuid=0a929c3e-ab9a-4206-8761-adf84b74622e) | Design: Creation of advanced abuse stories | automatic |
| [2a44b708-734f-4463-b0cb-86dc46344b2f](https://dsomm.owasp.org/activity-description?uuid=2a44b708-734f-4463-b0cb-86dc46344b2f) | Deployment: Inventory of production components | automatic |
| [48f97f31-931c-46eb-9b3e-e2fec0cd0426](https://dsomm.owasp.org/activity-description?uuid=48f97f31-931c-46eb-9b3e-e2fec0cd0426) | Design: Conduction of simple threat modeling on business level | automatic |
| [47419324-e263-415b-815d-e7161b6b905e](https://dsomm.owasp.org/activity-description?uuid=47419324-e263-415b-815d-e7161b6b905e) | Design: Conduction of simple threat modeling on technical level | automatic |
| [83057028-0b77-4d2e-8135-40969768ae88](https://dsomm.owasp.org/activity-description?uuid=83057028-0b77-4d2e-8135-40969768ae88) | Deployment: Inventory of production artifacts | automatic |
| [ae22dafd-bcd6-41ee-ba01-8b7fe6fc1ad9](https://dsomm.owasp.org/activity-description?uuid=ae22dafd-bcd6-41ee-ba01-8b7fe6fc1ad9) | Design: Conduction of advanced threat modeling | automatic |
| [bacf85b6-5bc0-405d-b5ba-a5d971467cc1](https://dsomm.owasp.org/activity-description?uuid=bacf85b6-5bc0-405d-b5ba-a5d971467cc1) | Design: Creation of simple abuse stories | automatic |
| [dd5ed7c1-bdbf-400f-b75f-6d3953a1a04e](https://dsomm.owasp.org/activity-description?uuid=dd5ed7c1-bdbf-400f-b75f-6d3953a1a04e) | Design: Creation of threat modeling processes and standards | automatic |
| [f88d1b17-3d7d-4c3d-8139-ad44fc4942d4](https://dsomm.owasp.org/activity-description?uuid=f88d1b17-3d7d-4c3d-8139-ad44fc4942d4) | Education and Guidance: Regular security training of security champions | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-31 Covert Channel Analysis](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-31) | curated |

More: [[standard-nist-800-53-v5]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PW.1.1 | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. | curated |

More: [[standard-nist-ssdf]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html) | curated |
|  | [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C1](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c1-security-requirements.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 5.2.3 | Any system components that are not at risk for malware are evaluated periodically to include the following: () A documented list of all system components not at risk for malware. () Identification and evaluation of evolving malware threats for those system components. () Confirmation whether such system components continue to not require anti-malware protection. (CUSTOMIZED APPROACH OBJECTIVE): The entity maintains awareness of evolving malware threats to ensure that any systems not protected from malware are not at risk of infection. (APPLICABILITY NOTES): System components covered by this requirement are those for which there is no anti-malware solution deployed per Requirement 5.2.1. | automatic |
| 5.2.3.1 | The frequency of periodic evaluations of system components identified as not at risk for malware is defined in the entity’s targeted risk analysis, which is performed according to all elements specified in Requirement 12.3.1. (CUSTOMIZED APPROACH OBJECTIVE): Systems not known to be at risk from malware are re-evaluated at a frequency that addresses the entity’s risk. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 11.3.1 | Internal vulnerability scans are performed as follows: () At least once every three months. () High-risk and critical vulnerabilities (per the entity’s vulnerability risk rankings defined at Requirement 6.3.1) are resolved. () Rescans are performed that confirm all highrisk and critical vulnerabilities (as noted above) have been resolved. () Scan tool is kept up to date with latest vulnerability information. () Scans are performed by qualified personnel and organizational independence of the tester exists. (CUSTOMIZED APPROACH OBJECTIVE): The security posture of all system components is verified periodically using automated tools designed to detect vulnerabilities operating inside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework. (APPLICABILITY NOTES): It is not required to use a QSA or ASV to conduct internal vulnerability scans. Internal vulnerability scans can be performed by qualified, internal staff that are reasonably independent of the system component(s) being scanned (for example, a network administrator should not be responsible for scanning the network), or an entity may choose to have internal vulnerability scans performed by a firm specializing in vulnerability scanning. | automatic |
| 11.3.1.3 | Internal vulnerability scans are performed after any significant change as follows: () High-risk and critical vulnerabilities (per the entity’s vulnerability risk rankings defined at Requirement 6.3.1) are resolved. () Rescans are conducted as needed. () Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV). (CUSTOMIZED APPROACH OBJECTIVE): The security posture of all system components is verified following significant changes to the network or systems, by using automated tools designed to detect vulnerabilities operating inside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework. (APPLICABILITY NOTES): Authenticated internal vulnerability scanning per Requirement 11.3.1.2 is not required for scans performed after significant changes. | automatic |
| 11.3.2.1 | External vulnerability scans are performed after any significant change as follows: () Vulnerabilities that are scored 4.0 or higher by the CVSS are resolved. () Rescans are conducted as needed. () Scans are performed by qualified personnel and organizational independence of the tester exists (not required to be a QSA or ASV). (CUSTOMIZED APPROACH OBJECTIVE): The security posture of all system components is verified following significant changes to the network or systems, by using tools designed to detect vulnerabilities operating from outside the network. Detected vulnerabilities are assessed and rectified based on a formal risk assessment framework. | automatic |
| 12.3.1 | Each PCI DSS requirement that provides flexibility for how frequently it is performed (for example, requirements to be performed periodically) is supported by a targeted risk analysis that is documented and includes: () Identification of the assets being protected. () Identification of the threat(s) that the requirement is protecting against. () Identification of factors that contribute to the likelihood and/or impact of a threat being realized. () Resulting analysis that determines, and includes justification for, how frequently the requirement must be performed to minimize the likelihood of the threat being realized. () Review of each targeted risk analysis at least once every 12 months to determine whether the results are still valid or if an updated risk analysis is needed. () Performance of updated risk analyses when needed, as determined by the annual review. (CUSTOMIZED APPROACH OBJECTIVE): Up to date knowledge and assessment of risks to the CDE are maintained. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [D-TA-B](https://owaspsamm.org/model/design/threat-assessment/stream-b) | Threat modeling | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [068-102](https://opencre.org/cre/068-102). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
