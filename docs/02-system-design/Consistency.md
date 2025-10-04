# Consistency

## Strong Consistency/Linearizability

Any replicas will get the latest write value
- has ordering
- read-your-write/read-after-write

## Sequential Consistency
> The result of any execution is the same as if the (read and write) operations by all proceses on the data-store were executed in the same sequential order and the operations of each individual process appear in this sequence in the order specified by its program.

A write to a variable does not have to be seen instantaneously, however, writes to variables by different processors have to be seen in the same order by all processors.

- has total ordering
  - writes to vari
- no read-your-write/read-after-write

note: 因果一致性和順序一致性之間的主要區別在於它們如何處理不相關的操作。 因果一致性模型允許不相關的操作以任何順序出現，而順序一致性模型要求所有操作都按照客戶端程式中指定的順序出現。

## Casual Consistency
> Writes that are potentially causally related must be seen by all processes in the same order.
Concurrent writes (i.e. writes that are NOT causally related) may be seen in a different order by different processes.

Causal relationships ensure own writes are visible.
- not total ordering
- read-your-write/read-after-write
  - i.e. related operations are ordered


## Eventual Consistency

> ensure high availability

All the replicas converge on a final value after a finite time and when no more writes are coming in. If new writes keep coming, replicas of an eventually consistent system might never reach the same state. Until the replicas converge, different replicas can return different values.
- no strict ordering
- no read-your-write/read-after-write


---

Replication data
- reliability: continue working after one replica crashes
- performance: read replicas, geo-distributed replicas

---

### References

> M. van Steen and A.S. Tanenbaum, Distributed Systems, 4th ed., distributed-systems.net, 2023.
