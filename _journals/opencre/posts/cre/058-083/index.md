---
id: "CRE-058-083"
title: "Monitoring"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-058-083
excerpt: "CRE 058-083 · in Operating processes for security › Detect and respond · 27 mappings to 6 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5, PCI DSS, SAMM
---
> **CRE**: [058-083](https://opencre.org/cre/058-083)
>
> **Part of**: [[cre-862-452]] › [[cre-887-750]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-pci-dss]], [[standard-samm]]

## Related CREs

- [[cre-842-876]]
- [[cre-176-154]]
- [[cre-418-853]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| LOG | Logging and Monitoring | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [1cd5e4b8-be36-4726-adc7-d8f843f47ac8](https://dsomm.owasp.org/activity-description?uuid=1cd5e4b8-be36-4726-adc7-d8f843f47ac8) | Monitoring: Audit of system events | automatic |
| [3d1f4c3b-f713-46d9-933a-54a014a26c03](https://dsomm.owasp.org/activity-description?uuid=3d1f4c3b-f713-46d9-933a-54a014a26c03) | Monitoring: Simple system metrics | automatic |
| [4eced38a-7904-4c45-adb0-50b663065540](https://dsomm.owasp.org/activity-description?uuid=4eced38a-7904-4c45-adb0-50b663065540) | Logging: Centralized system logging | automatic |
| [7c735089-6a83-419f-8b27-c1e676cedea1](https://dsomm.owasp.org/activity-description?uuid=7c735089-6a83-419f-8b27-c1e676cedea1) | Logging: Visualized logging | automatic |
| [7f36b9ba-bc05-4fd6-9a2a-73344c249722](https://dsomm.owasp.org/activity-description?uuid=7f36b9ba-bc05-4fd6-9a2a-73344c249722) | Monitoring: Deactivation of unused metrics | automatic |
| [8a442d8e-0eb1-4793-a513-571aef982edd](https://dsomm.owasp.org/activity-description?uuid=8a442d8e-0eb1-4793-a513-571aef982edd) | Monitoring: Alerting | automatic |
| [10e23a8c-22ff-4487-a706-87ccc9d0798e](https://dsomm.owasp.org/activity-description?uuid=10e23a8c-22ff-4487-a706-87ccc9d0798e) | Monitoring: Monitoring of costs | automatic |
| [42170a71-d4c8-47af-bd71-bf36875fd05b](https://dsomm.owasp.org/activity-description?uuid=42170a71-d4c8-47af-bd71-bf36875fd05b) | Monitoring: Grouping of metrics | automatic |
| [71699daf-b2a4-466b-a0b2-89f7dbb18506](https://dsomm.owasp.org/activity-description?uuid=71699daf-b2a4-466b-a0b2-89f7dbb18506) | Monitoring: Metrics are combined with tests | automatic |
| [8746647c-638c-473f-8e17-82c068e4c311](https://dsomm.owasp.org/activity-description?uuid=8746647c-638c-473f-8e17-82c068e4c311) | Monitoring: Screens with metric visualization | automatic |
| [b217c8bb-5d61-4b41-a675-1083993f83b1](https://dsomm.owasp.org/activity-description?uuid=b217c8bb-5d61-4b41-a675-1083993f83b1) | Logging: Analyze logs | automatic |
| [ccf4561d-253f-4762-adcb-bc4622fd6fc5](https://dsomm.owasp.org/activity-description?uuid=ccf4561d-253f-4762-adcb-bc4622fd6fc5) | Logging: Correlation of security events | automatic |
| [ccfdd0a8-991e-4269-ad77-c0a54ca655cb](https://dsomm.owasp.org/activity-description?uuid=ccfdd0a8-991e-4269-ad77-c0a54ca655cb) | Logging: Logging of security events | automatic |
| [d0d681e7-d6de-4829-ac64-a9eb2546aa0d](https://dsomm.owasp.org/activity-description?uuid=d0d681e7-d6de-4829-ac64-a9eb2546aa0d) | Monitoring: Coverage and control metrics | automatic |
| [d03bc410-74a7-4e92-82cb-d01a020cb6bf](https://dsomm.owasp.org/activity-description?uuid=d03bc410-74a7-4e92-82cb-d01a020cb6bf) | Monitoring: Advanced app. metrics | automatic |
| [d6f06ae8-401a-4f44-85df-1079247fa030](https://dsomm.owasp.org/activity-description?uuid=d6f06ae8-401a-4f44-85df-1079247fa030) | Monitoring: Targeted alerting | automatic |
| [ded39bcf-4eaa-4c5f-9c94-09acde0a4734](https://dsomm.owasp.org/activity-description?uuid=ded39bcf-4eaa-4c5f-9c94-09acde0a4734) | Monitoring: Visualized metrics | automatic |
| [e9a6d403-a467-445e-b98a-74f0c29da0b1](https://dsomm.owasp.org/activity-description?uuid=e9a6d403-a467-445e-b98a-74f0c29da0b1) | Monitoring: Simple application metrics | automatic |
| [e808028c-351c-42f1-bcd9-fba738d1fc55](https://dsomm.owasp.org/activity-description?uuid=e808028c-351c-42f1-bcd9-fba738d1fc55) | Monitoring: Defense metrics | automatic |
| [ed715b38-c34b-40cd-83fd-ce807f306fc1](https://dsomm.owasp.org/activity-description?uuid=ed715b38-c34b-40cd-83fd-ce807f306fc1) | Monitoring: Advanced availability and stability metrics | automatic |
| [f08a3219-6941-43ec-8762-4aff739f4664](https://dsomm.owasp.org/activity-description?uuid=f08a3219-6941-43ec-8762-4aff739f4664) | Monitoring: Simple budget metrics | automatic |
| [fe875e17-ae4a-45f8-a359-244aa4fcbc04](https://dsomm.owasp.org/activity-description?uuid=fe875e17-ae4a-45f8-a359-244aa4fcbc04) | Logging: Centralized application logging | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.16 | Monitoring activities | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SI-4 System Monitoring](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SI-4) | curated |

More: [[standard-nist-800-53-v5]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 12.8.4 | A program is implemented to monitor TPSPs’ PCI DSS compliance status at least once every 12 months. (CUSTOMIZED APPROACH OBJECTIVE): The PCI DSS compliance status of TPSPs is verified periodically. (APPLICABILITY NOTES): Where an entity has an agreement with a TPSP for meeting PCI DSS requirements on behalf of the entity (for example, via a firewall service), the entity must work with the TPSP to make sure the applicable PCI DSS requirements are met. If the TPSP does not meet those applicable PCI DSS requirements, then those requirements are also “not in place” for the entity. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [O-IM-A](https://owaspsamm.org/model/operations/incident-management/stream-a) | Incident Detection | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [058-083](https://opencre.org/cre/058-083). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
