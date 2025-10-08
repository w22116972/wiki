# PACELC theorem

```mermaid
flowchart TD

  P{Partitioned?}

  P -->|"(P) Yes\n(latency suffers)"| C{Tradeoff:\nConsistency vs.\navailability}
  C -->|A| PA
  C -->|C| PC

  P -->|"(E) No\n(availability suffers)"| E{Tradeoff:\nLatency vs.\nConsistency}
  E -->|L| EL
  E -->|C| EC
```

- PA/EL: prioritize availability and latency over consistency
- PA/EC: when there is a partition, choose availability; else, choose consistency
- PC/EL: when there is a partition, choose consistency; else, choose latency
- PC/EC: choose consistency at all times
    - MySQL cluster, BigTable
