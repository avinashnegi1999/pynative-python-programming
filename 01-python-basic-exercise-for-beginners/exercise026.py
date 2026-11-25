# ========question========
# Exercise 26. Merging Two Dictionaries
#
# Combine the entries of two dictionaries into one dictionary.
#
# Given Input:
#
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}Code language: Python (python)
#
# Expected Output:
#
# {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}


# ========hints========
# Look at dictionary merging operations; consider duplicate keys.


# Write your code below.

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

merged = {**dict1, **dict2}

print(merged)


# #pynative method solution =================================

# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}

# # Modern Python merge (Union Operator)
# merged_dict = dict1 | dict2

# print(merged_dict)
