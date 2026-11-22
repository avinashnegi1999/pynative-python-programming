# ========question========
# Exercise 26: Peekable Iterator
#
# Problem Statement: Wrap an iterator in a class that allows you to “peek” at the next value without actually consuming it.
#
# Purpose: Peeking is a fundamental technique in parsers, lexers, and lookahead algorithms, where a decision about the current token depends on what comes next. This exercise teaches you how to extend the standard iterator protocol with additional capabilities by wrapping an existing iterator in a class.
#
# Given Input: data = [10, 20, 30, 40]
#
# Expected Output:
#
# Peek: 10
# Consumed: 10
# Peek: 20
# Consumed: 20
# Consumed: 30
# Consumed: 40
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Think about how iteration stores state and signals that it is finished.


# Write your code below.

