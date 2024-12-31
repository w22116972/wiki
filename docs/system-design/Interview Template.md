# Interview Template

## 1. Understand the Problem and Design Scope

### 1.1 Functional Requirements (What the System Will Do)

**Key Questions:**
- **Who are the users?**
  - End users? Other services?
- **How will the system be used?**
  - Through a website, mobile app, or API?
- **What are the main features?**

### 1.2 Non-Functional Requirements (How the System Will Operate)

**Key Questions:**
- **Back-of-the-Envelope Estimations:**
  - Number of users, QPS (Queries Per Second)
  - Storage/memory size and cost
  - Network bandwidth usage
- **Scalability:**
  - Can the system handle the expected QPS?
- **Availability:**
  - Target SLA (e.g., 99.99%)
  - Fault tolerance
  - Avoiding single points of failure
- **Consistency:**
  - Strong consistency? Eventual consistency? Read-your-own-write consistency?
- **Latency:**
  - What is the acceptable latency?
- **Data Size and Growth:**
  - What is the current size of the data?
  - At what rate is the data expected to grow over time?
- **Data Consumption:**
  - How will the data be consumed by other subsystems or end users?
- **Read vs. Write Load:**
  - Is the workload read-heavy or write-heavy?

### 1.3 Privacy and Regulatory Requirements

- What privacy and regulatory requirements apply for storing or transmitting user data?

### 1.4 Design Goals

**List design goals based on the functional and non-functional requirements.**

---

## 2. High-Level Design

### Key Design Elements:
- **API Design**
- **Data Models:**
  - Database models
    - Follow up: state which column should be [indexed](../domain/database/Index.md)
  - Message data models
- **Service Definitions:**
  - Outline the components of the system

### Visualize with Diagrams:
- **UML Diagrams:** For services and their interactions
- **ERD (Entity-Relationship Diagram):** For database schema

---

## 3. Deep Dive into Components (Detailed Design)

### 3.1 Discuss Trade-Offs

- Highlight the **pros and cons** of different components.
- Evaluate **costs** of various choices.
- Identify weaknesses in the design and explain **why** they haven’t been addressed yet.

### 3.2 Focus on Key Components

**Critical Aspects to Address:**
- Request and response flow for critical paths
- Schema and data models
- Detailed breakdown of logic and functionality for individual components

### 3.3 Solve Potential Scaling Problems and Bottlenecks

**Key Considerations:**
- Load balancing
- Caching
- Sharding
- Horizontal scaling

---

## 4. Additional Technical Considerations

### 4.1 Data Durability

- What’s the target durability for the data?

### 4.2 Consistency Requirements

- Do we need strict consistency, or will eventual consistency suffice?

### 4.3 Latency and Performance

- What are the acceptable latency and performance thresholds for key operations?

---
