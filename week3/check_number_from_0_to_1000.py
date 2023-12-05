def check_number(number):
    if number < 1000 and number > 0:
        print(number, "is greater than 0 and lower than 1000")
    else:
        print("not legit number")


number_of_user = float(input("please input number"))

check_number(number_of_user)