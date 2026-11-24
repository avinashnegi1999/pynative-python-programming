# ========question========
# Exercise 4. String Slicing and Substring Removal
#
# Make a function that returns the part of a string left after removing its first n characters.
#
# Given Input:
#
# - remove_chars("pynative", 4)
#
# - remove_chars("pynative", 2)
#
# Expected Output:
#
# - tive
#
# - native


# ========hints========
# Consider where the retained substring begins.


# Write your code below.


def remove_chars(name, a):

    string = ""

    for i in range(a, len(name)):
        string += name[i]

    print(string)


remove_chars("pynative", 4)
remove_chars("pynative", 2)
