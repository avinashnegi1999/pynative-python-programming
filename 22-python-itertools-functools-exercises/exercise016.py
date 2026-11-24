# ========question========
# Exercise 16: Memoisation with lru_cache
#
# Problem Statement: Write a Python program that applies functools.lru_cache() to a recursive Fibonacci function, then compares its execution time and call count against the uncached version to quantify the speedup.
#
# Purpose: Memoisation with lru_cache is one of the most impactful single-line optimisations available in Python. It transforms exponential-time recursive functions into linear-time ones by caching results of previous calls. Understanding it is essential for dynamic programming, recursive tree traversal, and any scenario where the same subproblem is solved multiple times.
#
# Given Input: Compute fibonacci(35) with and without caching.
#
# Expected Output: The Fibonacci result, execution times for both versions, and cache statistics from cache_info().
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

