# ========question========
# Exercise 12: Flatten with Map & Reduce
#
# Problem Statement: Given a list of lists, use functools.reduce() with a lambda to flatten it into a single list. Do not use any for loops, list comprehensions, or itertools.
#
# Purpose: Flattening a nested structure is a classic exercise in functional reduction. Solving it with reduce() reinforces how any operation that accumulates a result across a sequence — not just arithmetic — can be expressed as a fold. It also demonstrates that the accumulator in reduce() can be any type, not just a number.
#
# Given Input: nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Visit each inner collection before adding its individual items to the result.


# Write your code below.

