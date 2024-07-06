# Interview Template

## 1. Understand problem and design scope

### 1-1. Functional Requirement (What system will do)

Ask
- Who are the users?
  - users? other services?
- How the system will be used?
  - website? mobile app? API?
- What are the main features?

### 1-2. Non-Functional Requirement (How system will do)

Ask
- Back-of-the-envelope estimation
  - Users, QPS
  - Storage/Memory size and cost
  - Network bandwidth usage
- Scalability (QPS)
- Availability (SLA)
  - 99.99%?
  - Fault tolerant
  - No single point of failure
- Consistency
  - Strong consistency? Eventual consistency? Read your own write consistency? 
- Latency

### 1-3. List design goals based on requirements

## 2. High Level Design

- API Design
- Define data models
  - Database models
  - Message data models

### Draw diagrams

- UML for services
- ERD for database models

## 3. Deep Dive into Components (Detailed Design)

### Pick components that you feel are important in designing the system.
- requests and response for critical paths
- schema, data models
- breakdown of logic and functionality of a single component

### ### Identify and solve potential scaling problems and bottlenecks

- load balancing
- caching
- sharding
- horizontal scaling

