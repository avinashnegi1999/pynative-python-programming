# ========question========
# Exercise 20: Lazy Data Pipeline with islice, filter, and partial
#
# Problem Statement: Write a Python program that builds a lazy data processing pipeline combining itertools.islice() to limit input, filter() with a functools.partial() predicate to select records, and functools.reduce() to aggregate the final result – without materialising any intermediate collection until the final step.
#
# Purpose: Real-world data pipelines must process large streams efficiently. Composing lazy itertools functions with functools higher-order tools creates pipelines that read only what they need, filter as they go, and aggregate in a single pass. This exercise ties together all the concepts from the module into a pattern directly applicable to log analysis, sensor data processing, and batch ETL jobs.
#
# Given Input: A simulated stream of 1000 sales records as (product, region, amount) tuples. Process only the first 200, keep those from the "North" region with amount above a threshold, and sum the qualifying amounts.
#
# Expected Output: Total revenue from qualifying North region sales in the first 200 records, with a step-by-step pipeline trace showing counts at each stage.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Separate the condition for keeping an item from the transformation of that item.


# Write your code below.

