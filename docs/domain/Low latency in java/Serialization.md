# Serialization

## Abstract

Convert short text String into Long to reduce memory usage and GC overhead

## Problem

- String has a lot of overhead of memory usage
- String is immutable, object pooling tends to create many objects for GC in initialization and deserialization

## Solution 1: Base-85 Encoding

encode up to 10 characters in a 64-bit long

## Solution 2: Nanosecond Timestamps

encode a yyyy/MM/dd’T’sss.SSSSSSSSS into a 64-bit long

## References

> https://dzone.com/articles/improving-serialization-and-memory-efficiency
