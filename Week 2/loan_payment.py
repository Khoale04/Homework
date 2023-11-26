#ask user input information
str_loan_amount = input ("Please insert your initial amount of loan: ")
loan = int(str_loan_amount)

str_interest_rate = input ("Please insert the interest: ")
interest = float(str_interest_rate)/100/12

str_duration = input("Please insert your choice of payment's duration (by month) ")
duration = int(str_duration)

#formular and calculation
monthly_amount_of_money = (loan * (interest * (1 + interest)**duration)) / (((1 + interest)**duration) - 1)
monthly_payment = "Your amount of monthly payment is " + str(monthly_amount_of_money)
print(monthly_payment)

total_amount_of_money = monthly_amount_of_money * 180
total_payment = "The total you have to pay is " + str(total_amount_of_money)
print(total_payment)


