def divisible_7(number):
    if number//7:
        print("this number is divisible by 7")
    else:
        print("this number is not divisible by 7")

user_number = int(input("please input a number"))
divisible_7(user_number)