# ========question========
# Exercise 23: CSV Row Parser
#
# Problem Statement: Given a multi-line CSV string, use a generator expression to lazily parse it row by row. Each yielded value should be a list of stripped string values produced by splitting on commas. Skip the header row. Consume the generator with a for loop and print each parsed row.
#
# Purpose: In real applications, CSV files can be gigabytes in size — far too large to load into memory at once. A generator expression over the lines of a file (or a string in this exercise) reads and parses one row at a time, keeping memory usage constant. This exercise builds the habit of thinking lazily about row-by-row data processing before reaching for a library like pandas.
#
# Given Input: A CSV string with a header row and four data rows containing name, age, and city fields.
#
# Expected Output:
#
# ['Alice', '30', 'New York']
# ['Bob', '25', 'London']
# ['Charlie', '35', 'Tokyo']
# ['Diana', '28', 'Paris']
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Work through the example by hand, identify the changing state, then check the stated constraints.


# Write your code below.

