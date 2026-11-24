# ========question========
# Exercise 14: Memoization with lru_cache
#
# Problem Statement: Write a recursive Fibonacci function decorated with @functools.lru_cache. Then write the same function without caching. Use Python’s time module to measure and compare how long each version takes to compute fib(35).
#
# Purpose: Naive recursive Fibonacci has exponential time complexity because it recomputes the same subproblems repeatedly. lru_cache applies memoization automatically: each unique argument is computed once and the result is stored for reuse. This exercise makes the performance difference concrete and introduces one of Python’s most useful built-in optimisation tools.
#
# Given Input: Compute fib(35) with both cached and uncached versions and print the elapsed time for each.
#
# Expected Output:
#
# Cached   fib(35) = 9227465  in 0.000012s
# Uncached fib(35) = 9227465  in 2.817043s
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Check parameters, return values, and scope before writing the function body.


# Write your code below.

