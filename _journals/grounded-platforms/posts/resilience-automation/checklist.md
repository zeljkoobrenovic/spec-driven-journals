---
timetoread: "7 min read"
---
*The working checklist behind this record. The Article tab carries the rationale and anti-patterns. Section 9 is the hands-on validation exercise from the reference implementation.*

## 1. Define Service Level Objectives (SLOs)

- [ ] We have identified the most critical services
- [ ] Each service has appropriate Service Level Indicators (SLIs), such as:
  - [ ] Availability
  - [ ] Error rate
  - [ ] Request success rate
  - [ ] Latency
- [ ] Each service has an SLO target
- [ ] The measurement window is defined (e.g. a rolling 30-day period)
- [ ] The corresponding error budget is calculated
- [ ] We have defined what happens when the error budget is nearly exhausted
- [ ] Deployment-freeze criteria are established where appropriate
- [ ] Services with different business criticality have different SLO targets
- [ ] SLO definitions are stored as version-controlled configuration
- [ ] We have considered a vendor-neutral specification such as OpenSLO
- [ ] Prometheus SLO rules are generated with a tool such as Sloth
- [ ] SLO status is published through Grafana dashboards, displaying:
  - [ ] Current SLO compliance
  - [ ] Error-budget remaining
  - [ ] Error-budget burn rate
  - [ ] Remaining allowable downtime
- [ ] Alerts fire on SLO violations and excessive burn rates

## 2. Automate Backup and Restore

- [ ] Kubernetes backups are automated, not manual procedures
- [ ] Backups cover Kubernetes resources, including:
  - [ ] CRDs
  - [ ] Secrets
  - [ ] ConfigMaps
  - [ ] Persistent volumes
- [ ] CSI volume snapshots are configured where applicable
- [ ] Backups are stored in durable object storage such as S3 or GCS
- [ ] Backup retention periods are defined
- [ ] Cross-region backup replication is enabled where DR requires it
- [ ] Recurring backups are scheduled
- [ ] On-demand backups are supported when needed
- [ ] A restore procedure is defined
- [ ] Restoration of Kubernetes resources is automated
- [ ] Restoration of persistent volumes is automated
- [ ] Application health is validated after restoration
- [ ] Logs are checked after restoration
- [ ] Restored data integrity is verified
- [ ] Restore tests run in an isolated test cluster
- [ ] Restore validation is scheduled regularly (e.g. weekly)
- [ ] Functional tests run against restored environments
- [ ] Performance tests run where appropriate
- [ ] Development teams have self-service backup configuration
- [ ] Resources can opt in to backups through labels or configuration

## 3. Define Recovery Objectives

- [ ] Every important service has a defined RTO
- [ ] The RTO represents the maximum acceptable restoration time
- [ ] Every important service has a defined RPO
- [ ] The RPO represents the maximum acceptable amount of data loss
- [ ] Backup frequency is adjusted to meet RPO requirements
- [ ] Recovery automation is adjusted to meet RTO requirements
- [ ] RTO/RPO targets differ based on business impact

## 4. Establish Chaos Engineering

- [ ] We identify meaningful failure scenarios
- [ ] Each chaos experiment has a defined scope
- [ ] Each experiment has a defined target workload
- [ ] Each experiment has a defined duration
- [ ] Each experiment has defined scheduling
- [ ] Expected system behavior is established before running the experiment
- [ ] Abort conditions and safety boundaries are established
- [ ] We use controlled failure injection rather than uncontrolled testing
- [ ] We test:
  - [ ] Pod failures
  - [ ] Network latency
  - [ ] Packet loss
  - [ ] CPU stress
  - [ ] Memory stress
  - [ ] Service dependency failures where appropriate
- [ ] We use Chaos Mesh for Kubernetes-native experiments where suitable
- [ ] Experiments are scheduled predictably
- [ ] Experiment schedules are communicated to affected teams
- [ ] We prefer business hours, when engineers are available to respond
- [ ] We avoid peak traffic unless peak-load resilience is the explicit objective
- [ ] More aggressive experiments run during dedicated DR drills or low-traffic periods

## 5. Monitor Chaos Experiments

- [ ] Prometheus metrics are monitored during experiments
- [ ] Grafana dashboards are monitored
- [ ] Application logs are reviewed
- [ ] We track:
  - [ ] CPU and memory errors
  - [ ] Latency percentiles
  - [ ] Pod restart counts
  - [ ] Request success rates
  - [ ] Database connection-pool behavior
  - [ ] SLO burn-rate alerts
  - [ ] Recovery-failure alerts
- [ ] Technical failures are correlated with business metrics
- [ ] Users impacted are recorded where possible
- [ ] Revenue or other business impact is recorded where relevant
- [ ] Experiment results are reviewed after completion
- [ ] Resilience gaps are identified
- [ ] Remediation work is created
- [ ] We retest after remediation

## 6. Test Managed Cloud Services

- [ ] We test slow-query scenarios
- [ ] We test connection-limit exhaustion
- [ ] We test managed database failover procedures
- [ ] We test cross-region latency
- [ ] We verify application behavior when managed dependencies degrade
- [ ] Graceful degradation paths are validated
- [ ] Retry and backoff behavior is verified
- [ ] Circuit breakers are tested under realistic conditions
- [ ] Managed-service recovery procedures are tested before an actual outage occurs

## 7. Test Kubernetes Workloads

- [ ] We kill individual pods
- [ ] We kill multiple pods simultaneously
- [ ] We inject sustained pod failures
- [ ] We induce network failures
- [ ] We introduce latency and packet loss
- [ ] We stress CPU resources
- [ ] We stress memory resources
- [ ] We verify ReplicaSets replace failed pods
- [ ] We measure recovery time
- [ ] We monitor restart counts
- [ ] We check whether application availability remains within its SLO

## 8. Prepare Disaster Recovery

- [ ] We have identified which systems must survive catastrophic failures
- [ ] Recovery priorities are defined
- [ ] We have determined whether multi-region architecture is required
- [ ] A primary region is configured
- [ ] A secondary or standby region is configured where required
- [ ] Databases are replicated across regions
- [ ] Object-storage backups are replicated across regions
- [ ] Cache/data services are replicated where necessary
- [ ] A standby Kubernetes environment is maintained where appropriate
- [ ] DNS health checks are configured
- [ ] A documented failover mechanism is configured
- [ ] Replica-promotion procedures are defined
- [ ] Application-restoration procedures are defined
- [ ] Monitoring operates during failover
- [ ] The architecture can meet required RTO targets — verified
- [ ] Replication can meet required RPO targets — verified
- [ ] Regular DR drills are run
- [ ] Actual recovery time is measured during drills
- [ ] Actual recovery performance is compared against RTO/RPO targets
- [ ] Procedures are updated based on test results

## 9. Chaos Mesh Exercise Validation

The hands-on validation run from the reference implementation:

- [ ] Install the Chaos Mesh Helm repository
- [ ] Update the Helm repository index
- [ ] Install Chaos Mesh in the `chaos-mesh` namespace
- [ ] Confirm `chaos-controller-manager` is running
- [ ] Confirm `chaos-dashboard` is running
- [ ] Create the `chaos-testing` namespace
- [ ] Deploy a three-replica `nginx:alpine` application named `demo-app`
- [ ] Confirm all three pods are running
- [ ] Apply `chaos-mesh-pod-failure.yaml`
- [ ] Confirm Chaos Mesh accepts the first experiment
- [ ] Observe pod events in real time
- [ ] Monitor pod restart counts
- [ ] Review namespace events by timestamp
- [ ] Measure how quickly replacement pods are created
- [ ] Check `chaos_mesh_` metrics in Prometheus/Grafana
- [ ] Compare chaos metrics with observed pod churn
- [ ] Delete experiment resources after testing
- [ ] Remove the `chaos-testing` namespace

## 10. Continuous Resilience Improvement

- [ ] Resilience testing is treated as an ongoing engineering practice
- [ ] SLO definitions stay version-controlled
- [ ] Error-budget consumption is reviewed regularly
- [ ] Restores are tested regularly rather than assuming backups work
- [ ] Chaos experiments run on a schedule
- [ ] Disaster-recovery drills run on a schedule
- [ ] Metrics, logs, and observations are captured from every test
- [ ] Discovered failure modes are documented
- [ ] Weaknesses found during testing are remediated
- [ ] Experiments are repeated after fixes
- [ ] Recovery procedures are practiced before real incidents occur
- [ ] We promote continuous learning and improvement across teams

The test running through the chapter: **for every practice — SLOs, backups, chaos, DR — can you show the date and result of the last time it was actually exercised?**
