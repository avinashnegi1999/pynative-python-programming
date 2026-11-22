# ========question========
# Exercise 10: Nested Try-Except
#
# Problem Statement: Write a function load_and_parse(filename, key) that opens a JSON file (outer try) and then looks up a key in the parsed data (inner try). Handle FileNotFoundError at the outer level and KeyError at the inner level so each failure is reported with an appropriate message.
#
# Purpose: Complex workflows often have multiple distinct failure points that require different recovery strategies. Nested try blocks let you apply fine-grained handling close to the source of each potential error, keeping the logic easier to reason about than a single flat block that catches everything.
#
# Given Input: A file data.json containing {"name": "Alice", "age": 30}. Call load_and_parse("data.json", "name"), then load_and_parse("data.json", "email"), then load_and_parse("missing.json", "name").
#
# Expected Output:
#
# Alice
# Error: key 'email' not found in the data.
# Error: file 'missing.json' does not exist.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

