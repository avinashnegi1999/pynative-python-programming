# ========question========
# Exercise 13: Custom Key with sorted()
#
# Problem Statement: Given a list of strings, sort them alphabetically by their last character using a lambda as the key argument to sorted(). Where two strings end with the same character, preserve their original relative order.
#
# Purpose: The key parameter of sorted() accepts any callable that extracts a sort value from each element. This exercise reinforces that the key does not have to be the element itself — it can be any derived value, including a substring, a computed property, or the result of a function call.
#
# Given Input: words = ["banana", "apple", "cherry", "date", "fig", "kiwi"]
#
# Expected Output: ['banana', 'apple', 'date', 'fig', 'cherry', 'kiwi']
#
# Source: https://pynative.com/python-lambda-functional-programming-exercises/


# ========hints========
# Identify the value that determines the ordering before choosing a sorting key.


# Write your code below.

