# Check MySQL index usage statistics

## Solution: `INFORMATION_SCHEMA` 

```sql
SELECT 
    TABLE_SCHEMA,
    TABLE_NAME,
    INDEX_NAME,
    SEQ_IN_INDEX,
    COLUMN_NAME,
    CARDINALITY,
    INDEX_TYPE,
    NON_UNIQUE
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = 'your_database_name';
```

## Solution: `EXPLAIN`

```sql
EXPLAIN SELECT * FROM your_table WHERE indexed_column = 'value';
```


## Solution: `performance_schema`

```sql
SELECT 
    OBJECT_SCHEMA,
    OBJECT_NAME,
    INDEX_NAME,
    COUNT_FETCH AS `Index Fetch Count`,
    COUNT_INSERT AS `Index Insert Count`,
    COUNT_UPDATE AS `Index Update Count`,
    COUNT_DELETE AS `Index Delete Count`
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE OBJECT_SCHEMA = 'your_database_name';

```

## Solution: Querying Slow Query Log

Enable and review the Slow Query Log to find queries that are not using indexes effectively:

Enable the slow query log:

```sql
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1; -- Log queries longer than 1 second
```

Analyze the slow query log file to identify queries missing indexes.

## Solution: `ANALYZE TABLE`

```sql
ANALYZE TABLE your_table_name;
```



