#In ​ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following:
#1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage)
#2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h month, the 18​th​ month, and so on.


current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = total_cost * 0.25

while current_savings < portion_down_payment:
    current_savings += annual_salary / 12 * portion_saved + current_savings * r /12
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print(months)
