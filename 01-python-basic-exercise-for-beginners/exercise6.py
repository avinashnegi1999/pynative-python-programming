# ========question========
# Exercise 6. Calculating Factorial with a Loop
#
# Calculate the factorial of a supplied number with a for loop.
#
# Given Input: number = 5
#
# Expected Output: The factorial of 5 is 120


# ========hints========
# Choose an initial running product that does not change a multiplication.


# Write your code below.


num = 10

fact = 1
for i in range(1, 11):

    fact = i * fact

print(fact)
