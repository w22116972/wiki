# Latency lags bandwidth

> David A. Patterson. 2004. Latency lags bandwith. Commun. ACM 47, 10 (October 2004), 71–75. https://doi.org/10.1145/1022594.1022596

## Conclusion

Bandwidth improves much more quickly than latency.

Bandwidth can be improved by money, while latency is limited by the speed of light.

## Reasons

### Moore's Law
- bandwidth improved by faster transistors, more transistors, more pins in parallel
- latency improved by faster transistors, but
  - The distances that signals need to travel between different parts of a chip can contribute to increased latency

### Distance sets lower bound to latency

Speed of light
- 300m has latency at least 1 microsecond
- Delay on word lines and bit lines are the largest part of row access time of a DRAM
> In Dynamic Random Access Memory (DRAM), the row access time refers to the period from when the memory controller issues a row address and opens a memory row (activation command) to when the data can be read or written. This time is one of the key performance metrics of DRAM operation. In this process, the delays on the "word lines" and "bit lines" constitute the largest portion of the row access time.
    
### Latency helps bandwidth but not vice versa

e.g. Lower DRAM latency -> higher number of DRAM accesses per second -> higher bandwidth

e.g. Faster spinning disk -> lower rotational latency -> higher bandwidth

e.g. Increasing linear density of bits per inch on track -> higher bandwidth but not lower latency 

### Buffer improves bandwidth but not latency

How Buffers Help Bandwidth:
Buffers can help maintain high bandwidth in networks by smoothing out bursts of data traffic. For example, if a device sends data in short, high-speed bursts, buffers can store these bursts and then release data at a steady rate, allowing the receiving end to process the stream more consistently without losing packets. This buffering helps to maximize the use of the network’s bandwidth capacity.

How Buffers Hurt Latency:
While buffers are good for managing bandwidth, they inherently introduce latency because data must wait in the queue before being processed. When a buffer is full, incoming packets must wait longer, increasing the overall time it takes for data to travel from source to destination.

Consider a video streaming service. When you stream a video, data packets are sent from the server and might be buffered at various points along the network to ensure smooth playback. The buffering allows the video to play without interruption even if there's a temporary dip in network speed, thus maintaining effective bandwidth utilization. However, the initial buffering of the video when you first hit play introduces a delay (latency) before the video starts. This is why you often experience a brief loading period before the video begins to play.

Overall, the statement captures a fundamental trade-off in network design analyzed by queuing theory: buffers can optimize bandwidth utilization by absorbing data bursts and releasing them at manageable rates, but this process can increase latency due to the time data spends waiting in queues.

## Techniques to reduce latency

### Cache

- Use locality of reference to allow a small fast memory to capture most accesses
  - e.g. L1 cache, L2 cache, L3 cache
- File systems use a large main memory to act as a file cache

### Replication

- Replicas close to users
- Database replicas

### Prediction

- Predict then prefetch
