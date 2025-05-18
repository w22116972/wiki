# SOLID Principle in Java

## Single Responsibility (SRP)

> A class should have only one reason to change, which corresponds to one role

Bad example
```java
public class Invoice {
    public void calculateTotal() { ... } // business logic
    public void saveToDatabase() { ... } // persistence logic
    public void printInvoice() { ... }   // presentation logic
}
```

Good Example
```java
class Invoice {
    public BigDecimal calculateTotal() { ... }
}

class InvoiceRepository {
    public void save(Invoice invoice) { ... }
}

class InvoicePrinter {
    public void print(Invoice invoice) { ... }
}
```

---

## Open/Closed Principle''

> You should be able to add new functionality by adding code, not by modifying existing classes

```java
public interface Notification {
    void send(String message);
}

public class EmailNotification implements Notification {
    public void send(String message) {
        // send email
    }
}

public class SMSNotification implements Notification {
    public void send(String message) {
        // send SMS
    }
}

public class NotificationService {
    private Notification notification;

    public NotificationService(Notification notification) {
        this.notification = notification;
    }

    public void notifyUser(String message) {
        notification.send(message);
    }
}
```
You can add new notification types without modifying NotificationService.

---

## iskov Substitution Principle (LSP)

> A subclass should be usable anywhere its superclass is expected, without causing bugs or incorrect behavior.

Examle: `Rectangle` should not inherit `Square`, they should both inherit `Shape`. Because their area are different given same width and height.
```java

```

---

## Interface Segregation Principle (ISP)

> No client should be forced to depend on methods it does not use

```java
// BAD: too many responsibilities
interface Worker {
    void work();
    void eat();
}

// GOOD: split interfaces
interface Workable {
    void work();
}

interface Eatable {
    void eat();
}

class HumanWorker implements Workable, Eatable {
    public void work() { ... }
    public void eat() { ... }
}

class RobotWorker implements Workable {
    public void work() { ... }
}
```

---

# Dependency Inversion Principle (DIP)

> High-level modules should not depend on low-level modules. Both should depend on abstractions.

Bad exmaple
```java
public class MySQLDatabase {
    public void save(String data) {
        System.out.println("Saving to MySQL: " + data);
    }
}

public class ReportService {
    private MySQLDatabase db = new MySQLDatabase(); // directly depends on concrete class
}
```

Good example
```java
public interface Database {
    void save(String data);
}

public class MySQLDatabase implements Database {
    public void save(String data) {
        System.out.println("Saving to MySQL: " + data);
    }
}

public class InMemoryDatabase implements Database {
    public void save(String data) {
        System.out.println("Pretend saving to memory: " + data);
    }
}

public class ReportService {
    private final Database db;

    public ReportService(Database db) {
        this.db = db;
    }
}
```