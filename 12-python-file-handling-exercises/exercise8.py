# ========question========
# Exercise 8: Check If File Exists
#
# Problem Statement: Write a Python program that checks whether a file called data.txt exists in the current directory and prints an appropriate message based on the result.
#
# Purpose: This exercise introduces the os.path module (or the modern pathlib alternative) for checking file existence before performing operations on it. This is a defensive programming practice that prevents crashes caused by attempting to open files that do not exist.
#
# Given Input: The filename data.txt is hardcoded. The file may or may not be present.
#
# Expected Output: File exists. if the file is present, or File does not exist. if it is not.
#
# Source: https://pynative.com/python-file-handling-exercises/


# ========hints========
# Use a file context manager and choose the mode carefully; writing can replace existing contents.


# Write your code below.

