# ========question========
# Exercise 23: Convert namedtuple to Dictionary
#
# Problem Statement: Write a Python program that creates a namedtuple instance and converts it to a regular dictionary using the _asdict() method, then demonstrates how to use the resulting dictionary for JSON serialisation.
#
# Purpose: Namedtuples cannot be directly serialised to JSON because json.dumps() does not recognise them as dictionaries. Converting to a dict first is the standard bridge between the lightweight namedtuple record model and JSON-based APIs, configuration files, or database serialisation layers.
#
# Given Input: A Product namedtuple with fields name, category, price, and in_stock.
#
# Expected Output: The namedtuple printed as a dict, then as a JSON string.
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

