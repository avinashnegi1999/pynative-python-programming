# ========question========
# Exercise 20: Lazy Squares
#
# Problem Statement: Create a generator expression that yields the squares of integers from 1 to 1,000,000. Retrieve only the first 10 values using itertools.islice(). Then compare the memory footprint of the generator against an equivalent list comprehension using sys.getsizeof() to make the efficiency difference concrete.
#
# Purpose: A list comprehension materialises every value into memory immediately. A generator expression computes each value only when requested and stores nothing beyond the current position. When only a small portion of a large sequence is needed, the generator uses a constant amount of memory regardless of the sequence’s theoretical length — a critical distinction for large-scale data processing.
#
# Given Input: Integers from 1 to 1,000,000.
#
# Expected Output:
#
# First 10 squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Generator size:   208 bytes
# List size:        8,000,056 bytes
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

