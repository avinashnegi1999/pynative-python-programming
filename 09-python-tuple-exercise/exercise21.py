# ========question========
# Exercise 21: Tuple Mutability
#
# Problem Statement: Create a tuple that contains a list as one of its elements. Modify the list in place and observe that the tuple’s identity stays the same while its contents appear to change.
#
# Purpose: This exercise uncovers one of Python’s most instructive subtleties: a tuple is immutable in the sense that its references cannot be reassigned, but if a reference points to a mutable object such as a list, that object itself can still be changed. Understanding this distinction is essential for writing predictable, bug-free code.
#
# Given Input: t = (1, 2, [3, 4, 5]), append 99 to the inner list
#
# Expected Output:
#
# Before: (1, 2, [3, 4, 5])
# After:  (1, 2, [3, 4, 5, 99])
# Same object? True
#
# Source exercise number: 28 (local files are consecutive).
# Source: https://pynative.com/python-tuple-exercise-with-solutions/


# ========hints========
# Remember tuples are immutable; distinguish creating a new tuple from changing a nested mutable object.


# Write your code below.

