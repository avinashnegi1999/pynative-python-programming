# ========question========
# Exercise 19. Multi-Tiered Income Tax Calculation
#
# Calculate tax using these fictional brackets: the first 10,000 is untaxed;
# the next 10,000 is taxed at 10%; everything above 20,000 is taxed at 20%.
#
# Given Input: income = 45000
#
# Expected Output: Total income tax to pay is 6000


# ========hints========
# Apply each rate only to the part of income inside its bracket.


# Write your code below.


income = 45000

tax = 0

if income <= 10000:
    income = income

elif income <= 20000:
    tax = income * (10 / 100)
    income = income - tax

else:
    tax = 10000 * (10 / 100) + (income - 20000) * (20 / 100)
    income = income - tax

print(f"total income tax to pay is {tax}, and total income after tax is: {income}")


# pynative solution ============================
# income = 45000
# tax_payable = 0
# print("Given income:", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # Tax on first 10k is 0. Tax on the rest is 10%
#     tax_payable = (income - 10000) * 10 / 100
# else:
#     # First 10,000 (0% tax)
#     # Next 10,000 (10% tax = 1,000)
#     tax_payable = 0 + (10000 * 10 / 100)
#     # Remaining income (20% tax)
#     tax_payable += (income - 20000) * 20 / 100

# print("Total income tax to pay is", tax_payable)
