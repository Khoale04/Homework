def calculate_number(n):
    previous_total = 0
    total = 0
    for current_number in range(1, n+1, 1):
            total = previous_total + current_number
            previous_total = total
            print(total)
    return total




calculate_number(3)

# #user input
# number_customer = input("Please input a number: ")
# #validate input
# if number_customer.isdigit():
#     number_of_customer = calculate_number(int(number_customer))
#     print()
#     print("Total is ")
# else:
#     print("Please, make sure you enter a number")
