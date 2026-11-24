# ========question========
# Exercise 13: Cartesian Product
#
# Problem Statement: Given two lists, use a nested list comprehension to generate every possible (x, y) pair where x comes from the first list and y comes from the second. This is the Cartesian product of the two lists. Do not use itertools.product.
#
# Purpose: The Cartesian product is needed any time you want to try every combination of two sets of values — grid coordinates, test parameter combinations, pairing sizes with colours in a catalogue, or generating game board positions. A nested comprehension produces it naturally and clearly, and understanding it is the key to recognising when itertools.product is the right tool for more complex cases.
#
# Given Input: xs = [1, 2, 3] and ys = ["a", "b", "c"]
#
# Expected Output:
#
# [(1, 'a'), (1, 'b'), (1, 'c'),
#  (2, 'a'), (2, 'b'), (2, 'c'),
#  (3, 'a'), (3, 'b'), (3, 'c')]
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

