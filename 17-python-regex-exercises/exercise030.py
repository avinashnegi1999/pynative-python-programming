# ========question========
# Exercise 30: Replace Multiple Delimiters
#
# Problem Statement: Write a Python program to replace all occurrences of spaces, commas, and dots in a string with a colon.
#
# Purpose: This exercise demonstrates how a single re.sub() call with a character class can replace multiple different delimiters simultaneously, replacing the need for chained str.replace() calls. Normalising mixed delimiters into a single consistent separator is a standard data-cleaning step in CSV processing, configuration parsing, and token splitting.
#
# Given Input: test_strings = ["one two three", "one,two,three", "one.two.three", "one, two. three", "no.delimiters,here today"]
#
# Expected Output:
#
# one two three          -> one:two:three
# one,two,three          -> one:two:three
# one.two.three          -> one:two:three
# one, two. three        -> one::two::three
# no.delimiters,here today -> no:delimiters:here:today
#
# - Python regex split
#
# - Python Regex replace
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Describe the required text structure first, including anchors, character groups, and repetitions.


# Write your code below.

