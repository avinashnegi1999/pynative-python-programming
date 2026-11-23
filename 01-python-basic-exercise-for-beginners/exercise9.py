# ========question========
# Exercise 9. Vowel Frequency Counter
#
# Count vowel occurrences in a sentence, treating uppercase and lowercase alike.
#
# Given Input: sentence = "Learning Python is fun!"
#
# Expected Output: Number of vowels: 6


# ========hints========
# Normalise letter case before testing vowel membership.

# Write your code below.


# =============my own solution using n²=================

sentence = "Learning Python is fun!"

# Convert the entire sentence to lowercase
sentence = sentence.lower()

# Create a list containing all five vowels
vowels = ["a", "e", "i", "o", "u"]

# Initialise counter to track total vowel occurrences
count = 0

# Outer loop: Iterate through each vowel in the vowel list
for i in range(len(vowels)):

    # Inner loop: Iterate through every character in the sentence
    for j in range(len(sentence)):

        # Compare the current vowel with the current sentence character
        if vowels[i] == sentence[j]:

            # If they match, increment the vowel counter by 1
            count += 1

# Display the total number of vowels found
print("Number of vowels:", count)


# ==============most optimical solution==============

# sentence = "Learning Python is fun!"
# vowels = "aeiou"
# count = 0

# # Convert to lowercase to handle 'A' and 'a' equally
# for char in sentence.lower():
#     if char in vowels:
#         count += 1

# print(f"Number of vowels: {count}")
