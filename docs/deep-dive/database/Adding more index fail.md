# Adding more index fail

## Problem: Resource Constraints: Limited memory/storage

### Situation:
- Load large indexes into insufficient memory for query execution
- Indexes require additional storage space and database server has limited disk capacity

### Solutions:
- Drop unused or redundant indexes based on index usage statistics
- Upgrade hardware
- Use batched writes to minimize the frequency of index updates.
- Use partial or filtered indexes that apply only to specific subsets of data.

## Problem: Index key length exceeds database limits


## Problem: Maximum number of indexes per table exceeded
