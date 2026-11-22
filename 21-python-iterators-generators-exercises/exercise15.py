# ========question========
# Exercise 15: Batch Processing
#
# Problem Statement: Write a generator that takes an iterable and yields chunks of a specific size (e.g., process a list of 100 items in batches of 10).
#
# Purpose: Batch processing is essential when working with APIs, databases, or large datasets where processing all items at once is impractical. This exercise shows how a generator can group an arbitrary stream of values into fixed-size chunks without loading the full dataset into memory.
#
# Given Input: items = list(range(1, 11)), batch_size = 3
#
# Expected Output:
#
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10]
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

