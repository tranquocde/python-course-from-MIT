annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise: "))
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0 #current savings starts at 0

invest_rate = 0.04 #at the end of each month, you receive
                   # an additional ​current_savings*r/12
monthly_salary = annual_salary/12
#initialize month
month = 0
while current_savings < down_payment:
    if month % 6 == 0 and month >0 : #raise the annual salary after each 6 months
        monthly_salary += monthly_salary * semi_annual_raise
    
    current_savings = current_savings + current_savings * 0.04/12 \
        + monthly_salary * portion_saved
    month += 1

print(f"Number of months :{month}")

