# Index

> lookup table (data structure) that enhances the speed of data retrieval operations in a database

- contains a copy of specific columns from the table, along with pointers to the full records
    - allow the database to quickly jump to the relevant data when a query uses the indexed column

## Principle

#### Write

- INSERT: New indexed key values are added to the B-Tree. The index finds the correct leaf node location to maintain sort order. The key value and its data address are stored. If the leaf node is full, it may split, potentially propagating up the tree to maintain balance.
- UPDATE: If an indexed column is updated, it's treated as a deletion of the old key value and an insertion of the new one. The old index entry is removed, and the new key value with its data address is added according to the insert logic.
- DELETE: When a row is deleted, its corresponding indexed key value is removed from the B-Tree. The index locates the leaf node containing the key and deletes the entry. If a node becomes too sparse after deletion, it might merge with another or redistribute keys to maintain balance and space efficiency.