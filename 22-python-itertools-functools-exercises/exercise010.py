# ========question========
# Exercise 10: takewhile and dropwhile
#
# Problem Statement: Write a Python program that uses itertools.takewhile() to collect temperature readings while they stay below 30°C, then uses itertools.dropwhile() to skip all readings below 30°C and return the remainder of the sequence.
#
# Purpose: takewhile() and dropwhile() model prefix-based filtering – operating on the leading portion of a sequence rather than all matching elements. They are used in log parsing (read lines until a sentinel), data stream processing (discard the warm-up period), and lazy evaluation of sorted data (stop as soon as a condition breaks). Understanding that they stop at the first failure, not at every failure, is the key conceptual distinction from filter().
#
# Given Input: temperatures = [18.2, 21.5, 24.8, 27.1, 29.6, 31.3, 28.4, 33.7, 30.1, 26.5]
#
# Expected Output: takewhile (below 30): [18.2, 21.5, 24.8, 27.1, 29.6] and dropwhile (skip below 30): [31.3, 28.4, 33.7, 30.1, 26.5]
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

