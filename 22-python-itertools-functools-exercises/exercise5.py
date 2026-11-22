# ========question========
# Exercise 5: Password Generator Using product()
#
# Problem Statement: Write a Python program that uses itertools.product() with the repeat parameter to generate all possible 4-digit PIN codes from digits 0-9, then reports the total count and demonstrates how quickly the search space grows with length.
#
# Purpose: The repeat argument of itertools.product() is the idiomatic way to model fixed-length sequences drawn from the same alphabet – PIN codes, passwords, binary strings, and DNA sequences. This exercise also builds intuition for exponential growth of search spaces, which is central to understanding password security and brute-force attack complexity.
#
# Given Input: digits = "0123456789", pin_length = 4
#
# Expected Output: Total 4-digit PINs: 10000, the first 5 and last 5 PINs, and a growth table showing search space size for lengths 1 through 6.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Consider the required character groups and whether secure randomness is necessary.


# Write your code below.

