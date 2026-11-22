# ========question========
# Exercise 20: Exception in Generator
#
# Problem Statement: Write a generator function file_lines(filename) that yields lines from a file one at a time, handles IOError gracefully if the file cannot be opened, and supports receiving injected exceptions from outside using generator.throw(). Demonstrate injecting a RuntimeError mid-iteration to cancel reading early.
#
# Purpose: Generators are lazy pipelines, and like any pipeline they need to handle both internal errors (bad file) and external signals (cancel this operation). The throw() method is the standard way to push an exception into a running generator, and understanding it is essential for building cooperative async-style systems and robust data pipelines.
#
# Given Input: A file sample.txt with three lines. Yield the first line normally, then inject a RuntimeError before the second line is yielded.
#
# Expected Output:
#
# Line 1: Hello from line 1
# Generator cancelled: operation aborted
# Done.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

