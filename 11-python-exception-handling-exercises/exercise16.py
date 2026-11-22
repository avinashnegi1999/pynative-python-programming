# ========question========
# Exercise 16: Exception Hierarchy
#
# Problem Statement: Define a three-level exception hierarchy: AppError as the base, DatabaseError inheriting from it, and ConnectionError inheriting from DatabaseError. Raise a ConnectionError and show that catching DatabaseError or AppError also intercepts it, while catching an unrelated exception type does not.
#
# Purpose: Exception hierarchies are the backbone of professional Python library design. They let users of your code choose how broadly or narrowly to catch errors. A caller that wants to handle all database problems catches DatabaseError; one that wants only connectivity failures catches ConnectionError. This exercise makes that mechanism concrete.
#
# Given Input: Raise ConnectionError("host unreachable") and catch it three times – once with each level of the hierarchy – to show that all three work.
#
# Expected Output:
#
# Caught as ConnectionError: host unreachable
# Caught as DatabaseError: host unreachable
# Caught as AppError: host unreachable
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

