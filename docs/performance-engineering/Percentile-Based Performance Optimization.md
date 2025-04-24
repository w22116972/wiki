# Percentile-Based Performance Optimization

#### Abstract
This guide provides a practical framework for understanding and optimizing service latency across key percentiles — P50, P95, and P99 — each representing different performance challenges and tuning strategies.

#### Prerequisite

Use k6 to measure latency percentile

## P50 (Median Latency)

Measures the latency experienced by the middle 50% of requests — half of all requests are faster, and half are slower. Reflects the typical user experience and is a baseline for system responsiveness under normal conditions.

#### Optimization Goal

Improve critical path

## P95 (Under Bursty Load Latency)

Measures the latency experienced by the slowest 5% of requests under load surges. Useful for identifying bottlenecks not visible in typical traffic (P50) but occurring more frequently than rare tail spikes (P99).

#### Optimization Goal
Handle increased concurrency and throughput spikes without degradation

## P99 (Tail latency)

Measures the latency experienced by the slowest 1% of requests. Highlights rare but impactful performance outliers, often caused by resource contention, long GC pauses, cold caches, or other edge-case conditions. Critical for maintaining system reliability and meeting strict SLAs/SLOs.

#### Optimization Goal

Improve the slowest requests that occur under edge-case conditions
