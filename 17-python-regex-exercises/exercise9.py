# ========question========
# Exercise 9: Match Start and End
#
# Problem Statement: Write a Python program to match a string that starts with a, ends with b, and has any characters in between (e.g., a123b, axyzb).
#
# Purpose: This exercise introduces the dot . wildcard and the use of anchors ^ and $ together with re.match() and re.fullmatch(). Matching by a known start and end while allowing arbitrary content in between is a practical technique used in file extension checks, protocol parsing, and delimiter-bounded field extraction.
#
# Given Input: test_strings = ["a123b", "axyzb", "ab", "a b", "ab ", "b123a", "a123"]
#
# Expected Output:
#
# a123b  -> Match
# axyzb  -> Match
# ab     -> Match
# a b    -> Match
# ab     -> No match (trailing space)
# b123a  -> No match
# a123   -> No match
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Describe the required text structure first, including anchors, character groups, and repetitions.


# Write your code below.

