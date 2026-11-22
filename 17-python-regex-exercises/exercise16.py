# ========question========
# Exercise 16: Validate Alphanumeric ID
#
# Problem Statement: Write a Python program to match a string that contains only uppercase letters, lowercase letters, numbers, and underscores, with no spaces or special characters allowed.
#
# Purpose: This exercise practises building strict allowlist patterns for input validation. Alphanumeric-plus-underscore strings are the standard format for identifiers in most programming languages, database column names, and API keys. Being able to validate this format reliably is a foundational defensive-programming skill.
#
# Given Input: test_strings = ["user_123", "User_Name", "invalid id", "bad-char!", "_leadingUnderscore", "ALL_CAPS_99"]
#
# Expected Output:
#
# user_123           -> Valid
# User_Name          -> Valid
# invalid id         -> Invalid
# bad-char!          -> Invalid
# _leadingUnderscore -> Valid
# ALL_CAPS_99        -> Valid
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Separate parsing a date from formatting or doing arithmetic with it.


# Write your code below.

