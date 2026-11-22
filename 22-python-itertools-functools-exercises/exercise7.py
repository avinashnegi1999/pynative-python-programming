# ========question========
# Exercise 7: Infinite Counter with islice
#
# Problem Statement: Write a Python program that uses itertools.count() to create an infinite counter starting at 100 with a step of 5, then uses itertools.islice() to safely extract the first 8 values and print them.
#
# Purpose: Infinite iterators model sequences that have no predetermined end – ID generators, timestamp sequences, mathematical series, and event numbering systems. itertools.count() paired with itertools.islice() is the canonical Python pattern for safely consuming a bounded slice of an infinite stream without risk of an infinite loop.
#
# Given Input: start = 100, step = 5, extract n = 8 values.
#
# Expected Output: [100, 105, 110, 115, 120, 125, 130, 135]
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Keep a counter and update it only when the required condition holds.


# Write your code below.

