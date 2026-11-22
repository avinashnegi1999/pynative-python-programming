# ========question========
# Exercise 28: Recursive Directory Walker
#
# Problem Statement: Write a generator that yields all file paths in a directory and its subdirectories using yield from.
#
# Purpose: Recursive directory traversal is one of the most common real-world applications of recursive generators. Using yield from keeps the code concise while avoiding the need to accumulate paths in a list, making it suitable for very large directory trees.
#
# Given Input: A temporary directory tree created at runtime:
#
# test_dir/
#     file1.txt
#     file2.txt
#     subdir/
#         file3.txt
#         file4.txt
#
# Expected Output:
#
# test_dir/file1.txt
# test_dir/file2.txt
# test_dir/subdir/file3.txt
# test_dir/subdir/file4.txt
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Define the smallest case first, then reduce larger inputs toward it.


# Write your code below.

