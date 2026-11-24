# ========question========
# Exercise 24: Data Throttler
#
# Problem Statement: Create a generator that wraps another iterable but only yields every n-th item.
#
# Purpose: Downsampling a stream by taking every n-th element is a common technique in signal processing, data visualisation, and performance testing. This exercise shows how a thin generator wrapper can add filtering logic to any existing iterable without modifying it.
#
# Given Input: data = list(range(1, 21)), n = 4
#
# Expected Output: 4 8 12 16 20
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

