# ========question========
# Exercise 26: Private Balance with Property Getter & Setter
#
# Problem Statement: Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, and exposed safely through a @property getter and a setter that validates the value before updating it.
#
# Purpose: This exercise demonstrates encapsulation, one of the four pillars of OOP. Using name-mangled private attributes alongside @property lets you control how external code reads and modifies internal state, preventing invalid data from being assigned.
#
# Given Input: BankAccount(1000), then deposit 500, then attempt to set balance to -200
#
# Expected Output:
#
# Current balance: 1000
# Current balance: 1500
# Invalid balance. Must be non-negative.
#
# Source: https://pynative.com/python-object-oriented-programming-oop-exercise/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

