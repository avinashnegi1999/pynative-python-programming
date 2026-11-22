# ========question========
# Exercise 27: Exception Handler
#
# Problem Statement: Create a generator that uses .throw() to handle specific errors passed into it during execution.
#
# Purpose: The .throw() method lets the caller inject an exception into a paused generator at the point of its current yield. This enables cooperative error handling between a generator and its driver, a pattern used in async frameworks and testing tools to simulate failure conditions mid-stream.
#
# Given Input: A sequence of values 1, 2, 3, with a ValueError injected after the second value.
#
# Expected Output:
#
# Yielded: 1
# Yielded: 2
# Caught ValueError: simulated error - skipping
# Yielded: 3
# Generator finished
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

