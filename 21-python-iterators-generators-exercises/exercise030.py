# ========question========
# Exercise 30: Generator Cleanup
#
# Problem Statement: Use a try...finally block within a generator to ensure a resource (like a database connection) is closed even if the generator is closed early.
#
# Purpose: Generators that hold open resources – file handles, network sockets, database cursors – must release them regardless of whether iteration completes normally or is abandoned. This exercise shows how try...finally inside a generator cooperates with the .close() method to guarantee cleanup, mirroring the behaviour of a context manager.
#
# Given Input: A simulated database with rows [("Alice", 30), ("Bob", 25), ("Carol", 35)]. Close the generator after reading only the first row.
#
# Expected Output:
#
# [DB] Connection opened
# Row: ('Alice', 30)
# [DB] Connection closed
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Yield one result at a time while preserving the state needed for the next.


# Write your code below.

