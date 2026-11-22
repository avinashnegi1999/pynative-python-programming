# ========question========
# Exercise 21: Infinite Fibonacci Generator
#
# Problem Statement: Write a generator function fibonacci() that yields Fibonacci numbers indefinitely. Then use itertools.takewhile() to lazily consume from it, stopping as soon as a value exceeds a given limit. Collect the results into a list and print them.
#
# Purpose: An infinite generator paired with takewhile() is the functional-style alternative to a while loop with a break condition. It separates the concern of producing values from the concern of deciding when to stop, making both halves independently reusable and testable. This pattern is fundamental to stream processing and lazy pipelines in Python.
#
# Given Input: All Fibonacci numbers up to but not including 200.
#
# Expected Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Keep the previous two terms available as the sequence advances.


# Write your code below.

