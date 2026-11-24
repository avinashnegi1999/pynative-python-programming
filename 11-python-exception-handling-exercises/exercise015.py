# ========question========
# Exercise 15: Context Manager with Exceptions
#
# Problem Statement: Implement a custom context manager class SuppressError using __enter__ and __exit__ that silently suppresses a specific exception type passed at construction time. Demonstrate it suppressing a ValueError while letting a TypeError propagate normally.
#
# Purpose: Understanding what happens inside a with statement unlocks a powerful Python design pattern. Context managers are used everywhere – in file handling, database transactions, threading locks, and test frameworks. Knowing how __exit__ controls exception propagation lets you build your own resource-management and error-suppression utilities.
#
# Given Input: Use SuppressError(ValueError) as a context manager around a block that raises ValueError, then demonstrate that a TypeError raised inside a second block is not suppressed.
#
# Expected Output:
#
# Entering context...
# ValueError suppressed.
# Outside context - execution continued.
# Entering context...
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

