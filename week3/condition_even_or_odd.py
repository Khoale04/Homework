def even_or_odd(number):
    if int(number) % 2 == 0 and int(number) > 0:
        print("it is an even number")
    else:
        print("it is an odd")
    return even_or_odd

#input customer
user_number = input("please input a number: ")

#validate input
if user_number.isdigit() and int(user_number) > 0:
    number_of_user = even_or_odd(user_number)
else:
    print("Please make sure you enter a number")


