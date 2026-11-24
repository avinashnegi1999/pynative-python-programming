# ========question========
# Exercise 16: Pipeline Function
#
# Problem Statement: Build a pipeline(*funcs) utility that takes any number of single-argument functions and returns a new function. When called with a value, the returned function passes it through each function in left-to-right order, feeding each result into the next — like a Unix pipe. Demonstrate it by building a text-processing pipeline.
#
# Purpose: A pipeline makes data transformation code read in the same direction as the transformations happen. Instead of deeply nested calls like f(g(h(x))), you write pipeline(h, g, f)(x) where the order of functions matches the order of operations. This pattern is central to data engineering, ETL scripts, and functional-style Python.
#
# Given Input: The string "  hello, world!  " passed through a pipeline that strips whitespace, converts to title case, replaces the comma, and appends an exclamation mark.
#
# Expected Output: Hello World!
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

