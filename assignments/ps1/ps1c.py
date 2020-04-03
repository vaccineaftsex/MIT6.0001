# -*- coding: utf-8 -*-
"""
MIT 6.0001 ps1 partC
Created on Fri Apr  3 19:11:39 2020

@author: mayux
"""

starting_salary = float(input("Enter the starting salary:"))
semi_annual_raise = .07
r = .04
total_cost = 1e6
portion_down_payment = .25
down_payment = total_cost * portion_down_payment

def best_saving_rate(m, n, step):
    r = .04
    k = (m + n) // 2
    portion_saved = k / 10000
    current_savings = 0.0
    annual_salary = starting_salary
    for current_month in range(1, 37):
        current_savings += current_savings * r / 12
        current_savings += annual_salary/12 * portion_saved
        if current_month % 6 ==0:
            annual_salary += annual_salary * semi_annual_raise

    if abs(current_savings - down_payment) <= 100:
        return (k/10000, step)
    if m + 1 == n:
        return(0 , -1)
        
    if current_savings > down_payment:
        return best_saving_rate(m, k, step+1)
    else:
        return best_saving_rate(k, n, step+1)


saving_rate, step = best_saving_rate(0,10000, step = 1)
if step == -1:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best saving rate:", saving_rate)
    print("Steps in bisection search:", step)