# ========question========
# Exercise 24. Generate Fibonacci Series
#
# Display 15 Fibonacci terms, beginning with 0 and 1; each later term adds the preceding two.
#
# Given Input: Terms = 15
#
# Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


# ========hints========
# Keep track of two neighbouring terms.


# Write your code below.


first_number = 0
second_number = 1
next_number = 0

for i in range(15):
    print(first_number, end=" ")

    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number


# #pynative solution==================
# num1, num2 = 0, 1
# print("Fibonacci series:")

# for i in range(15):
#     print(num1, end="  ")
#     # Calculate next term
#     res = num1 + num2
#     # Update values for next iteration
#     num1 = num2
#     num2 = res
