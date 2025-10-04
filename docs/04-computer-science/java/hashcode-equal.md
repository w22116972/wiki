# `hashcode()`, `==`, `equals()`

| Type                        | `==` Compares | `.equals()` Compares     | Use Case                              |
|-----------------------------|---------------|---------------------------|----------------------------------------|
| `int`, `float`, etc.        | Values        | Not available             | `==` is correct                        |
| `Integer`, `String`, custom objects | References    | Logical values (if overridden) | Use `.equals()`                        |
| Object keys in `HashMap`    | Not suitable  | Must override `equals()` & `hashCode()` | Required for correctness in collections |


## `==`: Reference equality for non-primitive, logic equality for primitive

- compare memory address

```java
String a = new String("test");
String b = new String("test");
System.out.println(a == b); // false
```

## `equals()`: logical equality

> If a.equals(b) returns true, then a.hashCode() == b.hashCode() must also be true.

#### rules required to be followed when overriding `equals`

- Reflexive: x.equals(x) must be true
- Symmetric: x.equals(y) ⇔ y.equals(x)
- Transitive: if x.equals(y) and y.equals(z), then x.equals(z)
- Consistent: repeated calls return the same result (if object state doesn’t change)
- Non-null: x.equals(null) must be false

#### when trying to override `equals`

Always ensure that overriding hashCode() as well, using consistent fields, to maintain the hash contract and avoid broken behavior in hash-based collections.

## `hashcode()`

> Design to support hash-based collection

Collections like HashMap, HashSet, and ConcurrentHashMap use hashCode() to find the bucket before using equals() to check for actual key equality.

If two logically equal objects have different hash codes, they will go to different buckets, and the map or set will fail to find the key — even though equals() says they are equal.

The objects in the same bucket has the same hashcode, and using `equals` to find specific object.

#### rules required to be followed when overriding

- If a.equals(b) returns true, then a.hashCode() == b.hashCode() must also be true.
- return the same value every time it's called
- use good hashing to ensure distributing uniformly
