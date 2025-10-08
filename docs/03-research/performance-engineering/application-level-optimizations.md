# Application-level Optimizations

## I/O-Bound Latency on the Critical Path

To optimize slow I/O (network, disk, DB) that block request processing and reduce concurrency. Prevent request threads from being blocked on slow external calls; maintain high throughput under load.

- Asynchronous Processing (includes async DB access)
- Avoid Synchronous I/O on Critical Path
- Efficient Network Protocols (e.g., gRPC, HTTP/3)

## Large Payload Overhead

To optimize excessive bandwidth usage, serialization/deserialization costs, and memory strain due to large response/request sizes.

- Compressed API Payloads
- Selective field filtering on API
    - use query parameter to return part of full response
- Pagination
- Streaming

## High Concurrency Throughput

To scale maximize request-handling capacity without proportional resource consumption increases

- asynchroos processing
- reduce network connection overhead
- multiplexing
- caching at code level

## CPU-Bound

To reduce CPU time per request

- efficient algorithm
- efficient data structures
- parallelization