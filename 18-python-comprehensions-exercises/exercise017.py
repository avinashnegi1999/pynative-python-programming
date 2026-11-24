# ========question========
# Exercise 17: Grouped Dict from Two Lists
#
# Problem Statement: Given a list of keys and a list of values of equal length, use a dict comprehension with zip() to pair them into a dictionary. Where a value is None, substitute it with the string "N/A".
#
# Purpose: Combining two parallel lists into a dictionary is a common data-wrangling task — turning a list of column headers and a list of row values into a record, for example. Adding the None-to-"N/A" substitution shows how a conditional expression on the value side of a dict comprehension handles missing data inline, without a separate preprocessing step.
#
# Given Input: keys = ["name", "age", "city", "email"] and values = ["Alice", 30, None, None]
#
# Expected Output: {'name': 'Alice', 'age': 30, 'city': 'N/A', 'email': 'N/A'}
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

