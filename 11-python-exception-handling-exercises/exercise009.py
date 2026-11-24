# ========question========
# Exercise 9: Else Clause
#
# Problem Statement: Write a function safe_sqrt(value) that converts user input to a float and calculates its square root. Use the try-except-else pattern so that a success message is printed only when no exception is raised, keeping success and error paths cleanly separated.
#
# Purpose: The else clause on a try block is one of Python’s less-known but very useful features. It keeps the “happy path” code out of the try block itself, which means only the risky operation is guarded and success logic is not accidentally shielded from other exceptions it might raise.
#
# Given Input: Call safe_sqrt("25") and safe_sqrt("abc").
#
# Expected Output:
#
# Success: the square root of 25.0 is 5.0
# Error: 'abc' is not a valid number.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

