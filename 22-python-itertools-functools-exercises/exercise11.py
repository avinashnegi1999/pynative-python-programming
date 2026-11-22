# ========question========
# Exercise 11: Group Consecutive Items
#
# Problem Statement: Write a Python program that uses itertools.groupby() to group a sorted list of transactions by category, then prints each group’s category, item count, and individual items.
#
# Purpose: Grouping consecutive elements by a shared key is a core operation in data processing pipelines – aggregating log entries by severity, summarising sales by region, or batching database records by status. itertools.groupby() provides this lazily without building intermediate dictionaries, making it ideal for streaming or large sorted datasets.
#
# Given Input: transactions = [("Food", 12.50), ("Food", 8.30), ("Travel", 45.00), ("Travel", 22.10), ("Travel", 15.75), ("Food", 6.90), ("Tech", 299.99)]
#
# Expected Output: Each category printed as a heading with its items listed beneath, followed by the item count and subtotal for that group.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

