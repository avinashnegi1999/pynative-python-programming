# ========question========
# Exercise 7: Count Occurrences Without KeyError
#
# Problem Statement: Write a Python program that counts the occurrences of each item in a list using defaultdict(int), without any manual initialisation of keys, and prints each item with its count.
#
# Purpose: Before Counter and defaultdict existed, counting with a plain dictionary required checking for key existence on every update. This exercise shows how defaultdict(int) solves that cleanly and helps you understand the underlying mechanism that Counter itself builds upon.
#
# Given Input: colours = ["red", "blue", "red", "green", "blue", "blue", "red", "yellow"]
#
# Expected Output: red: 3, blue: 3, green: 1, yellow: 1
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Keep a counter and update it only when the required condition holds.


# Write your code below.

