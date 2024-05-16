# Back-of-the-Envelope Estimation

## Latency numbers for estimations
These numbers are used to estimate the **order of magnitude** of the latency.
- L1 cache reference: 0.5 ns
- Branch mis-prediction: 5 ns
- L2 cache reference: 7 ns
- Mutex lock/unlock: < 100 ns
- Main memory reference: 100 ns
- Compress 1K bytes with Zippy: 10^4 ns
- Send 2K bytes over 1 Gbps network: 2 x 10^4 ns
- Read 1 MB sequentially from memory: 10^6 ns
- Round trip within same datacenter: 10^5 ns
- Disk seek: 10^7 ns
- Read 1 MB sequentially from network: 10^7 ns
- Read 1 MB sequentially from disk: 10^7 ns
- Send packet CA->Netherlands->CA: 150 ms = 150 x 10^6 ns
