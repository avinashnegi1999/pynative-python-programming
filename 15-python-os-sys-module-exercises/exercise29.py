# ========question========
# Exercise 29: Environment Config Loader
#
# Problem Statement: Write a Python program that simulates loading application configuration by reading multiple environment variables with fallback defaults, then prints a formatted summary of the configuration to standard output.
#
# Purpose: Reading configuration from environment variables is the industry-standard approach for twelve-factor applications. It keeps secrets and environment-specific settings out of source code. This exercise combines os.environ.get() with sys.stdout to build a realistic config-loading pattern used in web apps, APIs, and CLI tools.
#
# Given Input: Environment variables APP_HOST, APP_PORT, and APP_DEBUG – set within the script to simulate a configured environment.
#
# Expected Output: A formatted configuration summary printed to stdout showing each key and its resolved value.
#
# Source: https://pynative.com/python-os-sys-module-exercises/


# ========hints========
# Identify the relevant filesystem or process operation and handle paths carefully.


# Write your code below.

