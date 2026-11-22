# ========question========
# Exercise 25: Frozen Set
#
# Problem Statement: Write a Python program to create a frozenset, demonstrate that set operations work on it, and confirm that any attempt to modify it raises a TypeError.
#
# Purpose: This exercise introduces immutability in the context of sets. A frozenset can be used as a dictionary key or stored inside another set, making it valuable when you need a hashable, read-only collection, such as representing a fixed combination of permissions or configuration flags.
#
# Given Input: fs = frozenset([1, 2, 3, 4, 5])
#
# Expected Output:
#
# frozenset: frozenset({1, 2, 3, 4, 5})
# Intersection with {3, 4, 5, 6}: frozenset({3, 4, 5})
# Error: 'frozenset' object has no attribute 'add'
#
# Source: https://pynative.com/python-set-exercise-with-solutions/


# ========hints========
# Translate the requirement into membership relationships between collections.


# Write your code below.

