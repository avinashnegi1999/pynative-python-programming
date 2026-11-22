# ========question========
# Exercise 5. Variable Swapping (The In-Place Method)
#
# Exchange the values of a and b without introducing a temporary variable.
#
# Given Input: a = 5, b = 10
#
# Expected Output:
#
# Before Swap: a = 5, b = 10
# After Swap: a = 10, b = 5


# ========hints========
# Python supports simultaneous assignment.


# Write your code below.


a = 13
b = 17


a = a + b  # 50+22= 72

b = a - b  # 72-22= 50

a = a - b  # 72- 50= 22


print(f"the value of a:{a}, and the vlue of b : {b} ")
