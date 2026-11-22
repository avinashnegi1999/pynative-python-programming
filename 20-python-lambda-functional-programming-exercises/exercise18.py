# ========question========
# Exercise 18: Lazy Evaluation with Generators
#
# Problem Statement: Define an infinite sequence of natural numbers using a generator function. Use generator expressions (not map() or filter()) to lazily filter out odd numbers and square the remaining evens. Take only the first 5 results using itertools.islice().
#
# Purpose: An infinite sequence cannot be fully evaluated — it must be processed lazily. Generator expressions create lazy pipelines that compute each value only when it is requested, using constant memory regardless of how long the sequence is. This exercise shows how to build such pipelines and how itertools.islice() acts as the valve that controls how many values are pulled through.
#
# Given Input: An infinite stream of natural numbers starting from 1.
#
# Expected Output: [4, 16, 36, 64, 100]
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Yield one result at a time while preserving the state needed for the next.


# Write your code below.

