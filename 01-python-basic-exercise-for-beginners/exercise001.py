# ========question========
#Exercise 1. Arithmetic Product and Conditional Logic


#Write a Python function that accepts two integer numbers
# If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.



# Given Input:
# - Case 1: number1 = 20, number2 = 30
# - Case 2: number1 = 40, number2 = 30
#
# Expected Output:
# - The result is 600
# - The result is 70


# ========hints========
# Work out the product before choosing the return value.


def multiplication_or_sum(num1, num2):
    # Calculate product
    product = num1 * num2
    
    # Check if product is within the threshold
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Testing Case 1
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Testing Case 2
result = multiplication_or_sum(40, 30)
print("The result is", result)