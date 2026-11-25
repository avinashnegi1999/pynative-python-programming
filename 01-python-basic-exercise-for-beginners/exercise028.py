# ========question========
# Exercise 28. Odd/Even List Splitter
#
# Start with 10 integers. Loop through them, separating them into one list of even values and another of odd values.
#
# Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
#
# Expected Output:
#
# Even numbers: [12, 34, 10, 8, 2]
# Odd numbers: [7, 21, 5, 3, 19]


# ========hints========
# Use the remainder after division by two.


# Write your code below.


odd_list = []
even_list = []

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])

    else:
        odd_list.append(numbers[i])


print(even_list)
print(odd_list)


# # pynative solution ====================================================
# numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# evens = []
# odds = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)

# print(f"Even numbers: {evens}")
# print(f"Odd numbers: {odds}")
