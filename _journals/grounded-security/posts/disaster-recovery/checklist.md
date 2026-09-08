---
timetoread: "6 min read"
---
*The working checklist behind this record — the disaster-recovery build from business-agreed objectives through strategy, dependencies, scenarios, failover and failback, honest testing, and ongoing review. The Article tab carries the rationale and anti-patterns.*

## 1. Define Recovery Objectives

- [ ] Identify critical business services, applications, systems, and data
- [ ] Define the **Recovery Point Objective (RPO)** for each critical system
- [ ] Define the **Recovery Time Objective (RTO)** for each critical system
- [ ] Confirm that RPO and RTO targets are driven by business requirements
- [ ] Review the cost and technical complexity of meeting each target
- [ ] Obtain agreement from business owners on acceptable recovery targets
- [ ] Prioritize systems according to business impact and recovery urgency

## 2. Select Recovery Strategies

- [ ] Determine which recovery approach is appropriate for each system
- [ ] Consider **traditional physical backups** where appropriate
  - [ ] Store backup media at a separate, secure location
  - [ ] Confirm replacement hardware or infrastructure will be available after a disaster
  - [ ] Factor backup transport and restoration time into the RTO
- [ ] Consider a **warm standby** environment for faster recovery
  - [ ] Keep standby systems reasonably synchronized with production
  - [ ] Keep standby systems geographically separated from the primary environment
  - [ ] Document the process for redirecting DNS, routing, or network traffic during failover
- [ ] Consider **high availability** for systems requiring very short RPOs and RTOs
  - [ ] Ensure high-availability environments have enough spare capacity after a failure
- [ ] Consider an **alternate system** when restoring the original system is unnecessary
- [ ] Consider **system function reassignment** by repurposing noncritical systems during a disaster
  - [ ] Verify reassigned systems can safely support production workloads

## 3. Plan Cloud-Native Disaster Recovery

- [ ] Replicate critical applications and data to another cloud region or location
- [ ] Determine whether replication should be continuous or scheduled
- [ ] Use **Infrastructure as Code (IaC)** to recreate recovery environments quickly
- [ ] Verify IaC configurations accurately reproduce the production environment
- [ ] Configure cloud resources to scale when disaster recovery is activated
- [ ] Consider multi-region deployment for critical services
- [ ] Configure traffic rerouting to healthy regions
- [ ] Automate failover and failback where possible
- [ ] Use orchestration tools to reduce manual recovery steps
- [ ] Monitor cloud replication and recovery readiness
- [ ] Regularly test cloud recovery procedures
- [ ] Review cloud DR costs during normal and disaster operations

## 4. Identify Dependencies

- [ ] Map dependencies for every critical application and service
- [ ] Identify required network connectivity
- [ ] Identify routing and DNS dependencies
- [ ] Identify authentication and directory-service dependencies
- [ ] Identify databases, storage, APIs, and external services required by each system
- [ ] Confirm dependent services have compatible RTO and RPO targets
- [ ] Adjust unrealistic recovery targets when dependencies cannot meet them
- [ ] Include dependencies in tabletop exercises and DR testing

## 5. Prepare Disaster Scenarios

- [ ] Develop a ransomware or cyberattack scenario
- [ ] Develop a mission-critical hardware failure scenario
- [ ] Develop a complete datacenter or site-loss scenario
- [ ] Develop a prolonged power-outage scenario
- [ ] Develop a fire, flood, earthquake, or other physical-disaster scenario
- [ ] Develop a pandemic or loss-of-site-access scenario
- [ ] Include representatives from relevant IT and business teams when reviewing scenarios
- [ ] Identify how each scenario affects systems, people, facilities, and communications
- [ ] Determine whether the existing DR plan adequately addresses each scenario

## 6. Define Failover Procedures

- [ ] Establish clear criteria for declaring a disaster
- [ ] Define who is authorized to activate the DR plan
- [ ] Establish an escalation process for uncertain situations
- [ ] Document the exact steps required to fail over critical services
- [ ] Identify who performs each failover action
- [ ] Document DNS, routing, application, and infrastructure changes required during failover
- [ ] Confirm failover can meet the defined RTO
- [ ] Maintain an emergency communication plan for staff and stakeholders

## 7. Define Failback Procedures

- [ ] Document how services will return to the primary environment
- [ ] Confirm the original environment is stable before failback
- [ ] Synchronize data before returning services to the primary environment
- [ ] Plan failback during an appropriate maintenance window where possible
- [ ] Identify who is authorized to approve failback
- [ ] Communicate planned service impacts before switching back
- [ ] Verify applications and services after failback
- [ ] Document and resolve any issues discovered during the process

## 8. Test the Disaster Recovery Plan

- [ ] Schedule regular DR tests
- [ ] Perform tabletop exercises
- [ ] Perform technical recovery exercises
- [ ] Test scenarios without relying on systems that would be unavailable during the simulated disaster
- [ ] Verify systems can be recovered within the RTO
- [ ] Verify data can be recovered within the RPO
- [ ] Test backup restoration rather than assuming backups are usable
- [ ] Test network, DNS, authentication, and application dependencies
- [ ] Observe and document each test
- [ ] Record what worked well
- [ ] Record failures, delays, and unexpected dependencies
- [ ] Conduct a post-test debrief
- [ ] Assign corrective actions to specific owners
- [ ] Set deadlines for corrective actions
- [ ] Update the DR plan based on lessons learned
- [ ] Retest major changes

## 9. Protect Data at Rest

- [ ] Apply appropriate security controls to replicated and backup data
- [ ] Encrypt sensitive backup data where appropriate
- [ ] Restrict access to backup and recovery systems
- [ ] Require strong authentication for administrative access
- [ ] Apply controls comparable to those used in the production environment
- [ ] Confirm backup copies do not create a weaker path to sensitive information

## 10. Protect Data in Transit

- [ ] Encrypt data transmitted to backup or secondary systems
- [ ] Authenticate systems participating in replication
- [ ] Secure network connections used for backup and recovery
- [ ] Review replication traffic for exposure to untrusted networks
- [ ] Monitor recovery-related network activity for suspicious behavior

## 11. Maintain Patching and Configuration

- [ ] Keep recovery systems patched at an appropriate level
- [ ] Keep production and recovery configurations aligned
- [ ] Apply configuration changes to both primary and recovery environments
- [ ] Track intentional differences between environments
- [ ] Verify applications behave correctly on recovery systems
- [ ] Prevent outdated recovery systems from becoming a security weakness

## 12. Control User Access

- [ ] Define who can access recovery systems during a disaster
- [ ] Maintain least-privilege access wherever possible
- [ ] Protect personally identifiable, financial, and other sensitive information
- [ ] Do not remove security controls simply to accelerate recovery
- [ ] Document emergency-access procedures
- [ ] Review and revoke temporary access after the incident

## 13. Maintain Physical Security

- [ ] Confirm secondary sites have appropriate physical access controls
- [ ] Compare physical security at primary and recovery locations
- [ ] Protect servers, storage, backup media, and networking equipment
- [ ] Restrict access to authorized personnel
- [ ] Address security gaps if a secondary location uses office space rather than a dedicated datacenter

## 14. Communication and Documentation

- [ ] Maintain current contact details for recovery personnel
- [ ] Define communication channels to use during an outage
- [ ] Identify who communicates with employees, customers, vendors, and leadership
- [ ] Keep DR procedures accessible even if normal systems are unavailable
- [ ] Document roles and responsibilities
- [ ] Document recovery priorities and decision-making authority
- [ ] Record actions and decisions during an incident
- [ ] Communicate during all outages, regardless of size

## 15. Ongoing Review

- [ ] Review the DR plan after significant infrastructure or application changes
- [ ] Review RPO and RTO targets periodically with business owners
- [ ] Update dependency maps when systems change
- [ ] Review backup and replication success regularly
- [ ] Verify contact information remains current
- [ ] Incorporate lessons from incidents and DR tests
- [ ] Confirm the DR strategy continues to meet business requirements
- [ ] Ensure disaster recovery planning remains aligned with business continuity planning

With every section green, the plan holds where it counts: objectives the business signed, strategies priced per system, dependencies aligned, failover and failback rehearsed, and controls intact under pressure. The test running through the whole sequence: **has every backup been proven by a restore, and every RTO been proven by a test that did not lean on systems the disaster would have taken out?**
