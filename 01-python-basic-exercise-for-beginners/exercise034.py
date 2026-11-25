# ========question========
# Exercise 34. Print Reverse Number Pattern
#
# Print descending number rows: first 5 through 1, then 4 through 1, continuing down to a single 1.
#
# Given Input: Rows = 5
#
# Expected Output:
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# ========hints========
# Both the starting value per row and the values within a row decrease.


# Write your code below.


for i in range(5, 0, -1):
    num = i

    for j in range(i):
        print(num, end=" ")

        num = num - 1

    print()
