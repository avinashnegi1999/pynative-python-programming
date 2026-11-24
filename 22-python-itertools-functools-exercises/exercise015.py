# ========question========
# Exercise 15: Partial Functions
#
# Problem Statement: Write a Python program that uses functools.partial() to create a specialised power_of_2() function from the built-in pow() function, then applies it to a list of exponents and compares the result with equivalent lambda and loop approaches.
#
# Purpose: Partial application creates a new function by pre-filling one or more arguments of an existing function, reducing its arity. It is a cornerstone of functional programming that enables function reuse, cleaner callbacks, and more expressive APIs – particularly when working with map(), filter(), and event handlers where you need a single-argument callable but the underlying function requires more.
#
# Given Input: exponents = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Expected Output: Powers of 2 for each exponent: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

