## How to Answer in a System Design Interview

1. **For a read-heavy system**, consider using a cache.
2. **For a write-heavy system**, use message queues for asynchronous processing.
3. **For low latency requirements**, consider using a cache and a CDN.
4. **If atomicity, consistency, isolation, and durability (ACID) compliance is needed**, go for an RDBMS/SQL database.
5. **For unstructured data**, use a NoSQL database.
6. **For complex data (videos, images, files)**, go for blob/object storage.
7. **For complex pre-computation**, use message queues and a cache.
8. **For high-volume data search**, consider search indices or a search engine.
9. **For scaling an SQL database**, implement database sharding.
10. **For high availability, performance, and throughput**, use a load balancer.
11. **For global data delivery**, consider using a CDN.
12. **For graph data (data with nodes, edges, and relationships)**, utilize a graph database.
13. **For scaling various components**, implement horizontal scaling.
14. **For high-performing database queries**, use database indexes.
15. **For bulk job processing**, consider batch processing and message queues.
16. **For server load management and preventing DOS attacks**, use a rate limiter.
17. **For a microservices architecture**, use an API gateway.
18. **To avoid a single point of failure**, implement redundancy.
19. **For fault tolerance and durability**, implement data replication.
20. **For user-to-user fast communication**, use WebSockets.
21. **For failure detection in distributed systems**, implement a heartbeat.
22. **For data integrity**, use a checksum algorithm.
23. **For efficient server scaling**, implement consistent hashing.
24. **For decentralized data transfer**, consider the gossip protocol.
25. **For location-based functionality**, use quadtree or geohash, etc.
26. **Avoid specific technology names**; use generic terms.
27. **For high availability and consistency trade-off**, consider eventual consistency.
28. **For IP resolution and domain name query**, mention DNS (Domain Name System).
29. **For handling large data in network requests**, implement pagination.
30. **For cache eviction policy**, prefer LRU (Least Recently Used) cache.
