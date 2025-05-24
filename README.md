# Wiki

These are selected documents in the topics of system design, best practices, domain knowledge, and case studies.
Each title is a link to its related documents.

#### Performance Engineering

[P50, P95, P99 latency guide](https://github.com/w22116972/wiki/blob/main/docs/performance-engineering/Percentile-Based%20Performance%20Optimization.md)
- P50 is median latency
- P95 is under bursty load latency
- P99 is tail latency


#### Classic Papers

[Latency lags bandwidth by David A. Patterson](https://github.com/w22116972/wiki/blob/main/docs/classic-paper/Latency%20lags%20bandwidth.md)
- Bandwidth is way faster then latency, latency is limited by physical constraints(long distance, speed of light ... etc)
- 3 keys to improving latency: reduce distance(cache, replica), parallelism(multi-threading), prediction(preload, prefetch)