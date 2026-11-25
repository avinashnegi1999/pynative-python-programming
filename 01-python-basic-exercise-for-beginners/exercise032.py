# ========question========
# Exercise 32. Dictionary of Squares (Mapping Logic)
#
# Map every integer from 1 through 10 to its square in a dictionary.
#
# Given Input: Range: 1 to 10
#
# Expected Output:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# ========hints========
# Each dictionary entry associates a number with its square.


# Write your code below.


dict_square = {}

for i in range(1, 11):
    square = i * i  # value of key

    dict_square[i] = square

print(dict_square)
