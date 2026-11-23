# ========question========
# Exercise 16. Numerical Palindrome Check
#
# Determine whether an integer reads identically in both directions.
#
# Given Input:
#
# - Case 1: number = 121
#
# - Case 2: number = 125
#
# Expected Output:
#
# Number 125 is not palindrome number
# Number 121 is palindrome number


# ========hints========
# Compare the original digits with their reversed order.


# Write your code below.


num = input("Enter the number here: ")

length = len(num)
is_palindrome = True

for i in range(length // 2):

    # Compare characters from opposite ends of the string
    if num[i] == num[-(i + 1)]:
        continue
    else:
        is_palindrome = False
        break

if is_palindrome:
    print(f"Number {num} is palindrome number")
else:
    print(f"Number {num} is not palindrome number")


## pynative solution ===========================================
# def check_palindrome(number):
#     print("original number", number)
#     # Convert to string to reverse easily
#     original_str = str(number)
#     reversed_str = original_str[::-1]

#     if original_str == reversed_str:
#         print("Yes. given number is palindrome number")
#     else:
#         print("No. given number is not palindrome number")

# check_palindrome(121)
# check_palindrome(125)
