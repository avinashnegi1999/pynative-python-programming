# ========question========
# Exercise 30: Z-Score Outlier Detector Combining NormalDist and quantiles()
#
# Problem Statement: Write a Python function that combines statistics.NormalDist and statistics.quantiles() to build a dual-method outlier detector: one based on z-scores from the fitted normal distribution, and one based on the IQR fence method, then compares which values each method flags.
#
# Purpose: No single outlier detection method is universally best. The z-score method assumes normality and is sensitive to extreme values distorting the mean and standard deviation. The IQR method is non-parametric and robust to skew. Combining both in a single function and comparing their outputs builds the critical thinking needed to choose the right tool for a given dataset in real data cleaning pipelines.
#
# Given Input: data = [14, 18, 11, 13, 6, 8, 2, 74, 12, 9, 17, 15, 10, 13, 16, 8, 11, -5, 14, 12]
#
# Expected Output: Outliers flagged by each method printed separately, followed by a comparison showing agreements and disagreements.
#
# Source: https://pynative.com/python-math-statistics-exercises/


# ========hints========
# Choose the mathematical operation and check its domain and units.


# Write your code below.

