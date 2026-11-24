# ========question========
# Exercise 10. Finding Extremes (Min/Max) in a List
#
# Report the smallest and largest integers in a list.
#
# Given Input: nums = [45, 2, 89, 12, 7]
#
# Expected Output: Largest: 89 Smallest: 2


# ========hints========
# Python has built-ins for finding extreme values.


# Write your code below.


# Create a list of numbers
nums = [45, 2, 89, 12, 7]

# Initialise minimum and maximum with the first element of the list
minimum = nums[0]
maximum = nums[0]


# Function to find the minimum number
def find_min(x):

    # Access the global minimum variable
    global minimum

    # Check if the current element is smaller than or equal to minimum
    if minimum >= nums[x]:

        # Update minimum with the current element
        minimum = nums[x]


# Function to find the maximum number
def find_max(x):

    # Access the global maximum variable
    global maximum

    # Check if the current element is greater than or equal to maximum
    if maximum <= nums[x]:

        # Update maximum with the current element
        maximum = nums[x]


# Iterate through every index of the list
for i in range(len(nums)):

    # Call find_min() with the current index
    find_min(i)

    # Call find_max() with the current index
    find_max(i)


# Display the final minimum and maximum values
print("Minimum:", minimum)
print("Maximum:", maximum)


# ===============easiest approach=======================
# nums = [45, 2, 89, 12, 7]

# largest = max(nums)
# smallest = min(nums)

# print(f"Largest: {largest}")
# print(f"Smallest: {smallest}")
