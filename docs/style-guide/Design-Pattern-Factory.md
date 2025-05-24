# Design Pattern

## Factory Method

Define a interface for creating an object. Subclasses will decide which class to instantiate.

#### Advantages

- Decouple object creation from usage.
- The factory method can be extended to include object pooling or reuse mechanisms, allowing the system to return existing instances instead of creating new ones each time.

#### Scenario Examples

- Using a database **connection pool** to manage and reuse DB connections efficiently
- Managing threads with a **thread pool** to reduce the overhead of creating new threads
- Reusing instances for the creation of **expensive objects** (e.g., large data structures or rendering resources)

## Abstract Factory

Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

#### why

- Decouple object creation from usage
- Isolate concrete classes

## Code Examples of Factory

```java
// Product
interface Product {
    void use(); // A generic action for the product
}
```

```java
// Concrete Product 1
class ConcreteProductA implements Product {
    @Override
    public void use() {
        System.out.println("Using ConcreteProductA.");
    }
}

// Concrete Product 2
class ConcreteProductB implements Product {
    @Override
    public void use() {
        System.out.println("Using ConcreteProductB.");
    }
}
```

```java
// Creator (Abstract Class)
abstract class ProductFactory {
    // The factory method
    public abstract Product createProduct();

    // An operation that uses the product created by the factory method
    public void doSomethingWithProduct() {
        Product product = createProduct(); // The magic happens here
        System.out.print("Factory is now: ");
        product.use();
    }
}
```

```java
// Concrete Creator 1
class ConcreteProductAFactory extends ProductFactory {
    @Override
    public Product createProduct() {
        return new ConcreteProductA();
    }
}

// Concrete Creator 2
class ConcreteProductBFactory extends ProductFactory {
    @Override
    public Product createProduct() {
        return new ConcreteProductB();
    }
}
```

```java
public class SimpleProductFactoryMethodDemo {
    public static void main(String[] args) {
        ProductFactory factoryA = new ConcreteProductAFactory();
        factoryA.doSomethingWithProduct();
        // Output: Factory is now: Using ConcreteProductA.

        ProductFactory factoryB = new ConcreteProductBFactory();
        factoryB.doSomethingWithProduct();
        // Output: Factory is now: Using ConcreteProductB.

        // You can also get the product directly if needed
        Product myProductA = factoryA.createProduct();
        System.out.print("Directly created: ");
        myProductA.use(); // Output: Directly created: Using ConcreteProductA.
    }
}
```