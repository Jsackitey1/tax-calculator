"""
A  program to claculate the tax amount owed based on income
and the number of dependants

@author: Sackitey Joseph

"""

#Declare the variables needed for the calculations and set the initial amounts

income = 1000000

rate = 0.3
currency= "$"

## let the tax benefit for each dependant be 5000 dollars

dependants= 2

benefit = 5000

# Total deductions due to dependants


deductions= dependants*benefit


#Finding the taxable income

Taxable_income = income- deductions

Tax_owed= Taxable_income * rate

print(f"For an income of ${income:,.2f} with {dependants} dependants:")
print(f"Taxable income: {currency}{Taxable_income:,.2f}")
print(f"Tax owed: {currency}{Tax_owed:,.2f}")



