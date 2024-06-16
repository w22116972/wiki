# Oracle Secure Coding Guidelines for Java

### If a constructor/method is used to perform input validation, be sure to use the created/returned object and not the original input

Should always use the safe created object and not the original input. Because the original input may be unsafe.

```java
public class Main {
    public static void main(String[] args) {
        String unsafeInput = "hello<script>alert('xss')</script>";
        
        // 使用 SafeString 對象
        SafeString safeString = new SafeString(unsafeInput);

        // 打印原始輸入（不安全）
        System.out.println("Original input: " + unsafeInput);

        // 打印過濾後的值（安全）
        System.out.println("Sanitized value: " + safeString.getValue());
    }
}

```

### Avoid integer overflow

```java
// Is possible to overflow
if (current + extra > max)
// Is safe
if (current > max - extra)
```

Since `Integer.MIN_VALUE == -Integer.MIN_VALUE`

Use `java.lang.Math.addExact`, etc
```java
public class ExactArithmeticExample {
    public static void main(String[] args) {
        try {
            int minInt = Integer.MIN_VALUE;
            int negated = Math.negateExact(minInt);
            System.out.println("Negated value: " + negated);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: integer overflow when negating Integer.MIN_VALUE");
        }

        try {
            int minInt = Integer.MIN_VALUE;
            int absValue = Math.absExact(minInt);
            System.out.println("Absolute value: " + absValue);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: integer overflow when calculating absolute value of Integer.MIN_VALUE");
        }
    }
}
```

### Validate output from untrusted upcall (invoking a method of higher level code)

```java

public class JsonParser {
    private ObjectMapper objectMapper;

    public JsonParser() {
        this.objectMapper = new ObjectMapper();
    }

    public MyData parse(String jsonData) throws JsonProcessingException {
        // validate input
        if (jsonData == null || jsonData.trim().isEmpty()) {
            throw new IllegalArgumentException("JSON data cannot be null or empty");
        }
        
        // invoking a method of higher level code
        MyData data = objectMapper.readValue(jsonData, MyData.class);

        // validate output from untrusted upcall
        if (data == null || data.getId() == null || data.getName() == null) {
            throw new IllegalStateException("Parsed data is invalid");
        }

        return data;
    }
}
```

### Create copies of mutable data

If a method returns a reference to an internal mutable object, client code can change the instance's internal state. To avoid this, unless you intend to share the state, copy the mutable object and return the copy.

```java
public class CopyOutput {
    private final java.util.Date date;
    
    public java.util.Date getDate() {
        return (java.util.Date)date.clone();
    }
}

public final class CopyMutableInput {
    private final Date date;
    
    // Constructors should complete the deep copy before assigning values to a field
    public CopyMutableInput(Date date) {
        this.date = new Date(date.getTime());
    }
}
```

For collection, if the elements are mutable, then **deep copy**.

```java
// Date is mutable.
public void deepCopy(Collection<Date> dates) {
    Collection<Date> datesCopy = new ArrayList<>(dates.size());
    for (Date date : dates) {
        datesCopy.add(new java.util.Date(date.getTime()));
    }
    doLogic(datesCopy);
}
```

For collection, if the elements are immutable, then shallow copy (can be modified independently) or read-only view.

Use `Collections.unmodifiableList` to create a read-only view of the list, ensuring that any changes to the original list will be reflected in the unmodifiable list. However, the unmodifiable list itself cannot be modified.
This approach is particularly suitable for use in getter methods.

```java
public List<String> getItems() {
    return Collections.unmodifiableList(items);
}

// Shallow copy
public void shallowCopy(Collection<String> strs) {
    strs = new ArrayList<>(strs);
    doLogic(strs);
}
```


When designing a mutable value class, provide one of the following ways to create safe copies of its instances
```java
public class MutableValue {
    // 1. Constructors for creating safe copies
    public MutableValue(List<String> items) {
        this.items = new ArrayList<>(items);
    }
    
    public MutableValue(MutableValue other) {
        this.items = new ArrayList<>(other.items);
    }

    // 2. Static methods for creating safe copies
    public static MutableValue create(List<String> items) {
        return new MutableValue(items);
    }
    
    // 3. Public copy method
    public MutableValue copy() {
        return new MutableValue(new ArrayList<>(this.items));
    }
}
```

### Only use non-overridable methods in constructor e.g. `final`, `static`, or `private` methods 

To avoid attackers from overriding the method to perform malicious activities during object construction

### `class`/`interface` is `public` only if it is part of a published API otherwise `package-private`


### `class` is either `final` or `abstract`

Limit the extensibility of classes and methods

`class` is either `final` or `abstract` to prevent malicious subclasses from overriding methods(e.g. finalizers, cloning, etc.)

note: why subclass of non-final class overrides `clone` is bad because cloning results are in a shallow copy, sharing referenced objects but having different fields and separate intrinsic locks.


## References

> https://www.oracle.com/java/technologies/javase/seccodeguide.html
