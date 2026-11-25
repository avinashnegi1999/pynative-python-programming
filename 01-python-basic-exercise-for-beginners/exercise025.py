# ========question========
# Exercise 25. Check Leap Year
#
# Read a year and decide whether it is a leap year. Multiples of 4 qualify, except century years must also be multiples of 400.
#
# Given Input: year = 2024
#
# Expected Output: 2024 is a leap year


# ========hints========
# Check century exceptions as well as the four-year rule.


# Write your code below.


def is_leap(year):
    # Standard Leap Year Logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


is_leap(2024)
is_leap(2100)
