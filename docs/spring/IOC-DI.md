# Inversion of control, dependency injection in Spring

#### Inversion of control (IOC)

A design principle that object creation and dependency is handled by framework not application code
- e.g. Receive the object from external source instead of using `new` to create a class


#### Dependency Injection

A design pattern implements IoC
- inject the dependencies from constructor, setter, or field

#### Real-world Analogy

- Without IoC: The Car class creates its own Engine – tightly coupled and hard to replace or test.
- With DI: The Engine is provided to the Car externally. Now you can easily switch from a petrol engine to an electric one without changing the car's logic.

#### Advantages

- Loose Coupling: Classes depend on interfaces rather than concrete implementations
- Easier Testing: To inject mock dependencies for unit testing
- Better Maintainability: Changes in dependencies don’t require changes in the dependent class
- Easier Configuration: Manage object lifecycles declaratively by annotations

#### In Spring

- Spring IoC container (`ApplicationContext` or `BeanFactory`) is handling the control

Spring registers beans in IoC container in two ways
- Component scanning using annotations like @Component, @Service, @Repository, and @Controller. These are placed on class definitions, and Spring automatically detects them during classpath scanning
- Explicit bean declaration using @Bean methods inside a @Configuration-annotated class. This gives you more control over how the bean is created, especially for third-party or external library classes that you can't annotate directly.

#### when to use

- Use `@Component` and related annotations when the class is under your control and fits the standard application logic.
- Use `@Bean` methods when:
    - You need more fine-grained control (e.g., custom initialization logic).
    - You're dealing with external libraries or classes you cannot annotate.
    - You need to pass parameters to the constructor or method while creating the bean.

#### main Stages of Spring Bean Life Cycle

1. **Instantiation**
   - Spring creates the bean instance using the constructor or a factory method.

2. **Populate Properties (Dependency Injection)**
   - Spring injects dependencies via constructor, setters, or fields (`@Autowired`, etc.).

3. **Aware Interfaces (optional)**
   - If the bean implements interfaces like `BeanNameAware`, `ApplicationContextAware`, etc., Spring calls the corresponding methods to give the bean access to container internals.

4. **Post-processing**
   - Spring calls any `BeanPostProcessor` implementations' `postProcessBeforeInitialization()` method.

5. **Initialization**
   - If the bean:
     - Implements `InitializingBean`, Spring calls `afterPropertiesSet()`.
     - Has a method annotated with `@PostConstruct`, Spring calls it.
     - Has a custom init method defined in XML or `@Bean(initMethod = "init")`, Spring calls it.

6. **Post-Initialization**
   - Spring calls `postProcessAfterInitialization()` from any `BeanPostProcessor`s.

7. **Ready to Use**
   - The bean is now fully initialized and available for use by the application.

8. **Destruction**
   - On application shutdown:
     - If the bean implements `DisposableBean`, Spring calls `destroy()`.
     - If a custom destroy method is defined (e.g., `@Bean(destroyMethod = "cleanup")`), Spring calls it.
     - If `@PreDestroy` is present, the annotated method is called.
