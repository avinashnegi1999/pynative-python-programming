# ========question========
# Exercise 22: Chained Generator Pipeline
#
# Problem Statement: Build a three-stage generator pipeline: the first stage yields integers from a given range, the second filters only prime numbers from that stream, and the third formats each prime as a string like "Prime: 7". Chain all three stages together without materialising any intermediate list. Retrieve and print the first 10 results.
#
# Purpose: This exercise shows the full power of chaining generator expressions into a multi-stage pipeline. Each stage is a lazy wrapper around the previous one — values flow through all three transforms one at a time, with no intermediate collections ever built in memory. This pattern is the Python equivalent of Unix pipes and is the foundation of memory-efficient data processing at scale.
#
# Given Input: Integers from 2 to 100.
#
# Expected Output:
#
# ['Prime: 2', 'Prime: 3', 'Prime: 5', 'Prime: 7', 'Prime: 11',
#  'Prime: 13', 'Prime: 17', 'Prime: 19', 'Prime: 23', 'Prime: 29']
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Yield one result at a time while preserving the state needed for the next.


# Write your code below.

