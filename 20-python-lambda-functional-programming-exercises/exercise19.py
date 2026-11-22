# ========question========
# Exercise 19: Higher-Order Function Library
#
# Problem Statement: Implement your own versions of my_map(func, lst), my_filter(pred, lst), and my_reduce(func, lst, initial) from scratch using only recursion and lambdas. No loops, no built-in map/filter/reduce, and no list comprehensions. Verify each against a known input.
#
# Purpose: Rebuilding standard library functions from first principles is one of the most effective ways to understand how they work. This exercise makes explicit the recursive structure hidden inside every functional operation: process the head of the list, then recurse on the tail until the base case (an empty list) is reached.
#
# Given Input: numbers = [1, 2, 3, 4, 5]
#
# Expected Output:
#
# my_map    (square, numbers)      = [1, 4, 9, 16, 25]
# my_filter (is_even, numbers)     = [2, 4]
# my_reduce (multiply, numbers, 1) = 120
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

