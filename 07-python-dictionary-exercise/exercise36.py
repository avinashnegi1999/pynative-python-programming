# ========question========
# Exercise 36: Invert with Duplicate Values
#
# Problem Statement: Write a Python program to invert a dictionary where multiple keys may share the same value. Instead of overwriting, group all original keys that map to the same value into a list under that value as the new key.
#
# Purpose: This exercise helps you practice handling collisions during dictionary inversion, using setdefault() or defaultdict, and building grouped structures from flat data – a pattern common in indexing, tagging systems, and reverse lookups.
#
# Given Input: original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
#
# Expected Output: {1: ["a", "c"], 2: ["b", "e"], 3: ["d"]}
#
# Source: https://pynative.com/python-dictionary-exercise-with-solutions/


# ========hints========
# Track which values you have already encountered; check whether order must be preserved.


# Write your code below.

