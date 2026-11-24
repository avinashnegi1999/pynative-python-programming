# ========question========
# Exercise 3. String Indexing and Even Slicing
#
# Display the characters at positions 0, 2, 4, and so on in a string.
#
# Given Input: String: "pynative"
#
# Expected Output:
#
# Original String is  pynative
# Printing only even index chars
# p
# n
# t
# v


# ========hints========
# String positions begin at zero; think about a step size.


# Write your code below.


name = "pynative"

for i in range(0, len(name), 2):
    print(name[i])


# Original String
## name = "pynative"

## Print characters at even indexes
# print(name[::2])
