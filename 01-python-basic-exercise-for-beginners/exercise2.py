# ========question========
# Exercise 2. Cumulative Sum of a Range
#
# For each integer from 0 through 9, display it, the preceding integer, and their sum. Start the previous value at 0.
#
# Given Input: Range: numbers = range(10)
#
# Expected Output:
#
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number 0 Sum: 0
# Current Number 1 Previous Number 0 Sum: 1
# Current Number 2 Previous Number 1 Sum: 3
# ....
# Current Number 8 Previous Number 7 Sum: 15
# Current Number 9 Previous Number 8 Sum: 17


# ========hints========
# Keep the previous value between iterations.


# Write your code below.

print("Printing current and previous number sum in a range(10)")

j = 0

for i in range(10):
    sum = j + i     # here j still 0 for first term and i also 0 

    print(f"Current Number {i} Previous Number {j} Sum: {sum}")

    j = i   # here now j become i , in next term j value will be use as input before printing
    