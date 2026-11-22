# ========question========
# Exercise 12: Matrix Transposition
#
# Problem Statement: Given a 3×3 matrix represented as a list of lists, use a nested list comprehension to produce its transpose — a new matrix where rows and columns are swapped. Row i, column j of the original becomes row j, column i of the result.
#
# Purpose: Matrix transposition is a fundamental operation in linear algebra, image processing, and data manipulation (it is what pandas.DataFrame.T does internally). Implementing it with a nested list comprehension — where the outer loop produces rows and the inner loop fills columns — deepens understanding of how nested comprehensions build two-dimensional structures rather than flattening them.
#
# Given Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Expected Output:
#
# Original:   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Transposed: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Track row and column positions independently.


# Write your code below.

