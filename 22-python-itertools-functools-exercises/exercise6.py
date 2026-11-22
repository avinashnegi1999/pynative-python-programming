# ========question========
# Exercise 6: Chain Multiple Iterables
#
# Problem Statement: Write a Python program that uses itertools.chain() to merge three separate lists of department employees into a single iterable, then prints all names and the total headcount without creating an intermediate combined list.
#
# Purpose: Chaining iterables is one of the most common operations in data processing pipelines – merging results from multiple database queries, combining log files from different servers, or aggregating records from several CSV files. itertools.chain() does this lazily, forwarding elements from each source in sequence without copying data into a new list.
#
# Given Input: Three department lists: engineering = ["Alice", "Bob", "Charlie"], marketing = ["Diana", "Eve"], hr = ["Frank", "Grace", "Heidi"]
#
# Expected Output: All 8 names printed in order department by department, followed by Total employees: 8
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

