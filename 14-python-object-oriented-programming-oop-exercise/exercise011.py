# ========question========
# Exercise 11: Coffee Machine with Multi-Resource Tracking
#
# Problem Statement: Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.
#
# Purpose: This exercise combines state management, resource tracking, and conditional logic inside a single class. It mirrors how real-world stateful systems (vending machines, inventory systems, game resource managers) check preconditions before executing an action and update their internal state only when the action is valid.
#
# Given Input: CoffeeMachine(water=300, coffee=100, milk=200). A latte requires 200ml water, 20g coffee, and 150ml milk.
#
# Expected Output:
#
# Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
# Not enough resources to make a latte.
#
# Source: https://pynative.com/python-object-oriented-programming-oop-exercise/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

