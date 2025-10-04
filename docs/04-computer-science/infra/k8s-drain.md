# Kubernetes Drain

> actively cordon node (mark node as `NotSchedulable`) then evict all pods on that node

## Goal

- node maintainence
    - upgrading
- safely delete nodes
- immediately activate the process when disaster to shorten uptime
- release resources for high priority pods
    1. drain all pods on that node
    2. taint high priority pods to that node