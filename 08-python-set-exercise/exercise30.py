# ========question========
# Exercise 30: Shallow Copy vs. Assignment
#
# Problem Statement: Write a Python program to demonstrate the difference between assigning a set to a new variable with = and creating an independent copy using the .copy() method.
#
# Purpose: This exercise addresses one of the most common sources of subtle bugs in Python: confusing reference assignment with object copying. Understanding this distinction is essential whenever you intend to work with a separate version of a collection without affecting the original.
#
# Given Input: original = {1, 2, 3, 4, 5}
#
# Expected Output:
#
# --- Assignment (=) ---
# original: {1, 2, 3, 4, 5, 99}
# ref: {1, 2, 3, 4, 5, 99}
#
# --- Shallow copy (.copy()) ---
# original: {1, 2, 3, 4, 5}
# copied: {1, 2, 3, 4, 5, 42}
#
# Source: https://pynative.com/python-set-exercise-with-solutions/


# ========hints========
# Translate the requirement into membership relationships between collections.


# Write your code below.

