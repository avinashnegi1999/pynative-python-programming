# ========question========
# Exercise 11. Removing Duplicates from a List
#
# Return a new list containing each distinct value from an input list once.
#
# Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]
#
# Expected Output: Unique List: [1, 2, 3, 4, 5]


# ========hints========
# Think about a collection that forbids duplicates; decide whether order matters.


# Write your code below.


data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data = []

for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data)


# data = [1, 2, 2, 3, 4, 4, 4, 5]

# unique_data = []

# for i in range(len(data)):

#     duplicate = False

#     for j in range(len(unique_data)):

#         if data[i] == unique_data[j]:
#             duplicate = True
#             break

#     if duplicate == False:
#         unique_data.append(data[i])

# print(unique_data)


# data = [1, 2, 2, 3, 4, 4, 4, 5]

# # Set conversion removes duplicates automatically
# unique_data = list(set(data))

# print(f"Unique List: {unique_data}")
