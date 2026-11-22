# ========question========
# Exercise 9: Sorted with Multiple Keys
#
# Problem Statement: Given a list of employee dictionaries, each with a "name" and a "salary" key, sort the list by salary in descending order. Where two employees share the same salary, sort those entries by name in ascending alphabetical order. Use a single lambda as the key argument.
#
# Purpose: Sorting on more than one criterion is a common real-world requirement: leaderboards, reports, and data exports all need it. This exercise shows the tuple-key trick that lets a single lambda express a multi-level sort without any additional imports or helper functions.
#
# Given Input: employees = [{"name": "Alice", "salary": 70000}, {"name": "Bob", "salary": 90000}, {"name": "Charlie", "salary": 70000}, {"name": "Diana", "salary": 90000}]
#
# Expected Output:
#
# Bob        $90000
# Diana      $90000
# Alice      $70000
# Charlie    $70000
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Identify the value that determines the ordering before choosing a sorting key.


# Write your code below.

