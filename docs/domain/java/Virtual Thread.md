# Virtual Thread

> https://openjdk.org/jeps/444

## Abstract

A thread that not tied to OS thread, scheduled by the Java runtime


A thread is the smallest unit of processing that can be scheduled
1. Platform thread: a thin wrapper around an OS thread
    - the number of available platform threads is limited to the number of OS threads
    - tend to be long-lived, deep call stacks, be shared among many tasks
    - 1:1 schedule
2. Virtual thread
   - Java runtime maps a large number of virtual threads to a small number of OS threads (like virtual memory to physical memory)
   - When code in a virtual thread calls a blocking I/O operation, the Java runtime pauses the virtual thread until it can continue. The OS thread linked to the paused virtual thread can then be used for other virtual threads.
   - Higher throughput, not lower latency
     - good for long waiting I/O operations, not for long-running CPU intensive operations
     - good for thread-per-request style
   - tend to be short-lived, shallow call stacks
   - m:n schedule (JDK's scheduler assigns virtual threads to platform threads)
     - JDK's virtual thread scheduler is a work-stealing ForkJoinPool that operates in FIFO mode
     - The parallelism of the scheduler is the number of platform threads available for the purpose of scheduling virtual threads.

Running virtual thread is logically independent of its current carrier
- The value returned by Thread.currentThread() is always the virtual thread itself
- The stack traces of the carrier and the virtual thread are separate. An exception thrown in the virtual thread will not include the carrier's stack frames.
- Thread-local variables of the carrier are unavailable to the virtual thread

same scalability as the asynchronous style, except it is achieved transparently

### Why not asynchronous style

- In asynchronous programming, the interleaving of different stages of requests across different threads makes it difficult to profile and optimize performance
- Handling exceptions in asynchronous code can be complex and error-prone.
- Stack traces provide no usable context
- debuggers cannot step through request-handling logic
- profilers cannot associate an operation's cost with its caller


## Getting Started

Use builder
```java
Thread.Builder builder = Thread.ofVirtual().name("worker-", 0);
Runnable task = () -> {
    System.out.println("Thread ID: " + Thread.currentThread().threadId());
};

// name "worker-0"
Thread t1 = builder.start(task);   
t1.join();
System.out.println(t1.getName() + " terminated");

// name "worker-1"
Thread t2 = builder.start(task);   
t2.join();  
System.out.println(t2.getName() + " terminated");
```

Use Executors to separate thread management and creation
```java
void handle(Request request, Response response) {
    try (ExecutorService myExecutor = Executors.newVirtualThreadPerTaskExecutor()) {
        var future1 = executor.submit(() -> fetchURL(url1));
        var future2 = executor.submit(() -> fetchURL(url2));
        response.send(future1.get() + future2.get());
    } catch (ExecutionException | InterruptedException e) {
        response.fail(e);
    }
}

// Some I/O operation
String fetchURL(URL url) throws IOException {
    try (var in = url.openStream()) {
        return new String(in.readAllBytes(), StandardCharsets.UTF_8);
    }
}
```

A virtual thread is pinned in the following situations:
- The virtual thread runs code inside a `synchronized` block or method
- The virtual thread runs a native method or a foreign function

Rule: The number of virtual threads is always equal to the number of concurrent tasks in your application
- To represent every application task as a thread, don't use a shared thread pool

### Use Semaphores to Limit Concurrency

```java
ExecutorService es = Executors.newFixedThreadPool(10);
Result foo() {
    try {
        var fut = es.submit(() -> callLimitedService());
        return f.get();
    } catch (...) { ... }
}
```

### Virtual threads prefer Scoped Value over thread-local variables

[Scoped Value](./Scoped%20Value.md)

Note that using thread-local variables to cache shared expensive objects is sometimes done behind the scenes by asynchronous frameworks, under their implicit assumption that they are used by a very small number of pooled threads. This is one reason why mixing virtual threads and asynchronous frameworks is not a good idea: a call to a method may result in instantiating costly objects in thread-local variables that were intended to be cached and shared.

### Avoid long-lived and frequent use of a `syncrhonized`



```java
// before
synchronized(lockObj) {
    frequentIO();
}

// after
lock.lock();
try {
    frequentIO();
} finally {
        lock.unlock();
}
```

## With GC

- The stacks of virtual threads are stored in Java's garbage-collected heap as **stack chunk objects**.
- Unlike platform thread stacks, virtual thread stacks are not GC roots. Thus the references they contain are not traversed in a stop-the-world pause by garbage collectors




## References

> https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html#GUID-2BCFC2DD-7D84-4B0C-9222-97F9C7C6C521
