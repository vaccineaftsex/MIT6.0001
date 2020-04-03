# -*- coding: utf-8 -*-
"""
MIT 6.0001 ps1 partA
Created on Fri Apr  3 19:11:39 2020

@author: mayux
"""

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = .25
down_payment = total_cost * portion_down_payment
current_savings = 0.0
current_month = 0
r = .04

while current_savings < down_payment:
    current_month += 1
    current_savings += current_savings * r / 12
    current_savings += annual_salary/12 * portion_saved
    
print("Number of months:", current_month)