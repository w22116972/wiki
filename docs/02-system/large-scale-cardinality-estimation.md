---
date: 2025-10-05
tags: [design]
status: drafting
---

# Problem: Cardinality Estimation in a Large-Scale Set

## 1. Problem Statement

Given a very large stream or set of items (e.g., user visits, search queries, IP addresses), design a system to estimate the number of **unique** items (the cardinality) in the set. The data is too large to fit into memory, so storing every unique item seen is not feasible.

**Constraints:**

*   **Massive Data Volume:** The stream can contain billions or trillions of items.
*   **Memory Limitation:** The solution must use a small, fixed amount of memory.
*   **Real-time Processing:** The estimate should be available on demand with low latency.

---

## 2. Solution 1: Distributed Hash Set (Exact Count)

This is the brute-force, non-probabilistic approach that provides a 100% accurate count. It is the best solution when precision is non-negotiable and the cost of storing all unique items is acceptable.

**Best Scenario:** Financial reporting that requires counting the exact number of unique customers who made a purchase in a given quarter. In this context, any approximation is unacceptable, as it would lead to incorrect business metrics. The legal and financial requirements demand perfect accuracy.

### How It Works
You use a distributed key-value store (like Redis or Cassandra). For every item that arrives from the stream, you attempt to add it to the distributed set. The data is sharded across the cluster. The final cardinality is simply the total number of keys stored across all nodes.

### Key Characteristics
*   **Accuracy:** **100% Exact**.
*   **Space Complexity:** `O(U)`, where U is the number of unique items. This is the primary drawback as it can be massive.
*   **Time Complexity:** `O(1)` or `O(log U)` for each item insertion, plus network latency.
*   **Use Case:** When correctness is mandatory and cannot be compromised.

---

## 3. Solution 2: HyperLogLog (HLL) (Approximate, Best for Memory)

HyperLogLog is a highly advanced probabilistic algorithm that provides a very accurate estimate of cardinality using an astonishingly small and fixed amount of memory. It is the industry-standard and best solution for nearly all large-scale estimation problems.

**Best Scenario:** Counting the number of unique visitors on a major website like Google or Facebook in real-time. The scale is massive (billions of users), and a 99% accurate estimate (e.g., "1.21 billion users" vs. the true "1.20 billion") is perfectly acceptable for a dashboard. The memory savings are colossal, making it the only feasible option.

### How It Works
HLL is based on the observation that the cardinality of a set of uniformly distributed random numbers can be estimated by observing the maximum number of leading zeros in their binary representation. A rare pattern (e.g., 10 leading zeros) is much more likely to occur in a large set than a small one. HLL applies a hash function to make the input stream look like uniform random numbers and uses multiple small "registers" to store the maximum number of leading zeros observed across different subsets of the data, averaging them to produce a highly accurate estimate with a small, known standard error.

### Key Characteristics
*   **Accuracy:** **Approximate**, with a typical standard error of ~2% while using only 1.5 KB of memory.
*   **Space Complexity:** Extremely low and constant, `O(1)`.
*   **Time Complexity:** `O(1)` to process each item.
*   **Use Case:** The default choice for large-scale cardinality estimation in streaming or batch systems.

---

## 4. Solution 3: Linear Counting (Approximate, Best for Simplicity/Smaller Sets)

Linear Counting is another probabilistic algorithm that is simpler than HyperLogLog. It is the best solution for cardinality estimation on sets of **small to medium** size, where it can be more accurate than HLL and is easier to implement.

**Best Scenario:** Counting the number of unique users who interacted with a new, specific feature on a website within the last hour. The total number of unique users is expected to be in the thousands or low millions, not billions. In this case, Linear Counting provides excellent accuracy and is simpler to reason about than HLL.

### How It Works
Linear Counting uses a bit array (a bitmap) of size `m`, with all bits initially set to 0. When a new item arrives, it is hashed to an index in the array, and the bit at that index is set to 1. The cardinality is estimated based on the number of empty bits still remaining in the array, using a formula derived from statistics.

### Key Characteristics
*   **Accuracy:** **Approximate**. Very accurate for cardinalities up to `m`, but its accuracy degrades as the bitmap fills up.
*   **Space Complexity:** `O(m)`, where `m` is the size of the bitmap. It uses more memory than HLL but is still sub-linear compared to the exact approach.
*   **Time Complexity:** `O(1)` to process each item.
*   **Use Case:** Good for smaller-scale problems or as a component in more complex systems.

---

## 5. Comparison of Approaches and When to Use Which

| Feature             | Distributed Hash Set                       | HyperLogLog (HLL)                          | Linear Counting                            |
| ------------------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| **Accuracy**        | **100% Exact**                             | **Approximate** (~2% error)                | **Approximate** (error grows with size)    |
| **Primary Use Case**| **Source of truth, financial data**        | **Massive-scale, streaming data**          | **Small to medium-scale data**             |
| **Memory Usage**    | Very High (`O(U)`)                        | Extremely Low (`O(1)`, ~1.5KB)             | Low (`O(m)`)                               |
| **Complexity**      | Conceptually simple, operationally complex | Mathematically complex, easy to use via libs | Simple to implement and understand         |

### When to Use Which:

1.  **Choose a Distributed Hash Set when:**
    *   **You need a 100% correct number, period.** Any error is unacceptable.
    *   **Use Case:** Billing systems, compliance reporting, scientific data analysis where precision is paramount.

2.  **Choose HyperLogLog when:**
    *   **You are dealing with massive, web-scale data.** This is the default and most powerful tool for this problem.
    *   **Memory is a critical constraint.**
    *   **Use Case:** Counting unique visitors, unique search queries, unique IP addresses in a global network.

3.  **Choose Linear Counting when:**
    *   **The expected cardinality is not astronomically large.**
    *   **You want a simple, easy-to-implement solution** and the memory footprint is less critical than with HLL.
    *   **Use Case:** Counting unique users for an A/B test on a new feature, tracking unique API clients per hour.


