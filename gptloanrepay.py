# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:38:21 2023

@author: Alex Nolan
"""


def calculate_monthly_repayment(PV, r, n):
    # Convert annual percentage rate (APR) to monthly interest rate
    monthly_interest_rate = r / (12 * 100)
    
    # Calculate the denominator term (1 - (1 + r)^-n)
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    
    # Calculate the monthly repayment amount using the formula
    Pmt = monthly_interest_rate * PV / denominator
    
    return Pmt

# Input values
PV = 12000
r = 7.45
n = 48

# Call the function and print the result
monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount: $", round(monthly_repayment, 2))

"""
 The monthly repayment amount in this case is
 Approximately $289.87
 """
 