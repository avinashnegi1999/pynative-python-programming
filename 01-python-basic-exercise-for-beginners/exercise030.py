# ========question========
# Exercise 30. Word Frequency Counter (The Histogram)
#
# Build a dictionary mapping each word in a paragraph to its occurrence count.
#
# Given Input: text = "apple banana apple cherry banana apple"
#
# Expected Output: {'apple': 3, 'banana': 2, 'cherry': 1}


# ========hints========
# Keep one counter per distinct word.


# Write your code below.


# Original paragraph
text = "apple banana apple cherry banana apple"

# Split the paragraph into individual words
new_text = text.split()

# Create an empty dictionary to store word frequencies
dect1 = {}

# Loop through each word in the list
for i in new_text:

    # Reset counter for each new word
    count = 0

    # Compare the current word with every word in the list
    for j in new_text:

        # If both words match, increase the counter
        if i == j:
            count += 1

    # Store the word and its total occurrence count
    dect1[i] = count

# Display the final dictionary
print(dect1)


# # pynative solution ===============================
# text = "apple banana apple cherry banana apple"
# words = text.split()
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)
