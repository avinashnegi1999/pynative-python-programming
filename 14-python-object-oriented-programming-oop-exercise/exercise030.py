# ========question========
# Exercise 30: Character Class with Auto Level-Up Logic
#
# Problem Statement: Write a Python program that creates a Character class with health, exp, and level attributes. The character should automatically level up and reset exp whenever accumulated experience reaches or exceeds 100.
#
# Purpose: This exercise shows how to embed game logic directly into a class using a method that manages state transitions. It also demonstrates how to handle overflow (excess exp after levelling up) and keep multiple related attributes in sync.
#
# Given Input: Character("Aria", health=100), then gain_exp(60) twice
#
# Expected Output:
#
# Aria gained 60 exp. (Total: 60)
# Aria gained 60 exp. Level up! Now Level 2. (Remaining exp: 20)
#
# Source: https://pynative.com/python-object-oriented-programming-oop-exercise/


# ========hints========
# Decide which values belong to each instance and which behavior belongs in methods.


# Write your code below.

