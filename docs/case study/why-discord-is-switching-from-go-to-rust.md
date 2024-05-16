# Why Discord is switching from Go to Rust

> https://discord.com/blog/why-discord-is-switching-from-go-to-rust

## Background

"Read State" service is to keep track of which channels and messages you have read.
- Read States is accessed every time you connect to Discord, every time a message is sent and every time a message is read.
- There is one Read State per User per Channel. Each Read State has several counters that need to be updated atomically and often reset to 0

Each Read States server has an LRU cache of Read States
- Tens of millions of Read States in each cache.
- Hundreds of thousands of cache updates per second.

## Problem

**Read State** service has large latency spikes every few minutes due to garbage collection

In Go, on cache key eviction, memory is not immediately freed



