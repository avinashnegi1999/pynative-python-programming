# ========question========
# Exercise 27: Distribution Overlap Between Two Models
#
# Problem Statement: Write a Python program that uses NormalDist.overlap() to compute how much two normal distributions representing the error rates of two machine learning models overlap, then interprets what the overlap coefficient means for model comparison.
#
# Purpose: Overlap between distributions is a practical measure of how distinguishable two groups are – used in medical diagnostic accuracy (sensitivity vs specificity), A/B test analysis (are the two variants really different?), and model evaluation (do two models perform differently or are their results statistically indistinguishable?). NormalDist.overlap() computes this in one call without numerical integration.
#
# Given Input: Model A error rate: NormalDist(mu=0.15, sigma=0.03). Model B error rate: NormalDist(mu=0.22, sigma=0.04).
#
# Expected Output: An overlap coefficient between 0 and 1, with 1 meaning identical distributions and 0 meaning completely separate distributions.
#
# Source: https://pynative.com/python-math-statistics-exercises/


# ========hints========
# Choose the mathematical operation and check its domain and units.


# Write your code below.

