# Dynamic Dependency Injection on Jakarta, Jersey


## Quick Selection Guide

**Choose Strategy Pattern when**: You have a known, static set of implementations with simple selection logic

**Choose Factory Pattern when**: Selection logic is complex and involves multiple business criteria

**Choose Provider Pattern when**: Object creation is expensive and should be conditional

**Choose Registry Pattern when**: You need plugin-like extensibility and dynamic discovery

**Choose Configuration-Driven when**: You need to change behavior without code changes

---


## Decision Matrix

| **Criteria** | **Strategy Map/List** | **Factory Pattern** | **Provider Pattern** | **Registry Pattern** | **Configuration-Driven** |
|--------------|----------------------|-------------------|-------------------|-------------------|------------------------|
| **Selection Complexity** | Simple | Complex | Simple | Medium | Simple |
| **Performance** | Fastest | Fast | Medium | Fast | Fast |
| **Runtime Changes** | No | No | No | Yes | Yes |
| **Memory Usage** | All loaded | All loaded | Lazy | All loaded | All loaded |
| **Testability** | Excellent | Excellent | Good | Good | Excellent |
| **Configuration Dependency** | No | Optional | No | No | Yes |

---

## 1. Strategy Pattern with Map/List Injection

### Implementation
- **Map Injection**: `@Inject Map<String, Interface> strategies` - select by name/key
- **List Injection**: `@Inject List<Interface> strategies` - iterate and filter by capability
- Register implementations with `@Named("key")` or bind with names in AbstractBinder

### When to Use
- **Known set of implementations** that you want to select from at runtime
- **Simple selection logic** based on string keys or boolean conditions
- **Static set of strategies** that won't change during application runtime
- You need **fast lookup** performance with O(1) map access

### Example Scenarios
- Notification systems (email, SMS, push)
- Payment processors by type
- File format handlers (PDF, Excel, CSV)

---

## 2. Factory Pattern with Injected Dependencies

### Implementation
- Create factory interface with business method like `createService(criteria)`
- Factory constructor receives **all possible implementations** via injection
- Factory method contains **business logic** to decide which implementation to return

### When to Use
- **Complex selection logic** that can't be expressed with simple key-based lookup
- **Multiple criteria** needed for selection (tenant + region + feature flags)
- **Business rules** change frequently and need to be centralized
- You need to **create new instances** rather than reusing singletons

### Example Scenarios
- Multi-tenant database selection
- Region-specific service providers
- Feature flag driven implementations
- A/B testing service selection

---

## 3. Provider Pattern for Conditional Creation

### Implementation
- Inject `Provider<ExpensiveService>` instead of `ExpensiveService` directly
- Call `provider.get()` only when certain conditions are met
- Each call to `get()` can create new instance or return cached one

### When to Use
- **Expensive object creation** that should only happen when actually needed
- **Conditional instantiation** based on runtime parameters
- **Circular dependency resolution** when two services depend on each other
- **Lazy loading** of heavy resources until first usage

### Example Scenarios
- Database connections for large reports
- Machine learning model loading
- External API client initialization
- Heavy computation services

---

## 4. Registry Pattern

### Implementation
- Create registry that receives `List<Interface>` via constructor injection
- Registry auto-registers all implementations with their names/keys
- Provide `get(name)`, `getAll()`, and `register(name, impl)` methods

### When to Use
- **Plugin architecture** where implementations can be added/removed
- **Dynamic registration** of services at runtime
- **Discovery mechanism** to find all available implementations
- **Extensible systems** where new implementations are added frequently

### Example Scenarios
- Validation plugin system
- Data transformation plugins
- Custom authentication providers
- Report generator plugins

---

## 5. Configuration-Driven Selection

### Implementation
- Combine **Map injection** with **ConfigurationService** injection
- Use configuration properties to determine which implementation to select
- Provide fallback to default implementation when configuration is missing

### When to Use
- **Environment-specific implementations** (dev vs prod services)
- **Runtime behavior changes** without code deployment
- **Feature toggles** to switch between implementations
- **A/B testing** or gradual rollouts of new implementations

### Example Scenarios
- Development vs production notification services
- Database selection per environment
- Feature flag controlled processors
- Regional service implementations

---
