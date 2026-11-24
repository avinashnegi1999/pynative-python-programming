# ========question========
# Exercise 11: Re-raising Exceptions
#
# Problem Statement: Write a function process_data(value) that converts a string to an integer. Catch any ValueError, log a message to the console, and then re-raise the same exception so the calling code can handle it at a higher level.
#
# Purpose: Catching an exception purely to re-raise it is a common pattern in layered applications. A lower-level function may need to record a log entry or clean up state without fully swallowing the error, while still allowing the caller to decide how to respond. This exercise shows exactly how to do that with a bare raise statement.
#
# Given Input: Call process_data("abc") from a wrapping try block in the main code.
#
# Expected Output:
#
# [log] process_data failed: invalid literal for int() with base 10: 'abc'
# [main] Caught re-raised exception: invalid literal for int() with base 10: 'abc'
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

