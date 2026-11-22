# ========question========
# Exercise 16: Prime Sieve
#
# Problem Statement: Implement a generator that yields prime numbers using the Sieve of Eratosthenes logic.
#
# Purpose: This exercise shows how a classical algorithm can be expressed as a lazy generator. The sieve approach is significantly more efficient than trial division for finding all primes up to a limit, and mapping it to a generator makes the result easy to consume incrementally.
#
# Given Input: limit = 30
#
# Expected Output: 2 3 5 7 11 13 17 19 23 29
#
# Source: https://pynative.com/python-iterators-generators-exercises/


# ========hints========
# Check possible divisors; one exact divisor is enough to reject a candidate.


# Write your code below.

