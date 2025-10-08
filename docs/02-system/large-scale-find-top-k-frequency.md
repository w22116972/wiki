# Problem: Find Top K Frequent Items in a Large-Scale System

## 1. Problem Statement

Given a very large file or stream of data (e.g., terabytes) containing items (like words, IPs, URLs, or user IDs), find the top K most frequent items. The data is too large to fit into the memory of a single machine.

**Constraints:**

*   **Large Data Volume:** The input data cannot be loaded into memory at once.
*   **Distributed Processing:** The solution must be scalable and work across multiple machines.
*   **High Availability:** The system should be resilient to machine failures.

## 2. Challenges

*   **Memory Limitation:** A standard in-memory hash map for frequency counting is not feasible.
*   **Scalability:** The solution needs to scale horizontally as the data size grows.
*   **Data Distribution:** How to efficiently process data chunks and aggregate results from multiple machines.

---

## 3. Solution 1: MapReduce (Exact Counts)

This approach provides **exact** frequency counts and is the standard for **batch processing** where accuracy is paramount and latency is not a primary concern.

### How It Works
1.  **Map Phase:** The input data is split into chunks. Mappers process these chunks in parallel, emitting `(item, 1)` for each item. A local combiner can pre-aggregate counts to reduce network traffic.
2.  **Shuffle & Sort Phase:** The framework automatically groups all pairs by item, sending all counts for a single item to the same Reducer.
3.  **Reduce Phase:** Reducers sum the counts for each item, producing a final `(item, total_count)`.
4.  **Final Aggregation:** A final job sorts the results from all Reducers to find the top K items.

### Complexity Analysis
*   **Time Complexity:** `O(N)`, parallelized across the cluster. The main bottleneck is the I/O for the shuffle phase.
*   **Space Complexity:** `O(U)`, where U is the number of unique items, as every unique item must be stored.

---

## 4. Solution 2: Count-Min Sketch (Approximate, Probabilistic)

This approach uses a probabilistic data structure to produce **approximate** frequency counts. It is extremely memory-efficient and ideal for **high-volume streaming data** where some inaccuracy is acceptable.

### How It Works
A Count-Min Sketch is a `d x w` matrix of counters. An item's count is updated by hashing it `d` times and incrementing the corresponding counter in each of the `d` rows. The estimated frequency is the **minimum** of these `d` counters. This guarantees the estimate is never less than the true frequency but may be an overestimate.

In a distributed system, each node maintains a local sketch. These sketches can be merged at an aggregator by summing their matrices element-wise. The final top K is derived from this merged sketch, typically by tracking candidates in a min-heap.

### Complexity Analysis
*   **Time Complexity:** `O(N * d)`, where `d` is the number of hash functions (a small constant).
*   **Space Complexity:** `O(w * d)`, which is **constant** and independent of the number of items or their cardinality.

---

## 5. Solution 3: Heavy Hitters Algorithm (Space-Saving)

This is a highly practical streaming algorithm that provides a good balance between accuracy and memory efficiency. It's often more intuitive and accurate than Count-Min Sketch for the specific task of finding top K items.

### How It Works
The algorithm maintains a fixed-size data structure (e.g., a hash map and a min-heap) to track `m` candidate items, where `m` is slightly larger than `K`.

1.  **Process Item:** For each item in the stream:
2.  **If Item is Tracked:** Increment its count.
3.  **If Item is New and Space is Available:** If fewer than `m` items are tracked, add the new item with a count of 1.
4.  **If Item is New and Full:** If all `m` slots are full, find the item with the **minimum count**, evict it, and replace it with the new item. The new item inherits the evicted item's count and adds 1.

In a distributed system, each node runs a local Space-Saving instance. An aggregator then collects the `m` candidates from each node and runs a final round to determine the global top K from this much smaller, merged set.

### Complexity Analysis
*   **Time Complexity:** `O(N log m)`. The `log m` factor comes from heap operations to find the minimum and update counts.
*   **Space Complexity:** `O(m)`, which is effectively `O(K)`. This is constant and very memory-efficient.

---

## 6. Comparison of Approaches and When to Use Which

| Feature             | MapReduce (Exact)                          | Count-Min Sketch (Approximate)               | Space-Saving (Heavy Hitters)                 |
| ------------------- | ------------------------------------------ | -------------------------------------------- | -------------------------------------------- |
| **Accuracy**        | **100% Exact**                             | **Approximate** (overestimates)              | **Approximate** (guaranteed to find items with > N/m frequency) |
| **Use Case**        | **Batch Processing** (offline analytics, reports) | **High-Volume Streaming** (network monitoring) | **General-Purpose Streaming** (real-time trends) |
| **Memory Usage**    | Very High (`O(U)`)                        | Very Low (`O(w*d)`, constant)                | Low (`O(K)`, constant)                       |
| **Latency**         | High (minutes to hours)                    | Very Low (milliseconds)                      | Very Low (milliseconds)                      |
| **Guarantees**      | Correctness                                | Probabilistic error bounds                   | Deterministic error bounds                   |
| **Implementation**  | Simpler with frameworks (Spark, Hadoop)    | Requires careful tuning of `w` and `d`       | Relatively straightforward to implement      |

### When to Use Which:

1.  **Choose MapReduce when:**
    *   **Absolute accuracy is non-negotiable.** You are generating financial reports, conducting scientific research, or building critical business intelligence dashboards.
    *   **The process is offline.** The job can run for minutes or hours without impacting a live user experience.
    *   You are already operating within a Hadoop/Spark ecosystem.

2.  **Choose Count-Min Sketch when:**
    *   **You are processing an extremely high-throughput stream.** Think network traffic analysis, where you need to estimate frequencies of millions of distinct IPs per second.
    *   **Memory is the most critical constraint.** It offers the lowest memory footprint.
    *   **You only need frequency estimates** and don't need to store the items themselves. You can check the frequency of any item, not just the top K.

3.  **Choose Space-Saving when:**
    *   **You need a general-purpose, real-time solution for finding top K items.** This is the most common "best of both worlds" scenario.
    *   **You want better accuracy than Count-Min Sketch for the top items.** It directly tracks the candidates, avoiding the estimation errors from hash collisions for non-top items.
    *   **The use case is real-time analytics,** like a "trending topics" feature on a social media site, where you need a constantly updated list of the most popular items.