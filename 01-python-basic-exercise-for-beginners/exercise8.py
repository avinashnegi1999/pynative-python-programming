# ========question========
# Exercise 8. String Reversal
#
# Produce a reversed version of a supplied string.
#
# Given Input: text = "Python"
#
# Expected Output: Reversed: nohtyP


# ========hints========
# Think about traversing a sequence backwards.


# Write your code below.

text = "Python"

l = len(text)
reverse = ""

for i in range(l - 1, -1, -1):
    # Start from the last character (l - 1), go backwards by 1,
    # and stop at -1 (excluding -1), so index 0 is also included.
    reverse += text[i]

print(reverse)
