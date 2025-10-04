# Best Practices for Reliability

> https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html

## Goals

- detect failure
- heal itself
- scale on demand

## Application

### [!]Conﬁgure [Pod Disruption Budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- limit the amount of concurrent disruption that an application will experience

### Avoid running singleton Pods

- use **Deployment** instead of Pod for applications

### Run multiple replicas

- use **Horizontal Pod Autoscaler** to scale replicas automatically based on workload demand.

### Schedule replicas across nodes

- use **pod anti-aﬃnity** or **pod topology** to spread replicas across multiple worker nodes and multiple AZs

### use Kubernetes Metrics Server



## Control panel

### Clusters with more than 1000 services

- use `ipvs` mode to replace `iptables` mode of `kube-proxy`
- may experience EC2 API request throttling if the CNI needs to request IP addresses for Pods or if you need to create new EC2 instances frequently. 
    - You can reduce calls EC2 API by conﬁguring the CNI to cache IP addresses. 
    - You can use larger EC2 instance types to reduce EC2 scaling events

## Data panel