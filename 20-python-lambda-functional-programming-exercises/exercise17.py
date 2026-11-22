# ========question========
# Exercise 17: Transducer Pattern
#
# Problem Statement: Compose a filter (keep only even numbers) and a map (square each value) into a single reducing function — a transducer — that processes a list in one pass without creating any intermediate list. Apply it manually using functools.reduce().
#
# Purpose: Chaining filter() and map() creates a hidden intermediate iterator for each step. A transducer collapses the entire transformation stack into one reducing step, eliminating all intermediate allocations. This is how high-performance data pipelines in Clojure and similar languages work, and understanding it deepens your intuition for how lazy pipelines and stream processing operate.
#
# Given Input: numbers = list(range(1, 11))
#
# Expected Output: [4, 16, 36, 64, 100]
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Separate the row rule from the rule for items within that row.


# Write your code below.

