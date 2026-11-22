# ========question========
# Exercise 19: Cached Combination Counter
#
# Problem Statement: Write a Python program that implements a recursive combination function based on Pascal’s triangle identity using functools.lru_cache() for memoisation, then compares its results and call counts against math.comb() and the uncached recursive version.
#
# Purpose: Pascal’s triangle recurrence is a classic dynamic programming problem that demonstrates the synergy between recursion and memoisation. Building it from scratch reinforces understanding of how lru_cache() eliminates overlapping subproblem recomputation and why memoised recursion and bottom-up dynamic programming produce identical results.
#
# Given Input: Compute comb(10, 3), comb(15, 6), and comb(20, 10).
#
# Expected Output: Cached results matching math.comb(), with cache statistics showing the dramatic reduction in recursive calls.
#
# Source: https://pynative.com/python-itertools-functools-exercises/


# ========hints========
# Keep a counter and update it only when the required condition holds.


# Write your code below.

