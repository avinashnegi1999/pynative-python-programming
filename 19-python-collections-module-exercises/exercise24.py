# ========question========
# Exercise 24: Replace a Field Value
#
# Problem Statement: Write a Python program that creates a namedtuple instance representing a product listing and uses the _replace() method to produce updated copies with changed field values, without modifying the original instance.
#
# Purpose: Because namedtuples are immutable, _replace() is the correct way to create a modified version of an existing record – analogous to using dataclasses.replace() for dataclasses or spread syntax in JavaScript. This pattern is common in functional programming workflows where data is never mutated in place.
#
# Given Input: A Listing namedtuple with fields title, price, available, and rating.
#
# Expected Output: Original listing printed, then two modified copies with updated fields, confirming the original is unchanged.
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

