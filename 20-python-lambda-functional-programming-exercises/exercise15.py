# ========question========
# Exercise 15: Currying
#
# Problem Statement: Implement a curry(func) utility that transforms a two-argument function into a chain of single-argument functions, so that curry(add)(2)(3) returns the same result as add(2, 3). Then extend the idea to a manually curried three-argument function.
#
# Purpose: Currying converts a multi-argument function into a sequence of one-argument functions, each returning the next function in the chain until all arguments have been supplied. This technique enables partial application without functools.partial, makes functions trivially composable, and is a cornerstone concept in functional languages such as Haskell and ML.
#
# Given Input: A two-argument add(a, b) function and a three-argument volume(l, w, h) function.
#
# Expected Output:
#
# curry(add)(2)(3)        = 5
# curry(add)(10)(7)       = 17
# volume(2)(3)(4)         = 24
# box_with_height_4(2)(3) = 24
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

