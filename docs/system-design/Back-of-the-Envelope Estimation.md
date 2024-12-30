# Back-of-the-Envelope Estimation

## Metrics

- users
- QPS
- storage
- memory
- bandwidth(read/write)

## Latency numbers for estimations
These numbers are used to estimate the **order of magnitude** of the latency.

| Action                                   | Time                |
|------------------------------------------|---------------------|
| L1 cache reference                       | 0.5 ns              |
| Branch mis-prediction                    | 5 ns                |
| L2 cache reference                       | 7 ns                |
| Mutex lock/unlock                        | < 100 ns            |
| Main memory reference                    | 100 ns              |
| Compress 1K bytes with Zippy             | 10^4 ns             |
| Send 2K bytes over 1 Gbps network        | 2 x 10^4 ns         |
| Read 1 MB sequentially from memory       | 10^6 ns             |
| Round trip within same datacenter        | 10^5 ns             |
| Disk seek                                | 10^7 ns             |
| Read 1 MB sequentially from network      | 10^7 ns             |
| Read 1 MB sequentially from disk         | 10^7 ns             |
| Send packet CA -> Netherlands -> CA      | 150 ms = 150 x 10^6 ns |

CPU-bound work is 10 times faster than memory-bound work and 100 times faster than I/O-bound work

## Typical QPS for single-server datastore

| Component             | Queries Per Second (QPS)     |
|-----------------------|------------------------------|
| MySQL                 | 1,000                        |
| Key-Value Store       | 10,000                       |
| Cache Server          | 100,000 – 1,000,000          |

### Typical server can handle requests in a second

Assume 3.5 GHz (3,500,000,000 cycles /s)

$ \text{CPU}_{\text{time per clock cycle}}  =  \frac{1}{3.5 \times 10^9}$

$ \text{CPU}_{\text{time per program}} = (3.5 \times 10^6) \times 1 \times \frac{1}{3.5 \times 10^9} = 0.001 \, \text{second}$

$\text{Total requests a CPU executes in 1 second} = \frac{1}{10^{-3}} = 1000 \, \text{requests}$

$\text{Total requests a 64 core server executes in 1 second} = 64 \times 1000 = 64000 \, \text{requests}$



## Common approximations

- 1 TB/day = 10 MB/s
- 1 M QPDay = 10 QPS

## String in Java

In Java 17 on a 64-bit machine with compressed pointers, the memory footprint of a `String` object can be estimated as follows:

### Memory Calculation

For a `String` of length `N`:

- **String object:**
    - Object header: 12 bytes
    - `char[]` reference: 4 bytes
    - `coder`: 1 byte
    - `hash`: 4 bytes (initially 0)
    - Padding: 3 bytes (to align to 8-byte boundary)
    - **Total for String object:** 24 bytes

- **`char[]` array:**
    - Array header: 12 bytes
    - Characters: $\( N \times 2 \)$ bytes (each `char` is 2 bytes)
    - **Total for `char[]` array:** $\( 12 + (N \times 2) \)$ bytes

### Total Memory

$\[ \text{Total Memory} = 24 + 12 + (N \times 2) = 36 + (N \times 2) \text{ bytes} \]$

### Example

For a `String` of length 10:

$\[ \text{Total Memory} = 36 + (10 \times 2) = 36 + 20 = 56 \text{ bytes} \]$
