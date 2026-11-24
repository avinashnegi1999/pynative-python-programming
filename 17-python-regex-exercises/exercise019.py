# ========question========
# Exercise 19: Clean IP Addresses
#
# Problem Statement: Write a Python program to remove leading zeros from each segment of an IP address (e.g., convert 192.168.001.001 to 192.168.1.1).
#
# Purpose: This exercise introduces re.sub() with a callable replacement function, a powerful technique that goes beyond simple string substitution. Normalising IP address segments is a practical data-cleaning task encountered in network log processing, configuration file parsing, and input sanitisation pipelines.
#
# Given Input: ip_addresses = ["192.168.001.001", "010.000.000.001", "255.255.255.000", "192.168.1.1"]
#
# Expected Output:
#
# 192.168.001.001 -> 192.168.1.1
# 010.000.000.001 -> 10.0.0.1
# 255.255.255.000 -> 255.255.255.0
# 192.168.1.1     -> 192.168.1.1
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Describe the required text structure first, including anchors, character groups, and repetitions.


# Write your code below.

