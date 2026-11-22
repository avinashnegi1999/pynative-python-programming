# ========question========
# Exercise 28: Grading Curve with NormalDist.from_samples()
#
# Problem Statement: Write a Python program that uses NormalDist.from_samples() to fit a normal distribution to raw exam scores, then rescales all scores so that the distribution mean becomes 75, preserving the relative spread of the original grades.
#
# Purpose: Grade curving is a direct application of distribution shifting – adjusting all scores by a constant so the class mean hits a target without changing the relative ranking or spread. NormalDist.from_samples() provides a clean interface for fitting a distribution to observed data, and the resulting object’s parameters drive the rescaling logic.
#
# Given Input: raw_scores = [52, 61, 47, 73, 68, 55, 80, 44, 66, 71, 58, 49, 76, 63, 57]
#
# Expected Output: Original mean, target mean of 75, the shift applied, and the full list of curved scores.
#
# Source: https://pynative.com/python-math-statistics-exercises/


# ========hints========
# Choose the mathematical operation and check its domain and units.


# Write your code below.

