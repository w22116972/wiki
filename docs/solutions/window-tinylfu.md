# Window TinyLFU

## Why not LRU

- only care about recency
- if there are massive one-time data, it will evict previous frequent-accessed data

## Window TinyLFU

- focus on recency and frequency

### components

- window cache: all new data stay here first
- TinyLFU filter (Count-Min Sketch): calculate frequency of all new data in window cache
- main cache: data which passed TinyLFU filter stay here

