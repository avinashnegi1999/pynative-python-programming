# ========question========
# Exercise 14: Perfect Square Checker Using math.isqrt()
#
# Problem Statement: Write a Python function that uses math.isqrt() to check whether a given positive integer is a perfect square, then tests it against a range of values and prints which ones qualify.
#
# Purpose: Perfect square detection appears in number theory puzzles, competitive programming, cryptographic primality tests, and grid-layout algorithms (e.g. determining whether n items can be arranged in a square grid). Using math.isqrt() instead of math.sqrt() avoids floating-point rounding errors that can cause int(math.sqrt(n))**2 == n to return incorrect results for large perfect squares.
#
# Given Input: Test integers from 1 to 30, then verify specific large values.
#
# Expected Output: A list of perfect squares in the range 1-30 and a verification result for large numbers like 999999999999999999.
#
# Source: https://pynative.com/python-math-statistics-exercises/


# ========hints========
# Accumulate proper divisors and compare their total with the original number.


# Write your code below.

