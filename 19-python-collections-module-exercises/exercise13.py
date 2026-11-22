# ========question========
# Exercise 13: Implement a Simple LRU Cache
#
# Problem Statement: Write a Python program that implements a basic Least Recently Used (LRU) cache using OrderedDict. The cache should store up to a fixed number of entries and automatically evict the least recently used item when the limit is exceeded.
#
# Purpose: LRU caches are used in web browsers, database query caches, CDN layers, and CPU memory management to keep frequently accessed data in fast storage while discarding stale entries. Building one with OrderedDict is a classic interview question that demonstrates mastery of both data structure selection and cache eviction logic.
#
# Given Input: A cache with capacity = 3, followed by a sequence of get and put operations that triggers at least one eviction.
#
# Expected Output: Cache state printed after each operation showing which items are present and which was evicted.
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

