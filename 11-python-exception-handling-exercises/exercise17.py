# ========question========
# Exercise 17: Logging Exceptions
#
# Problem Statement: Configure Python’s logging module to write to a file called app.log. Write a function divide(a, b) that catches a ZeroDivisionError and uses logging.exception() to record the full traceback to the log file before returning None.
#
# Purpose: Printing errors to the console is fine for learning, but production code needs persistent, structured logs. Python’s built-in logging module provides log levels, file rotation, formatters, and – crucially – the ability to capture full tracebacks automatically. This exercise builds the habit of logging exceptions properly from the start.
#
# Given Input: Call divide(10, 0).
#
# Expected Output:
#
# Console: divide(10, 0) returned None
# app.log: ERROR:root:Division failed - ZeroDivisionError with full traceback
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

