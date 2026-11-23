# ========question========
# Exercise 15. Nested Loops for Pattern Generation
#
# Print five rows: row n contains the number n repeated n times.
#
# Given Input: Range: 1 to 5
#
# Expected Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# ========hints========
# Separate the row number from the number of repetitions.


# Write your code below.


# Outer loop for rows
for num in range(1, 6):
    # Inner loop for repetition
    for i in range(num):
        print(num, end=" ")  # end=" " keeps it on the same line
    # New line after each row
    print("\n")
