#Write a program to calculate how many months it will take you to save up enough money for a down payment.
#You will want your main variables to be floats, so you should cast user inputs to floats.
#Your program should ask the user to enter the following variables:
#1. The starting annual salary (annual_salary)
#2. The portion of salary to be saved (portion_saved)
#3. The cost of your dream home (total_cost)


current_savings = 0
r = 0.04
months = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

while current_savings < portion_down_payment:
    current_savings += annual_salary / 12 * portion_saved + current_savings * r /12
    months += 1
print(months)
