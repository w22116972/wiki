# Structured Concurrency

> https://openjdk.org/jeps/428

treats groups of related tasks running in different threads as a single unit of work.

### Why

Sequential implementation
```java
public String handle(String left, String right) throws Exception {
    String leftResult = getDataFromWebService(left);
    String rightResult = getDataFromDatabase(right);
    return Stream.of(leftResult, rightResult)
        .collect(Collectors.joining(","));
}
```

Virtual thread implementation
```java
public String handle(String left, String right) throws Exception {
    try (var executor = Executors.newVirtualThreadExecutor()) {
        String leftResult = executor.submit(() -> getDataFromWebService(left)).get();
        String rightResult = executor.submit(() -> getDataFromDatabase(right)).get();
        return Stream.of(leftResult, rightResult)
            .collect(Collectors.joining(","));
    }
}
```
- Problem: if there is a failure, it still needs to wait for other tasks to finish

Structured concurrency implementation: short-circuiting patterns
```java
public String handle(String left, String right) throws Exception {
    // ShutdownOnFailure cancels all subtasks if one of them fails
    try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
        Subtask<String> subtask1 = scope.fork(() -> getDataFromWebService(left));
        Subtask<String> subtask2 = scope.fork(() -> getDataFromDatabase(right));
        scope.join();
        scope.throwIfFailed();
        return Stream.of(subtask1, subtask2)
                .map(Subtask::get)
                .collect(Collectors.joining(","));
    }
}
```



## References

> https://www.youtube.com/watch?v=0mXGfsy7_Qo
