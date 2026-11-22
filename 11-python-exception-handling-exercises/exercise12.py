# ========question========
# Exercise 12: Custom Exception Class
#
# Problem Statement: Define a custom exception class InsufficientFundsError. Then create a BankAccount class with a withdraw(amount) method that raises InsufficientFundsError when the withdrawal amount exceeds the current balance. Handle the exception in the calling code.
#
# Purpose: Built-in exceptions are generic. Custom exceptions make your code self-documenting and allow callers to catch exactly the error your library or class can produce, without accidentally catching unrelated errors of the same built-in type. This pattern is standard in professional Python packages and frameworks.
#
# Given Input: Create a BankAccount with a balance of 100. Try to withdraw 150.
#
# Expected Output:
#
# Error: Cannot withdraw 150. Available balance: 100.
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

