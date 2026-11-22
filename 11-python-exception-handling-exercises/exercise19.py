# ========question========
# Exercise 19: Thread-Safe Exception Handling
#
# Problem Statement: Launch five threads that each perform a division. Some will raise a ZeroDivisionError. Catch exceptions inside each thread and store them in a shared list protected by a threading.Lock. After all threads complete, iterate the list and report all failures.
#
# Purpose: Exceptions raised in a thread do not propagate to the main thread automatically – they simply terminate the thread silently unless you handle them explicitly. This exercise teaches the correct pattern for capturing and surfacing thread-level errors in concurrent Python programs.
#
# Given Input: Five threads dividing 10 by the values [2, 0, 5, 0, 1].
#
# Expected Output:
#
# Thread-1: 10 / 2 = 5.0
# Thread-3: 10 / 5 = 2.0
# Thread-5: 10 / 1 = 10.0
#
# Errors collected:
# Thread-2: division by zero
# Thread-4: division by zero
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

