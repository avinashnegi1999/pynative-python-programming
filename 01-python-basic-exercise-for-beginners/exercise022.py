# ========question========
# Exercise 22. Custom Exponentiation Function
#
# Implement exponent(base, exp) using repeated multiplication; return the calculated power as an integer.
#
# Given Input: base = 2, exp = 5
#
# Expected Output: 2 raises to the power of 5: 32


# ========hints========
# Maintain a running product; consider an exponent of zero.


# Write your code below.


base = 2
exp = 5


def expo(a, b):
    result = 1

    for _ in range(b):
        result = result * a

    print(result)


expo(2, 5)
expo(8, 9)


# #pynaive solution
# def exponent(base, exp):
#     num = exp
#     result = 1
#     # Repeat multiplication 'exp' times
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is:", result)

# exponent(2, 5)
# exponent(5, 4)
