def divisible_7(number):
    if int(number) % 7 == 0 and int(number) > 0:
        print("this number is divisible by 7")
    else:
        print("This number is not divisible by 7")
    return divisible_7
#user input
user_number = input("Please input a number: ")

#validate input
if user_number.isdigit():
    user_of_number = divisible_7(user_number)
else:
    print("Please input a number")




