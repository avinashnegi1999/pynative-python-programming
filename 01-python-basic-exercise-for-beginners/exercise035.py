# ========question========
# Exercise 35. Digit Detection in Strings
#
# Examine a user-supplied string character by character with a for loop; report whether any character is a digit.
#
# Given Input: input_string = "Python3"
#
# Expected Output: The string 'Python3' contains digits: True


# ========hints========
# A string character has a method for checking whether it is a digit.


# Write your code below.


input_string = "Python3"

contains_digit = False  # first we make it flase

for i in range(len(input_string)):

    if input_string[i] in "0123456789":
        # if any index value matches any number it will return true
        # and break so no more loop, otherwise it will remain false
        contains_digit = True
        break

print(f"The string '{input_string}' contains digits: {contains_digit}")


# #pynative solution ========================================================
# input_string = "Python3"

# contains_digit = False

# for i in range(len(input_string)):

#     if input_string[i].isdigit():
#         contains_digit = True
#         break

# print(f"The string '{input_string}' contains digits: {contains_digit}")
