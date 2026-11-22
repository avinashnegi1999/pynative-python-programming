# ========question========
# Exercise 17: Custom Sorting with cmp_to_key
#
# Problem Statement: Write a Python program that uses functools.cmp_to_key() to sort a list of software version strings (e.g. "2.10.1") using a custom comparator function that correctly orders them numerically rather than lexicographically.
#
# Purpose: Python’s sorted() accepts a key function but not a comparator (compare) function. cmp_to_key() bridges this gap by wrapping a comparator – which returns negative, zero, or positive – into a key object that Python’s sort algorithm can use. This is essential when the ordering logic is inherently pairwise and cannot be expressed as a simple key extraction.
#
# Given Input: versions = ["1.10.2", "1.9.1", "2.0.0", "1.10.1", "1.2.3", "2.1.0", "1.10.10"]
#
# Expected Output: Versions sorted correctly in ascending order: 1.2.3, 1.9.1, 1.10.1, 1.10.2, 1.10.10, 2.0.0, 2.1.0
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Identify the value that determines the ordering before choosing a sorting key.


# Write your code below.

