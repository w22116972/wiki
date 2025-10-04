# Thread Safe

To ensure thread safe, you need to have **atomicity**, **visibility**, **ordering**

## Atomicity

> An operation is atomic if **other threads can only observe it as either not yet started or fully completed**, never in an intermediate state. It's an indivisible unit from the perspective of other threads.

### Java's Built-in Atomicity Rules

- Read operations for all variables are guaranteed to be atomic
    - e.g. `x = a;`, you will not see x having read only the first 32 bits of a while the remaining 32 bits were not yet read
- Write operations for types other than long and double are guaranteed to be atomic
    - e.g. `long` or `double` variables in 32-bits JVM, it might write lower 32-bits first then upper

### Race condition on atomicity 

#### Check-Then-Act

```java
// Example 1: check cache key
if (!map.containsKey(key)) {
    // other thread may put key value to map at this moment
    map.put(key, value);
}
```

```java
// Example 2: Lazy initialization
@NotThreadSafe
public class LazyInitRace {
    private ExpensiveObject instance = null;
    public ExpensiveObject getInstance() {
        if (instance == null)
            instance = new ExpensiveObject();
        return instance;
    }
}
```

Solution: Wrap composite operation into a single atomic operation
- `synchronized ExpensiveObject getInstance()`
- Initialization-on-demand holder idiom / Bill Pugh Singleton

```java
public class LazyInitHolder {
    private LazyInitHolder() {} // Private constructor

    private static class Holder {
        static final ExpensiveObject INSTANCE = new ExpensiveObject();
    }

    public static ExpensiveObject getInstance() {
        return Holder.INSTANCE;
    }
}
```

#### Read-Modify-Write

```java
count++;
```

In implementation, it has 3 steps
1. `load(count, register)`
2. `increment(register)`
3. `store(count, register)`

Solution: use `AtomicInteger`

## Visibility

> Visibility ensures that when one thread modifies a shared state, other threads are able to observe these changes.

### Issue

- For multi-processor/multi-core: data could be written to CPU register or processor cache before reaching main memory or shared cache level, it might be invisible to other threads
- For single-processor: if updated data is in register and context switch happens, then other threads won't see the latest updated data

```java
@NotThreadSafe
public class MutableInteger {
    private int value;
    public int get() { return value; }
    public void set(int value) { this.value = value; }
}
```

#### `volatile`

When one thread writes to a volatile variable, any subsequent read of that variable by any thread is guaranteed to see the value just written.

JVM inserts memory barriers around volatile accesses, which also enforce ordering:
- Before a volatile write, all preceding ordinary (non-volatile) writes must be flushed to main memory.
- After a volatile read, all subsequent ordinary reads must see up-to-date values from main memory.

These barriers prevent the compiler or CPU from reordering:

“the write/read of the volatile variable” with “ordinary reads/writes” across the barrier.

## Ordering

> Prevents unsafe reordering by the JIT, JVM, or CPU

#### 3 types of reordering

- RAW
- WAR
- WAW


#### Solution: Happen-before

volatile accesses, synchronized blocks (locks), and thread start/join aren’t just incidental features; they are the mechanisms by which the Java Memory Model defines and enforces happens-before relationships. In other words, they’re the “barriers” that prevent unsafe reordering and guarantee visibility.

volatile write → volatile read

A write to a volatile variable happens-before any subsequent read of that same variable.

This pair alone ensures that all memory writes before the volatile write become visible to the thread that does the volatile read.

Lock release → lock acquire

Exiting a synchronized(lock) block (the release) happens-before any subsequent entry to a synchronized(lock) block (the acquire) on the same monitor.

Guarantees that everything a thread did inside the synchronized is visible to the thread that next acquires that lock.

Thread start → thread run

A call to Thread.start() happens-before any action in the started thread.

Ensures the new thread sees all memory effects made by the spawning thread before start().

Thread termination → thread join

All actions in a thread happen-before another thread successfully returns from Thread.join() on that terminated thread.

Ensures that the joining thread sees everything the terminated thread did.