# ========question========
# Exercise 20: Unique Element Filter
#
# Problem Statement: Write a generator that takes an iterable with duplicates and yields only unique elements in the order they appear.
#
# Purpose: Deduplication while preserving insertion order is a common requirement in data cleaning, URL deduplication, and event stream processing. This exercise shows how a generator can maintain a small auxiliary data structure to track state without exposing it to the caller.
#
# Given Input: items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#
# Expected Output: 3 1 4 5 9 2 6
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Separate the condition for keeping an item from the transformation of that item.


# Write your code below.

