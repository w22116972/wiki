# Low latency


> https://www.youtube.com/watch?v=BKVWr65z8dQ
- No db in hot path
- fully in memory
  - memory mapped files in linux
- UDP
- 2 Nics
- Linux DPDK for fast packet processing
- tune MTU package size
- no container or k8s
- ec2 instance + bare metal
- single threaded state machine
  - no context switching
  - deterministic
- thread pin to dedicated core
  - only L1, L2 cache

Design principles
- zero GC in hot path
  - know exactly how amount of memory is needed, pre-allocate then reuse
- lock free algorithms in hot path
- non-blocking I/O in hot path
- don't handle exception in hot path
  - e.g. if some messages will cause exception, then there will be another path that execute these messages and handle the exception like logging. Make hot path only do one thing.
- single writer principle
- avoid data copying
- no logging
- no string

Use Aeron framework


---

- No GC
- short call stacks, and no recursion
- one physical core per thread
- non-locking data structures and use the one writer principle where possible
- don't use the kernel if possible
