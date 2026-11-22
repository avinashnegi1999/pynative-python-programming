# ========question========
# Exercise 40: Deep vs. Shallow Copy
#
# Problem Statement: Write a Python program that demonstrates the difference between a shallow copy and a deep copy of a dictionary containing nested lists, showing how changes to nested data affect each copy differently.
#
# Purpose: This exercise helps you understand how Python manages object references, why mutating nested structures in a shallow copy also affects the original, and when to use copy.deepcopy() – critical knowledge for avoiding hard-to-trace bugs in data processing and state management.
#
# Given Input: original = {"name": "Alice", "scores": [90, 85, 92]}
#
# Expected Output:
#
# Shallow copy scores: [90, 85, 92, 100]
# Original scores after shallow mutation: [90, 85, 92, 100]
#
# Deep copy scores: [90, 85, 92, 99]
# Original scores after deep mutation: [90, 85, 92, 100]
#
# Source: https://pynative.com/python-dictionary-exercise-with-solutions/


# ========hints========
# Identify the keys and values you need, and decide whether the result should modify or copy the input.


# Write your code below.

