# Process vs Thread

[TOC]

## 1. Basic Definitions

- **Process**:  
  An independent execution unit with its own **memory space**, **code**, **data**, and **system resources**. Processes are isolated from one another.

- **Thread**:  
  A lightweight unit of execution **within a process**. Multiple threads within the same process share the same memory and resources.

## 2. Key Differences

| Aspect              | Process                          | Thread                               |
|---------------------|-----------------------------------|----------------------------------------|
| **Memory**          | Separate memory space            | Shared memory within the process       |
| **Communication**   | Inter-Process Communication (IPC) – slower and complex | Shared variables – fast and easy       |
| **Isolation**       | Fully isolated (safer)           | Not isolated (risk of data corruption) |
| **Creation Overhead** | High                           | Low                                     |
| **Failure Impact**  | One process crash doesn't affect others | One thread crash can crash the process |

## 3. Backend Context

- **Processes** are used to **scale services independently** (e.g., microservices architecture). Each microservice typically runs in its own process.
- **Threads** are used for **concurrent tasks** within the same application (e.g., handling multiple HTTP requests).
- In high-performance backend systems:
  - Multi-threading is used for parallelism (e.g., thread pools in a Java web server).
  - Multi-processing is used for isolation and CPU utilization (e.g., worker processes for background jobs).

## 4. Example

> In Java, a web server might use a **thread pool** to handle HTTP requests concurrently. Each request is processed in its own thread but within the same process.  
> In a microservices system, each service might be deployed as a **separate process or container**, isolated from the others.

## 5. When to Use Which

- Use **threads** when:
  - You need concurrency within the same memory space.`
  - Tasks share state and you can manage synchronization.

- Use **processes** when:
  - Tasks need isolation.
  - You want to leverage multiple CPU cores safely.
  - Stability is a concern and failure of one task should not affect others.
