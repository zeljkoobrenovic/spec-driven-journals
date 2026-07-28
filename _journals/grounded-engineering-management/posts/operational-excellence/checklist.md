---
timetoread: "3 min read"
---
*The working checklist behind this record. The Article tab carries the rationale and anti-patterns.*

Based on Kate Matsudaira's article "Software Managers' Guide to Operational Excellence." Keys to success:

- Invest in quality assurance.
- Automate repetitive/manual tasks.
- Standardize and improve engineering processes.
- Measure and track performance data.
- Foster a culture of continuous improvement.

## 1. Launch Readiness

- [ ] Monitoring and dashboards are working and accessible
- [ ] Runbooks/playbooks exist and are understandable by unfamiliar team members
- [ ] Service-level objectives (SLOs) are defined and tracked
- [ ] Disaster recovery plans and backups are in place and tested
- [ ] Dependency failure behavior is understood (e.g., graceful degradation)
- [ ] Load and performance testing have been conducted
- [ ] Compliance requirements (security, privacy, regulations) are met

## 2. Incident Management

- [ ] An incident review process (retrospectives, RCAs) has been established
- [ ] Incident follow-up items are tracked and completed
- [ ] Alert volume is measured; high volumes are addressed
- [ ] Incident response quality is reviewed (e.g., SME coverage, focus on resolution)
- [ ] Weekly reviews of open incident action items occur

## 3. On-Call Management

- [ ] Defined on-call schedule and rotation length
- [ ] Backup plans are in place when someone doesn't respond to a pager
- [ ] On-call engineers have the right skills, tools, and permissions
- [ ] On-call pain (paging frequency, hours) is evaluated and minimized
- [ ] Clear expectations about feature work during on-call duty
- [ ] Rotation selection is fair and well-structured

## 4. Operational Data & System Health

- [ ] Dashboards provide visibility into the health of the system and the business
- [ ] Dashboards are reviewed regularly
- [ ] Awareness of current feature flags, marketing campaigns, and sales events
- [ ] Systems scale elastically, and thresholds are known

## 5. Customer Issue Tracking

- [ ] Frequency and type of customer-reported issues are tracked
- [ ] Trends in customer issues are analyzed (growing/shrinking)
- [ ] Quality management is considered in the context of new features
- [ ] Frequency of timeouts, errors, or crashes is tracked (especially mobile)

## 6. Failover & Recovery

- [ ] Disaster recovery plans are documented and tested
- [ ] Systems degrade gracefully when needed
- [ ] Time to full recovery is measured and optimized

## 7. CI/CD, Testing, and Automation

- [ ] High confidence in deployment quality
- [ ] Canary releases or feature flags are used for gradual rollouts
- [ ] Synthetic and real-user monitoring (RUM) are in place for key flows
- [ ] Systems have adequate observability and instrumentation
- [ ] Rollback/failover to a known good instance is always possible
