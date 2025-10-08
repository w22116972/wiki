# MapReduce

### What is MapReduce?
MapReduce is a programming model and an associated implementation for processing and generating large data sets. 
- By defining a `map` function that processes a key/value pair to generate a set of intermediate key/value pairs, and a `reduce` function that merges all intermediate values associated with the same intermediate key.

### How does MapReduce work?

1. Client submits a job to the master(coordinator) node.
   - Input files: Files containing data to be processed
   - Output directory: Directory to write final outputs to
   - Desired application: Application to run on the given input files (e.g. word count)
   - Number of reduce tasks: Number of sets to divide mapped keys into
2. Coordinator node divides input files into M pieces and assigns them to worker nodes.
3. Worker nodes run the `map` function on each piece of data and produce a set of intermediate key/value pairs.
4. Coordinator node shuffles and sorts the intermediate key/value pairs to group them by key.
5. Coordinator node assigns the groups to the worker nodes to run the `reduce` function.
6. Worker nodes write the final output to the output directory.
7. Client waits for the job to finish and then retrieves the output.
8. Coordinator node returns the final output to the client.
