
annual_salary = int(input("Enter the starting salary: "))
semi_annual_raise = .07
invest_rate = .04
portion_down_payment = .25
total_cost = 1000000
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12

#find best rate of savings a.k.a portion_saved within 36 months with errorness is 100
#dollars

def savings(saved,monthly_salary = monthly_salary):
    '''return amount of money after 36 months of savings, given portion_saved'''
    current_savings = 0
    for month in range(36):
        if month % 6 == 0 and month > 0:
            monthly_salary += monthly_salary * semi_annual_raise
        current_savings = current_savings + current_savings * 0.04/12 \
        + monthly_salary * saved
    return int(current_savings)

if savings(saved = 1) < down_payment: #for the case we can pay the down payment within 3years
    print("Can't pay the down payment within 3 years")
else:
    #initialize upper bound and lower bound
    lower_rate = 0
    upper_rate = 1
    #initialize first attempt at the middle
    best_rate = (lower_rate + upper_rate) / 2
    #initialize number of steps
    steps = 0

    #searching the best rate using bisection method
    while down_payment + 100 < savings(saved = best_rate) or \
        down_payment - 100 > savings(saved= best_rate):
        if savings(saved = best_rate) + 100 < down_payment:
            lower_rate = best_rate
            upper_rate = upper_rate
            best_rate = (lower_rate + upper_rate) / 2
        elif savings(saved = best_rate) - 100 > down_payment:
            lower_rate = lower_rate
            upper_rate = best_rate
            best_rate = (lower_rate + upper_rate) / 2
        steps += 1
    print(f"The downpayment is {down_payment}")
    print(f"The savings after 3 years is {savings(best_rate)}")
    print(f"The best rate is : {int(best_rate*1000)/1000} ") #return the best rate with 3 digits
    #after comma.
    print(f"Number of steps: {steps}")




