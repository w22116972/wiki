# Performance Tools



## Tools

- `jmh`
  - micro: method/class level [^1]
  - use case: comparing two algorithms in isolation, performance of hot code paths that truly dominate your app
    - JMH runs in isolation: No other threads, CPU competition, disk I/O, or cache contention
- async-profiler or IntelliJ profiler
  - macro: application level
  - def: runtime, sampling-based profiler
  - profile: CPU, Java, native, JNI, system calls
    - no safepoint bias, can catch short-lived methods
- Java Flight Recorder (JFR) + JDK Mission Control (JMC)
  - macro: application level
  - def: runtime, sampling-based profiler
  - profile: Java only
    - capture GC events, allocations, lock contention, thread behavior
    - but missed methods that don't hit safepoint


[^1]: My reference