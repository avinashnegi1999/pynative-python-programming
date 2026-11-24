# ========question========
# Exercise 10: defaultdict with set
#
# Problem Statement: Write a Python program that takes a list of (student, subject) pairs and uses defaultdict(set) to collect all unique subjects each student is enrolled in, then prints each student’s subject list.
#
# Purpose: Using a set as the default value automatically deduplicates entries, which is ideal when the source data may contain repeated pairs. This pattern appears in access control systems, tag collections, and any scenario where you need to associate a key with a unique group of values rather than an ordered list.
#
# Given Input: enrolments = [("Alice", "Maths"), ("Bob", "Science"), ("Alice", "Science"), ("Alice", "Maths"), ("Bob", "Maths"), ("Charlie", "Science")]
#
# Expected Output: Each student with their unique subjects, e.g. Alice: {'Maths', 'Science'}, Bob: {'Science', 'Maths'}, Charlie: {'Science'}
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

