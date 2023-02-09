annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0 #current savings starts at 0
monthly_salary = annual_salary/12
invest_rate = 0.04 #at the end of each month, you receive
                   # an additional ​current_savings*r/12

#initialize month
month = 0
while current_savings < down_payment:
    current_savings = current_savings + current_savings * 0.04/12 \
        + monthly_salary * portion_saved
    month += 1
print(f"Number of months :{month}")
    