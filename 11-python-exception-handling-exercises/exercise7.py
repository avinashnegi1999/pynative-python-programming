# ========question========
# Exercise 7: Multiple Exceptions
#
# Problem Statement: Write a function parse_and_divide(value, divisor) that converts value to a float and then divides it by divisor. Use a single try block that handles ValueError (bad conversion) and ZeroDivisionError (division by zero) with separate messages for each.
#
# Purpose: Real programs rarely face only one kind of failure. This exercise shows you how to stack multiple except clauses after one try block so each error type gets its own tailored response, keeping error-handling logic clear and maintainable.
#
# Given Input: Call parse_and_divide("abc", 2) and parse_and_divide("10", 0) and parse_and_divide("10", 2).
#
# Expected Output:
#
# Error: 'abc' cannot be converted to a number.
# Error: Cannot divide by zero.
# 5.0
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

