# ========question========
# Exercise 27. Finding Common Elements (Intersections)
#
# Use sets to identify values shared by two lists.
#
# Given Input:
#
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
#  Code language: Python (python)
#
# Expected Output: Common Elements: {4, 5}


# ========hints========
# Think about set intersection.


# Write your code below.

# Two lists
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

# Convert lists into sets
set_a = set(list_a)
set_b = set(list_b)

# Find common elements using intersection
common = set_a & set_b

# Display the result
print(f"Common Elements: {common}")


# # pynative solution====================================

# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]

# set_a = set(list_a)
# set_b = set(list_b)

# # Find common elements using intersection
# common = set_a & set_b  # like venn diagram

# print(f"Common Elements: {common}")
