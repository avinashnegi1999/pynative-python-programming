# ========question========
# Exercise 18: Retry Decorator
#
# Problem Statement: Write a @retry(times=3) decorator factory that re-runs the decorated function up to times attempts if it raises an exception. If all attempts fail, re-raise the last exception. Demonstrate it on a function that fails twice and succeeds on the third call.
#
# Purpose: Transient failures – network timeouts, temporary service unavailability, rate-limit responses – are a fact of life in distributed systems. A retry decorator is one of the most reused tools in a Python developer’s toolkit. Building it from scratch cements understanding of decorators, closures, and exception handling all at once.
#
# Given Input: A function flaky_call() that fails on the first two calls and succeeds on the third.
#
# Expected Output:
#
# Attempt 1 failed: temporary failure
# Attempt 2 failed: temporary failure
# Attempt 3 succeeded.
# Result: success
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Wrap the original callable while preserving its arguments and return value.


# Write your code below.

