def number(n):
    for number in range(1,11,1):
        print(number, end='\n')
    return number

#user input
user_number = input("Please input a number: ")

#validate input
if user_number.isdigit():
    number_of_user = number(user_number)
else:
    print("Please, make sure you enter a number")

# range(start, stop, step)