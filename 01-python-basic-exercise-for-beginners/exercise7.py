# ========question========
# Exercise 7. List Manipulation: Add and Remove
#
# Start with five fruits, add fig at the end, then delete the item at position 1.
#
# Given Input: fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#
# Expected Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']


# ========hints========
# Look at list methods for adding an item and removing by position.


# Write your code below.


fruits = ["apple", "banana", "cherry", "date", "elderberry"]


fruits.append("fig")  # here i insert fig at the end

print(fruits)


fruits.remove("banana")  # here it find word banana from list and remove it

print(fruits)
