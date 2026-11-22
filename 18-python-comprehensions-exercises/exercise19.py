# ========question========
# Exercise 19: Character Frequency Set
#
# Problem Statement: Given a sentence, use a set comprehension with a condition to build a set of all characters — excluding spaces — that appear more than once in the sentence. The result should contain each such character exactly once.
#
# Purpose: This exercise combines set comprehensions with a condition that requires querying the source data (the sentence’s character counts) to decide which elements to include. It shows that the filter condition in a comprehension is not limited to simple comparisons — it can call any function, including str.count(), which turns a comprehension into a concise frequency-based analysis tool.
#
# Given Input: sentence = "comprehension makes python powerful"
#
# Expected Output: A set of characters that each appear at least twice. Expected characters include 'o', 'e', 'n', 's', 'i', 'p', and 'h' (order may vary).
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Associate each distinct value with a counter.


# Write your code below.

