# ========question========
# Exercise 19: Log Filter
#
# Problem Statement: Create a generator that parses a log file and only yields lines containing the keyword ERROR.
#
# Purpose: This exercise combines file reading with conditional filtering in a single generator, demonstrating a pattern central to log analysis and data pipelines. Yielding only matching lines keeps memory usage constant and makes the generator composable with downstream stages.
#
# Given Input: A log file app.log with the following content:
#
# INFO: Server started
# ERROR: Disk quota exceeded
# INFO: Request received
# ERROR: Database connection failed
# WARNING: High memory usage
#
# Expected Output:
#
# ERROR: Disk quota exceeded
# ERROR: Database connection failed
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Separate the condition for keeping an item from the transformation of that item.


# Write your code below.

