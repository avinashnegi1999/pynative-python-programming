# ========question========
# Exercise 18: Pipeline with chain and reduce
#
# Problem Statement: Write a Python program that uses itertools.chain() to merge sales data from multiple regions into a single iterable, then uses functools.reduce() to compute the total, maximum, and minimum revenue in a clean pipeline without intermediate lists.
#
# Purpose: Combining chain() for lazy merging with reduce() for aggregation models a real-world ETL (Extract-Transform-Load) pattern: collect data from multiple sources, stream it through a unified pipeline, and collapse it into a result. Keeping the pipeline lazy avoids materialising large intermediate datasets into memory.
#
# Given Input: Three regional sales lists: north = [15200, 18400, 12100], south = [22300, 19800, 25100], east = [11500, 14200, 16800, 13400]
#
# Expected Output: Total revenue, maximum single-region sale, minimum single-region sale, and average, all computed from the chained stream.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

