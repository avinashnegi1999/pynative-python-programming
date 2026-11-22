# ========question========
# Exercise 25: Generator State Machine
#
# Problem Statement: Use a generator to represent a simple state machine (e.g., a Traffic Light that cycles between Green, Yellow, and Red).
#
# Purpose: State machines model systems where behaviour depends on the current state and transitions follow defined rules. Encoding one as a generator is elegant because yield naturally represents a pause between state transitions, and the generator’s internal scope holds the current state without any external variables.
#
# Given Input: Advance the traffic light through 6 transitions.
#
# Expected Output: Green Yellow Red Green Yellow Red
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Yield one result at a time while preserving the state needed for the next.


# Write your code below.

