---
id: "CRE-433-442"
title: "Verification"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-433-442
excerpt: "CRE 433-442 · in Development processes for security · 5 sub-requirements · 68 mappings to 7 standards and tools."
tags: Cloud Controls Matrix, DevSecOps Maturity Model (DSOMM), ISO 27001, NIST 800-53 v5, NIST SSDF, PCI DSS, SAMM
---
> **CRE**: [433-442](https://opencre.org/cre/433-442)
>
> **Part of**: [[cre-616-305]]
>
> **Maps to**: [[standard-cloud-controls-matrix]], [[standard-devsecops-maturity-model-dsomm]], [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-nist-ssdf]], [[standard-pci-dss]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n616305["Development processes for security"] --> n433442["Verification"]
  n433442 --> n364516["AI security assurance & validation"]
  n433442 --> n832555["Automated static security analysis of code an…"]
  n433442 --> n626250["Design review"]
  n433442 --> n207435["Dynamic security testing"]
  n433442 --> n411684["Manual code review"]
  style n433442 stroke-width:3px
---end mermaid---

## Contains

- [[cre-364-516]] — 9 more below
- [[cre-832-555]] — 1 more below
- [[cre-626-250]]
- [[cre-207-435]] — 2 more below
- [[cre-411-684]]

## Related CREs

- [[cre-464-513]]
- [[cre-004-517]]
- [[cre-613-285]]
- [[cre-732-148]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| AIS-05 | Automated Application Security Testing | curated |
| STA | Supply Chain Management, Transparency, and Accountability | curated |

More: [[standard-cloud-controls-matrix]]

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0a929c3e-ab9a-4206-8761-adf84b74622e](https://dsomm.owasp.org/activity-description?uuid=0a929c3e-ab9a-4206-8761-adf84b74622e) | Design: Creation of advanced abuse stories | automatic |
| [0cb2c39a-3cec-4353-b3ab-8d70daf4c9d2](https://dsomm.owasp.org/activity-description?uuid=0cb2c39a-3cec-4353-b3ab-8d70daf4c9d2) | Static depth for applications: Test for Patch Deployment Time | automatic |
| [1bd78cdd-ef11-4bb5-9b58-5af2e25fe1c5](https://dsomm.owasp.org/activity-description?uuid=1bd78cdd-ef11-4bb5-9b58-5af2e25fe1c5) | Test Intensity: Deactivating of unneeded tests | automatic |
| [2ebfc421-8c76-415c-a3b0-fa518915bd10](https://dsomm.owasp.org/activity-description?uuid=2ebfc421-8c76-415c-a3b0-fa518915bd10) | Test Intensity: High test intensity | automatic |
| [5b5a1eb2-113f-41fb-a3d6-06af4fdc9cea](https://dsomm.owasp.org/activity-description?uuid=5b5a1eb2-113f-41fb-a3d6-06af4fdc9cea) | Dynamic depth for applications: Usage of multiple scanners | automatic |
| [5e0ff85b-ec89-4ef0-96b1-5695fa0025dc](https://dsomm.owasp.org/activity-description?uuid=5e0ff85b-ec89-4ef0-96b1-5695fa0025dc) | Dynamic depth for applications: Coverage of more input vectors | automatic |
| [6a9cb303-0f98-48a8-bdcd-56d41c0012b8](https://dsomm.owasp.org/activity-description?uuid=6a9cb303-0f98-48a8-bdcd-56d41c0012b8) | Dynamic depth for applications: Coverage of hidden endpoints | automatic |
| [6c05c837-8c99-46e2-828b-7c903e27dba4](https://dsomm.owasp.org/activity-description?uuid=6c05c837-8c99-46e2-828b-7c903e27dba4) | Static depth for applications: Static analysis for important server side components | automatic |
| [6d2c3ac6-8afc-4af6-a5e9-6188341aca01](https://dsomm.owasp.org/activity-description?uuid=6d2c3ac6-8afc-4af6-a5e9-6188341aca01) | Dynamic depth for infrastructure: Test network segmentation | automatic |
| [6e180abc-7c98-4265-b4e9-852cb91b067b](https://dsomm.owasp.org/activity-description?uuid=6e180abc-7c98-4265-b4e9-852cb91b067b) | Static depth for applications: Local development security checks performed | automatic |
| [7bb70764-9392-4462-935d-e55b2e148199](https://dsomm.owasp.org/activity-description?uuid=7bb70764-9392-4462-935d-e55b2e148199) | Dynamic depth for infrastructure: Test of the configuration of cloud environments | automatic |
| [7de0ae33-6538-45cd-8222-a1475647ba58](https://dsomm.owasp.org/activity-description?uuid=7de0ae33-6538-45cd-8222-a1475647ba58) | Static depth for infrastructure: Correlate known vulnerabilities in infrastructure with new image versions | automatic |
| [07fe8c4f-ae33-4409-b1b2-cf64cfccea86](https://dsomm.owasp.org/activity-description?uuid=07fe8c4f-ae33-4409-b1b2-cf64cfccea86) | Static depth for applications: Software Composition Analysis (client side) | automatic |
| [8fc3de67-7b8d-420b-8d24-f35928cfed6e](https://dsomm.owasp.org/activity-description?uuid=8fc3de67-7b8d-420b-8d24-f35928cfed6e) | Static depth for infrastructure: Test the definition of virtualized environments | automatic |
| [13af1227-3dd1-4d4f-a9e9-53deb793c18f](https://dsomm.owasp.org/activity-description?uuid=13af1227-3dd1-4d4f-a9e9-53deb793c18f) | Static depth for applications: Test for Time to Patch | automatic |
| [017d9e26-42b5-49a4-b945-9f59b308fb99](https://dsomm.owasp.org/activity-description?uuid=017d9e26-42b5-49a4-b945-9f59b308fb99) | Static depth for applications: API design validation | automatic |
| [22aab0ef-76ce-4b8c-979c-3699784330db](https://dsomm.owasp.org/activity-description?uuid=22aab0ef-76ce-4b8c-979c-3699784330db) | Dynamic depth for applications: Coverage of service to service communication | automatic |
| [26e1c6d5-5632-4ec7-80d2-e564b98732ad](https://dsomm.owasp.org/activity-description?uuid=26e1c6d5-5632-4ec7-80d2-e564b98732ad) | Static depth for infrastructure: Software Composition Analysis | automatic |
| [46d6a2a8-f9dc-4c15-9fc8-1723cfecbddc](https://dsomm.owasp.org/activity-description?uuid=46d6a2a8-f9dc-4c15-9fc8-1723cfecbddc) | Static depth for infrastructure: Test the cloud configuration | automatic |
| [61e10f9c-e126-4ffa-af12-fdbe0d0a831f](https://dsomm.owasp.org/activity-description?uuid=61e10f9c-e126-4ffa-af12-fdbe0d0a831f) | Dynamic depth for infrastructure: Weak password test | automatic |
| [65a2d7d9-5441-46bf-a4e3-f76919857750](https://dsomm.owasp.org/activity-description?uuid=65a2d7d9-5441-46bf-a4e3-f76919857750) | Dynamic depth for applications: Usage of different roles | automatic |
| [73aaae0b-5d68-4953-9fa4-fd25bf665f2a](https://dsomm.owasp.org/activity-description?uuid=73aaae0b-5d68-4953-9fa4-fd25bf665f2a) | Application tests: Smoke Test | automatic |
| [79ef8103-e1ed-4055-8df8-fd2b2015bebe](https://dsomm.owasp.org/activity-description?uuid=79ef8103-e1ed-4055-8df8-fd2b2015bebe) | Test Intensity: Creation and application of a testing concept | automatic |
| [87b54313-fafd-4860-930f-5ef132b3e4ad](https://dsomm.owasp.org/activity-description?uuid=87b54313-fafd-4860-930f-5ef132b3e4ad) | Static depth for applications: Test libyear | automatic |
| [297be001-8d94-41ee-ab29-207020d423c0](https://dsomm.owasp.org/activity-description?uuid=297be001-8d94-41ee-ab29-207020d423c0) | Static depth for applications: Usage of multiple analyzers | automatic |
| [517b0957-4981-4ac0-b4c7-0d8d1934c474](https://dsomm.owasp.org/activity-description?uuid=517b0957-4981-4ac0-b4c7-0d8d1934c474) | Development and Source Control: Local development linting & style checks performed | automatic |
| [621fb6a5-5c0a-4408-826a-068868bb031b](https://dsomm.owasp.org/activity-description?uuid=621fb6a5-5c0a-4408-826a-068868bb031b) | Static depth for infrastructure: Test cluster deployment resources | automatic |
| [837f8f90-adc2-4e6b-9ebb-60c2ee29494d](https://dsomm.owasp.org/activity-description?uuid=837f8f90-adc2-4e6b-9ebb-60c2ee29494d) | Static depth for infrastructure: Test for malware | automatic |
| [845f06ec-148c-4c67-9755-7041911dcca5](https://dsomm.owasp.org/activity-description?uuid=845f06ec-148c-4c67-9755-7041911dcca5) | Dynamic depth for applications: Coverage of sequential operations | automatic |
| [6532c1fe-9d23-4228-8722-558ddabca7d4](https://dsomm.owasp.org/activity-description?uuid=6532c1fe-9d23-4228-8722-558ddabca7d4) | Dynamic depth for infrastructure: Test for unused Resources | automatic |
| [7121b0c7-6ace-4d6b-95d0-94535dbccb57](https://dsomm.owasp.org/activity-description?uuid=7121b0c7-6ace-4d6b-95d0-94535dbccb57) | Education and Guidance: Security code review | automatic |
| [9711f871-f79d-4573-8d4f-d2c98fd0d18e](https://dsomm.owasp.org/activity-description?uuid=9711f871-f79d-4573-8d4f-d2c98fd0d18e) | Dynamic depth for applications: Coverage of client side dynamic components | automatic |
| [13367d8f-e37f-4197-a610-9ffca4fde261](https://dsomm.owasp.org/activity-description?uuid=13367d8f-e37f-4197-a610-9ffca4fde261) | Static depth for infrastructure: Test of infrastructure components for known vulnerabilities | automatic |
| [58825d22-1ce6-4748-af81-0ec9956e4129](https://dsomm.owasp.org/activity-description?uuid=58825d22-1ce6-4748-af81-0ec9956e4129) | Static depth for infrastructure: Test of virtualized environments | automatic |
| [67667c97-c33e-4306-a4e5-e7b1d8e10c5a](https://dsomm.owasp.org/activity-description?uuid=67667c97-c33e-4306-a4e5-e7b1d8e10c5a) | Application tests: High coverage of security related module and integration tests | automatic |
| [598897a2-358e-441f-984c-e12ec4f6110a](https://dsomm.owasp.org/activity-description?uuid=598897a2-358e-441f-984c-e12ec4f6110a) | Test Intensity: Regular automated tests | automatic |
| [07796811-37f9-467c-9ff2-48f346e77ff3](https://dsomm.owasp.org/activity-description?uuid=07796811-37f9-467c-9ff2-48f346e77ff3) | Dynamic depth for applications: Simple Scan | automatic |
| [a6c4cefb-a0b7-4787-8cc7-a0f96b4b00d8](https://dsomm.owasp.org/activity-description?uuid=a6c4cefb-a0b7-4787-8cc7-a0f96b4b00d8) | Dynamic depth for infrastructure: Test for exposed services | automatic |
| [a8d7d1f1-fc24-49ab-8fb6-f3a03da9c61d](https://dsomm.owasp.org/activity-description?uuid=a8d7d1f1-fc24-49ab-8fb6-f3a03da9c61d) | Static depth for applications: Dead code elimination | automatic |
| [ab0a4b51-3b18-43f1-a6fc-a98e4b28453d](https://dsomm.owasp.org/activity-description?uuid=ab0a4b51-3b18-43f1-a6fc-a98e4b28453d) | Test Intensity: Default settings for intensity | automatic |
| [c6e3c812-56e2-41b0-ae01-b7afc41a004c](https://dsomm.owasp.org/activity-description?uuid=c6e3c812-56e2-41b0-ae01-b7afc41a004c) | Static depth for infrastructure: Test for stored secrets in code | automatic |
| [cb6321aa-0fbf-4996-9e08-05ab26ef4c1e](https://dsomm.owasp.org/activity-description?uuid=cb6321aa-0fbf-4996-9e08-05ab26ef4c1e) | Static depth for infrastructure: Test for new image version | automatic |
| [d0ba0be5-c573-405f-b905-b7a8f87a9cc7](https://dsomm.owasp.org/activity-description?uuid=d0ba0be5-c573-405f-b905-b7a8f87a9cc7) | Dynamic depth for applications: Coverage analysis | automatic |
| [d5e6303c-d5c6-4d59-b258-a3b9de38a07f](https://dsomm.owasp.org/activity-description?uuid=d5e6303c-d5c6-4d59-b258-a3b9de38a07f) | Static depth for infrastructure: Test for stored secrets in build artifacts | automatic |
| [d17dbff0-1f10-492a-b4c7-17bb59a0a711](https://dsomm.owasp.org/activity-description?uuid=d17dbff0-1f10-492a-b4c7-17bb59a0a711) | Static depth for applications: Exclusion of source code duplicates | automatic |
| [d918cd44-a972-43e9-a974-eff3f4a5dcfe](https://dsomm.owasp.org/activity-description?uuid=d918cd44-a972-43e9-a974-eff3f4a5dcfe) | Static depth for applications: Software Composition Analysis (server side) | automatic |
| [ddfe7c3c-b7a4-4cba-9041-b044d4a34e5b](https://dsomm.owasp.org/activity-description?uuid=ddfe7c3c-b7a4-4cba-9041-b044d4a34e5b) | Static depth for infrastructure: Test for image lifetime | automatic |
| [e237176b-bec5-447d-a926-e37d6dd60e4b](https://dsomm.owasp.org/activity-description?uuid=e237176b-bec5-447d-a926-e37d6dd60e4b) | Static depth for applications: Static analysis for important client side components | automatic |
| [eb2c7f9d-d0bd-4253-a2ba-cff2ace4a075](https://dsomm.owasp.org/activity-description?uuid=eb2c7f9d-d0bd-4253-a2ba-cff2ace4a075) | Application tests: Security unit tests for important components | automatic |
| [ee68331f-9b1d-4f61-844b-b2ea04753a84](https://dsomm.owasp.org/activity-description?uuid=ee68331f-9b1d-4f61-844b-b2ea04753a84) | Static depth for applications: Static analysis for all self written components | automatic |
| [efa52cc8-6c5c-4ba2-a3d2-7164b0402f34](https://dsomm.owasp.org/activity-description?uuid=efa52cc8-6c5c-4ba2-a3d2-7164b0402f34) | Static depth for applications: Stylistic analysis | automatic |
| [f2f0f274-c1a0-4501-92fe-7fc4452bc8ad](https://dsomm.owasp.org/activity-description?uuid=f2f0f274-c1a0-4501-92fe-7fc4452bc8ad) | Static depth for applications: Exploit likelihood estimation | automatic |
| [f4ff841d-3b2a-45d9-853e-5ec7ecbcb054](https://dsomm.owasp.org/activity-description?uuid=f4ff841d-3b2a-45d9-853e-5ec7ecbcb054) | Static depth for applications: Static analysis for all components/libraries | automatic |
| [f57d55f2-dc05-4b34-9d1f-f8ce5bfb0715](https://dsomm.owasp.org/activity-description?uuid=f57d55f2-dc05-4b34-9d1f-f8ce5bfb0715) | Application tests: Security integration tests for important components | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.29 | Security testing in development and acceptance | curated |
| 8.33 | Test information | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SA-11 Developer Testing and Evaluation](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SA-11) | curated |

More: [[standard-nist-800-53-v5]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PO.4.1 | Define criteria for software security checks and track throughout the SDLC. | curated |
| PO.4.2 | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. | curated |
| RV.1.2 | Review, analyze, and/or test the software’s code to identify or confirm the presence of previously undetected vulnerabilities. | curated |

More: [[standard-nist-ssdf]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.3.1.2 | The card verification code is not retained upon completion of the authorization process. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): The card verification code is the three- or four-digit number printed on the front or back of a payment card used to verify card-not-present transactions. | automatic |
| 9.4.5.1 | Inventories of electronic media with cardholder data are conducted at least once every 12 months. (CUSTOMIZED APPROACH OBJECTIVE): Media inventories are verified periodically. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [V-RT-A](https://owaspsamm.org/model/verification/requirements-driven-testing/stream-a) | Control verification | curated |
| [V-RT-B](https://owaspsamm.org/model/verification/requirements-driven-testing/stream-b) | Misuse/Abuse Testing | curated |
| [V-ST-A](https://owaspsamm.org/model/verification/security-testing/stream-a) | Scalable Baseline | curated |
| [V-ST-B](https://owaspsamm.org/model/verification/security-testing/stream-b) | Deep understanding | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [433-442](https://opencre.org/cre/433-442). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
