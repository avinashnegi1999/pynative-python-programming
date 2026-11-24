# ========question========
# Exercise 14: Validate User Input Loop
#
# Problem Statement: Write a program that repeatedly prompts the user to enter a positive integer. If the input is not a valid integer or is not positive, catch the exception or condition, display an error message, and ask again. The loop should only exit when valid input is received.
#
# Purpose: Real applications rarely get clean input on the first attempt. This exercise combines exception handling with a control loop to build a robust input routine – a pattern found in CLI tools, configuration wizards, and any program that interacts directly with a human user.
#
# Given Input: The user types abc, then -5, then 7 across three prompts.
#
# Expected Output:
#
# Enter a positive integer: abc
# Error: 'abc' is not a valid integer. Try again.
# Enter a positive integer: -5
# Error: -5 is not positive. Try again.
# Enter a positive integer: 7
# You entered: 7
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Separate parsing a date from formatting or doing arithmetic with it.


# Write your code below.

