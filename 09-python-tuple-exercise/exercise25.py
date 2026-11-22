# ========question========
# Exercise 25: The Hashability Paradox
#
# Problem Statement: Write a Python program that experiments with using tuples as dictionary keys. Demonstrate why a fully immutable tuple like (1, 2) works as a key, while a tuple containing a mutable object like (1, [2]) raises a TypeError.
#
# Purpose: This exercise builds a deep understanding of Python’s hashing rules. Dictionary keys must be hashable, meaning their value must never change after being inserted. A tuple containing a mutable list violates this guarantee, which is why Python rejects it. This concept is fundamental to understanding how sets and dictionaries work internally.
#
# Given Input: Attempt to use (1, 2) and (1, [2]) as dictionary keys
#
# Expected Output:
#
# (1, 2) as key: success, value = "immutable tuple"
# (1, [2]) as key: TypeError - unhashable type: 'list'
#
# Source exercise number: 32 (local files are consecutive).
# Source: https://pynative.com/python-tuple-exercise-with-solutions/


# ========hints========
# Remember tuples are immutable; distinguish creating a new tuple from changing a nested mutable object.


# Write your code below.

