# ========question========
# Exercise 8: Cycle Through a List
#
# Problem Statement: Write a Python program that uses itertools.cycle() to rotate through a list of three weekday shift labels and assigns one to each of 10 employees in order, wrapping back to the start when the labels run out.
#
# Purpose: Cyclic assignment is common in scheduling (round-robin task allocation), load balancing (distributing requests across servers), and UI patterns (alternating row colours in tables). itertools.cycle() handles the wrap-around automatically, eliminating the manual modulo arithmetic that would otherwise be needed.
#
# Given Input: shifts = ["Morning", "Afternoon", "Night"] and employees = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
#
# Expected Output: Each employee printed with their assigned shift, cycling through Morning, Afternoon, Night and repeating.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Think about whether the task combines, groups, or lazily consumes input items.


# Write your code below.

