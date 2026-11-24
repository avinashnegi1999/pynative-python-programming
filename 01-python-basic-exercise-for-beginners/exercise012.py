# ========question========
# Exercise 12. List Comparison and Boolean Logic
#
# Write a function that returns True when a list's first and final values match; otherwise return False.
#
# Given Input:
#
# - numbers_x = [10, 20, 30, 40, 10]
#
# - numbers_y = [75, 65, 35, 75, 30]
#
# Expected Output:
#
# Given list: [75, 65, 35, 75, 30] | result is False
# Given list: [10, 20, 30, 40, 10] | result is True


# ========hints========
# Compare the two boundary positions.


# Write your code below.


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

first_of_x = numbers_x[0]
length_x = len(numbers_x)
last_of_x = numbers_x[length_x - 1]

first_of_y = numbers_y[0]
length_y = len(numbers_y)
last_of_y = numbers_y[length_y - 1]


def compare(x, y):
    if x == y:  # comparing only first and last index of list
        return True
    else:
        return False


print(compare(first_of_x, last_of_x))
print(compare(first_of_y, last_of_y))


# # pynative solution

# def first_last_same(number_list):
#     print("Given list:", number_list)

#     first_num = number_list[0]
#     last_num = number_list[-1]

#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
