# ========question========
# Exercise 17: Running Average
#
# Problem Statement: Create a generator that maintains and yields the running average of a stream of numbers.
#
# Purpose: This exercise shows how a generator can carry internal state between yields to perform stateful stream processing. A running average is a common operation in monitoring, analytics, and signal processing, and computing it lazily avoids storing the entire history of values.
#
# Given Input: numbers = [10, 20, 30, 40, 50]
#
# Expected Output: 10.0 15.0 20.0 25.0 30.0
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Keep track of both the total and how many items contribute to it.


# Write your code below.

