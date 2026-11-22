# ========question========
# Exercise 20: Bounded deque for Recent History
#
# Problem Statement: Write a Python program that creates a deque with maxlen=5 to simulate a recent browsing history buffer, demonstrating that adding a sixth item automatically discards the oldest entry.
#
# Purpose: A bounded deque is the simplest way to maintain a fixed-size sliding window of recent events without manually checking length or removing old entries. It appears in terminal command history, log tail buffers, moving average calculations, and any feature that shows “last N items” to the user.
#
# Given Input: A sequence of six page URLs added one at a time to a deque(maxlen=5).
#
# Expected Output: History buffer state after each addition, showing the oldest URL being dropped when the sixth is added.
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

