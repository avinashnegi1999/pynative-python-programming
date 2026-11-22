# ========question========
# Exercise 41: Multiple Inheritance and MRO
#
# Practice Problem: Create two classes, Flyer (with a fly() method) and Swimmer (with a swim() method). Create a Duck class that inherits from both. Use the __mro__ attribute to inspect the search order.
#
# Given Input:
#
# d = Duck()
# d.fly()
# d.swim()
#
# Expected Output:
#
# Flying high!
# Swimming fast!
# MRO: (<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)
#
# Source: https://pynative.com/intermediate-python-exercises/


# ========hints========
# Reuse the parent class behavior and override only what the task changes.


# Write your code below.

