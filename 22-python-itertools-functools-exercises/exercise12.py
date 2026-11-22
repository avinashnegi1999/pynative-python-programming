# ========question========
# Exercise 12: Compress a Sequence
#
# Problem Statement: Write a Python program that uses itertools.compress() to filter a list of product names using a parallel boolean selector list, keeping only the products whose corresponding selector value is truthy.
#
# Purpose: itertools.compress() is the idiomatic tool for mask-based filtering – selecting elements at positions where a parallel boolean array is True. This pattern appears in data science (applying a boolean mask to a sequence), feature selection (choosing columns based on a selector array), and configuration-driven visibility toggles.
#
# Given Input: products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"] and in_stock = [1, 0, 1, 1, 0, 1]
#
# Expected Output: Available products: ['Laptop', 'Keyboard', 'Monitor', 'Webcam']
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

