# ========question========
# Exercise 14: List Flattener
#
# Problem Statement: Use yield from to create a recursive generator that flattens a nested list (e.g., [1, [2, 3], 4]).
#
# Purpose: This exercise introduces yield from, a keyword that delegates generation to a sub-iterable. Combining it with recursion produces an elegant solution for traversing arbitrarily deep nested structures – a pattern that appears frequently in tree processing and JSON parsing.
#
# Given Input: nested = [1, [2, [3, 4], 5], [6, 7], 8]
#
# Expected Output: 1 2 3 4 5 6 7 8
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Visit each inner collection before adding its individual items to the result.


# Write your code below.

