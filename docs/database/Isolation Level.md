# Database Isolation Level 

Database has ACID including Isolation. It decides how and when changes made by one transaction

| Isolation Level        | Dirty Read | Non-repeatable Read | Phantom Read |
|------------------------|------------|----------------------|---------------|
| READ_UNCOMMITTED       | Yes        | Yes                  | Yes           |
| READ_COMMITTED         | No         | Yes                  | Yes           |
| REPEATABLE_READ        | No         | No                   | Yes           |
| SERIALIZABLE           | No         | No                   | No            |

#### Concurrency Problems Table

| Concurrency Problem | Description                                     | Caused By                     | Example Scenario                                           | Severity | Typical Fix                         |
| ------------------- | ----------------------------------------------- | ----------------------------- | ---------------------------------------------------------- | -------- | ----------------------------------- |
| Dirty Read          | Reads uncommitted data from another transaction | Read before commit            | T1 updates balance; T2 reads it before commit              | High     | Use READ COMMITTED or higher        |
| Non-repeatable Read | Reads same row twice with different results     | Update between reads          | T1 reads user name; T2 updates and commits; T1 reads again | Medium   | Use REPEATABLE READ or SERIALIZABLE |
| Phantom Read        | Gets different result set from identical query  | Insert/delete between queries | T1 queries "WHERE age > 30", T2 inserts matching row       | Medium   | Use SERIALIZABLE or predicate locks |

#### Isolation Levels Table

| Isolation Level  | Description                            | Prevents                    | Allows                               | Performance Impact  | Use Case                                     |
| ---------------- | -------------------------------------- | --------------------------- | ------------------------------------ | ------------------- | -------------------------------------------- |
| READ UNCOMMITTED | Allows all reads including uncommitted | None                        | Dirty, non-repeatable, phantom reads | Very low (fast)     | Analytics with no consistency need           |
| READ COMMITTED   | Reads only committed data              | Dirty reads                 | Non-repeatable, phantom reads        | Low                 | General use cases (e.g., PostgreSQL default) |
| REPEATABLE READ  | Locks rows for the duration            | Dirty, non-repeatable reads | Phantom reads                        | Medium              | Financial or reporting systems               |
| SERIALIZABLE     | Full transaction isolation             | All 3 problems              | None                                 | High (most locking) | Inventory, booking systems                   |
