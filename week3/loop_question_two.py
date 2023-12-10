def calculate_number(n):
    previous_number = 1
    for calculate_number in range(1, n+1, 1):
        if calculate_number == 1:
            print(calculate_number, end = " ")
        else:
            print("+", calculate_number, end = " ")
    return calculate_number

#user input
number_customer = input("Please input a number: ")
#validate input
if number_customer.isdigit():
    number_of_customer = calculate_number(int(number_customer))

    print()
    print("Total is ")
else:
    print("Please, make sure you enter a number")
