# ========question========
# Exercise 37: Property Decorators (@property)
#
# Practice Problem: Create a Student class with a name and a score. Use the @property decorator to create a getter for the score, and a @score.setter to ensure that any score assigned is between 0 and 100.
#
# Given Input:
#
# s = Student("Kevin")
# s.score = 105 # Should trigger a ValueError
#
# Expected Output: ValueError: Score must be between 0 and 100.
#
# Source: https://pynative.com/intermediate-python-exercises/


# ========hints========
# Wrap the original callable while preserving its arguments and return value.


# Write your code below.

