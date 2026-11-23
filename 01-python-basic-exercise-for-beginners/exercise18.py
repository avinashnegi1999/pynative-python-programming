# ========question========
# Exercise 18. Integer Digit Extraction and Reversal
#
# Display an integer's digits from right to left, separated by spaces. Practise extracting digits arithmetically.
#
# Given Input: number = 7536
#
# Expected Output: 6 3 5 7


# ========hints========
# Base 10 arithmetic can isolate and remove the last digit.


# Write your code below.


numbers = 7536

output_number = ""

# Solving using arithmetic operations and recursion.


def isolate(x):
    global output_number  # Access the global output_number variable.

    if x == 0:  # Base case: stop recursion when no digits remain.
        return

    num = x % 10  # Modulo (%) extracts the last digit. Example: 7536 % 10 = 6.

    num_2 = (
        x // 10
    )  # Floor division (//) removes the last digit. Example: 7536 // 10 = 753.

    output_number += str(
        num
    )  # Convert the extracted digit into a string and append it.

    isolate(num_2)  # Recursive call with the remaining number.


isolate(numbers)  # Initial function call.

print(output_number)  # Display the extracted digits.


# # pynative solution ======================================

# number = 7536
# print("Given Number:", number)

# while number > 0:
#     # Get the last digit
#     digit = number % 10

#     # Remove the last digit from number
#     number = number // 10

#     print(digit, end=" ")
