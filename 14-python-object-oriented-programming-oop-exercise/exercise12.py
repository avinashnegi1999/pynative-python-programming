# ========question========
# Exercise 12: Shared Class Attribute Across Instances
#
# Problem Statement: Write a Python program to create a Vehicle class with a class attribute color = "White" that is shared by all instances. Create two vehicle objects and demonstrate that both share the same default color, then show that changing the class attribute updates all instances that have not overridden it.
#
# Purpose: This exercise clarifies the distinction between class attributes and instance attributes. Class attributes are defined directly on the class and shared across every instance, making them ideal for default values or constants that apply universally. Understanding this difference prevents subtle bugs when mutable data is accidentally shared between objects.
#
# Given Input: v1 = Vehicle("Tesla", 250) and v2 = Vehicle("BMW", 200).
#
# Expected Output:
#
# Tesla - Color: White, Speed: 250
# BMW - Color: White, Speed: 200
# Tesla - Color: Red, Speed: 250
# BMW - Color: Red, Speed: 200
#
# Source: https://pynative.com/python-object-oriented-programming-oop-exercise/


# ========hints========
# Decide which values belong to each instance and which behavior belongs in methods.


# Write your code below.

