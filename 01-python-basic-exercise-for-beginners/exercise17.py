# ========question========
# Exercise 17. Merging Lists with Parity Filtering
#
# Combine the odd values of the first list with the even values of the second list.
#
# Given Input:
#
# - list1 = [10, 20, 25, 30, 35]
#
# - list2 = [40, 45, 60, 75, 90]
#
# Expected Output: [25, 35, 40, 60, 90]


# ========hints========
# Filter each source list using its own parity rule.


# Write your code below.


list1 = [10, 20, 25, 30, 35]

list2 = [40, 45, 60, 75, 90]

output_list = []  # first and empty list

for num in list1:
    if num % 2 != 0:
        output_list.append(num)  # adding each odd element on empty list
    else:
        None

for num in list2:
    if num % 2 == 0:
        output_list.append(num)  # adding each even element on updated output list


print(output_list)


# #pynative solution================================

# def merge_list(list1, list2):
#     result_list = []

#     # Get odd numbers from list1
#     for num in list1:
#         if num % 2 != 0:
#             result_list.append(num)

#     # Get even numbers from list2
#     for num in list2:
#         if num % 2 == 0:
#             result_list.append(num)

#     return result_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list:", merge_list(list1, list2))
