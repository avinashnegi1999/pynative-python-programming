# ========question========
# Exercise 25: namedtuple with Default Values
#
# Problem Statement: Write a Python program that defines a Config namedtuple using the defaults parameter so that some fields have fallback values and can be omitted at instantiation, then creates instances with and without the optional fields.
#
# Purpose: Default values make namedtuples practical for configuration objects, optional record fields, and function return types where some fields may not always be populated. This feature was added in Python 3.6.1 and removes the need to subclass or use __new__ tricks to achieve optional fields.
#
# Given Input: A Config namedtuple with required fields host and port, and optional fields debug (default False), timeout (default 30), and max_retries (default 3).
#
# Expected Output: A fully specified config and a minimal config printed side by side, showing default values filling in the omitted fields.
#
# Source: https://pynative.com/python-collections-module-exercises/


# ========hints========
# Choose the collection whose built-in behavior matches the operation.


# Write your code below.

