---
id: "CRE-004-517"
title: "Security requirements"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-004-517
excerpt: "CRE 004-517 · in Governance processes for security › Security Analysis and documentation · 1 sub-requirement · 43 mappings to 7 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5, NIST SSDF, PCI DSS, SAMM
---
> **CRE**: [004-517](https://opencre.org/cre/004-517)
>
> **Part of**: [[cre-567-755]] › [[cre-766-162]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-nist-ssdf]], [[standard-pci-dss]], [[standard-samm]]

## Contains

- [[cre-782-234]]

## Related CREs

- [[cre-510-324]]
- [[cre-074-873]]
- [[cre-260-200]]
- [[cre-072-713]]
- [[cre-787-638]]
- [[cre-433-442]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| AIS-02 | Application Security Baseline Requirements | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [00e91a8a-3972-4692-8679-674ab8547486](https://dsomm.owasp.org/activity-description?uuid=00e91a8a-3972-4692-8679-674ab8547486) | Application Hardening: Parametrization | automatic |
| [4cae98c2-4163-44ed-bb88-3c67c569533a](https://dsomm.owasp.org/activity-description?uuid=4cae98c2-4163-44ed-bb88-3c67c569533a) | Application Hardening: App. Hardening Level 3 | automatic |
| [03643ca2-03c2-472b-8e19-956bf02fe9b7](https://dsomm.owasp.org/activity-description?uuid=03643ca2-03c2-472b-8e19-956bf02fe9b7) | Application Hardening: App. Hardening Level 2 (75%) | automatic |
| [b597928e-54d6-48a5-a806-8003dcd56aab](https://dsomm.owasp.org/activity-description?uuid=b597928e-54d6-48a5-a806-8003dcd56aab) | Application Hardening: App. Hardening Level 1 (50%) | automatic |
| [cf819225-30cb-4702-8e32-60225eedc33d](https://dsomm.owasp.org/activity-description?uuid=cf819225-30cb-4702-8e32-60225eedc33d) | Application Hardening: App. Hardening Level 1 | automatic |
| [e1f37abb-d848-4a3a-b3df-65e91a89dcb7](https://dsomm.owasp.org/activity-description?uuid=e1f37abb-d848-4a3a-b3df-65e91a89dcb7) | Application Hardening: Context-aware output encoding | automatic |
| [ffe86caf-2fec-4630-b514-2db83983984d](https://dsomm.owasp.org/activity-description?uuid=ffe86caf-2fec-4630-b514-2db83983984d) | Application Hardening: App. Hardening Level 2 | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 5.14 | Information transfer | curated |
| 8.26 | Application security requirements | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-18 Mobile Code](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-18) | curated |

More: [[standard-nist-800-53-v5]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PO.1.2 | Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time. | curated |

More: [[standard-nist-ssdf]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.1.1 | All security policies and operational procedures that are identified in Requirement 1 are: () Documented. () Kept up to date. () In use. () Known to all affected parties. (CUSTOMIZED APPROACH OBJECTIVE): Expectations, controls, and oversight for meeting activities within Requirement 1 are defined, understood, and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management’s intent. | automatic |
| 1.2.5 | All services, protocols, and ports allowed are identified, approved, and have a defined business need. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized network traffic (services, protocols, or packets destined for specific ports) cannot enter or leave the network. | automatic |
| 1.2.6 | Security features are defined and implemented for all services, protocols, and ports that are in use and considered to be insecure, such that the risk is mitigated. (CUSTOMIZED APPROACH OBJECTIVE): The specific risks associated with the use of insecure services, protocols, and ports are understood, assessed, and appropriately mitigated. | automatic |
| 2.2 | System components are configured and managed securely. | automatic |
| 3.4 | Access to displays of full PAN and ability to copy PAN is restricted. | automatic |
| 3.4.1 | PAN is masked when displayed (the BIN and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN. (CUSTOMIZED APPROACH OBJECTIVE): PAN displays are restricted to the minimum number of digits necessary to meet a defined business need. (APPLICABILITY NOTES): This requirement does not supersede stricter requirements in place for displays of cardholder data—for example, legal or payment brand requirements for point-of-sale (POS) receipts. This requirement relates to protection of PAN where it is displayed on screens, paper receipts, printouts, etc., and is not to be confused with Requirement 3.5.1 for protection of PAN when stored, processed, or transmitted. | automatic |
| 3.5 | Primary account number (PAN) is secured wherever it is stored. | automatic |
| 4.1.1 | All security policies and operational procedures that are identified in Requirement 4 are: () Documented. () Kept up to date. () In use. () Known to all affected parties. (CUSTOMIZED APPROACH OBJECTIVE): Expectations, controls, and oversight for meeting activities within Requirement 4 are defined and adhered to by affected personnel. All supporting activities are repeatable, consistently applied, and conform to management’s intent. | automatic |
| 6.5.5 | Live PANs are not used in pre-production environments, except where those environments are included in the CDE and protected in accordance with all applicable PCI DSS requirements. (CUSTOMIZED APPROACH OBJECTIVE): Live PANs cannot be present in pre-production environments outside the CDE. | automatic |
| 8.2.1 | All users are assigned a unique ID before access to system components or cardholder data is allowed. (CUSTOMIZED APPROACH OBJECTIVE): All actions by all users are attributable to an individual. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts within point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). | automatic |
| 9.3.2 | Procedures are implemented for authorizing and managing visitor access to the CDE, including: () Visitors are authorized before entering. () Visitors are escorted at all times. () Visitors are clearly identified and given a badge or other identification that expires. () Visitor badges or other identification visibly distinguishes visitors from personnel. (CUSTOMIZED APPROACH OBJECTIVE): Requirements for visitor access to the CDE are defined and enforced. Visitors cannot exceed any authorized physical access allowed while in the CDE. | automatic |
| 9.3.3 | Visitor badges or identification are surrendered or deactivated before visitors leave the facility or at the date of expiration. (CUSTOMIZED APPROACH OBJECTIVE): Visitor identification or badges cannot be reused after expiration. | automatic |
| 9.4.1 | All media with cardholder data is physically secured. (CUSTOMIZED APPROACH OBJECTIVE): Media with cardholder data cannot be accessed by unauthorized personnel. | automatic |
| 9.5.1.1 | An up-to-date list of POI devices is maintained, including: () Make and model of the device. () Location of device. () Device serial number or other methods of unique identification. (CUSTOMIZED APPROACH OBJECTIVE): The identity and location of POI devices is recorded and known at all times. | automatic |
| 10.4.1.1 | Automated mechanisms are used to perform audit log reviews. (CUSTOMIZED APPROACH OBJECTIVE): Potentially suspicious or anomalous activities are identified via a repeatable and consistent mechanism. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 10.7.1 | Additional requirement for service providers only: Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems: () Network security controls. () IDS/IPS. () FIM. () Anti-malware solutions. () Physical access controls. () Logical access controls. () Audit logging mechanisms. () Segmentation controls (if used). (CUSTOMIZED APPROACH OBJECTIVE): Failures in critical security control systems are promptly identified and addressed. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. This requirement will be superseded by Requirement 10.7.2 as of 31 March 2025. | automatic |
| 10.7.2 | Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of the following critical security control systems: () Network security controls. () IDS/IPS. () Change-detection mechanisms. () Anti-malware solutions. () Physical access controls. () Logical access controls. () Audit logging mechanisms. () Segmentation controls (if used). () Audit log review mechanisms. () Automated security testing tools (if used). (CUSTOMIZED APPROACH OBJECTIVE): Failures in critical security control systems are promptly identified and addressed. (APPLICABILITY NOTES): This requirement applies to all entities, including service providers, and will supersede Requirement 10.7.1 as of 31 March 2025. It includes two additional critical security control systems not in Requirement 10.7.1. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 10.7.3 | Failures of any critical security controls systems are responded to promptly, including but not limited to: () Restoring security functions. () Identifying and documenting the duration (date and time from start to end) of the security failure. () Identifying and documenting the cause(s) of failure and documenting required remediation. () Identifying and addressing any security issues that arose during the failure. () Determining whether further actions are required as a result of the security failure. () Implementing controls to prevent the cause of failure from reoccurring. () Resuming monitoring of security controls. (CUSTOMIZED APPROACH OBJECTIVE): Failures of critical security control systems are analyzed, contained, and resolved, and security controls restored to minimize impact. Resulting security issues are addressed, and measures taken to prevent reoccurrence. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider until 31 March 2025, after which this requirement will apply to all entities. This is a current v3.2.1 requirement that applies to service providers only. However, this requirement is a best practice for all other entities until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 11.6 | Unauthorized changes on payment pages are detected and responded to. | automatic |
| 12.3.2 | A targeted risk analysis is performed for each PCI DSS requirement that the entity meets with the customized approach, to include: () Documented evidence detailing each element specified in Appendix | automatic |
| 12.5 | PCI DSS scope is documented and validated. | automatic |
| A1.2.3 | Processes or mechanisms are implemented for reporting and addressing suspected or confirmed security incidents and vulnerabilities, including: () Customers can securely report security incidents and vulnerabilities to the provider. () The provider addresses and remediates suspected or confirmed security incidents and vulnerabilities according to Requirement 6.3.1. (CUSTOMIZED APPROACH OBJECTIVE): Suspected or confirmed security incidents or vulnerabilities are discovered and addressed. Customers are informed where appropriate. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. Requirements in this Appendix are not eligible for the Customized Approach. | automatic |
| A2.1 | POI terminals using SSL and/or early TLS are confirmed as not susceptible to known SSL/TLS exploits. | automatic |
| A2.1.1 | Where POS POI terminals at the merchant or payment acceptance location use SSL and/or early TLS, the entity confirms the devices are not susceptible to any known exploits for those protocols. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): This requirement is intended to apply to the entity with the POS POI terminal, such as a merchant. This requirement is not intended for service providers who serve as the termination or connection point to those POS POI terminals. Requirements A2.1.2 and A2.1.3 apply to POS POI service providers. The allowance for POS POI terminals that are not currently susceptible to exploits is based on currently known risks. If new exploits are introduced to which POS POI terminals are susceptible, the POS POI terminals will need to be updated immediately. | automatic |
| A2.1.3 | Additional requirement for service providers only: All service providers provide a secure service offering. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. | automatic |
| A3.2 | PCI DSS scope is documented and validated. | automatic |
| A3.3.1 | Failures of critical security control systems are detected, alerted, and addressed promptly, including but not limited to failure of: () Network security controls () IDS/IPS () FIM () Anti-malware solutions () Physical access controls () Logical access controls () Audit logging mechanisms () Segmentation controls (if used) () Automated audit log review mechanisms. This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. () Automated code review tools (if used). This bullet is a best practice until its effective date; refer to (APPLICABILITY NOTES): below for details. PCI DSS Reference: Requirements 1-12 (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): The bullets above (for automated log review mechanisms and automated code review tools (if used)) are best practices until 31 March 2025, after which they will be required as part of Requirement A3.3.1 and must be fully considered during a PCI DSS assessment. | automatic |
| A3.3.1.2 | Failures of any critical security control systems are responded to promptly. Processes for responding to failures in security control systems include: () Restoring security functions. () Identifying and documenting the duration (date and time from start to end) of the security failure. () Identifying and documenting the cause(s) of failure, including root cause, and documenting remediation required to address the root cause. () Identifying and addressing any security issues that arose during the failure. () Determining whether further actions are required as a result of the security failure. () Implementing controls to prevent the cause of failure from reoccurring. () Resuming monitoring of security controls. PCI DSS Reference: Requirements 1-12 (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. | automatic |
| A3.5 | Suspicious events are identified and responded to. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [D-SR-A](https://owaspsamm.org/model/design/security-requirements/stream-a) | Software Requirements | curated |
| [G-PC-A](https://owaspsamm.org/model/governance/policy-and-compliance/stream-a/) | Policy & Standards | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [004-517](https://opencre.org/cre/004-517). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
