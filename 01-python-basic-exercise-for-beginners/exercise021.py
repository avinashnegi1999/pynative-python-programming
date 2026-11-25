# ========question========
# Exercise 21. Downward Half-Pyramid Pattern
#
# Draw five rows of stars, decreasing from five stars in the first row to one in the last.
#
# Given Input: Rows: 5
#
# Expected Output:
#
# * * * * *
# * * * *
# * * *
# * *
# *


# ========hints========
# The number of stars falls by one on each row.


# Write your code below.


for i in range(5):

    for j in range(5 - i):
        print("*", end="\t")

    print()


# # pynative solution
# # Loop from 5 down to 1
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*", end=" ")
#     print("\n")
