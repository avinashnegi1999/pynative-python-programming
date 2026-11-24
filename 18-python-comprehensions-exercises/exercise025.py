# ========question========
# Exercise 25: Comprehension vs Generator Benchmark
#
# Problem Statement: Write the same transformation — squaring all even numbers from 1 to 100,000 — as both a list comprehension and a generator expression. Use sys.getsizeof() to compare their memory footprints and timeit.timeit() to measure construction time and full iteration time for each. Print a clear report and explain when each form is preferable.
#
# Purpose: Knowing that generators are more memory-efficient than lists is theoretical until you measure it. This exercise makes both differences concrete with real numbers, and frames the decision not as “generators are always better” but as a trade-off: generators win on memory and initial construction speed, while lists win when you need random access, multiple iterations, or a known length. Understanding this trade-off is essential for writing Python that is both correct and efficient at scale.
#
# Given Input: Even numbers from 1 to 100,000, squared.
#
# Expected Output:
#
# --- Memory ---
# List  size: 434,944 bytes
# Gen   size:     208 bytes
#
# --- Construction time (1000 runs) ---
# List  build: 0.4521s
# Gen   build: 0.0003s
#
# --- Full iteration time (1000 runs) ---
# List  iter:  0.1843s
# Gen   iter:  0.5102s
#
# Source: https://pynative.com/python-comprehensions-exercises/


# ========hints========
# Yield one result at a time while preserving the state needed for the next.


# Write your code below.

