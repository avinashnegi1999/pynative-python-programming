# ========question========
# Exercise 13: Exception Chaining
#
# Problem Statement: Write a function load_config(filename) that reads a JSON config file. If the file is missing, catch the FileNotFoundError and raise a higher-level ConfigurationError using raise ConfigurationError(...) from original_exception to preserve the original cause in the chain.
#
# Purpose: Exception chaining lets you translate low-level technical errors into meaningful domain-level errors without discarding the debugging context. A caller that receives a ConfigurationError knows exactly what went wrong in business terms, while the full original traceback is still accessible via __cause__ for developers who need it.
#
# Given Input: Call load_config("config.json") when the file does not exist.
#
# Expected Output:
#
# ConfigurationError: Could not load config file 'config.json'.
# Caused by: [Errno 2] No such file or directory: 'config.json'
#
# Source: https://pynative.com/python-exception-handling-exercises/


# ========hints========
# Identify the operation that can fail and handle the specific expected error.


# Write your code below.

