# ========question========
# Exercise 8: Finally Block
#
# Problem Statement: Write a function read_file(filename) that opens a file manually (without a with statement), reads its contents, and uses a finally block to ensure the file handle is always closed, whether the read succeeds or an exception is raised.
#
# Purpose: The finally block is Python’s mechanism for guaranteed cleanup. Understanding it is essential for managing resources such as file handles, database connections, and network sockets correctly, especially in older codebases or situations where the with statement is not available.
#
# Given Input: Call read_file("hello.txt") where the file exists, and then read_file("missing.txt") where it does not.
#
# Expected Output:
#
# File closed.
# Hello from the file!
# ---
# File closed.
# Error: 'missing.txt' not found.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

