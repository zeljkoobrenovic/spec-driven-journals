---
timetoread: "6 min read"
---
*The working checklist behind this record — the cost, performance, and scalability build, end to end. The Article tab carries the rationale and anti-patterns. Tools named here (OpenCost, Grafana, Karpenter, VPA/Goldilocks, Kyverno/Gatekeeper) are the reference stack; substitute equivalents freely as long as the property holds.*

## 1. Define Goals and Trade-Offs

- [ ] We have defined availability and performance SLOs
- [ ] We have identified acceptable latency, throughput, and downtime
- [ ] We have calculated the cost required to meet each SLO
- [ ] Cost/performance/scalability trade-offs are explicit
- [ ] Infrastructure cost is justified by the business value delivered
- [ ] We do not choose infrastructure based only on the lowest price

## 2. Establish Cost Observability

- [ ] Cloud-native cost reporting is enabled
- [ ] OpenCost (or equivalent) is installed and configured for Kubernetes cost visibility
- [ ] We have consistent Kubernetes labels for:
  - [ ] Team
  - [ ] Cost center
  - [ ] Business unit
  - [ ] Application
- [ ] Cost labels are applied consistently to namespaces and deployments
- [ ] We track CPU cost
- [ ] We track memory allocation and memory cost
- [ ] We have Grafana dashboards for cost reporting
- [ ] Workload costs are allocated to specific teams or projects
- [ ] Showback or chargeback reporting is established

## 3. Establish a Workload Baseline

- [ ] We have selected the application to optimize
- [ ] Its current hourly and monthly cost is recorded
- [ ] A measurable cost-reduction target is set
- [ ] We monitor actual CPU usage
- [ ] We monitor actual memory usage
- [ ] Peak CPU periods are identified
- [ ] Peak memory periods are identified
- [ ] We know whether CPU and memory peaks occur at the same time
- [ ] Actual usage is compared with configured resource requests

## 4. Rightsize Workloads

- [ ] Oversized CPU requests are reduced, leaving reasonable headroom
- [ ] Oversized memory requests are reduced, leaving reasonable headroom
- [ ] We have determined whether the workload is:
  - [ ] CPU-bound
  - [ ] Memory-bound
  - [ ] I/O-bound
  - [ ] Storage-bound
- [ ] An appropriate instance category is selected for the workload
- [ ] Compute-optimized instances are considered for CPU-heavy workloads
- [ ] Memory-optimized instances are considered for memory-heavy workloads
- [ ] Automated instance selection (Karpenter) is considered

## 5. Configure Horizontal Pod Autoscaling

- [ ] HPA is configured for workloads that benefit from additional replicas
- [ ] Minimum replicas are set appropriately
- [ ] Maximum replicas are set appropriately
- [ ] CPU utilization targets are configured
- [ ] Memory utilization targets are configured where appropriate
- [ ] Scale-up behavior is safe
- [ ] Scale-down behavior is safe
- [ ] Stabilization windows reduce scaling thrash
- [ ] Custom business-level metrics are considered, such as:
  - [ ] Requests per second
  - [ ] Queue depth
  - [ ] Active sessions
- [ ] HPA is tested under generated load
- [ ] Scaling maintains the required SLO

## 6. Evaluate Vertical Pod Autoscaling

- [ ] VPA is installed if required
- [ ] VPA runs in recommendation/"off" mode first
- [ ] VPA has had enough time to observe realistic workload behavior
- [ ] CPU recommendations are reviewed
- [ ] Memory recommendations are reviewed
- [ ] Goldilocks is used, if desired, to inspect recommendations
- [ ] High-confidence recommendations are implemented
- [ ] Minimum and maximum resource limits are defined
- [ ] Containers that should not be modified (such as sidecars) are excluded
- [ ] We have decided whether HPA and VPA should be used together

## 7. Optimize Infrastructure Capacity

- [ ] Stable baseline capacity is identified
- [ ] On-demand capacity is used where stability is required
- [ ] Spot instances are evaluated for fault-tolerant workloads
- [ ] Spot instances are avoided for unsuitable workloads, such as:
  - [ ] Business-critical single replicas
  - [ ] Long-running jobs that cannot tolerate interruption
  - [ ] Highly latency-sensitive operations
- [ ] Interruption handling is configured for spot workloads
- [ ] Taints/tolerations are configured where spot nodes require workload isolation
- [ ] Node affinity prefers spot capacity where appropriate
- [ ] Fallback to on-demand capacity is allowed when needed
- [ ] Committed-use discounts are evaluated for predictable baseline workloads
- [ ] We do not overcommit beyond the true baseline
- [ ] Committed capacity is not used for highly variable development, test, batch, or emerging workloads

## 8. Implement Cost Governance

- [ ] ResourceQuotas are defined for each team or namespace
- [ ] CPU request quotas are set
- [ ] Memory request quotas are set
- [ ] CPU limits are set
- [ ] Memory limits are set
- [ ] Maximum pod counts are limited where appropriate
- [ ] Persistent volume claims are limited where appropriate
- [ ] LimitRanges are configured for individual containers
- [ ] Default resource requests are defined
- [ ] Default resource limits are defined
- [ ] Minimum and maximum allowable resources are defined
- [ ] Workloads are required to declare CPU requests
- [ ] Workloads are required to declare memory requests
- [ ] Resource requirements are enforced with policy-as-code tools (Kyverno or Gatekeeper — see [[policy-as-code]])

## 9. Configure Cost Anomaly Detection

- [ ] A normal cost baseline is established
- [ ] Unexpected cost spikes trigger alerts
- [ ] Current spending rates are compared with historical averages
- [ ] Anomaly thresholds are tuned based on observed production behavior
- [ ] Memory leaks that continuously increase resource consumption are investigated
- [ ] Workloads consuming unexpectedly high CPU are investigated
- [ ] Alerts are reviewed and refined over time

## 10. Integrate Cost Controls into CI/CD

- [ ] Workload cost is estimated before production deployment
- [ ] New CPU requests are compared with the previous deployment
- [ ] New memory requests are compared with the previous deployment
- [ ] Unusually large increases in resource requirements are flagged
- [ ] Major cost increases require explicit approval or override
- [ ] Namespace ResourceQuotas are checked during deployment
- [ ] Deployments that would exceed namespace budgets fail
- [ ] Failed quota checks return a clear remediation message
- [ ] Estimated monthly cost is added to deployment metadata
- [ ] Cost information appears in pull-request or deployment summaries
- [ ] Post-deployment cost is compared with the previous seven-day average

## 11. Measure Optimization Results

- [ ] Post-optimization cost is compared with the original baseline
- [ ] Performance has not degraded
- [ ] Availability SLOs are still being met
- [ ] Latency remains acceptable under load
- [ ] Autoscaling responds correctly
- [ ] Remaining waste is identified
- [ ] Optimization is repeated where necessary

## 12. The Worked Exercise: A 30% Reduction Round

The handbook's completion exercise — one full pass of the loop, run as training:

- [ ] Establish the application's baseline cost
- [ ] Set a 30% cost-reduction target
- [ ] Profile CPU and memory usage for 1 week
- [ ] Rightsize resource requests using observed usage
- [ ] Configure HPA targeting approximately 75% CPU utilization
- [ ] Load-test the HPA configuration
- [ ] Run VPA in recommendation/"off" mode
- [ ] Review VPA/Goldilocks recommendations after 1 week
- [ ] Evaluate whether a different instance type would be cheaper
- [ ] Measure results after approximately 2 weeks
- [ ] Determine whether the 30% reduction target was achieved
- [ ] Document the changes made
- [ ] Document the cost and performance results
- [ ] Share the findings with the platform team

## Final Review

- [ ] Cost is visible and attributable
- [ ] SLOs are defined and measurable
- [ ] Workloads are appropriately sized
- [ ] Autoscaling is configured where beneficial
- [ ] Capacity uses the right mix of on-demand, spot, and committed resources
- [ ] Cost guardrails prevent uncontrolled consumption
- [ ] Cost anomalies trigger alerts
- [ ] CI/CD exposes the financial impact of deployments
- [ ] Optimization is treated as a continuous platform practice, not a one-time project
