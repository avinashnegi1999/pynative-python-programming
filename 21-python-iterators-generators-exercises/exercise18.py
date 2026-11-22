# ========question========
# Exercise 18: Sliding Window
#
# Problem Statement: Write a generator that yields a sliding window of size n over a sequence (e.g., for [1, 2, 3, 4] with window size 2, it yields (1, 2), (2, 3), (3, 4)).
#
# Purpose: Sliding windows appear in time-series analysis, text n-gram generation, and signal smoothing. This exercise demonstrates how a generator can maintain a small buffer of recent values and expose it as a structured output, combining slicing with lazy production.
#
# Given Input: sequence = [1, 2, 3, 4, 5], n = 3
#
# Expected Output: (1, 2, 3) (2, 3, 4) (3, 4, 5)
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

