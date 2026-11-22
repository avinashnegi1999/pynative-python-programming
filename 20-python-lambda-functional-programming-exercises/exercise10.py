# ========question========
# Exercise 10: Partial Functions
#
# Problem Statement: Write a general multiply(x, n) function that returns x * n. Use functools.partial() to create two specialised functions from it: double(x), which always multiplies by 2, and triple(x), which always multiplies by 3. Call both with several values.
#
# Purpose: partial() lets you lock in one or more arguments of an existing function to produce a simpler, more focused callable. This avoids writing wrapper functions by hand and is particularly useful when an API expects a one-argument callable but your logic needs additional context baked in.
#
# Given Input: Call double(5), double(9), triple(4), and triple(7).
#
# Expected Output:
#
# double(5) = 10
# double(9) = 18
# triple(4) = 12
# triple(7) = 21
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

