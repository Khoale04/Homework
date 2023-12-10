def multiple_of_5(number):
    if int(number) % 5 == 0:
        print("Hello")
    else:
        print("Goodbye")
    return multiple_of_5
#user input
user_number = input("Please enter a number: ")

#validate input
if user_number.isdigit() and int(user_number) > 0:
    number_of_user = multiple_of_5(user_number)
else:
    print("Please, make sure you enter a number")