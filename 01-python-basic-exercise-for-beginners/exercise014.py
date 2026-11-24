# ========question========
# Exercise 14. Substring Frequency Analysis
#
# Count occurrences of the substring Emma in a supplied sentence.
#
# Given Input:
#
# - str_x = "Emma is good developer. Emma is a writer"
#
# Expected Output: Emma appeared 2 times


# ========hints========
# Look for a string method that counts substrings.


# Write your code below.


# Exercise 14: Count occurrences of a word in a sentence

text = "Emma is good developer. Emma is a writer"
target = "Emma"

count = 0  # Keeps track of how many times the target word appears

# split() is a string method that separates a sentence into individual words.
# It returns a list of words, using whitespace (spaces, tabs, etc.) as separators.
words = text.split()

# Direct iteration: Loop through each word in the list, one at a time.
for word in words:

    # Compare the current word with the target word.
    # == checks whether both strings contain exactly the same text.
    if word == target:

        # If they match, increase the counter by 1.
        count += 1

# Display the total number of matches.
print(f"Emma appeared {count} times")


# # Pynative solution ==================

# str_x = "Emma is good developer. Emma is a writer"
# count = str_x.count("Emma")
# print(f"Emma appeared {count} times")
