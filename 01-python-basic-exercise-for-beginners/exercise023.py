# ========question========
# Exercise 23. Check Palindrome Number
#
# Test an integer for palindrome symmetry again. Try mathematical digit reversal as an alternative to exercise 16.
#
# Given Input: number = 121
#
# Expected Output:
#
# Original number 121
# Yes. given number is palindrome number


# ========hints========
# Preserve the original number before working through its digits.


# Write your code below.


number = 121

original_number = number

number_str = str(number)

compare_number = ""
for i in range(len(number_str)):
    # here reminder of number getting added as a string to empty string
    compare_number += str(number % 10)
    number = number // 10  # here we getting rest of number

print(f" the compare number is {compare_number}")


if int(compare_number) == int(original_number):
    print("yes, given number is palindrome number ")

else:
    print(" it is not")


# # pynative solution=====================
# def check_palindrome(number):
#     # Convert to string to easily reverse
#     str_num = str(number)
#     reverse_str = str_num[::-1]

#     if str_num == reverse_str:
#         print(f"Original number {number}")
#         print("Yes. given number is palindrome number")
#     else:
#         print(f"Original number {number}")
#         print("No. given number is not palindrome number")

# check_palindrome(121)
