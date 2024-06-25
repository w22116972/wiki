# Unique ID generator

### sol:  128-bit UUIDs

- every server is easy to generate a unique ID

Challenge: not sortable

### sol: Snowflake

64-bit ID
- 1 bit for sign
- 41 bits for time in milliseconds
- 5 bits for a machine id
- 5 bits for a data center id
- 12 bits for a sequence number
  - in same machine same process, sequence number is incremented
  - at most 4096 unique IDs per millisecond

The bit size is not fixed, it can be adjusted based on the requirement.

Challenge: Depends on system clock
- if the system clock is rolled back, then the system will generate duplicate IDs
  - Solution: Implement logic to detect clock rollbacks. Maintain the sequence number progression even if the timestamp is earlier, ensuring IDs remain unique as long as the sequence number hasn't wrapped around.
- if in the multicore system, then the system will generate duplicate IDs
  - Solution: Ensure each core/thread has isolated instances of the ID generator or uniquely identify each generator instance with its own worker ID. This way, no two cores can produce the same ID, even if they operate at the same exact millisecond.
- use NTP to synchronize the system clock

### Universally Unique Lexicographically Sortable Identifier (ULID)

> https://github.com/ulid/spec

- sortable UUID

