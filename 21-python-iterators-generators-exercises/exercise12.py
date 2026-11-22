# ========question========
# Exercise 12: CSV Row Parser
#
# Problem Statement: Create a generator that yields rows from a CSV file as dictionaries, using the first row as keys.
#
# Purpose: This exercise combines file reading with dictionary construction to produce a practical data-ingestion pattern. Yielding rows as dictionaries makes downstream code more readable, and the generator keeps memory consumption low for large CSV files.
#
# Given Input: A CSV file data.csv with the following content:
#
# name,age,city
# Alice,30,New York
# Bob,25,London
# Carol,35,Sydney
#
# Expected Output:
#
# {'name': 'Alice', 'age': '30', 'city': 'New York'}
# {'name': 'Bob', 'age': '25', 'city': 'London'}
# {'name': 'Carol', 'age': '35', 'city': 'Sydney'}
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

