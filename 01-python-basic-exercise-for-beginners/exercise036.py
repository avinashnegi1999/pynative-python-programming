# ========question========
# Exercise 36. Capitalize First Letter (Title Case)
#
# Uppercase the first letter of every word in a string without calling title().
#
# Given Input: text = "hello world from python"
#
# Expected Output: Hello World From Python


# ========hints========
# Break the sentence into words, transform each, then reassemble it.


# Write your code below.


text = "hello world from python"

new_text = text.split()  # Split the sentence into a list of individual words

new_sentance = ""

for word in new_text:
    new_sentance += word.capitalize()  # Capitalize the first letter of each word
    new_sentance += " "  # Add a space after each word

print(new_sentance.strip())  # Remove leading and trailing whitespace


# # pynative solution
# text = "hello world from python"

# # Split the string into a list of words
# words = text.split()
# capitalized_words = []

# for word in words:
#     # Capitalize each word and add to the new list
#     capitalized_words.append(word.capitalize())

# # Join the list back into a single string
# result = " ".join(capitalized_words)
# print(result)
