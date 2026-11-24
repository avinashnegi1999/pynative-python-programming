# ========question========
# Exercise 6: Type Error Guard
#
# Problem Statement: Write a function add_values(a, b) that returns the sum of two values. If the arguments are of incompatible types (for example, a string and an integer), catch the TypeError and return a descriptive error message instead of crashing.
#
# Purpose: Python is dynamically typed, which means type mismatches only surface at runtime. This exercise teaches you to guard operations that assume specific types, a habit that becomes critical when processing data from external sources such as APIs, CSV files, or user forms where the shape of the data is not always guaranteed.
#
# Given Input: Call add_values(10, "20") and add_values(10, 20).
#
# Expected Output: Error: incompatible types for addition. for the first call and 30 for the second.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

