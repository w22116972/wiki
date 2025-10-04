# Nanoseconds Tier Optimizations



## Branchless in C++

> https://www.youtube.com/watch?v=g-WPhYREFjk


### use `|`, `&` to replace  `||`, `&&`

short-circuiting: use `&&`
```java
public int processData(Data data, int total) {
    if (data.valueA > 0 && data.valueB > 0) {
        total += 100;
    }
    return total;
}
```

bitwise operators: use `&`
```java
public int processData(Data data, int total) {
    boolean isAPositive = data.valueA > 0;
    boolean isBPositive = data.valueB > 0;
    boolean bothArePositive = isAPositive & isBPositive;
    int flag = bothArePositive? 1:0;
    total += 100 * flag;
    return total;
}
```


### use index array to replace condition

if condition
```java
String result;
if (true) {
    result = "true";
} else {
    result = "false";
}
return result;
```

index array
```java
Stringp[] results = {"true", "false"};
int conditionIndex = (true)? 1:0;
return results[conditionIndex];
```

### use data-oriented to replace interface

- using interface requires JVM to lookup real object during runtime

interface
```java
interface Shape {}
class Circle implements Shape {}
class Square implements Shape {}
public double calculate(List<Shape> ss) {...}
```

data-oriented
```java
enum ShapeType {CIRCLE, SQUARE}
class CircleData {}
class SquareData {}
public double calculate(List<CircleData> cs, List<SquareData> ss) {...}
```
