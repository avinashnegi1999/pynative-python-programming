# ========question========
# Exercise 31. Print Alternate Prime Numbers
#
# Find primes up to 20 and display alternate entries, starting with the first prime: 2, 5, 11, 17.
#
# Given Input: Limit = 20
#
# Expected Output: 2, 5, 11, 17


# ========hints========
# First identify the primes, then take alternate positions.


# Write your code below.

for i in range(2, 21):

    is_prime = True  # here we make is_prime ture

    for j in range(2, i):

        if i % j == 0:
            is_prime = False
            # here is_prime get false if it divide between 1 and i even once
            # it will break the loop
            break

    if is_prime:  # here if any number which was not false get printed only one time
        print(i, end=", ")


# #pynatie solution =============================
# primes = []

# for num in range(2, 21):
#     # Check if number is prime
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)

# # Print alternate primes
# alternate_primes = primes[::2]
# print(alternate_primes)
