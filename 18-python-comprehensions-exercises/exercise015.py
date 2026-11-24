# ========question========
# Exercise 15: Nested Filtering
#
# Problem Statement: Given a list of lists of numbers, use a list comprehension to extract only those sub-lists where every element is positive. Each qualifying sub-list should appear in the output intact — do not flatten or modify the inner lists.
#
# Purpose: This exercise separates nested filtering from nested iteration. Rather than looping inside a sub-list to transform its contents, you are evaluating a condition that considers the sub-list as a whole and either keeps it or discards it. This pattern appears whenever you want to select complete rows, groups, or records based on a property of all their members.
#
# Given Input: groups = [[1, 2, 3], [-1, 4, 5], [6, 7, 8], [0, 9, 10], [-3, -1, 2], [4, 5, 6]]
#
# Expected Output: [[1, 2, 3], [6, 7, 8], [4, 5, 6]]
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Separate the condition for keeping an item from the transformation of that item.


# Write your code below.

