# ========question========
# Exercise 11: Function Composition
#
# Problem Statement: Write a compose(f, g) utility function that returns a new function equivalent to applying g first and then f to the result — that is, compose(f, g)(x) should equal f(g(x)). Test it by composing a lambda that doubles a number with a lambda that adds 3.
#
# Purpose: Function composition is a fundamental concept in functional programming. Rather than calling functions one by one in sequence, composition lets you build a new function by wiring existing ones together. The result is more reusable, more testable, and reads like a description of a pipeline rather than a sequence of instructions.
#
# Given Input: Compose double = lambda x: x * 2 and add_three = lambda x: x + 3. Call the composed function with 5.
#
# Expected Output: double(add_three(5)) = 16
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

