# Join Large Dataset > 100 TBs/hr

## Abstract

Use either Broadcast Join or Sorted Bucket Join to avoid shuffling large datasets.

## Broadcast Join

1. Identify the smaller dataset(< 10 GB): Determine which of the two datasets is smaller and can be efficiently broadcasted.
2. Broadcast the smaller dataset: Distribute the smaller dataset to all worker nodes in the cluster.
3. Perform the join on each worker node: Each worker node performs the join operation locally between its partition of the larger dataset and the broadcasted smaller dataset.
4. Collect the results: Gather the results from all worker nodes to form the final joined dataset.

## Sorted Bucket Join

1. Sort both datasets by the join key: Ensure both datasets are sorted based on the key that will be used for the join operation.
2. Partition both datasets into buckets: Divide each sorted dataset into buckets, ensuring that records with the same join key end up in the same bucket.
3. Shuffle the buckets to the same worker node: Distribute the buckets across worker nodes, making sure that corresponding buckets from both datasets are located on the same node.
4. Join the buckets on the same worker node: Perform the join operation on the corresponding buckets located on the same worker node.
5. Merge the results: Combine the results from the join operations performed on each worker node.

note: Sort should be prepared in advance, so it is not included in the processing time.

## References

> https://www.youtube.com/watch?v=g23GHqJje40
