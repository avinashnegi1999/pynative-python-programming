# ========question========
# Exercise 13. Filtering Lists with Conditional Logic
#
# Display the multiples of 5 found in a supplied list.
#
# Given Input: num_list = [10, 20, 33, 46, 55]
#
# Expected Output:
#
# Divisible by 5:
# 10, 20, 55


# ========hints========
# Divisibility means the remainder is zero.


# Write your code below.

new_list = []

num_list = [10, 20, 33, 46, 55]

for i in range(len(num_list)):
    if num_list[i] % 5 == 0:
        new_list.append(num_list[i])

print("num divisible by 5 is :", new_list)


# # pynative solution
# num_list = [10, 20, 33, 46, 55]
# print("Given list is", num_list)
# print("Divisible by 5:")

# # Iterate through each element
# for num in num_list:
#     # Check divisibility
#     if num % 5 == 0:
#         print(num)
