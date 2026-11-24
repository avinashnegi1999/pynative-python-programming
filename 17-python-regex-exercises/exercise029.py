# ========question========
# Exercise 29: Swap Characters
#
# Problem Statement: Write a Python program to replace all whitespace characters with an underscore, and all underscores with a whitespace, in a single pass over the string.
#
# Purpose: This exercise introduces the technique of performing two simultaneous character substitutions without one replacement interfering with the other. True in-place swapping requires a strategy that distinguishes the original characters from those that have already been substituted, and is a practical problem in slug generation, identifier normalisation, and format conversion pipelines.
#
# Given Input: test_strings = ["hello world", "hello_world", "the quick_brown fox_jumps", "no_change"]
#
# Expected Output:
#
# hello world           -> hello_world
# hello_world           -> hello world
# the quick_brown fox_jumps -> the_quick brown_fox jumps
# no_change             -> no change
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Describe the required text structure first, including anchors, character groups, and repetitions.


# Write your code below.

