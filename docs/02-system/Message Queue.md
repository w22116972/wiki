# Message Queue

Ask functional
- format and size of message
  - text only? json? binary? multimedia?
- Can consume same message multiple times?
- Are messages consumed in the same order they are produced?
- Delivery guarantee?
  - at least once? at most once? exactly once?

Ask non-functional
- Availability -> SLA for uptime -> how many 9s?
- Scalability -> Horizontally scalable -> Throughput/latency requirements -> how many messages per second? how many consumers/producers?
- Durability -> Data retention policy -> how long messages are stored?

